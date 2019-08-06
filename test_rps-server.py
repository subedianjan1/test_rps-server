from command import *
#Create object C
C = commands()
C.send_cmds('SetPower', 3, 0)
print (C.send_cmds('GetPower'))


def test_port0():
    #Trun ON
    assert C.send_cmds('SetPower', 0, 1) == True
    assert C.send_cmds('GetPower')== "P60=1P61=0P62=0P63=0"
    #Trun OFF
    assert C.send_cmds('SetPower', 0, 0) == True
    assert C.send_cmds('GetPower')== "P60=0P61=0P62=0P63=0"
    #Check status
    assert C.form_query(1,' ', 1) == {'P61': 1}
    

    
def test_port1():
    #Trun ON
    assert C.send_cmds('SetPower', 1, 1) == True
    assert C.send_cmds('GetPower')== "P60=0P61=1P62=0P63=0"
    #Trun OFF
    assert C.send_cmds('SetPower', 1, 0) == True
    assert C.send_cmds('GetPower')== "P60=0P61=0P62=0P63=0"


def test_port2():
    #Trun ON
    assert C.send_cmds('SetPower', 2, 1) == True
    assert C.send_cmds('GetPower')== "P60=0P61=0P62=1P63=0"
    #Trun OFF
    assert C.send_cmds('SetPower', 2, 0) == True
    assert C.send_cmds('GetPower')== "P60=0P61=0P62=0P63=0"


def test_port3():
    #Trun ON
    assert C.send_cmds('SetPower', 3, 1) == True
    assert C.send_cmds('GetPower')== "P60=0P61=0P62=0P63=1"
    #Trun OFF
    assert C.send_cmds('SetPower', 3, 0) == True
    assert C.send_cmds('GetPower')== "P60=0P61=0P62=0P63=0"

