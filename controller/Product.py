from models.Product import Product


class ProductController():
    def __init__(self):
        self.product_model = Product()

    def getTotalProducts(self):
        db = self.product_model.getDb()

        try:
            res = db.session.query(db.func.count(Product.id)).first()[0]
        except Exception as e:
            res = 0
            print(e)
        finally:
            db.session.close()

        return res

    def getLastProducts(self):
        db = self.product_model.getDb()

        try:
            res = db.session.query(Product).order_by('date_created').limit(5)
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()

        return res
