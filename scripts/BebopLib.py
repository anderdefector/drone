#  -*- coding: utf-8 -*-
er_antx = 0.0
er_anty = 0.0
er_antz = 0.0 

def conv_ang(ang_d):
    cn1=-2.981e-10
    cn2=2.223e-07
    cn3=-1.798e-05
    cn4=-0.007787
    cn5=0.004498
    cp1=5.749e-10
    cp2=-5.023e-07
    cp3=0.000128
    cp4=-0.01078
    cp5=1.119

    if(ang_d < 0.0):
        ang_d=360-abs(ang_d)

    if (ang_d>=0 and ang_d<180):
        p=cn1*pow(ang_d,4)+cn2*pow(ang_d,3)+cn3*pow(ang_d,2)+cn4*ang_d+cn5
    elif (ang_d>=180 and ang_d<=360):
        p=cp1*pow(ang_d,4)+cp2*pow(ang_d,3)+cp3*pow(ang_d,2)+cp4*ang_d+cp5
    
    return p

def control_P(ref,q,kp,sat,dz):
 	er=ref-q
	tao=kp*er
	if abs(er)<=dz:
		tao=0.0
	if tao>sat:
		tao=sat
	if tao<-sat:
		tao=-sat
        return tao

#Controles con modelo dinámico
def PDz( q_ref, q, kp, kd, sat, death_zone):
    global er_antz
    err=q_ref-q
    der=err-er_antz
    er_antz=err
    tao=kp*err+kd*der
    if abs(err)<=death_zone:
        tao=0
    if tao>sat:
        tao=sat
    if tao<-sat:
        tao=-sat
    
    return tao
    
def PDx(q_ref, q, kp, kd, sat, death_zone, uz, m, g):
    global er_antx
    err=q_ref-q
    print "error = "+str(err)+ "\n"
    der=err-er_antx
    print "derror = "+str(der)+ "\n"
    er_antx=err
    print "errant = "+str(er_antx)+ "\n"
    tao=(kp*err+kd*der)/( uz + (m*g))
    if abs(err)<=death_zone:
        tao=0
    if tao>sat:
        tao=sat
    if tao<-sat:
        tao=-sat
    return tao
    
def PDy(q_ref, q, kp, kd, sat, death_zone, uz, m, g):
    global er_anty
    err=q_ref-q
    der=err-er_anty
    er_anty=err
    tao=(kp*err+kd*der)/( uz + (m*g))
    if abs(err)<=death_zone:
        tao=0
    if tao>sat:
        tao=sat
    if tao<-sat:
        tao=-sat
    return tao


    #Controles con modelo dinámico

