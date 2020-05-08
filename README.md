# Diseño del programa de Serenatas aplicando los principios SOLID

A través de este programa se podrá gestionar los musicos e instrumentos, de manera aleatoria, que podrán asistir a los eventos para los cuales se les contrate. Se tiene en cuenta que cada uno de estos musicos van a tener una disponibilidad condicionada por el desarrollo de sus distintas actividades personales, razón por la cual cada uno de ellos asistira a la serenata si para ese momento estan disponibles. A la llegada de la serenata los instrumentos se podrán afinar y tocar.

### Aplicando los principios SOLID 🔧
---
El desarrollo de este ejercicio tiene como objetivo la aplicación de los principios SOLID (minimo 3), y se encuentra dividido en dos partes, la primera parte que es su diseño y la segunda, que comprende la implementación. De acuerdo a lo anterior, se mostrara en su primera parte la estructura de este desarrollo por medio de su Diagrama de Clases y se ubicara de manera clara donde estan aplicados estos principios. 

### DISEÑO: Diagrama de Clases📋
---

 	
### Ubicación de cada principio📌
---
Se explica donde y como esta aplicado cada uno de los principios SOLID, y se ilustra con el diagrama de clases especifico de donde se evidencia.

#### Principio de Responsabilidad Unica
---
Este principio es el que se refiere a que una clase debe cambiar por una unica razón, para ubicar este principio se debe en primer lugar identificar las responsabilidades que tiene cada clase y pensar en que al momento de la extensión o cambios que se requieran se consiga afectar al menor numero de partes posibles de la aplicación.

En este caso especifico este principio se aplico en la separación entre el estado de la persona y la representación 
#### Principio de Open/Closed
---
Este es el principio que trata sobre como las clases deben estar abiertas a extensiones y cerradas a modificaciones, esto quiere decir, que si requiero agregar una nueva funcionalidad no puedo modificar el codigo pero si lo puedo extender.

En este caso el principio se ubica en la clase Instrumento, cada vez que tenga que agregar otro nuevo tipo de instrumentos, se debe modificar el código y es allí donde aplicamos el principio Open/Closed exactamente cuando yo desee agregar otra funcionalidad, en este caso, otro tipo de instrumentos, no tengo que modificar la clase de Instrumento, porque esta se penso como una clase abstracta que tiene los metodos de tocar y afinar que se utilizan para todos los tipos de instrumentossin que se tenga que tocar la clase Instrumento posteriormente.

#### Principio de Sustitución de Liskov
---

#### Principio de Segregación de Interfaces
---

#### Principio de Inversión de Dependencias
---
Este principio trata acerca de que los modulos de nivel alto no deben depender de modulos de nivel bajo sino de abstracciones, es decir que lo más importante no puede depender de lo menos importante. Si se logra que un modulo no dependa de otro ya lo podre utilizar en otros proyectos

### Autores✒️
---
Angie Alina Estefania Peña Bolivar - 20181020146

### Información Adicional⚙️
---
Se encuentra, por el momento, unicamente el diseño del desarrollo.
