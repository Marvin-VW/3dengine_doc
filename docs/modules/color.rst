Color Module
============

This module provides functionality for color manipulation, including predefined color constants, color adjustment, and color conversion.

Classes
--------

Color
-----

The `Color` class contains predefined color constants and methods for manipulating colors.

Predefined Colors
-----------------
The `Color` class contains several predefined colors. Each color is represented as an RGB tuple.

- **ALICE_BLUE**: (255, 248, 240)
- **ANTIQUE_WHITE**: (215, 235, 250)
- **AQUA**: (255, 255, 0)
- **AQUAMARINE**: (212, 255, 127)
- **AZURE**: (255, 255, 240)
- **BEIGE**: (220, 245, 245)
- ...

Methods
--------

- **`RandomColor()`**: Returns a random color from the predefined color list.
  
- **`intensity(light_direction, normal)`**: Calculates the intensity of light on a surface based on the light direction and surface normal. Returns a float value.

- **`bgr_to_hsl(b, g, r)`**: Converts BGR color values to HSL (Hue, Saturation, Lightness) values. Returns a tuple of HSL values.

- **`hsl_to_bgr(h, l, s)`**: Converts HSL values to BGR color values. Returns a tuple of BGR values.

- **`adjust_bgr_intensity(base_color, intensity)`**: Adjusts the brightness of a base color based on the given intensity. Returns a new BGR color tuple.

Usage Examples
--------------
