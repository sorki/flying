from solid import *
from solid.utils import *

from config import *


META = {
    'model': 'y6_body',
    'author': 'Richard Marko',
    'date': '2014-22-12',
    'segments': segments,
}

def body_outer_cutout():
    return cylinder(
        r=body_outer_r - body_outer_ring_w,
        h=body_outer_h + 100,
        center=True)

def body_outer():
    return (
        cylinder(
            r=body_outer_r,
            h=body_outer_h,
            center=True)
        - body_outer_cutout()
    )


def body_inner():
    return (
        cylinder(r=body_inner_r, h=body_inner_h, center=True)
        - down(1)(
            cylinder(r=body_inner_r - body_inner_ring_w, h=body_inner_h + 100, center=True))
    )

def mounting_holes_ring(r, num, offset, rot_offset=0):
    holes = []
    angle = 360. / num
    for i in range(num):
        holes.append(
                rotate([0, 0, i * angle + rot_offset]) (
                    translate([0, offset, 0])(
                        cylinder(r=r, h=100, center=True))
                    )
                )

    return holes


import y6_arm

def y6_body():
    return union()([
       #background(rotate(-90)(import_stl('/home/rmarko/hs/reprap/prints/y6/Logicflight_Y6m_-_Simplest__Durable_mini_Drone/bodyfix.stl'))),
        body_outer(),
        body_inner(),
    ]) - union()([
        mounting_holes_ring(m3_hole_r, holes_outer_num, holes_outer_offset),
        mounting_holes_ring(m3_hole_r, holes_inner_num, holes_inner_offset,
            rot_offset=45),
        y6_arm.holes(),
    ])



if __name__ == "__main__":
    out = y6_body()
    scad_render_to_file(out,
                        filepath='{0}.scad'.format(META['model']),
                        file_header='$fn = %s;' % META['segments'],
                        include_orig_code=False)
