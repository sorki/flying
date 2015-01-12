from solid import *
from solid.utils import *

def spacer(h=12, r_in=2, r_out=3.5):
    return color([1,1,1,0.9])(
        cylinder(r=r_out, h=h, center=True)
        - down(1)(cylinder(r=r_in, h=h*2, center=True))
    )

if __name__ == "__main__":
    scad_render_to_file(spacer(),
                        filepath='spacer.scad',
                        include_orig_code=False)
