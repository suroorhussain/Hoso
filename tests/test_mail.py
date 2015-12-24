import hoso.channels as channels
from mock import Mock
from hoso.channels import mail

def test_authentication():
   mock = Mock()
   mock.authentication()
   username = "hoso@gamil.com"
   password = "password"
   login = mock.SendGridClient(username, password)
   mock.login = "True"
   mock.authentication.assert_called_with()

def test_broadcast():
   mock_server = Mock()
   mock_server.broadcast()
   To = "hoso@gmail.com"
   Message = "hai all"
   return_value = mock_server.mail( To, Message)
   mock_server.return_value == "mail sent"
   mock_server.broadcast.assert_called_with()
   
