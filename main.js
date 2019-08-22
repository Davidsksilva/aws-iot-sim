var awsIot = require("aws-iot-device-sdk");

var device = awsIot.device({
  keyPath: "./auth/drone-sim-0.private.key",
  certPath: "./auth/drone-sim-0.cert.pem",
  caPath: "./auth/root-CA.crt",
  clientId: "sdk-nodejs-53c03dd9-b543-40ca-879e-a4eb0ddbd3e0",
  host: "ap60jigczfevx-ats.iot.us-east-2.amazonaws.com"
});

//
// Device is an instance returned by mqtt.Client(), see mqtt.js for full
// documentation.
//
device.on("connect", function() {
  console.log("connect");
  device.subscribe("topic_1");
  // device.publish("topic_2", JSON.stringify({ test_data: 1 }));
});

device.on("message", function(topic, payload) {
  console.log("message", topic, payload.toString());
});
