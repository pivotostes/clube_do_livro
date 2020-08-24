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

    def getTotalUser(self):
        db = self.user_model.getDb()

        try:
            res = db.session.query(db.func.count(User.id)).first()[0]
        except Exception as e:
            res = 0
            print(e)
        finally:
            db.session.close()

        return res
