#!/bin/sh
R=98/102/25.8/28.7
J=M7i
T=$1
c0=$2
echo $1,$2
PS=${T}s.ps
PDF=${T}s.pdf

gmt grdcut ../background/GMTdata/ANTsichuan.grd -R$R -Gcut.grd
gmt psxy -R$R -J$J -K -T  > $PS
gmt pscoast -R -J -K -O -Bx1 -By1 -BWSEN+t"ANT" -A10000 -Sskyblue -Gdarkyellow -W1p,blue,"-." -Dc >> $PS
gmt grdgradient cut.grd -A0/90 -Gtmp_grad.grd -Ne0.7
gmt grdimage cut.grd -R -J -K -O -Itmp_grad.grd -C../../lms/innermaterial/topo.cpt >> $PS
gmt psxy ../../lms/fault.cn -R -J -Sf1i/0.05i  -K -O -W1.5p>> $PS
cat ../background/ANTcut.lst|while read line
do
echo $line|awk '{print $3,$2}'|gmt psxy -R -J -K -O -St0.3c -W0.7p -Gred >>$PS
echo $line|awk '{print $3,$2,$1}'|gmt pstext -R -J -F+f4p,1,black+jTL -D-0.17c/-0.2c -K -O >> $PS
done
python rayt.py -T$T -C$c0
cat rayt.dat|while read line
do
sta1lat=`echo $line|awk '{print $1}'`
sta1lon=`echo $line|awk '{print $2}'`
sta2lat=`echo $line|awk '{print $3}'`
sta2lon=`echo $line|awk '{print $4}'`
gmt psxy -R -J -W0.2p,black -K -O >> $PS << EOF
$sta1lon $sta1lat
$sta2lon $sta2lat
EOF
done
gmt psxy -R -J -O -T >> $PS
ps2pdf $PS $PDF
rm *.grd $PS *.history rayt.dat
