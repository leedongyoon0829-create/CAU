def count_vowel(text):
    count=0
    for i in text.lower():
        if i in "aeiou":
            count+=1
    return count
s=input("input string: ")
print(f"Number of vowles:{count_vowel(s)}")
