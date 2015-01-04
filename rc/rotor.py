from solid import *
from solid.utils import *

def rotor(r_inch=6):
    rmm = (r_inch * 25.4)/2
    return color([0.6, 0, 0, 0.6])(
        cylinder(r=rmm, h=1, center=True)
        - down(1)(cylinder(r=rmm - 2, h=10, center=True)))

if __name__ == "__main__":
    scad_render_to_file(rotor(),
                        filepath='rotor.scad',
                        include_orig_code=False)
