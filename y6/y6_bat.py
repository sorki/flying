from solid import *
from solid.utils import *

from config import *

from y6_body import body_holes

META = {
    'model': 'y6_bat',  # will create model_name.scad
    'author': 'Richard Marko',
    'date': '2015-01-03',
    'segments': segments,
}


def bat_holder_part():
    return union()(
        cube([bat_holder_h, bat_holder_w, bat_holder_d], center=True)
    ) - union()(
        up(bat_holder_d/2. - bat_strip_h/2.)(
            cube([100, bat_strip_w, bat_strip_h], center=True)),
    )


def bat_holder():
    return (
            translate([bat_holder_offset, 0, -bat_holder_d / 2])(
                bat_holder_part())
            - body_holes())

def bat_holders():
    return bat_holder() + mirror([1, 0, 0])(bat_holder())


if __name__ == "__main__":
    out = bat_holder()
    scad_render_to_file(out,
                        filepath='{0}.scad'.format(META['model']),
                        file_header='$fn = %s;' % META['segments'],
                        include_orig_code=False)
