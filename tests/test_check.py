import unittest
from check import checkuser

'''
def test_valid_user():
	user = "foo@outlook.com" 
	result = checkuser.validate(user)
	assert "AADSTS50126" in result, "Conta Existente"
'''

def test_invalid_user():
	user = "teste@outlook.com"
	result = checkuser.validate(user)
	assert "AADSTS50034" in result, "Conta Inexistente"

