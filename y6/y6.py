from solid import *
from solid.utils import *

from rc import bat
from y6_body import y6_body
from y6_arm import arms

from config import *

META = {
    'model': 'y6',
    'author': 'Richard Marko',
    'date': '2014-01-03',
    'segments': segments,
}


def y6():
    return union()([
        background(y6_body()),
        arms(),
        background(
            down(body_outer_h + 9)(bat.generic_battery_model(112, 35, 18))
        ),
    ])


if __name__ == "__main__":
    out = y6()
    scad_render_to_file(out,
                        filepath='{0}.scad'.format(META['model']),
                        file_header='$fn = %s;' % META['segments'],
                        include_orig_code=False)
