from solid import *
from solid.utils import *

META = {
    'model': 'model_name',  # will create model_name.scad
    'author': 'Richard Marko',
    'date': '2014-30-12',
}


def assembly():
    corner = rotate([90, 0, 0])(cylinder(r=width / 2, h=height))

    return hull()(
        [translate([i * (length / 2 - width / 2), 0, 0])(corner)
         for i in [-1, 1]]
    )


if __name__ == "__main__":
    out = assembly()
    scad_render_to_file(out,
                        filepath='{0}.scad'.format(META['model']),
                        include_orig_code=False)
