
from passlib import  context

pwd_context = context.CryptContext(schemes=['bcrypt'], deprecated = 'auto')
class Hash():
    def bcryt(password: str):
        return pwd_context.hash(password)
    def verify(hashed_password, plain_password):
        return pwd_context.verify(plain_password,hashed_password)