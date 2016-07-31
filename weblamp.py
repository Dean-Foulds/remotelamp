import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

pins = {
	4 : {'name' : 'kettle', 'state' : GPIO.LOW},
  7 : {'name' : 'flower_lamp', 'state' : GPIO.LOW}
	}

for pin in pins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
  GPIO.setup(R1, GPIO.OUT)

@app.route("/")
def main():
	for pin in pins:
		pins[pin]['state'] = GPIO.input(pin)
	templateData = {
		'pins' : pins
		}
	return render_template('main.html', **templateData)

@app.route("/<changePin>/<action>")
def action(changePin, action):
	changePin = int(changePin)
	deviceName = pins[changePin]['name']
	if action == "on":
		GPIO.output(changePin, GPIO.HIGH)
		message = "Turned " + deviceName + " off."
	if action == "off":
		GPIO.output(changePin, GPIO.LOW)
		message = "Turned " + deviceName + " on."
	if action == "toggle":
		GPIO.output(changePin, not GPIO.input(changePin))
		message = "Toggled " + deviceName + "."

	for pin in pins:
		pins[pin]['state'] = GPIO.input(pin)

  R1 = 7
# R2 = 11
# R3 = 12
# R4 = 13
# R5 = 15
# R6 = 16
# R7 = 18
# R8 = 22

 R1ONH = 18
 R1ONM = 40
 R1ONS = 1
# R2ONH = 18
# R2ONM = 40
# R2ONS = 2
# R3ONH = 18
# R3ONM = 40
# R3ONS = 3
# R4ONH = 18
# R4ONM = 40
# R4ONS = 4
# R5ONH = 18
# R5ONM = 40
# R5ONS = 5
# R6ONH = 18
# R6ONM = 40
# R6ONS = 6
# R7ONH = 18
# R7ONM = 40
# R7ONS = 7
# R8ONH = 18
# R8ONM = 40
# R8ONS = 8

R1OFFH = 20
R1OFFM = 30
R1OFFS = 1
# R2OFFH = 18
# R2OFFM = 41
# R2OFFS = 02
# R3OFFH = 18
# R3OFFM = 41
# R3OFFS = 3
# R4OFFH = 18
# R4OFFM = 41
# R4OFFS = 4
# R5OFFH = 18
# R5OFFM = 41
# R5OFFS = 5
# R6OFFH = 18
# R6OFFM = 41
# R6OFFS = 6
# R7OFFH = 18
# R7OFFM = 41
# R7OFFS = 7
# R8OFFH = 18
# R8OFFM = 41
# R8OFFS = 8

Relay 1 On Logic
    if hour == R1ONH:             #Relay 1 On Hour setting
        if minute == R1ONM:         #Relay 1 On Minute setting
            if second == R1ONS:         #Relay 1 On Second setting
                 GPIO.output(R1, GPIO.LOW)      #Turn On Relay 1 if all above conditions are true

# #Relay 8 Off Logic
#     if hour == R8OFFH:            #Relay 8 Off Hour setting
#         if minute == R8OFFM:         #Relay 8 Off Minute setting
#             if second == R8OFFS:         #Relay 8 Off Second setting
#                 GPIO.output(R8, GPIO.HIGH)   #Turn Off Relay 8 if all above conditions are true
#
#GPIO.setup(R1, GPIO.OUT)
# GPIO.setup(R2, GPIO.OUT)
# GPIO.setup(R3, GPIO.OUT)
# GPIO.setup(R4, GPIO.OUT)
# GPIO.setup(R5, GPIO.OUT)
# GPIO.setup(R6, GPIO.OUT)
#GPIO.setup(R7, GPIO.OUT)
# GPIO.setup(R8, GPIO.OUT)
#
while True:
    dt = list(time.localtime())#Get local time and store it in dt
    hour = dt[3]
    minute = dt[4]
    second = dt[5]
    time.sleep(0.5)
    os.system('clear')
    print 'Current time: ',hour,minute,second;
    print 'Relay 1 Settings   Relay 5 Settings'
    print 'On at ',R1ONH,':',R1ONM,':',R1ONS,'   ''On at ',R5ONH,':',R5ONM,':',R5ONS;
    print 'Off at ',R1OFFH,':',R1OFFM,':',R1OFFS,'   ''Off at ',R5OFFH,':',R5OFFM,':',R5OFFS;
    print ''
    # print 'Relay 2 Settings   Relay 6 Settings'
    # print 'On at ',R2ONH,':',R2ONM,':',R2ONS,'   ''On at ',R6ONH,':',R6ONM,':',R6ONS;
    # print 'Off at ',R2OFFH,':',R2OFFM,':',R2OFFS,'   ''Off at ',R6OFFH,':',R6OFFM,':',R6OFFS;
    # print ''
    # print 'Relay 3 Settings   Relay 7 Settings'
    # print 'On at ',R3ONH,':',R3ONM,':',R3ONS,'   ''On at ',R7ONH,':',R7ONM,':',R7ONS;
    # print 'Off at ',R3OFFH,':',R3OFFM,':',R3OFFS,'   ''Off at ',R7OFFH,':',R7OFFM,':',R7OFFS;
    # print ''
    # print 'Relay 4 Settings   Relay 8 Settings'
    # print 'On at ',R4ONH,':',R4ONM,':',R4ONS,'   ''On at ',R8ONH,':',R8ONM,':',R8ONS;
    # print 'Off at ',R4OFFH,':',R4OFFM,':',R4OFFS,'   ''Off at ',R8OFFH,':',R8OFFM,':',R8OFFS;



	templateData = {
		'message' : message,
		'pins' : pins
	}

	return render_template('main.html', **templateData)

if __name__ == "__main__":
	app.run(host='192.168.1.70', port=80, debug=True)

GPIO.cleanup()
