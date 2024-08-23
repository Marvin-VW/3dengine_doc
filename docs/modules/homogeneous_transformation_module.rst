.. _homogeneous_transformation_module:

Homogeneous Transformation Module
=================================

The Homogeneous Transformation module is a fundamental component in 3D graphics, it allows us to transform objects within our 3D space. As already mentioned we use different coordinate systems and this module combines translation, rotation, and scaling into a single matrix operation, allowing for efficient manipulation of objects positions, orientations, and sizes relative to these coordinate systems.

The following code snippets implement the creation of a homogeneous transformation matrix and its application to a camera system and a 3D cube:




**Explanation of the Components**:


1. **DEG_TO_RAD Method**:

   .. code-block:: python
        :caption: :mod:`Matrix_Functions` class
        :linenos:

        def DEG_TO_RAD(deg: float) -> float:
            return deg*(pi/180.0)

   Converts degrees to radians, a necessary step for performing trigonometric calculations in the rotation matrices. Since trigonometric functions in Python's `math` module expect angles in radians, this utility function ensures that the input angles are appropriately converted.

------------------------------------------------------------------------------------------------------------------------

2. **create_homogeneous_transformation_matrix Method**:

    .. code-block:: python
        :caption: :mod:`Matrix_Functions` class
        :linenos:

        def create_homogeneous_transformation_matrix(
                translation_x: float, translation_y: float, translation_z: float,
                rotation_roll: float, rotation_pitch: float, rotation_yaw: float, 
                scale: int) -> np.array:

            rotation_matrix_roll = np.array([
                [1, 0, 0, 0],
                [0, cos(rotation_roll), -sin(rotation_roll), 0],
                [0, sin(rotation_roll), cos(rotation_roll), 0],
                [0, 0, 0, 1]
            ])

            rotation_matrix_pitch = np.array([
                [cos(rotation_pitch), 0, sin(rotation_pitch), 0],
                [0, 1, 0, 0],
                [-sin(rotation_pitch), 0, cos(rotation_pitch), 0],
                [0, 0, 0, 1]
            ])

            rotation_matrix_yaw = np.array([
                [cos(rotation_yaw), -sin(rotation_yaw), 0, 0],
                [sin(rotation_yaw), cos(rotation_yaw), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])

            translation_matrix = np.array([
                [1, 0, 0, translation_x],
                [0, 1, 0, translation_y],
                [0, 0, 1, translation_z],
                [0, 0, 0, 1]
            ])

            if scale == 0:
                scale = 1

            scale_matrix = np.array([
                [scale, 0, 0, 0],
                [0, scale, 0, 0],
                [0, 0, scale, 0],
                [0, 0, 0, 1]
            ])

            transformation_matrix = np.matmul(
                translation_matrix,
                np.matmul(
                    scale_matrix,
                    np.matmul(
                        rotation_matrix_yaw,
                        np.matmul(rotation_matrix_pitch, rotation_matrix_roll)
                    )
                )
            )
            return transformation_matrix



   This method generates a 4x4 homogeneous transformation matrix based on provided translation, rotation, and scale parameters. The matrix is a combination of:

   - **Translation Matrix**: Moves the object in 3D space by shifting its position along the x, y, and z axes.


   .. image:: images/translation_matrix.png
    :width: 800
    :alt: Alternative text

   - **Rotation Matrices**: Three separate matrices for rotating the object around the roll, pitch, and yaw axes (corresponding to rotations around the x, y, and z axes).
   
    .. image:: images/real_rotation.png
        :width: 800
        :alt: Alternative text

   - **Scale Matrix**: Scales the object uniformly along all axes, which is especially useful for resizing objects in a 3D scene.
    
    .. image:: images/scaling_matrix.png
        :width: 800
        :alt: Alternative text

   These matrices are multiplied in a specific order to generate one final transformation matrix.

------------------------------------------------------------------------------------------------------------------------

3. **homogeneous_transformation Method**:

    .. code-block:: python
        :caption: :mod:`Matrix_Functions` class
        :linenos:

        def homogeneous_transformation(cls, window):
        V_T_C = cls.create_homogeneous_transformation_matrix(
            (window.get_camera_system_translation_x() - 10000) / 1000.0,
            (window.get_camera_system_translation_y() - 10000) / 1000.0,
            (window.get_camera_system_translation_z() - 10000) / 1000.0,
            cls.DEG_TO_RAD(window.get_camera_system_rotation_roll() / 10.0),
            cls.DEG_TO_RAD(window.get_camera_system_rotation_pitch() / 10.0),
            cls.DEG_TO_RAD(window.get_camera_system_rotation_yaw() / 10.0),
            1
        )


        C_T_V = np.linalg.inv(V_T_C)

        V_T_Cube = cls.create_homogeneous_transformation_matrix(
            (window.get_cube_system_translation_x() - 10000) / 1000.0,
            (window.get_cube_system_translation_y() - 10000) / 1000.0,
            (window.get_cube_system_translation_z() - 10000) / 1000.0,
            cls.DEG_TO_RAD(window.get_cube_system_rotation_roll() / 10.0),
            cls.DEG_TO_RAD(window.get_cube_system_rotation_pitch() / 10.0),
            cls.DEG_TO_RAD(window.get_cube_system_rotation_yaw() / 10.0),
            window.get_cube_system_scale()
        )

        return V_T_C, C_T_V, V_T_Cube

   This class method applies the homogeneous transformation matrix to both the camera system and a 3D cube within the scene. It does this by:

   - Creating a transformation matrix (:mod:`V_T_C`) for the camera based on its current position, orientation, and a default scale of 1.
   - Calculating the inverse of this matrix (:mod:`C_T_V`) to transform coordinates from the camera's perspective back to the world coordinates.
   - Creating another transformation matrix (:mod:`V_T_Cube`) for the cube, taking into account its translation, rotation, and scale properties.

   The method returns three matrices: :mod:`V_T_C`, :mod:`C_T_V`, and :mod:`V_T_Cube`, which are essential for further rendering and object manipulation in the 3D engine.

------------------------------------------------------------------------------------------------------------------------

**Applications**:

- **Camera System**: The camera's transformation matrix (:mod:`V_T_C`) is used to position and orient the camera within the 3D scene. The inverse matrix (:mod:`C_T_V`) allows for transforming objects from camera space back to world space, essential for accurate rendering.

- **Object Transformation**: The cube's transformation matrix (:mod:`V_T_Cube`) is applied to the 3D cube to position, rotate, and scale it within the scene, relative to the camera's viewpoint.
