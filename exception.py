class InvalidNameError(BaseException):
    def __str__(self):
        print("Name should not contain any digits or symbols. Try again!!")
class InvalidMobileNumberError(BaseException):
    def __str__(self):
        print("Entered mobile number is incorrect. Try again!!")
class InvalidEmailError(BaseException):
    def __str__(self):
        print("Please enter valid e-mail address!!")
class InvalidaddressError(BaseException):
    def __str__(self):
        print("Try again with the valid address")
class InvalidPasswordError(BaseException):
    def __str__(self):
        print("Enter")
class PasswordCheck:
    def password_validation(passwd):
        specialsym=['@','$','#','%']
        val=True
        if len(passwd)<8:
            print("Length should be atleast 8 ")
            val=False
        if not any(char.isupper() for char in passwd):
            print("Password should contain atleast one Uppercase letter")
            val=False
        if not any(char.islower() for char in passwd):
            print("Password should contain atleast one Lowercase letter")
            val=False
        if not any(char in specialsym for char in passwd):
            print("Password should contain atleast one of the symbols(@#$%) ")
            val=False
        if val:
            return val
        