"""Task 2 - Pythagoras fractal"""

import numpy as np
import matplotlib.pyplot as plt

START_X = 0
START_Y = 0
START_ANGLE = 90
START_STEP = 100


def get_new_point(old_point, step, angle):
    """Calculate new point"""

    radians = np.radians(angle)
    new_point = [
        float(old_point[0] + step * np.cos(radians)),
        float(old_point[1] + step * np.sin(radians)),
    ]
    return new_point


def branch_build(step, angle, points: list, level):
    """Calculate points of tree branches"""

    if level > 0:
        old_point = points[-1]
        for angle_rotate in [-45, 45]:
            points.append(get_new_point(old_point, step, angle + angle_rotate))
            points = branch_build(step / 2, angle + angle_rotate, points, level - 1)
            points.append(old_point)

    return points


def tree_build(x, y, angle, step, levels) -> list:
    """Build tree"""
    points = []
    for angle_rotate in [-90, 90]:
        points.append(get_new_point([x, y], step / 100, angle + angle_rotate))
    points.append([x, y])
    points.append(get_new_point([x, y], step, angle))
    return branch_build(step / 2, angle, points, levels)


def tree_draw(points, level):
    """Draw fractal"""
    title = f"Pythagoras tree of the level {level}"
    plt.figure(facecolor="black", num=title)
    ax = plt.axes()
    ax.set_facecolor("black")
    ax.set_aspect("equal", "box")
    plt.plot(*zip(*points), color="deepskyblue")
    plt.scatter(*zip(*points), color="deepskyblue", s=10)
    plt.show()


if __name__ == "__main__":
    print("\nEnter the number of levels of the Pythagoras fractal >> ...")
    levels = int(input())
    tree_draw(tree_build(START_X, START_Y, START_ANGLE, START_STEP, levels), levels)
