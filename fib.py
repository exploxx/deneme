3# -*- coding: utf-8 -*-
say=raw_input("Bir sayı girin = ")

i=int(say)
ilk=0
son=1
while (i>0):
	top=ilk+son
	ilk=son
	son=top
	print i, " , " , top
	i=i-1
	
	
	




