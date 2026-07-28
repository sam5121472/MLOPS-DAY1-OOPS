class chatbook:
    
    def __init__(self):
        self.username = ""
        self.password = ""
        self.login = False
        self.menue()
        
    def menue(self):
        user_input = input("""welcome to chatbook, how would you like to proceed
                     1. press 1 to signup
                     2. press 2 to signin
                     3. press 3 to add a post
                     4. press 4 to message your friend
                     5. press anyother key to exit""")
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
            
    def signup(self):
        
        email = input("enter the email")
        passward = input("enter a strong password")
        self.username = email
        self.password = passward
        print("you have successfully signup!!")
        print("\n")
        self.menue()
        
    def signin(self):
        if self.username  == "" and self.password == "":
            print("please press 1 to signup !")
        else:
            uname = input("enter the user_name or email here")
            passw = input("enter the password here")
            
            if self.username == uname and self.password == passw:
                print("you have signin successfully! ")
                self.login = True
                
            else:
                print("please enter correct credientials")
        self.menue()
        
        

obj = chatbook()

