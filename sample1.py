import numpy as np
import fcl

v1 = np.array([1.0, 2.0, 3.0])
v2 = np.array([2.0, 1.0, 3.0])
v3 = np.array([3.0, 2.0, 1.0])
x, y, z = 1, 2, 3
rad, lz = 1.0, 3.0
n = np.array([1.0, 0.0, 0.0])
d = 5.0

t = fcl.TriangleP(v1, v2, v3) # Triangle defined by three points
b = fcl.Box(x, y, z)          # Axis-aligned box with given side lengths
s = fcl.Sphere(rad)           # Sphere with given radius
e = fcl.Ellipsoid(x, y, z)    # Axis-aligned ellipsoid with given radii
c = fcl.Capsule(rad, lz)      # Capsule with given radius and height along z-axis
c = fcl.Cone(rad, lz)         # Cone with given radius and cylinder height along z-axis
c = fcl.Cylinder(rad, lz)     # Cylinder with given radius and height along z-axis
h = fcl.Halfspace(n, d)       # Half-space defined by {x : <n, x> < d}
p = fcl.Plane(n, d)       
