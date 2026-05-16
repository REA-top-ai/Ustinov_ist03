from sqlalchemy.orm import Session
from models import Author, Post, Comment
from datetime import datetime

def create_author(session: Session, name: str, email: str) -> Author:
    new_author = Author(name=name, email=email)
    session.add(new_author)
    session.commit()
    session.refresh(new_author)
    return new_author

def get_author_by_email(session: Session, email: str) -> Author | None:
    return session.query(Author).filter(Author.email == email).first()

def create_post(session: Session, title: str, content: str,
                author_id: int, published: bool = False) -> Post:
    new_post = Post(title=title, content=content,
                    author_id=author_id, published=published)
    session.add(new_post)
    session.commit()
    session.refresh(new_post)
    return new_post

def get_published_posts(session: Session, limit: int = 10) -> list[Post]:
    return session.query(Post).filter(Post.published == True).limit(limit).all()

def get_posts_by_author(session: Session, author_id: int, limit: int = 10) -> list[Post]:
    return session.query(Post).filter(Post.author_id == author_id).limit(limit).all()

def update_post_status(session: Session, post_id: int, published: bool) -> bool:
    post = session.query(Post).filter(Post.id == post_id).first()
    if post is None:
        return False
    post.published = published
    session.commit()
    return True

def add_comment(session: Session, post_id: int, author_name: str, text: str) -> Comment:
    new_comment = Comment(post_id=post_id, author_name=author_name, text=text)
    session.add(new_comment)
    session.commit()
    session.refresh(new_comment)
    return new_comment

def get_top_authors_by_posts(session: Session, limit: int = 3) -> list[tuple[str, int]]:
    from sqlalchemy import func, desc
    result = (session.query(Author.name, func.count(Post.id).label('post_count'))
              .join(Post)
              .group_by(Author.id)
              .order_by(desc('post_count'))
              .limit(limit)
              .all())
    return result

# 1. Найти автора по имени
def get_author_by_name(session: Session, name: str) -> Author | None:
    return session.query(Author).filter(Author.name == name).first()

# 2. Опубликованные посты за определённую дату
def get_published_posts_by_date(session: Session, date: datetime) -> list[Post]:
    from datetime import timedelta
    next_day = date + timedelta(days=1)
    return (session.query(Post)
            .filter(Post.published == True)
            .filter(Post.created_at >= date)
            .filter(Post.created_at < next_day)
            .all())

# 3. Добавить сразу нескольких авторов
def create_authors_bulk(session: Session, authors_data: list[dict]) -> list[Author]:
    authors = []
    for data in authors_data:
        author = Author(name=data["name"], email=data["email"])
        session.add(author)
        authors.append(author)
    session.commit()
    for author in authors:
        session.refresh(author)
    return authors

# 4. Найти пост по id с комментариями
def get_post_with_comments(session: Session, post_id: int):
    post = session.query(Post).filter(Post.id == post_id).first()
    if post is None:
        return None
    return post, post.comments