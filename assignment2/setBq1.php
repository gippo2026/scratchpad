<?php


$name = $_GET['name'];
$clgName = $_GET['clgname'];
$message = $_GET['msg'];

function greeting($name = 'Someone', $clgName = 'Unknown college', $message = 'No message')
{
    return "$name has send a message from $clgName as following: $message";
}

$args = [];

if ($name != "") {
    $args['name'] = $name;
}
if ($clgName != "") {
    $args['clgName'] = $clgName;
}
if ($message != "") {
    $args['message'] = $message;
}

echo greeting(...$args);
