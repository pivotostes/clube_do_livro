from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active
from sqlalchemy.orm import relationship

from models.User import User
from models.Category import Category

config = app_config[app_active]
db = SQLAlchemy(config.APP)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=False)
    qtd = db.Column(db.Integer, nullable=True, default=0)
    image = db.Column(db.Text(), nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    date_created = db.Column(db.String(),
                             default=db.func.current_timestamp(),
                             nullable=False)

    last_update = db.Column(db.String(),
                            onupdate=db.func.current_timestamp(),
                            nullable=False)

    status = db.Column(db.Integer, default=1,
                       nullable=True)

    user_created = db.Column(db.Integer, db.ForeignKey(User.id),
                             nullable=False)

    category = db.Column(db.Integer, db.ForeignKey(Category.id),
                         nullable=False)

    # cria a relacao da tabela User/Category com a tabela produto
    # uma vez que são FK.
    user = relationship(User)
    category_re = relationship(Category)
