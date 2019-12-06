from mpmath import *
import matplotlib.pyplot as plt

def fp(p):
    # Define the given parameters
    Ra = 11.5
    Kb = 12*60/1000
    Kt = 12*60/1000
    Km = 16.2*0.02835*9.81*0.0254
    J = 2.5*0.02835*9.81*(0.0254**2)
    b = 0
    Kc = 1
    Ti = 0.0005*60
    Td = 0.00005*60

    G = Km/(Ra*(J*p+b)+Kb*Km) # TF of load
    Gc = Kc*(1 + 1/(Ti*p) + Td*p)
    # Gc = Kc*(1 + Td*p)
    # Gc = Kc
    return Gc*G/(p*(1+Kt*Gc*G))


mp.dps = 5; mp.pretty = True

# Generate time vector
tm = [0.01*tm for tm in range(1, 50)]
omega_res = [60*invertlaplace(fp,tt,method='talbot') for tt in tm]
plt.plot(tm, omega_res)
plt.xlabel("time [s]")
plt.ylabel(r"$\omega$(t) [RPM]")
plt.title("Step response for PID controller")
plt.show()
