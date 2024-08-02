# Packed Shape Array Macro for Layout Editor

## Overview

This Python script generates a text file containing coordinates (x, y) and radius information for hexagonally packed shapes within a specified area. Each shape can have random offsets from perfect packing and random fluctuations in radius within a specified percentage range.

A separate Layout Editor macro is provided to process the text file and generate the shape array as a gds file.

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
* `domain_spacing`: ceneter to center distance between shapes
* `max_dev`: maximum deviation in the center position and radius (controlled independently)

## Output

The script generates a tab delimited text file (hex_packed_array.txt) in the current directory containing the following information for each shape:

`x_position`    `y_position`    `radius`    `layer`

# Layout Editor macro

## Requirements

Layout Editor build 20230925

## Shape definition

Shapes are defined after the line:

`layout->drawing->activeLayer=layer;`

To generate circles:

`layout->drawing->p(x,y);`

`layout->drawing->p(x,y+r);`

`layout->drawing->circle();`


To generate polygons:
`layout->drawing->p(x1,y1);`

`layout->drawing->p(x2,y2);`

...

`layout->drawing->polygon();`


`p(x,y)` defines each consecutive point in the polygon. The last point will automatically connect to the first point. `ModCirclesFromFile.layout` is set up to generate hexagons.

## Usage

Macros can be ran in Layout Editor using Utilies > Macros.
