# Aspect Ratio Node

This node allows you to calculate the width and height of an image based on a base resolution, an aspect ratio, and an orientation (landscape or portrait).

## Usage

1. Select the base resolution. This should be the length of the shortest side of the desired image.
2. Select the desired aspect ratio from the dropdown menu.
3. Select the desired orientation (landscape or portrait) from the dropdown menu.
4. The node will output the calculated width and height, rounded to the nearest multiple of 8.

## Example

If you input a base resolution of 540, select the aspect ratio 4:3, and select the landscape orientation, the node will output a width of 720 and a height of 540.

If you input a base resolution of 540, select the aspect ratio 4:3, and select the portrait orientation, the node will output a width of 540 and a height of 720.

## Installation

To install this node, place the `aspect_ratio.py` file in the `invokeai/nodes` directory.

## Supported Aspect Ratios

The following aspect ratios are supported:

- 1:1 (Square)
- 16:9 (Widescreen)
- 4:3 (Standard)
- 3:2 (Photographic)
- 5:4 (Classic)
- 5:3 (Widescreen)

## Supported Orientations

The following orientations are supported:

- Landscape
- Portrait