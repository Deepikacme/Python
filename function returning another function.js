function outer(){ 
    return function(){ 
        console.log("Hello"); 
    }; 
} 
let result=outer(); 
result(); 