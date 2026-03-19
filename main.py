from pathlib import Path
from colorama import Fore, init
import sys

init(autoreset=True)


def parse_folder(path: Path, level=0):
    indent = "    " * level  # 4 пробіли на рівень

    for element in path.iterdir():
        if element.is_dir():
            print(Fore.RED + f"{indent}📂 {element.name}")
            parse_folder(element, level + 1)
        elif element.is_file():
            print(Fore.GREEN + f"{indent}📄 {element.name}")


def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до папки")
        return

    path = Path(sys.argv[1])

    if not path.is_dir():
        print("Це не папка")
        return

    print(Fore.YELLOW + f"📁 {path.name}")
    parse_folder(path)


if __name__ == "__main__":
    main()


# cd ~/Desktop/Projects/goit-algo-hw-04
# python main.py homework
