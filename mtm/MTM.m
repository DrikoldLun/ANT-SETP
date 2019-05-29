clear;
close all;
% constants of AR(4) in Eq (46a) in Percival and Walden, 1993
a=2.7607;
b=-3.8106;
c=2.6535;
d=-.9238;
dt=1; % time step set to 1
w=0:.001:pi/dt; % scale for frequency
f=w./(2*pi/dt); % frequency scaled between 0 and 0.5 (for plot)
z=exp(-j*w*dt); % z^(-1)
X=1./(1-a*z-b*z.^2-c*z.^3-d*z.^4); % Fourier transform
PX=X.*conj(X); % Power
LPX=10*log10(PX); % Power in dB

%subplot(3,1,1);
%plot(f,LPX) % Compare theoretical spectrum Figs. 3 and 4 in Handout
%title('Spectrum AR(4)');
%xlabel('Frequency');
%ylabel('Power (dB)');

%create a time series
x(1:4)=randn(1,4); % set initial values
disp(x);
for i=5:1028; % create time series in loop
x(i)=a*x(i-1)+b*x(i-2)+c*x(i-3)+d*x(i-4)+randn(1);
end;
x=x(5:1028); % remove the initial values
subplot(2,1,1);
plot(x);
title('Instance of the AR(4) time series');
xlabel('Time');
ylabel('amplitude');
% Use the matlab pmtm function
NW=4; % set NW to 4 as in the example in Figs. 3 & 4
[Pxx,W] = pmtm(x,NW);
F=W./(2*pi/dt); % frequency scaled between 0 and 0.5 (for plot)
LPxx=10*log10(Pxx*NW); % compute in dB and multiply by NW to scale as LPX
% The standard Periodogram
x1=x.*(hann(length(x)))';
Y1=fft(x1);
Y=fft(x);
Pyy=Y.*conj(Y)/length(x);
LPyy=10*log10(Pyy);
Pyy1=Y1.*conj(Y1)/length(x1);
LPyy1=10*log10(Pyy1);
% The following produces Fig. 5 in the handout
% Note that results across trials may differ due to randomness
subplot(2,1,2);hold;
plot(f,LPX,'k.')
plot(F,LPyy(1:length(F)))
plot(F,LPyy1(1:length(F)),'g')
plot(F,LPxx,'r')
title('Spectra AR(4) Theoretical(black), Periodogram(blue), Hanning(green), Multitaper(red)');
xlabel('Frequency');
ylabel('Power (dB)');
