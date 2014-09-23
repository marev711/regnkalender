#! /bin/bash -
download_folder=downloads
figure_folder=figures
#rm -f ${download_folder}/* ${figure_folder}/*
mkdir -p $download_folder $figure_folder
#for fil in $(seq -w 12 31)
#do 
#    wget -q -P $download_folder http://www.smhi.se/sgn0102/maps/rrdm_1408${fil}.gif
#    convert ${download_folder}/rrdm_1408${fil}.gif -crop 74x52+59+463 +repage ${figure_folder}/rrdm_1408${fil}-cropped.jpg
#    sleep 0.5
#done
for fil in $(seq -w 1 22)
do 
    target_file=rrdm_1409${fil}.gif
    if [ -f ${download_folder}/${target_file} ]
    then
        continue
    else
        wget -q -P $download_folder http://www.smhi.se/sgn0102/maps/rrdm_1409${fil}.gif
        convert ${download_folder}/rrdm_1409${fil}.gif -crop 74x52+59+463 +repage ${figure_folder}/rrdm_1409${fil}-cropped.jpg
        sleep 0.5
    fi
done
