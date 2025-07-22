import os
import requests
import json
from colorama import Fore, Style, init
from pystyle import Colors, Colorate, Center
from datetime import datetime
from time import perf_counter, sleep

with open("token.txt", "r") as file:
    tokens = [line.strip() for line in file if line.strip()]
init(autoreset=True)

class Console:

    def __init__(self):
        self.show_banner()
    
    def show_banner(self):
        print(Colorate.Horizontal(Colors.white_to_blue, rf"""


 _                       
| |                      
| |_ __ ___   __ _  ___  
| | '_ ` _ \ / _` |/ _ \ 
| | | | | | | (_| | (_) |
|_|_| |_| |_|\__,_|\___/ 
                                                  
Made by github.com/fatihwrld
[{datetime.now().strftime('%H:%M')}] Total {len(tokens)} tokens found.

      """))


console = Console()