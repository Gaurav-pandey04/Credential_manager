print("Welcome!\nEnter your login details")

fo_name=open('username.txt','r')
fo_passwd=open('userpassword.txt','r')

user_name=[]
user_passwd=[]

fo_name_read= fo_name.readlines()
user_name.append(fo_name_read)
[username]=user_name
verify_username=[s.rstrip() for s in username]

fo_passwd_read= fo_passwd.readlines()
user_passwd.append(fo_passwd_read)
[userpasswd]=user_passwd
verify_userpasswd=[p.rstrip() for p in userpasswd]

#Function which verify the user authentication
def verification():
    user_name=input("Enter a User Name > ")
    for value in verify_username:
        if user_name==value:
            user_passd=input("Enter a password > ")
            index = verify_username.index(user_name)
            for valuepass in verify_userpasswd:
                if user_passd==verify_userpasswd[index]:
                    print("Login Sucessfully!")
                    break
                else:
                    print("Wrong Password")
                    verification()
                    break
            break

verification()