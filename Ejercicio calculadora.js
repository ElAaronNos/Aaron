const readline = require('readline');

function mostrarMenu() {
    console.log("Selecciona una opción");
    console.log("[1] Suma");
    console.log("[2] Resta");
    console.log("[3] Multiplicación");
    console.log("[4] División");
    console.log("[5] Salir");
}

function realizarOperacion(opcion, numero1, numero2) {
    switch (opcion) {
        case '1':
            return numero1 + numero2;
        case '2':
            return numero1 - numero2;
        case '3':
            return numero1 * numero2;
        case '4':
            if (numero2 === 0) {
                console.log("Math Error: División por cero");
                return null;
            }
            return numero1 / numero2;
        default:
            console.log("Opción no válida");
            return null;
    }
}

function calculadora() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    function preguntar() {
        mostrarMenu();
        rl.question("Seleccione una opción: ", (opcion) => {
            if (opcion === '5') {
                console.log("¡Hasta luego!");
                rl.close();
                return;
            }
            rl.question("Ingrese el primer número: ", (input1) => {
                const numero1 = parseFloat(input1);
                rl.question("Ingrese el segundo número: ", (input2) => {
                    const numero2 = parseFloat(input2);
                    const resultado = realizarOperacion(opcion, numero1, numero2);
                    if (resultado !== null) {
                        console.log("Resultado: " + resultado);
                    }
                    preguntar();
                });
            });
        });
    }

    preguntar();
}


calculadora();