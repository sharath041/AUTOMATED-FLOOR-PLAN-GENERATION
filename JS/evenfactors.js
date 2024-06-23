let a=40;
function even_factors(a){
    for(i=0;i<=a;i++){
        if(a%i==0 && i%2==0){
            console.log(i);
        }
    }
}
even_factors(a)