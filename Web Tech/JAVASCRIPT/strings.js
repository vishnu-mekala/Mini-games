// Strings and its methods

let str1 = 'Hello'
let str2 = 'World'
let str3 = 'BRIM'

// console.log("str1 = "+str1)
// document.write("str1 = "+str1+'<br>')
// console.log("str2 = "+str2)
// document.write("str2 = "+str2+'<br>')
// console.log("str3 = "+str3)
// document.write("str3 = "+str3+'<br>')

// // to find length of string - str1.length

// console.log("length of str1 = "+str1.length)
// document.write("length of str1 = "+str1.length+'<br>')

// console.log("length of str2 = "+str2.length)
// document.write("length of str2 = "+str2.length+'<br>')

// let a = str1.length
// document.write(a+'<br>')
// let b = 'world'.length
// document.write(b+'<br>')


// //startsWith        first char index position = 0
// let sw = str1.startsWith('H')
// document.write(sw+'<br>')
// let sw1 = 'aphator'.startsWith('h')
// document.write(sw1+'<br>')
// let sw2 = str2.startsWith('H')
// document.write(sw2+'<br>')
// let sw3 = 'World'.startsWith('W')
// document.write(sw3+'<br>')

// let sw4 = str1.startsWith('l',3)    //startsWith character along with the index position of it
// document.write(sw4+'<br>')          //true because at 3 index position 'l' is present

// //endsWith()  takes the length of string not the array/index values i.e., endPosition - length
// let ew1 = str1.endsWith('w')
// document.write(ew1+'<br>')
// let ew2 = str1.endsWith('o',5)
// document.write(ew2+'<br>')

// //toUpperCase()                     //it will not affect the orginal string data/value
// let uc1 = str1.toUpperCase()
// document.write(uc1+'<br>')
// let uc2 = 'aphator'.toUpperCase()
// document.write(uc2+'<br>')

// //toLowerCase()
// let lc1 = str3.toLowerCase()
// document.write(lc1+'<br>')
// let lc2 = 'APHATOR'.toLowerCase()
// document.write(lc2+'<br>')

//to display char index position (Array Method)
document.write(str1[1]+'<br>')
document.write(str2[4]+'<br>')
document.write(str1[5]+'<br>') //undefined

//charAt() to display char index position (String Method)
let ca1 = str1.charAt(1)
let ca2 = str2.charAt(4)
let ca3 = str1.charAt(5)

        document.write(ca1+'<br>')
        document.write(ca2+'<br>')
        document.write(ca3+'<br>') // >> Blank (if no char is present at that index value)

//charCodeAt() to display char ASCII values at specific index position
let cca1 = str1.charCodeAt(1)
let cca2 = str2.charCodeAt(4)
let cca3 = str1.charCodeAt(5)

        document.write(cca1+'<br>')
        document.write(cca2+'<br>')
        document.write(cca3+'<br>') // >> NaN : Not a Number

//indexOf
let io = str1.indexOf('o')
document.write(io+'<br>')   // >> 4
let io1 = str1.indexOf('f')
document.write(io1+'<br>')   // >> -1 (if char is not present in the given str)
let io2 = str2.indexOf('o')
document.write(io2+'<br>')  // >> 1
let io3 = str1.indexOf('l')
document.write(io3+'<br>')  // >> 2 (if two or more same chars in a str, only the first char position will be displayed)

//lastIndexOf
let lio1 = str1.lastIndexOf('l')
document.write(lio1+'<br>') // >> 3 (if two or more same chars in a str, the last char position will be displayed i.e., lastindexof)
let lio2 = str2.lastIndexOf('l')
document.write(lio2+'<br>') // >> 3

//substring
let ss1 = str1.substring(1,5) // syntax = str.substring(start,end+1)
document.write(ss1+'<br>') // >> ello
let ss2 = str1.substring(5,1) 
document.write(ss2+'<br>')  // >> ello (o/p is same as 1,5)
let ss3 = str2.substring(0,4) 
document.write(ss3+'<br>') // >> Worl

//substr
let sstr1 = str1.substr(2,3) // syntax = str.substr(start,end) where, end = number of chars to be displayed from starting char
document.write(sstr1+'<br>') // >> llo
let sstr2 = str2.substr(1,7) // 
document.write(sstr2+'<br>') // >> orld
let sstr3 = str2.substr(1) // syntax: str.substr(start) if end is not mentioned the it'll display entire str till end position from given start position
document.write(sstr3+'<br>') // >> orld

//slice - same as substring method in this we have negative index, i.e.,
// 0 = H = (-5)
// 1 = e = (-4)
// 2 = l = (-3)
// 3 = l = (-2)
// 4 = o = (-1)
let sl1 = str1.slice(1,-2)
document.write(sl1+'<br>') // >> el
let sl2 = str1.slice(-4,4)
document.write(sl2+'<br>') // >> ell

//repeat
let r1 = str1.repeat(4) // syntax: str.repeat(number of times you need the str to be repeated)
document.write(r1+'<br>') // >> HelloHelloHelloHello
let r2 = str2.repeat(2)
document.write(r2+'<br>') // >> WorldWorld


//trim = It will trim/remove starting and ending spaces of a string
let str4 = "       Hello Aphator.com     "
document.write(str4 + "=" + str4.length +'<br>') //without str.trim()
let t1 = str4.trim()
document.write(t1 + "=" + t1.length +'<br>') //with str.trim()

//split
let str5 = 'a ball caught dog'
let sp1 = str5.split(' ')
document.write(sp1+'<br>')
console.log(sp1)

//Immutability
/*
     - String is Immutable
     - On the string we perform some changes using inbuilt methods, all the changes is effected to New String. Original string will be unchanged this behaviour is called its as Immutability.

*/
let i1 = "hello"
let i2 = i1.toLocaleUpperCase()

if (i1 != i2)
{console.log("Immutable")}
else
{console.log("Not Immutable")}

// let sd = "z"
// let cca111 = sd.charCodeAt(0)
// document.write(cca111+'<br>')

for (i=97; i<=122; i++)
{document.write((String.fromCharCode(i))+"<br>")}