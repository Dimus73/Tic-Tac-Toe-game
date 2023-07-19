const axios = require("axios");

const options = {
  method: 'GET',
  url: 'https://stujo-tic-tac-toe-stujo-v1.p.rapidapi.com/%7Bstate%7D/%7Bplayer%7D',
  headers: {
    'X-RapidAPI-Key': '945e00047cmshd06dc63baf2cca4p1f2ac1jsn59adf7565e14',
    'X-RapidAPI-Host': 'stujo-tic-tac-toe-stujo-v1.p.rapidapi.com'
  }
};

axios.request(options).then(function (response) {
	console.log(response.data);
}).catch(function (error) {
	console.error(error);
});