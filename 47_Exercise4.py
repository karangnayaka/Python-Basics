# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode

st = input("Enter message")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding")
coding = True if (coding == "1") else False
print(coding)
#Coding Logic
if (coding):
    nwords = []
    for word in words:
        if (len(word) >= 3):
            r1 = "dsf"
            r2 = "jkr"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

#Decoding logic
else:
    nwords = []
    for word in words:
        if (len(word) >= 3):
            stnew = word[3:-3]    #word[3:-3] slices the string starting from the 4th character (word[3]) up to the 3rd character from the end (word[-3]). This effectively removes the first three characters and the last three characters from the word.
            stnew = stnew[-1] + stnew[:-1]   #stnew[-1] gets the last character of the modified stnew.
            nwords.append(stnew)              #stnew[:-1] gets all characters of stnew except the last one
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

