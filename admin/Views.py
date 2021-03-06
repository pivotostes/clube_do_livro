from flask_admin.base import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect
from controller.User import UserController
from controller.Product import ProductController
from controller.Category import CategoryController


class HomeView(AdminIndexView):
    @expose('/')
    def index(self):
        user = UserController()
        category = CategoryController()
        product = ProductController()

        return self.render('home_admin.html', totalUsers=user.getTotalUser(),
                           totalCategories=category.getTotalCategories(),
                           totalProducts=product.getTotalProducts(),
                           products=product.getLastProducts())


class RoleView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')


class UserView(ModelView):
    column_exclude_list = ('password', 'recovery_code')
    form_excluded_columns = ('recovery_code', 'last_update')
    column_details_exclude_list = ('password', 'recovery_code')
    can_view_details = True
    can_create = True
    can_edit = True
    can_delete = True

    form_widget_args = {
        'password': {
            'type': 'password'
        }
    }

    def on_model_change(self, form, model, is_created):
        if form.password.data is not None:
            model.set_password(form.password.data)

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')


class CategoryView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')


class ProductView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')
