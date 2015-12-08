var fs = require('fs');
var readline = require('readline');

var readable = fs.createReadStream(__dirname + '/test.in', {
    encoding: 'utf8'
});
var interface = readline.createInterface({
  input: readable,//process.stdin
  terminal: false
});

var temp = [];
interface.on('line', function(line){
    temp.push(line)
});

interface.on('close', function(){
    var m = {};
    var testKey = function(x) {
        if(!/^\d+$/.test(x) && !m.hasOwnProperty(x))
            return false;
        return true;
    };
    var getValue = function(x) {
        if(/^\d+$/.test(x))
            return +x;
        return m[x];
    };
    while(temp.length > 0){
        var line = temp.shift();
        var s = line.split(' ');
        if(s[0] === 'NOT'){
            if(!testKey(s[1])){
                temp.push(line);
                continue;
            }
            m[s[3]] = (~getValue(s[1])) & 0xffff;
        } else {
            if(!testKey(s[0])){
                temp.push(line);
                continue;
            }
            if(s[1] !== '->'){
                if(!testKey(s[2])){
                    temp.push(line);
                    continue;
                }
            }
            if(s[1] === 'AND')
                m[s[4]] = (getValue(s[0]) & getValue(s[2])) & 0xffff;
            else if(s[1] === 'OR')
                m[s[4]] = (getValue(s[0]) | getValue(s[2])) & 0xffff;
            else if(s[1] === 'LSHIFT')
                m[s[4]] = (getValue(s[0]) << getValue(s[2])) & 0xffff;
            else if(s[1] === 'RSHIFT')
                m[s[4]] = (getValue(s[0]) >> getValue(s[2])) & 0xffff;
            else
                m[s[2]] = getValue(s[0]);
        }
    }
    console.log(m['a']);
});
