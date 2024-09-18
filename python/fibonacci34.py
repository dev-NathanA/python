def fib():
    n = int(input("Enter a number:"))
    a = 0
    b = 1
    if n<=1:
        print(a)
    elif n<=2:
        print(a,'\n', b)
    elif n>=3:
        print(a,"\n", b)
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            print(c)
        
    
for i in range(10):
    fib()
        

 
    
