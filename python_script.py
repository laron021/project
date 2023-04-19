# import modules
import os
import sys
import subprocess
import shutil

#DECLARE COLORS
PURPLE = '\033[1;95m'
RED = '\033[1;31m'
BLUE = '\033[1;90m'
DBLUE = '\033[96m'
CYAN = '\033[1;92m'
ENDCOLOR = '\033[0m'


#Check if the current user is root
if os.geteuid() == 0:
    print(RED + 'You are running as root!' + ENDCOLOR)

else:
    print(RED + 'You need to be root to run this program. Exiting...' + ENDCOLOR)  #
    sys.exit(1)

#CHECK IF THE NECCESARRY PROGRAMS ARE INSTLLED
# Run the command and capture the output
result = subprocess.run("which nmap", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# Check if the command was successful (exit code 0)
if result.returncode == 0:
    pass
else:
    print("nmap is not installed. Install it with sudo apt install nmap")

#RUN AND SAVE
#folder_name = "my_reports"
#os.system(f"mkdir {folder_name}")

if not os.path.exists('my_reports'):
    os.makedirs('my_reports')

def run_and_save(command, output_file):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if the command was successful (exit code 0)
    if result.returncode == 0:
        # Display the output on the screen
        print(DBLUE + result.stdout.decode("utf-8") + ENDCOLOR)
        print(CYAN + 'SCAN PERFORMED SUCCESFULLY' + ENDCOLOR)  # green text

    else:
        print(RED + "Failed to run the command. Error message:" + ENDCOLOR)
        print(result.stderr.decode("utf-8"))

    saveit = input("save the result?(y/n): ")
    if saveit == 'y':
        # Save the output to a file in the specified folder
        output_path = os.path.join('my_reports', f"{output_file}.txt")
        with open(output_path, "w") as file:
            file.write(result.stdout.decode("utf-8"))
        print(RED + f'Command output has been saved to {output_path}!' + ENDCOLOR)

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


def install_docker():
    # Check if docker is installed
    if subprocess.run(['which', 'docker'], stdout=subprocess.PIPE).returncode == 0:
        print(RED+'Docker is already installed'+ENDCOLOR)
        return

    # Install docker
    subprocess.run(['sudo', 'apt', 'install', '-y', 'docker.io'])

    # Check if installation was successful
    if subprocess.run(['which', 'docker'], stdout=subprocess.PIPE).returncode == 0:
        print(RED+'Docker is installed!'+ENDCOLOR)
    else:
        print(RED+'Failed to install Docker'+ENDCOLOR)
        return


def download_zap_docker_image():
    # Check if OWASP Zap is already downloaded
    if subprocess.run(['docker', 'images', '-q', 'owasp/zap2docker-stable'], stdout=subprocess.PIPE).stdout.strip():
        print(RED+'OWASP Zap is available'+ENDCOLOR)
        return

    # Download OWASP Zap
    subprocess.run(['docker', 'pull', 'owasp/zap2docker-stable'])

    # Check if download was successful
    if subprocess.run(['docker', 'images', '-q', 'owasp/zap2docker-stable'], stdout=subprocess.PIPE).stdout.strip():
        print(RED+'OWASP Zap downloaded'+ENDCOLOR)
    else:
        print(RED+'Failed to download OWASP Zap'+ENDCOLOR)

#---------------------------------------------------------------------------
by = CYAN+'''          by laron'''+ENDCOLOR
print(RED+'''
     ____                                            
    |  _ \  _   _  _ __ ___   _ __ ___   _   _       
    | | | || | | || '_ ` _ \ | '_ ` _ \ | | | |      
    | |_| || |_| || | | | | || | | | | || |_| |      
    |____/  \__,_||_| |_| |_||_| |_| |_| \__, |      
                              ____       |___/       
                            / ___|   ___  __ _  _ __  ''' + ENDCOLOR)
print(by+RED + '''          \___ \  / __|/ _` || '_ \ 
                             ___) || (__| (_| || | | |
                            |____/  \___|\__,_||_| |_|        ''' + ENDCOLOR)

print(BLUE + '''
     _______________________________________ 
    |  ___________________________________  |
    | |     Information gathering and     | |
    | |    vulnerability scanning tool    | |
    | |           for dummies             | |
    | |___________________________________| |
    |_______________________________________|  
    ''' + ENDCOLOR)
# Display the menu to the user
def menu():
    #print(BLUE + '-------------------' + ENDCOLOR)
    print(BLUE + '1: OS guessing' + ENDCOLOR)
    print(BLUE+ '2: Check if host is up' + ENDCOLOR)
    print(BLUE + '3: Service and version detection' + ENDCOLOR)
    print(BLUE + '4: OWASP ZAP' + ENDCOLOR)
    print(BLUE + '5: OWASP Nettacker' + ENDCOLOR)
    print(DBLUE + '6: Remove program' + ENDCOLOR)
    print(BLUE + '7: DNS Enum' + ENDCOLOR)
    print(BLUE+ '8: Exit program' + ENDCOLOR)
    print(BLUE + '-------------------' + ENDCOLOR)

def option1():
    print("Option 1 selected")
    IPadress = input(f"{PURPLE}IP Address: {ENDCOLOR}")
    def nmap_os_scan(IPadress):
        command = ["sudo", "nmap", "-O","--fuzzy", f"{IPadress}"]
        result = subprocess.run(command, capture_output=True, text=True)
        output_lines = result.stdout.split("\n")
        os_detected = False
        for line in output_lines:
            if "Device type" in line:
                os_detected = True
            if os_detected:
                print(DBLUE + line + ENDCOLOR)

    nmap_os_scan(IPadress)

def option2():
    print("Option 2 selected")
    # Add code to execute option 2 here
    IPadress = input(f"{PURPLE}IP Address: {ENDCOLOR}")
    command = f"sudo hping3 -S -p 80,443,22,21,23 -c 1 {IPadress}"
    run_and_save(command,"Host_up_check:"+IPadress)


def option3():
    print("Option 3 selected")
    IPadress = input(f"{PURPLE}IP Address: {ENDCOLOR}")
    command = f"sudo nmap -sS -sV -T4 {IPadress}"
    run_and_save(command, "output11.txt")

def option4():
    print("Option 4 selected")
    # Add code to execute option 4 here
    def run_zap_scan(target_url):
        command = f'docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-full-scan.py -t {target_url} -g gen.conf -r REPORT_OWASP.html'
        subprocess.run(command, shell=True)

    install_docker()
    download_zap_docker_image()
    inp = input('URL: ')
    run_zap_scan(inp)

def option5():
    print("OWASP selected")
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

def option7():
    print("Option 7 selected")
    domain = input(f"{PURPLE} Domain/URL:{ENDCOLOR}")
    command = f"dnsenum -r {domain}"
    run_and_save(command, "output14.txt")

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
        option7()
    elif choice == "8":
        print(RED + 'Exiting...' + ENDCOLOR)
        break
    else:
        print("Invalid choice. Please try again.")
