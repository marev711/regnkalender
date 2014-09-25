#! /usr/bin/env python

import calendar
import datetime
import markup
from markup import oneliner as e
import pdb
import os
import re

fig_folder = "figures"
symbols = [fig for fig in os.listdir(fig_folder) if re.search("rrdm", fig) is None]

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

    page.table.open(id="month")
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
                 curr_weather = None
                 for sym_file in symbols:
                     if re.search(curr_date, sym_file) is not None:
                         curr_weather = sym_file

                 page.td.open(class_=classtype)
                 page.span(day)

                 if curr_weather is not None:
                     page.img(src=os.path.join(fig_folder, curr_weather))
                 page.div(class_=classtype)
                 page.td.close()
         page.tr.close()
    page.table.close()
    page.h3("En liten f&#246;rklaring till bilderna:")
    page.p("Regndata h&#228;mtas fr&#229;n SMHI:s hemsida och nederb&#246;rden i &#214;sterg&#246;tland ritas om till ett moln. Molnen betyder")
    page.table(id="explanation")
    page.tr.open()
    page.td.open()
    page.img(width="50px", align="middle", src="definitions/0-1.png")
    page.span(": sol eller v&#228;ldigt lite regn")
    page.td.close()
    page.td.open()
    page.img(width="50px", align="middle", src="definitions/5-10.png")
    page.span(": 5-10 mm regn")
    page.td.close()
    page.td.open()
    page.img(width="50px", align="middle", src="definitions/20-more.png")
    page.span(": mycket regn")
    page.td.close()
    page.tr.close()


    page.tr.open()
    page.td.open()
    page.img(width="50px", align="middle", src="definitions/1-3.png")
    page.span(": 1-3 mm regn")
    page.td.close()
    page.td.open()
    page.img(width="50px", align="middle", src="definitions/10-15.png")
    page.span(": 10-15 mm regn")
    page.td.close()
    page.td()
    page.tr.close()

    page.tr.open()
    page.td.open()
    page.img(width="50px", align="middle", src="definitions/3-5.png")
    page.span(": 3-5 mm regn")
    page.td.close()
    page.td.open()
    page.img(width="50px", align="middle", src="definitions/15-20.png")
    page.span(": 15-20 mm regn")
    page.td.close()
    page.td()
    page.tr.close()

    page.div.close()



    fhtml = open("index.html", "w")
    for line in page.content:
        fhtml.write("%s\n" % line)
    fhtml.close()

if __name__ == "__main__": 
    main() 
