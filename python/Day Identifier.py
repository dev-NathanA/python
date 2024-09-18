def dayfinder():
    d = int(input("Enter a day:"))
    m = int(input("Enter a month:"))
    y = int(input("Enter a year:"))
    a = y//400
    b = a*400
    c = (y - b)- 1
    if c == 0:
        h = 0
    z = c//4
    e = 2*z
    f = c - z
    g = e + f
    h = g%7
    j = m - 1
    if j == 0:
        i = 0
    elif j == 1:
        i = 3
    elif j == 2:
        i = 3
    elif j == 3:
        i = 6
    elif j == 4:
        i = 1
    elif j == 5:
        i = 4
    elif j == 6:
        i = 6
    elif j == 7:
        i = 2
    elif j == 8:
        i = 5
    elif j == 9:
        i = 0
    elif j == 10:
        i = 3
    elif j == 11:
        i = 5
    elif j == 12:
        i = 1
    k = d%7
    l = k + i + h
    n = l%7
    if n == 1:
        o = "Monday"
    elif n == 2:
        o = "Tuesday"
    elif n == 3:
        o = "Wednesday"
    elif n == 4:
        o = "Thursday"
    elif n == 5:
        o = "Friday"
    elif n == 6:
        o = "Saturday"
    elif n == 0:
        o = "Sunday"
    print("The day on ", d, m, y, " is ", o)

dayfinder()
dayfinder()
dayfinder()
dayfinder()
dayfinder()
    




