import requests
import hashlib


# API se data lane ke liye function
def request_api_data(query_char):

    # API URL
    url = "https://api.pwnedpasswords.com/range/" + query_char

    # API request bhejo
    response = requests.get(url)

    # Agar response 200 nahi hai to error do
    if response.status_code != 200:
        raise RuntimeError(
            f"Error Fetching: {response.status_code}, Check the API and try again."
        )

    # Response return karo
    return response


# Password ko SHA-1 hash me convert karo
def pwned_api_check(password):

    # Password ko SHA-1 hash me convert karo
    sha1_password = hashlib.sha1(
        password.encode("utf-8")      # String → Bytes
    ).hexdigest().upper()             # Hash → Hex String → Uppercase

    # Hash return karo
    return sha1_password


# Test
print(
    pwned_api_check("hellooooooo")
)


# requests → API se data lene ke liye.
# hashlib → Password ka SHA-1 hash banane ke liye.
# request_api_data() → API ko request bhejta hai aur response return karta hai.
# pwned_api_check() → Password ko SHA-1 hash me convert karta hai.
# encode("utf-8") → String ko bytes me badalta hai.
# hexdigest() → Hash object ko hexadecimal string banata hai.
# upper() → Hash ko uppercase me convert karta hai.


# Hash Function → Input ko fixed-length hash me convert karta hai.
# One Way → Hash se original input wapas nahi milta.
# Same Input = Same Hash.
# Small Change = Completely Different Hash.
# Common Algorithms → MD5, SHA-1, SHA-256.
# Password Checker Project → SHA-1 use karega.
# Hash Tables → Fast lookup ke liye hash function use karti hain (O(1) average time).