import requests
from colorama import Fore, Style, init
from pystyle import Colors, Colorate
from datetime import datetime
from modules.console import console

init(autoreset=True)

with open("token.txt", "r") as file:
    tokens = [line.strip() for line in file if line.strip()]

class TokenChecker:
    def __init__(self):
        self.console = console
        self.api_url = "https://discord.com/api/v9"

    def check_token(self):
        for token in tokens:
            headers = {
                "Authorization": token
            }
                        
            try:
                response = requests.get(f"{self.api_url}/users/@me", headers=headers)

                if response.status_code == 200:
                    user_data = response.json()

                    valid_info = [
                        Colorate.Horizontal(Colors.white_to_blue, f"[{datetime.now().strftime('%H:%M')}]"),
                        Colorate.Horizontal(Colors.green_to_white, "Token Valid"),
                        Colorate.Horizontal(Colors.green_to_yellow, f"Username: {user_data['username']}"),
                        Colorate.Horizontal(Colors.green_to_white, f"Email: {user_data['email']}"),
                        Colorate.Horizontal(Colors.green_to_yellow, f"Verified: {user_data['verified']}"),
                        Colorate.Horizontal(Colors.white_to_blue, f"[{token.split('.')[0]}]")
                    ]
                    
                    print("  |  ".join(valid_info))
                    with open("valid.txt", "a") as f:
                        f.write(f"{token}\n")

                else:
                    invalid_info = [
                        Colorate.Horizontal(Colors.white_to_blue, f"[{datetime.now().strftime('%H:%M')}]"),
                        Colorate.Horizontal(Colors.red_to_white, "Token Invalid"),
                        Colorate.Horizontal(Colors.red_to_yellow, f"Status: {response.status_code}"),
                        Colorate.Horizontal(Colors.white_to_blue, f"[{token.split('.')[0]}]")
                    ]
                    print("  |  ".join(invalid_info))
                    with open("invalid.txt", "a") as f:
                        f.write(f"{token}\n")


            except Exception as e:
                print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    token_checker = TokenChecker()
    token_checker.check_token()