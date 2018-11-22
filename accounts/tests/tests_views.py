from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

class  AccountsTestsView(TestCase):
    def test_cadastro_view_status_code(self):
        url = reverse('cadastro')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_logout_view_status_code(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_home_url_resolves_home_view(self):
        u = User()
        response = c.post('cadastro', {'username': 'john', 'password': 'smith'})
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_null(self):
        view = resolve('cadastro')
        u = User()
        self.assertEquals(u, None)

    def test_home_url_resolves_home_not_null(self):
        u = User()
        response = u.post('cadastro', {'username': 'john', 'password': 'smith'})
        self.assertEquals(u, object())
