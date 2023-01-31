#ask user to inout id and check the length of email is greater than 10 and less than 20 its a valid email


#email = input("Enter an email:")
#length = len(email)
#
#if length >= 10 and length <= 20:
#    print("Valid Email")
#else:
#    print("Invalid Email")
#
#if email.index('@'):
#    print("valid")
#else:
#    print("Invliad")

"""
email = input("Enter an email:")
length = len(email)

def length_text(email):
    if length >= 10 and length <= 20:
        print("valid Email")
    else:
        print("Invlaid")
    
def check

"""


def checklength(s):
    if len(s)>=10 and len(s)<=20:
        return True
    else:
        False

def check_char(s):
    if s.index('@'):
        return True
    else:
        return False


email = input("Enter an email:")
print(check_char(email) and checklength(email))