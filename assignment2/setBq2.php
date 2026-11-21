<?php


$radius = $_GET['radius'];
$height = $_GET['height'];
$breadth = $_GET['breadth'];
$length = $_GET['length'];
$width = $_GET['width'];
$op = $_GET['op'];


function areaCircle($radius)
{
    return 3.14 * $radius * $radius;
}

function areaTriangle($height, $breadth)
{
    return 0.5 * $height * $breadth;
}

function areaRectangle($length, $width)
{
    return $length * $width;
}

switch ($op) {
    case 1:
        echo "Area of Circle = " . areaCircle($radius);
        break;

    case 2:
        echo "Area of triangle = " . areaTriangle($height, $breadth);
        break;

    case 3:
        echo "Area of rectangle = " . areaRectangle($length, $width);
        break;
}
