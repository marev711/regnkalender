#! /usr/bin/env python

import calendar
import datetime
import markup
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

    print '''
 <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN" >
 <HTML >
 <head >

 <title >February 2007</title >
 <style type="text/css" >
 </style >
 </head >

 <body >

 <div id="container" >
 <b class="rtop" ><b class="r1" ></b > <b class="r2" ></b ><b class="r3" ></b > <b class="r4" ></b ></b >'''

    print '<h1> %s %s </h1 >' %(current_month, current_yr)
    print '''
 <table id="month" >
 <thead >
 <tr >
 <th >M&#229;ndag</th >
 <th >Tisdag</th >
 <th >Onsdag</th >
 <th >Torsdag</th >
 <th >Fredag</th >
 <th class="weekend" >L&#246;rdag</th >
 <th class="weekend" >S&#246;ndag</th >
 </tr >
 </thead >
 <tbody >
 '''
    month = calendar.monthcalendar(current_yr, current_no)
    nweeks = len(month)
    for w in range(0,nweeks):
         week = month[w]
         print "<tr>"
         for x in xrange(0,7):
             day = week[x]
             if x == 5 or x == 6:
                 classtype = 'weekend'
             else:
                 classtype = 'day'
             if day == 0:
                 classtype = 'previous'
                 print '<td class="%s"></td>' %(classtype)
             else:
                 curr_date = datetime.datetime(current_yr, current_no, day).strftime("%y%m%d")
                 print curr_date
                 print '<td class="%s">%s</span><div class="%s"></div></td>' %(classtype, day, classtype)
         print "</tr>"
    print ''' </tbody>
 </table>
 </div>
 </body>
 </html>'''

if __name__ == "__main__": 
    main() 
