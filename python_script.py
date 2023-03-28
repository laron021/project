# Check if the current user is root
import os
import sys
import subprocess

PURPLE = '\033[1;95m'
RED1 = '\033[1;31m'
RED2 = '\033[0m'
BLUE1 = '\033[1;90m'
BLUE2 = '\033[0m'

#Check if the current user is root
if os.geteuid() == 0:
    print(RED1 + 'You are running as root!' + RED2)

else:
    print('\033[1;31m' + 'You need to be root to run this program. Exiting...' + '\033[0m')  # green text
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
    print("nmap is not installed. Install it with sudo apt install gobuster")





print(BLUE1 + ''' 

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
''' + BLUE2)  # green text

def menu():
    #          bold, color
    print('\033[1;90m' + '1: Scan with nmap' + '\033[0m')  # dark cyan text
    print('\033[1;90m' + '2: DNSRecon' + '\033[0m')  # dark cyan text
    print('\033[1;90m' + '3: IP a' + '\033[0m')  # dark cyan text
    print('\033[1;90m' + '4: Option four' + '\033[0m')  # dark cyan text
    print('\033[1;90m' + '5: Option five' + '\033[0m')  # dark cyan text
    print('\033[1;90m' + '6: Option six' + '\033[0m')  # dark cyan text
    print('\033[1;32m' + '7: Exit program' + '\033[0m')  # dark cyan text

def save_command_output_to_file(command, output_file):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if the command was successful (exit code 0)
    if result.returncode == 0:
        # Display the output on the screen
        print(result.stdout.decode("utf-8"))
        print('\033[1;92m' + 'SCAN PERFORMED SUCCESFULLY' + '\033[0m')  # green text

    else:
        print("Failed to run the command. Error message:")
        print(result.stderr.decode("utf-8"))

    saveit = input("save the result?(y/n): ")
    if saveit == 'y':
        # Save the output to a file
        with open(output_file, "w") as file:
            file.write(result.stdout.decode("utf-8"))
        print('\033[1;31m' + f'Command output has been saved to {output_file}.txt!' + '\033[0m')

    else:
        print('\033[1;31m' + 'Result not saved!' + '\033[0m')

def option1():
    print("Option 1 selected")
    # Add code to execute option 1 here
    #command = "nmap -p 80 192.168.0.109"
    IPadress = input("IP: ")
    command = 'nmap -p 80 -vv '+ IPadress
    save_command_output_to_file(command, "output9.txt")


def option2():
    print("Option 2 selected")
    # Add code to execute option 2 here
    IPadress = input("site name: ")
    command = 'dnsrecon -d ' + IPadress +' -t axfr'
    save_command_output_to_file(command,"output10.txt")


def option3():
    print("Option 3 selected")
    command = "ip a"
    save_command_output_to_file(command, "output11.txt")

def option4():
    print("Option 4 selected")
    # Add code to execute option 4 here

def option5():
    print("Option 5 selected")
    # Add code to execute option 5 here

def option6():
    print("Option 6 selected")
    # Add code to execute option 6 here




# Display the menu to the user

while True:
    menu()
    choice = input(f"{PURPLE}Enter your choice: ")

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
        print('\033[1;31m' + 'Exiting...' + '\033[0m')
        break
    else:
        print("Invalid choice. Please try again.")
