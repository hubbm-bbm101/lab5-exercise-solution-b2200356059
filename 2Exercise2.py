mail=input("Write your e-mail:")
def ismail_valid(mail): 
    if "@" in mail and "." in mail:
        print("Your mail is valid")
    else:
        print("Your mail is not valid")
ismail_valid(mail)