from flask_admin.contrib.sqla import ModelView


class RoleView(ModelView):
    pass


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


class CategoryView(ModelView):
    pass


class ProductView(ModelView):
    pass
