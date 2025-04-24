from flask_login import UserMixin


class UserLogin(UserMixin):
    def fromDB(self, user_id, db):
        self.__user = db.getUser(user_id)  # наш метод возврата из бд
        return self
    
    def create(self, user):
        self.__user = user
        return self
    
    # def is_authenticated(self):  # определены в ЮзерМиксин
    #     return True
    #
    # def is_active(self):
    #     return True
    #
    # def is_anonymous(self):
    #     return False
    #
    def get_id(self):
        return str(self.__user['id'])
