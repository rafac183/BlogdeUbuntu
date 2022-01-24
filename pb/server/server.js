var cafecito = require("express"); //require(la trae como una funcion) busca las librerias instaladas en tu compu y las trae y las guarda en la variable
var aplicacion = cafecito(); //exp==traigo todas las librerias y las meto en expres, luego esa funcion la coloco en una variable

aplicacion.get("/", inicio);
aplicacion.get("/git", cursos);

function inicio(resultado)
{
  resultado.send("Este es el <strong>home</strong> genial!!");
}

function cursos(resultado)
{
  resultado.send("Estos son los <strong>cursos</strong>");
}

aplicacion.listen(8989);

// platzi.com/js