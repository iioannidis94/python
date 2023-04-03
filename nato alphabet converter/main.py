import pandas

#a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


#a list of the phonetic code words from a word that the user inputs.
e = True
while e:
    word = input("Enter a word: ").upper()
    try:
        output = [phonetic_dict[item] for item in word]
        e = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(output)


