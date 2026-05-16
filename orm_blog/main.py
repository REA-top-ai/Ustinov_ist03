from database import SessionLocal, engine, Base
from models import Author, Post, Comment
from crud import *

def main():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    try:
        print("Начинаем тестирование...\n")

        author1 = create_author(session, "Устинов Алескандр", "alx.ustinov@yandex.ru")
        author2 = create_author(session, "Степан Ложков", "om7go@gmail.com")
        print(f"{author1.name} (id={author1.id})")
        print(f"{author2.name} (id={author2.id})\n")

        post1 = create_post(session, "Первый пост", "Содержание первого поста.", author1.id, published=True)
        post2 = create_post(session, "Черновик", "Этот пост не опубликован.", author1.id, published=False)
        post3 = create_post(session, "Пост Сани", "Текст от Сани.", author2.id, published=True)

        add_comment(session, post1.id, "Читатель1", "Отличная статья!")
        add_comment(session, post1.id, "Читатель2", "Спасибо за материал!")
        add_comment(session, post1.id, "Аноним", "Коротко.")

        update_post_status(session, post2.id, published=True)

        print("Опубликованные посты:")
        for post in get_published_posts(session):
            print(f"  '{post.title}' — {post.author.name}")

        print("\nТоп авторов:")
        for rank, (name, count) in enumerate(get_top_authors_by_posts(session), 1):
            print(f"  {rank}. {name}: {count} пост(ов)")

        found = get_author_by_email(session, "alx.ustinov.ru")
        print(f"\nНайден автор: {found.name}")

        # Тест 1: поиск по имени
        print("\nПоиск по имени:")
        found_by_name = get_author_by_name(session, "Анна Петрова")
        if found_by_name:
            print(f"  Найден: {found_by_name.name}, {found_by_name.email}")

        # Тест 2: посты за сегодня
        print("\nПосты за сегодня:")
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        posts_today = get_published_posts_by_date(session, today)
        for p in posts_today:
            print(f"  '{p.title}'")

        # Тест 3: добавить нескольких авторов сразу
        print("\nДобавляем нескольких авторов:")
        new_authors = create_authors_bulk(session, [
            {"name": "Мария Иванова", "email": "maria@example.com"},
            {"name": "Алексей Козлов", "email": "alex@example.com"},
        ])
        for a in new_authors:
            print(f"  Создан: {a.name} (id={a.id})")

        # Тест 4: пост с комментариями
        print("\nПост с комментариями:")
        result = get_post_with_comments(session, post1.id)
        if result:
            post, comments = result
            print(f"  Пост: '{post.title}'")
            for c in comments:
                print(f"    Комментарий от {c.author_name}: {c.text}")

    except Exception as e:
        print(f"Ошибка: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    main()