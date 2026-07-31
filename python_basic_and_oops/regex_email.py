import re

pattern = re.compile(
    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
)

email = "john@gmail.com"

if pattern.fullmatch(email):
    print("Valid Email")
else:
    print("Invalid Email")


#     Email validation ke liye Regex kyu use karte hain?

# Taaki galat format wale emails ko reject kiya ja sake aur sirf valid emails hi accept hon.

# Q3 ^ aur $ ka kya use hai?
# ^ → String ki beginning.
# $ → String ka end.

# Dono milkar ensure karte hain ki poori string pattern follow kare.

# Q4 Dot (.) ko \. kyu likhte hain?

# Kyuki Regex me . ka matlab "koi bhi ek character" hota hai. Actual dot match karne ke liye usse escape (\.) karna padta hai.



# Regex ka sabse common real-world use input validation hai.
# Email validation ke liye generally fullmatch() use karna better hota hai.
# ^ string ki beginning aur $ string ke end ko represent karta hai.
# \. actual dot (.) ko match karta hai.
# + ka matlab hota hai one or more characters.
# Regex ko manually likhne ke bajay trusted patterns use karna aur unhe samajhna professional practice hai.
# Regex101 pattern test karne, explanation dekhne aur Python code generate karne ke liye bahut useful tool hai.