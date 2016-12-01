from pyPhysicsSandbox import *

window('Pinball', 600, 600)
gravity(0, 900)

# lines = []
# lines.append(static_line((450, 500), (550, 50), 1))
# lines.append(static_line((150, 500), (50, 50), 1))
# lines.append(static_line((550, 50), (300, 0), 1))
# lines.append(static_line((300, 0), (50, 50), 1))
# lines.append(static_line((300, 180), (200, 200), 1))
#
# for line in lines:
#     line.elasticity = 0.7
#     line.group = 1

r_pos_x = 150
r_pos_y = 500

r_flipper = poly(((r_pos_x-20, r_pos_y-20), (r_pos_x+120, r_pos_y-100), (r_pos_x-20, r_pos_y+20)), 100)
r_flipper.color = Color('blue')
r_flipper.group = 1

l_pos_x = 450
l_pos_y = 500

l_flipper = poly(((l_pos_x+20, l_pos_y-20), (l_pos_x-120, l_pos_y-100), (l_pos_x+20, l_pos_y+20)), 100)
l_flipper.color = Color('blue')
l_flipper.group = 1

# r_pivot = pivot((r_pos_x, r_pos_y))
# r_pivot.group = 1
# r_pivot.connect(r_flipper)
# #rotary_spring(r_flipper, r_pivot, 0.15, 20000000,900000)
#
# l_pivot = pivot((l_pos_x, l_pos_y))
# l_pivot.group = 1
# l_pivot.connect(l_flipper)
# #rotary_spring(l_flipper, l_pivot, 0.15, 20000000,900000)

#r_flipper.hit(600-450+100, 600-100)

run(False)
