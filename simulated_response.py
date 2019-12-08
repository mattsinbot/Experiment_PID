from mpmath import *
import matplotlib.pyplot as plt

def fp(p):
    # Define the given parameters
    Ra = 11.5
    Kb = 12*60/1000                      # convert to V/RPS
    Kt = 12*60/1000                      # convert to V/RPS
    Km = 16.2*0.02835*9.81*0.0254        # convert FPS to SI unit
    J = 2.5*0.02835*9.81*(0.0254**2)     # convert FPS to SI unit
    b = 0
    Kc = 1
    Ti = 0.0005*60                       # convert minute to second
    Td = 0.00005*60                      # convert minute to second

    G = Km/(Ra*(J*p+b)+Kb*Km)            # TF of load
    Gc = Kc*(1 + 1/(Ti*p) + Td*p)        # TF of PID controller
    # Gc = Kc*(1 + Td*p)
    # Gc = Kc
    return Gc*G/(p*(1+Kt*Gc*G))          # TF of the whole system
    
def step_info(resp, t, resp_final):
	# Find the index for 10% and 90% of total response
	tol = 1e-1
	tl_ind, th_ind, ts_ind, tp = 0, 0, 0, 0
	vl, vh, vs_l, vs_h = 0.10*resp_final, 0.90*resp_final, 0.98*resp_final, 1.02*resp_final
	peak_val = 0 
	for ind, val in enumerate(resp):
		# print(ind, val, abs(val-vs), abs(val-resp_final))
		if abs(val-vl) < tol:
			tl_ind = ind
		if abs(val-vh) < tol:
			th_ind = ind
		if ts_ind != 0:
			if vs_l > val or vs_h < val:
				ts_ind = 0
		if vs_l < val and vs_h > val and ts_ind == 0:
			ts_ind = ind
		if val > peak_val:
			peak_val = val
	print("Rise time: %1.3f sec"%(t[th_ind]-t[tl_ind]))
	print("Settling time: %1.3f sec"%t[ts_ind])
	print("Overshoot: %2.3f percent"%((peak_val-resp_final)*100/resp_final))
	return tl_ind, th_ind, ts_ind

mp.dps = 5; mp.pretty = True

# Set point
set_pt = 1000/12

# Generate time vector
tm = [0.0001*tm for tm in range(1, 5000)]

# Multiply the output with 60 to convert RPS to RPM
omega_res = [60*invertlaplace(fp,tt,method='talbot') for tt in tm] # RPM

# Call step_info
stepInfo = step_info(omega_res, tm, set_pt)

plt.plot(tm, omega_res)
plt.plot([tm[stepInfo[0]], tm[stepInfo[0]]], [0, omega_res[stepInfo[0]]], "C1")
plt.plot([tm[stepInfo[1]], tm[stepInfo[1]]], [0, omega_res[stepInfo[1]]], "C1")
plt.plot([tm[stepInfo[2]], tm[stepInfo[2]]], [0, omega_res[stepInfo[2]]], "C2")
plt.text(tm[stepInfo[1]]/2, omega_res[stepInfo[1]]/2, "rise time")
plt.text(tm[stepInfo[2]], omega_res[stepInfo[2]]/2, "setteling time")
plt.xlabel("time [s]")
plt.ylabel(r"$\omega$(t) [RPM]")
plt.title("Step response for PID controller")
plt.grid()
plt.show()
