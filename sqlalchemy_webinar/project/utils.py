from project.database import session_factory
from project.models import User
from typing import List


# CRUD
def add_user(name: str, email: str) -> User:
    with session_factory() as session:
        user = User(name=name, email=email)

        session.add(user)
        session.commit()
    return user


def get_user_by_id(id: int) -> User:
    with session_factory() as session:
        user = session.query(User).filter(User.id == id).first()
        return user 


def get_all_users() ->  List[User]:
    with session_factory() as session:
        users = session.query(User).all()
        return users


def update_user(id: int, new_name: str | None, new_email: str | None) -> User:
    with session_factory() as session:
        user = get_user_by_id(id)
        if not user:
            return None
        if not new_email and not new_name:
            return None
        if new_email:
            user.email = new_email
        if new_name:
            user.name = new_name
        session.add(user)
        session.commit()
    return user


def drop_user(id: int) -> str:
    with session_factory() as session:
        user = get_user_by_id(id)
        if not user:
            return 'User not found'
        session.delete(user)
        session.commit()
    return 'User has been deleted'
