import string

COMMON_PASSWORDS = {
    "123456",
    "123456789",
    "qwerty",
    "password",
    "12345",
    "qwerty123",
    "1q2w3e",
    "12345678",
    "111111",
    "1234567890",
    "1234567",
    "password1",
    "123123",
    "abc123",
    "qwe123",
    "1q2w3e4r",
    "admin",
    "qwertyuiop",
    "654321",
    "1234",
    "iloveyou",
    "000000",
    "password123",
    "1qaz2wsx",
    "zaq12wsx",
    "qazwsx",
    "letmein",
    "monkey",
    "dragon",
    "football",
    "baseball",
    "welcome",
    "shadow",
    "master",
    "superman",
    "trustno1",
    "sunshine",
    "princess",
    "flower",
    "hottie",
    "loveme",
    "starwars",
    "whatever",
    "freedom",
    "computer",
    "michael",
    "jennifer",
    "jordan",
    "hunter",
    "ranger",
    "buster",
    "soccer",
    "harley",
    "hockey",
    "killer",
    "george",
    "sexy",
    "andrew",
    "charlie",
    "thomas",
    "robert",
    "tiger",
    "zxcvbn",
    "zxcvbnm",
    "asdfghjkl",
    "asdf1234",
    "q1w2e3r4",
    "qwerty1",
    "p@ssw0rd",
    "passw0rd",
    "letmein123",
    "changeme",
    "default",
    "root",
    "toor",
    "guest",
    "test",
    "demo",
    "sample",
    "temp",
    "temp123",
    "abcd1234",
    "a1b2c3d4",
    "1qaz2wsx3edc",
    "121212",
    "123321",
    "7777777",
    "1111111",
    "88888888",
    "target123",
    "987654321",
    "159753",
    "qwerty12345"

}

def convert_time(seconds):
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif minutes < 60:
        return f"{minutes:.2f} minutes"
    elif hours < 24:
        return f"{hours:.2f} hours"
    elif days < 365:
        return f"{days:.2f} days"
    else:
        return f"{years:.2f} years"

while True:
    password = input("\nEnter the password to check (or type 'exit' to quit): ")
    if password.lower() == "exit":
        print("Exiting password checker. Goodbye!")
        break

    print("\nChecking password strength...\n")
    print("-" * 50)

    if password in COMMON_PASSWORDS:
        print("[!] This password exists in the common password database!")
        print("Estimated time to crack: instantly!")
        continue

    score = 0
    charset_size = 0

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    if len(password) >= 8:
        score += 1
        print("[+] Password length is good!")

    if any(c.islower() for c in password):
        score += 1
        charset_size += len(lowercase)
        print("[+] Password contains lowercase letters!")

    if any(c.isupper() for c in password):
        score += 1
        charset_size += len(uppercase)
        print("[+] Password contains uppercase letters!")

    if any(c.isdigit() for c in password):
        score += 1
        charset_size += len(digits)
        print("[+] Password contains digits!")

    if any(c in symbols for c in password):
        score += 1
        charset_size += len(symbols)
        print("[+] Password contains special characters!")

    if charset_size == 0:
        charset_size = 1  

    combinations = charset_size ** len(password)
    guesses_per_second = 1_000_000_000
    seconds = combinations / guesses_per_second

    print("\nStrength result")
    print("-" * 50)

    if score <= 1:
        print("[!] Password is weak!")
    elif score == 2:
        print("[!] Password is moderate!")
    elif score == 3:
        print("[+] Password is strong!")
    else:
        print("[+] Password is very strong!")

    print(f"Estimated time to crack: {convert_time(seconds)}")
