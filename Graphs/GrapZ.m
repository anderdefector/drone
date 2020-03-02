load Datos.txt

zd = Datos(:,5);
zp = Datos(:,6);

 figure
 
 plot(zd,'-r')
 hold on
 plot(zp,'-b')
 title('Control PD altura kp=1 kd=1.4 sat=0.3 deathzone=0.02 ' )
 xlabel('Muestras')
 ylabel('Z [m]')
 
 grid on