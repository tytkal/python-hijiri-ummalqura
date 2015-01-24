#Python Hijri Umalqurra
##Introduction
Python Umalqurra Calender is an API that will give you the ability to convert Gregorian to Hijri and hijri to Gregorian
it will give you the day name in arabic and english , and the month name in Hijri arabic and Gregorian.
##Install
You can install the library through pip 
```sh
pip install umalqurra
```
##Usage
you can run the code in the python interpreter to see the result 
```py
from umalqurra.hijri_date import HijriDate
#create the object with Gregorian date 
um = HijriDate(1989,1,10,gr=True)
#to see the day in Hijri
um.day # result : 3.0
#to see the month in Hijri
um.month #result is 6.0
#year
um.year #1409
#day name in arabic
print um.day_name #الثلاثاء
#day in english
um.day_name_en #Tuesday
#month in Hijri Arabic
print um.month_name #جمادي الاخرة
#month in Gregorian English
um.month_name_gr #January
#year in Gregorian
um.year_gr #1989
#month in Gregorian
um.month_gr # 1
#day in Gregorian
um.day_gr # 10
```
if you want to convert from Hijri to Gregorian just change the parameter in the constructor and don't pass flag 'gr'
```py
#create the object with Hijri date 
um = HijriDate(1436,3,15)
```
if you want to set the Hijri date from method not constructor
```py
um = HijriDate()
um.set_date(1409,6,3)
```
if you want to set the Gregorian date from method not constructor
```py
um = HijriDate()
um.set_date_from_gr(2015,1,6)
```
if you want the current day 
```py
um = HijriDate.today()
um.day
```
##Reference
The Hijri algorthem code has been transulate from javascript to python.
The java script was developed by Suhail Alkowaileet https://github.com/xsoh/Hijri.js/blob/master/Hijri.js
also I use this code for more understanding https://github.com/kbwood/calendars/blob/master/jquery.calendars.ummalqura.js
