#! /usr/bin/env python
import os
from get_dominant_color import get_dominant_color
import re
import sys

date_regexp_str = '.*_([0-9]{6})-.*'

if __name__ == "__main__":
    date_regexp = re.compile(date_regexp_str)
    fig_dir = sys.argv[1]
    figs = os.listdir(fig_dir)
    fig_dates = dict([(date_regexp.search(fig).group(1), fig) for fig in figs])
    fig_dates_sorted = sorted(fig_dates)
    figs_sorted = [fig_dates[date] for date in fig_dates_sorted]
    print figs_sorted

    sys.exit(1)

#    max_color=$(./get_dominant_color.py ${figure_folder}/rrdm_1409${fil}-cropped.jpg)
#    range=$(./find_mm_range.py $max_color)
#    echo 1409${fil}": "$max_color"  --  "$range
