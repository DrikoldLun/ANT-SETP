#!/bin/sh
R=97/108/20.5/29.5
#R=98/102/25.8/28.7
J=M7i
PS=ANT.ps
PDF=2fig.pdf

gmt grdcut ../GMTdata/ANTsichuan.grd -R$R -Gcut.grd
gmt psxy -R$R -J$J -K -T  > $PS
gmt pscoast -R$R -J$J -X2 -Y-1.5 -K -O -Bx1 -By1 -BWSEN -A1000 -Sskyblue -Gdarkyellow -W1p,blue,"-." -Dc >> $PS
gmt grdgradient cut.grd -A0/90 -Gtmp_grad.grd -Ne0.7
gmt grdimage cut.grd -R$R -J$J -K -O -Itmp_grad.grd -C../../../lms/innermaterial/topo.cpt >> $PS
gmt psxy ../fault.china.dbase.xy.bak -R$R -J$J -K -O -W1p,black >> $PS
gmt psmeca cmt5.dat -Sm0.4c/0 -Gred -R$R -J$J -T0 -M -K -O >> $PS
gmt psmeca cmt6.dat -Sm0.6c/0 -Gred -R$R -J$J -T0 -M -K -O >> $PS
gmt psmeca cmt7.dat -Sm0.8c/0 -Gred -R$R -J$J -T0 -M -K -O >> $PS
gmt pslegend -R -J -DjTR+w4c+o0.1/0.1 -X0.1 -Y0.1 -F+gwhite+r -K -O << EOF >> $PS
S 0.3c c 0.4c - 0.1p 1c Mw=5.0~6.0
G 0.1c
S 0.3c c 0.6c - 0.1p 1c Mw=6.0~7.0
G 0.3c
S 0.3c c 0.8c - 0.1p 1c Mw=7.0~8.0
G 0.1c
EOF
gmt pstext texts.dat -R$R -J$J -N -K -O >> $PS

Rg=82/111/19/35
Jg=M4i
#gmt grdcut GMTdata/TP.grd -R$Rg -Gcut1.grd
cut2=../GMTdata/TPsmooth.grd
gmt pscoast -R$Rg -J$Jg -B0 -B+gwhite -Df -N1 -A5000 -X-4 -Y13 -K -O --MAP_FRAME_TYPE=plain >> $PS
gmt grdgradient $cut2 -A0/90 -Gtmp_grad1.grd -Ne0.7
gmt grdimage $cut2 -R$Rg -J$Jg -K -O -Itmp_grad1.grd -C../../../lms/innermaterial/topo.cpt >> $PS
gmt grdcontour $cut2 -R$Rg -J$Jg -A1000+f8p -K -O >> $PS
gmt psbasemap -R$Rg -J$Jg -D$R -F+p0.5p,blue -K -O >> $PS
gmt pstext textg.dat -R$Rg -J$Jg -F+f10p,red -N -K -O >> $PS

gmt psxy -R$R -J$J -O -T >> $PS
ps2pdf $PS $PDF
rm tmp*.grd $PS *.history cut*grd
evince $PDF
