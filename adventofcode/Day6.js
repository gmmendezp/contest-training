var fs = require('fs');
var readline = require('readline');

var readable = fs.createReadStream(__dirname + '/test.in', {
    encoding: 'utf8'
});
var interface = readline.createInterface({
  input: readable,//process.stdin
  terminal: false
});

var m = Array(1000).fill().map(()=>Array(1000).fill().map(()=>0));
interface.on('line', function(line){
    var s = line.split(' ');
    if(s[0] === 'turn'){
        var val = -1
        var a = s[2].split(',').map((x)=>+x);
        var b = s[4].split(',').map((x)=>+x);
        if(s[1] === 'on')
            val = 1
        for(var i=a[0]; i<=b[0]; i++){
            for(var j=a[1]; j<=b[1]; j++){
                m[i][j] += val;
                if(m[i][j] < 0)
                    m[i][j] = 0;
            }
        }
    } else {
        var a = s[1].split(',').map((x)=>+x);
        var b = s[3].split(',').map((x)=>+x);
        for(var i=a[0]; i<=b[0]; i++)
            for(var j=a[1]; j<=b[1]; j++)
                m[i][j] += 2;
    }
});

interface.on('close', function(){
    console.log(m.reduce((a,b)=>a + b.reduce((b1,b2)=>b1 + b2),0));
});
