# `defaults.py`

This file includes default variables and utility functions that are useful throughout the rest of the components.

## Variables

- `WIND_COMPASS_DEVIATION`: The amount of noise that is added to each calculated vector on the wind map. To learn more, see the [WindMap](./WindMap.md) page.
- `TICK_TIME_SCALE`: The time scale at which the balloon tick operates. To learn more, see the [Balloon](./Balloon.md) page.
- `SPEED_OF_LIGHT`: Speed of light in a vacuum, in meters/second.

## Functions

### point_to_matrix_coord(x, y)

This function takes graphical coordinates as an (x,y) pair and converts them to matrix indices. The wind map is centered on (0,0), which means WindMap[0][0] is **not** coordinate (0,0).

### round_threshold(a, step)

Takes a value a and rounds it to the closest threshold value. For example, if the threshold is 0.6, then when `a = 1.5`, your output is 1.2.

### after_pop_velocity(t, t_pop)

Takes the given balloon pop time and current flight time to calculate the velocity of the balloon based on a dedicated function. More information about this function is on the [Balloon](./Balloon.md) page.

### spherical_to_vector(spherical)

Takes the angles of a spherical coordinate system ($\phi$,$\theta$) and turns them into a unit, rectangular 3D vector.