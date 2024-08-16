==============================
FpsCounter Module
==============================

The `FpsCounter` class calculates and filters the frames per second (FPS) of the rendering process.

Class `FpsCounter`
-------------------

.. autoclass:: utils.fps_counter.FpsCounter
   :members:
   :undoc-members:
   :inherited-members:

Methods
--------

- `__init__(filter_window_size=1)`: Initializes the FPS counter with a filter window size for smoothing the FPS values.
- `update()`: Updates the FPS count with the time elapsed since the last update.
- `get_fps()`: Returns the most recent FPS value.
- `get_fps_filtered()`: Returns the average FPS value over the filter window size.
