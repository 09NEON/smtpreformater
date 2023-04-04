import os
import time
from colorama import Fore, Style, Back
from concurrent.futures import ThreadPoolExecutor

start_time = time.time()
gr = '\033[32m'
bgr = '\033[107m'
wh = '\033[97m'
bl = '\033[34m'
Style = '\033[0m'

def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def v3(star):
    host = ''
    port = ''
    user = ''
    pwd = ''
    if "URL:" in star:
        star = fp.readline()
    if "METHOD:" in star:
        star = fp.readline()
    if "MAILHOST:" in star:
        star = star.replace(" ", "")
        star = star.replace('"', "")
        star = star.replace('\n', "")
        x = star.split(':', 1)
        host = x[1] + "|"
        star = fp.readline()
    if "MAILPORT:" in star:
        star = star.replace(" ", "")
        star = star.replace('"', "")
        star = star.replace('\n', "")
        x = star.split(':', 1)
        port = x[1] + "|"
        star = fp.readline()
    if "MAILUSER:" in star:
        star = star.replace(" ", "")
        star = star.replace('"', "")
        star = star.replace('\n', "")
        x = star.split(':', 1)
        user = x[1] + "|"
        star = fp.readline()
    if "MAILPASS:" in star:
        star = star.replace(" ", "")
        star = star.replace('"', "")
        star = star.replace("\n", "")
        x = star.split(':', 1)
        pwd = x[1]
        star = fp.readline()
    if "MAILFROM:" in star:
        star = fp.readline()
    if "FROMNAME:" in star:
        pass
    mrigel = open("Duplicated.txt", "a")
    mrigel.write(f'{host}{port}{user}{pwd}\n')
    mrigel.close()

def extract_data(input_file, output_file):
    with open(input_file, "r") as f:
        data = f.read().strip()

    sets = data.split("\nMAIL_HOST=")[1:]

    unique_sets = []
    for s in sets:
        lines = s.strip().split("\n")
        set_dict = {}
        for line in lines:
            parts = line.strip().split("=")
            if len(parts) == 2:
                key, value = parts
                set_dict[key] = value
        unique_sets.append(set_dict)

    with open(output_file, "w") as f:
        for s in unique_sets:
            username = s.get('MAIL_USERNAME', '')
            port = s.get('MAIL_PORT', '')
            from_address = s.get('MAIL_FROM_ADDRESS', '')
            password = s.get('MAIL_PASSWORD', '')
            from_name = s.get('MAIL_FROM_NAME', '')
            f.write(f"{username}|{port}|{from_address}|{password}|{from_name}\n")

def main():
    screen_clear()
    print(f"{'':^50}")
    print(f"{Fore.GREEN}{'':^50}")
    print(f"{Fore.GREEN}{'Starting...':^50}")
    print(f"{'':^50}")
    print(f"{Fore.WHITE}{'Created By 09NEON':^50}")
    print(f"{'':^50}")
    print(f"{Fore.RESET}{'https://t.me/ghost_store_logs':^50}")
    print(f"{'':^50}")

    input_path = input("Enter your input file path: ")
    if not os.path.isfile(input_path):
        print(f'Enter a valid .txt file in the same folder')
        return

    output_path = "successful.txt"
    extract_data(input_path, output_path)

    print(f"--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()