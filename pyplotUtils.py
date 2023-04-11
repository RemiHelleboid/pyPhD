import sys
import os
import pathlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress, gaussian_kde
import scipy.constants as const

import scienceplots
plt.style.use(['science', 'ieee', 'high-vis', 'grid'])

# Change de DPI of figures. (Not needed)
# plt.rcParams['figure.dpi'] = 160


def simple_xy_plot(X, Y)
  fig, axs = plt.subplots()
  axs.plot(X, Y, label='My Label')
  axs.set_yscale('log')
  
  # Force scientific notation for x axis.
  axs.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
  
