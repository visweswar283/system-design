class Email:
    def __init__(self, from_email, to_email, subject, body):
        self.from_email = from_email
        self.to_email = to_email
        self.subject = subject
        self.body = body
        self.is_read = False

    
    def get_summary(self):
        return f"From: {self.from_email}\n To: {self.to_email}\n Subject: {self.subject}"
    
    def get_full_content(self):
        return f"{self.get_summary()}\nBody: {self.body}"
    
    def mark_as_read(self):
        self.is_read = True

    def archive(self):
        print("Archived Email ")

    def delete(self):
        print("Deleted Email ")

    def moveMail(self):
        print(f"email moved to {folder_name} ")
        pass

    def snooze(self):
        print("Email snoozed temporarily ")

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


for k, v in email_storage.items():
    print("Email received: ")
    print(f"{v}")


showLabels()
print("choose one option from the ")
