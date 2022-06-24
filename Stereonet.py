# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:46:36 2021

@author: User
"""
import matplotlib.pyplot as plt
import mplstereonet
import numpy as np
import pandas as pd



df = pd.read_csv(r'C:\Users\User\OneDrive\rosetplot\11-17-2021\MAT.csv')


# df.info()
strikes = df.Strike
dips = df['Dip']

# %% bins creation

bin_edges = np.arange(-10,366,10)
number_of_strikes, bin_edges = np.histogram(strikes, bin_edges)

number_of_strikes[0]+= number_of_strikes[1]

half = np.sum(np.split(number_of_strikes[:-1], 2),0)
two_halves = np.concatenate([half, half])


# %%

fig = plt.figure(figsize=(16,8))

ax = fig.add_subplot(121, projection='stereonet')
ax.pole(strikes, dips, c='k', label='Pole of the Planes')
ax.density_contourf(strikes, dips, measurement='poles', cmap='Reds')
ax.set_title('Density coutour of the Poles', y=1.10)
ax.grid()

ax.grid()

ax = fig.add_subplot(122, projection='polar')
ax.set_title('Rose Diagram', y=1.10)
ax.bar(np.deg2rad(np.arange(0, 360, 10)), two_halves, 
       width=np.deg2rad(10), bottom=0.0, color='.8', edgecolor='k')
# np.histogram(60,bin_edges)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_thetagrids(np.deg2rad(np.arange(0, 360, 10), lables= np.arange(0,360,10)))
ax.set_rgrids(np.arange(1, two_halves.max() + 1, 2), angle=0, weight= 'black')

fig.tight_layout()



