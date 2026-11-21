<?php


$arr = [1,2,3,4,5,6,7,8,9,10];
print_r($arr);
echo "<hr>";

$queueops = $_GET['queueops'];
$op = $_GET['op'];

switch ($op) {
    case 1:
        array_unshift($arr, $queueops);
        echo "<br>After push operation queue is<br>";
        print_r($arr);
        echo "<hr>";
        foreach ($arr as $val) {
            echo "$val<br>";
        }
        break;

    case 2:
        $popElement = array_shift($arr);
        echo "<br>Deleted element is $popElement<br>";
        echo "<br>queue is: ";
        print_r($arr);
        echo "<hr>";
        foreach ($arr as $val) {
            echo "$val<br>";
        }
        break;

    case 3:
        echo "<br>queue is: <br>";
        foreach ($arr as $val) {
            echo "$val<br>";
        }
        break;
}
