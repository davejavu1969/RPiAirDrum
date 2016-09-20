# RPiAirDrum
Raspberry Pi Air Drum Kit

Nice easy project that's a lot of fun too. 

You'll need to install the following if these libraries are not already installed on your Pi... 

Bluetooth... 

sudo apt-get install --no-install-recommends bluetooth

Cwiid... With thanks to Donnie Smith for the original and very awesome library! 

sudo apt-get install python-cwiid

You'll need to know the MAC addresses of both controllers.

Enter the following at the command prompt... 

hcitool scan 

Then press buttons 1 + 2 on both controllers, their MAC addresses will then be displayed. 
You need to enter these into the AirDrum.py script where it says to do so.

You'll need to unzip the 'drumkit' folder to the same location as the .py file. The code currently has these both just on the pi user Desktop.

I've kept the code very simple so you can play around with it. You can also get literally thousands of drum samples online

Try getting some different ones and see what you can make it sound like! 

Enjoy :-) 
