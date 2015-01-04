import math

segments = 40

m3_hole_r = 1.9

n_arms = 3
arm_len = 80
arm_w = 16
arm_h = 16
arm_angle = 360 / n_arms

prop = 5

body_outer_r = 55
body_outer_ring_w = 15
body_outer_h = 5

body_inner_r = body_outer_r - body_outer_ring_w
body_inner_ring_w = 22
body_inner_h = 2

holes_outer_num = 8
holes_outer_offset = 31

holes_inner_num = 4
holes_inner_offset = 21

two_parts_body = False
if two_parts_body:
    body_outer_h /= 2.
    body_inner_h /= 2.

bat_holder_w = 52
bat_holder_h = 10
bat_holder_d = 10
bat_holder_offset = 22

bat_strip_w = 37
bat_strip_h = 0.8

landing_w = 54
landing_h = 8
landing_d = 4
landing_offset = 22
landing_down_offset = 36

closed_loop = not True
