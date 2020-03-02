#!/usr/bin/env python
from Tkinter import *
import ttk
import BebopLib as bl

import rospy
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from bebop_msgs.msg import Ardrone3PilotingStateAltitudeChanged
from bebop_msgs.msg import CommonCommonStateBatteryStateChanged

root = Tk()
root.title("Bebop Interface")

mainframe = ttk.Frame(root, padding ="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)

rospy.init_node('BebopGUI', anonymous=False)


takeoff_pub = rospy.Publisher('/bebop/takeoff', Empty, queue_size=1)

x_odom = StringVar()
y_odom = StringVar()
z_odom = StringVar()
yaw_odom = StringVar()
odom_var=Odometry()


def receive_height(data):
    global height
    height = data.altitude
    z_odom.set("{0:.2f}".format(height))  

def receive_odom(data):
    global odom_var
    odom_var= data
    x_odom.set("{0:.2f}".format(odom_var.pose.pose.position.x))
    y_odom.set("{0:.2f}".format(odom_var.pose.pose.position.y))
    yaw_odom.set("{0:.2f}".format(odom_var.pose.pose.orientation.z))
    

#Subscribers
rospy.Subscriber("/bebop/odom", Odometry, receive_odom)
rospy.Subscriber("/bebop/states/ardrone3/PilotingState/AltitudeChanged", Ardrone3PilotingStateAltitudeChanged, receive_height)
#rospy.Subscriber("/bebop/states/common/CommonState/BatteryStateChanged", CommonCommonStateBatteryStateChanged, Bebop_P4_support.receive_beteria

def takeoff_pub():
    takeoff_pub = rospy.Publisher('/bebop/takeoff', Empty, queue_size=1)
    ttk.Label(mainframe, text="          ").grid(column=3, row=1, sticky=W)
    ttk.Label(mainframe, text="Take Off").grid(column=3, row=1, sticky=W)
    takeoff_pub.publish(Empty())

def land_pub():
    land_pub = rospy.Publisher('/bebop/land', Empty, queue_size=1)
    ttk.Label(mainframe, text="              ").grid(column=3, row=1, sticky=W)
    ttk.Label(mainframe, text="Land").grid(column=3, row=1, sticky=W)
    land_pub.publish(Empty())


def enviar_velocidad(vx,vy,vz,vaz):
    vel_pub = rospy.Publisher('/bebop/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x = float(vx)
    vel_msg.linear.y = float(vy)
    vel_msg.linear.z = float(vz)
    vel_msg.angular.z = float(vaz)
    vel_pub.publish(vel_msg)

def forward_pub():
    enviar_velocidad(1,0.0,0.0,0.0)

def backward_pub():
    enviar_velocidad(-1,0.0,0.0,0.0)

def left_pub():
    enviar_velocidad(0.0,1,0.0,0.0)
def right_pub():
    enviar_velocidad(0.0,-1,0.0,0.0)

def up_pub():
    enviar_velocidad(0.0,0.0,1,0.0)
def down_pub():
    enviar_velocidad(0.0,0.0,-1,0.0)

def ccw_pub():
    enviar_velocidad(0.0,0.0,0.0,1)
def cw_pub():
    enviar_velocidad(0.0,0.0,0.0,-1)


def prueba():
    if(onevar.get() == True):
        trayectoria()
            
    if(onevar.get() == False):
        print("False")

def trayectoria():
    
    x_v =  bl.control_P(4.0, odom_var.pose.pose.position.x, 0.1, 0.5, 0.2)
    enviar_velocidad(x_v,0.0,0.0,0.0)
    print "Prueba " + str(x_v)
    if (x_v != 0.0):
        trayectoria()








onevar = BooleanVar()
onevar.set(False)
one=ttk.Checkbutton(mainframe, text="Avanza", variable=onevar,onvalue=True,offvalue=False, command=prueba)
one.grid(column=1, row=4)
feet = StringVar()
print (type(bl.conv_ang(45)))
meters = str(bl.conv_ang(45))
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W,E))




#-------------- Despliegue datos de odometria y altura -------------------------
ttk.Label(mainframe, textvariable=x_odom).grid(column=1, row=2, sticky=(W,E))
ttk.Label(mainframe, textvariable=y_odom).grid(column=2, row=2, sticky=(W,E))
ttk.Label(mainframe, textvariable=z_odom).grid(column=3, row=2, sticky=(W,E))
ttk.Label(mainframe, textvariable=yaw_odom).grid(column=4, row=2, sticky=(W,E))

ttk.Label(mainframe, text="x (m)").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="y (m)").grid(column=2, row=3, sticky=W)
ttk.Label(mainframe, text="z (m)").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="az ()").grid(column=4, row=3, sticky=W)
#-------------- Despliegue datos de odometria y altura -------------------------

#---------------------------- Botones de Control -------------------------------

ttk.Button(mainframe, text="Giro CCW", command=ccw_pub).grid(column=1, row=5, sticky=W)
ttk.Button(mainframe, text="Adelante", command=forward_pub).grid(column=2, row=5, sticky=W)
ttk.Button(mainframe, text="Giro CW", command=cw_pub).grid(column=3, row=5, sticky=W)


ttk.Button(mainframe, text="Izquierda", command=left_pub).grid(column=1, row=6, sticky=W)
ttk.Button(mainframe, text="Hover", command=takeoff_pub).grid(column=2, row=6, sticky=W)
ttk.Button(mainframe, text="Derecha", command=right_pub).grid(column=3, row=6, sticky=W)

ttk.Button(mainframe, text="Arriba", command=up_pub).grid(column=1, row=7, sticky=W)
ttk.Button(mainframe, text="Atras", command=backward_pub).grid(column=2, row=7, sticky=W)
ttk.Button(mainframe, text="Abajo", command=down_pub).grid(column=3, row=7, sticky=W)
#---------------------------- Botones de Control -------------------------------



ttk.Button(mainframe, text="Take Off", command=takeoff_pub).grid(column=3, row=4, sticky=W)
ttk.Button(mainframe, text="Land", command=land_pub).grid(column=2, row=4, sticky=W)

ttk.Label(mainframe, text="1").grid(column=3, row=1, sticky=W)



for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
#root.bind('<Return>',calculate)

root.mainloop()