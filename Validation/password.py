def pass_word():
    password = input("enter you password \n")
    code = True
    counter=0
    while code:
        if password == "abcd":
            print("correct")
            code=False
        else:
            print("Wrong Password")
            password = input("enter you password again\n")
            counter=counter+1
            if counter>=3:
                print("SYtem Locked")


pass_word()
