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



const checkbox_agua = document.getElementById('checkbox_agua');
const input_Agua = document.getElementById('id_Precio_Agua');
const div_agua = document.getElementById('div-agua');

checkbox_agua.addEventListener('change', function() {
  if (checkbox_agua.checked) {
    input_Agua.removeAttribute('disabled');
  } else {
    input_Agua.setAttribute('disabled','disabled');
    input_Agua.value ='';
  }
});

const checkbox_ABL = document.getElementById('checkbox_ABL');
const input_ABL = document.getElementById('id_Precio_ABL');

checkbox_ABL.addEventListener('change',function(){
  if (checkbox_ABL.checked){
    input_ABL.removeAttribute('disabled');
  } else {
    input_ABL.setAttribute('disabled','disabled');
    input_ABL.value = '';
  }
});

const checkbox_Pasto = document.getElementById('checkbox_Pasto');
const input_Pasto = document.getElementById('id_Precio_Pasto');

checkbox_Pasto.addEventListener('change',function(){
  if (checkbox_Pasto.checked){
    input_Pasto.removeAttribute('disabled');
  }else {
    input_Pasto.setAttribute('disabled','disabled')
    input_Pasto.value = '';

  }
});