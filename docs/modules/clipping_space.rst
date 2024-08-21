.. _clipping_module:

Clipping Space Module
=====================

This module defines the `Clipping_Space` class, which clips triangles against planes (i.e., the view frustum).

The module consists of the following class:

- `Clipping_Space`: Represents the clipping space operations, including normalization and determining which parts of a 3D object are within the visible space.

.. class:: Clipping_Space()

    **Attributes:**

    - **projection_matrix**: The matrix used to normalize 3D points.

    - **border**: The boundary limit for clipping.

    **Methods:**

    .. method:: __init__()

        Initializes the `Clipping_Space` class with a default normalization matrix matrix and border.

        .. code-block:: python
            :caption: :mod:`__init__` method

            def __init__(self) -> None:

                fov = np.deg2rad(64/1.77)
                aspect_ratio = 1.77
                near = 1
                far = 100.0
                self.projection_matrix = self.create_perspective_projection_matrix(fov, aspect_ratio, near, far)
                self.border = 1


--------------------------------------------------------------------------------------------------------------------------------

    .. method:: create_perspective_projection_matrix(fov, aspect_ratio, near, far)

        Creates a normalization matrix based on the field of view, aspect ratio, near, and far clipping planes.

        **Parameters:**

        - `fov`: The field of view in radians.

        - `aspect_ratio`: The aspect ratio of the view.

        - `near`: The near clipping plane distance.

        - `far`: The far clipping plane distance.

        **Returns:**
        - A NumPy array representing the normalization matrix.

        .. code-block:: python
            :caption: :mod:`create_perspective_projection_matrix` method

            def create_perspective_projection_matrix(self, fov, aspect_ratio, near, far):
                
                f = 1.0 / np.tan(fov / 2)
                nf = 1 / (near - far)
                
                return np.array([
                    [f / aspect_ratio, 0, 0, 0],
                    [0, f, 0, 0],
                    [0, 0, (far + near) * nf, (2 * far * near) * nf],
                    [0, 0, -1, 0]
                ])

-----------------------------------------------------------------------------------------------------------------------------------------

    .. method:: cube_in_space(cube_points: list)

        Processes a list of Triangles and determines which triangles (from the object) are within the View Frustum, clipping those that are partially inside.

        **Parameters:**

        - `cube_points`: A list of triangles.

        **Returns:**

        - A list of triangles that are fully or partially within the clipping space.

        .. code-block:: python
            :caption: :mod:`cube_in_space` method

            def cube_in_space(self, cube_points: list):

                full_triangle_list = []

                # For each triangle:
                for triangle in cube_points:

                    full_point_list = []
                    inside_point = []
                    outside_point = []

                    for point in triangle.camera_points:
                        clip_space_point = np.matmul(self.projection_matrix, point)
                        ndc_point = clip_space_point / clip_space_point[3]

                        # Check which points are in space
                        if -self.border <= ndc_point[0] <= self.border and -self.border <= ndc_point[1] <= self.border and 1 <= ndc_point[2] <= 100:
                            inside_point.append(ndc_point)
                        else:
                            outside_point.append(ndc_point)

                    # All points inside -> return triangle
                    if len(inside_point) == 3:
                        full_triangle_list.append(triangle)

                    # No points inside -> return none
                    elif len(inside_point) == 0:
                        continue

                    # One point inside -> two new points
                    elif len(inside_point) == 1:
                        _, new_point1 = self.find_intersection_with_plane(inside_point[0], outside_point[0])
                        _, new_point2 = self.find_intersection_with_plane(inside_point[0], outside_point[1])

                        full_point_list.append(inside_point[0])
                        full_point_list.append(np.vstack([new_point1.reshape(-1, 1), [[1]]]))
                        full_point_list.append(np.vstack([new_point2.reshape(-1, 1), [[1]]]))

                        for pos, point in enumerate(full_point_list):
                            full_point_list[pos] = self.transfer_back_camera_space(point)
                            triangle.camera_points = full_point_list

                        full_triangle_list.append(triangle)

                    # Two points inside -> two new triangles
                    elif len(inside_point) == 2:
                        _, new_point1 = self.find_intersection_with_plane(inside_point[0], outside_point[0])
                        _, new_point2 = self.find_intersection_with_plane(inside_point[1], outside_point[0])

                        # First triangle
                        full_point_list = []
                        full_point_list.append(np.vstack([new_point1.reshape(-1, 1), [[1]]]))
                        full_point_list.append(np.vstack([new_point2.reshape(-1, 1), [[1]]]))
                        full_point_list.append(inside_point[0])
                        
                        for pos, point in enumerate(full_point_list):
                            full_point_list[pos] = self.transfer_back_camera_space(point)
                        
                        triangle_new1 = copy.deepcopy(triangle)
                        triangle_new1.camera_points = full_point_list
                        full_triangle_list.append(triangle_new1)
                        
                        # Second triangle
                        full_point_list = []
                        full_point_list.append(inside_point[0])
                        full_point_list.append(np.vstack([new_point2.reshape(-1, 1), [[1]]]))
                        full_point_list.append(inside_point[1])
                        
                        for pos, point in enumerate(full_point_list):
                            full_point_list[pos] = self.transfer_back_camera_space(point)
                        
                        triangle_new2 = copy.deepcopy(triangle)
                        triangle_new2.camera_points = full_point_list
                        full_triangle_list.append(triangle_new2)

                return full_triangle_list

-----------------------------------------------------------------------------------------------------------------------------

    .. method:: intersection_with_plane_x(A, B, x)

        Calculates the intersection of a line segment between two points and a plane parallel to the YZ-plane at a given x-coordinate.

        **Parameters:**

        - `A`: The first point of the line segment.

        - `B`: The second point of the line segment.

        - `x`: The x-coordinate of the plane.

        **Returns:**

        - The intersection point as a NumPy array, or `None` if there is no intersection.

        .. code-block:: python
            :caption: :mod:`intersection_with_plane_x` method

            @staticmethod
            def intersection_with_plane_x(A, B, x):
                if A[0] == B[0]:
                    return None
                t = (x - A[0]) / (B[0] - A[0])
                if 0 <= t <= 1:
                    intersection = A + t * (B - A)
                    return intersection
                return None

-----------------------------------------------------------------------------------------------------------------------------------

    .. method:: intersection_with_plane_y(A, B, y)

        Calculates the intersection of a line segment between two points and a plane parallel to the XZ-plane at a given y-coordinate.

        **Parameters:**

        - `A`: The first point of the line segment.

        - `B`: The second point of the line segment.

        - `y`: The y-coordinate of the plane.

        **Returns:**

        - The intersection point as a NumPy array, or `None` if there is no intersection.

        .. code-block:: python
            :caption: :mod:`intersection_with_plane_y` method

            @staticmethod
            def intersection_with_plane_y(A, B, y):
                if A[1] == B[1]:
                    return None
                t = (y - A[1]) / (B[1] - A[1])
                if 0 <= t <= 1:
                    intersection = A + t * (B - A)
                    return intersection
                return None

---------------------------------------------------------------------------------------------------------------------------------

    .. method:: find_intersection_with_plane(point1, point2)

        Finds the intersection points between a line segment and the clipping planes.

        **Parameters:**

        - `point1`: The first point of the line segment.

        - `point2`: The second point of the line segment.

        **Returns:**

        - The plane where the intersection occurs and the intersection point as a NumPy array.

        .. code-block:: python
            :caption: :mod:`find_intersection_with_plane` method

            def find_intersection_with_plane(self, point1, point2):

                planes_x = [-self.border, self.border]
                planes_y = [-self.border, self.border]

                A = point1.flatten()
                A = A[:3]
                B = point2.flatten()
                B = B[:3]

                # Get intersections with borders
                intersections = {
                    "left": self.intersection_with_plane_x(A, B, planes_x[0]),
                    "right": self.intersection_with_plane_x(A, B, planes_x[1]),
                    "bottom": self.intersection_with_plane_y(A, B, planes_y[0]),
                    "top": self.intersection_with_plane_y(A, B, planes_y[1])
                }

                # Delete points with "None"
                valid_intersections = {}
                for plane, point in intersections.items():
                    if point is not None:
                        valid_intersections[plane] = point

                if not valid_intersections:
                    return None, None

                # Get closest border
                closest_intersection = min(valid_intersections, key=lambda k: np.linalg.norm(valid_intersections[k] - A))

                return closest_intersection, valid_intersections[closest_intersection]

-------------------------------------------------------------------------------------------------------------------------------------------------------
    
    .. method:: transfer_back_camera_space(point)

        Transfers a point from the clipping space back to the camera space by inverting the projection matrix transformation and normalize by w.

        **Parameters:**
        - `point`: The point in clipping space as a NumPy array.

        **Returns:**
        - The point converted back to camera space as a NumPy array.

        .. code-block:: python
            :caption: :mod:`transfer_back_camera_space` method

            def transfer_back_camera_space(self, point):
                # Invert the projection transformation
                converted_point = np.matmul(np.linalg.inv(self.projection_matrix), point)
                converted_point /= converted_point[3]  # Normalize by w to get back the original point

                return converted_point
