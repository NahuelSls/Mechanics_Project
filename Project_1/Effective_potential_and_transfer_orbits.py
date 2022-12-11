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

'''

'''

# Velocity of the Earth in its final orbit (assuming circular):
v_circ1 = np.sqrt(G * m_s / r1_e)

# Vectors (radial distance, angular momentum and energy):
rad1 = np.arange(0, rfinal1, dr1)
lal = rad1.size

l1 = np.zeros(lal)
e1 = np.zeros(lal)
veff1 = np.zeros(lal)

# First component of the former vector using initial values
rad1[0] = r1
l1[0] = l1_e
e1[0] = e1_e
veff1[0] = veff1_e

veffmin1 = 10**90

'''
INFORMATION FOR THE EFFECTIVE POTENTIAL OF THE TRANSFER ORBIT
'''

# Velocities at the perihelion and the aphelion of the transfer orbit
r_p = r0_e
r_a = r1_e

v_p = np.sqrt(G * m_s / r_p) * np.sqrt(2 * r_a / (r_p + r_a))
v_a = np.sqrt(G * m_s / r_a) * np.sqrt(2 * r_p / (r_p + r_a))

# VELOCITY AND KINETIC VARIATIONS OF THE TRANSFER ORBIT CAN BE CALCULATED
# Velocity variation at the PERIGEE:
delta_v_p = v_p - v_circ0
delta_v_a = v_circ1 - v_a

delta_k_p = 0.5 * m_e * (v_p**2 - v_circ0**2)
delta_k_a = 0.5 * m_e * (v_circ1**2 - v_a**2)

# Init. radius, rad. step and final radius of the simulation of the transfer orbit:
r_i = 1e7
d_r_i = 1e9
r_final_i = 50e11

# Angular momentum and energy of the Earth in transfer orbit:
li_e = m_e * r_p * v_p
ei_e = 0.5 * m_e * v_p**2 - G * m_s * m_e / r_p
veffi_e = li_e**2 / (m_e * r1**2) - G * m_s * m_e / r1

print('\n{:_^70}'.format('RESULTS') +
      '\n{:_^70}'.format('') +

      '\nINITIAL ORBIT:' +
      '\n- The angular momentum is', '{:.2e}'.format(l0_e), 'kgm^2/s.' +
      '\n- The energy is', '{:.2e}'.format(e0_e), 'J.' +
      '\n- The minimum effective potential is', '{:.2e}'.format(veff0_e), 'J.' +
      '\n{:_^70}'.format('') +

      '\nFINAL ORBIT:' +
      '\n- The angular momentum is:', '{:.2e}'.format(l1_e), 'kgm^2/s.' +
      '\n- The energy is', '{:.2e}'.format(e1_e), 'J.' +
      '\n- The minimum effective potential is', '{:.2e}'.format(veff1_e), 'J.' +
      '\n{:_^70}'.format('') +
      '\n{:_^70}'.format('') +

      '\nVARIATIONS:' +
      '\n- The velocity variation to transfer from the initial orbit to the transfer orbit at its PERIHELION is Delta VP =',
      '{:.2e}'.format(delta_v_p), 'm/s.' +
      '\n- The velocity variation to transfer from the transfer orbit at its APHELION to the final circular orbit is Delta VA =',
      '{:.2e}'.format(delta_v_a), 'm/s.' +
      '\n\n- The K variation to transfer from the initial circular orbit to the transfer orbit at its PERIHELION is Delta KP =',
      '{:.2e}'.format(delta_k_p), 'm/s.' +
      '\n- The K variation to transfer from the transfer orbit at its APHELION to the final circular orbit is Delta KA =',
      '{:.2e}'.format(delta_k_a), 'm/s.' +
      '\n{:_^70}'.format('') +
      '\n{:_^70}'.format('') +

      '\nTRANSFER ORBIT:' +
      '\nThe angular momentum is')
