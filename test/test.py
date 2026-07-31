import unittest
import script


class TestGame(unittest.TestCase):

    def test_correct_guess(self):
        self.assertTrue(script.run_guess(5, 5))

    def test_wrong_guess(self):
        self.assertFalse(script.run_guess(0, 5))

    def test_out_of_range(self):
        self.assertFalse(script.run_guess(11, 5))

    def test_wrong_type(self):
        self.assertFalse(script.run_guess("hello", 5))


if __name__ == "__main__":
    unittest.main()



#     Explanation
# import unittest

# Python ka built-in testing module import kar rahe hain.

# Ye hume testing ke tools deta hai.

# Jaise

# TestCase
# assertTrue()
# assertFalse()
# assertEqual()

# Without iske hum tests nahi likh sakte.

# import script

# Yahan hum apni actual file import kar rahe hain.

# Suppose

# script.py

# ke andar ye function hai

# def run_guess(guess, answer):

# To test file me hum use aise call karenge

# script.run_guess(5,5)
# Class
# class TestGame(unittest.TestCase):
# Explanation

# Ye ek testing class hai.

# TestCase

# Python ko batata hai ki

# "Is class ke andar jo methods hain wo tests hain."

# Isliye sabhi test methods isi class ke andar likhte hain.