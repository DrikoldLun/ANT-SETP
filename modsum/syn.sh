sprep96 -HS 0 -HR 0 -M W2.d -d dfile -R -NMOD 1
sdisp96
sdpsrf96 -R -XMIN 0 -XMAX 0.5 -YMIN 2.5 -YMAX 4.5 -TXT
plotnps -F7 -W10 -EPS < SDISPR.PLT > disp.eps
#scomb96 -R -FMIN 0 -FMAX 2 -CMIN 2.5 -CMAX 4.5
#sregn96
#slegn96
#sdpegn96 -R -C -XMIN 0 -XMAX 2 -YMIN 2.5 -YMAX 4.5
#plotnps -F7 -W10 -EPS < SREGNC.PLT > regn.eps
#sdpder96 -R -K 2 -XLEN 3 -X0 1 -YLEN 4 -YMIN 0 -YMAX 69
#plotnps -F7 -W10 -EPS < SRDER.PLT > regn.eps
#spulse96 -d dfile -V -i > file96 #| fprof96
#plotnps -F7 -W10 < FPROF96.PLT > syn.eps
#f96tosac file96
#mv *ZVF.sac mtm/synll.sac
