#  based on nuts_and_bolts.scad from MCAD library
#  https:# github.com/elmom/MCAD/
#  Copyright 2010 D1plo1d
#  This library is dual licensed under the GPL 3.0 and the GNU Lesser General Public License as per http:# creativecommons.org/licenses/LGPL/2.1/ .


MM = "mm"
INCH = "inch" # Not yet supported

# Based on: http:# www.roymech.co.uk/Useful_Tables/Screws/Hex_Screws.htm
METRIC_NUT_AC_WIDTHS = [
    -1, # 0 index is not used but reduces computation
    -1,
    -1,
    6.40, # m3
    8.10, # m4
    9.20, # m5
    11.50, # m6
    -1,
    15.00, # m8
    -1,
    19.60, # m10
    -1,
    22.10, # m12
    -1,
    -1,
    -1,
    27.70, # m16
    -1,
    -1,
    -1,
    34.60, # m20
    -1,
    -1,
    -1,
    41.60, # m24
    -1,
    -1,
    -1,
    -1,
    -1,
    53.1, # m30
    -1,
    -1,
    -1,
    -1,
    -1,
    63.5 # m36
]
METRIC_NUT_THICKNESS = [
    -1, # 0 index is not used but reduces computation
    -1,
    -1,
    2.40, # m3
    3.20, # m4
    4.00, # m5
    5.00, # m6
    -1,
    6.50, # m8
    -1,
    8.00, # m10
    -1,
    10.00, # m12
    -1,
    -1,
    -1,
    13.00, # m16
    -1,
    -1,
    -1,
    16.00 # m20
    -1,
    -1,
    -1,
    19.00, # m24
    -1,
    -1,
    -1,
    -1,
    -1,
    24.00, # m30
    -1,
    -1,
    -1,
    -1,
    -1,
    29.00 # m36
]

COURSE_METRIC_BOLT_MAJOR_THREAD_DIAMETERS = [
    # based on max values
    -1,  # 0 index is not used but reduces computation
    -1,
    -1,
    2.98, # m3
    3.978, # m4
    4.976, # m5
    5.974, # m6
    -1,
    7.972, # m8
    -1,
    9.968, # m10
    -1,
    11.966, # m12
    -1,
    -1,
    -1,
    15.962, # m16
    -1,
    -1,
    -1,
    19.958, # m20
    -1,
    -1,
    -1,
    23.952, # m24
    -1,
    -1,
    -1,
    -1,
    -1,
    29.947, # m30
    -1,
    -1,
    -1,
    -1,
    -1,
    35.940 # m36
]
