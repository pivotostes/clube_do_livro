from flask_admin import Admin
from flask_admin.menu import MenuLink
from admin.Views import RoleView, ProductView, CategoryView, UserView, HomeView

from models.Role import Role
from models.Category import Category
from models.Product import Product
from models.User import User


def start_views(app, db):

    admin = Admin(app=app, name='Clube do Livro',
                  base_template='admin/base.html', template_mode='bootstrap3',
                  index_view=HomeView())

    admin.add_view(RoleView(Role, db.session, "Funções", category='Acesso'))
    admin.add_view(UserView(User, db.session, "Usuários", category='Acesso'))
    admin.add_view(CategoryView(Category, db.session, "Categorias",
                                category='Estoque'))
    admin.add_view(ProductView(Product, db.session, "Produtos",
                               category='Estoque'))

    admin.add_link(MenuLink(name='Sair', url='/logout'))
