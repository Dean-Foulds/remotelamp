import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

pins = {
	4 : {'name' : 'kettle', 'state' : GPIO.LOW},
	24 : {'name' : 'lamp', 'state' : GPIO.LOW}
	}
	
for pin in pins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
	
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
		
	templateData = {
		'message' : message,
		'pins' : pins
	}							

	return render_template('main.html', **templateData)
	
if __name__ == "__main__":
	app.run(host='192.168.1.70', port=80, debug=True)
	
GPIO.cleanup()	
