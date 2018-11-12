from django.urls import reverse
from django.test import TestCase
class CoreTestsView(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
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
        url = reverse('qsomos')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

