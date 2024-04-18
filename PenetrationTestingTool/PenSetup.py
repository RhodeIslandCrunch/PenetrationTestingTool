def SQLWrite():
    # Open/create the file in write mode
    with open("SQLSingleAttacks.txt", "a") as file:
        # Keep accepting input until the user enters "QUIT"
        while True:
            # Get input from the user
            user_input = input("Enter SQL command you wish to add (or 'QUIT' to exit): ")
            # If user_input is "QUIT", exit the loop
            if user_input.upper() == "QUIT":
                break
            # Write the input to the file
            file.write(user_input + "\n")
    print("Commands have been written to SQLSingleAttacks.txt.")
    print("Returning to menu")
def SQLWriteDouble():
    # Open/create the file in write mode
    with open("SQLDoubleAttacks.txt", "a") as file:
        # Keep accepting input until the user enters "QUIT"
        while True:
            # Get input from the user
            user_input = input("Enter SQL command you wish to add (or 'QUIT' to exit): ")
            # If user_input is "QUIT", exit the loop
            if user_input.upper() == "QUIT":
                break
            # Write the input to the file
            file.write(user_input + "\n")
    print("Commands have been written to SQLDoubleAttacks.txt.")
    print("Returning to menu")

def SQLBatchWrite():
    # Open/create the file in write mode
    with open("SQLBatchAttacks.txt", "a") as file:
        # Keep accepting input until the user enters "QUIT"
        while True:
            # Get input from the user
            user_input = input("Enter SQL command you wish to add seperated by a ; (or 'QUIT' to exit): ")
            # If user_input is "QUIT", exit the loop
            if user_input.upper() == "QUIT":
                break
            # Write the input to the file
            file.write(user_input + "\n")
    print("Commands have been written to SQLBatchAttacks.txt.")
    print("Returning to menu")
def emailSubWrite():
    # Open/create the file  in write mode
    with open("EmailSubject.txt", "w") as file:
        # Get the subject line input from the user
        subject_line = input("Enter the email subject line (maximum 78 characters): ")
        # Truncate the subject line to 78 characters if it exceeds the limit
        if len(subject_line) > 78:
            print("Warning: Subject line exceeds 78 characters. It will be truncated.")
            subject_line = subject_line[:78]
        # Write the subject line to the file
        file.write(subject_line)
    print("Subject line has been written to EmailSubject.txt.")

def emailListWrite():
    # Open/create the file in write mode
    with open("EmailList.txt", "a") as file:
        # Keep accepting input until the user enters "QUIT"
        while True:
            # Get input from the user
            user_input = input("Enter email address you wish to add (or 'QUIT' to exit): ")
            # If user_input is "QUIT", exit the loop
            if user_input.upper() == "QUIT":
                break
            # Write the input to the file
            file.write(user_input + "\n")
    print("Email addresses have been written to EmailList.txt")
    print("Returning to menu")

def envWrite():
    # Open/create the file in write mode
    with open(".env", "w") as file:
        # Get user inputs
        userEmail = input("Enter your email: ")
        userPass = input("Enter your password: ")
        userPort = input("Enter your port: ")
        file.write(f"EMAILACC={userEmail}\n")
        file.write(f"EMAILPASS={userPass}\n")
        file.write(f"EMAILPORT={userPort}\n")
    print("Values have been written to .env")
    print("Returning to menu")
def emailContents():
    with open("EmailContents.txt", "w") as file:
        body = input("Enter email body: ")
        file.write(body)
    print("Email Contents have been written to EmailContents.txt")
def baitURL():
    with open("BaitURL.txt", "w") as file:
        bait = input("Enter your bait URL: ")
        file.write(bait)
    print("Bait URL has been written to BaitURL.txt")
    print("Please set up network security to track traffic to the bait URL.")
    print("Returning to menu")

#Running in global space for main, dont worry about it
print("Penetration Testing Tool File Setup")
# Set this so the menu can start
# essentially do while
userChoice = 1
#The menu and cycle
while userChoice != 0:
        print("Create or append which file?")
        print("1: SQLSingleAttacks.txt")
        print("2: SQLDoubleAttacks.txt")
        print("3: SQLBatchAttacks.txt")
        #print("4: .env file , use this for email account settings")
        #print("5: EmailSubject.txt")
        #print("6: EmailList.txt")
        #print("7: EmailContents.txt")
        #print("8: PhisingURL.txt")
        print("0: Exit Menu and End Program")
        userChoice = int(input("Please enter an integer: "))
        if userChoice == 1:
            SQLWrite()
        if userChoice == 2:
            SQLWriteDouble()
        if userChoice == 3:
            SQLBatchWrite()
        #if userChoice == 4:
        #    envWrite()
        #if userChoice == 5:
        #    emailSubWrite()
        #if userChoice == 6:
        #    emailListWrite()
        #if userChoice == 7:
        #if userChoice == 8:
        #    baitURL()