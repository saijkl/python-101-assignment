class Login:
    def __init__(self, id, password):
        self.id = id
        self.password = password
        self.error = "Enter a valid username and password"
    def check(self):
        if (self.id == log_id and self.password == log_pass):
            print("Login successful")
        else:
            print(self.error)

log = Login("Sai234",  "Sai234")
log_id = input("Enter your user ID: ")
log_pass = input("Enter password: ")
log.check()

