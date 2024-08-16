==============================
Clipping_Space Module
==============================

The `Clipping_Space` class manages the perspective projection and clipping of objects within the viewing frustum.

Class `Clipping_Space`
----------------------

.. autoclass:: utils.clipping_space.Clipping_Space
   :members:
   :undoc-members:
   :inherited-members:

Methods
--------

- `__init__()`: Initializes the clipping space with default perspective projection parameters.
- `create_perspective_projection_matrix(fov, aspect_ratio, near, far)`: Creates a perspective projection matrix based on field of view, aspect ratio, and near/far planes.
- `cube_in_space(cube_points)`: Clips the cube points to the viewing frustum and returns the visible triangles.
- `intersection_with_plane_x(A, B, x)`: Calculates intersection with a vertical plane at `x`.
- `intersection_with_plane_y(A, B, y)`: Calculates intersection with a horizontal plane at `y`.
- `find_intersection_with_plane(point1, point2)`: Finds intersections of a line segment with the clipping planes.
- `transfer_back_camera_space(point)`: Converts a point from clip space back to camera space.
