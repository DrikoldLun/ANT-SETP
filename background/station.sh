#!/bin/sh
R=97/108/20.5/29.5
#R=98/102/25.8/28.7
J=M7i
PS=ANT.ps
PDF=ANT.pdf

gmt grdcut GMTdata/ANTsichuan.grd -R$R -Gcut.grd
gmt psxy -R$R -J$J -K -T  > $PS
gmt pscoast -R -J -K -O -Bx1 -By1 -BWSEN+t"ANT" -A10000 -Sskyblue -Gdarkyellow -W1p,blue,"-." -Dc >> $PS
gmt grdgradient cut.grd -A0/90 -Gtmp_grad.grd -Ne0.7
gmt grdimage cut.grd -R -J -K -O -Itmp_grad.grd -C../../lms/innermaterial/topo.cpt >> $PS
gmt psxy CN-faults.dat -R -J -K -O -W1p,black >> $PS
cat ANTsta.lst|while read line
do
echo $line|awk '{print $3,$2}'|gmt psxy -R -J -K -O -St0.3c -W0.7p -Gyellow >>$PS
echo $line|awk '{print $3,$2,$1}'|gmt pstext -R -J -F+f4p,1,black+jTL -D-0.17c/-0.2c -K -O >> $PS
done
gmt pstext texts.dat -R$R -J$J -N -K -O >> $PS
gmt psxy -R$R -J$J -O -T >> $PS
ps2pdf $PS $PDF
rm tmp*.grd $PS *.history
