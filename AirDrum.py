import cwiid
import time
import os


wm = None
wm2 = None

i=1

while not wm:
        for x in range(0,6):
                try:
                        time.sleep(0.5)
                        print "Bluetooth pairing attempt " + str(i)
                        wm = cwiid.Wiimote("Insert WiiMote MAC address here")
                        wm.led = 1
                        if wm:
                                break

                        
                except RuntimeError:
                        if (i>=5):
                                print("cannot create connection")
                                quit()
                        print "Error opening wiimote connection"
                        i +=1

print "Remote #1 Connected"

time.sleep(1)

i=1

while not wm2:
        for x in range(0,5):
                try:
                        time.sleep(0.5)
                        print "Bluetooth pairing attempt " + str(i)
                        wm2 = cwiid.Wiimote("Insert WiiMote MAC address here")
                        wm2.led = 2
                        if wm2:
                                break

                except RuntimeError:
                        if (i>=5):
                                print("cannot create connection")
                                quit()
                        print "Error opening wiimote connection"
                        i +=1

print "Remote #2 Connected"

time.sleep(1)


#set wiimote to report button presses and accelerometer state
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

wm2.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC


buttons = wm.state['buttons']
buttons2 = wm2.state['buttons']
acc = wm.state
acc2 = wm2.state

tom_hit = False
tom_hit2 = False

snare_hit = False
bongo_hit = False

cym1_hit = False
cym1_hit2 = False

while not(buttons == 140 or buttons2 == 140):
        buttons = wm.state['buttons']
        buttons2 = wm2.state['buttons']
        acc = wm.state
        acc2 = wm2.state 
        pos1 = acc['acc']
        pos2 = acc2['acc']
        but1 = acc['buttons']
        but2 = acc2['buttons'] 

        if (buttons == 13): # Halt
                wm.led = 2
                print ("Halting Raspberry Pi...")
                bashCommand = ("sudo halt")

        ## Controller #1 ##
        if but1 == 0 and pos1[0] >= 120 and pos1[2] <= 105 and not tom_hit:
                print "Tom1"
                print pos1
                os.system('aplay /home/pi/Desktop/drumkit/Tom01.wav &' )
                tom_hit = True

        if but1 == 4 and pos1[0] >= 120 and pos1[2] <= 105 and not bongo_hit:
                print "Bongo"
                print pos1
                os.system('aplay /home/pi/Desktop/drumkit/kit1103.wav &' )
                bongo_hit = True

        if pos1[0] <= 30 and pos1[1] >= 141 and not cym1_hit:
                print "Cymbal"
                print pos1
                os.system('aplay /home/pi/Desktop/drumkit/CYMBL1.wav &' )                
                cyml_hit = True

        if pos1[2] >=  110 and tom_hit:
                tom_hit = False
        if pos1[2] >=  110 and bongo_hit:
                bongo_hit = False
        if pos1[0] > 50 and cym1_hit:
                cym1_hit = False



        ## Controller #2 ##

        if but2 == 4 and pos2[0] >= 120 and pos2[2] <= 105 and not tom_hit2:
                print "Tom2"
                print pos2
                os.system('aplay /home/pi/Desktop/drumkit/kit252.wav &' )
                tom_hit2 = True

        if but2 == 0 and pos2[0] >= 120 and pos2[2] <= 105 and not snare_hit:
                print "Snare1"
                print pos2
                os.system('aplay /home/pi/Desktop/drumkit/Snare09.wav &' )
                snare_hit = True


        if pos2[0] >= 190 and not cym1_hit2:
                print "Cymbal2"
                print pos2
                os.system('aplay /home/pi/Desktop/drumkit/Ride2.wav &' )                
                cyml_hit2 = True

        if pos2[2] >=  110 and tom_hit2:
                tom_hit2 = False
        if pos2[2] >=  110 and snare_hit:
                snare_hit = False
        if pos2[0] > 50 and cym1_hit2:
                cym1_hit2 = False 
       






