# ECOR 1041 Lab 6

__author__ = "Emily Causi"
__student_number__ = "101236902"

# ======================================================
# Exercise 1

def parrot_trouble(talking: bool, hour: int) -> bool:
    """Return whether or not a parrot is talking within specified hours.
    Parameters: hour >= 0, 
    hour <= 23
    >>> parrot_trouble(True, 5)
    True
    >>> parrot_trouble(True, 20)
    False
    >>> parrot_trouble(False, 9)
    False
    """
    return talking == True and hour < 7 or hour > 20

# ======================================================
# Exercise 2

def alarm_clock(day: int, vacation: bool) -> str:
    """Return when an alarm will ring dependant on the day and occasion?
    Parameters: day >= 0,
    day <= 6
    >>> alarm_clock(0, False)
    '10:00'
    >>> alarm_clock(0, True)
    'off'
    >>> alarm_clock(3, False)
    '7:00'
    """ 
    if(vacation == True and day == 0 or day == 6):
        return "off"
    elif(vacation == True and day > 0 and day < 6):
        return "10:00"
    elif(vacation == False and day > 0 and day < 6):
        return "7:00"
    else:
        return "10:00"

# ======================================================
# Exercise 3

def close_far(a: int, b: int, c: int) -> bool: 
    """Return which inputted value is closest to the first, allowing an error of one.
    >>> close_far(1, 2, 10)
    True
    >>> close_far(1, 2, 3)
    False
    >>> close_far(4, 1, 3)
    True
    """
    if (((abs(a - b) <= 1) and (abs(a - c )>= 2) and (abs(b - c) >= 2)) or
        ((abs(a - c) <= 1) and (abs(a - b) >= 2) and (abs(c - b) >= 2))):
        return True
    else:
        return False

# ======================================================
# Exercise 4

def blackjack(a: int, b: int) -> int:
    """Return whichever inputted value is nearer to 21 without being over.
    Parameters: a >= 0,
    b >= 0
    >>> blackjack(30, 0)
    0
    >>> blackjack(17, 22)
    17
    >>> blackjack(19, 20)
    20
    """
    if (a > 21 and b > 21):
        return 0
    elif (a > 21):
        return b
    elif (b > 21):
        return a
    else:
        if (21 - a < 21 - b):
            return a
        else:
            return b

# ======================================================
# Exercise 5

def assistance(income: float, children: int) -> int:
    """Return amount of financial assistance to household based on income and number of children per family.
    Parameters: children >= 0
    >>> assistance(35000, 3)
    4500
    >>> assistance(20000, 1)
    2000
    >>> assistance(19000, 4)
    8000
    """
    if (30000 <= income < 40000 and children == 3): 
        return 1500*children
    elif (20000 <= income < 30000 and children == 2):
        return 1000*children
    else: 
        return 2000*children

# ======================================================
# Exercise 6

def add_up(n: int) -> float:
    """Return a float value given an integer based on a sequence expression.
    Parameters: n >= 0
    >>> add_up(5)
    8.7
    >>> add_up(2)
    2.5
    >>> add_up(4)
    6.42
    """
    total_sum = 0.0
    for i in range(1, n + 1):
        total_sum += i / (n - i + 1)
    return round(total_sum,2)   

# ======================================================
# Exercise 7

def fib(n: int) -> int:
    """Return the Fibonacci sequence number at the index specified.
    Parameters: n >= 0
    >>> fib(6)
    8
    >>> fib(2)
    1
    >>> fib(7)
    13
    """
    previous = 0
    fib_number = 1
    for i in range(2, n + 1):
        temp = fib_number
        fib_number = previous + fib_number
        previous = temp
    return fib_number  

# ======================================================
# Exercise 8

def years_to_double(initial: float, rate: float) -> int:
    """Return the number of years needed to double a bank investment.
    Parameters: rate >= 0,
    initial >= 0
    >>> years_to_double(10000, 5.0)
    15
    >>> years_to_double(22.0, 7.0)
    11
    >>> years_to_double(100.2, 2.2)
    32
    """
    x = initial*2
    n = 0
    while (initial < x):
        initial += initial*(rate/100)
        n += 1
    return n