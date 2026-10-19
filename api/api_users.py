from api.api_base import BaseAPI

class UsersAPI(BaseAPI):

    def get_all_users(self):
        return self.GET("/users")

    def get_single_user(self, user_id):
        return self.GET(f'/users/{user_id}')

    def search_users(self, query):
        return self.GET('/users/search', params={'q':query})

    def filter_users(self, key, value):
        return self.GET('/users/filter', params={'key':key, 'value':value})

    def limit_and_skip_users(self, limit, skip,select):
        return self.GET('/users', params={'limit':limit, 'skip':skip, 'select':select})

    def sort_users(self,sortBy,order):
        return self.GET('/users', params={'sortBy':sortBy, 'order':order})

    def get_users_carts_by_id(self, user_id):
        return self.GET(f'/users/{user_id}/carts')

    def get_users_post_by_id(self, user_id):
        return self.GET(f'/users/{user_id}/posts')

    def add_new_user(self, payload):
        return self.POST('/users/add', payload)

    def patch_user(self, user_id, payload):
        return self.PATCH(f'/users/{user_id}', payload)

    def put_user(self, user_id, payload):
        return self.PUT(f'/users/{user_id}', payload)

    def delete_user(self, user_id):
        return self.DELETE(f'/users/{user_id}')