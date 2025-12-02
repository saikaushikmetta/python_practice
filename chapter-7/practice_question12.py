#write a funtion that takes a string and returns the count of vowels and consonants separately
vowels=['A', 'E', 'I', 'O', 'U']
consonants=['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
count1=0
count2=0
user=input("enter a string").upper()
for i in user:
    if i in vowels:
        count1+=1
    elif i in consonants:
        count2+=1
    else:
        print("enter valid string")
print("number vowels in the string",count1)
print("number of consonants in string",count2)