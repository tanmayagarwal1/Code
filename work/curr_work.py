# -*- coding: utf-8 -*-
"""
Created on Tue April 20 00:13:50 2021

@author: Tanmay Agarwal 

Potential Field based planner

"""

from collections import deque
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import serial 
import argparse 
from dronekit import connect, VehicleMode, InternalGlobalRelative 

parser=argparse.ArgumentParser()
parser.add_argument('--connect',default='127.0.0.1:14550')
args=parser.parse_args()
vehicle=connect(args.connect, baud=921600,wait_ready=True )
ser=serial.Serial("/dev/ttyACM0",9600,timeout=1)

KP = 5.0 
ETA = 100.0 
AREA_WIDTH = 30.0 
OSCILLATIONS_DETECTION_LENGTH = 3

show_animation = True


oX = [-5]
oY = [0]

def goatMap_x(x):
    return (x - (-0.5)) * (1000 - 2000) / (0.5 - (-0.5)) + 2000

def goatMap_y(y):
    return (y - (-0.5)) * (2000 - 1000) / (0.5 - (-0.5)) + 1000


def calc_potential_field(gx, gy, ox, oy, reso, rr, sx, sy):
    minx = min(min(ox), sx, gx) - AREA_WIDTH / 2.0
    miny = min(min(oy), sy, gy) - AREA_WIDTH / 2.0
    maxx = max(max(ox), sx, gx) + AREA_WIDTH / 2.0
    maxy = max(max(oy), sy, gy) + AREA_WIDTH / 2.0
    xw = int(round((maxx - minx) / reso))
    yw = int(round((maxy - miny) / reso))

    # calc each potential
    pmap = [[0.0 for i in range(yw)] for i in range(xw)]

    for ix in range(xw):
        x = ix * reso + minx

        for iy in range(yw):
            y = iy * reso + miny
            ug = calc_attractive_potential(x, y, gx, gy)
            uo = calc_repulsive_potential(x, y, ox, oy, rr)
            uf = ug + uo
            pmap[ix][iy] = uf

    return pmap, minx, miny


def calc_attractive_potential(x, y, gx, gy):
    return 0.5 * KP * np.hypot(x - gx, y - gy)


def calc_repulsive_potential(x, y, ox, oy, rr)
    minid = -1
    dmin = float("inf")
    for i, _ in enumerate(ox):
        d = np.hypot(x - ox[i], y - oy[i])
        if dmin >= d:
            dmin = d
            minid = i

    dq = np.hypot(x - ox[minid], y - oy[minid])

    if dq <= rr:
        if dq <= 0.1:
            dq = 0.1

        return 0.5 * ETA * (1.0 / dq - 1.0 / rr) ** 2
    else:
        return 0.0


def get_motion_model():
    motion = [[1, 0],
              [0, 1],
              [-1, 0],
              [0, -1],
              [-1, -1],
              [-1, 1],
              [1, -1],
              [1, 1]]

    return motion


def oscillations_detection(previous_ids, ix, iy):
    previous_ids.append((ix, iy))

    if (len(previous_ids) > OSCILLATIONS_DETECTION_LENGTH):
        previous_ids.popleft()


    previous_ids_set = set()
    for index in previous_ids:
        if index in previous_ids_set:
            return True
        else:
            previous_ids_set.add(index)
    return False



def potential_field_planning(sx, sy, gx, gy, ox, oy, reso, rr):
    

    pmap, minx, miny = calc_potential_field(gx, gy, ox, oy, reso, rr, sx, sy)
    initi_distX = 0
    initi_distY =
    d = np.hypot(sx - gx, sy - gy)
    ix = round((sx - minx) / reso)
    iy = round((sy - miny) / reso)
    gix = round((gx - minx) / reso)
    giy = round((gy - miny) / reso)

    if show_animation:
        draw_heatmap(pm
        plt.gcf().canvas.mpl_connect('key_release_event',
                lambda event: [exit(0) if event.key == 'escape' else None])
        plt.plot(ix, iy, "*k")
        plt.plot(gix, giy, "*m")
        
    rx, ry = [sx], [sy]
    motion = get_motion_model()
    previous_ids = deque()


    while d >= reso:
        i = int(ser.readline().decode('utf-8').rstrip())
        if i < 150:
            oX.append(sx + (i/100)+0.1)
            oY.append(sy)
        else:
            dummy = 1
        pmap, minx, miny = calc_potential_field(gx, gy, ox, oy, reso, rr, sx, sy)
        d = np.hypot(sx - gx, sy - gy)
        ix = round((sx - minx) / reso)
        iy = round((sy - miny) / reso)
        gix = round((gx - minx) / reso)
        giy = round((gy - miny) / reso)
        if show_animation:
            draw_heatmap(pmap)
            plt.gcf().canvas.mpl_connect('key_release_event',
                   lambda event: [exit(0) if event.key == 'escape' else None])
            plt.plot(ix, iy, "*k")
            plt.plot(gix, giy, "*m")
        minp = float("inf")
        minix, miniy = -1, -1
        for i, _ in enumerate(motion):
            inx = int(ix + motion[i][0])
            iny = int(iy + motion[i][1])
            if inx >= len(pmap) or iny >= len(pmap[0]) or inx < 0 or iny < 0:
                p = float("inf") 
                print("outside potential!")
            else:
                p = pmap[inx][iny]
            if minp > p:
                minp = p
                minix = inx
                miniy = iny
        ix = minix
        iy = miniy
        xp = ix * reso + minx
        yp = iy * reso + miny
        sx = xp
        sy = yp
        V_x = sx - initi_distX
        V_y = sy - initi_distY 
        time_duration = 1
        Vx=goatMap_x(V_x)
        Vy=goatMap_y(V_y)
        vehicle.channels.overrides['2'] = Vx
        vehicle.channels.overrides['1'] = Vy
        time.sleep(1)
      
        
        
        print("velocity in x :", V_x)
        print("velocity in y :", V_y)
        print(sx)
        print(sy)
        initi_distX = sx
        initi_distY = sy
        d = np.hypot(gx - xp, gy - yp)
        rx.append(xp)
        ry.append(yp)

        if (oscillations_detection(previous_ids, ix, iy)):
            print("Oscillation detected at ({},{})!".format(ix, iy))
            

        if show_animation:
            plt.plot(ix, iy, ".r")
            plt.pause(0.01)

    print("Goal!!")

    return rx, ry


def draw_heatmap(data):
    data = np.array(data).T
    plt.pcolor(data, vmax=100.0, cmap=plt.cm.Blues)

def main():
    print("potential_field_planning start")

    sx = 0.0 
    sy = 0.0 
    gx = 7.0 
    gy = 0.0 
    grid_size = 0.3 
    robot_radius = 1.2  

    ox = oX
    oy = oY
    
    if show_animation:
        plt.grid(True)
        plt.axis("equal"
    _, _ = potential_field_planning(
        sx, sy, gx, gy, ox, oy, grid_size, robot_radius)

    if show_animation:
        plt.show()


if __name__ == '__main__':
    print(__file__ + " start!!")
    main()
    print(__file__ + " Done!!")

def send_velocity(velocity_x, velocity_y, velocity_z, duration):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,    
        0, 0,   
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        0b0000111111000111,
        0, 0, 0,
        velocity_x, velocity_y, velocity_z, 
        0, 0, 0, 
        0,
    for x in range(0,duration):
        vehicle.send_mavlink(msg)
        time.sleep(1)
