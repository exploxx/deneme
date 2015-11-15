# -*- coding: utf-8 -*-
#import usal
hxdc={"A":10, "B":11, "C":12,"D":13,"E":14,"F":15,"a":10, "b":11, "c":12,"d":13,"e":14,"f":15,\
"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}

def usal(m,n):
    i=0
    mult=1
    while (i<n): 
          mult=mult*m
          
          i+=1
    return mult
    
print
print "<===== Hexadesimal sayıyı Ondalığa Çevirir! =====>"
gir=raw_input("Bir HEX sayi girin : ")

#----ters al 
sayi=[]
i=len(gir)-1

while (i>=0):

       sayi.append(gir[i])
       
       i-=1           
gg=True
i=0
top=0
while (i<len(sayi)):
     if sayi[i]  not in hxdc:
        print
        print "Yalnış giriş!!"
        print
        gg=False
        break
     #top+= hxdc[sayi[i]]*usal.usal(16,i) 
     top+= hxdc[sayi[i]]*usal(16,i) 
     i+=1
if gg:
     print "Hexadecimal", gir, " = ", top
print