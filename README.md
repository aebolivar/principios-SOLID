# Diseño del programa de Orquesta aplicando los principios SOLID

<p align="center"> <img src="https://github.com/aebolivar/principios-SOLID/blob/master/imagenes%20README/Encabezado.png"> </p> 

A través de este programa se podrá gestionar los musicos e instrumentos, de manera aleatoria, que podrán asistir a los eventos para los cuales se les contrate. Se tiene en cuenta que cada uno de estos musicos van a tener una disponibilidad condicionada por el desarrollo de sus distintas actividades personales, razón por la cual cada uno de ellos asistira a al evento de la orquesta si para ese momento estan disponibles. A la llegada de la orquesta los instrumentos se podrán afinar y tocar.

### Aplicando los principios SOLID 🔧
---

<p align="center"> <img src="https://github.com/aebolivar/principios-SOLID/blob/master/imagenes%20README/SOLID.png"> </p> 

El desarrollo de este ejercicio tiene como objetivo la aplicación de los principios SOLID (minimo 3), y se encuentra dividido en dos partes, la primera parte que es su diseño y la segunda, que comprende la implementación. De acuerdo a lo anterior, se mostrara en su primera parte la estructura de este desarrollo por medio de su Diagrama de Clases y se ubicara de manera clara donde estan aplicados estos principios. 

### DISEÑO: Diagrama de Clases📋
--- 	
![Diagrama de clases: PRU](https://github.com/aebolivar/principios-SOLID/blob/master/Diagrama%20de%20Clases/Diagrama%20de%20Clases.jpg)

### Ubicación de cada principio📌
---
Se explica donde y como esta aplicado cada uno de los principios SOLID, y se ilustra con el diagrama de clases enfocando la parte en donde se evidencia.

#### Principio de Responsabilidad Unica
---
Este principio es el que se refiere a que una clase debe cambiar por una unica razón, para ubicar este principio se debe en primer lugar identificar las responsabilidades que tiene cada clase y pensar en que al momento de la extensión o cambios que se requieran se consiga afectar al menor numero de partes posibles de la aplicación.

En este caso especifico este principio se aplico en la separación entre las clases de cada instrumento y la representación de estos, la clase conserva sus metodos, y la interfaz incluso se puede extende para terminal o navegador para ver la representación del instrumento, para así mostrar como si cambia alguna de las dos clases no va a afectar a la otra, se abran logrado desacoplar.

![Diagrama de clases: PRU](https://github.com/aebolivar/principios-SOLID/blob/master/Diagrama%20de%20Clases/PrincipioResponsabilidadUnica.png)

#### Principio de Open/Closed
---
Este es el principio que trata sobre como las clases deben estar abiertas a extensiones y cerradas a modificaciones, esto quiere decir, que si requiero agregar una nueva funcionalidad no puedo modificar el codigo pero si lo puedo extender.

En este caso el principio se ubica en la clase Instrumento, cada vez que tenga que agregar otro nuevo tipo de instrumentos, se debe modificar el código y es allí donde aplicamos el principio Open/Closed exactamente cuando yo desee agregar otra funcionalidad, en este caso, otro tipo de instrumentos, no tengo que modificar la clase de Instrumento, porque esta se penso como una clase abstracta que tiene los metodos de tocar y afinar que se utilizan para todos los tipos de instrumentos sin que se tenga que tocar la clase Instrumento posteriormente.

![Diagrama de clases: PRU](https://github.com/aebolivar/principios-SOLID/blob/master/Diagrama%20de%20Clases/PrincipioOpenClosed.png)

#### Principio de Sustitución de Liskov
---
Este principio se basa en asegurarnos de que cuando extendemos una clase, no estamos alterando el comportamiento de la clase principal, en lo práctico el principio expone como si se tiene una clase base que tiene una clase derivada y esta última se sustituye y el programa sigue funcionando, entonces la clase derivada es una subtipo de la clase base, y se cumple con lo que se enuncia inicialmente.

![Diagrama de clases: PRU](https://github.com/aebolivar/principios-SOLID/blob/master/Diagrama%20de%20Clases/PrincipioSustitucionLiskov.png)

#### Principio de Segregación de Interfaces
---
En este caso este principio se enfoco en la clase Musico y se analizo como esta tenía metodos que no iba a implementar en todos los casos, y contrario a solucionarlo con un metodo vacío o una expeción, se debe tener como guia este principio que nos habla acerca de que las clases no deben depender de interfaces que no se vayan a utilizar, para este caso se tomo la interfaz que tenia dos metodos y se dividio en dos interfaces, esto permite que las interfaces se usen por completo, esto se hizo de esta forma para visualizar ell principio a pequeña escala pero ya en una situación más compleja la solución no es tan sencilla y se puede solucionar con un patron de diseño.

![Diagrama de clases: PRU](https://github.com/aebolivar/principios-SOLID/blob/master/Diagrama%20de%20Clases/PrincipioSegregaci%C3%B3nInterfaces.png)

#### Principio de Inversión de Dependencias
---
Este principio trata acerca de que los modulos de nivel alto no deben depender de modulos de nivel bajo sino de abstracciones, es decir que lo más importante no puede depender de lo menos importante, y esto se puede lograr por medio de abstracciones. Una de las ventajas de este principio es que si se logra que un modulo no dependa de otro se podra utilizar en otros proyectos.

En este caso este principio se evidencia en la creación de la clase Instrumento donde se encuentran dos metodos, afinar y tocar, y si estos se crean en una interfaz que sea funcionesInstrumento y por medio de una inyección de dependencias mediante el constructor, es decir, llamar a los metodos de la interfaz desde la clase , se puede observar como puedo cambiar la interfaz sin afectar el comportamiento. 

![Diagrama de clases: PRU](https://github.com/aebolivar/principios-SOLID/blob/master/Diagrama%20de%20Clases/PrincipioInversi%C3%B3ndeDependencias.png)

### Autores✒️
---
Angie Alina Estefania Peña Bolivar - 20181020146

### Información Adicional⚙️
---
Primera parte: Diseño, que se encuentra en el presente README
Segunda parte: Implementación, que se encuentra en la carpeta "orquesta_final"

### Configuración🛠️
---

<p align="center"> <img src="https://github.com/aebolivar/principios-SOLID/blob/master/imagenes%20README/Python.png" width="200" height="200"/> </p> 
<p align="center"> <img src="https://github.com/aebolivar/principios-SOLID/blob/master/imagenes%20README/Flask.png" width="400" height="200"/> </p> 

Para poder ejecutar el programa correctamente debe tener instalado Flask.
Flask es un MicroFrameWork, un ambiente web.
Para instalar Flask usar el siguiente comando:

![Diagrama de clases](https://github.com/aebolivar/principios-SOLID/blob/master/Diagrama%20de%20Clases/pip.png)

'pip install Flask'

Para mayor información consulte la pagina de Flask: https://flask.palletsprojects.com/en/1.1.x/installation/
OBSERVACIÓN: Si su consola no reconoce 'pip' como un comando seguramente deberá modificar la configuración de 'PATH'.
