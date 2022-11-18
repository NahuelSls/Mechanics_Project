import matplotlib.pylab as plt
import numpy as np
import math

# Relevant constants, units S.I.
# Gravity constant:
G = 6.67e-11

# Mass constants (Earth and Sun):
m_s = 1.9885e30
m_e = 5.972e24

'''
INFORMATION FOR THE EFFECTIVE POTENTIAL OF THE EARTH IN ITS INITIAL ORBIT
'''

# Initial conditions for the Earth (assuming circular orbit):
r0_e = 2.28e11
v0_e = (G * m_s / r0_e)**0.5
r0 = 1e7

# Angular momentum and Energy (Earth):
l0_e = m_e * r0_e * v0_e
e0_e = 0.5 * m_e * v0_e**2 - G * m_s * m_e / r0_e
veff0_e = l0_e**2 / (m_e * r0**2) - G * m_s * m_e / r0

'''

'''

# Earth velocity in its initial orbit:
v_circ0 = np.sqrt(G * m_s / r0_e)

# Time step and final radius for the simulation of the effective potentials:
dr0 = 1e9
rfinal0 = 220e11

# Vectors. Radial distance (rad), angular momentum (l) and energy (e):
rad0 = np.arange(0, rfinal0, dr0)
lal = rad0.size

l0 = np.zeros(lal)
e0 = np.zeros(lal)
veff0 = np.zeros(lal)

veffmin0 = 10**90

# Saving the first components of the former vectors using initial values
rad0[0] = r0
l0[0] = l0_e
e0[0] = e0_e
veff0[0] = veff0_e

'''
INFORMATION FOR THE EFFECTIVE POTENTIAL OF THE EARTH IN THE FINAL ORBIT
'''

# Initial conditions for the Earth in Mars (assuming circular orbit):
r1_e = 2.25 * 1.28e11
v1_e = (G * m_s / r1_e) ** 0.5
r1 = 1e7

# Time step and final radius for the simulation of the effective potential:
dr1 = 1e9
rfinal1 = 500e11

# Angular momentum and Energy of the Earth in the new orbit:
l1_e = m_e * r1_e * v1_e
e1_e = 0.5 * m_e * v1_e**2 - G * m_s * m_e / r1_e
veff1_e = l1_e**2 / (m_e * r1**2) - G * m_s * m_e / r1




print('\n{:-^50}'.format('RESULTS') +

      '\nINITIAL ORBIT:' +
      '\n- The angular momentum is', '{:.2e}'.format(l0_e), 'kgm^2/s.' +
      '\n- The energy is', '{:.2e}'.format(e0_e), 'J.' +
      '\n- The minimum effective potential is', '{:.2e}'.format(veff0_e), 'J.' +

      '\n{:-^50}'.format('') +
      '\nFINAL ORBIT:' +
      '\n- The angular momentum is:', '{:.2e}'.format(l1_e), 'kgm^2/s.' +
      '\n- The energy is', '{:.2e}'.format(e1_e), 'J.' +
      '\n- The minimum effective potential is', '{:.2e}'.format(veff1_e), 'J.')