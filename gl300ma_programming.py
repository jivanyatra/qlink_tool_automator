import pyautogui as pag
from time import sleep
import json
from sys import exit

scr_width, scr_height = pag.size()
ctr_x = scr_width/2
ctr_y = scr_height/2

buf_y = scr_height*0.15

focus_target = (ctr_x, ctr_y-buf_y)

old_app_shortcut = ['ctrl', 'alt', 'shift', '0']
new_app_shortcut = ['ctrl', 'alt', 'shift', '9']
app_load_time = 2


# example info moved externally to "sample_config.json"
# actual config expected in "config.json"
"""
#example info to be changed locally
url1 = ""
port1 = "10000"
password1 = "password1"
command1 = "AT+GTSRI={},4,,1,{url1},{port1},,0,,0,0,0,,,,FFFF$".format(password1, url1=url1, port1=port1)

ip2 = ""
port2 = "10002"
password2 = "password2"
command2 = "AT+GTDMS={},2,{},1,{ip2},{port2},,,120,7F9F,,0,,0,30,,FFFF$".format(password2, password2, ip2=ip2, port2=port2)
"""
path_to_cfg = "config.json"
break_list = ['quit', 'q', 'exit', 'x']

def build_config() -> None:
    """builds a default config from sample_config.json, or shows an error and builds a basic backup"""
    global path_to_cfg
    
    cfg = {}
    
    try:
        with open("sample_config.json") as f:
            cfg = json.load(f)
    except FileNotFoundError as e:
        print("sample_config.json not found; building config from scratch")
    
    if not cfg:
        cfg = {
            "load_times": {
                "old_tool": 4,
                "new_tool": 2
            },
            "key_delays": {
                "typing": 0.01,
                "old_enter": 1,
                "old_exit": 2,
                "new_enter": 1,
                "new_exit": 2
            },
            "tool_paths": {
                "old_tool": "",
                "new_tool": ""
            },
            "commands": {
                "old_cmd": "",
                "new_cmd": ""
            },
            "pw": {
                "old_pw": "",
                "new_pw": ""
            },
            "old_serv": {
                "url": "",
                "port": ""
            },
            "new_serv": {
                "ip": "",
                "port": ""
            }
        }
    try:
        with open(path_to_cfg, "w") as f:
            json.dump(cfg, f)
    except PermissionError:
        print("You do not have permission to write/edit files in this folder.")
        print("Try moving these files to a folder that you have permissions for.")
        i = input("Press the enter key to quit this application >")
        exit()

def load_config(path_to_cfg) -> dict:
    """loads a json config (calls a validate function) and returns a dict"""
    try:
        with open(path_to_cfg) as f:
            cfg = json.load(f)
    except FileNotFoundError:
        print("config not found, building config file")
        build_config()

    if not validate_config(cfg):
        print("Config Validation failed")
        return {}

def validate_config(cfg) -> bool:
    """checks config for empty or invalid values"""
    for section, values in cfg:
        for k, v in values:
            if not v:
                print("Invalid Config: Missing Parameters")
                return False
            if section == "load_times" or \ # ugly split line, but looks better in my IDE for now
               section == "key_delays":
                # I know this section isn't the most efficient; need to move these
                # checks so they don't occur every time
                if not isinstance(v, int) and not isinstance(v, float):
                    print("Invalid Config: times and delays must be int or float")
                    return False
    return True

def launch_enter_old_tool() -> None:
    """launches the old tool, enters the pw, and enters the program"""
    pag.hotkey(*old_app_shortcut)
    sleep(6)
    pag.click(focus_target)
    pag.hotkey('shift', 'tab')
    pag.hotkey('shift', 'tab')
    pag.hotkey('backspace')
    pag.typewrite(password1, 0.01)
    pag.typewrite(['tab', 'tab', 'space'], 0.05)
    sleep(2)

def program_old_tool() -> None:
    """launches raw programming window, programs unit, then closes old tool"""
    pag.hotkey('ctrl', 'l')
    sleep(0.5)
    pag.typewrite(command1, 0.01)
    pag.hotkey('enter')
    sleep(2)
    pag.hotkey('alt', 'f4')
    pag.hotkey('alt', 'f4')
    pag.hotkey('alt', 'f4')
#    sleep(1)

def launch_enter_new_tool() -> None:
    """launches the new tool, changes baud rate, and enters the program"""
    pag.hotkey(*new_app_shortcut)
    sleep(app_load_time+1)
    pag.click(focus_target)
    pag.hotkey('shift', 'tab')
    pag.hotkey('shift', 'tab')
    pag.hotkey('shift', 'tab')
    pag.hotkey('home')
    pag.typewrite(['tab', 'tab', 'tab', 'space'], 0.05)
    sleep(1)

def program_new_tool() -> None:
    """launches the raw programming window, programs unit, then closes the new tool"""
    pag.hotkey('ctrl', 'l')
    sleep(0.5)
    pag.typewrite(command2, 0.01)
    pag.hotkey('enter')
    sleep(2)
    pag.hotkey('alt', 'f4')
    pag.hotkey('alt', 'f4')
    sleep(1)

def preload() -> None:
    """Does the config loading"""
    cfg = load_config()
    if not cfg:

def main() -> None:
    
    # main loop
    while True:
        s = input("Enter (or q to quit) --> ")
        if s in break_list:
            break
        launch_enter_old_tool()
        program_old_tool()
        launch_enter_new_tool()
        program_new_tool()

if __name__ == "__main__":
    main()