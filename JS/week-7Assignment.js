let array=[12,5,343,24,6644,6];
let result=array.reduce((sum,Element)=>(sum+Element));
console.log(result)




//2.modifying array using map function
let array1=[1,2,3,4];
let result2=array1.map((ele,index)=>(ele+((index+1)*10)));
console.log(result2)






//3.finding highest marks 
let array2= [

    { name:"ravi", marks :{ maths: 89, physics : 70 , chemistry :88}},

    { name:"bhanu", marks :{ maths: 98, physics : 50 , chemistry :68}},

    { name:"kiran", marks :{ maths: 50, physics : 82 , chemistry :94}},

];
highest= {
    maths: { name: '', marks: ""},
    physics: { name: '', marks: "" },
    chemistry: { name: '', marks: ""}
  };

let result3=array2.forEach((student)=>{
        for(subject in student.marks){
            if (student.marks[subject] > highest[subject].marks) {
                highest[subject].marks = student.marks[subject];
                highest[subject].name = student.name;}
}});
console.log('Highest marks in maths:', highest.maths.name);
console.log('Highest marks in physics:', highest.physics.name);
console.log('Highest marks in chemistry:', highest.chemistry.name);





let highestMaths=array2.reduce((acc,std)=>(acc.marks.maths > std.marks.maths? acc : std));
console.log("highest marks in maths : ",highestMaths.name);
let highestPhysics=array2.reduce((acc1,std1)=>(acc1.marks.physics>std1.marks.physics? acc1 : std1));
console.log("highest marks in physics:",highestPhysics.name);
let highestChemistry=array2.reduce((acc2,std2)=>(acc2.marks.chemistry>std2.marks.chemistry? acc2 : std2));
console.log("highest marks in chemistry:",highestChemistry.name);