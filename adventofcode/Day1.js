var fs = require('fs');
var readline = require('readline');

var readable = fs.createReadStream(__dirname + '/test.in', {
    encoding: 'utf8',
    highWaterMark: 16 * 1024
});
var interface = readline.createInterface({
  input: readable,//process.stdin
  terminal: false
});
interface.on('line', function(line){
    var count = minus1 = 0;
    var found = false;
    for(var i=0; i<line.length; i++) {
        var c = line[i];
        count += (c === '(') ? 1 : -1;
        if(count === -1 && !found) {
            minus1 = i;
            found = true;
        }
    }
    console.log(count, minus1);
});
