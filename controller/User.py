from models.User import User


class UserController():
    def __init__(self):
        self.user_model = User()

    def get_admin_login(self, user_id):
        return User.query.filter_by(id=user_id).first()

    def login(self, email, password):
        user = User.query.filter_by(email=email).first()
        if user:
            verify = user.verify_password(user.password, password)
            if verify:
                return user

        return None
