var fs = require('fs');
var readline = require('readline');

var readable = fs.createReadStream(__dirname + '/test.in', {
    encoding: 'utf8'
});
var interface = readline.createInterface({
  input: readable,//process.stdin
  terminal: false
});

var totalDecode = 0;
var totalEncode = 0;
interface.on('line', function(line){
    var decoderCount = function(s){
        var total = 0;
        var i = 0;
        for(var i=0; i < s.length; i++){
            if(s[i] !== '\"'){
                if(s[i] === '\\'){
                    i++;
                    if(s[i] == 'x'){
                        total += 3;
                        i += 2;
                    } else {
                        total += 1
                    }
                }
            } else {
                total++;
            }
        }
        return total;
    };
    var encoderCount = function(s){
        var total = 2;
        for(var i=0; i < s.length; i++)
            if(s[i] === '\"' || s[i] === '\\')
                total++;
        return total;
    };
    totalDecode += decoderCount(line)
    totalEncode += encoderCount(line)
});

interface.on('close', function(){
    console.log(totalDecode, totalEncode)
});
