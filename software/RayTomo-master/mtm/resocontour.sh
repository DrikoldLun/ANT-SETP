#!/bin/sh
gmtset LABEL_FONT = Helvetica
gmtset LABEL_FONT_SIZE = 14p
#R=97/108/20.5/29.5
#R=98/102/25.8/28.7
R=98/107/23/29.5
J=M7i
T=24
J=M7i
PS=tomo.ps
PDF=tomofig/reso${T}s.pdf
#file=c${T}s.dat
file=TEST_0.1_200_1500_${T}_reso.dat
topo=../../../GMTdata/ANTsichuan.grd
fault=../../../../lms/fault.cn

#gmt grdcut $topo -R$R -Gcut.grd
makecpt -Cpolar -T-0.1/1/0.001 > tmp.cpt
#xyz2grd $file -Gtmp.grd -R$R -I1/1
awk '{print $4,$3,$5}' $file|surface -R$R -I0.01/0.01 -T0.25 -Gtmp.grd
grdfilter tmp.grd -Fg0.5 -D0 -Gtmp1.grd
#grdfilter cut.grd -Fg0.6 -D0 -Gcut1.grd
#grdsample tmp.grd -Gtmp2.grd -I0.01/0.01 -R$R
psbasemap -R$R -J$J -Ba1:"Longitude":/a1:"Latitude":WnSe -Y6 -K -P -V > $PS
#gmt pscoast -R -J -K -O -Bx1 -By1 -BWSEN+t"ANT" -A10000 -Sskyblue -Gdarkyellow -W1p,blue,"-." -Dc >> $PS
#grdgradient cut.grd -A0/90 -Gtmp_grad.grd -Ne0.7gmt grdgradient cut.grd -A0/90 -Gtmp_grad.grd -Ne0.7
#gmt psxy $fault -R$R -J$J -Sf1i/0.05i -W1.5p -K -O >> $PS
grdimage tmp1.grd -R$R -J$J -K -O -Ctmp.cpt >> $PS
grdcontour tmp1.grd -R$R -J$J -A0.2+f12p -K -O >> $PS
pstext -R$R -J$J -K -O >> $PS <<EOF
106.5 29.2 15 0 Helvetica CM ${T}s
EOF
psscale -Ctmp.cpt -D9/-1/8/0.2h -O -K -I -Ba0.2:"resolution": -V >> $PS
ps2pdf $PS $PDF
rm tmp* $PS *.history cut.grd
evince $PDF
