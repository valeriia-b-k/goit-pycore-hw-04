import sys
from pathlib import Path
from colorama import Fore, Style, init


def directory_structure(path: Path, indent: str = ""):
    try:
        for el in path.iterdir():
            if el.is_dir():
                print(f"{indent}{Fore.BLUE}{el.name}/")
                directory_structure(el, indent + "  ")
            else:
                print(f"{indent}{Fore.GREEN}{el.name}")
    except Exception as e:
        print(f"{indent}{Fore.RED}Error reading {path}: {e}")

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "❌ Помилка: необхідно вказати шлях до директорії як аргумент.")
        print("📌 Приклад використання: C:/Projects/vscode-basics/goit-pycore-hw-04/picture")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(Fore.RED + f"❌ Шлях не існує: {directory_path}")
        sys.exit(1)
    elif not directory_path.is_dir():
        print(Fore.RED + f"❌ Вказаний шлях не є директорією: {directory_path}")
        sys.exit(1)

    print(Fore.YELLOW + f"📂 Вміст директорії: {directory_path}\n")
    directory_structure(directory_path)

if __name__ == "__main__":
    sys.argv = ["goit-pycore-hw-04_3.py", "C:/Projects/vscode-basics/goit-pycore-hw-04/picture"]
    main()