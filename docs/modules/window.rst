.. _window_module:

Window Class
============

The `Window` class provides an interface for interacting with camera and cube systems in a graphical environment using OpenCV. It allows the user to control the position, rotation, and scale of both systems using trackbars and mouse events.

Overview
--------

The `Window` class is designed to manage the interaction between a camera system and a cube system in a 3D space. It provides methods for handling user input through OpenCV windows, trackbars, and mouse events.

Class
-----

.. class:: Window

    **Methods:**

    .. method:: __init__()

        Initializes the `Window` class, setting up initial parameters for the camera and cube systems and creating the necessary OpenCV windows and trackbars.

        **Example:**

        .. code-block:: python
            :caption: Example of creating a `Window` object

            window = Window()

    .. method:: window_creator()

        Creates and configures the OpenCV windows and trackbars for the camera and cube settings.

        **Example:**

        .. code-block:: python
            :caption: Example of creating the windows

            window.window_creator()

    .. method:: toggle_normal(value)

        Toggles the display of normals on or off based on the trackbar value.

        **Parameters:**
        - `value`: The value from the "Normals" trackbar.

        **Example:**

        .. code-block:: python
            :caption: Example of toggling normals

            window.toggle_normal(1)

    .. method:: toggle_planes(value)

        Toggles the display of planes on or off based on the trackbar value.

        **Parameters:**
        - `value`: The value from the "Planes" trackbar.

        **Example:**

        .. code-block:: python
            :caption: Example of toggling planes

            window.toggle_planes(1)

    .. method:: toggle_points(value)

        Toggles the display of points on or off based on the trackbar value.

        **Parameters:**
        - `value`: The value from the "Points" trackbar.

        **Example:**

        .. code-block:: python
            :caption: Example of toggling points

            window.toggle_points(1)

    .. method:: window_show(class_cam)

        Displays the camera image in the "image window" using the provided camera class.

        **Parameters:**
        - `class_cam`: An instance of a camera class containing the `camera_image` attribute.

        **Example:**

        .. code-block:: python
            :caption: Example of showing the window

            window.window_show(camera_instance)

    .. method:: get_camera_system_translation_x()

        Retrieves the current X translation value of the camera system from the trackbar.

        **Returns:**
        - The X translation value as an integer.

        **Example:**

        .. code-block:: python
            :caption: Example of getting the X translation of the camera system

            x_translation = window.get_camera_system_translation_x()

    .. method:: get_camera_system_translation_y()

        Retrieves the current Y translation value of the camera system from the trackbar.

        **Returns:**
        - The Y translation value as an integer.

        **Example:**

        .. code-block:: python
            :caption: Example of getting the Y translation of the camera system

            y_translation = window.get_camera_system_translation_y()

    .. method:: get_camera_system_translation_z()

        Retrieves the current Z translation value of the camera system from the trackbar.

        **Returns:**
        - The Z translation value as an integer.

        **Example:**

        .. code-block:: python
            :caption: Example of getting the Z translation of the camera system

            z_translation = window.get_camera_system_translation_z()

    .. method:: get_camera_system_rotation_roll()

        Retrieves the current roll rotation value of the camera system from the trackbar.

        **Returns:**
        - The roll rotation value as an integer.

        **Example:**

        .. code-block:: python
            :caption: Example of getting the roll rotation of the camera system

            roll_rotation = window.get_camera_system_rotation_roll()

    .. method:: get_camera_system_rotation_pitch()

        Retrieves the current pitch rotation value of the camera system from the trackbar.

        **Returns:**
        - The pitch rotation value as an integer.

        **Example:**

        .. code-block:: python
            :caption: Example of getting the pitch rotation of the camera system

            pitch_rotation = window.get_camera_system_rotation_pitch()

    .. method:: get_camera_system_rotation_yaw()

        Retrieves the current yaw rotation value of the camera system from the trackbar.

        **Returns:**
        - The yaw rotation value as an integer.

        **Example:**

        .. code-block:: python
            :caption: Example of getting the yaw rotation of the camera system

            yaw_rotation = window.get_camera_system_rotation_yaw()

    .. method:: get_cube_system_translation_x()

        Retrieves the current X translation value of the cube system from the trackbar.

        **Returns:**
        - The X translation value as an integer.

        **Example:**

        .. code-block:: python
            :caption: Example of getting the X translation of the cube system

            x_translation = window.get_cube_system_translation_x()

    .. method:: get_cube_system_translation_y()

        Retrieves the current Y translation value of the cube system from the trackbar.

        **Returns:**
        - The Y translation value as an integer.

        **Example:**

        .. code-block:: python
            :caption: Example of getting the Y translation of the cube system

            y_translation = window.get_cube_system_translation_y()

    .. method:: get_cube_system_translation_z()

        Retrieves the current Z translation value of the cube system from the trackbar.

        **Returns:**
        - The Z translation value as an integer.

        **Example:**

        .. code-block:: python
            :caption: Example of getting the Z translation of the cube system

            z_translation = window.get_cube_system_translation_z()

    .. method:: get_cube_system_rotation_roll()

        Retrieves the current roll rotation value of the cube system from the trackbar.

        **Returns:**
        - The roll rotation value as an integer.

        **Example:**

        .. code-block:: python
            :caption: Example of getting the roll rotation of the cube system

            roll_rotation = window.get_cube_system_rotation_roll()

    .. method:: get_cube_system_rotation_pitch()

        Retrieves the current pitch rotation value of the cube system from the trackbar.

        **Returns:**
        - The pitch rotation value as an integer.

        **Example:**

        .. code-block:: python
            :caption: Example of getting the pitch rotation of the cube system

            pitch_rotation = window.get_cube_system_rotation_pitch()

    .. method:: get_cube_system_rotation_yaw()

        Retrieves the current yaw rotation value of the cube system from the trackbar.

        **Returns:**
        - The yaw rotation value as an integer.

        **Example:**

        .. code-block:: python
            :caption: Example of getting the yaw rotation of the cube system

            yaw_rotation = window.get_cube_system_rotation_yaw()

    .. method:: get_cube_system_scale()

        Retrieves the current scale value of the cube system from the trackbar.

        **Returns:**
        - The scale value as an integer.

        **Example:**

        .. code-block:: python
            :caption: Example of getting the scale of the cube system

            scale = window.get_cube_system_scale()

    .. staticmethod:: nothing(value)

        A static method that does nothing. Used as a placeholder for trackbar callbacks.

        **Parameters:**
        - `value`: The value passed by the trackbar.

        **Example:**

        .. code-block:: python
            :caption: Example of using the `nothing` method

            cv.createTrackbar("dummy", "window", 0, 100, Window.nothing)

    .. method:: handle_movement()

        Handles keyboard input for camera movement. The camera can be moved forward, backward, left, right, up, or down using the WASDQE keys.

        **Example:**

        .. code-block:: python
            :caption: Example of handling camera movement

            window.handle_movement()

    .. method:: move_camera(direction, speed)

        Moves the camera in the specified direction at the given speed.

        **Parameters:**
        - `direction`: The direction to move the camera. Can be 'forward', 'backward', 'left', 'right', 'up', or 'down'.
        - `speed`: The speed of the movement as an integer.

        **Example:**

        .. code-block:: python
            :caption: Example of moving the camera

            window.move_camera('forward', 100)

    .. method:: mouse_event_handler(event, x, y, flags, param)

        Handles mouse events, allowing the user to rotate the camera using the mouse.

        **Parameters:**
        - `event`: The type of mouse event.
        - `x`: The x-coordinate of the mouse event.
        - `y`: The y-coordinate of the mouse event.
        - `flags`: Additional flags for the mouse event.
        - `param`: Additional parameters.

        **Example:**

        .. code-block:: python
            :caption: Example of handling a mouse event

            cv.setMouseCallback("image window", window.mouse_event_handler)
