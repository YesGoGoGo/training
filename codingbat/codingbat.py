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




