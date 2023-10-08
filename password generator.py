import random
import string

def generate_password(length):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Prompt the user for the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print("Generated Password: " + password)

if __name__ == "__main__":
    main()
