var fs = require('fs');
var readline = require('readline');
var combinatorics = require('js-combinatorics');

var readable = fs.createReadStream(__dirname + '/test.in', {
    encoding: 'utf8'
});
var interface = readline.createInterface({
  input: readable,//process.stdin
  terminal: false
});

var dist = Array(3).fill().map(()=>Array(3).fill().map(()=>0));
var index = {};
var x = 0;
interface.on('line', function(line){
    s = line.split(' ');
    if(!(s[0] in index)){
        index[s[0]] = x;
        x++;
    }
    if(!(s[2] in index)){
        index[s[2]] = x;
        x++;
    }
    dist[index[s[0]]][index[s[2]]] = +s[4];
    dist[index[s[2]]][index[s[0]]] = +s[4];
});

interface.on('close', function(){
    console.log(Math.min.apply(null, combinatorics.permutation(Object.keys(index).map((x)=>index[x])).map((p)=> p.reduce((y,x,i,a)=> y + ((i > 0) ? dist[x][a[i-1]] : 0)))));
    console.log(Math.max.apply(null, combinatorics.permutation(Object.keys(index).map((x)=>index[x])).map((p)=> p.reduce((y,x,i,a)=> y + ((i > 0) ? dist[x][a[i-1]] : 0)))));
});

