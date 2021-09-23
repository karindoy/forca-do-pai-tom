def main():
    word = input('Digite uma palavra para a forca: ')
    wordList = list(word)
    lettersFound = []

    wordLength = len(word)
    n_lettersFound = 0

    print('_______')
    print('|      |')
    print('|')
    print('|')
    print('|')
    print('|')
    print('|')

    while(n_lettersFound < len(word)):

        while(wordLength > 0):

            print('_ ', end='')
            lettersFound.append(" _ ")
            wordLength -= 1

        print()
        print()

        letter = input('Digite uma letra: ')

        indexLettersInWord = 0

        while indexLettersInWord < len(wordList):
            if wordList[indexLettersInWord] == letter:
                lettersFound[indexLettersInWord] = " " + letter + " "
                n_lettersFound += 1

            indexLettersInWord += 1
        wordFound = ''.join(lettersFound)
        print('_______')
        print('|      |')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')

        print(wordFound)


main()
