from api.api_base import BaseAPI

class ProductsAPI(BaseAPI):

    def get_all_products(self):
        return self.GET('/products')

    def get_single_product(self, product_id):
        return self.GET(f"/products/{product_id}")

    def search_products(self, query):
        return self.GET('/products/search',params={"q":query})

    def limit_and_skip_product(self,limit,skip, select):
        return self.GET("/products",params={"limit":limit,"skip":skip,"select":select})

    def sort_products(self, sortBy, order):
        return self.GET("/products", params={"sortBy":sortBy,"order":order})

    def get_all_categories(self):
        return self.GET("/products/categories")

    def get_categories_list(self):
        return self.GET("/products/category-list")

    def get_category_name(self,category_name):
        return self.GET(f"/products/category/{category_name}")

    def add_product(self,payload):
        return self.POST("/products/add", payload)

    def update_product(self,product_id,payload):
        return self.PUT(f"/products/{product_id}", payload)

    def patch_product(self,product_id,payload):
        return self.PATCH(f"/products/{product_id}", payload)

    def delete_product(self,product_id):
        return self.DELETE(f"/products/{product_id}")