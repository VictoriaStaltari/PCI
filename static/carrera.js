// Obtener el nombre de la carrera desde la URL
const path = window.location.pathname; 
// Ejemplo: "/carrera/ingenieria_electronica"
const carrera = path.split("/")[2];
console.log(carrera); // "ingenieria_electronica"


const materias = [
    { nombre: "Matemática", codigo: "MAT101" },
    { nombre: "Física", codigo: "FIS101" }
];

// Crear los checkboxes dinámicamente
const materiasDiv = document.getElementById('materiasDiv');
materias.forEach(materia => {
    const label = document.createElement('label');
    const checkbox = document.createElement('input');
    label.htmlFor = materia.codigo;
    checkbox.type = 'checkbox';
    checkbox.id = materia.codigo;
    checkbox.name = materia.codigo;
    checkbox.classList.add('materia-checkbox');
    label.appendChild(document.createTextNode(materia.nombre));
    materiasDiv.appendChild(label);
    materiasDiv.appendChild(checkbox);
});

// Agregar evento para manejar el envío del formulario
const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
    event.preventDefault();
    const materias_cursadas = Array.from(document.querySelectorAll('.materia-checkbox:checked')).map(checkbox => checkbox.name);
    const cant_materias = document.getElementById('materiasPorCuatrimestre').value

    const data = {
        materias: materias_cursadas,
        cant_materias
    };

    localStorage.setItem('datos_especificos', JSON.stringify(data));

    // Enviar los datos al servidor
    fetch(form.action, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Éxito:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});