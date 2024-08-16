===============================
Vectors Module
===============================

The `vectors` module provides utilities for vector operations and normal calculations.

Classes
--------

.. autoclass:: utils.vectors.CalculateNormal
   :members:
   :undoc-members:
   :inherited-members:

Methods
--------

- `CalculateNormal.vector(point1, point2)`: Computes the vector from `point1` to `point2`.

- `CalculateNormal.DEG_TO_RAD(deg)`: Converts degrees to radians.

- `CalculateNormal.normal(triangle, scale=0.5)`: Calculates the normal vector for a triangle and scales it.

- `CalculateNormal.get_shadow(triangles, light_vec)`: Computes shadow points for given triangles and a light vector.

- `CalculateNormal.find_intersection(plane_normal, line_point, line_dir, plane_d=2)`: Finds the intersection of a line with a plane.
