
document.addEventListener("DOMContentLoaded", function() {
    const mapElement = document.getElementById('map');
    const apiKey = mapElement.getAttribute('data-key');

    if (apiKey) {
        loadGoogleMaps(apiKey);
    } else {
        console.error('No API key found for Google Maps.');
    }
});

function loadGoogleMaps() {
    const script = document.createElement('script');
    script.src = `https://maps.googleapis.com/maps/api/js?key=${GOOGLE_API_KEY}&callback=initMap`;
    script.defer = true;
    script.async = true;
    document.head.appendChild(script);
}

// function initMap() {
//     const mapElement = document.getElementById('map');
//     const map = new google.maps.Map(mapElement, {
//         zoom: 14,
//         center: { lat: -34.590747, lng: -58.4174746 } // Centro inicial del mapa
//     });

//     // Guarda la referencia del mapa en una variable global si necesitas acceder desde otras funciones
//     window.myMap = map;
// }

function setLocation(coordinates, iftsName) {


    // Cambia la fuente del iframe con las coordenadas seleccionadas
    var iframe = document.getElementById('gmap');
    var gmapSrc = `https://www.google.com/maps/embed/v1/place?key=GOOGLE_API_KEY&q=${coordinates}`;
    
    iframe.src = gmapSrc;
    
    // Mostrar una alerta o log con el nombre de la institución seleccionada (opcional)
    console.log('Mostrando mapa de: ' + iftsName);
    

    // Coordenadas se esperan en el formato "lat,long"
    // var gmap = document.getElementById("gmap");
    // console.log("La clave de la API es: ");
    // console.log(GOOGLE_API_KEY);
    // // Generar nueva URL para el mapa de Google Maps Embed API con las coordenadas
    // var newSrc = `https://www.google.com/maps/embed/v1/view?key=${GOOGLE_API_KEY}&center=${coordinates}&zoom=15`;
    // https://www.google.com/maps/embed/v1/view?key=${GOOGLE_API_KEY}&center=${coordinates}&zoom=15
    
    // // Actualizar el src del iframe para cambiar la ubicación en el mapa
    // gmap.src = newSrc;
}

// function setLocation(coordenadas) {
//     // Separar las coordenadas en latitud y longitud
//     const [latitud, longitud] = coordenadas.split(',');

//     // Convertir las cadenas a números
//     const latitudNum = parseFloat(latitud);
//     const longitudNum = parseFloat(longitud);

//     // Verificar si las conversiones fueron exitosas
//     if (!isNaN(latitudNum) && !isNaN(longitudNum)) {
//         // Centra el mapa en las nuevas coordenadas
//         const map = window.myMap;
//         map.setCenter({ lat: latitudNum, lng: longitudNum });

//         // Opcional: Mostrar marcador en las coordenadas
//         const marker = new google.maps.Marker({
//             position: { lat: latitudNum, lng: longitudNum },
//             map: map,
//             icon: {
//                 url: "http://maps.google.com/mapfiles/ms/icons/red-dot.png" // Establece el icono rojo
//             }
//         });
//     } else {
//         console.error('Error al convertir las coordenadas:', coordenadas);
//     }
// }


// Inicializa el mapa cuando la ventana carga
window.onload = initMap;
