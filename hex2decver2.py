# -*- coding: utf-8 -*-
import usal
hxdc={"A":10, "B":11, "C":12,"D":13,"E":14,"F":15,\
"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}

    
print
print "<===== Hexadesimal sayıyı Ondalığa Çevirir! =====>"
gir=raw_input("Bir HEX sayi girin : ")
gir=gir.upper()
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
     if sayi[i] not in hxdc:
        print
        print "<===== Yalnış giriş!! =====>"
        print
        gg=False
        break
     top+= hxdc[sayi[i]]*usal.usal(16,i) 
     
     i+=1
if gg:
     print "Hexadecimal", gir, " = ", top
print