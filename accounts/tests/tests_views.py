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
        response = u.post('cadastro', {'username': 'john','email': 'john@j.com' , 'password1': 'smith123', 'password2': 'smith123'})
        self.assertEquals(u[0], object())

    def test_home_url_resolves_home_whith_username(self):
        data = {'email': 'gileno@h.com', 'password1': 'teste123', 'password2': 'teste123'}
        response = self.client.post('cadastro', data)
        self.assertFormError(response, 'form', 'username', 'Este campo é obrigatório.')

    def test_home_url_resolves_home_whith_email(self):
        data = {'username': 'gileno', 'password1': 'teste123', 'password2': 'teste123'}
        response = self.client.post('cadastro', data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')

    def test_home_url_resolves_home_whith_password1(self):
        data = {'username': 'gileno','email': 'gileno@h.com', 'password2': 'teste123'}
        response = self.client.post('cadastro', data)
        self.assertFormError(response, 'form', 'password1', 'Este campo é obrigatório.')

    def test_home_url_resolves_home_whith_password2(self):
        data = {'username': 'gileno','email': 'gileno@h.com', 'password1': 'teste123'}
        response = self.client.post('cadastro', data)
        self.assertFormError(response, 'form', 'password2', 'Este campo é obrigatório.')

    def test_home_url_resolves_home_differents_passwords(self):
        data = {'username': 'gileno','email': 'gileno@h.com', 'password1': 'teste123','password2': 'teste1232'}
        response = self.client.post('cadastro', data)
        self.assertNotEquals(data['password1'], data['password2'])



