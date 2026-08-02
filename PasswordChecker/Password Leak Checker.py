# GOAL:
# Check whether a password has appeared in any known
# data breach using the Pwned Passwords API.

# How it works:
# 1. Take password(s) from the command line.
# 2. Convert password into SHA-1 hash.
# 3. Send ONLY the first 5 characters of the hash to the API.
# 4. API returns all matching hash suffixes.
# 5. Compare the remaining hash (tail) locally.
# 6. Print how many times the password has been leaked.

import requests   # API ko request bhejne ke liye
import hashlib    # Password ka SHA-1 hash banane ke liye
import sys        # Command line arguments lene ke liye


# API se password data lane ke liye function
def request_api_data(query_char):

    # API URL + hash ke first 5 characters
    url = "https://api.pwnedpasswords.com/range/" + query_char

    # API ko GET request bhejo
    response = requests.get(url)

    # Agar request successful nahi hui
    if response.status_code != 200:
        raise RuntimeError(
            f"Error Fetching: {response.status_code}, Check the API and try again."
        )

    # API response return karo
    return response


# API response me password kitni baar leak hua check karo
def get_password_leaks_count(hashes, hash_to_check):

    # Har line ko ":" ke basis par split karo
    # Format: HASH:COUNT
    hashes = (
        line.split(":")
        for line in hashes.text.splitlines()
    )

    # Sabhi hashes check karo
    for h, count in hashes:

        # Agar hash match ho gaya
        if h == hash_to_check:

            # Leak count return karo
            return count

    # Match nahi mila
    return 0


# Password ko SHA-1 hash me convert karke API check karo
def pwned_api_check(password):

    # Password ka SHA-1 hash banao
    sha1_password = hashlib.sha1(
        password.encode("utf-8")
    ).hexdigest().upper()

    # Hash ke first 5 characters
    first5_char = sha1_password[:5]

    # Remaining hash (Tail)
    tail = sha1_password[5:]

    # API se matching hashes lao
    response = request_api_data(first5_char)

    # Leak count return karo
    return get_password_leaks_count(response, tail)


# Main function
def main(args):

    # Har password ko check karo
    for password in args:

        # Leak count nikalo
        count = pwned_api_check(password)

        # Agar password leak hua hai
        if count:
            print(
                f"{password} was found {count} times... You should probably change your password!"
            )

        # Password safe hai
        else:
            print(
                f"{password} was NOT found. Carry on!"
            )

    return "Done!"


# Program start
if __name__ == "__main__":

    # Pehla argument file name hota hai, isliye [1:]
    sys.exit(main(sys.argv[1:]))