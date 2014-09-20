#! /usr/bin/env python
import colormath
import colormath.color_objects
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie1976
import csv
import pdb
import sys
from operator import itemgetter

class labrange:
    def __init__(self, hex_rgb, vrange):
        srgb = colormath.color_objects.sRGBColor(0,0,0)
        self.lab = convert_color(srgb.new_from_rgb_hex(hex_rgb), colormath.color_objects.LabColor)
        self.vrange = vrange
        self.delta_e = 1000000

    def distance(self, lab_cf):
        self.delta_e = delta_e_cie1976(self.lab, lab_cf)
        

def keydef(x):
    return x.delta_e



# Read refernce list
f = open("colors_in_map_colorbar_rgb_hex.txt", "r")
crange_list = list(csv.reader(f, delimiter='\t'))
crange = [labrange(cr[0].split()[0], cr[0].split()[1]) for cr in crange_list]

# Read requested value
srgb = colormath.color_objects.sRGBColor(0,0,0)
hex_rgb = sys.argv[1]
lab_hexed = convert_color(srgb.new_from_rgb_hex(hex_rgb), colormath.color_objects.LabColor)

for labr in crange:
    labr.distance(lab_hexed)

crange_sorted = sorted(crange, key=keydef)
print crange_sorted[0].vrange
