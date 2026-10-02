sentence = input("Enter a sentence: ")

words = sentence.split()

number_of_words = len(words)
longest_word = max(words, key=len)
reverse_sentence = " ".join(words[::-1])

print("Number of words =", number_of_words)
print("Longest word =", longest_word)
print("Reverse word order =", reverse_sentence)