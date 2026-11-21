<?php


$arr = [1,2,3,4,5,6,7,8,9,10];
$search = $_GET['search'];
print_r($arr);
echo "<hr>";
if (in_array($search, $arr)) {
    echo "<br>";
    echo "<b>Element $search found in array at pos: " . array_search($search, $arr) . "<b>";
} else {
    echo "<br>Element not found";
}
