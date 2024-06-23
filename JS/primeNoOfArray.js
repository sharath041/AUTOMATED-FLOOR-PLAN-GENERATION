let a=[2,4,5,7,9,33];
let i;
for (i=0;i<a.length;i++){
    let count=0;
    for(let j=1;j<=a[i];j++){
        if(a[i]%j==0){
            count ++;
        }
        
    }
    if(count==2){
        console.log(a[i]);
    }
}