#! /usr/bin/env python

import calendar
import datetime
import markup
from markup import oneliner as e
import pdb
import re

year = ['Januari',
        'Februari',
        'Mars',
        'April',
        'Maj',
        'Juni',
        'Juli',
        'Augusti',
        'September',
        'Oktober',
        'November',
        'December']

def main():
    firstday = 0
    today = datetime.datetime.date(datetime.datetime.now())
    current = re.split('-', str(today))
    current_no = int(current[1])
    current_month = year[current_no-1]
    current_day = int(re.sub('\A0', '', current[2]))
    current_yr = int(current[0])

    page = markup.page()
    page.init(title="Regnkalender",
              css=('definitions/calendar.css'),
              header="",
              footer="")

    page.div(id='container')

    page.b.open(class_='rtop')
    page.b.open(class_='r1')
    page.b.close()
    page.b.open(class_='r2')
    page.b.close()                                                                  
    page.b.open(class_='r3')
    page.b.close()                                                                  
    page.b.open(class_='r4')
    page.b.close()                                                                  
    page.b.close()

    page.h1(current_month + " " + str(current_yr))

    page.table(id="month")
    page.thead.open()
    page.tr.open()
    
    page.th('M&#229;ndag')
    page.th('Tisdag')
    page.th('Onsdag')
    page.th('Torsdag')
    page.th('Fredag')
    page.th('L&#246;rdag', class_="weekend")
    page.th('S&#246;ndag', class_="weekend")
    page.tr.close()
    page.thead.close()

    page.tbody.open()

    month = calendar.monthcalendar(current_yr, current_no)
    nweeks = len(month)
    for w in range(0, nweeks):
         week = month[w]
         page.tr.open()
         for x in xrange(0,7):
             day = week[x]
             if x == 5 or x == 6:
                 classtype = 'weekend'
             else:
                 classtype = 'day'
             if day == 0:
                 classtype = 'previous'
                 page.td(class_=classtype)
             else:
                 curr_date = datetime.datetime(current_yr, current_no, day).strftime("%y%m%d")
                 print curr_date
                 page.td.open(class_=classtype)
                 page.span(day)
                 page.div(class_=classtype)
                 page.td.close()
         page.tr.close()
    page.div.close()



    fhtml = open("calendar.html", "w")
    for line in page.content:
        fhtml.write("%s\n" % line)
    fhtml.close()

if __name__ == "__main__": 
    main() 
