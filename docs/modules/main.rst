.. _main_module:

Engine Module
=============

This module defines the :mod:`Engine` class, which acts as the core of the rendering engine. Here is the outlined code corresponding to the pipeline.

.. class:: Engine()

    The :mod:`Engine` class serves as the central hub for the 3D rendering process, managing everything from camera transformations to backface culling, clipping and rendering frames.

    **Attributes:**

    - **camera_model**: Instance of :mod:`CameraModel` to manage the camera's intrinsic properties and transformations.
    - **window**: Instance of :mod:`Window` to handle the rendering window and user input.
    - **clipping_space**: Instance of :mod:`Clipping_Space` for handling object clipping within the view frustum.
    - **fps_counter**: Instance of :mod:`FpsCounter` for managing and displaying the frames per second (FPS).
    - **V_T_C**: View-to-camera transformation matrix.
    - **C_T_V**: Camera-to-view transformation matrix (inverse of :mod:`V_T_C`).
    - **V_T_Cube**: View-to-cube transformation matrix.
    - **render_list**: List of objects or triangles to render.
    - **mesh_list**: List of 3D mesh objects to be transformed and rendered.


**Methods**

    .. method:: __init__()

        Initializes the :mod:`Engine` class by setting up the camera model, window, clipping space, FPS counter, and transformation matrices.

        **Code:**

        .. code-block:: python
            :caption: :mod:`__init__` method

            def __init__(self):

                self.camera_model = CameraModel(0.00452, 0.00254, 0.004, 1280, 720, 1280/2, 720/2)
                self.window = Window()
                self.clipping_space = Clipping_Space()
                self.fps_counter = FpsCounter(60)
                self.V_T_C = Matrix_Functions.create_homogeneous_transformation_matrix(0, 0, 0, 0, 0, 0, 0)
                self.C_T_V = np.linalg.inv(self.V_T_C)
                self.V_T_Cube = Matrix_Functions.create_homogeneous_transformation_matrix(2, 0, 1, 0, 0, 0, 0)
                self.render_list = []
                self.mesh_list = []

    .. method:: fps_setter()

        Updates and displays the current frames per second (FPS) on the camera image.

        **Code:**

        .. code-block:: python
            :caption: :mod:`fps_setter` method

            def fps_setter(self):
                fps = self.fps_counter.get_fps_filtered()
                cv.putText(self.camera_model.camera_image, f"FPS: {fps:.0f}", (10, 30), cv.FONT_HERSHEY_PLAIN, 1.2, (0, 255, 0), 1)

    .. method:: is_triangle_facing_camera(normal, tri, cam)

        Determines if a triangle is facing the camera by calculating the dot product of the triangle's normal and the vector from the camera to the triangle.

        **Parameters:**
        - `normal`: The normal vector of the triangle.
        - `tri`: The centroid of the triangle.
        - `cam`: The camera position vector.

        **Returns:**
        - The dot product, indicating whether the triangle is facing the camera (negative value) or not (positive value).

        **Code:**

        .. code-block:: python
            :caption: :mod:`is_triangle_facing_camera`

            def is_triangle_facing_camera(self, normal, tri, cam):
                dot_product = ( normal[0] * (tri[0] - cam[0]) +
                                normal[1] * (tri[1] - cam[1]) +
                                normal[2] * (tri[2] - cam[2])   )
                return dot_product

    .. method:: main()

        The main loop of the engine, responsible for updating the window, handling transformations, clipping, and rendering the 3D objects.

        **Code:**

        .. code-block:: python
            :caption: :mod:`main` method

            def main(self):

                # file_path = r"utils\resources\VideoShip.obj"
                # struc = Structure_Generator.load_from_obj(file_path)
                # self.mesh_list.extend(struc)

                cube = Cube(size=1, pos_x=0, pos_y=0, pos_z=0)
                self.mesh_list.extend(cube.mesh)

                while True:

                    # self.window.handle_movement()
                    self.fps_counter.update()
                    self.camera_model.reset_camera_image()

                    self.V_T_C, self.C_T_V, self.V_T_Cube = Matrix_Functions.homogeneous_transformation(self.window)
                    camera_vector_world = self.camera_model.get_camera_vectors(self.V_T_C)

                    visiable_triangles = []

                    for triangle in self.mesh_list:

                        triangle.world_points = self.camera_model.world_transform(triangle.points, self.V_T_Cube)
                        triangle.normal, normal_start, normal_end, triangle.centroids = CalculateNormal.normal(triangle.world_points)
                        transformed_normals = self.camera_model.camera_transform([normal_start, normal_end], self.C_T_V)

                        if self.window.show_normals:
                            self.camera_model.draw_camera_image_arrow(transformed_normals[0], transformed_normals[1])

                        if self.is_triangle_facing_camera(triangle.normal, triangle.centroids, camera_vector_world) < 0.0:

                            light_direction = (1, -0.5, -0.8)
                            triangle.ilm = Color.intensity(light_direction, triangle.normal)
                            triangle.color = Color.adjust_bgr_intensity(Color.ALICE_BLUE, triangle.ilm)

                            triangle.camera_points = self.camera_model.world_transform(triangle.world_points, self.C_T_V)
                            visiable_triangles.append(triangle)

                    sorted_list = sorted(visiable_triangles, key=lambda triangle: triangle.centroids[2], reverse=True)

                    shadow_points = Shadow.get_shadow(self.mesh_list, light_direction)
                    shadow_points_camera = self.camera_model.world_transform(shadow_points, self.C_T_V)
                    self.camera_model.draw_poly(shadow_points_camera)

                    clipped_triangles = []
                    clipped_triangles.extend(self.clipping_space.cube_in_space(sorted_list))

                    self.camera_model.draw_all_cube_lines(clipped_triangles)
                    if self.window.show_points:
                        self.camera_model.draw_all_cube_points(clipped_triangles)
                    if self.window.show_planes:
                        self.camera_model.fill_cube_faces(clipped_triangles)

                    self.fps_setter()
                    self.window.window_show(self.camera_model)

    **Usage:**

    To use the :mod:`Engine` class, simply create an instance and call the `main()` method to start the rendering loop.

    **Code:**
    
    .. code-block:: python
        :caption: :mod:`Engine` class

        engine = Engine()
        engine.main()
