class chatbook:
    
    __userid = 0
    
    def __init__(self):
        self.id = chatbook.__userid
        chatbook.__userid +=1
        self.__name = "default"
        self.username = ""
        self.password = ""
        self.login = False
        #self.menue()
        
    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value
        
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
            self.mypost()
        elif user_input == "4":
            self.message()
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
        
    def mypost(self):
        if self.login == True:
            txt = input("type your post")
            print("following content has been posted",txt)
        
        else:
            print("you need to signin first to post")
            
        print("\n")
        self.menue()
        
    def message(self):
        if self.login == True:
            txt = input("enter the message")
            friend = input("whom you want to send")
            print("your message has been send to ", friend)
        
        else:
            print("signin first to send message")
        
        print("\n")
        self.menue()
        
        
        

obj = chatbook()

