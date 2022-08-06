from pathlib import Path
from pprint import pprint

print(sorted(Path('.').glob('*.*')))

filename = input(f'Please enter file name to open: ')

if __name__ == "__main__":
    funcs = f'[a = read_last_10_lines / b = read_first_10_lines /\n c = read_all_file ' \
            f'/ d = findlongword / e = amountline / f = repeatwords/exit]'

    if Path(filename).exists():
        with open(filename, mode="r", encoding="utf-8") as file:
            print(f'Opening file with name: {filename}')
            if file:
                print()
                while True:
                    decision = input(f'What i should do: {funcs}: ')
                    if decision == "a": # read_last_10_lines
                        with open("text.txt", mode="r", encoding="utf-8") as file:
                            print(*(file.read().split("\n")[-10:]), sep='\n')
                    elif decision == "b": # read_first_10_lines
                        with open("text.txt", mode="r", encoding="utf-8") as file:
                            print(*(file.read().split("\n")[:11]), sep='\n')
                    elif decision == "c": # read_all_file
                        with open("text.txt", mode="r", encoding="utf-8") as file:
                            print(file.read())
                    elif decision == "d": # findlongword
                        with open("text.txt", mode="r", encoding="utf-8") as file:
                            words_in_text = file.read()
                            words_in_text = words_in_text.replace(",", "")
                            words_in_text = words_in_text.replace(".", "")

                            max_len_word = words_in_text.split()
                            print(f'Maximal len of word in file is: {max(max_len_word, key=len)}')
                    elif decision == "e": # amountline
                        with open("text.txt", mode="r", encoding="utf-8") as file:
                            count = 0
                            for _ in file:
                                count += 1
                            print(f"Total lines in file: {count}")
                    elif decision == "f": #repeatwords
                        with open("text.txt", mode="r", encoding="utf-8") as file:
                            words_in_text = file.read()
                            words_in_text = words_in_text.replace(",", "")
                            words_in_text = words_in_text.replace(".", "")

                            counter_words = {}
                            words = words_in_text.split()
                            for word in words:
                                if word.isalpha():
                                    counter_words[word] = counter_words.get(word, 0) + 1
                            pprint(counter_words)

                    elif decision == "exit":
                        print(f'see you')
                        break
            else:
                print(f'File not exist try again')
