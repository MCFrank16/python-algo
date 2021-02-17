def caesarCipherEncryptor(string, key):
    # Write your code here.
    newLetters = []
    newKey = key % 26
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey))
    return "".join(newLetters)

def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)


# def caesarCipherEncryptor(string, key):
#     newString = ""
#     for letter in string:
#         newLetter = ord(letter) + key
#         if newLetter <= 122:
#             newString += chr(newLetter)
#         else:
#             newString += chr(96 + newLetter % 122)
#     return newString

print(caesarCipherEncryptor('abc', 52))
