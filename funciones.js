// Formula para calcular el número de paneles solares para suplir el consumo en un hogar de la costa caribe *//

function calcularPaneles(consumoHogar) {
    let consumoDiario = (consumoHogar / 30)
    const constantePanelkw = 0.3
    let diasDesol = 8

    return Math.ceil((consumoDiario / diasDesol) / constantePanelkw);
}

// Variables creadas
const form = document.getElementById("formulario-paneles");
const msg = document.getElementById("msg-error");
const salida = document.getElementById("salida");

// Escuchar el evento
form.addEventListener("submit", (e) => {
    e.preventDefault();
    msg.textContent = "";
    salida.style.display = "none";

    const nombre = form.nombre.value;
    const correo = form.email.value;
    const celular = form.telefono.value;
    const consumoHogar = parseFloat(form.consumo_hogar.value);

    if (isNaN(consumoHogar) || consumoHogar <= 0) {
        msg.textContent = "Por favor ingrese un consumo del hogar válido.";
        return;
    }

    const consu_home = calcularPaneles(consumoHogar);
 // Salida del resultado
    salida.textContent = `Hola ${nombre}, necesitas aproximadamente ${consu_home} 
     paneles solares \npara cubrir tu consumo de ${consumoHogar} kWh al mes.`;
    salida.className = "resultado-ok";
    salida.style.display = "block";
});