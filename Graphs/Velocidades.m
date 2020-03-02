clc
clear
load Datos.txt

vx = Datos(:,9);


 figure
 
 plot(vx,'-r')
 hold on
 title('Control PD X kp=0.3 kd=1.4 sat=0.3 deathzone=0.02 ' )
 xlabel('Muestras')
 ylabel('X [m]')
 
 grid on