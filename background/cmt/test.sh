#!/bin/sh
R=97/108/20.5/29.5
#R=98/102/25.8/28.7
J=M7i
PS=ANT.ps
PDF=2fig.pdf

gmt psxy -R$R -J$J -K -T  > $PS
#gmt pstext text.dat -R$R -J$J -N -K -O >> $PS

Rg=82/111/19/35
Jg=M4i
#gmt grdcut GMTdata/TP.grd -R$Rg -Gcut1.grd
cut2=../GMTdata/TPsmooth.grd
gmt pscoast -R$Rg -J$Jg -B+gwhite -Df -N1 -A5000 -K -O >> $PS
#gmt pscoast -R$Rg -J$Jg -B0 -B+gwhite -Df -N1 -A5000 -X-2 -Y12 -K -O --MAP_FRAME_TYPE=plain >> $PS
gmt grdgradient $cut2 -A0/90 -Gtmp_grad1.grd -Ne0.7
gmt grdimage $cut2 -R$Rg -J$Jg -K -O -Itmp_grad1.grd -C../../../lms/innermaterial/topo.cpt >> $PS
gmt grdcontour $cut2 -R$Rg -J$Jg -A1000+f8p -K -O >> $PS
gmt psbasemap -R$Rg -J$Jg -D$R -F+p0.5p,blue -K -O >> $PS
gmt pstext textg.dat -R$Rg -J$Jg -F+f10p,red -N -K -O >> $PS

gmt psxy -R$R -J$J -O -T >> $PS
ps2pdf $PS $PDF
rm tmp*.grd $PS *.history cut*grd
evince $PDF
