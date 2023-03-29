# Check if the current user is root
import os
import sys
import subprocess

PURPLE = '\033[1;95m'
RED = '\033[1;31m'
BLUE = '\033[1;90m'
CYAN = '\033[1;92m'
ENDCOLOR = '\033[0m'

#Check if the current user is root
if os.geteuid() == 0:
    print(RED + 'You are running as root!' + ENDCOLOR)

else:
    print(RED + 'You need to be root to run this program. Exiting...' + ENDCOLOR)  #
    sys.exit(1)

#CHECK IF THE NECCESARRY PROGRAMS ARE INSTLLED
# Define the command to check if gobuster is installed
command33 = "which nmap"
# Run the command and capture the output
result = subprocess.run(command33, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# Check if the command was successful (exit code 0)
if result.returncode == 0:
    print("nmap is installed!")
else:
    print("nmap is not installed. Install it with sudo apt install nmap")





print(BLUE + ''' 

██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝ 
         _______________________________________ 
        |  ___________________________________  |
        | | basic information gathering toool | |
        | |___________________________________| |
        |_______________________________________|
''' + ENDCOLOR)

def run_and_save(command, output_file):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if the command was successful (exit code 0)
    if result.returncode == 0:
        # Display the output on the screen
        print(result.stdout.decode("utf-8"))
        print(CYAN + 'SCAN PERFORMED SUCCESFULLY' + ENDCOLOR)  # green text

    else:
        print("Failed to run the command. Error message:")
        print(result.stderr.decode("utf-8"))

    saveit = input("save the result?(y/n): ")
    if saveit == 'y':
        # Save the output to a file
        with open(output_file, "w") as file:
            file.write(result.stdout.decode("utf-8"))
        print(RED + f'Command output has been saved to {output_file}.txt!' + ENDCOLOR)

    else:
        print(RED + 'Result not saved!' + ENDCOLOR)

# Display the menu to the user
def menu():
    #          bold, color
    print(BLUE + '1: Scan with nmap' + ENDCOLOR)  # dark cyan text
    print(BLUE+ '2: DNSRecon' + ENDCOLOR)  # dark cyan text
    print(BLUE + '3: IP a' + ENDCOLOR)  # dark cyan text
    print(BLUE + '4: Option four' + ENDCOLOR)  # dark cyan text
    print(BLUE + '5: Option five' + ENDCOLOR)  # dark cyan text
    print(BLUE + '6: Option six' + ENDCOLOR)  # dark cyan text
    print('\033[1;32m' + '7: Exit program' + ENDCOLOR)  # dark cyan text


def option1():
    print("Option 1 selected")
    # Add code to execute option 1 here
    IPadress = input("IP: ")
    command = 'nmap -p 80 -vv '+ IPadress
    run_and_save(command, "output9.txt")


def option2():
    print("Option 2 selected")
    # Add code to execute option 2 here
    IPadress = input("site name: ")
    command = 'dnsrecon -d ' + IPadress +' -t axfr'
    run_and_save(command,"output10.txt")


def option3():
    print("Option 3 selected")
    command = "ip a"
    run_and_save(command, "output11.txt")

def option4():
    print("Option 4 selected")
    # Add code to execute option 4 here

def option5():
    print("Option 5 selected")
    # Add code to execute option 5 here

def option6():
    print("Option 6 selected")
    # Add code to execute option 6 here






while True:
    menu()
    choice = input(f"{PURPLE}Enter your choice: {ENDCOLOR}")

    # Execute the selected option
    if choice == "1":
        option1()
    elif choice == "2":
        option2()
    elif choice == "3":
        option3()
    elif choice == "4":
        option4()
    elif choice == "5":
        option5()
    elif choice == "6":
        option6()
    elif choice == "7":
        print(RED + 'Exiting...' + ENDCOLOR)
        break
    else:
        print("Invalid choice. Please try again.")
