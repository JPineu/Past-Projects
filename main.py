#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

#Color Sensor start at port S2
color_sensor = ColorSensor(Port.S4)
ultra_sens=UltrasonicSensor(Port.S3)
feed_motor = Motor(Port.A)
dispensador = Motor(Port.B)
#passadeira = Motor(Port.C)
but_emerg= TouchSensor(Port.S1)
#Ultra sonic sensor start at port S1
# ultrasonic_sensor=UltrasonicSensor(port.S1)
dist_inicial=0
#Motor start at port A
dist_inicial=ultra_sens.distance()
#Contagem de Bolas
bolas=0
i=0



 





# Write your program here.
#initial text
ev3.screen.draw_text(0, 0, "Order the colors" , text_color=Color.BLACK, background_color=None)

#Ordering colors by pressing on brick buttons

cores = []
while i < 4:
  
  ev3.screen.draw_text(0, 0, "Order the colors" , text_color=Color.BLACK, background_color=None)
  
  if Button.CENTER in ev3.buttons.pressed():
    ev3.screen.clear()
    break
    ev3.screen.draw_text(0, 0, "Reset completed" , text_color=Color.BLACK, background_color=None)
    wait(1000)
    ev3.screen.clear()
  elif Button.LEFT in ev3.buttons.pressed():
    ev3.screen.clear()
    cores.append(Color.RED)
    i+=1
    ev3.screen.draw_text(0, 0, "Red" , text_color=Color.BLACK, background_color=None)
    wait(1000)
    ev3.screen.clear()
  elif Button.RIGHT in ev3.buttons.pressed():
    ev3.screen.clear()
    cores.append(Color.BLUE)
    i+=1
    ev3.screen.draw_text(0, 0, "Blue" , text_color=Color.BLACK, background_color=None)
    wait(1000)
    ev3.screen.clear()
  elif Button.UP in ev3.buttons.pressed():
    ev3.screen.clear()
   
    cores.append(Color.YELLOW)
    i+=1
    ev3.screen.draw_text(0, 0, "YELLOW" , text_color=Color.BLACK, background_color=None)
    wait(1000)
    ev3.screen.clear()  
  elif Button.DOWN in ev3.buttons.pressed():
    ev3.screen.clear()
    cores.append(Color.GREEN)
    i+=1
    ev3.screen.draw_text(0, 0, "Green" , text_color=Color.BLACK, background_color=None)
    wait(1000)
    ev3.screen.clear()
  elif ultra_sens.distance() > dist_inicial + 6:
    bolas+=1
    print(bolas)
    wait(1000)
  if but_emerg.pressed() == True : 
    dispensador.run_angle(90,130)
    break


#How many balls are on the system to be ordered


print(cores)

print(color_sensor.color())

m=0
print(cores[m])


k=0


porta=0


#cor= Color.BLACK
while m < len(cores):
  
  #cor == color_sensor.color()
  #print(cor)
  #passadeira.run_angle(50,-144)
  dispensador.run_angle(90,120)
  wait(1500)
  dispensador.run_angle(90,-120)
  

  
    

  if color_sensor.color() == cores[m]:
    print("Bola aceite.Cor do sensor")
    wait(1000)
    porta_a = porta
    porta=1
    if porta != porta_a:  
      feed_motor.run_angle(90, 90)
      
    print(color_sensor.color())
    k=0
    print(k) 
    bolas-=1  
    print("bolas")
    print(bolas)
    
  elif color_sensor.color() in [Color.RED, Color.GREEN, Color.YELLOW, Color.BLUE]:
    print("Bola rejeitada.Cor do Sensor:")
    wait(1000)
    porta_a = porta
    porta=0
    if porta != porta_a:  
      feed_motor.run_angle(90, -90)
    
    print(color_sensor.color())
    k+=1
    print(k)
    
    if k > bolas:
      wait(500)
      m+=1
      k=0
     
      #k=1
  elif bolas==0:
      wait(500)
      if porta==1:
        feed_motor.run_angle(90, -90)

      dispensador.run_angle(100,-600)
      break
  elif but_emerg.pressed() == True:
      dispensador.run_angle(100,600)
      break
  

 
if m == len(cores):
  dispensador.run_angle(100,-600)
  if porta==1:
    feed_motor.run_angle(90,-90)
      

