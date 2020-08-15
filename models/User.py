from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from config import app_config, app_active
from models.Role import Role
from passlib.hash import pbkdf2_sha256
from flask_login import UserMixin

config = app_config[app_active]
db = SQLAlchemy(config.APP)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    date_created = db.Column(db.DateTime(),
                             default=db.func.current_timestamp(),
                             nullable=False)

    last_update = db.Column(db.DateTime(),
                            onupdate=db.func.current_timestamp(),
                            nullable=True)

    recovery_code = db.Column(db.String(200), nullable=True)
    active = db.Column(db.Boolean(), default=1, nullable=True)
    role = db.Column(db.Integer, db.ForeignKey(Role.id), nullable=False)

    funcao = relationship(Role)

    def __repr__(self):
        return '{} - {}'.format(self.id, self.username)

    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)

    def verify_password(self, password_hash, password_no_hash):
        return pbkdf2_sha256.verify(password_no_hash, password_hash)
