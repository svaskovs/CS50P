from validator_collection import validators

def main():
    print(validate(input("What's your email address? ")))

def validate(email):
    try:
        if validators.email(email):
            return "Valid"
    except ValueError:
        return "Invalid"

if __name__ == "__main__":
    main()
