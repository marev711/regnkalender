import struct
import Image
import scipy
import scipy.misc
import scipy.cluster
import sys

def get_dominant_color(image_path):
    NUM_CLUSTERS = 5

    image = sys.argv[1]
    im = Image.open(image)
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
