<?php

$num1 = $_GET['num1'];
$num2 = $_GET['num2'];
$op = $_GET['op'];

function mod($num1, $num2)
{
    return $num1 % $num2;
}

function power($num1, $num2)
{
    return (pow($num1, $num2));
}

switch ($op) {
    case 1:
        echo "Mod = " . mod($num1, $num2);
        break;

    case 2:
        echo "Power = " . power($num1, $num2);
        break;
}
