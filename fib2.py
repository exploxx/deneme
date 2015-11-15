def fib(n):
    
    if n>1:
       return  fib(n-1)+fib(n-2)
    else:
       return n

gir=raw_input("bir sayi gir:")
nn=int(gir)

i=0
while (i<=nn):
     print i, "--->", fib(i)
     i+=1
