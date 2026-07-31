def run_guess(guess, answer):
    try:
        guess = int(guess)

        if 1 <= guess <= 10:

            if guess == answer:
                return True

            return False

        return False

    except ValueError:
        return False