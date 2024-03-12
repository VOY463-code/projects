import random
import string

def generate_password(length=12):
    # Kies willekeurige karakters uit letters, cijfers en leestekens
    characters = string.ascii_letters + string.digits + string.punctuation
    # Genereer een wachtwoord met de opgegeven lengte
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Vraag de gebruiker om de lengte van het wachtwoord
password_length = int(input("Geef de gewenste lengte van het wachtwoord op: "))

# Genereer en print het wachtwoord
random_password = generate_password(password_length)
print("Het gegenereerde wachtwoord is:", random_password)
