===============================
Window Module
===============================

The `window` module handles the creation and management of windows for camera and cube settings using OpenCV.

Classes
--------

.. autoclass:: utils.window.Window
   :members:
   :undoc-members:
   :inherited-members:

Methods
--------

- `Window.__init__()`: Initializes the window with default settings and creates trackbars for camera and cube parameters.

- `Window.window_creator()`: Creates the OpenCV windows and trackbars for adjusting camera and cube settings.

- `Window.toggle_normal(value)`: Toggles the display of normals.

- `Window.toggle_planes(value)`: Toggles the display of planes.

- `Window.toggle_points(value)`: Toggles the display of points.

- `Window.window_show(class_cam)`: Displays the camera image in the "image window".

- `Window.get_camera_system_translation_x()`: Gets the X translation value for the camera system.

- `Window.get_camera_system_translation_y()`: Gets the Y translation value for the camera system.

- `Window.get_camera_system_translation_z()`: Gets the Z translation value for the camera system.

- `Window.get_camera_system_rotation_roll()`: Gets the roll rotation value for the camera system.

- `Window.get_camera_system_rotation_pitch()`: Gets the pitch rotation value for the camera system.

- `Window.get_camera_system_rotation_yaw()`: Gets the yaw rotation value for the camera system.

- `Window.get_cube_system_translation_x()`: Gets the X translation value for the cube system.

- `Window.get_cube_system_translation_y()`: Gets the Y translation value for the cube system.

- `Window.get_cube_system_translation_z()`: Gets the Z translation value for the cube system.

- `Window.get_cube_system_rotation_roll()`: Gets the roll rotation value for the cube system.

- `Window.get_cube_system_rotation_pitch()`: Gets the pitch rotation value for the cube system.

- `Window.get_cube_system_rotation_yaw()`: Gets the yaw rotation value for the cube system.

- `Window.get_cube_system_scale()`: Gets the scale value for the cube system.

- `Window.nothing(value)`: A placeholder function for trackbar callbacks.

- `Window.handle_movement()`: Handles camera movement based on user input.

- `Window.move_camera(direction, speed)`: Moves the camera in the specified direction with the given speed.

- `Window.mouse_event_handler(event, x, y, flags, param)`: Handles mouse events for rotating the camera.
