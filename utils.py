import parameter
import current
import sympy as sp 


def update_parameters(t):
    S = parameter.S.subs(dict(zip(parameter.thetaParam, current.currentThetas)))
    J = parameter.J.subs(dict(zip(parameter.thetaParam, current.currentThetas)))
    phi = J.nullspace()
    t = t 
    e = t - S
    
    return S, J, t, e, phi
