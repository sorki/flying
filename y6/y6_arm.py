from solid import *
from solid.utils import *

from rc import rotor

from config import *
from y6_body import body_outer, body_outer_cutout

META = {
    'model': 'y6_arm',
    'author': 'Richard Marko',
    'date': '2015-01-03',
}


def y6_arm_body():
    pull = 2
    return (
        right(arm_len/2 + body_inner_r - pull)(
            cube([arm_len, arm_w, arm_h],
                 center=True))
        - body_outer_cutout()
    )

def y6_arm_hole():
    return right(body_outer_r - body_outer_ring_w / 2.)(
            cylinder(r=m3_hole_r, h=100, center=True)
           )

def y6_arm():
    return y6_arm_body() - y6_arm_hole() - body_outer()

def arms():
    return [rotate(arm_angle * i)(y6_arm()) for i in range(n_arms)]

def holes():
    return [rotate(arm_angle * i)(y6_arm_hole()) for i in range(n_arms)]

def rotors():
    return [rotate(arm_angle * i)
            (right(arm_len + body_inner_r)(rotor.rotor(prop))) for i in range(n_arms)]


if __name__ == "__main__":
    out = y6_arm()
    scad_render_to_file(out,
                        filepath='{0}.scad'.format(META['model']),
                        include_orig_code=False)
