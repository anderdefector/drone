#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    Nov 17, 2019 03:26:45 PM CST  platform: Linux

import sys
import rospy
from sensor_msgs.msg import Image
from nav_msgs.msg import Odometry
from bebop_msgs.msg import Ardrone3PilotingStateAltitudeChanged
from bebop_msgs.msg import CommonCommonStateBatteryStateChanged
from std_msgs.msg import String


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import bebop_control_orbaslam_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Top_level (root)
    bebop_control_orbaslam_support.set_Tk_var()
    bebop_control_orbaslam_support.init(root, top)
    rospy.init_node("Interface", anonymous=False)
    rospy.Subscriber("/slam_bebop_pose", String, bebop_control_orbaslam_support.receive_pose)
    rospy.Subscriber("/bebop/image_raw", Image, bebop_control_orbaslam_support.receive_img)    
    rospy.Subscriber("/bebop/odom", Odometry , bebop_control_orbaslam_support.receive_odom)
    rospy.Subscriber("/bebop/states/ardrone3/PilotingState/AltitudeChanged", Ardrone3PilotingStateAltitudeChanged, bebop_control_orbaslam_support.receive_altitud)
    rospy.Subscriber("/bebop/states/common/CommonState/BatteryStateChanged", CommonCommonStateBatteryStateChanged, bebop_control_orbaslam_support.receive_beteria)
    root.mainloop()

w = None
def create_Top_level(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Top_level (w)
    bebop_control_orbaslam_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Top_level():
    global w
    w.destroy()
    w = None

class Top_level:
    def __init__(self, top=None):

        top.geometry("600x479+386+159")
        top.title("Bebop Control")

        self.imagen = tk.Label(top)
        self.imagen.place(relx=0.417, rely=0.23, height=240, width=320)
        self.imagen.configure(background="#2de305")

        self.coordenadas = tk.Text(top)
        self.coordenadas.place(relx=0.083, rely=0.271,height=180, relwidth=0.293)
        self.coordenadas.configure(background="#e1e9f5")
        self.coordenadas.configure(font="TkFixedFont")
        self.coordenadas.configure(width=176)

        self.L1_txt = tk.Label(top)
        self.L1_txt.place(relx=0.15, rely=0.219, height=18, width=99)
        self.L1_txt.configure(text='''Puntos a Seguir''')

        self.Lf_1 = tk.LabelFrame(top)
        self.Lf_1.place(relx=0.083, rely=0.668, relheight=0.24, relwidth=0.283)
        self.Lf_1.configure(relief='groove')
        self.Lf_1.configure(text='Posición')
        self.Lf_1.configure(width=170)

        self.Lbl_x = tk.Label(self.Lf_1)
        self.Lbl_x.place(relx=0.118, rely=0.13, height=18, width=136, bordermode='ignore')
        self.Lbl_x.configure(text='x:')
        self.Lbl_x.configure(width=136)

        self.Lbl_z = tk.Label(self.Lf_1)
        self.Lbl_z.place(relx=0.118, rely=0.565, height=18, width=136, bordermode='ignore')
        self.Lbl_z.configure(activebackground="#f9f9f9")
        self.Lbl_z.configure(text='z:')

        self.Lbl_y = tk.Label(self.Lf_1)
        self.Lbl_y.place(relx=0.118, rely=0.348, height=18, width=136, bordermode='ignore')
        self.Lbl_y.configure(activebackground="#f9f9f9")
        self.Lbl_y.configure(text='y:')

        self.Lbl_a = tk.Label(self.Lf_1)
        self.Lbl_a.place(relx=0.118, rely=0.739, height=18, width=136, bordermode='ignore')
        self.Lbl_a.configure(activebackground="#f9f9f9")
        self.Lbl_a.configure(text='a:')

        self.Bt_inicio = tk.Button(top)
        self.Bt_inicio.place(relx=0.083, rely=0.919, height=28, width=159)
        self.Bt_inicio.configure(text='Iniciar')
        self.Bt_inicio.configure(width=159)
        self.Bt_inicio.configure(command=bebop_control_orbaslam_support.fcn_inicio)
        self.logo_unicauca = tk.Label(top)
        self.logo_unicauca.place(relx=0.15, rely=0.042, height=68, width=66)
        self.logo_unicauca.configure(width=66)

        self.logo_cinvestav = tk.Label(top)
        self.logo_cinvestav.place(relx=0.817, rely=0.042, height=68, width=66)
        self.logo_cinvestav.configure(activebackground="#f9f9f9")

        self.titulo = tk.Label(top)
        self.titulo.place(relx=0.35, rely=0.084, height=18, width=226)
        self.titulo.configure(text='Control de Trayectoria Bebop')
        self.titulo.configure(width=226)

if __name__ == '__main__':
    vp_start_gui()





