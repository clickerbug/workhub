import string
import secrets
from random import choice
from user.models import User


def generate_unique_username(username):
    generatedUsername = username + ''.join([choice(string.digits) for i in range(3)])
    try:
        User.objects.get(username=generatedUsername)
        return generate_unique_username(username)
    except User.DoesNotExist:
        return generatedUsername


def generate_username_from_email(email):
    try:
        emailUsername = email.split('@')[0]
        return generate_unique_username(emailUsername)
    except IndexError:
        return None


def generate_password():
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(10))
