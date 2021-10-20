#!/usr/bin/python3

import time, os

banner = """

\033[1;32m
  ___ _  _ ___ _____ _   _    _    ___ _  _  ___ 
 |_ _| \| / __|_   _/_\ | |  | |  |_ _| \| |/ __|
  | || .` \__ \ | |/ _ \| |__| |__ | || .` | (_ |
 |___|_|\_|___/ |_/_/ \_\____|____|___|_|\_|\___|


"""
os.system("clear")
os.system("mv .ddosstart ddosstart")
print(banner)
os.system("cp ddosstart $HOME/../usr/bin")
os.system("mv ddosstart .ddosstart")
time.sleep(5.0)
print("\033[32m Installing Successfull !")
print("\033[32m Execute ddosstart command to start")
