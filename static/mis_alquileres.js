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


//JS para checkbox de crear alquiler
const checkbox_Agua = document.getElementById('checkbox_agua');
const input_Agua = document.getElementById('id_Precio_Agua');
const checkbox_Pasto = document.getElementById('checkbox_Pasto');
const input_Pasto = document.getElementById('id_Precio_Pasto');
const checkbox_ABL = document.getElementById('checkbox_ABL');
const input_ABL = document.getElementById('id_Precio_ABL');

function checkbox_crear_alquiler(checkbox,input){
  if (checkbox.checked){
    input.removeAttribute('disabled');
  }else {
    input.setAttribute('disabled','disabled')
    input.value = '';

  }
}

checkbox_Agua.addEventListener('change', function() {
  checkbox_crear_alquiler(checkbox_Agua,input_Agua)
});

checkbox_ABL.addEventListener('change',function(){
  checkbox_crear_alquiler(checkbox_ABL,input_ABL)
});

checkbox_Pasto.addEventListener('change',function(){
  checkbox_crear_alquiler(checkbox_Pasto,input_Pasto)
});

//JS para checkbox de editar alquiler

const checkbox_agua_editar = document.getElementById('checkbox_agua_editar');
const input_agua_editar = document.getElementById('id_Precio_Agua_editar');
const checkbox_ABL_editar = document.getElementById('checkbox_ABL_editar');
const input_ABL_editar = document.getElementById('id_Precio_ABL_editar');
const checkbox_Pasto_editar = document.getElementById('checkbox_Pasto_editar');
const input_Pasto_editar = document.getElementById('id_Precio_Pasto_editar');

const input_invisible_agua = document.getElementById('input_invisible_agua');
const input_invisible_Pasto = document.getElementById('input_invisible_Pasto');
const input_invisible_ABL = document.getElementById('input_invisible_ABL');

function actualizarCheckbox(checkbox,input) {
  if (input.value !== '0') {
    
    input.removeAttribute('disabled')
    checkbox.checked = true;
  } else {
    
    checkbox.checked = false;
    input.value = '';
  }
}
actualizarCheckbox(checkbox_agua_editar,input_agua_editar)
actualizarCheckbox(checkbox_ABL_editar,input_ABL_editar)
actualizarCheckbox(checkbox_Pasto_editar,input_Pasto_editar)


checkbox_agua_editar.addEventListener('change',function(){
  checkbox_crear_alquiler(checkbox_agua_editar,input_agua_editar);
  checkbox_editar_alquiler(checkbox_agua_editar,input_agua_editar,input_invisible_agua);
});
checkbox_Pasto_editar.addEventListener('change',function(){
  checkbox_crear_alquiler(checkbox_Pasto_editar,input_Pasto_editar);
  checkbox_editar_alquiler(checkbox_Pasto_editar,input_Pasto_editar,input_invisible_Pasto);
});
checkbox_ABL_editar.addEventListener('change',function(){
  checkbox_crear_alquiler(checkbox_ABL_editar,input_ABL_editar);
  checkbox_editar_alquiler(checkbox_ABL_editar,input_ABL_editar,input_invisible_ABL);
});


function checkbox_editar_alquiler(checkbox,input,input_invisible){
  if (!checkbox.checked){
    input.setAttribute('disabled','disabled');
    input_invisible.removeAttribute('disabled');
  } else {
    input_invisible.setAttribute('disabled','disabled');
  }
}
