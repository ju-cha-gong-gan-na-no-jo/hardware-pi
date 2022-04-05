const express = require('express');
const morgan = require('morgan');
const path = require('path');
const fs = require('fs')
const app = express();
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const axios = require("axios");

app.set('port', process.env.PORT || 3000)
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());


axios({
  method: 'get',
  url: 'http://15.165.153.54:3000/lcd',
//  responseType: 'stream'
})
  .then(function (response) {
    console.log(response.data)
    let number = response.data["now_place"]
    console.log(number)
    require('child_process').execSync(`python3 /home/pi/data/lcd/RPi_I2C_LCD_driver/example.py ${number}`);
    setTimeout(() => process.exit(0), 10000);
  })
  .catch(function (error) {
    console.log(error);
  });
  














//app.get('/lcd/catch', function(req,res){
//axios.get('http://15.165.153.54:3000/lcd')
//.then(function (response) {
 // console.log(response)
//  console.log(response.data)
//  let number = response.data["now_place"]
//  console.log(number)
//  require('child_process').execSync(`python3 example.py ${number}`); 
//})
//.catch(function (error) {
//  console.log(error);
//});
//});

app.listen(app.get('port'), () =>{
 	console.log('3000 Port : 서버 실행 중')
 	});
