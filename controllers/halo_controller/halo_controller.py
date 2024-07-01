from controller import Robot
from controller import Keyboard
#from controller import Pen

# create the Robot instance.
robot = Robot()
kb= Keyboard()

timestep = int(robot.getBasicTimeStep())

motorA = robot.getDevice("A motor")
motorB = robot.getDevice("B motor")
motorC = robot.getDevice("C motor")
motorD = robot.getDevice("D motor")
motorE = robot.getDevice("E motor")
motorF = robot.getDevice("F motor")

pen=robot.getDevice("pen")

kb.enable(timestep)

ds= robot.getDevice("ds")
ds.enable(timestep)

motorA_pos=3.14
motorB_pos=0
motorC_pos=0
motorD_pos=0
motorE_pos=0
motorF_pos=0
b = 0.921
e = 0.5


draw=True

colors=[0xF01010,0xFF7F00,0xFFFF00,0x00FF00,0x0000FF,0x4B0082,0x9400D3]
color_index=0

pen.setInkColor(0xF01010,1)

def add_delay(delay_time_steps):

    time_counter = 0
    while robot.step(timestep)  !=  -1:
        if time_counter  >=  delay_time_steps:
            break
        
        time_counter += 1
        
def halo(a = 3.14):
    motorB.setPosition(b)
    motorE.setPosition(e)
    motorA.setPosition(a)
    
halo()
add_delay(50)
halo(3.14)
add_delay(15)
halo(3.5)
add_delay(15)
halo(3)
add_delay(15)
halo(2.9)
add_delay(15)
halo(2.8)
add_delay(15)
halo(2.7)
add_delay(15)
halo(2.6)
add_delay(15)
halo(2.5)
add_delay(15)
halo(2.4)
add_delay(15)
halo(2.3)
add_delay(15)
halo(2.2)
add_delay(15)
halo(2.1)
add_delay(15)
halo(2)
add_delay(15)
halo(1.9)
add_delay(15)
halo(1.8)
add_delay(15)
halo(1.7)
add_delay(15)
halo(1.6)
add_delay(15)
halo(1.5)
add_delay(15)
halo(1.4)
add_delay(15)
halo(1.3)
add_delay(15)
halo(1.2)
add_delay(15)
halo(1.1)
add_delay(15)
halo(1)
add_delay(15)
halo(0.9)
add_delay(15)
halo(0.8)
add_delay(15)
halo(0.7)
add_delay(15)
halo(0.6)
add_delay(15)
halo(0.5)
add_delay(15)
halo(0.4)
add_delay(15)
halo(0.3)
add_delay(15)
halo(0.2)
add_delay(15)
halo(0.1)
add_delay(15)
halo(0)
add_delay(15)
halo(-0.1)
add_delay(15)
halo(-0.2)
add_delay(15)
halo(-0.3)
add_delay(15)
halo(-0.4)
add_delay(15)
halo(-0.5)
add_delay(15)
halo(-0.6)
add_delay(15)
halo(-0.7)
add_delay(15)
halo(-0.8)
add_delay(15)
halo(-0.9)
add_delay(15)
halo(-1)
add_delay(15)
halo(-1.1)
add_delay(15)
halo(-1.2)
add_delay(15)
halo(-1.3)
add_delay(15)
halo(-1.4)
add_delay(15)
halo(-1.5)
add_delay(15)
halo(-1.6)
add_delay(15)
halo(-1.7)
add_delay(15)
halo(-1.8)
add_delay(15)
halo(-1.9)
add_delay(15)
halo(-2)
add_delay(15)
halo(-2.1)
add_delay(15)
halo(-2.2)
add_delay(15)
halo(-2.3)
add_delay(15)
halo(-2.4)
add_delay(15)
halo(-2.5)
add_delay(15)
halo(-2.6)
add_delay(15)
halo(-2.7)
add_delay(15)
halo(-2.8)
add_delay(15)
halo(-2.9)
add_delay(15)
halo(-3.0)
add_delay(15)
halo(-3.14)
        
        
def moveback():
    motorA.setPosition(motorA_pos)
    motorB.setPosition(motorB_pos)
    motorC.setPosition(motorC_pos)
    motorD.setPosition(motorD_pos)
    motorE.setPosition(motorE_pos)
    motorF.setPosition(motorF_pos)
    
add_delay(15)
moveback()

# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    ds_val=ds.getValue()
    # print(movement)
    
     
    # motorA.setPosition(motorA_pos)
    # motorB.setPosition(motorB_pos)
    # motorC.setPosition(motorC_pos)
    # motorD.setPosition(motorD_pos)
    # motorE.setPosition(motorE_pos)
    # motorF.setPosition(motorF_pos)