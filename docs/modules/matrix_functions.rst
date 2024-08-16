==============================
Matrix_Functions Module
==============================

The `Matrix_Functions` class provides various static methods for creating and manipulating matrices used for transformations in the 3D engine.

Class `Matrix_Functions`
------------------------

.. autoclass:: utils.matrix_functions.Matrix_Functions
   :members:
   :undoc-members:
   :inherited-members:

Methods
--------

- `DEG_TO_RAD(deg)`: Converts degrees to radians.
- `create_homogeneous_transformation_matrix(translation_x, translation_y, translation_z, rotation_roll, rotation_pitch, rotation_yaw, scale)`: Creates a homogeneous transformation matrix with translation, rotation, and scaling.
- `homogeneous_transformation(window)`: Generates the view, camera, and cube transformation matrices based on the current window state.
