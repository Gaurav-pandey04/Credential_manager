print("Welcome!\nEnter your login details")

verify_username=["user","user2","user3","user4"]

verify_userpasswd=["stud","stud2","stud3","stud4"]

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