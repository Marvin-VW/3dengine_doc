.. _fps_module:

FpsCounter Module
=================

This module provides the `FpsCounter` class, which is used for calculating and tracking the frames per second (FPS) in real-time applications.

Overview
--------

The `FpsCounter` class calculates FPS based on the time difference between updates and maintains a history of recent FPS values for filtered FPS calculation.

Classes
-------

.. class:: FpsCounter(filter_window_size=1)

    A class for tracking and calculating frames per second (FPS).

    **Parameters:**
    
    - `filter_window_size` (int, optional): The number of recent FPS values to consider for the filtered FPS calculation. Default is `1`.

    **Attributes:**

    - `filter_window_size` (int): The size of the window for FPS filtering.
    - `last_timestamp` (float): The timestamp of the last FPS calculation.
    - `fps` (float | None): The most recent FPS value calculated.
    - `fps_history` (List[float]): A list storing the recent FPS values.

    **Methods:**

    .. method:: update() -> None

        Updates the FPS counter with the time difference since the last call.

        **Usage Example:**

        .. code-block:: python
            :caption: Example of `update` method usage

            fps_counter = FpsCounter()
            fps_counter.update()

    .. method:: get_fps() -> float

        Returns the most recent FPS value.

        **Returns:**
        - A `float` representing the most recent FPS value.

        **Usage Example:**

        .. code-block:: python
            :caption: Example of `get_fps` method usage

            fps = fps_counter.get_fps()

    .. method:: get_fps_filtered() -> float

        Returns the filtered FPS value, which is the average of the FPS values in the history.

        **Returns:**
        - A `float` representing the filtered FPS value.

        **Usage Example:**

        .. code-block:: python
            :caption: Example of `get_fps_filtered` method usage

            filtered_fps = fps_counter.get_fps_filtered()
