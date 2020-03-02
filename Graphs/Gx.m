load Datos.txt

xd = Datos(:,1);
xp = Datos(:,2);

 figure
 
 plot(xd,'-r')
 hold on
 plot(xp,'-b')
 title('Control PD X kp=1 kd=0 sat=0.2 deathzone=0.05 ' )
 xlabel('Muestras')
 ylabel('X [m]')
 
 grid on