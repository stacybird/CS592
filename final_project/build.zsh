#!/bin/zsh
# Start with a decimal string.  XOR with slightly random byte to ensure 
# 0x7f is never generated
foreach i (`cat userlist`)
  mkdir -p $i
  export ZZ=`echo $i | sha256sum | awk '{print $1}' | cut -c 1-6 | tr \[a-f\] \[A-F\]`
  export AA=`echo "ibase=16;$ZZ" | bc`
  export BB=`echo $i | sha512sum | sum | awk '{print ($1 % 32)+96}'`
  cat Ch12CovertLaunching_process.c.template | sed s/AAAAAA/$AA/ | sed s/BBBBBB/$BB/ >! program.c
  gcc -m32 -o ${i}/Ch12CovertLaunching_process program.c
end
rm program.c
