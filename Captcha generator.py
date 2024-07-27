import random
import string

def generate_captcha():
    characters = string.ascii_letters + string.digits + '!@#$%^&*()_+-=[]{}|;:,.<>?'
    captcha = ''.join(random.choice(characters) for _ in range(5))
    
    return captcha
captcha = generate_captcha()
print("Generated CAPTCHA:", captcha)
