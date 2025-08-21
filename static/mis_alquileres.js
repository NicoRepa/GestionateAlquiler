const btn_abrir_alquiler_modal = document.querySelectorAll('.btn_abrir_alquiler_modal')
const alquiler_modal = document.querySelectorAll('.alquiler_modal')
const btn_cerrar_modal_alquiler =  document.querySelectorAll('.btn_cerrar_modal_alquiler')

btn_abrir_alquiler_modal.forEach((btn, index) => {
    btn.addEventListener('click', () => {
        alquiler_modal[index].showModal();
    });
});

btn_cerrar_modal_alquiler.forEach((btn, index) => {
    btn.addEventListener('click', () => {
    alquiler_modal[index].close();
    });
});


const botonImprimir = document.getElementById('imprimir-pagina-btn');
const iframe = document.getElementById('print-iframe');

botonImprimir.addEventListener('click', () => {
    // 1. Asignar la URL de la página que queremos imprimir al iframe
    iframe.src = '/alquiler/imprimir_alquileres/';

    // 2. Escuchar el evento 'onload' del iframe
    // La impresión solo debe activarse una vez que la página dentro del iframe se haya cargado por completo
    iframe.onload = () => {
        // 3. Llamar al método de impresión del contenido del iframe
        iframe.contentWindow.print();
    };
});