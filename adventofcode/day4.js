var crypto = require('crypto');
var md5sum = crypto.createHash('md5');

var s = 'iwrupvqb';
md5sum.update(s);
var i = 0;
var val = '';
while(val.substring(0,6) !== '000000') {
    i += 1
    val = crypto.createHash('md5').update(s + i).digest('hex');
}
console.log(val, i);
