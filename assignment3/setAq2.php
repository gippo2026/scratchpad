<?php


$str = $_GET['str'];
$op = $_GET['op'];

switch ($op) {
    case 1:
        echo "Lower case = " . strtolower($str);
        break;

    case 2:
        echo "Title case = " . ucwords($str);
        break;

    case 3:
        echo "Reverse = " . strrev($str);
        break;
}
