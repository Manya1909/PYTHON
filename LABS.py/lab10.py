sentence = input("Enter a sentence: ")

position = int(input("Enter position for indexing: "))
print("Character at position", position, ":", sentence[position])

start = int(input("Enter start index for slicing : "))
end = int(input("Enter end index for slicing   : "))
print("Sliced string:", sentence[start:end])

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())

old_word = input("Enter word to replace: ")
new_word = input("Enter replacement word: ")
print("After replace:", sentence.replace(old_word, new_word))

print("Length of sentence:", len(sentence))