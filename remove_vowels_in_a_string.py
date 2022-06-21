def vowel_list(char ):
    return char in ["a","e","i","o","u"]

def remove_vowels(word):
    
    non_vowel_string = ""
    for each_letter in word:
        if vowel_list(each_letter):
            continue
        non_vowel_string += each_letter
    return non_vowel_string

print(remove_vowels("sabarish"))
