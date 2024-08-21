.. _color_module:

Color Module
============

This module, named :mod:`camera_model`, provides functionalities for color manipulation and light intensity calculations. The primary class in this module is :mod:`Color`, which contains a variety of color constants and methods for color operations.

.. class:: Color()

    **Class Attributes**

    - **ALICE_BLUE**, **ANTIQUEMENT_WHITE**, ..., **YELLOW_GREEN**: These are predefined colors represented as tuples in BGR format.

    **Methods**

    .. method:: RandomColor()

    - Returns a random color from the predefined set of colors.

    .. code-block:: python
        :caption: :mod:`RandomColor` method

        @classmethod
        def RandomColor(cls):
            color_names = [attr for attr in dir(cls) if not callable(getattr(cls, attr))]
            random_color_name = random.choice(color_names)
            return getattr(cls, random_color_name)

---------------------------------------------------------------------------------------

    .. method:: intensity()
    
    - This method computes the intensity of light as the dot product between the normalized light direction and the normal vector.

    - The result is then negated to ensure that positive values indicate illumination.

    .. note::
        The 'light intensity' is controlled by the Lightness component of the HSL model, which is why the :mod:`bgr_to_hsl` and :mod:`hsl_to_bgr` methods are used.

    .. code-block:: python
        :caption: :mod:`intensity` method

        @staticmethod
        def intensity(light_direction, normal):
            norm = np.linalg.norm(light_direction)
            normalized_light_direction = light_direction / norm
            intensity = np.dot(normalized_light_direction, normal) * (-1)
            return intensity

------------------------------------------------------------------------------------------------

    .. method:: bgr_to_hsl()

    - Converts a BGR color tuple to an HSL (Hue, Saturation, Lightness) representation.

    .. code-block:: python
        :caption: :mod:`bgr_to_hsl` method

        @staticmethod
        def bgr_to_hsl(b, g, r):
            return colorsys.rgb_to_hls(r/255.0, g/255.0, b/255.0)

------------------------------------------------------------------------------------------------

   .. method::  hsl_to_bgr()

    - Converts HSL values back to a BGR tuple.

    .. code-block:: python
        :caption: :mod:`hsl_to_bgr` method

        @staticmethod
        def hsl_to_bgr(h, l, s):
            r, g, b = colorsys.hls_to_rgb(h, l, s)
            return int(b * 255), int(g * 255), int(r * 255)

------------------------------------------------------------------------------------------------

    .. method:: adjust_bgr_intensity()

    - Adjusts the intensity of a BGR color by modifying its lightness.

    .. code-block:: python
        :caption: :mod:`adjust_bgr_intensity` method

        @staticmethod
        def adjust_bgr_intensity(base_color, intensity):
            B, G, R = base_color
            H, L, S = Color.bgr_to_hsl(B, G, R)
            new_L = L * intensity
            new_B, new_G, new_R = Color.hsl_to_bgr(H, new_L, S)
            return (new_B, new_G, new_R)