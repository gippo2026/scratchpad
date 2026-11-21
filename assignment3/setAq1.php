<?php



$str = $_GET['str'];
$op = $_GET['op'];

function strLength($str)
{
    $length = 0;
    while (isset($str[$length])) {
        $length++;
    }
    return $length;
}

function cntVowel($str)
{
    $cnt = 0;
    $length = strLength($str);
    $string = strtolower($str);

    for ($i = 0; $i < $length; $i++) {
        if ($string[$i] == 'a' || $string[$i] == 'e' || $string[$i] == 'i' || $string[$i] == 'o' || $string[$i] == 'u') {
            $cnt++;
        }
    }
    return $cnt;
}

switch ($op) {
    case 1:
        echo "length of the string $str = " . strLength($str);
        break;

    case 2:
        echo "Total vowels in the string $str = " . cntVowel($str);
        break;
}
