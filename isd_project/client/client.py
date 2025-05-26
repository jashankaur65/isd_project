from email_validator import validate_email, EmailNotValidError

class Client:
    def __init__(self, first_name, last_name, email, client_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__client_number = client_number
        self.set_email(email)

    def set_email(self, email):
        try:
            valid = validate_email(email)
            self.__email = valid.email
        except EmailNotValidError as e:
            raise ValueError(str(e))

    def get_email(self):
        return self.__email

    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    def get_client_number(self):
        return self.__client_number

    def __str__(self):
        return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email}"
