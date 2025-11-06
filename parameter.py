import sympy as sp
import const
import current

#t for the servo angle of each servo
t1, t2, t3, t4= sp.symbols('t1 t2 t3 t4')

thetaParam = sp.Matrix([t1, t2, t3, t4]).T

L1 = sp.Matrix([[-const.l1 * sp.cos(t1)],
               [0],
               [const.l1 * sp.sin(t1)]])

L2 = sp.Matrix([[const.l2*sp.cos(const.PI_3_2 - t3 - t2)],
               [0],
               [const.l2*sp.sin(const.PI_3_2 - t3 - t2)]])

L3 = sp.Matrix([[const.l3*sp.cos(const.PI + t4 - t3 - t2)],
               [0],
               [const.l3*sp.sin(const.PI + t4 - t3 - t2)]])

#XZ forward kinematics
L = L1 + L2 + L3

#Rotation matrix from base motor t1
R = sp.Matrix([[ sp.cos(t1), -sp.sin(t1), 0],
              [ sp.sin(t1),  sp.cos(t1), 0],
              [         0,          0, 1]])

# XYZ space forward kinematics
S = R * L

#Jacobian
J = S.jacobian([t1, t2, t3, t4])
