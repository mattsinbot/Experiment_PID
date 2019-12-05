import csv
import matplotlib.pyplot as plt

time_arr, ip_arr, op_arr = [], [], []
with open("experiment_1/data_prof_software_processed.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        time_arr.append(float(row[0]))
        ip_arr.append(float(row[1]))
        op_arr.append(float(row[2]))
plt.plot(time_arr, ip_arr, label="ip:waveform generator")
plt.plot(time_arr, op_arr, label="op:system response")
plt.xlabel("time [s]")
plt.ylabel("Rotation speed [RPM]")
plt.legend(loc="best")
# plt.grid()
plt.show()
