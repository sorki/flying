from solid import *
from solid.utils import *

from pcb import generic_pcb


def kk20():
    return generic_pcb(51.5, 51.5)

if __name__ == "__main__":
    scad_render_to_file(kk20(),
                        filepath='kk20.scad',
                        include_orig_code=False)
