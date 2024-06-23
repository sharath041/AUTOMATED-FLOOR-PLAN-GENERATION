let s='aaaabbababababbbbabababaaaa';
let frequencyA=0;
let frequencyB=0;
for(i=0;i<s.length;i++){
    if(s[i]=='a'){
        frequencyA++;
    }
    if(s[i]=='b'){
        frequencyB++;
    }
}
console.log("Frequency of a is:",frequencyA);
console.log("Frequency of b is:",frequencyB);






//Counting number of words in a string
let str='how are you all'
function count (str){
    let words=str.split(' ');
    let wordscount=words.length;
    return wordscount;

}
console.log(count(str))