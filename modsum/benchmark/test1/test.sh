#!/bin/sh
newdir=${1}to${2}
mkdir ${newdir}
cp pre.py ${newdir}/
cp ../modv/* ${newdir}/
cp ../specv/* ${newdir}/
cd ${newdir}
sac << EOF
r *.sac
bp n 4 c ${1} ${2}
w over
q
EOF
python pre.py
