#! /usr/bin/env python
import os
from aux import get_dominant_color
from aux import color2mm_range
import re
import sys

date_regexp_str = '.*_([0-9]{6})-.*'

if __name__ == "__main__":
    fig_dir = sys.argv[1]
    date_regexp = re.compile(date_regexp_str)
    figs = os.listdir(fig_dir)
    fig_dates = dict([(date_regexp.search(fig).group(1), fig) for fig in figs])
    fig_dates_sorted = sorted(fig_dates)
    figs_sorted = [fig_dates[date] for date in fig_dates_sorted]

    date_mm_range = {}
    for fig_file in [os.path.join(fig_dir, fig) for fig in figs_sorted]:
        hex_rgb = get_dominant_color(fig_file)
        mm_range = color2mm_range(hex_rgb)

        curr_date = date_regexp.search(fig_file).group(1)
        date_mm_range[curr_date] = mm_range
    print date_mm_range
    sys.exit(1)

#    max_color=$(./get_dominant_color.py ${figure_folder}/rrdm_1409${fil}-cropped.jpg)
#    range=$(./find_mm_range.py $max_color)
#    echo 1409${fil}": "$max_color"  --  "$range
