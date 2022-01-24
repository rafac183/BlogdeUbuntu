function sumas(...params) {
    let acum = 0
    for (let i = 0; i < params.length; i++) {
        acum = acum + params[i]
    }
    
    let acum2 = 0

    for (const elem of params) {
        acum2 = acum2 + elem
    }
    return acum2
}
const numbers = [3 ,5, 6, 4, 10, 15]
console.log(sumas(...numbers))
//console.log(numbers[numbers.length - 1])

// primera vuelta

/*
- acum = 0 + 3 
- acum = 3 + 5
- acum = 8 + 6
- acum = 14 + 4
- acum = 18 + 10
- acum = 28 + 15

*/