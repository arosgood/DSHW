import matplotlib
from matplotlib import pyplot as plt

x = [1000, 2500, 5000, 7500, 10000]


increasing_insertion_y = [0.0001622, 0.0004682, 0.0007926, 0.0011716, 0.0017898]
increasing_selection_y =[0.0789004,
0.5021028,
1.9970702,
4.4615054,
8.209642]
decreasing_insertion_y = [0.112923,0.8021316,3.1957942,7.0808684,12.8185022]
decreasing_selection_y = [0.0897514,
0.5893144,
2.225229,
4.9102068,
8.818708]

random_insertion_y = [0.0606416, 0.3997944, 1.6726676, 3.6273352, 6.6861754]
random_selection_y = [0.0858718,
0.511588,
2.1043226,
5.0300196,
8.192985]

plt.figure(figsize=(18, 6))
###increasing graphs###
plt.subplot(131)
plt.plot(x, increasing_insertion_y, '-g', label='Insertion', ls = '--', marker = '.')
plt.plot(x, increasing_selection_y, '-b', label='Selection', ls = '--', marker = '.')
plt.title("Increasing values")
plt.xlabel("Number of values in array")
plt.ylabel("Average time")
plt.legend()
plt.savefig('increasing_values.png', dpi = 900)


###decreasing graphs###
plt.subplot(132)
plt.plot(x, decreasing_insertion_y, '-g', label='Insertion', ls = '--', marker = '.')
plt.plot(x, decreasing_selection_y, '-b', label='Selection', ls = '--', marker = '.')
plt.title("Decreasing values")
plt.xlabel("Number of values in array")
plt.ylabel("Average time")
plt.legend()
plt.savefig('decreasing_values.png')

###random graphs###
plt.subplot(133)
plt.plot(x, random_insertion_y, '-g', label='Insertion', ls = '--', marker = '.')
plt.plot(x, random_selection_y, '-b', label='Selection', ls = '--', marker = '.')
plt.title("Random values")
plt.xlabel("Number of values in array")
plt.ylabel("Average time")
plt.legend()
plt.savefig('random_values.png')