#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
weekday_number = now.weekday()

#Convert current date to Julian date.
from calverter import Calverter
cal = Calverter()
julian = cal.gregorian_to_jd(year,month,day)


#Convert Julian date to Islamic date.
hijri = cal.jd_to_islamic(julian)


#Convert Islamic date to weekday_name, day_number, month_name, year format.
hijri_year = hijri[0]
hijri_month = hijri[1]
hijri_day_number = hijri[2]
hijri_date = [weekday_number, hijri_day_number, hijri_month, hijri_year]


#Convert hijri_month (which are in number forms) into month names.

# Just define 12 months names:
islamic_months = ["محرّم", "صفر", "ربيع_اﻷوّل", 
                  "ربيع_الثّاني", "جمادى_اﻷولى", 
                  "جمادى_الثّانية", "رجب", "شعبان", 
                  "رمضان", "شوّال", "ذو_القعدة", "ذوالحجّة"]
# On the next step get the right name: 
hijri_date[2] = islamic_months[hijri_month - 1] # 1 <= hijri_month <= 12

islamic_day_names = ["الإثنين", "الثّلاثاء", "اﻷربعاء",
                     "الخميس", "الجمعة", "السّبت", "اﻷحد"]
hijri_date[0] = islamic_day_names[weekday_number] # 0 <= weekday_number <= 6

#print(hijri_date)
print(" ".join(str(x) for x in hijri_date)) #str(hijri_date)