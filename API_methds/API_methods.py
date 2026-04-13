
import requests as r


BASE_URL = "https://newsapi.org/v2"


def fetch_news(endpoint: str, api_key: str, params: dict) -> dict:
    """
    Получение новостей с NewsAPI
    """
    final_params = {k: v for k, v in params.items() if v is not None}
    return _make_request(endpoint, api_key, final_params)


def _make_request(endpoint: str, api_key: str, params: dict = None) -> dict:
    url = f"{BASE_URL}/{endpoint}"
    default_params = {"apiKey": api_key}

    if params:
        default_params.update(params)

    try:
        response = r.get(url, params=default_params, timeout=10)
        return response.json()
    except r.exceptions.RequestException as e:
        raise Exception(f"Ошибка запроса к NewsAPI: {e}")
    except ValueError:
        raise Exception("Ошибка обработки JSON ответа")


def generate_summary(api_key: str, articles: list[dict]) -> str:
    """
    Генерация краткого обзора новостей через Mistral
    """
    url = "https://api.mistral.ai/v1/chat/completions"

    # собираем текст из статей
    articles_text = ""
    for i, article in enumerate(articles[:8], 1):
        title = article.get("title", "No title")
        desc = article.get("description", "No description")
        articles_text += f"{i}. {title} - {desc}\n"

    # твой уникальный prompt (важно)
    prompt = f"""
Ты пишешь для игрового блога. Сделай краткий обзор новостей (200-250 слов) на русском языке.

Объясни:
- что произошло
- почему это важно для игроков
- общий вывод по индустрии

Новости:
{articles_text}
"""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistral-small",
        "messages": [{"role": "user", "content": prompt}],
    }

    try:
        response = r.post(url, headers=headers, json=data, timeout=15)
        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Ошибка при работе с Mistral API: {e}"