# Goal

# Suppose kisi ne tumhe ek text file di hai.

# Example

# test.txt

# Hello
# My name is Ishika
# I love Python

# Tumhe is file ko Japanese me translate karna hai aur ek new file banani hai.

# solution---

# ******Step 1 : Install Translation Library
# pip install translate

from translate import Translator

translator = Translator(to_lang="ja")

with open("test.txt", "r", encoding="utf-8") as file:
    text = file.read()

translation = translator.translate(text)

with open("test-ja.txt", "w", encoding="utf-8") as file:
    file.write(translation)

print("✅ Translation Complete!")

#output   test.txt successfully read hui.
# ✅ English text Japanese me translate ho gaya.
# ✅ test-ja.txt successfully create ho gayi.