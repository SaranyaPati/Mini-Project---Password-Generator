import random
def generate_password(letters, numbers, symbols):
    password = letters + numbers + symbols
    password = ''.join(random.sample(password, len(password)))
    return password
length = int(input("Enter the desired Password length: "))
letters = input("Enter the letters you want in your password: ")
numbers = input("Enter the numbers you want in your password: ")
symbols = input("Enter the symbols you want in your password: ")
password = generate_password(letters, numbers, symbols)
print(f"Generated Password: {password}")
print(f"Letters: {letters}")
print(f"Numbers: {numbers}")
print(f"Symbols: {symbols}")