from API_methds.API_methods import  fetch_news, generate_summary

TOPIC = "gaming"

if __name__ == "__main__":
    # получаем новости
    result = fetch_news(
        endpoint="everything",
        api_key="e9ab7edf931141c789b87603727dc276",
        params={"q": TOPIC, "language": "en", "pageSize": 10}
    )

    articles = result.get("articles", [])

    # делаем краткий обзор
    summary = generate_summary("kQqBRtxRtprQbtGVEhwbAVrbMaXj0V0v", articles)

    # сохраняем в файл
    with open("../gaming_news.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    # выводим в консоль
    print("=== Gaming News Summary ===\n")
    print(summary)