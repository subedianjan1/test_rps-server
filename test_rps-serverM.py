'''
Usage: pytest -v -rx test_rps-serverM.py
-rx shows the complete reason for expected fails.

'''

import pytest
from commandM import *
#Create object C
C = commands()

@ pytest.mark.xfail(reason="CommandM is modifed only to accept Hex values")
def test_SendData():
 assert C.send_cmds('SendData', 1, 3,0) == 1, "Expected fail"
 
@ pytest.mark.xfail(reason="CommandM is modifed only to accept Hex values")
def test_SendDataS():
 assert C.send_cmds('SendData', '11', 3,0) == '11', "Expected fail"

def test_SendDataH():
 assert C.send_cmds('SendData', 0x0A, 3,0) == 0x0A




    


