import random
import string

def generate_captcha():
    # Define all possible characters for the CAPTCHA
    characters = string.ascii_letters + string.digits + '!@#$%^&*()_+-=[]{}|;:,.<>?'
    
    # Generate a random CAPTCHA of length 5
    captcha = ''.join(random.choice(characters) for _ in range(5))
    
    return captcha

# Generate and print a CAPTCHA
captcha = generate_captcha()
print("Generated CAPTCHA:", captcha)