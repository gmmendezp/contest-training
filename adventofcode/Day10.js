var s = '1321131112';
for(var i=0; i<40; i++) {
    var n = '';
    var count = 0;
    var last = ' ';
    for(c in s){
        if(last !== c) {
            n += (count ? count : '') + last;
            last = c;
            count = 0;
        }
        count++;
    }
    n += count + last
    s = n;
}
console.log(n.length);
