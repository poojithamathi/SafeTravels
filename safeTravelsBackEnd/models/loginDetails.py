import re


class loginDetails:
    def __init__(self, emailAddress, password):
        self.emailAddress = emailAddress
        self.password = password
    
    def validateEmail(self):
        if(len(self.emailAddress) <= 2):
            return False
        emailRegex = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        validate = re.search(emailRegex, self.emailAddress)
        if validate:
            return True
        else:
            return False

