import string


class AlphabetIterator:
    def __init__(self, letter: str):
        self.letter = letter
        self.letters = AlphabetIterator.LowerOrUpper(self)
        self.end = 26

    def LowerOrUpper(self):
        if self.letter.islower():
            letters = list(string.ascii_lowercase)
        else:
            letters = list(string.ascii_uppercase)
        return letters

    def get_letters(self):
        return self.letters

    def __iter__(self):
        for i, l in enumerate(self.letters):
            if l == self.letter:
                self.counter = i
        return self

    def __next__(self):
        if self.counter == self.end:
            raise StopIteration()
        curr = self.letters[self.counter]
        self.counter += 1
        return curr


if __name__ == '__main__':
    while True:
        try:
            my_letter = input("insert a letter from the English alphabet or $ to exit: ")
            if my_letter == "$":
                break
            my_letters = AlphabetIterator(my_letter)
            a = AlphabetIterator('f')
            for letter in my_letters:
                print(letter)
            continue
        except ValueError:
            print('The input is incorrect')
        except Exception as e:
            print(e)
        finally:
            print("\n")
            pass
