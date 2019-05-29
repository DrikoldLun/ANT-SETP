#!/bin/sh
#R=97/108/20.5/29.5
#R=98/102/25.8/28.7
R=98/107/23/29.5
J=M7i
PS=cbt_model3.2.ps
PDF=cbt_model3.2.pdf
file=cbt_model3.2.dat
#topo=../../../GMTdata/ANTsichuan.grd
#fault=../../../../lms/fault.cn

#gmt grdcut $topo -R$R -Gcut.grd
makecpt -Cseis1.cpt -T2.44/3.56/0.01 > tmp.cpt
#xyz2grd $file -Gtmp.grd -R$R -I0.25/0.25
awk '{print $3,$4,$5}' $file|surface -R$R -I0.01/0.01 -T0.25 -Gtmp.grd
#grdfilter tmp.grd -Fg0.6 -D0 -Gtmp1.grd
#grdfilter cut.grd -Fg0.6 -D0 -Gcut1.grd
#grdsample tmp.grd -Gtmp2.grd -I0.01/0.01 -R$R
psbasemap -R$R -J$J -Ba1:"Longitude":/a1:"Latitude":WnSe -K -P -V >> $PS
#gmt pscoast -R -J -K -O -Bx1 -By1 -BWSEN+t"ANT" -A10000 -Sskyblue -Gdarkyellow -W1p,blue,"-." -Dc >> $PS
#grdgradient cut.grd -A0/90 -Gtmp_grad.grd -Ne0.7gmt grdgradient cut.grd -A0/90 -Gtmp_grad.grd -Ne0.7
#gmt psxy $fault -R$R -J$J -Sf1i/0.05i -W1.5p -K -O >> $PS
grdimage tmp.grd -R$R -J$J -K -O -Ctmp.cpt >> $PS
psscale -Ctmp.cpt -D5/-1/8/0.2h -O -K -I -B0.2 -V >> $PS
ps2pdf $PS $PDF
rm tmp* $PS *.history cut.grd
#evince $PDF
