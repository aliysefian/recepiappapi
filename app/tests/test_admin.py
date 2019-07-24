from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self):
        """
        bfore test start
        :return:
        """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_super_user(email='admin@admin.com', password='test123')
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(email='user@admin.com', password='test123', name='test ')

    def test_users_listed(self):
        url = reverse('admin:app_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_chage_page(self):
        url = reverse("admin:app_user_change", args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """

        :return:
        """
        url = reverse("admin:app_user_add")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
