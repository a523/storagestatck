from django.test import TestCase
from django.urls import reverse


class UserTestCase(TestCase):
    def test_get_user_list(self):
        resp = self.client.get(reverse('user_admin:users_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(isinstance(resp.json(), list))

    def test_create_user(self):
        user_info = {'user_name': 'xin', 'password': 'test_a!'}
        resp = self.client.post(reverse('user_admin:users_list'), user_info)
        self.assertEqual(resp.status_code, 201)
        new_user_info = resp.json()
        user_id = new_user_info['id']
        self.assertTrue(isinstance(new_user_info, dict))
        self.assertTrue(isinstance(user_id, int))
        self.assertFalse(new_user_info['is_superuser'], "设计应不能通过web创建超级用户")

    def test_get_user_detail(self):
        pass

    def test_update_user(self):
        pass

    def delete_user(self):
        pass
