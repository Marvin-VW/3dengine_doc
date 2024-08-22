.. _window_module:

Window Class
============

The `Window Class` module provides a framework for handling a camera system's interaction with a 3D cube model. It includes functionalities such as window creation, camera movement, and interaction through mouse events and keyboard inputs.

.. class:: Window()


    .. method:: __init__()

    The :mod:`__init__` method initializes the :mod:`Window` class by setting default values for camera and cube system parameters, window names, mouse state, and update intervals.

    .. code-block:: python
        :caption: :mod:`__init__` method

        def __init__(self):
            self.camera_system_translation_x = 10000
            self.camera_system_translation_y = 10000
            self.camera_system_translation_z = 10000
            self.camera_system_rotation_roll = 2700
            self.camera_system_rotation_pitch = 0
            self.camera_system_rotation_yaw = 2700

            self.cube_system_translation_x = 16000
            self.cube_system_translation_y = 10000
            self.cube_system_translation_z = 10000
            self.cube_system_rotation_roll = 0
            self.cube_system_rotation_pitch = 0
            self.cube_system_rotation_yaw = 300
            self.cube_system_scale = 1

            self.camera_window_name = "camera settings"
            self.cube_window_name = "cube settings"

            self.mouse_is_pressed = False
            self.right_button_mode = False
            self.last_mouse_position = (0, 0)

            self.last_update_time = time.time()
            self.update_interval = 0.05
            
            self.show_normals = False
            self.show_planes = False
            self.show_points = False

            self.window_creator()

-----------------------------------------------------------------------------------------------

    .. method:: window_creator()

    The :mod:`window_creator` method sets up the necessary OpenCV windows and trackbars for adjusting camera and cube parameters.

    .. code-block:: python
        :caption: :mod:`window_creator` method

        def window_creator(self):
            cv.namedWindow("image window", cv.WINDOW_AUTOSIZE)
            cv.namedWindow("camera settings", cv.WINDOW_NORMAL)
            cv.namedWindow("cube settings", cv.WINDOW_NORMAL)
            ...
            cv.setMouseCallback("image window", self.mouse_event_handler)

--------------------------------------------------------------------------------------------------

    .. method:: toggle_normal(), toggle_planes(), toggle_points()

    These methods toggle the display of normals, planes, and points on the cube.

    .. note::
        These functions control the settings in the :ref:`Main Engine Loop <main_module>`.

    .. code-block:: python
        :caption: :mod:`toggle_normal` method

        def toggle_normal(self, value):
            self.show_normals = not self.show_normals

    .. code-block:: python
        :caption: :mod:`toggle_planes` method

        def toggle_planes(self, value):
            self.show_planes = not self.show_planes

    .. code-block:: python
        :caption: :mod:`toggle_points` method

        def toggle_points(self, value):
            self.show_points = not self.show_points

-----------------------------------------------------------------------------------------------------

    .. method:: window_show()

    The :mod:`window_show` method displays the current frame of the camera.

    .. code-block:: python
        :caption: :mod:`window_show` method

        def window_show(self, class_cam):
            cv.imshow("image window", class_cam.camera_image)
            cv.waitKey(1)

--------------------------------------------------------------------------------------------------------

    .. method:: get_*()

    These methods retrieve the current values of the camera and cube system parameters.

    .. code-block:: python
        :caption: :mod:`get_camera_system_translation_x` method

        def get_camera_system_translation_x(self):
            return cv.getTrackbarPos("X", self.camera_window_name)


    .. code-block:: python
        :caption: :mod:`get_camera_system_translation_` method

        def get_camera_system_translation_y(self):
            return cv.getTrackbarPos("Y", self.camera_window_name)

        ...

----------------------------------------------------------------------------------------------------------

    .. method:: handle_movement()

    The :mod:`handle_movement` method manages the camera's movement in response to keyboard inputs.

    .. code-block:: python
        :caption: :mod:`handle_movement` method

        def handle_movement(self):
            camera_speed = 100
            current_time = time.time()
            if current_time - self.last_update_time >= self.update_interval:
                self.last_update_time = current_time
                
                key = cv.waitKey(30) & 0xFF
            
                if key == ord('d'):
                    self.move_camera('forward', camera_speed)
                if key == ord('a'):
                    self.move_camera('backward', camera_speed)
                if key == ord('w'):
                    self.move_camera('left', camera_speed)
                if key == ord('s'):
                    self.move_camera('right', camera_speed)
                if key == ord('q'):
                    self.move_camera('down', camera_speed)
                if key == ord('e'):
                    self.move_camera('up', camera_speed)


--------------------------------------------------------------------------------------------------------------

    .. method:: move_camera()

    The :mod:`move_camera` method calculates the direction vectors based on the camera's current yaw and pitch and updates the camera's position accordingly.

    .. note::
        This way, the camera movement using W, A, S, and D is not influenced by the direction you're looking at.

    .. code-block:: python
        :caption: :mod:`move_camera` method

        def move_camera(self, direction, speed):
            # Calculate vectors
            yaw = np.deg2rad(self.camera_system_rotation_yaw / 10.0)
            pitch = np.deg2rad(self.camera_system_rotation_pitch / 10.0)

            forward_x = np.cos(pitch) * np.cos(yaw)
            forward_y = np.cos(pitch) * np.sin(yaw)
            forward_z = np.sin(pitch)

            right_x = np.sin(yaw)
            right_y = -np.cos(yaw)
            right_z = 0

            up_x = 0
            up_y = 0
            up_z = 1

            if direction == 'forward':
                self.camera_system_translation_x += int(forward_x * speed)
                self.camera_system_translation_y += int(forward_y * speed)
                self.camera_system_translation_z += int(forward_z * speed)
            elif direction == 'backward':
                self.camera_system_translation_x -= int(forward_x * speed)
                self.camera_system_translation_y -= int(forward_y * speed)
                self.camera_system_translation_z -= int(forward_z * speed)
            elif direction == 'left':
                self.camera_system_translation_x -= int(right_x * speed)
                self.camera_system_translation_y -= int(right_y * speed)
            elif direction == 'right':
                self.camera_system_translation_x += int(right_x * speed)
                self.camera_system_translation_y += int(right_y * speed)
            elif direction == 'up':
                self.camera_system_translation_z += int(up_z * speed)
            elif direction == 'down':
                self.camera_system_translation_z -= int(up_z * speed)
                
            self.camera_system_translation_x = np.clip(self.camera_system_translation_x, 0, 20000)
            self.camera_system_translation_y = np.clip(self.camera_system_translation_y, 0, 20000)
            self.camera_system_translation_z = np.clip(self.camera_system_translation_z, 0, 20000)
            cv.setTrackbarPos("X", self.camera_window_name, self.camera_system_translation_x)
            cv.setTrackbarPos("Y", self.camera_window_name, self.camera_system_translation_y)
            cv.setTrackbarPos("Z", self.camera_window_name, self.camera_system_translation_z)

---------------------------------------------------------------------------------------------------------------+

    .. method:: mouse_event_handler()

    The :mod:`mouse_event_handler` method handles the mouse interactions with the window, allowing users to rotate the camera view by dragging or clicking inside the window by right-click.

    .. note:: 
        With the left click, you can drag your view like on Google Maps. With the right click, your mouse movement will control the camera, and a double right-click will exit this mode.

    .. code-block:: python
        :caption: :mod:`mouse_event_handler` method

        def mouse_event_handler(self, event, x, y, flags, param):
            if event == cv.EVENT_LBUTTONDOWN:
                self.mouse_is_pressed = True
                self.last_mouse_position = (x, y)
            elif event == cv.EVENT_LBUTTONUP:
                self.mouse_is_pressed = False
            elif event == cv.EVENT_RBUTTONDOWN:
                self.right_button_mode = True
            elif event == cv.EVENT_RBUTTONDBLCLK:
                self.right_button_mode = False
                self.last_mouse_position = (x, y)
            elif event == cv.EVENT_MOUSEMOVE:
                if self.mouse_is_pressed or self.right_button_mode:
                    dx = x - self.last_mouse_position[0]
                    dy = y - self.last_mouse_position[1]
                    self.camera_system_rotation_yaw += dx
                    self.camera_system_rotation_roll += dy 
                    if self.camera_system_rotation_yaw > 3600:
                        self.camera_system_rotation_yaw -= 3599
                    if self.camera_system_rotation_roll > 3600:
                        self.camera_system_rotation_roll -= 3599
                    if self.camera_system_rotation_yaw < 0:
                        self.camera_system_rotation_yaw += 3599
                    if self.camera_system_rotation_roll < 0:
                        self.camera_system_rotation_roll += 3599
                    cv.setTrackbarPos("Yaw", self.camera_window_name, self.camera_system_rotation_yaw)
                    cv.setTrackbarPos("Roll", self.camera_window_name, self.camera_system_rotation_roll)
                    self.last_mouse_position = (x, y)
