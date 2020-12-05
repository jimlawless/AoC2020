# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

$option=[System.StringSplitOptions]::RemoveEmptyEntries

[string[]]$lines = Get-Content -Path "./input2.txt" 

$total = 0
foreach($line in $lines) {
    $words=$line.split(" -:",$option)
    $p=$words[3].ToCharArray()
    $howMany=0
    if($p[ ([int]$words[0]-1) ] -eq $words[2]) {
        $howMany=$howMany+1
    }
    if($p[ ([int]$words[1]-1) ] -eq $words[2]) {
        $howMany=$howMany+1
    }
    if($howMany -eq 1) { 
        echo $line
        $total=$total+1
    }
}

echo "Total $total"
