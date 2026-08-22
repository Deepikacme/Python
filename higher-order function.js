function calculate(operation) { 
    return operation(10,20);
 } 
 let result=calculate((a,b)=>a+b); 
 console.log(result); 