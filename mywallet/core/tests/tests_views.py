class LoginTests(TestCase):
    def test_home_url_resolves_home_view(self):
            view = resolve('/login')
            self.assertEquals(view.func, login)

class RecuperaSenhaTests(TestCase):
    def test_home_url_resolves_home_view(self):
            view = resolve('/recuperaSenha')
            self.assertEquals(view.func, recuperaSenha)

class ContatoTests(TestCase):
    def test_home_url_resolves_home_view(self):
            view = resolve('/contato')
            self.assertEquals(view.func, contato)

class MainTests(TestCase):
    def test_home_url_resolves_home_view(self):
            view = resolve('/main')
            self.assertEquals(view.func, main)

class InvestimentoTests(TestCase):
    def test_home_url_resolves_home_view(self):
            view = resolve('/investimento')
            self.assertEquals(view.func, investimento)

class DespesaTests(TestCase):
    def test_home_url_resolves_home_view(self):
            view = resolve('/despesa')
            self.assertEquals(view.func, despesa)

class QSOMOSTests(TestCase):
    def test_home_url_resolves_home_view(self):
            view = resolve('/qsomos')
            self.assertEquals(view.func, qsomos)
