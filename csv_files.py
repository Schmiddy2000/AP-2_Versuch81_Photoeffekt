import pandas as pd
import os
import chardet
from time import time
import numpy as np
from matplotlib import pyplot as plt
import re

path_457 = '/Users/lucas1/Desktop/Uni/Physiklabor A/Physiklabor für Anfänger Teil 2/Versuch 81 - ' \
           'Photoeffekt/Materialien/457nm_final_USB2G541981_16-25-05-212.txt'
path_494 = '/Users/lucas1/Desktop/Uni/Physiklabor A/Physiklabor für Anfänger Teil 2/Versuch 81 - ' \
           'Photoeffekt/Materialien/494nm_final_USB2G541981_16-26-31-212.txt'
path_595 = '/Users/lucas1/Desktop/Uni/Physiklabor A/Physiklabor für Anfänger Teil 2/Versuch 81 - ' \
           'Photoeffekt/Materialien/595nm_final_USB2G541981_16-31-38-355.txt'
path_657 = '/Users/lucas1/Desktop/Uni/Physiklabor A/Physiklabor für Anfänger Teil 2/Versuch 81 - ' \
           'Photoeffekt/Materialien/657nm_final_USB2G541981_16-30-18-497.txt'


def getDataframe(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    df = pd.read_csv(file_path, delimiter='\t', decimal=',', skiprows=1, header=None,
                     names=['Intensity'], encoding=result['encoding'])

    return df


df_457 = getDataframe(path_457).values
df_494 = getDataframe(path_494).values
df_595 = getDataframe(path_595).values
df_657 = getDataframe(path_657).values

wavelength_lin = np.arange(350, 1001, 1)

df_array = np.array([df_457, df_494, df_595, df_657])
wavelength_array = np.array([457, 494, 595, 657])
color_array = np.array(['b', 'g', 'orange', 'r'])


plt.figure(figsize=(12, 5))


def plotSpectrum(start_wavelength, stop_wavelength):
    k = 0

    start_index = start_wavelength - 350
    stop_index = stop_wavelength - 350

    plt.title('Vergleich der unterschiedlichen Leuchtdiodenspektren')
    plt.xlabel(r'Wellenlänge $\lambda$ in [nm]')
    plt.ylabel('Intensität in [arbitrary units]')

    for df in df_array:
        plt.plot(wavelength_lin[start_index:stop_index], df[start_index:stop_index], ls='--', c=color_array[k], lw=0.8,
                 label=r'$\lambda = {}$nm'.format(wavelength_array[k]))
        k += 1

    plt.grid()
    plt.xlim(start_wavelength, stop_wavelength)
    plt.subplots_adjust(left=0.08, right=0.95, top=0.93, bottom=0.1)
    plt.legend()

    plt.savefig('Emissionsspektren_Vergleich.png', dpi=300)
    plt.show()

    return None


plotSpectrum(400, 700)
