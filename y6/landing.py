from solid import *
from solid.utils import *

from config import *

from y6_body import body_holes, mounting_holes_ring
from mcad.nuts_and_bolts import nut_hole

META = {
    'model': 'landing',  # will create model_name.scad
    'author': 'Richard Marko',
    'date': '2015-01-04',
    'segments': segments,
}


def landing_horiz_part():
    return (
        cube([landing_w, landing_h, landing_d], center=True)
    )

def landing_cylinder():
    r = 20
    r_sub = 4
    return (
        translate([landing_w / 2 - 0., landing_offset + landing_h/2., -r])(
            rotate([90, 0, 0])(
                cylinder(r=r, h=landing_h)
                - down(1)(cylinder(r=r-r_sub, h=landing_h+10))
            )
        ))

def landing_leg():
    body = landing_cylinder()
    return body
            #- translate([4 - landing_w/2 , 0, -r - 30])(
            #    (cube([50, 50, 50]))

def landing_part():
    body = (
            landing_leg()
            + mirror([1, 0, 0])(landing_leg())
            - hull()(
                translate([0, landing_offset, -landing_d / 2])(
                    scale([1, 1.1, 1.1])(
                    landing_horiz_part())),
                translate([0, landing_offset, -landing_d / 2 - landing_down_offset])(
                    scale([1, 1.1, 1.1])(
                    landing_horiz_part())),
                )
            + translate([0, landing_offset, -landing_d / 2])(
                landing_horiz_part())
            - body_holes()
            )

    # nut holes
    body -= down(4.1)(union()([mounting_holes_ring(m3_hole_r*2, holes_outer_num,
                holes_outer_offset, obj=nut_hole(3))]))


    if closed_loop:
            body += translate([0, landing_offset, -landing_d / 2 - landing_down_offset])(
                landing_horiz_part())


    return body

def landing():
    return landing_part() + mirror([0, 1, 0])(landing_part())


if __name__ == "__main__":
    out = rotate([90,0,0])(landing_part())
    scad_render_to_file(out,
                        filepath='{0}.scad'.format(META['model']),
                        file_header='$fn = %s;' % META['segments'],
                        include_orig_code=False)
