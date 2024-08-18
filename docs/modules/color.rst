.. _color_module:

Color Module
============

This module provides the `Color` class, which includes predefined color constants and several static methods for color manipulation, including generating random colors, adjusting color intensity, and converting between color spaces.

Overview
--------

The `Color` class includes a variety of predefined color constants, each represented as a tuple of BGR (Blue, Green, Red) values. Additionally, it provides methods for random color selection, intensity calculation, and color space conversion.

Classes
-------

.. class:: Color

    A class containing color constants and static methods for color manipulation.

    **Class Attributes:**

    The following attributes represent predefined colors as BGR tuples:

    - `ALICE_BLUE = (255, 248, 240)`
    - `ANTIQUE_WHITE = (215, 235, 250)`
    - `AQUA = (255, 255, 0)`
    - ...

    **Methods:**

    .. method:: RandomColor()

        Selects a random color from the predefined color constants.

        **Returns:**
        - A tuple representing a random color in BGR format.

        **Example:**

        .. code-block:: python
            :caption: Example of `RandomColor` method

            random_color = Color.RandomColor()

    .. method:: intensity(light_direction, normal)

        Calculates the light intensity on a surface based on the light direction and the surface normal.

        **Parameters:**
        - `light_direction`: A 1D `numpy.array` representing the direction of the light source.
        - `normal`: A 1D `numpy.array` representing the normal vector of the surface.

        **Returns:**
        - A `float` representing the intensity of the light on the surface.

        **Example:**

        .. code-block:: python
            :caption: Example of `intensity` method

            intensity_value = Color.intensity(light_direction, normal)

    .. method:: bgr_to_hsl(b, g, r)

        Converts a BGR color to HSL (Hue, Saturation, Lightness) format.

        **Parameters:**
        - `b`: Blue component (0-255).
        - `g`: Green component (0-255).
        - `r`: Red component (0-255).

        **Returns:**
        - A tuple `(h, l, s)` where `h` is hue, `l` is lightness, and `s` is saturation.

        **Example:**

        .. code-block:: python
            :caption: Example of `bgr_to_hsl` method

            h, l, s = Color.bgr_to_hsl(255, 128, 0)

    .. method:: hsl_to_bgr(h, l, s)

        Converts an HSL color to BGR format.

        **Parameters:**
        - `h`: Hue component (0-1).
        - `l`: Lightness component (0-1).
        - `s`: Saturation component (0-1).

        **Returns:**
        - A tuple `(b, g, r)` where `b`, `g`, and `r` are the blue, green, and red components (0-255).

        **Example:**

        .. code-block:: python
            :caption: Example of `hsl_to_bgr` method

            b, g, r = Color.hsl_to_bgr(0.5, 0.5, 0.5)

    .. method:: adjust_bgr_intensity(base_color, intensity)

        Adjusts the intensity of a BGR color.

        **Parameters:**
        - `base_color`: A tuple `(b, g, r)` representing the base color in BGR format.
        - `intensity`: A `float` representing the intensity multiplier.

        **Returns:**
        - A tuple `(b, g, r)` representing the adjusted color in BGR format.

        **Example:**

        .. code-block:: python
            :caption: Example of `adjust_bgr_intensity` method

            adjusted_color = Color.adjust_bgr_intensity((255, 128, 0), 0.8)
