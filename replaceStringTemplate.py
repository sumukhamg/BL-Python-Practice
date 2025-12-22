message = "Hello <<UserName>>, How are you?"
name = input("Enter your name:")

def checkLength(name):  
    if len(name) < 3:
        print("name should have minimum of 3 character")
        return False
    return True

if checkLength(name):
    message = message.replace( "<<UserName>>", name )

print(message)