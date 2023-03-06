<?php
require 'vendor/autoload.php';

use \Smalot\PdfParser\Parser;

// Carga PDF
$parser = new Parser();
$pdf = $parser->parseFile('archivo.pdf');

// Extrae el texto.
$texto = $pdf->getText();

// Busca las palabras clave y extrae
$nombre = obtenerNombre($texto);
$apellido = obtenerApellido($texto);
$id = obtenerID($texto);
$puesto = obtenerPuesto($texto);
$fecha = obtenerFecha($texto);
$conclusiones = obtenerConclusiones($texto);

// Formatea la información en JSON
$data = array(
    'nombre' => $nombre,
    'apellido' => $apellido,
    'id' => $id,
    'puesto' => $puesto,
    'fecha' => $fecha,
    'conclusiones' => $conclusiones
);
$json = json_encode($data);

// Funciones para extraer la información
function obtenerNombre($texto) {
    // Obtener el nombre del PDF
    return $nombre;
}

function obtenerApellido($texto) {
    // Obtener el apellido del PDF
    return $apellido;
}

function obtenerID($texto) {
    // Obtener el número de ID del PDF
    return $id;
}

function obtenerPuesto($texto) {
    // Obtener el puesto de trabajo del PDF
    return $puesto;
}

function obtenerFecha($texto) {
    // Obtener la fecha del PDF
    return $fecha;
}

function obtenerConclusiones($texto) {
    // Obtener las conclusiones del PDF
    return $conclusiones;
}

// Devuelve los datos en formato JSON
echo $json;
?>
