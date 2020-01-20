# Program:       Stellar Diameters, formerly DIAMETER.
# Release:       v2.2, January 20, 2020.
# Description:   Program to estimate a star's diameter using the Stefan-Boltzmann law.
# Environment:   Python script, developed under Python 3.6.9.
# Author:        Armando Caussade.
# Contact:       http://armandocaussade.org/
# Copyright:     (c) 2020, 1999, 1990, 1989.  Some rights reserved.
# License:       GNU General Public License v2.0.
b = 7.567176066
c = 8.472351626
f = 8.441230762
g = 0.262275297
import os
os.system("clear")
print()
TYELLOW =  "\033[1;33m"
ENDC = "\033[m"
print(TYELLOW+"Stellar Diameter v2.2, formerly DIAMETER")
print("By Armando Caussade, http://armandocaussade.org/"+ENDC)
print()
v = float(input("Apparent V Magnitude? "))
m = float(input("Absolute V Magnitude? "))
t = float(input("Effective Temperature? "))
bc = float(input("Bolometric Correction? "))
import math
d9 = (v - m + b) / 5
d = 10 ** (d9)
lm = 0.4 * (4.84 - m)
l = 10 ** (lm)
d1 = (-0.2 * m) - (2 * math.log10(t)) - (0.2 * bc) + c
dm = 10 ** (d1)
d0 = (-0.2 * v) - (2 * math.log10(t)) - (0.2 * bc) + f
da = 10 ** (d0)
sb = v + (5 * d0) - g
s1 = sb - 15
ms = 10 ** ((4.75 - m - bc) / 8.75)
print()
print("---------------------------------------------")
print("Distance (Light Years)            ", "% 10.2f" % d)
print("Luminosity (Sun=1)                ", "% 10.2f" % l)
print("Mass (Sun=1)                      ", "% 10.2f" % ms)
print("---------------------------------------------")
print("Linear Diameter (Sun=1)           ", "% 10.2f" % dm)
print("Angular Diameter (mili-arc-sec)   ", "% 10.2f" % da)
print("Surface Brightness (mag/arc-sec²) ", "% 10.2f" % s1)
print("---------------------------------------------")
print()
a = input("Press any key to exit")
if a:
   exit(0)
import os
os.system("clear")
