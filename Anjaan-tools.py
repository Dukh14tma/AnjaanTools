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

logo()

# main menu code
def Main_Menu():
    cls()
    print(f"{Yellow}This tool is in under development ")
    print("So maybe few tools didn't work have a good day")
    os.system("sleep 3")
    cls()
    logo()
    Authour()
    print("")
    print(f"{Red}This tool is in development stage")
    print(f"{Green}[1]. Programming Languages")
    print(f"[2]. Web Hacking Tools")
    print(f"[3]. Vulnerability Scanner Tools")
    print(f"[4]. Hash Breaking Tools")
    print(f"[0]. Exit")
    print("")
    print("")
    Opt = int(input("Enter Your Option: "))

    if Opt==1:
        Program_Lang()
    elif Opt==2:
        Web_hacking()
    elif Opt==3:
        Vuln_Scan()
    elif Opt==4:
        Hash_Break()
    elif Opt==0:
        print(f"{Red}Exiting the program")
        exit()
    elif Opt=="":
        print("{Red}Enter somthimg")
        Main_Menu()
    else:
        print(f"{Red}Please choose from an options")
        Main_Menu()


#Adding Creator Details
def Authour():
    print(f"{Yellow}{101*'='}")
    print(f"{41* '='} Created By: 4njaan {40* '='}")
    print(f"{38 * '='}    Version: Beta 0.1    {38* '='}")

#Screen Clear Function
def cls():
    if sys.platform.startswith('win'):
        subproicess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)


# installing code here
def install_package(pkg):
    try:
        q1 = input("You want to install this [Y/N]: ").lower()
   85         if q1 == "y":
~  86             q2 = input("Are you sure you want install this [Y/N]: ").lower()
   87             if q2 == "y" or q2 == "Y":
~  88                 q3 = input("So if you install this it means you know how to make programs in this language [Y/N]").lower()
   89                 if q3 == "Y" or q3 == "y":
~  90                     q4 = input("Verify: Are you human [Y/N]").lower
   91                     if q4 == "y" or q4 =="Y":
   92                         q5 = input("Ok one last question [OK/NO]" ).lower()
~  93                         if q5 == "ok" or q5=="y":
   94                             q6 = input("Are You Really sure to install this [Y/N]").lower()
   95                             if q6 == "y":
   96                                 print("")
   97                                 print("Ok! I'm installing this because you incest me")
   98                                 print("Wait few second")                                                                                ~  99                                 os.system(f"apt install {pkg} -y 2> /dev/null")
  100                                 os.system("sleep 3")
  101                                 print(f"{Green}Successfully Installed {pkg}")
  102                             else:
  103                                 print("Please! Don't be angry i am just asking you")
  104                                 print("OK i'll install this for you")                                                                   ~ 105                                 os.system(f"apt install {pkg} -y 2> /dev/null")
  106                                 os.system("sleep 3")
  107                                 print(f"{Green}Successfully Installed {pkg}")
  108                         else:
  109                             q7 = input("But i have only one last question[Ok/No] ").lower()
~ 110                             if q7 == "ok" or q7=="y":
  111                                 q8 = input("Are You Really sure to install this [Y/N]").lower(
  112                                 if q8 == "y":
  113                                     print()
  114                                     print("Ok! I'm installing this because you incest me")
  115                                     print("Wait few second")
  116                                     os.system("sleep 3")
~ 117                                     os.system(f"apt install {pkg} -y 2> /dev/null")
  118                                     os.system("sleep 3")
  119                                     print(f"{Green}Successfully Installed {pkg}")
  120                                 else:
  121                                     print("Please! Don't be angry i am just asking you")
  122                                     print("OK i'll install this for you")
~ 123                                     os.system(f"apt install {pkg} -y 2> /dev/null")
  124                                     os.system("sleep 3")
  125                                     print(f"{Green}Successfully Installed {pkg}")
  126                             else:
  127                                 print("Please! Don't be angry i am just asking you")
  128                                 print("OK i'll install this for you")
~ 129                                 os.system(f"apt install {pkg} -y 2> /dev/null")
  130                                 os.system("sleep 3")
  131                                 print(f"{Green}Successfully Installed {pkg}")
  132                     else:
  133                         print("Please! Don't be angry i am just asking you")
  134                         print("OK i'll install this for you")
~ 135                         os.system(f"apt install {pkg} -y 2> /dev/null")
  136                         os.system("sleep 3")
  137                         print(f"{Green}Successfully Installed {pkg}")
  138                 else:
  139                     print("OK i'll install this for you")
~ 140                     os.system(f"apt install {pkg} -y 2> /dev/null")
  141                     os.system("sleep 3")
  142                     print(f"{Green}Successfully Installed {pkg}")
  143             else:
  144                 print("Oh! you don't you want to install this")
  145                 print("ok going back to Main Menu")
  146                 os.system("sleep 3")
  147                 Main_Menu()
  148         else:
  149             print("Oh! you don't you want to install this")
  150             print("ok going back to Main Menu")
  151             os.system("sleep 3")
  152             Main_Menu()
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
        pkg = "jdk-17"
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
 
