from pathlib import Path
from pprint import pprint
from string import punctuation
print(sorted(Path('.').glob('*.*')))


class File:
    @staticmethod
    def read_last_10_lines():
        print(*(file.read().split("\n")[-10:]), sep='\n')

    @staticmethod
    def read_first_10_lines():
        print(*(file.read().split("\n")[:11]), sep='\n')

    @staticmethod
    def read_all_file():
        return file.read()

    @staticmethod
    def find_longest_word():
        words_in_text = file.read()
        for punc in punctuation:
            if punc in words_in_text:
                words_in_text = words_in_text.replace(punc, "")
        max_len_word = words_in_text.split()
        return f'Maximal len of word in file is: {max(max_len_word, key=len)}'

    @staticmethod
    def lines_number():
        count = 0
        for _ in file:
            count += 1
        return f"Total lines in file: {count}"

    @staticmethod
    def words_frequency():
        words_in_text = file.read()
        for punc in punctuation:
            if punc in words_in_text:
                words_in_text = words_in_text.replace(punc, "")
        counter_words = {}
        words = words_in_text.split()
        for word in words:
            if word.isalpha():
                counter_words[word] = counter_words.get(word, 0) + 1
        return counter_words

    @staticmethod
    def move_to_start():
        file.seek(0)


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
                        File.move_to_start()
                    elif decision == "b":  # read_first_10_lines
                        File.read_first_10_lines()
                        File.move_to_start()
                    elif decision == "c":  # read_all_file
                        print(File.read_all_file())
                        File.move_to_start()
                    elif decision == "d":  # findlongword
                        print(File.find_longest_word())
                        File.move_to_start()
                    elif decision == "e":  # amountline
                        print(File.lines_number())
                        File.move_to_start()
                    elif decision == "f":  # repeatwords
                        pprint(File.words_frequency())
                        File.move_to_start()

                    elif decision == "exit":
                        print(f'see you')
                        break
    else:
        print(f'File not exist try again')
