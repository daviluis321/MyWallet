from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings

from model_mommy import mommy

class CoreTestLogin(TestCase):

	def setUp(self):
		self.client    = Client()
		self.login_url = reverse('login')
		self.user      = mommy.make('User', username='test_user', is_active = True)

		self.user.set_password('test_password')
		self.user.save()

	def tearDown(self):
		self.user.delete()


	def test_login_ok(self):
		data 		 = {'username': 'test_user', 'password': 'test_password'}
		response     = self.client.post(self.login_url, data)
		redirect_url = reverse(settings.LOGIN_REDIRECT_URL)

		self.assertRedirects(response, redirect_url)
		#self.assertTrue(response.wsgi_request.user.is_authenticated())

	def test_login_error(self):
		data 	  = {'username': self.user.username, 'password': '321'}
		response  = self.client.post(self.login_url, data)
		error_msg = 'Por favor, entre com um usuário  e senha corretos. Note que ambos os campos diferenciam maiúsculas e minúsculas.'

		self.assertFormError(response, 'form', None, error_msg)