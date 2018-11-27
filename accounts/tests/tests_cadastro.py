from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

class  CadastroTestsView(TestCase):
    def test_cadastro_view_status_code(self):
        url = reverse('cadastro')
        response = self.client.get(url)
        self.assertNotEquals(response.status_code, 404)

class RegisterViewTestCase(TestCase):

    def setUp(self):
        self.client = User()
        self.register_url = reverse('accounts:cadastro')

    def test_register_ok(self):
        data = {
            'username': 'gileno', 'email': 'test@test.com','password1': 'teste123', 'password2': 'teste123'
        }
        response = self.client[0].post(self.register_url, data)
        index_url = reverse('cadastro')
        self.assertRedirects(response, index_url)
        self.assertEquals(User.objects.count(), 1)

    def test_email_error(self):
        data = {
            'username': 'gileno', 'email': 'test@test','password1': 'teste123', 'password2': 'teste123'
        }
        response = self.client[0].post(self.register_url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')

    def test_password_error(self):
        data = {
            'username': 'gileno', 'email': 'test@test','password1': 'teste', 'password2': 'teste2'
        }
        response = self.client[0].post(self.register_url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')

    def test_name_null(self):
        data = {
            'email': 'test@test','password1': 'teste', 'password2': 'teste2'
        }
        response = self.client[0].post(self.register_url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')

    def test_email_null(self):
        data = {
            'username': 'gileno','password1': 'teste', 'password2': 'teste2'
        }
        response = self.client[0].post(self.register_url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')

    def test_password_null(self):
        data = {
            'username': 'gileno','password1': 'teste','password2': 'teste2'
        }
        response = self.client[0].post(self.register_url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')

    def test_password2_null(self):
        data = {
            'username': 'gileno','password1': 'teste','password': 'teste2'
        }
        response = self.client[0].post(self.register_url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
