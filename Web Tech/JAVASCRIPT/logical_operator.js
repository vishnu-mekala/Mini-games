document.write("<h2> Logical Operator</h2>")

let a = 10
let b = 20
let c = 5

let S1 = (a>b) && (a<b) || (c<b)
document.write("S1 = "+S1+"<br>")

let S2 = (c>b) && (b<a) || (c<a)
document.write("S2 = "+S2+"<br>")
