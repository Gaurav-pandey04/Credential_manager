#Greets the user with welcome message and ask to enter login details
print("Welcome!\nEnter your login details")

#open the username.txt and userpassword.txt where usernames and userpasswords are saved
fo_name=open('username.txt','r')
fo_passwd=open('userpassword.txt','r')

#Empty list to take username and password from files
user_name=[]
user_passwd=[]

#username
fo_name_read= fo_name.readlines()                #reading every lines of username.txt
user_name.append(fo_name_read)                   #appending all lines into user_name(list)
[username]=user_name                             #removing extra list
verify_username=[n.rstrip() for n in username]   #rermoving extra spaces(lines)

#password
fo_passwd_read= fo_passwd.readlines()               #reading every lines of userpassword.txt
user_passwd.append(fo_passwd_read)                  #appending all lines into user_passwd(list)
[userpasswd]=user_passwd                            #removing extra list
verify_userpasswd=[p.rstrip() for p in userpasswd]  #rermoving extra spaces(lines)


#Verify the username
def User_verify():          
    for value in verify_username:
        if user_name==value:
            return 0                                 #If user is verified then return 0 
 

#Verify the password of user
def Passwd_verify():
    user_passd=input("Enter a password > ")          #Takes the password from user
    index = verify_username.index(user_name)         #Finds the index to verify only those password which is associated with the respective user only
    for valuepass in verify_userpasswd:
        if user_passd==verify_userpasswd[index]:     #Verify the password of user
            print("Login Sucessfully!")              #Display login Sucessfull message to the user
            break
        else:
            print("You have entered wrong Password")  #Display Wrong password message to the user
            Passwd_verify()                           #Again call the function to enter login details again to the user
            break
       

#Display wrong username message
def wrong_username():
    print("You have entered wrong username!")


#Takes the username from user
user_name=input("Enter a User Name > ")        
if User_verify()==0:                 #If user is true then it will authenticate password of user
    Passwd_verify()
else:
    wrong_username()                #If user is false then it will display message