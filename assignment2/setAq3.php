<?php


$num = $_GET['num'];

function revNumber($num)
{
    $digit = 0;
    $rev = 0;

    while ($num > 0) {
        $digit = $num % 10;
        $rev = ($rev * 10) + $digit;
        $num = (int) ($num / 10);
    }
    return $rev;
}

echo "<h2>Reverse of the number $num is = " . revNumber($num) . "</h2>";
