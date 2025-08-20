const modal = document.getElementById('crear_alquiler_modal')
const btn_abrir_modal = document.getElementById('btn_crear_alquiler_modal')
const btn_cerrar_modal = document.getElementById('btn_cerrar_modal_crear_alquiler')
const crear_alquiler_modal = document.getElementById('crear_alquiler_modal')
btn_abrir_modal.addEventListener('click', () =>{
    modal.showModal();
})

btn_cerrar_modal.addEventListener('click', () =>{
    modal.close();
})

const btn_editar_alquiler_modal = document.getElementById('btn_editar_alquiler_modal')
const editar_alquiler_modal = document.getElementById('editar_alquiler_modal')
const btn_cerrar_modal_editar_alquiler =  document.getElementById('btn_cerrar_modal_editar_alquiler')

btn_editar_alquiler_modal.addEventListener('click', () =>{
    editar_alquiler_modal.showModal();
})

btn_cerrar_modal_editar_alquiler.addEventListener('click', () =>{
    editar_alquiler_modal.close();
})

