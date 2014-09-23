#! /usr/bin/env python
import os
from aux import get_dominant_color
from aux import color2mm_range
import markup
import pdb
import re
import shutil
import sys

date_regexp_str = '.*_([0-9]{6})-.*'
def_folder = "definitions"
fig_folder = "figures"

if __name__ == "__main__":
    fig_dir = sys.argv[1]
    date_regexp = re.compile(date_regexp_str)
    figs = os.listdir(fig_dir)
    fig_dates = dict([(date_regexp.search(fig).group(1), fig) for fig in figs if re.search("rrdm", fig) is not None])
    fig_dates_sorted = sorted(fig_dates)
    figs_sorted = [fig_dates[date] for date in fig_dates_sorted]

    date_mm_range = {}
    page = markup.page()
    page.init(title="My title",
              css=(os.path.join(def_folder, 'fig-side-by-side.css')),
              header="Regnkalendern",
              footer="Slutet gott allting gott")
    page.p()
    for fig_file in [os.path.join(fig_dir, fig) for fig in figs_sorted]:
        hex_rgb = get_dominant_color(fig_file)
        mm_range,image = color2mm_range(hex_rgb)
        weather_sym = os.path.join(def_folder, image)

        curr_date = date_regexp.search(fig_file).group(1)
        date_mm_range[curr_date] = mm_range
        page.p(class_='stop-side-by-side')
        page.div(class_='side-by-side')
        page.b(curr_date)
        page.img(src=fig_file)
        page.img(src=weather_sym)
        page.hr()
        page.div.close()

        shutil.copy(weather_sym, os.path.join(fig_folder, curr_date + "_" + image))


    fhtml = open("regnkalender.html", "w")
    for line in page.content:
        fhtml.write("%s\n" % line)
    fhtml.close()
#    max_color=$(./get_dominant_color.py ${figure_folder}/rrdm_1409${fil}-cropped.jpg)
#    range=$(./find_mm_range.py $max_color)
#    echo 1409${fil}": "$max_color"  --  "$range
