


def Inbox():
    pass

def Promotions():
    pass

def Social():
    pass

def Updates():
    pass

def Forums():
    pass

def Spam():
    pass

def Trash():
    pass


# Labels in the Email folder
def showLabels():
    print("1. Inbox")
    print("2. Promotions")
    print("3. Social")
    print("4. Updates")
    print("5. Forums")
    print("6. Spam")
    print("7. Trash")


#First whenver user get the email as of now I will try to manually label it.

#First I will create email structure From, TO, Subject, and Body

# First I will use Dictionary to create key value pairs where key is index(0,1,2) and value is email


print("Hello User, Please write an email I will label to manually")
email_content = ""
email_storage = {}
index = 1

while True:
    text = input("Enter Email to write email or Exit: ")
    if text == "Exit":
        print("Done with Emails ")
        break
    
    from_email_address = input("Enter From email address: ")
    to_email_address = input("Enter To email address: ")
    subject = input("Enter the subject of the email: ")
    body = input("Enter body of the email: ")

    email_content = " Email From: " + from_email_address + " \n " + "TO: " + to_email_address + " \n " + "Subject: " + subject + " \n " + "Body: " + body

    # this will be the email storage of all emails
    email_storage[index] = email_content


    index += 1


for k, v in email_storage.items():
    print("Email received: ")
    print(f"{v}")


showLabels()
print("choose one option from the ")
