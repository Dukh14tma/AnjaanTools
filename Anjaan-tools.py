#!bin/python
import os
import sys
import subprocess
#from colorama import Fore, Style


#Colors Defines
Green = "\33[1;32;40m"
Red = "\33[1;31;40m"
Yellow = "\33[1;33;40m"
Cyan = "\33[1;36;40m"

#Logo Code Here
def logo():
    print(f"""{Cyan} _______  _       _________ _______  _______  _           _________ _______  _______  _        _______
(  ___  )( (    /|\__    _/(  ___  )(  ___  )( (    /|    \__   __/(  ___  )(  ___  )( \      (  ____ \\
| (   ) ||  \  ( |   )  (  | (   ) || (   ) ||  \  ( |       ) (   | (   ) || (   ) || (      | (    \/
| (___) ||   \ | |   |  |  | (___) || (___) ||   \ | | _____ | |   | |   | || |   | || |      | (_____
|  ___  || (\ \) |   |  |  |  ___  ||  ___  || (\ \) |(_____)| |   | |   | || |   | || |      (_____  )
| (   ) || | \   |   |  |  | (   ) || (   ) || | \   |       | |   | |   | || |   | || |            ) |
| )   ( || )  \  ||\_)  )  | )   ( || )   ( || )  \  |       | |   | (___) || (___) || (____/\\______) |
|/     \||/    )_)(____/   |/     \||/     \||/    )_)       )_(   (_______)(_______)(_______/\\_______)
                                                                                                       """)

def update():
    """Updates the tool from the git repo."""
    cls()
    logo()
    Authour()
    print(f"{Yellow}Update Tool")
    print("")
    print("This will update the tool from the git repo.")
    print("Any changes made to the tool will be overwritten.")
    os.system("sleep 2")
    print("")
    print("Are you sure you want to update the tool?")
    ans = input("[Y/N] ").lower()
    if ans == "y":
        subprocess.run(["git", "pull"])
        print("Tool updated successfully!")
        os.system("sleep 2")
    else:
        print("Update cancelled.")


def Main_Menu():
    """The main menu of the tool."""
    while True:
        cls()
        logo()
        Authour()
        print(f"{Green}Main Menu")
        print("")
        print("[1]. Programming Languages")
        print("[2]. Web Hacking Tools")
        print("[3]. Vulnerability Scanner Tools")
        print("[4]. Hash Breaking Tools")
        print("[5]. DDos tool")
        print("[6]. Update Tool")
        print("[0]. Exit")
        print("")
        print("")
        opt = int(input("Enter your option: "))
        if opt == 1:
            Program_Lang()
        elif opt == 2:
            web_hacking()
        elif opt == 3:
            Vuln_Scan()
        elif opt == 4:
            Hash_Break()
        elif opt == 5:
            DDos()
        elif opt == 6:
            update()
        elif opt == 0:
            print("Exiting the program...")
            exit()
        else:
            print("Invalid option!")


#Adding Creator Details
def Authour():
    print(f"{Yellow}{101*'='}")
    print(f"{39* '='} Created By: Dukh14tma {39* '='}")
    print(f"{38 * '='}    Version: Beta 0.2    {38* '='}")

#Screen Clear Function
def cls():
    if sys.platform.startswith('win'):
        subproicess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)

#DDos code
def DDos():
    cls()
    logo()
    Authour()
    print("DDos")
# installing code here
def install_package(pkg):
    try:
        q1 = input("You want to install this [Y/N]: ").lower()
        if q1 == "y":
            q2 = input("Are you sure you want install this [Y/N]: ").lower()
            if q2 == "y" or q2 == "Y":
                q3 = input("So if you install this it means you know how to make programs in this language [Y/N]").lower()
                if q3 == "Y" or q3 == "y":
                    q4 = input("Verify: Are you human [Y/N]").lower
                    if q4 == "y" or q4 =="Y":
                         q5 = input("Ok one last question [OK/NO]" ).lower()
                         if q5 == "ok" or q5=="y":
                             q6 = input("Are You Really sure to install this [Y/N]").lower()
                             if q6 == "y":
                                 print("")
                                 print("Ok! I'm installing this because you incest me")
                                 print("Wait few second")                                                                                
                                 os.system(f"apt install {pkg} -y 2> /dev/null")
                                 os.system("sleep 3")
                                 print(f"{Green}Successfully Installed {pkg}")
                             else:
                                 print("Please! Don't be angry i am just asking you")
                                 print("OK i'll install this for you")                                                                   
                                 os.system(f"apt install {pkg} -y 2> /dev/null")
                                 os.system("sleep 3")
                                 print(f"{Green}Successfully Installed {pkg}")
                         else:
                             q7 = input("But i have only one last question[Ok/No] ").lower()
                             if q7 == "ok" or q7=="y":
                                 q8 = input("Are You Really sure to install this [Y/N]").lower()
                                 if q8 == "y":
                                     print()
                                     print("Ok! I'm installing this because you incest me")
                                     print("Wait few second")
                                     os.system("sleep 3")
                                     os.system(f"apt install {pkg} -y 2> /dev/null")
                                     os.system("sleep 3")
                                     print(f"{Green}Successfully Installed {pkg}")
                                 else:
                                     print("Please! Don't be angry i am just asking you")
                                     print("OK i'll install this for you")
                                     os.system(f"apt install {pkg} -y 2> /dev/null")
                                     os.system("sleep 3")
                                     print(f"{Green}Successfully Installed {pkg}")
                             else:
                                 print("Please! Don't be angry i am just asking you")
                                 print("OK i'll install this for you")
                                 os.system(f"apt install {pkg} -y 2> /dev/null")
                                 os.system("sleep 3")
                                 print(f"{Green}Successfully Installed {pkg}")
                    else:
                        
                        print("Please! Don't be angry i am just asking you")
                        print("OK i'll install this for you")
                        os.system(f"apt install {pkg} -y 2> /dev/null")
                        os.system("sleep 3")
                        print(f"{Green}Successfully Installed {pkg}")
                else:
                    
                    print("OK i'll install this for you")
                    os.system(f"apt install {pkg} -y 2> /dev/null")
                    os.system("sleep 3")
                    print(f"{Green}Successfully Installed {pkg}")
            else:
                print("Oh! you don't you want to install this")
                print("ok going back to Main Menu")
                os.system("sleep 3")
                Main_Menu()
        else:
            print("Oh! you don't you want to install this")
            print("ok going back to Main Menu")
            os.system("sleep 3")
            Main_Menu()
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {pkg}. Error Occured")



#Programming language code here

def Program_Lang():
    cls()
    logo()
    Authour()
    print(f"{Green}Programming Languages")
    print
    print(f"""1.  C/C++
2.  Crystal
3.  Dart
4.  Elixir
5.  Erlang
6.  Forth
7.  Go
8.  Groovy
9.  Blade
10. Java
11. JavaScrip
12. Kotlin
13. Lua54
14. Nim
15. Swift
16. Tcl
17. Perl
18. PHP
19. Picolisp
20. JQuery
21. Python
22. Racket
23. Ruby
""")
    print("")
    print("")
    Opt = int(input("Enter Your Option: "))

    if Opt == 1:
        pkg = "clang"
        install_package(pkg)
    elif Opt == 2:
        pkg = "crystal"
        install_package(pkg)
    elif Opt == 3:
        pkg = "dart"
        install_package(pkg)
    elif Opt == 4:
        pkg = "elixir"
        install_package(pkg)
    elif Opt == 5:
        pkg = "erlang"
        install_package(pkg)
    elif Opt == 6:
        pkg = "pforth"
        install_package(pkg)
    elif Opt == 7:
        pkg = "golang"
        install_package(pkg)
    elif Opt == 8:
        pkg = "groovy"
        install_package(pkg)
    elif Opt == 9:
        pkg = "blade"
        install_package(pkg)
    elif Opt == 10:
        pkg = "openjdk-17"
        install_package(pkg)
    elif Opt == "node.js":
        pkg = "d"
        install_package(pkg)
    elif Opt == 12:
        pkg = "kotlin"
        install_package(pkg)
    elif Opt == 13:
        pkg = "lua54"
        install_package(pkg)
    elif Opt == 14:
        pkg = "nim"
        install_package(pkg)
    elif Opt == 15:
        pkg = "swift"
        install_package(pkg)
    elif Opt == 16:
        pkg = "tcl"
        install_package(pkg)
    elif Opt == 17:
        pkg = "perl"
        install_package(pkg)
    elif Opt == 18:
        pkg = "php"
        install_package(pkg)
    elif Opt == 19:
        pkg = "picolisp"
        install_package(pkg)
    elif Opt == 20:
        pkg = "jql"
        install_package(pkg)
    elif Opt == 21:
        pkg = "python3"
        install_package(pkg)
    elif Opt == 22:
        pkg = "racket"
        install_package(pkg)
    elif Opt == 23:
    	pkg = "ruby"
    	install_package(pkg)
    else:
        print("You Enter Worng option")
        Program_lang()

#Web Hacking Tools Code
def Web_hacking():
    cls()
    logo()
    Authour()
    print(f"{Green}Web Hacking Tools")
    print(f"{Yellow}The developer didn't write this code Because he is lazy")
    print("Maybe he write some day until you can enjoy by choosing another option")
    os.system("sleep 5")
    Main_Menu()

#Vulnerability Scanning tools
def Vuln_Scan():
    cls()
    logo()
    Authour()
    print(f"{Green}Vulnerability Scanning Tools")
    print(f"{Yellow}The developer didn't write this code Because he is lazy")
    print("Maybe he write some day until you can enjoy by choosing another option")
    os.system("sleep 5")
    Main_Menu()

#Hash Breaking Tools
def Hash_Break():
    cls()
    logo()
    Authour()
    print(f"{Green}Hash Breaking Tools")
    print(f"{Yellow}The developer didn't write this code Because he is lazy")
    print("Maybe he write some day until you can enjoy by choosing another option")
    os.system("sleep 5")
    Main_Menu()

#Main Menu Code is Here


try:
    Main_Menu()

except KeyboardInterrupt:
    print(f"{Red}Program Is Clossing now")
except ValueError:
    print(f"{Red}Wrong Option Closing the Program")
 
