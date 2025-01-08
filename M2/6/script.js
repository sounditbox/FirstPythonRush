function fib(n) {
    // Функция вычисления n-го числа Фибоначчи
    // var const let
    let a = 0;
    let b = 1;
    for (let i = 0; i < n; i++) {
        let temp = a;
        a = b;
        b = temp + b;
    }
    return a;
}

console.log(fib(10));