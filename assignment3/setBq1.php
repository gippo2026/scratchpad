<?php


$srnumber = $_GET['srnumber'];
$subname = $_GET['subname'];
$marks = $_GET['marks'];

$s = explode(",", $srnumber);
$n = explode(",", $subname);
$m = explode(",", $marks);
$length = count($s);

echo "<h1>Student information</h1><br>";
echo "<table border = 1><tr><th>Serial number</th>
<th>Subject name</th>
<th>Marks</th>
  </tr>";

$total = 0;
$per = 0;

for ($i = 0; $i < $length; $i++) {
    $total += $m[$i];
    echo "<tr>
  <td>$s[$i]</td>
  <td>$n[$i]</td>
  <td>$m[$i]</td>
  </tr>";
}

$per = round(($total / $length), 2);

echo "<tr><td colspan = 2>Total</td><td>$total</td></tr>";
echo "<tr><td colspan = 2>Percentage</td><td>$per</td></tr>
  </table>";
