from solid import *
from solid.utils import *

from rc import bat, control, powerdist
from y6_body import y6_body
from y6_arm import arms, rotors
from y6_bat import bat_holders
from landing import landing

from config import *

META = {
    'model': 'y6',
    'author': 'Richard Marko',
    'date': '2014-01-03',
    'segments': segments,
}


def y6():
    return union()([
        (y6_body()),
        arms(),
        (
            down(body_outer_h + 16)(bat.generic_battery_model(112, 35, 18))
        ),
        down(2)(bat_holders()),
        (down(12)(landing())),
        up(20)(rotors()),
        up(10)(control.kk20()),
        up(2)(powerdist.mini_power_board()),
    ])


if __name__ == "__main__":
    out = y6()
    scad_render_to_file(out,
                        filepath='{0}.scad'.format(META['model']),
                        file_header='$fn = %s;' % META['segments'],
                        include_orig_code=False)
