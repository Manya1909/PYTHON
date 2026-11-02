
sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"

words = len(sentence.split())
vowel_count = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in sentence:
    if ch in vowels:
        vowel_count += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

letters = vowel_count + consonants

if letters > 0:
    percentage = (vowel_count / letters) * 100
else:
    percentage = 0

print("DOCUMENT ANALYSIS REPORT")
print("Sentence:", sentence)
print("Total characters:", len(sentence))

print("Character Breakdown")
print("Words:", words)
print("Vowels:", vowel_count)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

print("Summary")
print("Total letters:", letters)
print("Vowel percentage:", round(percentage, 1), "%")

print("Analysis Complete!")
