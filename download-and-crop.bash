#! /bin/bash -
download_folder=downloads
figure_folder=figures
rm -f ${download_folder}/* ${figure_folder}/*
mkdir -p $download_folder $figure_folder
for fil in $(seq -w 1 16)
do 
    wget -q -P $download_folder http://www.smhi.se/sgn0102/maps/rrdm_1409${fil}.gif
    convert ${download_folder}/rrdm_1409${fil}.gif -crop 74x52+59+463 +repage ${figure_folder}/rrdm_1409${fil}-cropped.jpg
    max_color=$(./get_dominant_color.py ${figure_folder}/rrdm_1409${fil}-cropped.jpg)
    range=$(./find_mm_range.py $max_color)
    echo 1409${fil}": "$max_color"  --  "$range
    sleep 0.5
done
