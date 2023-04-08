# import modules
import os
import sys
import subprocess
import shutil

#DECLARE COLORS
PURPLE = '\033[1;95m'
RED = '\033[1;31m'
BLUE = '\033[1;90m'
CYAN = '\033[1;92m'
LCYAN = '\033[1;32m'
ENDCOLOR = '\033[0m'

#Check if the current user is root
if os.geteuid() == 0:
    print(RED + 'You are running as root!' + ENDCOLOR)

else:
    print(RED + 'You need to be root to run this program. Exiting...' + ENDCOLOR)  #
    sys.exit(1)

#CHECK IF THE NECCESARRY PROGRAMS ARE INSTLLED
command33 = "which nmap"
# Run the command and capture the output
result = subprocess.run(command33, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# Check if the command was successful (exit code 0)
if result.returncode == 0:
    pass
else:
    print("nmap is not installed. Install it with sudo apt install nmap")


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

#OWASP NETTACKER
def install_owasp_nettacker():
    git_clone_command = ["git", "clone", "https://github.com/OWASP/Nettacker.git"]
    #nettacker_directory = "Nettacker"

    try:
        print(RED + "Cloning OWASP Nettacker from GitHub..." + ENDCOLOR)
        subprocess.check_output(git_clone_command)
        print(RED + "Cloning completed." + ENDCOLOR)
    except subprocess.CalledProcessError as e:
        print(RED + f"Error while cloning OWASP Nettacker: {e}" + ENDCOLOR)
        sys.exit(1)

    try:
        print(RED + "Installing OWASP Nettacker dependencies..." + ENDCOLOR)
        #os.chdir(nettacker_directory)
        #subprocess.check_output(["pip3", "install", "-r", "Nettacker/requirements.txt"])
        output = subprocess.run('pip3 install -r Nettacker/requirements.txt', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(output.stdout.decode("utf-8"))
        print(RED + "Installation completed." + ENDCOLOR)
    except subprocess.CalledProcessError as e:
        print(RED + f"Error while installing OWASP Nettacker dependencies: {e}" + ENDCOLOR)
        sys.exit(1)


def run_owasp_nettacker(target_ip):
    nettacker_script = "nettacker.py"
    command = f"python3 Nettacker/nettacker.py -i {target_ip} -m port_scan"

    try:
        print(BLUE + f"Starting OWASP Nettacker on target: {target_ip}" + ENDCOLOR)
        output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # output = subprocess.check_output(["python3 " nettacker_script + " -i " + target_ip + " -M" + " dir_scan"])
        print(BLUE + "OWASP Nettacker scan completed." + ENDCOLOR)
        print(output.stdout.decode("utf-8"))
    except subprocess.CalledProcessError as e:
        print(RED + f"Error while running OWASP Nettacker: {e}" + ENDCOLOR)
        sys.exit(1)

#---------------------------------------------------------------------------
print(BLUE + ''' 

██╗███╗   ██╗███████╗ ██████╗ ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
██║████╗  ██║██╔════╝██╔═══██╗██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
██║██╔██╗ ██║█████╗  ██║   ██║███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
██║██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                                                                          
                 _______________________________________ 
                |  ___________________________________  |
                | |     Information gathering and     | |
                | |    vulnerability scanning tool    | |
                | |             by laron              | |
                | |___________________________________| |
                |_______________________________________|
                

''' + ENDCOLOR)

# Display the menu to the user
def menu():
    print(CYAN + '-------------------' + ENDCOLOR)
    print(BLUE + '1: Scan with nmap' + ENDCOLOR)
    print(BLUE+ '2: DNSRecon' + ENDCOLOR)
    print(BLUE + '3: IP a' + ENDCOLOR)
    print(BLUE + '4: install requirements' + ENDCOLOR)
    print(BLUE + '5: OWASP Nettacker' + ENDCOLOR)
    print(BLUE + '6: Remove program' + ENDCOLOR)
    print(LCYAN+ '7: Exit program' + ENDCOLOR)
    print(CYAN + '-------------------' + ENDCOLOR)

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
    command = "pip install -r requirements.txt"
    run_and_save(command, "output11.txt")
    run_and_save("import requests", "output11.txt")

def option5():
    print("Option 5 selected")
    IPadress = input(f"{PURPLE}IP Address: {ENDCOLOR}")
    # Add code to execute option 5 here
    isExist = os.path.exists("Nettacker")

    if isExist == False:
        install_owasp_nettacker()
        run_owasp_nettacker(IPadress)

    else:
        print(RED + "OWASP Nettacker installed" + ENDCOLOR)
        run_owasp_nettacker(IPadress)


def option6():
    print("Option 6 selected")
    # get the directory where the script is located
    delete = input(f"{RED}Do you want to delete the program?(y/n): {ENDCOLOR}")
    if delete == 'y':
        print(RED + f'Deleting files...' + ENDCOLOR)
        dir_path = os.path.dirname(os.path.realpath(__file__))

        # delete all files and subdirectories in the directory
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path} due to {e}")

        # delete the script itself
        os.unlink(os.path.realpath(__file__))

    else:
        pass





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
