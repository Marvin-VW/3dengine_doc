.. _matrix_module:

Matrix Functions Module
=======================

This module defines the :mod:`Matrix_Functions` class, which provides functions for creating homogeneous transformation matrices.

The module consists of the following class:

- `Matrix_Functions`: Creates matrices for world-to-camera, camera-to-world, and world-to-cube transformations, as well as for translation, rotation, and scaling.

.. class:: Matrix_Functions()

The `Matrix_Functions` class offers methods to create rotation, translation, and scaling matrices.

**Methods:**

    .. method:: DEG_TO_RAD(deg: float) -> float

        Converts an angle from degrees to radians.

        **Parameters:**

        - `deg`: The angle in degrees.

        **Returns:**

        - The angle in radians.

        **Code:**

        .. code-block:: python
            :caption: :mod:`DEG_TO_RAD` method

            def DEG_TO_RAD(deg: float) -> float:
                return deg * (pi / 180.0)

    .. method:: create_homogeneous_transformation_matrix(translation_x: float, translation_y: float, translation_z: float, rotation_roll: float, rotation_pitch: float, rotation_yaw: float, scale: int) -> np.array

        Creates a homogeneous transformation matrix combining translation, rotation (roll, pitch, yaw), and scaling.

        **Parameters:**

        - `translation_x`: Translation along the x-axis.

        - `translation_y`: Translation along the y-axis.

        - `translation_z`: Translation along the z-axis.

        - `rotation_roll`: Rotation around the x-axis (roll).

        - `rotation_pitch`: Rotation around the y-axis (pitch).

        - `rotation_yaw`: Rotation around the z-axis (yaw).

        - `scale`: Uniform scaling factor.

        **Returns:**

        - A `numpy.array` representing the homogeneous transformation matrix.

        **Code:**

        .. code-block:: python
            :caption: :mod:`create_homogeneous_transformation_matrix` method
            :emphasize-lines: 5, 12, 19, 26, 36, 43-47

            def create_homogeneous_transformation_matrix(translation_x: float, translation_y: float, translation_z: float,
                                                         rotation_roll: float, rotation_pitch: float, rotation_yaw: float,
                                                         scale: int) -> np.array:

                rotation_matrix_roll = np.array([
                    [1,	                0,				    0,				    0],
                    [0,	                cos(rotation_roll),	-sin(rotation_roll),0],
                    [0,	                sin(rotation_roll),	cos(rotation_roll),	0],
                    [0,	                0,				    0,				    1]
                ])

                rotation_matrix_pitch = np.array([
                    [cos(rotation_pitch),	0,	                sin(rotation_pitch),0],
                    [0,					    1,	                0,					0],
                    [-sin(rotation_pitch),  0,	                cos(rotation_pitch),0],
                    [0,					    0,	                0,					1]
                ])

                rotation_matrix_yaw = np.array([
                    [cos(rotation_yaw),	-sin(rotation_yaw),	0,	                0],
                    [sin(rotation_yaw),     cos(rotation_yaw),	0,	                0],
                    [0,					    0,				    1,	                0],
                    [0,					    0,				    0,	                1]
                ])

                translation_matrix = np.array([
                    [1,	0,	0,  translation_x],
                    [0,	1,	0,	translation_y],
                    [0,	0,	1,	translation_z],
                    [0,	0,	0,	1]
                ])

                if scale == 0:
                    scale = 1

                scale_matrix = np.array([
                    [scale,	0,	    0,    0],
                    [0,	    scale,	0,  	0],
                    [0,	    0,	    scale,	0],
                    [0,	    0,	    0,	    1]
                ])

                transformation_matrix = np.matmul(translation_matrix,
                                              np.matmul(scale_matrix,
                                                        np.matmul(rotation_matrix_yaw,
                                                                  np.matmul(rotation_matrix_pitch,
                                                                            rotation_matrix_roll))))
                return transformation_matrix

    .. method:: homogeneous_transformation(cls, window)

        Computes the world-to-camera (:mod:`V_T_C`), camera-to-world (:mod:`C_T_V`), and cube-to-world (:mod:`V_T_Cube`) transformation matrices based on the window's camera and cube properties.

        **Parameters:**

        - `window`: The window instance providing translation, rotation, and scaling parameters for both the camera and the cube (:ref:`Window Module <window_module>`).

        **Returns:**

        - `V_T_C`: The world-to-camera transformation matrix.

        - `C_T_V`: The camera-to-world transformation matrix (inverse of `V_T_C`).

        - `V_T_Cube`: The cube-to-world transformation matrix.

        **Code:**

        .. code-block:: python
            :caption: :mod:`homogeneous_transformation` method
            :emphasize-lines: 3, 13, 15

            @classmethod
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
