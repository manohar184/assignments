#9: Use else block to display a message “Done” after successful execution of for loop.


userList["Manohar","Gopal","Sai","Sarath"]
name=input("Enter the user name :")
for user in userList:
    if user == name:
        print("Done")
    else:
        print("Invalid user name")

