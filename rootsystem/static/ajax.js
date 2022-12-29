

function cargar(recurso, value){
    var xmlhttp;
    var layer;
    var cantidad = value;
    xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function(){
        respuesta = xmlhttp.readyState;
        estado = xmlhttp.status;
        if (respuesta == 4 && estado == 200){
            layer = document.getElementById('respuesta');
            layer.innerHTML = xmlhttp.responseText;
            // document.getElementById('titulo').innerHTML = titulo;
            // console.log(v)
        } else {
            document.getElementById('respuesta').innerHTML = "Cargando ...";
        }
    }
    xmlhttp.open("GET", recurso+cantidad, true);
    xmlhttp.send();
}
