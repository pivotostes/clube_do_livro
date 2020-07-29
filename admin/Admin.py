from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from models.Role import Role
from models.Category import Category
from models.Product import Product
from models.User import User


def start_views(app, db):

    admin = Admin(app=app, name='Clube do Livro',
                  base_template='admin/base.html', template_mode='bootstrap3')

    admin.add_view(ModelView(Role, db.session, "Funções", category='Acesso'))
    admin.add_view(ModelView(User, db.session, "Usuários", category='Acesso'))
    admin.add_view(ModelView(Category, db.session, "Categorias",
                             category='Estoque'))
    admin.add_view(ModelView(Product, db.session, "Produtos",
                             category='Estoque'))