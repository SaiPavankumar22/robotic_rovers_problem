## Problem Statement

A squad of robotic rovers are to be landed by ISRO on a plateau on Moon. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth.

A rover's position and location is represented by a combination of x and y coordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation.

> An example position might be `0, 0, N`, which means the rover is in the bottom left corner and facing North.

In order to control a rover, ISRO sends a simple string of letters. The possible letters are:

- `L` – Makes the rover spin **90 degrees left**, without moving from its current spot.
- `R` – Makes the rover spin **90 degrees right**, without moving from its current spot.
- `M` – **Move forward** one grid point, and maintain the same heading.

> Assume that the square directly North from `(x, y)` is `(x, y+1)`.

---

## Input Format

- The **first line** of input is the upper-right coordinates of the plateau. The lower-left coordinates are assumed to be `0, 0`.
- The rest of the input pertains to the rovers deployed. Each rover has **two lines** of input:
  1. The rover's **position** — two integers and a letter separated by spaces (x coordinate, y coordinate, and orientation).
  2. A series of **instructions** telling the rover how to explore the plateau.
- Each rover will be finished **sequentially** — the second rover won't start moving until the first one has finished.

---

## Output Format

The output for each rover should be its **final coordinates and heading**.

---

## Sample Input

```
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

## Expected Output

```
1 3 N
5 1 E
```