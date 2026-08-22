function greet(){
    console.log("hello");

}
function execute(callback){
    callback();
}
execute(greet);