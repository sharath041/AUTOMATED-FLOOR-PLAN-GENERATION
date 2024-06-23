let student={
    name:'SharathChandra',
    rollNo:540,
    marks:[99,97,89,93,95,96],
    address:{
        village:'sadasivpet',
        pincode:502291,
        district:'sangareddy'
    },
    percentage:function(){
        let sum=0;
        for(let i of this.marks){
            sum=sum+i;
        }
        let avg=sum/600;
        let percent=avg*100;
        return percent;
    }
}
console.log(student);
console.log(student.percentage());