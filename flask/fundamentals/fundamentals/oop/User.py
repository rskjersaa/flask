class User:
    def __init__(self,fname,lname,email,age):
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.age =age
        self.rewards_member = False
        self.gold_card_points = 0
        

    def display_info(self):
                    print(f"""                    {self.first_name} 
                    {self.last_name}
                    {self.email}
                    { self.age} 
                    {self.rewards_member} 
                    {self.gold_card_points}""")
                    return self

# new_user = User("pam")

    
    def enroll(self):
        self.rewards_member = True
        self.gold_card_points = 200 
        return self

# pam.display_info()

    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        return self

    
user_2=User("jim","jones","jim@aol.com", 23)
pam = User("pam","marshall", "pam@aol.com", 34)
# pam.display_info()

# pam.enroll()
# # pam.display_info()
# pam.spend_points (50)
# pam.display_info()
pam.display_info().enroll().spend_points(50).display_info()

user_2.display_info().enroll().spend_points (20).display_info()

# user_2.enroll()
# user_2.spend_points (20)
# user_2.display_info()

# user_2.display_info()