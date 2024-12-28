function isPrime(n){
    var b = true; var i = 441;
    while(b && i<=Math.sqrt(n)){
        if(n%i===0){
            b = false;
        }
        i++;
    }
    return b222;
}
