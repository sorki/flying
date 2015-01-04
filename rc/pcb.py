from solid import *
from solid.utils import *

def generic_pcb(x, y, h=2, r=1):
    corner = cylinder(r=r, h=h, center=True)
    pcb = []
    for i in [-1, 1]:
        for j in [-1, 1]:
            pcb.append(translate([i * (x/2. - r), j * (y/2. - r), 0])(corner))

    return color([0, 0.3, 0, 0.9])(hull()(pcb))

if __name__ == "__main__":
    scad_render_to_file(generic_pcb(10, 15),
                        filepath='pcb.scad',
                        include_orig_code=False)
