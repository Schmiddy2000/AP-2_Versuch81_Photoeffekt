import numpy as np
from matplotlib import pyplot as plt

# Data:

Intensity1 = 1.1
Intensity2 = 1.3
Intensity3 = 3

part1_I1_negative = np.array([3.6, 6.7, 7.5, 8.8, 9.2, 10.2, 10.8, 11.4, 11.6, 11.9, 12.3, 12.4, 12.6]) * -1e-6
part1_I1_negative_rev = part1_I1_negative[::-1]
part1_U1_negative = np.array([0.01, 0.57, 1.04, 1.38, 2.02, 3.09, 4.05, 5.36, 6.06, 7.08, 8.27, 9.05, 9.99]) * -1
part1_U1_negative_rev = part1_U1_negative[::-1]

part1_I1_positive = np.array([2.76, 2.16, 1.19, 0.69, 0.32, 0.19, 0.07, 0.01, 0, -0.01]) * -1e-6
part1_U1_positive = np.array([0.04, 0.18, 0.4, 0.54, 0.7, 0.8, 0.99, 1.24, 1.4, 1.95])

part1_I1 = np.concatenate((part1_I1_negative_rev, part1_I1_positive))
part1_U1 = np.concatenate((part1_U1_negative_rev, part1_U1_positive))


part1_I2_negative = np.array([23.8, 39.9, 54.4, 67.8, 80.4, 90.6, 103.6, 112.1, 118.1, 120.7, 125.8, 130.8,
                             134.3]) * -1e-6
part1_I2_negative_rev = part1_I2_negative[::-1]
part1_U2_negative = np.array([0.01, 0.42, 0.85, 1.33, 1.93, 2.58, 3.73, 4.78, 5.69, 6.17, 7.29, 8.71, 9.99]) * -1
part1_U2_negative_rev = part1_U2_negative[::-1]

part1_I2_positive = np.array([15.03, 14.5, 12.68, 9.22, 7.46, 5.19, 3.69, 1.29, 0.09, 0.05, -0.02, -0.04,
                             -0.05]) * -1e-6
part1_U2_positive = np.array([0.16, 0.17, 0.23, 0.37, 0.43, 0.53, 0.59, 0.74, 0.98, 1.02, 1.2, 1.42, 2.11])

part1_I2 = np.concatenate((part1_I2_negative_rev, part1_I2_positive))
part1_U2 = np.concatenate((part1_U2_negative_rev, part1_U2_positive))


part1_I3_negative = np.array([42, 85, 109, 153, 176, 213, 250, 285, 316, 337, 358, 385, 402]) * -1e-3
part1_I3_negative_rev = part1_I3_negative[::-1]
part1_U3_negative = np.array([0.01, 0.66, 1.05, 1.79, 2.22, 3, 3.94, 5.06, 6.19, 7.05, 7.96, 9.17, 9.99]) * -1
part1_U3_negative_rev = part1_U3_negative[::-1]

part1_I3_positive = np.array([26, 20.4, 13.2, 8.6, 1.2, 0.9, 0.2, 0.1, 0]) * -1e-6
part1_U3_positive = np.array([0.27, 0.35, 0.497, 0.597, 0.851, 0.875, 0.96, 1.028, 2])   # 2 is just in the 0-range

part1_I3 = np.concatenate((part1_I3_negative_rev, part1_I3_positive))
part1_U3 = np.concatenate((part1_U3_negative_rev, part1_U3_positive))

# Part 2:

part2_L1_I_negative = np.array([])


# The function 'plotCurve' scatters the x and y data. You have to add a color and a label for each data set.
# Optionally you can add x and y errors and specify weather they should be shown or not.

def plotCurve(x_array, y_array, my_color, my_label, x_err=None, y_err=None, plot_errors=True):
    if x_err is None:
        x_err = np.zeros(len(x_array))

    if y_err is None:
        y_err = np.zeros(len(y_array))

    plt.scatter(x_array, y_array * 1e6, marker='x', label=my_label, c=my_color)

    if plot_errors:
        plt.errorbar(x_array, y_array * 1e6, xerr=x_err, yerr=y_err, fmt='none', elinewidth=0.7, capthick=0.7,
                     capsize=3, ecolor='black')

    plt.grid()

    return None


plt.figure(figsize=(12, 5.5))


def Part1PlotSemiCombined():
    plt.subplot(2, 1, 1)
    plt.title('Kennlinie bei kleiner (oben) und großer (unten) Intensität')
    plt.ylabel('Stromstärke in [$\mu$A]')
    plotCurve(part1_U1, part1_I1, my_color='orange', my_label='Diodenspannung 1,1V')
    plotCurve(part1_U2, part1_I2, my_color='b', my_label='Diodenspannung 1,3V')
    plt.grid()
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.xlabel('Spannung in [V]')
    plt.ylabel('Stromstärke in [mA]')
    plotCurve(part1_U3, part1_I3/1e3, my_color='r', my_label='Diodenspannung 3V')

    plt.subplots_adjust(left=0.08, right=0.95, top=0.95, bottom=0.08, hspace=0.15)
    plt.legend(loc=4)

    plt.savefig('Kennlinien_Intensitaetsvergleich(beide_Richtungen).png', dpi=300)
    plt.show()

    return None


# Part1PlotSemiCombined()


def plotWholeRangeComparison():
    plt.subplot(3, 1, 1)
    plt.title('Kennlinie bei kleiner (oben) und großer (unten) Intensität')
    plt.ylabel('Stromstärke in [$\mu$A]')
    plotCurve(part1_U1, part1_I1, my_color='orange', my_label='Diodenspannung 1,1V')
    # plt.grid()
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.ylabel('Stromstärke in [$\mu$A]')
    plotCurve(part1_U2, part1_I2, my_color='b', my_label='Diodenspannung 1,3V')
    # plt.grid()
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.xlabel('Spannung in [V]')
    plt.ylabel('Stromstärke in [mA]')
    plotCurve(part1_U3, part1_I3 / 1e3, my_color='r', my_label='Diodenspannung 3V')

    plt.subplots_adjust(left=0.08, right=0.95, top=0.95, bottom=0.08)
    plt.legend()

    # plt.savefig('Kennlinien_Intensitaetsvergleich_big_overview.png', dpi=300)
    plt.show()

    return None


# plotWholeRangeComparison()


