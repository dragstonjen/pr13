def simple_text_editor():
    filename = input("Введіть назву нового файлу (наприклад, 'test.txt'): ")
    print("Введіть текст. Щоб завершити — залиште порожній рядок.")
    
    with open(filename, 'w', encoding='utf-8') as file:
        while True:
            line = input()
            if line == "":
                break
            file.write(line + '\n')

    print("\nФайл збережено. Ось його вміст:")
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())


def analyze_file():
    filename = input("Введіть назву файлу для аналізу: ")
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("Файл не знайдено.")
        return

    lines = text.splitlines()
    words = text.split()
    characters = len(text)

    print("\nАналіз файлу:")
    print(f"Рядків: {len(lines)}")
    print(f"Слів: {len(words)}")
    print(f"Символів: {characters}")


def find_and_replace():
    filename = input("Введіть назву файлу для редагування: ")
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print("Файл не знайдено.")
        return

    old = input("Що замінити (слово або фраза): ")
    new = input("На що замінити: ")
    updated_content = content.replace(old, new)

    new_filename = input("Введіть назву нового файлу для збереження (наприклад, 'new_test.txt'): ")
    with open(new_filename, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print("Зміни збережено у новому файлі.")


# === Меню для запуску ===
def main():
    while True:
        print("\n=== Меню ===")
        print("1. Створити новий текстовий файл")
        print("2. Аналіз файлу")
        print("3. Пошук і заміна в тексті")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            simple_text_editor()
        elif choice == '2':
            analyze_file()
        elif choice == '3':
            find_and_replace()
        elif choice == '0':
            print("Завершення програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
