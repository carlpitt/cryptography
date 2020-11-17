# Python 3.8

# monoalphabetic substitution ciphers: Caesar, multiplicative, and affine

# alphabet of capital letters
alpha_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# dict of integers [1, 26] coprime with 26 and
# their respective modular multiplicative inverses
valid_mkeys = { 1:  1,  3: 9,  5: 21,  7: 15, 9: 3, 11: 19, 15: 7, 17: 23,
               19: 11, 21: 5, 23: 17, 25: 25}

def text_clean(text):
    """
    text: str
    returns the string of letters of text to upper case
    """
    return "".join(i for i in str(text).upper() if i in alpha_str)

def text_block(text, size = 5):
    """
    text: str
    size: int > 0, optional
    returns the string of letters of text to upper case in groups of size
        delimited by spaces
    """
    text = text_clean(text)
    return " ".join(text[i:i + size] for i in range(0, len(text), size))

def isprime(n):
    """
    n: number
    returns True if n is prime, else False
    """
    # Edge cases
    if n % 1 > 0:
        return False
    n = int(n)
    if n == 2 or n == 3:
        return True
    if n < 2 or n & 1 == 0 or n % 3 == 0:
        return False
    # Checks for factors with form f = 6i +/- 1 on 5 <= f <= sqrt(n)
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def mod_mult_inv(a, m):
    """
    a: int
    m: int > 0
    returns modular multiplicative inverse of a under modulo m
    (x such that (a * x) mod b = 1) if it exists, else -1
    """
    a %= m
    if a == 0:
        return -1
    if isprime(m):
        # Uses Fermat's little theorem
        return pow(a, m - 2, m)
    # Uses the extended Euclidean algorithm
    x0, x1, y0, y1, b = 0, 1, 1, 0, m
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return x0 % m if b == 1 else -1



# Caesar cipher
def caesar_encipher(plaintext, akey):
    """
    plaintext: str
    akey: int
    returns each letter in plaintext replaced by a letter akey positions down the alphabet
    """
    akey %= 26
    # direct translation using alpha_str
    #return text_block("".join(alpha_str[(alpha_str.find(i) + akey) % 26] for i in text_clean(plaintext)))
    
    # uses chr(65 - 90) and ord("A" - "Z")
    #return text_block("".join(chr((ord(i) + akey - 65) % 26 + 65) for i in text_clean(plaintext)))
    
    # creates alphabet (better for longer messages)
    caesar_alpha = {alpha_str[i]: chr((i + akey) % 26 + 65) for i in range(26)}
    return text_block("".join(caesar_alpha[i] for i in text_clean(plaintext)))
def caesar_decipher(ciphertext, akey):
    """
    ciphertext: str
    akey: int
    returns each letter in ciphertext replaced by a letter akey positions up the alphabet
    """
    akey %= 26
    # direct translation using alpha_str
    #return "".join(alpha_str[(alpha_str.find(i) - akey) % 26] for i in text_clean(ciphertext)).lower()
    
    # uses chr(65 - 90) and ord("A" - "Z")
    #return "".join(chr((ord(i) - akey - 65) % 26 + 65) for i in text_clean(ciphertext)).lower()
    
    # creates alphabet (better for longer messages)
    caesar_alpha = {alpha_str[i]: chr((i - akey) % 26 + 65) for i in range(26)}
    return "".join(caesar_alpha[i] for i in text_clean(ciphertext)).lower()

# multiplicative cipher
def mult_encipher(plaintext, mkey):
    """
    plaintext: str
    mkey: int
    returns each letter in plaintext replaced by a letter akey positions down the alphabet
    """
    mkey %= 26
    # direct translation using alpha_str
    #return text_block("".join(alpha_str[(mkey * alpha_str.find(i)) % 26] for i in text_clean(plaintext)))
    
    # uses chr(65 - 90) and ord("A" - "Z")
    #return text_block("".join(chr((mkey * (ord(i) - 65)) % 26 + 65) for i in text_clean(plaintext)))
    
    # creates alphabet (better for longer messages)
    mult_alpha = {alpha_str[i]: chr((mkey * i) % 26 + 65) for i in range(26)}
    return text_block("".join(mult_alpha[i] for i in text_clean(plaintext)))
def mult_decipher(ciphertext, mkey):
    mkey %= 26
    # direct translation using alpha_str
    #return "".join(alpha_str[(valid_mkeys[mkey] * alpha_str.find(i)) % 26] for i in text_clean(ciphertext)).lower()
    
    # uses chr(65 - 90) and ord("A" - "Z")
    #return "".join(chr(valid_mkeys[mkey] * (ord(i) - 65) % 26 + 65) for i in text_clean(ciphertext)).lower()
    
    # creates alphabet (better for longer messages)
    mult_alpha = {alpha_str[i]: chr((valid_mkeys[mkey] * i) % 26 + 65) for i in range(26)}
    return "".join(mult_alpha[i] for i in text_clean(ciphertext)).lower()

# affine cipher
def affine_encipher(plaintext, mkey, akey):
    mkey %= 26
    akey %= 26
    # direct translation using alpha_str
    #return text_block("".join(alpha_str[(mkey * alpha_str.find(i) + akey) % 26] for i in text_clean(plaintext)))
    
    # uses chr(65 - 90) and ord("A" - "Z")
    #return text_block("".join(chr((mkey * (ord(i) - 65) + akey) % 26 + 65) for i in text_clean(plaintext)))
    
    # creates alphabet (better for longer messages)
    affine_alpha = {alpha_str[i]: chr((mkey * i + akey) % 26 + 65) for i in range(26)}
    return text_block("".join(affine_alpha[i] for i in text_clean(plaintext)))
def affine_decipher(ciphertext, mkey, akey):
    mkey %= 26
    akey %= 26
    # direct translation using alpha_str
    #return "".join(alpha_str[(valid_mkeys[mkey] * (alpha_str.find(i) - akey)) % 26] for i in text_clean(ciphertext)).lower()
    
    # uses chr(65 - 90) and ord("A" - "Z")
    #return "".join(chr(valid_mkeys[mkey] * (ord(i) - akey - 65) % 26 + 65) for i in text_clean(ciphertext)).lower()
    
    # creates alphabet (better for longer messages)
    affine_alpha = {alpha_str[i]: chr((valid_mkeys[mkey] * (i - akey)) % 26 + 65) for i in range(26)}
    return "".join(affine_alpha[i] for i in text_clean(ciphertext)).lower()



from seaborn import barplot

alpha_list =       [  "A",    "B",    "C",    "D",    "E",    "F",    "G",
                      "H",    "I",    "J",    "K",    "L",    "M",    "N",
                      "O",    "P",    "Q",    "R",    "S",    "T",    "U",
                      "V",    "W",    "X",    "Y",    "Z"]

letter_freq_list = (8.167,  1.492,  2.782,  4.253, 12.702,  2.228,  2.015,
                    6.094,  6.966,  0.153,  0.772,  4.025,  2.406,  6.749,
                    7.507,  1.929,  0.095,  5.987,  6.327,  9.056,  2.758,
                    0.978,  2.360,  0.150,  1.974,  0.074)

def letter_freq(text):
    """
    text: str
    Returns a list of the letter frequencies of each letter in text
    """
    text = text_clean(text)
    return [text.count(i) / len(text) for i in alpha_str]
def graph_freq(text):
    """
    Graphs the letter frequencies of text
    """
    barplot(alpha_list, letter_freq(text))

def expected_count(text):
    """
    text: str
    Returns a list of the expected counts of each letter in text
    """
    length = len(text_clean(text))
    return [length * letter_freq_list[i] / 100 for i in range(26)]
def actual_count(text):
    """
    text: str
    Returns a list of the actual counts of each letter in text
    """
    text = text_clean(text)
    return [text.count(i) for i in alpha_str]

def chi_squared_score(text):
    """
    text: str
    Returns the chi-squared score of text
    """
    text = text_clean(text)
    aL, eL = actual_count(text), expected_count(text)
    L = [aL[i] - eL[i] for i in range(26)]
    return sum(L[i] * L[i] / eL[i] for i in range(26))

def chi_squared_caesar_decipher(ciphertext):
    """
    ciphertext: str
    Returns a tuple of all the possible Caesar plaintexts from best to worst
    """
    ciphertext = text_clean(ciphertext)
    L = []
    for akey in range(26):
        t = caesar_decipher(ciphertext, akey)
        L.append((akey, t, chi_squared_score(t)))
    return tuple(i for i in sorted(L, key = lambda i: i[2]))
def chi_squared_affine_decipher(ciphertext):
    """"
    ciphertext: str
    Returns a tuple of the 26 best possible affine plaintexts
    """
    ciphertext = text_clean(ciphertext)
    L = []
    for mkey in valid_mkeys.keys():
        for akey in range(26):
            t = affine_decipher(ciphertext, mkey, akey)
            L.append((mkey, akey, t, chi_squared_score(t)))
    return tuple(i for i in sorted(L, key = lambda i: i[3]))[:26]
