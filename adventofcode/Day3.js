var fs = require('fs');
var readline = require('readline');

var readable = fs.createReadStream(__dirname + '/test.in', {
    encoding: 'utf8'
});
var interface = readline.createInterface({
  input: readable,//process.stdin
  terminal: false
});

interface.on('line', function(line){
    var i = [0, 0];
    var j = [0, 0];
    var w = 0;
    var a = { 0 : new Set([0])};
    for (var x = 0; x < line.length; x++) {
        var c = line[x];
        if(c === '>')
            i[w]++;
        else if(c === '<')
            i[w]--;
        else if(c === 'v')
            j[w]++;
        else if(c === '^')
            j[w]--;
        if(!a[i[w]]) {
            a[i[w]] = new Set();
        }
        a[i[w]].add(j[w]);
        w ^= 1;
    }
    w = 0;
    Object.keys(a).forEach(function (key) {
        w += a[key].size;
    });
    console.log(w);
});
