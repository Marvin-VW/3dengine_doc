.. _vector_module:

Calculate Normal and Shadow Module
==================================

This module contains the `CalculateNormal` and `Shadow` classes, which provide methods for normal and vector calculation and shadow calculation.

Class Overview
--------------

1. **CalculateNormal**: A class that provides methods for calculating normal vectors of triangles in 3D space.
2. **Shadow**: A class that provides methods for calculating shadow projections of 3D triangles onto a plane.


--------------------------------------------------------------------------------------------------------------------------------

.. class:: CalculateNormal()

This class contains static methods to calculate the normal vector of a triangle.

**Methods:**

    .. method:: vector(point1, point2)

    This method calculates the vector between two points.

    **Parameters:**
        - `point1 (np.ndarray)`: The first point in 3D space.

        - `point2 (np.ndarray)`: The second point in 3D space.

    **Returns:**
        - `np.ndarray`: The vector from `point1` to `point2`.

    **Code:**

    .. code-block:: python
        :caption: :mod:`vector` method

        @staticmethod    
        def vector(point1, point2):
            return point2 - point1


------------------------------------------------------------------------------

    .. method:: normal(triangle, scale = 0.5)

    
    This method calculates the normal vector of a triangle in 3D space.

    **Parameters:**

        - `triangle (list of np.ndarray)`: A list containing three 3D points representing the vertices of the triangle.

        - `scale (float, optional)`: A scaling factor for the normal vector (default is 0.5).

    
    **Returns:**

        - `tuple`: A tuple containing:

        - `scaled_normal (np.ndarray)`: The scaled normal vector.

        - `normal_start (np.ndarray)`: The starting point of the normal vector.

        - `normal_end (np.ndarray)`: The end point of the normal vector.

        - `centroid (np.ndarray)`: The centroid of the triangle.


    .. code-block:: python
        :caption: :mod:`normal` method

        @staticmethod
        def normal(triangle, scale = 0.5):
                    
            p1 = triangle[0].flatten()
            p1 = p1[:3]

            p2 = triangle[1].flatten()
            p2 = p2[:3]

            p3 = triangle[2].flatten()
            p3 = p3[:3]

            # vectors
            vec1 = CalculateNormal.vector(p1, p2)
            vec2 = CalculateNormal.vector(p1, p3)
            
            # normal vector
            normal_vector = np.cross(vec1, vec2)
            
            # normalize to unit length
            norm = np.linalg.norm(normal_vector)
            if norm == 0:
                norm = 0.5
            
            normalized_normal = normal_vector / norm
            
            # mid of triangle
            centroid = (p1 + p2 + p3) / 3

            # scale vector
            scaled_normal = normalized_normal * scale

            # z,x,y
            scaled_normal = (scaled_normal[0], scaled_normal[1], scaled_normal[2])

            normal_start = centroid
            normal_end = centroid + scaled_normal

            # reshape to homogenous
            normal_start = np.vstack([normal_start.reshape(-1, 1), [[1]]])
            normal_end = np.vstack([normal_end.reshape(-1, 1), [[1]]])

            return scaled_normal, normal_start, normal_end, centroid

-------------------------------------------------------------------------------------------------------

.. class:: Shadow()

This class provides static methods to calculate the shadow projections of 3D triangles onto a plane.

**Methods:**

    .. method:: get_shadow(triangles, light_vec)

    This method calculates the shadow projection of triangles onto a plane based on a given light vector.

    **Parameters:**
    - `triangles (list)`: A list of triangle objects, where each triangle contains a list of 3D world points.
    - `light_vec (np.ndarray)`: A 3D vector representing the direction of the light source.

    **Returns:**
    - `list of np.ndarray`: A list of points representing the shadow projection on the plane.


    .. code-block:: python
        :caption: :mod:`get_shadow` method

        @staticmethod
        def get_shadow(triangles, light_vec):

            shadow_points = []
            plane_normal = np.array([0, 0, 1])

            for triangle in triangles:
                for point in triangle.world_points:
                    shadow_points.append(Shadow.find_intersection(plane_normal, point[:3].flatten(), light_vec))

            unique_array = list(map(np.array, set(tuple(arr) for arr in shadow_points)))
            shadow_points = []

            for point in unique_array:
                shadow_points.append(np.vstack([point.reshape(-1, 1), [[1]]]))

            return shadow_points

---------------------------------------------------------------------------------------------------------------

.. method:: find_intersection(plane_normal, line_point, line_dir, plane_d=2)

    This method calculates the intersection point between a line and a plane.

    .. note::
        This function is used by the :mod:`get_shadow` method.

    **Parameters:**

    - `plane_normal (np.ndarray)`: The normal vector of the plane.

    - `line_point (np.ndarray)`: A point on the line.

    - `line_dir (np.ndarray)`: The direction vector of the line.

    - `plane_d (float, optional)`: The plane offset from the origin (default is 2).


    **Returns:**

    - `np.ndarray or None`: The intersection point, or `None` if the line is parallel to the plane.

    .. code-block:: python
        :caption: :mod:`find_intersection` method

        @staticmethod
        def find_intersection(plane_normal, line_point, line_dir, plane_d=2):

            a, b, c = plane_normal
            x0, y0, z0 = line_point
            vx, vy, vz = line_dir
            
            denominator = a * vx + b * vy + c * vz
            
            if denominator == 0:
                return None
            
            t = -(a * x0 + b * y0 + c * z0 + plane_d) / denominator
            
            intersection_point = np.array([x0 + t * vx, y0 + t * vy, z0 + t * vz])
            
            return intersection_point

    .. warning::
        The shadow is only cast on the bottom plane. While the height can be adjusted, it will not affect other objects.