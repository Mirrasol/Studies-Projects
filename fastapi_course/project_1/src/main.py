from fastapi import FastAPI
# from fastapi_course.project_1.src.database import db_users, db_feedback
from fastapi_course.project_1.src.models import User, Feedback
from fastapi_course.project_1.src.utils import is_adult

app = FastAPI()

# user1 = User(name='Lohn', id=1)
db_feedback = []

@app.get('/')
def read_root():
    return {'message': 'Hi there!'}


@app.get('/custom')
def read_custom_message():
    return {'message': 'Custom Here'}


# @app.get('/users')
# def get_user():
#     return {**user1}


@app.post('/user')
def check_user(user: User):
    return {
        'name': user.name,
        'age': user.age,
        'is_adult': is_adult(user.age),
    }


@app.post('/feedback')
def send_feedback(feedback: Feedback):
    db_feedback.append({'name': feedback.name, 'message': feedback.message})    
    return {'message': f"Feedback received. Thank you, {feedback.name}."}


@app.get('/feedback')
def check_feedback():
    return db_feedback
