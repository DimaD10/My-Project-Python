while(True):
    try:
        with open("text.txt") as src:

            empty = 0
            word = input("\nВведіть слово: ")
            list = src.read().split('\n')
            for a in list:
                for b in a.split():
                    if b.lower() == word.lower():
                        print("Абзац, в якоми присутнє введене слово: "+ a)
                        empty += 1
                        
            if empty == 0:
                print("Такого слова в тексті не знайдено.")
    except FileNotFoundError:
        print("\n<<< ERROR >>>\nФайлу не знайдено.") 
        break