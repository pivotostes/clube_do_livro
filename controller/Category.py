from models.Category import Category


class CategoryController():
    def __init__(self):
        self.category_model = Category()

    def getTotalCategories(self):
        db = self.category_model.getDb()

        try:
            res = db.session.query(db.func.count(Category.id)).first()[0]
        except Exception as e:
            res = 0
            print(e)
        finally:
            db.session.close()

        return res
