//2
while(true) { //Empieza el bucle
let i = prompt("coloque un signo: ")
let n = prompt("coloque un numero: ")
let stop = false

if (n == 0){ //Si dice 0
    console.log("No lleva signo porque es 0")   
    stop = true
} else {
    
 if (i == "+") { //Si dice +
     console.log("el signo es positivos", i+n)
     stop = true
 } else if (i == "-") { //Si dice -
     console.log("el signo es negativo", i+n)
     stop = true
 } else { //Si pone otra cosa
     console.log("Asegurese que sea menos o mas")
 }
 
}
 if (stop == true) break; //parar cuando stop sea true
}
///4
console.log("[for]")
for (let c = 1; c < 11;) { //empieza el for
     console.log(c)
     c ++; //suma 1
}
////5
console.log("[while]")
let b = 1 
while (true) { //empieza while
    console.log(b)
    b ++; //suma 1
    if (b >= 11) break //parar cuando b sea mayor o igual a 10
}