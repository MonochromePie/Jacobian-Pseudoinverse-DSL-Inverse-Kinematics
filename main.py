import parameter
import current
import utils
import sympy as sp


#Run once to initialize S and target
S = parameter.S.subs(dict(zip(parameter.thetaParam, current.currentThetas)))
target = S

#initial update
S, J, t, e, phi = utils.update_parameters(target)


while True:
    print("Current Position:", [e for e in S])
    target = (input("Enter target x,y,z coordinates separated by commas (or 'q' to quit): ").split(','))
    if target == ['q']:
        break

    t = sp.Matrix([float(coord) for coord in target])

    S, J, t, e, phi = utils.update_parameters(t)

    while e.norm() > 0.001:
        #psuedo inverse
        J_pinv =  J.pinv()

        #solve for delta thetas, Jacobian pseudo inverse nullsplace method aka damped least squares
        delta_thetas = J_pinv * e + (sp.eye(4) - J_pinv * J) * phi[0]

        current.currentThetas += delta_thetas
        S, J, t, e, phi = utils.update_parameters(t)
        print(S)
        print(e.norm())
        #i hate my life

    print("Current Angle:" , [round(e*180/3.1415,3) for e in current.currentThetas])



