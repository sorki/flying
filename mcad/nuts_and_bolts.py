from solid import *
from solid.utils import *

from constants import *

def nut_hole(size, units=MM, tolerance = 0.0001, proj = -1):
    # takes a metric screw/nut size and looksup nut dimensions
    radius = METRIC_NUT_AC_WIDTHS[size]/2.+tolerance
    height = METRIC_NUT_THICKNESS[size]+tolerance
    if proj == -1:
        out = cylinder(r=radius, h=height, center=[0,0])
        out.add_param('$fn', 6)
        return out
    if proj == 1:
        out = circle(r=radius)
        out.add_param('$fn', 6)
        return out
    if proj == 2:
        return translate([-radius/2, 0])(
            square([radius*2, height]))


def bolt_hole(size, length, units=MM, tolerance = 0.0001, proj = -1):
    radius = COURSE_METRIC_BOLT_MAJOR_THREAD_DIAMETERS[size]/2.+tolerance
    capHeight = METRIC_NUT_THICKNESS[size]+tolerance
    capRadius = METRIC_NUT_AC_WIDTHS[size]/2+tolerance

    if proj == -1:
        return (translate([0, 0, -capHeight])(
            cylinder(r= capRadius, h=capHeight))
            + cylinder(r = radius, h = length))
    if proj == 1:
        return circle(r = radius)
    if proj == 2:
        return (
        translate([-capRadius/2, -capHeight])(
            square([capRadius*2, capHeight]))
        + square([radius*2, length])
        )
