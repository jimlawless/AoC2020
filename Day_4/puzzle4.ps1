# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

[string[]]$lines = Get-Content -Path "./input.txt" 

$byr=0
$iyr=0
$eyr=0
$hgt=0
$hcl=0
$ecl=0
$pass_id=0
$cid=0

$total=0

foreach($line in $lines) {
    if($line -eq ""){
        if(($byr+$iyr+$eyr+$hgt+$hcl+$ecl+$pass_id) -eq 7) {
            $total = $total + 1
        }
        $byr=0
        $iyr=0
        $eyr=0 
        $hgt=0
        $hcl=0
        $ecl=0
        $pass_id=0
        $cid=0
    }
    else {
        $byr=$byr + $(if($line.indexOf("byr:") -ge 0) {1} else {0})
        $iyr=$iyr + $(if($line.indexOf("iyr:") -ge 0) {1} else {0})
        $eyr=$eyr + $(if($line.indexOf("eyr:") -ge 0) {1} else {0}) 
        $hgt=$hgt + $(if($line.indexOf("hgt:") -ge 0) {1} else {0})
        $hcl=$hcl + $(if($line.indexOf("hcl:") -ge 0) {1} else {0})
        $ecl=$ecl + $(if($line.indexOf("ecl:") -ge 0) {1} else {0})
        $pass_id=$pass_id + $(if($line.indexOf("pid:") -ge 0) {1} else {0})
        $cid=$cid + $(if($line.indexOf("cid:") -ge 0) {1} else {0})
    }
}

if(($byr+$iyr+$eyr+$hgt+$hcl+$ecl+$pass_id) -eq 7) {
    $total = $total + 1
}

echo $total

