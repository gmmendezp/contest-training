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

var paper = ribbon = 0;
interface.on('line', function(line){
    x = line.split('x').map(Number);
    a = x[0] * x[1];
    b = x[0] * x[2];
    c = x[1] * x[2];
    paper += 2 * (a + b + c) + Math.min(a,b,c);
    ribbon += 2 * (x[0] + x[1] + x[2] - Math.max(x[0], x[1], x[2])) + x[0] * x[1] * x[2];
});

interface.on('close', function(){
    console.log(paper, ribbon);
});
