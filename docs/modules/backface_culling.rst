.. _backface_culling_model:

Backface Culling Module
=======================

Backface culling is a computer graphics technique used to improve rendering efficiency by eliminating the need to triangles that are not visible to the camera.
This technique is based on the principle that when an object's surface faces away from the camera, it does not contribute to the final image, and thus, rendering it would be unnecessary and wasteful.

In this module we are dealing with the following code snippet of the Engine Loop:


    .. code-block:: python
        :caption: :mod:`main` method
        :linenos:

        def main(self):

            ...

            for triangle in self.mesh_list:

                triangle.world_points = self.camera_model.world_transform(triangle.points, self.V_T_Cube)
                triangle.normal, normal_start, normal_end, triangle.centroids = CalculateNormal.normal(triangle.world_points)
                transformed_normals = self.camera_model.camera_transform([normal_start, normal_end], self.C_T_V)

                if self.window.show_normals:
                    self.camera_model.draw_camera_image_arrow(transformed_normals[0], transformed_normals[1])

                if self.is_triangle_facing_camera(triangle.normal, triangle.centroids, camera_vector_world) < 0.0:

                        ...


------------------------------------------------------------------------------------------------------------------------

Without Backface Culling the Cube would look like the following:

.. image:: ../resources/backface_culling/without.png
  :width: 800
  :alt: without Backface Culling


--------------------------------------------------------------------------------------------------------------------------

With Backface Culling the Cube would look like the following:

.. image:: ../resources/backface_culling/with.png
  :width: 800
  :alt: with Backface Culling

I guess you can see the difference. But whats the math behind this technique?

1. **Surface Normals Calculation**: 
Each polygon in a 3D object has a surface normal, which is a vector perpendicular to the polygon's surface. This normal helps determine the orientation of the polygon relative to the camera.

The normal is calculated the following way, with the help of the cross product:

.. image:: ../resources/backface_culling/cross.png
  :width: 800
  :alt: cross product


.. image:: ../resources/backface_culling/normal.png
  :width: 800
  :alt: normal


.. note::
    a x b (a cross b) is the vector perpendicular to the triangle's surface. This vector is called the normal.


.. warning::
    It is important that all triangle points are clockwise; otherwise, the normals will point in the wrong direction (equivalent to b x a).


Now that we have the surface normals and the normal of the camera (if you missed that, check out the Initialization module), we can move on to the next step.


2. **Dot Product Test**: 

The angle between the surface normal and the camera's view direction is calculated using the dot product. If the result of this dot product is positive (1), it means the polygon is facing away from the camera. If it's negative (-1), the polygon is facing towards the camera.

.. image:: ../resources/backface_culling/dot.png
  :width: 800
  :alt: dot product

To keep only the faces visible to the camera, we need to eliminate all faces with a negative dot product. And that's the magic behind this module. Check out the code further down the page.


**Benefits**:

- **Performance Improvement**: By not rendering polygons that aren't visible, the system saves computational resources, allowing for faster rendering and potentially higher frame rates.

- **Simplified Shading**: Since only the visible polygons are processed, the shading and lighting calculations are simplified.



**Code**

