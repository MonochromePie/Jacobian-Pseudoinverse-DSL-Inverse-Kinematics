
l1 = 0.35/2
l2 = 0.35
l3 = 0.35*3/2
l4 = 0.7

g = 9.81
link = 0.5 *g
m1 = 0.6 *g
m2 = (0.3*4+1.5)*g


torque = link*(l1+l3) + m1 * l2 + m2*(l4)
print(torque)
