from django.core.urlresolvers import reverse
from django.test import TestCase

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_login_view_status_code(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
   	def test_main_view_status_code(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_contato_view_status_code(self):
        url = reverse('contato')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_quem_somos_view_status_code(self):
        url = reverse('quem_somos')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

