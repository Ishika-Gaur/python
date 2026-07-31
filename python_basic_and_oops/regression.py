import re

text = "search inside of this please"

match = re.search("this", text)

print(match.span())

print(match.start())

print(match.end())

print(match.group())


# What is Regular Expression (Regex)?

# Regular Expression (Regex) ek special pattern hota hai jiska use hum text ya string me kuch search, match, validate ya replace karne ke liye karte hain.

# Regex bahut jyada information deta hai.

# Jaise

# ✔ kaha mila

# ✔ kitni baar mila

# ✔ kis position pe mila

# ✔ pattern match hua ya nahi

# ✔ replace bhi kar sakte hain

# Method	Kya karta hai?
# search()	String me kahin bhi search karta hai
# match()	Sirf beginning check karta hai
# fullmatch()	Puri string exactly match honi chahiye
# findall()	Saare matches return karta hai