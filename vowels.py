sentence = input("Sentence: ")

vowels = 0

for letter in sentence:
    if letter.lower() in "aeiou":
        vowels += 1

print("Vowels:", vowels)
