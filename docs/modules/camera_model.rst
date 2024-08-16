==============================
CameraModel Module
==============================

The `CameraModel` class handles the camera's perspective in the 3D engine. It provides methods for transforming 3D points into 2D space, drawing points and lines, and filling polygons.

Class `CameraModel`
-------------------

.. autoclass:: utils.camera_model.CameraModel
   :members:
   :undoc-members:
   :inherited-members:

Methods
-------

- `__init__(sensor_width, sensor_height, focal_length, resolution_x, resolution_y, u0, v0)`: Initializes the camera model with the given parameters.
- `transform_normals_to_world_space(normals, V_T_Cube)`: Transforms normals into world space.
- `world_transform(triangle, V_T_Cube)`: Transforms a triangle's points into the world space.
- `camera_transform(object, C_T_V)`: Transforms a 3D object into the camera's space.
- `draw_all_cube_points(triangles)`: Draws all points of the cube on the camera image.
- `draw_camera_image_point(C_point)`: Draws a single point on the camera image.
- `draw_all_cube_lines(triangles)`: Draws all edges of the cube.
- `draw_camera_image_line(C_point0, C_point1)`: Draws a line between two points on the camera image.
- `draw_camera_image_arrow(C_point0, C_point1)`: Draws an arrow from one point to another.
- `fill_cube_faces(triangles)`: Fills the faces of the cube on the camera image.
- `draw_poly(points)`: Draws a filled polygon on the camera image.
- `reset_camera_image()`: Resets the camera image to a blank state.
- `get_camera_vectors(V_T_C)`: Computes the camera's forward vector in the world space.
