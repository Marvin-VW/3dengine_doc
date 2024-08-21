.. _fps_module:

FpsCounter Module
=================


The `FpsCounter Module` module provides functionality to measure and track the frames per second (FPS) using the `FpsCounter` class. This class allows for real-time tracking of FPS and includes options to filter the FPS value over a window of time.

.. class:: FpsCounter()

    **Initialization**

    The `__init__` method initializes the `FpsCounter` object with the following parameters:

    - `filter_window_size`: The number of FPS values to average when filtering. This provides a more stable FPS output.

    .. method:: __init__()

        This method sets up the initial state, including the `last_timestamp`, which is used to calculate the time delta between frames, and initializes the FPS history list.

        .. code-block:: python
            :caption: :mod:`__init__` method
    
            def __init__(self, filter_window_size=1):
                self.filter_window_size = filter_window_size
                self.last_timestamp = time.time()
                self.fps: float | None = None
                self.fps_history: List[float] = []

---------------------------------------------------------------------------

    **Updating FPS**

    The :mod:`update` method updates the current FPS value. It calculates the time difference between the last update and the current one to determine the FPS:

    - `delta_time`: Time difference between the current and the last frame.
    - `fps`: Calculated as `1.0 / delta_time`, representing the frames per second.

    .. method:: update()

        The method also appends the new FPS value to the history list, which is used for filtering.

        .. code-block:: python
            :caption: :mod:`update` method

            def update(self) -> None:
                timestamp = time.time()
                delta_time = timestamp - self.last_timestamp
                self.last_timestamp = timestamp
                try:
                    self.fps = 1.0 / delta_time
                except:
                    self.fps = 0
                self.fps_history.append(self.fps)
                if len(self.fps_history) > self.filter_window_size:
                    self.fps_history.pop(0)

----------------------------------------------------------------------------------

    **Getting FPS**

    The :mod:`get_fps` method returns the latest FPS value calculated in the :mod:`update` method. This provides real-time FPS without any filtering.

    .. method:: get_fps()

        .. code-block:: python
            :caption: :mod:`get_fps` method

            def get_fps(self) -> float:
                return self.fps

----------------------------------------------------------------------------------------------

    **Filtered** FPS**

    The :mod:`get_fps_filtered` method returns a filtered FPS value, which is the average of the FPS values in the history list. This provides a more stable and smoothed FPS value over time.

    .. method:: get_fps_filtered()

        .. code-block:: python
            :caption: :mod:`get_fps_filtered` method

            def get_fps_filtered(self) -> float:
                if len(self.fps_history):
                    return sum(self.fps_history) / len(self.fps_history)
                else:
                    return 0
                        
---------------------------------------------------------------------------------------------------------

    **Examples**

    Here is a basic usage example:

    .. code-block:: python

        from camera_model import FpsCounter
        import time

        fps_counter = FpsCounter(filter_window_size=5)

        while True:
            # Simulate a process that takes time
            time.sleep(0.01)
            fps_counter.update()
            print("Current FPS:", fps_counter.get_fps())
            print("Filtered FPS:", fps_counter.get_fps_filtered())

    This example shows how to create an `FpsCounter` object, update it in a loop, and retrieve both real-time and filtered FPS values.