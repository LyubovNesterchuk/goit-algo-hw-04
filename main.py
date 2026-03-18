from pathlib import Path
from colorama import Fore
import sys


def parse_folder(path: Path):
    
    
    
    for element in path.iterdir():
        if element.is_dir():
            print(Fore.RED + f"{element.name}")
            parse_folder(element)
        elif element.is_file():
            print(Fore.GREEN + f"{element.name}")

    # for element in path.iterdir():
    #     if element.is_dir():
    #         print(Fore.RED + f"This is folder: {element.name}")
    #         parse_folder(element)
    #     elif element.is_file():
    #         print(Fore.GREEN + f"This is file: {element.name}")

if len(sys.argv) < 2:
    print("Будь ласка, вкажіть шлях до папки")
    sys.exit(1)

path = Path(sys.argv[1])

if not path.exists() or not path.is_dir():
    print("Вказаний шлях не існує або це не папка")
    sys.exit(1)

parse_folder(path) # в терміналі python main.py homework
