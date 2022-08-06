from pathlib import Path
from pprint import pprint

print(sorted(Path('.').glob('*.*')))


class File:
    @staticmethod
    def read_last_10_lines():
        with open(filename, mode="r", encoding="utf-8") as file:
            print(*(file.read().split("\n")[-10:]), sep='\n')

    @staticmethod
    def read_first_10_lines():
        with open(filename, mode="r", encoding="utf-8") as file:
            print(*(file.read().split("\n")[:11]), sep='\n')

    @staticmethod
    def read_all_file():
        with open(filename, mode="r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def find_longest_word():
        with open(filename, mode="r", encoding="utf-8") as file:
            words_in_text = file.read()
            words_in_text = words_in_text.replace(",", "")
            words_in_text = words_in_text.replace(".", "")

            max_len_word = words_in_text.split()
            return (f'Maximal len of word in file is: {max(max_len_word, key=len)}')

    @staticmethod
    def lines_number():
        with open(filename, mode="r", encoding="utf-8") as file:
            count = 0
            for _ in file:
                count += 1
            return (f"Total lines in file: {count}")

    @staticmethod
    def words_frequency():
        with open(filename, mode="r", encoding="utf-8") as file:
            words_in_text = file.read()
            words_in_text = words_in_text.replace(",", "")
            words_in_text = words_in_text.replace(".", "")

            counter_words = {}
            words = words_in_text.split()
            for word in words:
                if word.isalpha():
                    counter_words[word] = counter_words.get(word, 0) + 1
            return counter_words


if __name__ == "__main__":
    filename = input(f'Please enter file name to open: ')
    funcs = f'[a = read_last_10_lines / b = read_first_10_lines /\n c = read_all_file ' \
            f'/ d = findlongword / e = amountline / f = repeatwords / exit]'

    if Path(filename).exists():
        with open(filename, mode="r", encoding="utf-8") as file:
            print(f'Opening file with name: {filename}')
            if file:
                print()
                while True:
                    decision = input(f'What i should do: {funcs}: ')
                    if decision == "a":  # read_last_10_lines
                        File.read_last_10_lines()
                    elif decision == "b":  # read_first_10_lines
                        File.read_first_10_lines()
                    elif decision == "c":  # read_all_file
                        print(File.read_all_file())
                    elif decision == "d":  # findlongword
                        print(File.find_longest_word())
                    elif decision == "e":  # amountline
                        with open("text.txt", mode="r", encoding="utf-8") as file:
                            print(File.lines_number())
                    elif decision == "f":  # repeatwords
                        pprint(File.words_frequency())

                    elif decision == "exit":
                        print(f'see you')
                        break
    else:
        print(f'File not exist try again')
