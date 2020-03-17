import hashlib
from getpass import getpass


class User:
    def __init__(self, login, password, first_name, last_name, dob, email, position=None):
        self.login = login
        pass_hash = hashlib.sha256()
        pass_hash.update(password.encode())
        self.password = pass_hash.hexdigest()
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.position = position

        archive = open("acc", "a+")

        counter = 1
        with open('acc', 'r') as ar:
            for line in ar:
                counter += 1

        archive.write(f"{counter}/{self.login}/{self.password}/{self.first_name}/{self.last_name}/{self.dob}/{self.email}/{self.position};\r\n")
        archive.close()


class SignIn:
    def __init__(self, login, password):
        self.login = login

        pass_hash2 = hashlib.sha256()
        pass_hash2.update(password.encode())
        self.password = pass_hash2.hexdigest()

        match = False
        with open('acc', 'r') as ar:
            for line in ar:
                if f"/{self.login}/" in line:
                    print("Login match!")
                    match = True
                    if self.password in line:
                        print("Pass match!")
                        print("")

                        counter = 0
                        for idx, i in enumerate(line):
                            if i == '/':
                                counter += 1
                                if counter == 3:
                                    info_display = ((line[idx:-2]).split("/"))
                                    break

                        for i in info_display:
                            if i != '':
                                print(i)
                        break
                    else:
                        print("Pass doesn't match!")
            if not match:
                print("Login was not found!")
        ar.close()


def pass_check(passw):
    error = False
    if len(passw) < 6:
        return "Pass should be at least 6 symbols long!"
    if len(passw) > 20:
        return "Pass should be 16 symbols long max!"
    if not any(char.isdigit() for char in passw):
        return "Pass should contain at least 1 digit!"
    if not any(char.isupper() for char in passw):
        return "Pass should contain at least one uppercase letter!"
    if not any(char.islower() for char in passw):
        return "Pass should contain at least one lowercase letter!"
    if not error:
        return "This is fine!"



