import os
import time
import getpass
os.system("clear")
print("\n \t\t\tWelcome to the Automating tool\n")
passwd = getpass.getpass("\n \t\t Please enter your password :\n")
def initial():
    os.system("clear")
    print("\n \t\t\tWelcome to the Automating tool\n")
    print("\n\t\t **---> Press <---**\n")
    time.sleep(1)
    print("\n\t  1 -> To work on RedHat Linux OS ")
    time.sleep(1)
    print("\n\t  2 -> To work on Docker Containers ")
    time.sleep(1)
    print("\n\t  3 -> To work on Hadoop Technology ")
    time.sleep(1)
    print("\n\t  4 -> To work on AWS cloud ")
    time.sleep(1)
    print("\n\t  5 -> To exit from the program ")
    time.sleep(1)
    print("\n\t  6 -> How to use this tool  ")
    return

if passwd != "kps":
    print("\n \t\t Authorization failed...\n ")
    time.sleep(1)
    print("\t\t Try Again..\n")
    time.sleep(1)
else :
    time.sleep(1)
    print("\n\t\t  Successfully logged in :-)")
    time.sleep(1)
#    initial()

    while True :
        initial()
        print("\n\t\t Enter your choice : ", end="")
        choice = int(input())
        print("\n\t\t\t Press enter to continue ....\n")
        input()

        if choice == 1 :
            print("\n\tLet us Work on RHEL8...\n")
            time.sleep(1)
            os.system("python3 /team-task/linux-script.py")
            print("\n\t\t\t Press enter to continue ....\n")
            input()
        elif choice == 2 :
            print("\n\tDocker container\n")
            time.sleep(1)
            print("\n\t\t\t Press enter to continue ....\n")
            input()
        elif choice == 3:
            print("\n\tHadoop Technology\n ")
            time.sleep(1)
            print("\n\t\t\t Press enter to continue ....\n")
            input()
        elif choice == 4:
            print("\n\t AWS cloud\n")
            time.sleep(1)
            print("\n\t\t\t Press enter to continue ....\n")
            input()
        elif choice == 5:
            print("\n\tBye Byee... going Offline\n")
            time.sleep(1)
            exit()
        elif choice == 6:
            print("\n\t Read the manual\n")
            print("\n\t\t\t Press enter to continue ....\n")
            input()
        else :
            print("\n\t Invalid Choice :(   Try Again")
            time.sleep(2)
            input()
