# -*- coding: utf-8 -*-
devam=True
while(devam):
   print
   sec= raw_input("Enter 'E' for Exit, \n 'F' Fahrenheit To Celsius; \n 'C' Celsius To Fahrenheit : ")
   
       
   if sec.upper()== "F" :
       drc= raw_input("What is degree ? : ")
       try:
          int(drc)
          print drc, "Fahrenheit is " , "%5.1f" % ((int(drc)-32)/1.8),  " Celsius"
       except:
          print "=== Doğru Giriş Yap! ==="
   elif sec.upper()== "C" :
        drc= raw_input("What is degree ? : ")
        try:
          int(drc)
          print drc, "Celsius is " , "%5.1f" % (int(drc)*1.8+32),  " Fahrenheit"
        except:
          print "=== Doğru Giriş Yap! ===" 
   else :
       
       break
       