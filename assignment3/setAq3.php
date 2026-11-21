<?php


$smallStr = $_GET['smallStr'];
$largeStr = $_GET['largeStr'];
$op = $_GET['op'];

$pos = strpos($largeStr, $smallStr);

switch ($op) {
    case 1:
        if ($pos === 0) {
            echo "Small string present at the start of large string";
        } else {
            echo "Small string not present in the start of the large string";
        }
        break;

    case 2:
        if ($pos !== false) {
            echo "Small string present in large string at pos: $pos";
        } else {
            echo "Small string not present in large string";
        }
        break;

    default:
        echo "Please enter both the small and large string to calculate the position";
        break;
}
