def seconds_to_hms(seconds):
    hours = seconds // (60 * 60)
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{hours}:{minutes:02d}:{seconds:02d}"


print(seconds_to_hms(4000))

# =====================================

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return round(fahrenheit, 1)


print(celsius_to_fahrenheit(37))

# =====================================

def split_evenly(total, people):
    each = total // people
    remainder = total % people
    return each, remainder


print(split_evenly(17, 5))

# =====================================

def initials(full_name):
    names = full_name.split()
    result = ""
    i = 0
    while i < len(names):
        result = result + names[i][0].upper() + "."
        i = i + 1
    return result


print(initials("Abdullah Hassan"))

# =====================================

def is_palindrome_word(word):
    word = word.strip().lower()
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False


print(is_palindrome_word("level"))

# =====================================

def mask_email(email):
    position = email.index("@")
    name = email[:position]
    domain = email[position:]
    if len(name) <= 2:
        return email
    else:
        return name[0] + "*" * (len(name) - 2) + name[-1] + domain


print(mask_email("ahs@gmail.com"))

# =====================================

def middle(values):
    length = len(values)
    if length % 2 == 1:
        return values[length // 2 : length // 2 + 1]
    else:
        return values[length // 2 - 1 : length // 2 + 1]


print(middle([1, 2, 3, 4, 5]))

# =====================================

def rotate_left(values, k):
    result = values[:]
    length = len(result)
    if length == 0:
        return result
    k = k % length
    i = 0
    while i < k:
        first = result[0]
        result = result[1:]
        result = result + [first]
        i = i + 1
    return result


print(rotate_left([1, 2, 3, 4, 5], 7))

# =====================================

def fib_list(n):
    result = []
    a = 0
    b = 1
    i = 0
    while i < n:
        result = result + [a]
        next_number = a + b
        a = b
        b = next_number
        i = i + 1
    return result


print(fib_list(7))

# =====================================

def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps = steps + 1
    return steps


print(collatz_steps(7))
