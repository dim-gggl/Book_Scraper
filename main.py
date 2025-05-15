import subprocess

def main():
    choice = input(
        "\n\n\n\n\n"
        f"{'From which source would you like to extract data from ?':^90}\n"
        f"{' ':5}{'1 - A single book':<30}\n"
        f"{' ':5}{'2 - A single category':<30}\n"
        f"{' ':5}{'3 - All the categories':<30}\n"
        f"{' ':5}{'4 - All categories + books covers':<30}\n"
        f"{' ':5}{'q - quit':<30}"
    ).strip().lower()
    match choice:
        case "1":
            subprocess.run(["python3", "scripts/phase_1.py"])
        case "2":
            subprocess.run(["python3", "scripts/phase_2.py"])
        case "3":
            subprocess.run(["python3", "scripts/phase_3.py"])
        case "4":
            subprocess.run(["python3", "scripts/phase_4.py"])
        case "q":
            print("Bye !")
        case _:
            print("Wrong input !")

if __name__ == '__main__':
    main()
