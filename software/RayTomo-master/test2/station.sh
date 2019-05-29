#!/bin/sh
R=98/102/26/29
#R=98/102/25.8/28.7
J=M7i
PS=tomo.ps
PDF=tomo.pdf
file=TEST_2000_450_1000_10.1_%_

#gmt grdcut GMTdata/ANTsichuan.grd -R$R -Gcut.grd
makecpt -Crainbow -T-3/4/0.01 > tmp.cpt
#xyz2grd $file -Gtmp.grd -R$R -I0.5/0.5
awk '{print $1,$2,$3}' $file|surface -R$R -I0.01/0.01 -T0.25 -Gtmp.grd
grdsample tmp.grd -Gtmp2.grd -I0.01/0.01 -R$R
psbasemap -R$R -J$J -Ba1:"Longitude":/a1:"Latitude":WnSe -K -P -V > $PS
#gmt pscoast -R -J -K -O -Bx1 -By1 -BWSEN+t"ANT" -A10000 -Sskyblue -Gdarkyellow -W1p,blue,"-." -Dc >> $PSgmt grdgradient cut.grd -A0/90 -Gtmp_grad.grd -Ne0.7gmt grdgradient cut.grd -A0/90 -Gtmp_grad.grd -Ne0.7
grdimage tmp.grd -R$R -J$J -K -O -Ctmp.cpt >> $PS
psscale -Ctmp.cpt -D9/2.8/6/0.25 -O -K -B1 >> $PS
ps2pdf $PS $PDF
rm tmp* $PS *.history
evince $PDF
