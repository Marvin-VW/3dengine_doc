.. _camera_model:

Camera Model Module
===================

This module defines the :mod:`CameraModel` class, which provides various functions for handling camera transformations, drawing operations on images, and related computations.

The module consists of the following class:

- `CameraModel`: Represents a camera model that allows transformations and drawing operations on a virtual camera image.

.. class:: CameraModel(sensor_width: float, sensor_height: float, focal_length: float, resolution_x: int, resolution_y: int, u0: int, v0: int)

    This class represents a camera model that simulates a camera's image processing capabilities.

    **Attributes:**

    - **sensor_width**: The width of the camera sensor.
    - **sensor_height**: The height of the camera sensor.
    - **focal_length**: The focal length of the camera.
    - **resolution_x**: The horizontal resolution of the camera image.
    - **resolution_y**: The vertical resolution of the camera image.
    - **u0**: The x-coordinate of the principal point.
    - **v0**: The y-coordinate of the principal point.
    - **camera_image**: The simulated camera image as a NumPy array.
    - **I_T_C**: The transformation matrix from camera coordinates to image coordinates.

    **Methods:**

    .. method:: __init__(sensor_width: float, sensor_height: float, focal_length: float, resolution_x: int, resolution_y: int, u0: int, v0: int)
        
        Initializes the `CameraModel` class with the given sensor dimensions, focal length, image resolution, and principal point.

        .. code-block:: python
            :caption: :mod:`__init__` method
            :emphasize-lines: 13-14

            def __init__(self, sensor_width: float, sensor_height: float, focal_length: float, resolution_x: int, resolution_y: int, u0: int, v0: int):
                self.sensor_width: float = sensor_width
                self.sensor_height: float = sensor_height
                self.focal_length: float = focal_length
                self.resolution_x: int = resolution_x
                self.resolution_y: int = resolution_y
                self.u0: int = u0
                self.v0: int = v0

                self.camera_image = np.zeros((resolution_y, resolution_x, 3), dtype=np.uint8)
                self.reset_camera_image()

                rho_width = sensor_width / resolution_x
                rho_height = sensor_height / resolution_y

                matrix_k = np.array([
                    [1/rho_width,   0,              u0],
                    [0,             1/rho_height,   v0],
                    [0,             0,               1],
                ])

                matrix_c = np.array([
                    [focal_length,  0,              0,  0],
                    [0,             focal_length,   0,  0],
                    [0,             0,              1,  0],
                ])

                self.I_T_C = np.matmul(matrix_k, matrix_c)

------------------------------------------------------------------------------------

    .. method:: transform_normals_to_world_space(normals, V_T_Cube)

        Transforms normals from the camera's local coordinate space to the world coordinate space using the :ref:`view-to-cube transformation matrix <matrix_module>`.

        **Parameters:**

        - `normals`: The normal vectors in camera coordinates.

        - `V_T_Cube`: The transformation matrix from the cube to the world.

        **Returns:**
        
        - The transformed normal vectors in world coordinates.

        .. code-block:: python
            :caption: :mod:`transform_normals_to_world_space` method

            @staticmethod
            def transform_normals_to_world_space(normals, V_T_Cube):
                normals_in_world_space = V_T_Cube[:3, :3] @ normals
                return normals_in_world_space

------------------------------------------------------------------------------------

    .. method:: world_transform(triangle, V_T_Cube)

        Applies a world transformation to a triangle using the :ref:`view-to-cube transformation matrix <matrix_module>`.

        **Parameters:**

        - `triangle`: A list of points representing the triangle.
        
        - `V_T_Cube`: The transformation matrix from the cube to the world.

        **Returns:**
        - The transformed triangle points.

        .. code-block:: python
            :caption: :mod:`world_transform` method

            @staticmethod
            def world_transform(triangle, V_T_Cube):
                transformed_triangles = []

                for point in triangle:
                        transformed_triangle = V_T_Cube @ point
                        transformed_triangles.append(transformed_triangle)

                return transformed_triangles

------------------------------------------------------------------------------------

    .. method:: camera_transform(object, C_T_V)

        Transforms object points from world coordinates to camera coordinates.

        **Parameters:**
        
        - `object`: A list of points representing the object.

        - `C_T_V`: The transformation matrix from the world to the camera.

        **Returns:**

        - The transformed object points in camera coordinates.

        .. code-block:: python
            :caption: :mod:`camera_transform` method

            @staticmethod
            def camera_transform(object, C_T_V):
                transformed_triangles = []

                for point in object:
                    transformed_triangle = tuple(C_T_V @ point)
                    transformed_triangles.append(transformed_triangle)

                return transformed_triangles

------------------------------------------------------------------------------------

    .. method:: draw_all_cube_points(triangles: List) -> None

        Draws all points of the cube on the camera image.

        .. note::
            This method handles only the triangle points; the actual drawing will be performed in the :mod:`draw_camera_image_point` method.

        **Parameters:**

        - `triangles`: A list of triangles representing the cube.

        .. code-block:: python
            :caption: :mod:`draw_all_cube_points` method

            def draw_all_cube_points(self, triangles: List) -> None:

                for triangle in triangles:
                    for point in triangle.camera_points:
                        self.draw_camera_image_point(point)

------------------------------------------------------------------------------------

    .. method:: draw_camera_image_point(C_point: np.array) -> None

        Draws a single point on the camera image using the camera coordinates from the :mod:`draw_all_cube_points` method.

        **Parameters:**

        - `C_point`: The point in camera coordinates.

        .. code-block:: python
            :caption: :mod:`draw_camera_image_point` method

            def draw_camera_image_point(self, C_point: np.array) -> None:
                I_point = np.matmul(self.I_T_C, C_point)
                u = int(I_point[0] / I_point[2])
                v = int(I_point[1] / I_point[2])
                cv.circle(self.camera_image, (u, v), 5, (255, 0, 0), 2)

------------------------------------------------------------------------------------

    .. method:: draw_all_cube_lines(triangles: List) -> None

        Draws all edges of the cube on the camera image.

        .. note::
            This method handles only the triangle points; the actual drawing will be performed in the :mod:`draw_camera_image_line` method.

        **Parameters:**

        - `triangles`: A list of triangles representing the cube.

        .. code-block:: python
            :caption: :mod:`draw_all_cube_lines` method

            def draw_all_cube_lines(self, triangles : List) -> None:

                for triangle in triangles:
                    for i in range(3):
                        C_point0 = triangle.camera_points[i]
                        C_point1 = triangle.camera_points[(i + 1) % 3]
                        self.draw_camera_image_line(C_point0, C_point1)

------------------------------------------------------------------------------------

    .. method:: draw_camera_image_line(C_point0: np.array, C_point1: np.array) -> None

        Draws a line between two points on the camera image using the camera coordinates given by the :mod:`draw_all_cube_lines` method.

        **Parameters:**

        - `C_point0`: The first point in camera coordinates.

        - `C_point1`: The second point in camera coordinates.

        .. code-block:: python
            :caption: :mod:`draw_camera_image_line` method

            def draw_camera_image_line(self, C_point0: np.array, C_point1: np.array) -> None:
                I_point0 = np.matmul(self.I_T_C, C_point0)
                I_point1 = np.matmul(self.I_T_C, C_point1)

                u0 = int(I_point0[0] / I_point0[2])
                v0 = int(I_point0[1] / I_point0[2])

                u1 = int(I_point1[0] / I_point1[2])
                v1 = int(I_point1[1] / I_point1[2])

                cv.line(self.camera_image, (u0, v0), (u1, v1), (0, 0, 0), 1)

------------------------------------------------------------------------------------

    .. method:: draw_camera_image_arrow(C_point0: np.array, C_point1: np.array) -> None

        Draws an arrow from one point to another on the camera image.

        **Parameters:**

        - `C_point0`: The starting point in camera coordinates.

        - `C_point1`: The ending point in camera coordinates.

        .. code-block:: python
            :caption: :mod:`draw_camera_image_arrow` method

            def draw_camera_image_arrow(self, C_point0: np.array, C_point1: np.array) -> None:
                try:
                    I_point0 = np.matmul(self.I_T_C, C_point0)
                    I_point1 = np.matmul(self.I_T_C, C_point1)

                    u0 = int(I_point0[0] / I_point0[2])
                    v0 = int(I_point0[1] / I_point0[2])

                    u1 = int(I_point1[0] / I_point1[2])
                    v1 = int(I_point1[1] / I_point1[2])

                    cv.arrowedLine(self.camera_image, (u0, v0), (u1, v1), (0, 255, 0), 2)
                except:
                    raise ValueError(f"Could draw normal {C_point0}, {C_point1}")

------------------------------------------------------------------------------------

    .. method:: fill_cube_faces(triangles: List) -> None

        Fills the faces of the cube with a specified color on the camera image.

        .. note::
            The color can be specified in the :ref:`Main Engine Loop <main_module>`.


        **Parameters:**

        - `triangles`: A list of triangles representing the cube.

        .. code-block:: python
            :caption: :mod:`fill_cube_faces` method

            def fill_cube_faces(self, triangles: List) -> None:
                for triangle in triangles:
                    I_points = []

                    for C_point in triangle.camera_points:
                        I_point = np.matmul(self.I_T_C, C_point)
                        
                        u = int(I_point[0] / I_point[2])
                        v = int(I_point[1] / I_point[2])

                        I_points.append((u, v))
                    
                    Poly_Points = np.array(I_points, np.int32)
                    cv.fillPoly(self.camera_image, [Poly_Points], triangle.color)

------------------------------------------------------------------------------------

    .. method:: draw_poly(points: List[np.array]) -> None

        Draws a polygon defined by a list of points on the camera image.

        .. note::
            This method is used to draw a shadow generated by the :ref:`Vector Module <vector_module>`.

        **Parameters:**

        - `points`: A list of points representing the polygon.

        .. code-block:: python
            :caption: :mod:`draw_poly` method

            def draw_poly(self, points: List[np.array]) -> None:

                I_points = []

                for point in points:

                    I_point = np.matmul(self.I_T_C, point)
                        
                    u = int(I_point[0] / I_point[2])
                    v = int(I_point[1] / I_point[2])

                    I_points.append((u, v))
                    
                Poly_Points = np.array(I_points, np.int32)
                hull = cv.convexHull(Poly_Points)
                cv.fillPoly(self.camera_image, [hull], (50,50,50))

------------------------------------------------------------------------------------

    .. method:: reset_camera_image() -> None

        Resets the camera image to a blank (white) image.

        .. code-block:: python
            :caption: :mod:`reset_camera_image` method

            def reset_camera_image(self) -> None:
                self.camera_image.fill(255)

------------------------------------------------------------------------------------

    .. method:: get_camera_vectors(V_T_C: np.array) -> np.array

        Calculates the camera's forward vector in world coordinates. 

        **Parameters:**

        - `V_T_C`: The transformation matrix from the :ref:`world-to-camera <matrix_module>`.

        **Returns:**
        - The forward vector of the camera in world coordinates.

        .. code-block:: python
            :caption: :mod:`get_camera_vectors` method

            @staticmethod
            def get_camera_vectors(V_T_C: np.array) -> np.array:
                rotation_matrix = V_T_C[:3, :3]
                forward_vector = -rotation_matrix[:, 2]
                camera_position = V_T_C[:3, 3]
                final_vector_x = forward_vector[0] + camera_position[0]
                final_vector_y = forward_vector[1] + camera_position[1]
                final_vector_z = forward_vector[2] + camera_position[2]
                return (final_vector_x, final_vector_y, final_vector_z)
