import requests
from datetime import datetime, timedelta

NEWS_API_KEY='e9ab7edf931141c789b87603727dc276'
MISTRAL_API_KEY='w6efAwRcK4C1imCpVLsJDxH2jDQaL8GK'
TOPIC = "футбол"

def get_news_from_newsapi(api_key, topic):
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    url = "https://newsapi.org/v2/everything"
    params = {
        'q': topic,
        'from': yesterday,
        'language': 'ru',
        'apiKey': api_key,
        'pageSize': 10
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        articles = response.json().get('articles', [])
        return articles
    else:
        print(f"Ошибка NewsAPI: {response.status_code}")
        return []

def create_prompt_from_news(articles, topic):
    if not articles:
        return f"Ты аналитик новостей. Напиши аналитическую аннотацию (250-300 слов) о событиях по теме '{topic}' за последний день. Пиши на русском языке."

    news_text = ""
    for i, article in enumerate(articles[:10], 1):
        title = article.get('title', 'Без заголовка')
        description = article.get('description', '')
        if description:
            news_text += f"{i}. {title}\n   {description}\n\n"

    prompt = f"""Ты аналитик новостей. Проанализируй эти статьи по теме "{topic}" и напиши аннотацию (250-300 слов).

СТАТЬИ:
{news_text}
Напиши аналитическую аннотацию о том, что произошло за последний день. Включи ключевые события, тренды и оценку ситуации. Пиши на русском языке."""
    return prompt

def get_mistral_annotation(api_key, prompt):

    url = "https://api.mistral.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistral-large-latest",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 1000
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        annotation = result['choices'][0]['message']['content']

        with open("text", "w", encoding="utf-8") as f:
            f.write(annotation)
        print("\n" + annotation)
        return annotation
    else:
        print(f"Ошибка Mistral: {response.status_code}")
        print(response.text)
        return None


def main():
    print("Получаем новости из NewsAPI...")
    articles = get_news_from_newsapi(NEWS_API_KEY, TOPIC)
    print(f"Найдено статей: {len(articles)}")


    prompt = create_prompt_from_news(articles, TOPIC)


    print("\nОтправляем запрос в Mistral AI...")
    get_mistral_annotation(MISTRAL_API_KEY, prompt)

if __name__ == "__main__":
    main()