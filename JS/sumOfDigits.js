let a=2718;
function sumOfDigits(a){
    let sum=0;
    while(a>0) {
        let rem=a%10;
        sum=sum+rem;
        a=Math.floor(a/10);
    }
    return sum;
}
console.log(sumOfDigits(a));