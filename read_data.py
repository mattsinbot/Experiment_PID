import csv
import matplotlib.pyplot as plt

time_arr, ip_arr, op_arr = [], [], []
count = 0
with open("experiment_1/experiment1_Processed_Data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
    	if count >= 25:
    		if count == 25:
    			time_offset = float(row[0])
    		time_arr.append(float(row[0])-time_offset)
    		ip_arr.append(float(row[1]))
    		op_arr.append(float(row[2]))
    	count += 1
    	if count == 800:
        	break
plt.plot(time_arr, ip_arr, label="ip:waveform generator")
plt.plot(time_arr, op_arr, label="op:system response")
plt.xlabel("time [s]")
plt.ylabel("Rotation speed [RPM]")
plt.legend(loc="best")
# plt.grid()
plt.show()
