# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

[string[]]$lines = Get-Content -Path "./input.txt" 

$x=0
$y=0

$width=$lines[0].Length

$trees=0

while ($y -lt $lines.Length) {
    # over 3 down 1.
    $x=($x+3) % $width
    $y = $y + 1
    if($y -lt $lines.Length) {
        $c=$lines[$y].Substring($x,1);
        if($c -eq "#") {
            $trees = $trees + 1
        }
    }
}

echo $trees
