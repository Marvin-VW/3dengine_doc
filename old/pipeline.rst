===========================
3D Engine Pipeline Overview
===========================

This document outlines the pipeline of the 3D engine, detailing the steps from object creation to the final rendering of a scene.

Pipeline Stages
===============

1. Object Initialization and Loading
------------------------------------

**Object Creation**:
   - Objects like :mod:`Cube` and :mod:`Rectangle` are instantiated with their respective size and initial positions.
   - :mod:`self.mesh_list.extend(cube.mesh)` adds the mesh data (triangles) of the created object to the main mesh list for rendering.

   For more details, check out the :ref:`Shape Module <shape_module>`.

**Optional Object Loading**:
   - Objects can also be loaded from external files like :mod:`.obj` files using methods such as :mod:`Structure_Generator.load_from_obj`.

   Refer to the :ref:`Import Module <import_module>` module for more information on loading and handling :mod:`.obj` files.

2. Main Loop
------------

   - The core of the engine runs in a continuous loop where the scene is updated and rendered every frame.

3. Camera and Transformations
-----------------------------

**Camera Reset**:
   - The camera image is reset using :mod:`self.camera_model.reset_camera_image()`.

   For a closer look of this function, review the :ref:`Camera Module <camera_model>`.

**Homogeneous Transformations**:
   - Transformation matrices are generated using :mod:`Matrix_Functions.homogeneous_transformation(self.window)`, which calculate the view-to-camera (:mod:`V_T_C`), camera-to-view (:mod:`C_T_V`), and object-to-camera (:mod:`V_T_Cube`) transformations.

   To dive deeper into the matrices, check out the :ref:`Matrix Functions Module <matrix_module>`.

**World to Camera Space Transformation**:
   - The world points of each triangle are transformed into camera space using :mod:`self.camera_model.world_transform`.

   These transformations are part of the :ref:`Camera Module <camera_model>` using the matrices of the :ref:`Matrix Functions Module <matrix_module>`.

4. Backface Culling and Lighting Calculations
----------------------------------------------

**Normal Calculation**:
   - For each triangle, the normal vector and centroids are calculated using :mod:`CalculateNormal.normal`.
   
   Normal calculations are handled in the :ref:`Vector Module <vector_module>` using the :mod:`CalculateNormal` class.


**Backface Culling**:
   - The :mod:`is_triangle_facing_camera` function in the :ref:`Main Engine Loop <main_module>` checks if the triangle is facing the camera by comparing the normal with the camera vector. Only visible triangles are processed further.

**Lighting Calculations**:
   - If the triangle is visible, the lighting intensity is calculated based on the light direction using :mod:`Color.intensity` and :mod:`Color.adjust_bgr_intensity`.

   Lighting calculations are managed by the :ref:`Color Module <color_module>`.

5. Shadow Calculation
---------------------

   - Shadows are computed for the scene based on the light direction using :mod:`Shadow.get_shadow`.
   - These shadow points are also transformed into camera space using :mod:`self.camera_model.camera_transform` in the :ref:`Camera Module <camera_model>`.

   Shadow calculations are found in the :ref:`Vector Module <vector_module>` using the :mod:`Shadow` class.

6. Depth Sorting
----------------

**Depth Sorting**:
   - Visible triangles are sorted based on their depth (z-coordinate of centroids) using :mod:`sorted`.

   Sorting is typically handled within the :ref:`Main Engine Loop <main_module>`.

7. Frustum Clipping
--------------------

**Clipping**:
   - Triangles are clipped against the view frustum to ensure that only the visible parts are rendered, using :mod:`self.clipping_space.cube_in_space`.

   Clipping operations are done by the :ref:`Clipping Module <clipping_module>`.

8. Rendering
------------

**Shadow Rendering**:
   - Shadows are rendered on the scene using the transformed shadow points.

   The shadow points are transformed into view space using the :mod:`I_T_C` Matrix in the :ref:`Camera Model Module <camera_model>`.

**Settings**:
   - Depending on the settings, different aspects of the triangles are drawn:
       - **Normals** are drawn if :mod:`window.show_normals` is enabled.
       - **Triangle Lines** and **Points** are drawn if :mod:`window.show_points` is enabled.
       - **Triangle Faces** are filled if :mod:`window.show_planes` is enabled.

   Rendering settings and operations are managed by the :ref:`Window Module <window_module>`.

**Frame Rate Management**:
   - The frame rate is controlled using :mod:`self.fps_setter()` to ensure smooth rendering.

   Frame rate management is covered in the :ref:`FPS Module <fps_module>`.

9. Display
----------

   - The final image, including the rendered objects and shadows, are displayed on the screen using :mod:`window.window_show`.

   The display process is controlled by the :ref:`Window Module <window_module>`  