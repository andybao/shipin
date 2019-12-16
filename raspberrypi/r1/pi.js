const Gpio = require('onoff').Gpio;
const led = new Gpio(17, 'out');

$("#on").click(function() {
    led.writeSync(1);
    alert("ON");
});
$("#off").click(function() {
    led.writeSync(0);
    alert("OFF");
});