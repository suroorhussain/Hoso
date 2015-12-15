import channels
from mock import Mock
from channels import mail

def test_authentication():
   mock = Mock()
   mock.authentication()
   username = "hoso@gamil.com"
   password = "password"
   login = mock.SendGridClient(username, password)
   mock.login = "True"
   mock.authentication.assert_called_with()
   
