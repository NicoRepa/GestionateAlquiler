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

const fechaInput = document.getElementById('id_Fecha_contrato');

    fechaInput.addEventListener('input', function(event) {
        const input = event.target;
        let valor = input.value.replace(/\D/g, ''); // Elimina cualquier carácter que no sea un número

        if (valor.length >= 2 && valor.length < 4) {
            valor = valor.substring(0, 2) + '/' + valor.substring(2);
        } else if (valor.length >= 4) {
            valor = valor.substring(0, 2) + '/' + valor.substring(2, 4) + '/' + valor.substring(4, 8);
        }

        input.value = valor;
});

const checkbox_agua = document.getElementById('checkbox_agua');
const miInput = document.getElementById('id_Precio_Agua');
const div_agua = document.getElementById('div-agua');
const div = document.getElementById('div-invisible');

checkbox_agua.addEventListener('change', function() {
  if (checkbox_agua.checked) {
    div.classList.remove('invisible');
    div_agua.classList.remove('invisible');
  } else if (checkbox_ABL.checked || checkbox_Pasto.checked){
    div_agua.classList.add('invisible');
    miInput.value ='';
  } else {
    div.classList.add('invisible');
    div_agua.classList.add('invisible');
    miInput.value ='';
  }
});

const checkbox_ABL = document.getElementById('checkbox_ABL');
const input_ABL = document.getElementById('id_Precio_ABL');
const div_ABL = document.getElementById('div-ABL');

checkbox_ABL.addEventListener('change',function(){
  if (checkbox_ABL.checked){
    div.classList.remove('invisible');
    div_ABL.classList.remove('invisible');
  } else if (checkbox_agua.checked || checkbox_Pasto.checked){
    div_ABL.classList.add('invisible');
    input_ABL.value ='';
  } else {
    div.classList.add('invisible');
    div_ABL.classList.add('invisible')
    input_ABL.value = '';

  }
});

const checkbox_Pasto = document.getElementById('checkbox_Pasto');
const input_Pasto = document.getElementById('id_Precio_Pasto');
const div_Pasto = document.getElementById('div-Pasto');

checkbox_Pasto.addEventListener('change',function(){
  if (checkbox_Pasto.checked){
    div.classList.remove('invisible');
    div_Pasto.classList.remove('invisible');
  } else if (checkbox_agua.checked || checkbox_ABL.checked){
    div_Pasto.classList.add('invisible');
    input_Pasto.value ='';
  } else {
    div.classList.add('invisible');
    div_Pasto.classList.add('invisible')
    input_Pasto.value = '';

  }
});