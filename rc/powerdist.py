from solid import *
from solid.utils import *

from pcb import generic_pcb


def mini_power_board():
    return color([0, 0, 0.5, 0.5])(generic_pcb(36.1, 36.1))

if __name__ == "__main__":
    scad_render_to_file(mini_power_board(),
                        filepath='mpd.scad',
                        include_orig_code=False)
