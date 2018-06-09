from bottle import route, run, template
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [18, 23]
ledStates = [0, 0]
button = 24
GPIO.setup(leds[0], GPIO.OUT)
GPIO.setup(leds[1], GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while run:

def update_leds():
#    while True:
            #for i, value in enumerate(ledStates):       
                GPIO.output(leds[0], True)
                time.sleep(1)
                GPIO.output(leds[0], False)
                time.sleep(1)
                GPIO.output(leds[0], True)
                time.sleep(1)
                GPIO.output(leds[0], False)
                time.sleep(1)
                GPIO.output(leds[0], True)
                time.sleep(1)
                GPIO.output(leds[0], False)
                time.sleep(1)
#        if n==3:
#            break
#            GPIO.output(leds[i], False)
            
    
           
def stop():
    for i, value in enumerate(ledStates):
        GPIO.output(leds[0], False)
    
control_page = """

<script>
function changed(id)
{
window.location.href='/' + id
}

function audio(){
    var audio = new Audio('a.mp3');
    audio.play();
}
</script>
<h1>GPIO Control</h1>
<h2>Button
% if btnState:
    =Up
% else:
    =Down
% end
</h2>
<h2>LED</h2>
<input type='button' onClick='changed({{led0}})' value='LED {{led0}}'/>
<input type='button' onClick='changed({{led1}})' value='LED {{led1}}'/>
<input type='button' onClick='changed({{led2}})' value='LED {{led2}}'/>
<input type='button' onClick='audio()' />
"""


@route('/')
@route('/<led>')
def index(led="n"):
    if led == "0" and led != "favicon.ico":
        num = int(led)
        ledStates[num] = not ledStates[num]
        stop()
    
    elif led == "1" and led != "favicon.ico":
        num = int(led)
        ledStates[num] = not ledStates[num]
        update_leds()
        
    state = GPIO.input(button)
    return template(control_page, btnState=state,
led0=0, led1=1, led2=2)


run(host='localhost', port=8080)