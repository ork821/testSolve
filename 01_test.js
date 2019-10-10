let factorial = (n) => {
    let result = 1;
    if (n < 0) {
        console.log('Error')
        return;
    }

    if (n == 0) {
        console.log(result)
    }

    for (let i = 1; i < n + 1; i++) {
        result *= i
    }
    console.log(result)
}

factorial(12)
