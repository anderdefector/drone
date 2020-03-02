load Datos.txt

xd = Datos(:,1);
xp = Datos(:,2);

yd = Datos(:,3);
yp = Datos(:,4);

zd = Datos(:,5);
zp = Datos(:,6);

zod = Datos(:,7);
zop = Datos(:,8);

 figure
 
 plot3(xd,yd,zd,'-r')
 hold on
 plot3(xp,yp,zp,'-b')
 title('Control PD xyz kpxy = 0.3  kdxy = 30 sat = 0.2 ' )
 xlabel('X [m]')
 ylabel('y [m]')
 zlabel('Z [m]')
 
 grid on