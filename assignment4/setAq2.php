<?php


$arr = [1,2,3,4,5,6,7,8,9,10];
print_r($arr);
echo "<hr>";

$stackops = $_GET['stackops'];
$op = $_GET['op'];

switch ($op) {
    case 1:
        array_push($arr, $stackops);
        echo "<br>After push operation stack is<br>";
        print_r($arr);
        echo "<hr>";
        foreach ($arr as $val) {
            echo "$val<br>";
        }
        break;

    case 2:
        $popElement = array_pop($arr);
        echo "<br>Deleted element is $popElement<br>";
        echo "<br>Stack is: ";
        print_r($arr);
        echo "<hr>";
        foreach ($arr as $val) {
            echo "$val<br>";
        }
        break;

    case 3:
        echo "<br>Stack is: <br>";
        foreach ($arr as $val) {
            echo "$val<br>";
        }
        break;
}
