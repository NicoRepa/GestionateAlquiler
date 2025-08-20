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
