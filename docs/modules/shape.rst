===============================
Shape Module
===============================

The `shape` module contains the definitions for `Triangle4D`, `Cube`, and `Rectangle` classes. These classes are used to represent and manipulate 3D shapes.

Classes
--------

.. autoclass:: shape.Triangle4D
   :members:
   :undoc-members:
   :inherited-members:

.. autoclass:: shape.Cube
   :members:
   :undoc-members:
   :inherited-members:

.. autoclass:: shape.Rectangle
   :members:
   :undoc-members:
   :inherited-members:

Methods
--------

- `Triangle4D(p1, p2, p3)`: Initializes a 4D triangle with points `p1`, `p2`, and `p3`.

- `Cube.create_point(x, y, z)`: Creates a point in 4D homogeneous coordinates.

- `Cube.__init__(size, pos_x, pos_y, pos_z)`: Initializes a cube with the given size and position.

- `Cube.generate_vertices(size)`: Generates the vertices and triangles for the cube.

- `Cube.set_position(pos_x, pos_y, pos_z)`: Sets the position of the cube by applying a translation matrix.

- `Rectangle.create_point(x, y, z)`: Creates a point in 4D homogeneous coordinates.

- `Rectangle.__init__(size_x, size_y, size_z, pos_x, pos_y, pos_z)`: Initializes a rectangle with the given dimensions and position.

- `Rectangle.generate_vertices(size_x, size_y, size_z)`: Generates the vertices and triangles for the rectangle.

- `Rectangle.set_position(pos_x, pos_y, pos_z)`: Sets the position of the rectangle by applying a translation matrix.
