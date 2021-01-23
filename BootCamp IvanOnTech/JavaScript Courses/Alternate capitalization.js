function capitalize(string){
   Number.isFinite(parseFloat(n));
   for (i=0;i<string.length; i++){
     if (isEven(string[i])){
       string[i].toUpperCase();
     } 
     else if (isOdd(string[i])){
       string[i].toLowerCase();       
     }
  return []; 
     
     for (i=0;i<string.length; i++){
     if (isOdd(string[i])){
       string[i].toUpperCase();
     } 
     else if (isEven(string[i])){
       string[i].toLowerCase();       
     }
  return []; 
}  
  
function isEven(n) {
   return n % 2 == 0;
}

function isOdd(n) {
   return Math.abs(n % 2) == 1;
}

