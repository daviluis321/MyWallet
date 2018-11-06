from django.test import TestCase

# Create your tests here.


class HomeTests(TestCase):
	def test_home_view_status_code(self):
        url = reverse('cadastro')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

	def test_home_url_resolves_home_view(self):
        view = resolve('/cadastro')
        self.assertEquals(view.cadastro, cadastro)

	def test_home_url_resolves_home_view(self):
        view = resolve('/cadastro')
        self.assertEquals(User.objects, None)

