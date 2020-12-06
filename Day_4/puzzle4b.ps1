# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

$option=[System.StringSplitOptions]::RemoveEmptyEntries
[string[]]$lines = Get-Content -Path "./input.txt" 

$h=@{}

function emptyVariables($e) {
    $e.byr=0
    $e.iyr=0
    $e.eyr=0
    $e.hgt=0
    $e.hcl=0
    $e.ecl=0
    $e.pass_id=0
    $e.cid=0
    $e.keep=@{}
}

function checkValidity($v) {
    $v.invalid=1
    if(($v.byr+$v.iyr+$v.eyr+$v.hgt+$v.hcl+$v.ecl+$v.pass_id) -eq 7) {
        $v.invalid=0
        $t=[int]$v.keep.byr
        if( ($t -lt 1920) -or ($t -gt 2002)) {
             $v.invalid=1
        }

        $t=[int]$v.keep.iyr
        if( ($t -lt 2010) -or ($t -gt 2020)) {
            $v.invalid=1
        }

        $t=[int]$v.keep.eyr
        if( ($t -lt 2020) -or ($t -gt 2030)) {
            $v.invalid=1
        }

        $t=$v.keep.hgt
        [int]$num=[int]$t.substring(0,$t.length-2)
        $suffix=$t.substring($t.length-2,2)
        if($suffix -eq "cm") {
            if(($num -lt 150) -or ($num -gt 193)) {
               $v.invalid=1
            }
        }
        if($suffix -eq "in") {
            if(($num -lt 59) -or ($num -gt 76)) {
                $v.invalid=1
            }
        }
        if(($suffix -ne "cm") -and ($suffix -ne "in")) {
            $v.invalid=1
        }

        $t=$v.keep.hcl
        if(! $($t -match "^[#][0-9a-f]{6}$")) {
            $v.invalid=1
        }

        $t=$v.keep.ecl
        if("amb blu brn gry grn hzl oth ".indexOf($t) -lt 0) {
            $v.invalid=1
        }

        $t=$v.keep.pid
        if(! $($t -match "^[0-9]{9}$")) {
            $v.invalid=1
        }
        if($v.invalid	 -eq 0) {
            $v.total = $v.total + 1
        }
    }
}

$h.total=0
emptyVariables $h

foreach($line in $lines) {
    if($line -eq ""){
        checkValidity $h
        emptyVariables $h
    }
    else {
        $h.byr=$h.byr + $(if($line.indexOf("byr:") -ge 0) {1} else {0})
        $h.iyr=$h.iyr + $(if($line.indexOf("iyr:") -ge 0) {1} else {0})
        $h.eyr=$h.eyr + $(if($line.indexOf("eyr:") -ge 0) {1} else {0}) 
        $h.hgt=$h.hgt + $(if($line.indexOf("hgt:") -ge 0) {1} else {0})
        $h.hcl=$h.hcl + $(if($line.indexOf("hcl:") -ge 0) {1} else {0})
        $h.ecl=$h.ecl + $(if($line.indexOf("ecl:") -ge 0) {1} else {0})
        $h.pass_id=$h.pass_id + $(if($line.indexOf("pid:") -ge 0) {1} else {0})
        $h.cid=$h.cid + $(if($line.indexOf("cid:") -ge 0) {1} else {0})
        $pairs=$line.split(" ",$option)
        foreach($pair in $pairs) {
            $pieces=$pair.split(":",$option)
            $h.keep[$pieces[0]]=$pieces[1]
        }
    }
}
checkValidity $h
echo $h.total
