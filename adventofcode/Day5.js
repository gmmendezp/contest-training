var fs = require('fs');
var readline = require('readline');

var readable = fs.createReadStream(__dirname + '/test.in', {
    encoding: 'utf8'
});
var interface = readline.createInterface({
  input: readable,//process.stdin
  terminal: false
});

var vowels = 'aeiou';
var forbidden = ['ab', 'cd', 'pq', 'xy'];
var count1 = count2 = 0;
interface.on('line', function(line){
    // first half
    var countVowels = 0;
    var twice = false;
    var nice = true;
    var last = '';
    for (var k = 0; k < line.length; k++) {
        var x = line[k];
        if(vowels.indexOf(x) >= 0)
            countVowels++;
        if(x === last)
            twice = true;
        forbidden.forEach(function(f){
            if(x === f[1] && last === f[0])
                nice = false;
        });
        last = x;
    }
    if(nice && twice && countVowels >= 3)
        count1++;
    // end first half
    // second half
    var x = new Set();
    twice = false;
    var trio = false;
    last = '';
    for(var i = 0; i < line.length - 1; i++){
        var current = line.substring(i, i+2);
        if(x.has(current))
            twice = true;
        if(last !== '')
            x.add(last)
        last = current;
        if(i < line.length - 2) {
            temp = line.substring(i, i+3);
            if(temp[0] === temp[2])
                trio = true;
        }
    }
    if(twice && trio)
        count2++;
    // end second half
});

interface.on('close', function(){
    console.log(count1, count2);
});
