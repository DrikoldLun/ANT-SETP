#!/bin/sh
gmt set GMT_COMPATIBILITY = 4
gmt set PS_MEDIA = a4
#R=-250/250/0/400
R=-500/500/0/980
J=X6.5i/6.5i
PS=${1}s.ps
PDF=arangefig/${1}s.pdf
path=filter1/${1}s/
#path=datasample1/

pssac2 -R$R -J$J -B100:"Time(sec)":/100:"\Distance(km)":WSen -M0.1 -W0.00001p,black -Ekt-3 ${path}*.sac > $PS

ps2pdf $PS $PDF
rm $PS
