from command import *
#Create object C
C = commands()
C.send_cmds('SetPower', 3, 0)
print (C.send_cmds('GetPower'))
