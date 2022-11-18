import matplotlib.pylab as plt
import numpy as np
import math

# Relevant constants, units S.I.
# Gravity constant
G = 6.67e-11

# Mass constants (Earth and Sun)
m_s = 1.9885e30
m_e = 5.972e24

# Initial conditions for the Earth (assuming circular orbit)
r0_e = 2.28e11
v0_e = (G * m_s / r0_e)**0.5
r0 = 1.e7

# Angular momentum and Energy (Earth)
l0_e = m_e * r0_e * v0_e
e0_e = 0.5 * m_e * v0_e**2 - G * m_s * m_e / r0_e
veff0_e = l0_e**2 / (m_e * r0**2) - G * m_s * m_e / r0

print('\nRESULTS')
print('\nINITIAL ORBIT:')
print('- The angular momentum is', '{:.2e}'.format(l0_e), 'kgm^2/s.')
print('- The energy is', '{:.2e}'.format(e0_e), 'J.')
print('- The minimum effective potential is', '{:.2e}'.format(veff0_e), 'J.')
