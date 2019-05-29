sprep96 -M model.wat -DT 0.01 -NPTS 100 -R -NMOD 100
sdisp96 -v
sdpsrf96 -R -XMIN 0 -XMAX 4 -YMIN 3.0 -YMAX 5.0
plotnps -F7 -W10 -EPS < SDISPR.PLT > 04013.eps
evince 04013.eps
