# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

[string[]]$lines = Get-Content -Path "./input.txt" 

$width=$lines[0].Length

$accum=1

function calculateTrees([int]$xinc,[int]$yinc) {
    [int]$x=0
    [int]$y=0


    [int]$trees=0

    while ($y -lt $lines.Length) {
        # over $xinc down $yinc
        $x=($x+$xinc) % $width
        $y = $y + $yinc
        if($y -lt $lines.Length) {
            $c=$lines[$y].Substring($x,1);
            if($c -eq "#") {
                $trees = $trees + 1
            }
        }
    }
    #echo $trees
    return [int]$trees
}
$accum=$accum * [int](calculateTrees 1 1)
$accum=$accum * [int](calculateTrees 3 1)
$accum=$accum * [int](calculateTrees 5 1)
$accum=$accum * [int](calculateTrees 7 1)
$accum=$accum * [int](calculateTrees 1 2)

echo "Total trees: $accum"