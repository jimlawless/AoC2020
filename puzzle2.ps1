# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

$option=[System.StringSplitOptions]::RemoveEmptyEntries

[string[]]$lines = Get-Content -Path "./input2.txt" 

$total = 0
foreach($line in $lines) {
    $words=$line.split(" -:",$option)
    $count=@{}
    foreach($chr in $words[3].ToCharArray()) {
        $strchr=[string]$chr
        $count[$strchr]=$count[$strchr]+1
    }
    $c=[int]$count[$words[2]];
    if(($c -ge [int]$words[0]) -and ($c -le [int]$words[1])) {
        echo $line
        $total = $total + 1
    }
}

echo "Total $total"
