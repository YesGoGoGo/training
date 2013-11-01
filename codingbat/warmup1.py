"""Given 2 ints, a and b, return True if one if them is 10 or if
their sum is 10.
http://codingbat.com/prob/p124984
"""


# Mine
def makes10(a, b):
    return (a == 10 or b == 10 or a + b == 10)

# Theirs
## Nailed it!!!


"""Given an int n, return True if it is within 10 of 100 or 200.
Note: abs(num) computes the absolute value of a number.
http://codingbat.com/prob/p124676
"""


# Mine
def near_hundred(n):
    return (abs(n - 100) <= 10 or abs(n - 200) <= 10)


# Theirs
def their_near_hundred(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

# I got this right, but wonder why they needed parens around
# the entire expression?

""" Given 2 int values, return True if one is negative and one is
positive. Except if the parameter "negative" is True, then return
True only if both are negative.
http://codingbat.com/prob/p162058
"""


# Mine
def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0

    return (a < 0 and b > 0) or (b < 0 and a > 0)


# Theirs
def their_pos_neg(a, b, negative):
    if negative:
        return (a < 0 and b < 0)
    else:
        return ((a < 0 and b > 0) or (a > 0 and b < 0))

# Again with the extra parentheses.  Still don't get it ...
# Maybe just a style thing?  They tested against about 20
# different param sequences, and I got them all right, so
# presumably it's good.


"""
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.
"""


# Mine
def not_string(str):
    if not str[:3] == "not":
        str = "not " + str
    return str


# Theirs
def their_not_string(str):
    if len(str) >= 3 and str[:3] == "not":
        return str
    return "not " + str

# Like mine better here, I think.  I don't see the purpose of
# checking len(str) >= 3, other than for performance, maybe?


"""
Given a non-empty string and an int n, return a new string where
the char at index n has been removed. The value of n will be a
valid index of a char in the original string (i.e. n will be in the
range 0..len(str)-1 inclusive).
def missing_char(str, n):
"""


# Mine
def missing_char(str, n):
    s = n + 1
    return str[:n] + str[s:]


# Theirs
def theirs_missing_char(str, n):
    front = str[:n]
    back = str[n + 1:]
    return front + back


# Best
def best_missing_char(str, n):
    return str[:n] + str[n + 1:]

# Interesting that some of their solutions felt less explicit to
# me, and now I'm writing solutions that are less explicit than
# theirs.  Also could have just used n + 1 in the slice -- didn't
# know that was possible!

"""
Given a string, return a new string where the first and last chars
have been exchanged.
"""


# Mine
def front_back(str):
    if len(str) > 1:
        first = str[0]
        middle = str[1:-1]
        last = str[-1]
        return last + middle + first
    return str


# Theirs
def front_back(str):
    if len(str) <= 1:
        return str
    mid = str[1:len(str) - 1]  # can be written as str[1:-1]
    # last + mid + first
    return str[len(str) - 1] + mid + str[0]

# Hmmm ... Looks like they are just showing that [:-1] is like
# [:len(str) - 1], which isn't that important.  From there, the
# only real difference is that I named and split them.  So, now it
# goes back the other way, and they start

