var fs = require('fs');
var readline = require('readline');

var readable = fs.createReadStream(__dirname + '/test.in', {
    encoding: 'utf8'
});
var writable = fs.createWriteStream(__dirname + '/test.out');
var interface = readline.createInterface({
  input: readable,//process.stdin
  output: writable,//process.stdout
  terminal: false
});

var index = 0;
interface.on('line', function(line){
    // line is the number of cases
    interface.removeAllListeners('line');
    interface.on('line', function(line){
        index++;
        x = line;
        interface.output.write(`Case #${index}: ${x}\n`);
    });
});

interface.on('close', function(){

});
