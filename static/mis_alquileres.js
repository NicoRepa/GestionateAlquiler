const modal = document.getElementById('crear_alquiler_modal')
const btn_abrir_modal = document.getElementById('btn_crear_alquiler_modal')
const btn_cerrar_modal = document.getElementById('btn_cerrar_modal_crear_alquiler')

btn_abrir_modal.addEventListener('click', () =>{
    modal.showModal();
})

btn_cerrar_modal.addEventListener('click', () =>{
    modal.close();
})