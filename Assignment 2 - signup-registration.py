class signup:
    def __init__(self, id, password):
        self.id = id
        self.password = password
        self.error = "Enter a valid username and password"
    def check(self):
        if (self.id == log_id and self.password == log_pass):
            print("Registeration successful")
        else:
            print(self.error)    
            
log = signup("Sai678",   "Sai67rty")
log_id = input("Enter your user ID: ")
log_pass = input("Enter password: ")
log.check()   
              
