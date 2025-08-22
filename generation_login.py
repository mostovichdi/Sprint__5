import random
import string


class GenerationEmailPassword:

    def __init__(self):
        self.email = None
        self.password = None
        self.name = None

    def generate_email(self):
        domains = ["@yandex.ru", "@gmail.com", "@mail.ru"]
        chars = string.ascii_letters
        self.email = ''.join(random.choice(chars) for char in range(7)) + ''.join(random.choice(domains))
        return self.email
    
    def generate_password(self):
        chars = string.ascii_letters + string.digits + string.punctuation
        self.passwod = ''.join(random.choice(chars)).join(random.choice(chars) for char in range(7)) 
        return self.passwod
    
    def generate_name(self):
        chars = string.ascii_letters
        # length = random.randint(5, 10)
        self.name = ''.join(random.choice(chars) for char in range(6))
        return self.name