import unittest
from unittest.mock import patch, MagicMock
from src.app import cadastro_user, cadastro, wellcome, get_product_price, processar_pagamento, criar_user, enviar_sms, enviar_email
class TestApp(unittest.TestCase):
#-------------------------------------------------
    def test_cadastro_user(self):
        cadastro = cadastro_user('vivi', 'vivi@gmail.com')
        self.assertEqual(cadastro, 'sucesso')

    #def test_cadastro_user_false(self):
    #    cadastro_user = ('vivi', 'vivi@gmail.com')
    #    cadastro = cadastro_user('viviane', 'vivi@gmail.com')
    #    self.assertEqual(cadastro, 'email ja cadastrado')

    @patch("src.app.save", return_value = True)
    def test_cadastrar_usuario_válido(self, mock_salvar):
        nome = "Viviane"
        cpf = "49313989875"
        resultado = cadastro(nome, cpf)
        self.assertTrue(resultado)
        mock_salvar.assert_called_once_with({'nome':nome, 'cpf':cpf})
#-------------------------------------------------
    @patch('src.app.send_mail', return_value = True)
    def test_process_envio_bv(self, mock_send_mail):
        resultado = wellcome('vivi@gmail.com')
        self.assertEqual(resultado, 'email enviado')
        mock_send_mail.assert_called_once_with('vivi@gmail.com')
#-------------------------------------------------
    @patch('src.app.fetch_product_price_from_api')
    def test_get_product_price(self, mock_fetch):
        mock_fetch.return_value = {
            'status_code': 200,
            'json': {'preco':150.00}
        }
        product_id = 12345
        price = get_product_price(product_id)
        self.assertEqual(price,150.00)
        mock_fetch.assert_called_once_with(product_id)
#-------------------------------------------------
    @patch('src.app.enviar_pagamento', return_value = True)
    def test_processar_pagamento(self, mock_enviar_pagamento):
        resultado = processar_pagamento('150.00')
        self.assertEqual(resultado, 'pagamento confirmado')
        mock_enviar_pagamento.assert_called_once_with('150.00')
#-------------------------------------------------
#13
    @patch('src.app.enviar_email')
    @patch('src.app.enviar_sms')
    def test_criar_user(self, mock_enviar_sms, mock_enviar_email):
        criar_user('Viviane', 'viviane@teste.com', '123456789')
        mock_enviar_email.assert_called_once_with('viviane@teste.com', "cadastro realizado")
        mock_enviar_sms.assert_called_once_with('123456789', "cadastro realizado")
        self.assertEqual(mock_enviar_email.call_count, 1)
        self.assertEqual(mock_enviar_sms.call_count, 1)
#-------------------------------------------------
if __name__ == '__main__':
     unittest.main()

