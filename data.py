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
part1_U3_positive = np.array([0.27, 0.35, 0.497, 0.597, 0.851, 0.875, 0.96, 1.028, 2])  # 2 is just in the 0-range

part1_I3 = np.concatenate((part1_I3_negative_rev, part1_I3_positive))
part1_U3 = np.concatenate((part1_U3_negative_rev, part1_U3_positive))

# Part 2:

# --- Lambda = (657 +- 15) nm

I_657_negative = np.array([6.3, 14.1, 17.7, 20.3, 23.0, 24.1, 25.1, 25.5, 26.8]) * -1e-6
I_657_negative_rev = I_657_negative[::-1]
U_657_negative = np.array([-0.01, 0.66, 1.24, 1.94, 3.03, 4.01, 5.57, 7.03, 9.99]) * -1
U_657_negative_rev = U_657_negative[::-1]

I_657_positive = np.array([5.3, 2.1, 1.2, 0.6, 0.4, 0.1, 0, -0.02, -0.03]) * -1e-6
U_657_positive = np.array([0.07, 0.31, 0.43, 0.62, 0.7, 0.89, 1.2, 1.57, 2.38])

I_657 = np.concatenate((I_657_negative_rev, I_657_positive))
U_657 = np.concatenate((U_657_negative_rev, U_657_positive))

# --- Lambda = (595 +- 15) nm

I_595_negative = np.array([10.4, 21, 29.2, 36.9, 41.3, 43.8, 45.5, 46.9, 47.8, 49.3]) * -1e-6
I_595_negative_rev = I_595_negative[::-1]
U_595_negative = np.array([-0.01, 0.49, 1.09, 2.05, 3.04, 3.94, 4.98, 6.27, 7.53, 9.99]) * -1
U_595_negative_rev = U_595_negative[::-1]

I_595_positive = np.array([8.45, 5.55, 6.85, 4.49, 3.87, 2.69, 1.89, 1.2, 0.66, 0.35, 0.17, 0.07, 0.04, 0.01,
                           0, -0.01, -0.03]) * -1e-6
U_595_positive = np.array([0.09, 0.12, 0.15, 0.26, 0.29, 0.36, 0.42, 0.49, 0.6, 0.72, 0.83, 0.98, 1.03, 1.14,
                           1.17, 1.26, 2.15])

I_595 = np.concatenate((I_595_negative_rev, I_595_positive))
U_595 = np.concatenate((U_595_negative_rev, U_595_positive))

print('I:', len(I_595_positive), 'U:', len(U_595_positive))

# --- Lambda = (457 +- 15) nm

I_457_negative = np.array([24.2, 42.3, 55.4, 64.4, 73.9, 84.7, 93.6, 98.5, 103.3, 106.4, 109.8, 112.7]) * -1e-6
I_457_negative_rev = I_457_negative[::-1]
U_457_negative = np.array([-0.01, 0.55, 1.03, 1.44, 2, 2.9, 4.05, 4.96, 6.11, 7.14, 8.53, 9.99]) * -1
U_457_negative_rev = U_457_negative[::-1]

I_457_positive = np.array([14.83, 11.87, 9.88, 7.49, 4.36, 2.81, 1.09, 0.91, 0.78, 0.6, 0.43, 0.33, 0.3,
                           0.11, 0.06, 0.02, 0, -0.02, -0.04, -0.05]) * -1e-6
U_457_positive = np.array([0.15, 0.28, 0.36, 0.46, 0.61, 0.7, 0.84, 0.86, 0.87, 0.9, 0.93, 0.95, 0.99, 1.04,
                           1.08, 1.14, 1.18, 1.3, 1.45, 1.83])

I_457 = np.concatenate((I_457_negative_rev, I_457_positive))
U_457 = np.concatenate((U_457_negative_rev, U_457_positive))


# The function 'plotCurve' scatters the x and y data. You have to add a color and a label for each data set.
# Optionally you can add x and y errors and specify weather they should be shown or not.

def plotCurve(x_array, y_array, my_color, my_label, x_err=None, y_err=None, plot_errors=True, plot_lines=False):
    if x_err is None:
        x_err = np.zeros(len(x_array))

    if y_err is None:
        y_err = np.zeros(len(y_array))

    plt.scatter(x_array, y_array * 1e6, marker='x', label=my_label, c=my_color, s=12)

    if plot_lines:
        plt.plot(x_array, y_array * 1e6, lw=0.4, c=my_color)

    if plot_errors:
        plt.errorbar(x_array, y_array * 1e6, xerr=x_err, yerr=y_err, fmt='none', elinewidth=0.7, capthick=0.7,
                     capsize=3, ecolor='black')

    plt.grid()

    return None


plt.figure(figsize=(12, 5.5))


def plotVT2_overview():     # Hier vielleicht noch mit curve_fits arbeiten --> U_G bestimmen.

    plt.title('Übersicht der Kennlinien verschiedener Leuchtdioden')
    plt.xlabel('Diodenspannung in [V]')
    plt.ylabel('Stromstärke in [$\mu$A]')

    plt.grid(alpha=0.5)

    plotCurve(U_657, I_657, 'r', r'$\lambda = 657$nm', plot_errors=False, plot_lines=True)
    plotCurve(U_595, I_595, 'orange', r'$\lambda = 595$nm', plot_errors=False, plot_lines=True)
    plotCurve(U_457, I_457, 'b', r'$\lambda = 457$nm', plot_errors=False, plot_lines=True)
    plotCurve(part1_U2, part1_I2, 'g', r'$\lambda = ???$nm (VT1)', plot_errors=False, plot_lines=True)

    plt.subplots_adjust(left=0.08, right=0.95, top=0.95, bottom=0.08)
    plt.legend(loc=4)

    plt.savefig('Kennlinien_verschiedene_Dioden_overview.png', dpi=300)
    plt.show()

    return None


## plotVT2_overview()


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
    plotCurve(part1_U3, part1_I3 / 1e3, my_color='r', my_label='Diodenspannung 3V')

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
