import colormath
import colormath.color_objects
import csv
import Image
import pdb
import scipy
import scipy.cluster
import scipy.misc
import struct
import sys

from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie1976
from operator import itemgetter

def get_dominant_color(image_path):
    NUM_CLUSTERS = 5

    im = Image.open(image_path)
    im = im.resize((150, 150))      # optional, to reduce time
    ar = scipy.misc.fromimage(im)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2])

    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)

    vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

    index_max = scipy.argmax(counts)                    # find most frequent
    peak = codes[index_max]
    color = ''.join(chr(c) for c in peak).encode('hex')
    return color


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
def color2mm_range(hex_rgb):
    f = open("colors_in_map_colorbar_rgb_hex.txt", "r")
    crange_list = list(csv.reader(f, delimiter='\t'))
    crange = [labrange(cr[0].split()[0], cr[0].split()[1]) for cr in crange_list]
    
    # Read requested value
    srgb = colormath.color_objects.sRGBColor(0,0,0)
    lab_hexed = convert_color(srgb.new_from_rgb_hex(hex_rgb), colormath.color_objects.LabColor)
    
    for labr in crange:
        labr.distance(lab_hexed)
    
    crange_sorted = sorted(crange, key=keydef)
    return crange_sorted[0].vrange
