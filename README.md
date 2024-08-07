# Packed Shape Array Macro for LayoutEditor

## Overview

This Python script generates a text file containing coordinates (x, y) and radius information for hexagonally packed shapes within a specified area. Each shape can have random offsets from perfect packing and random fluctuations in radius within a specified percentage range.

A separate LayoutEditor macro is provided to process the text file and generate the shape array as a gds file.

# Python script

## Requirements

Python 3.x

Required Python packages (install via `pip`):
* `numpy`
* `random`

## Parameters

* `x_maxDimension`: box size in x
* `y_maxDimension`: box size in y
* `radius`: shape radius
* `domain_spacing`: center to center distance between shapes
* `max_dev`: maximum deviation in the center position or radius

## Output

The script generates a comma delimited text file (hex_packed_array.txt) in the current directory containing the following information for each shape:

```text
x_position,y_position,radius,layer
```

Example output:

```text
0.326,0.279,0.3,1
1.313,0.208,0.3,1
...
```

# LayoutEditor macro

## Requirements

LayoutEditor build 20230925

## Shape definition

Shapes are defined after the line:

```text
layout->drawing->activeLayer=layer;
```

To generate circles:

```text
layout->drawing->p(x,y);
layout->drawing->p(x,y+r);
layout->drawing->circle();
```

To generate polygons:

```text
layout->drawing->p(x1,y1);
layout->drawing->p(x2,y2);
...
layout->drawing->polygon();
```

`p(x,y)` defines each consecutive point in the polygon. The last point will automatically connect to the first point. ModCirclesFromFile.layout is set up to generate hexagons.

## Installation

```bash
git clone https://github.com/agauer/Packed-Shape-Array-for-Layout-Editor.git
```

## Usage

Run the Python script with the following command:

```bash
python hexArray_layout.py
```

Macros can be ran in LayoutEditor application using Utilies > Macros.
