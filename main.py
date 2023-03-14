import requests
import ctypes, os
blocklist = requests.get("https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts").text

try:
    with open("C:\Windows\System32\drivers\etc\hosts", "a") as file:
        file.write("\n" + blocklist)
    print("Successfully blocked Ads & Malaware")
except:
    print("Failed to write to hosts file, please make sure you run this script as admin")
