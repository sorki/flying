from solid import *
from solid.utils import *


# Battery brands
# ID, Name

BATTERY_BRAND_CSV = '''
TNA,Turnigy nano-tech
TUR,Turnigy
ZIP,Zippy
'''

# ID
# Brand, Name, Type, Config (s), Config (p), Capacity (mAh),
# Discharge constant (C), Dicharge burst (C), Max Charge Rate (C)
# Length (mm), Height (mm), Width (mm), Weight (g), Connector, Model

BATTERY_DATA = '''
TNA,nano-tech,Lipo,2,1,2200,25,50,5,112,35,18,133,XT60,tnt
'''


def generic_battery_model(length, height, width):
    corner = rotate([90, 0, 0])(cylinder(r=width / 2, h=height, center=True))

    return color([0, 0, 0.5, 0.5])(hull()(
        [translate([i * (length / 2 - width / 2), 0, 0])(corner)
         for i in [-1, 1]]
    ))


if __name__ == "__main__":
    scad_render_to_file(generic_battery_model(112, 35, 18),
                        filepath='bat.scad',
                        include_orig_code=False)
