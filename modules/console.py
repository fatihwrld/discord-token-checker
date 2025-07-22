import os
import requests
import json
from colorama import Fore, Style, init
from pystyle import Colors, Colorate, Center
from datetime import datetime
from time import perf_counter, sleep

init(autoreset=True)

class Console:

    def __init__(self, token_count=0):
        self.token_count = token_count
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
[{datetime.now().strftime('%H:%M')}] Total {self.token_count} tokens found.

      """))


console = Console()
