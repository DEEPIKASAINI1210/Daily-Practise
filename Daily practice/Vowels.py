#vowels
text=input("enter a word").upper()
count=0
for i in text:
    if i in "AEIOU":
        count+=1
print("Number of vowels:",count)