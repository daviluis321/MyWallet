from django.core import mail
from django.test import TestCase

class EmailTest(TestCase):
    def test_send_email(self):
        # Envia mensagem.
        mail.send_mail('Hello Word', 'Aqui vai a mensagem.',
            'mywallet@example.com', ['to@example.com'],
            fail_silently=False)
        # Verifica se o assunto da mensagem é igual
        self.assertEqual(mail.outbox[0].subject, 'Hello Word')
        print(mail.outbox[0])  
        # Verifica se uma mensagem foi enviada.
        self.assertEqual(len(mail.outbox), 1)

  