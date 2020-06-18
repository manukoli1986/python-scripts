# PIG LATIN rules : 
# 1. If word starts with vowel, add 'ay' to end
# 2. If word does not start with a vowel, put the first letter at the end,
#    and then add 'ay' 

words = ["a","e","i","o","u"]

def latin_words(word):
    if word[0].lower() in "aeiou":
        return word+"ay"
    else:
        return word[1:]+word[0]+"ay"

# print(latin_words("mayank"))

chinetwork=["mayank", "himanshu","dev"]
print(list(map(latin_words,chinetwork)))

