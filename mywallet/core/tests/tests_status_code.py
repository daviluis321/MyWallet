from django.urls import reverse
from django.test import TestCase
class CoreStatus(TestCase):
    def test_home_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_login_status_code(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_main_status_code(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_contato_status_code(self):
        url = reverse('contato')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_investimento_status_code(self):
        url = reverse('investimento')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        
    def test_despesa_status_code(self):
        url = reverse('despesa')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
  
    def test_quem_somos_status_code(self):
        url = reverse('qsomos')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    