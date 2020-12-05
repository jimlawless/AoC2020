# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

[int[]]$nums = Get-Content -Path "./input1.txt" 

foreach($i in $nums) {
   foreach($j in $nums) {
       if(($i+$j) -eq 2020) {
         echo "$i $j $($i*$j)"
      }
   }
}

foreach($i in $nums) {
   foreach($j in $nums) {
      foreach($k in $nums) {
         if(($i+$j+$k) -eq 2020) {
            echo "$i $j $k $($i*$j*$k)"
         }
      }
   }
}
