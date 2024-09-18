def calendar():
    print("Enter a date --------\/")
    d = int(input("Enter a day:"))
    m = int(input("Enter a month:"))
    y = int(input("Enter a year:"))
    q = y//400
    if q == 4:
        a = y - 1601
    if q == 5:
        a = y - 2001
    if a < 100:
        b = 0
        c = a
    if 100 < a < 200:
        b = 5
        c = a - 100
    if 200 < a < 300:
        b = 3
        c = a - 200
    if 300 < a < 400:
        b = 1
        c = a - 300
    if a > 400:
        b = 0
        c = a - 400
    e = c//4
    f = e * 2
    g = c - e
    h = f + g + b
    i = h%7
    if y%400 == 0 or y%4 == 0:
        february = 1
    else:
        february = 0
    if m == 1:
        j = d%7
    if m == 2:
        j = 3 
    if m == 3:
        j = 3 + february
    if m == 4:
        j = 6 + february
    if m == 5:
        j = 8 + february
    if m == 6:
        j = 11 + february
    if m == 7:
        j = 13 + february
    if m == 8:
        j = 16 + february
    if m == 9:
        j = 19 + february
    if m == 10:
        j = 21 + february
    if m == 11:
        j = 24 + february
    if m == 12:
        j = 26 + february
    k = j + d
    l = k%7
    if l == 1:
        n = "monday"
    if l == 2:
        n = "tuesday"
    if l == 3:
        n = "wednesday"
    if l == 4:
        n = "thursday"
    if l == 5:
        n = "friday"
    if l == 6:
        n = "saturday"
    if l == 0:
        n = "sunday"
    print("The day on", d, m, y," was", n)
            
         
            
             
       
        
           
        
        
        
    
    
    
    
    


























calendar()
calendar()
calendar()
calendar()
calendar()
calendar()

    





