from api.base_api import BaseAPI


class UsersAPI(BaseAPI):

    def get_users(self, page=2):
        return self.get(
            f"/api/users?page={page}"
        )

    def get_user(self, user_id):
        return self.get(
            f"/api/users/{user_id}"
        )

    def create_user(self, user_data):
        return self.post(
            "/api/users",
            user_data
        )

    def update_user(self, user_id, user_data):
        return self.put(
            f"/api/users/{user_id}",
            user_data
        )

    def delete_user(self, user_id):
        return self.delete(
            f"/api/users/{user_id}"
        )
    
    def patch_user(self, user_id, user_data):
        return self.patch(
            f"/api/users/{user_id}",
            user_data
        )
