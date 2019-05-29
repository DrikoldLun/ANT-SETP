#!/bin/sh
R=97/108/20.5/29.5
J=M7i
PS=cmt.ps
PDF=cmt.pdf

gmt grdcut ../GMTdata/ANTsichuan.grd -R$R -Gcut.grd
gmt psxy -R$R -J$J -K -T > $PS
gmt pscoast -R -J -K -O -B1g1 -BWSEN+t"ANT" -A10000 -Sskyblue -Gdarkyellow -W1p,blue,"-." -Dc >> $PS
gmt grdgradient cut.grd -A0/90 -Gtmp_grad.grd -Ne0.7
gmt grdimage cut.grd -R -J -K -O -Itmp_grad.grd -C../../../lms/innermaterial/topo.cpt >> $PS
gmt psxy ../CN-faults.dat -R -J -K -O -W1p >> $PS
gmt psmeca cmt.dat -Sm0.5c/0 -Gred -R -J -T0 -K -O >> $PS
gmt pslegend -R -J -DjTR+w4c+o0.1/0.1 -X0.1 -Y0.1 -F+gwhite+r -K -O << EOF >> $PS
S 0.3c c 0.4c - 0.1p 1c Mw=5.0~6.0
G 0.1c
S 0.3c c 0.6c - 0.1p 1c Mw=6.0~7.0
G 0.3c
S 0.3c c 0.8c - 0.1p 1c Mw=7.0~8.0
G 0.1c
EOF
gmt pstext text.dat -R$R -J$J -N -K -O >> $PS

ps2pdf $PS $PDF
rm $PS tmp_grad.grd cut.grd
evince $PDF
