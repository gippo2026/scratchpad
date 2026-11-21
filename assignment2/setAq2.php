<?php

$sumn = $_GET['sumn'];
$factorial = $_GET['fact'];
$op = $_GET['op'];

function sumn($sumn)
{
    $sum = 0;
    for ($i = 0; $i <= $sumn; $i++) {
        $sum += $i;
    }
    return $sum;
}

function factorial($factorial)
{
    $fact = 1;
    for ($i = 1; $i <= $factorial; $i++) {
        $fact *= $i;
    }
    return $fact;
}

switch ($op) {
    case 1:
        echo "Sum of first $sumn numbers is = " . sumn($sumn);
        break;

    case 2:
        echo "factorial of $factorial = " . factorial($factorial);
        break;
}
