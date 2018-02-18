// This example uses data from api.openweathermap.org
// Please note you will require an api key.
messagetype = message.split(' ')[0].toLowerCase();
if (messagetype == 'weather') {
    requestString = 'http://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+lng+'&units=metric&appid=APIKEY';

data = getData(requestString);

json = JSON.parse(data);

output = json['weather'][0]['main'] + '/' + json['weather'][0]['description'];

return output;

} else {

	return 'Unknown request:  '+message;

}

