#import string
# from collections import Counter
# words = cleaned_text.split()
# word_count = len(words)
# print(f"Total words: {word_count}")
text = "beeravalli"
count_dict = {}
for char in text:
    if char in count_dict.keys():
        count_dict[char] += 1
    else:
        count_dict[char] = 1
print(count_dict)
# s = len(input("enter a string:").split())
# print(s)
