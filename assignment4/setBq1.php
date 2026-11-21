<?php


$op = $_GET['op'];

$arr1 = ["a" => 50,"b" => 10,"c" => 40,"d" => 30,"e" => 20];
$arr2 = ["aaa" => 35,"bbb" => 30,"ccc" => 20,"ddd" => 10,"eee" => 1000];
$arr3 = ["id1" => 100,"id2" => 90,"id3" => 75,"id4" => 80,"id5" => 45];

switch ($op) {
    case 1:
        echo "<h1>Array is: </h1>";
        print_r($arr3);
        echo "<hr>";
        echo "<h2>After sorting: </h2>";
        echo "<hr>";
        sort($arr3);
        print_r($arr3);
        break;

    case 2:
        echo "<h1>Array is: </h1>";
        print_r($arr3);
        echo "<hr>";
        echo "<h2>After sorting(without keys change): </h2>";
        echo "<hr>";
        asort($arr3);
        print_r($arr3);
        break;

    case 3:
        echo "<h1>First array is: </h1>";
        print_r($arr3);
        echo "<hr>";
        echo "<h1>Second array is: </h1>";
        print_r($arr1);
        echo "<hr>";
        echo "<h2>Merge arrays: </h2>";
        echo "<hr>";
        $merge = array_merge($arr3, $arr1);
        print_r($merge);
        break;

    case 4:
        echo "<h1>First array is: </h1>";
        print_r($arr2);
        echo "<hr>";
        echo "<h1>Second array is: </h1>";
        print_r($arr1);
        echo "<hr>";
        echo "<h2>Intersection of arrays: </h2>";
        echo "<hr>";
        $intersect = array_intersect($arr2, $arr1);
        print_r($intersect);
        break;

    case 5:
        echo "<h1>First array is: </h1>";
        print_r($arr2);
        echo "<hr>";
        echo "<h1>Second array is: </h1>";
        print_r($arr1);
        echo "<hr>";
        echo "<h2>Diffrence between two arrays: </h2>";
        echo "<hr>";
        $intersect = array_diff($arr2, $arr1);
        print_r($intersect);
        break;
}
