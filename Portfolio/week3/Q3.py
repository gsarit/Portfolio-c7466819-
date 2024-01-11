# Modify your previous program so that the password must be between 8 and 12 characters (inclusive) long.
def check_password(password):
    if 8 <= len(password) <= 12:
        return True
    else:
        return False

def main():
    password = input("Enter your password: ")

    if check_password(password):
        print("Password is valid.")
    else:
        print("Password must be between 8 and 12 characters long.")

if __name__ == "__main__":
    main()