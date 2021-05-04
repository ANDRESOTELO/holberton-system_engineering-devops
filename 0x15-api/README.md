# API

## What is an API?
Aplication Programming Interface Un conjunto de reglas que definen como dos aplicaciones interactuan entre si. Es decir quien inicia la comunicación, que mensajes envían, cuales respuestas se esperan, entre otros. 
En la programación orientada a objetos, la API es el conjunto de todos los miembros públicos que ofrece una clase, es decir las propiedades y funcioones que ofrtece a otros objetods para que pyueda usar sus servicios.

No podemos hablar de REST sin hablar de los protocolos HTTP, los cuales son protocolos de transferencia. Un protocolo son un conjunto de reglas que definen como se hace la comunicación entre dos entidades. 

Para ver los encabezados de HTTP de un sitio web en la linea de comandos podemos usar el comando curl -v https://example.com > /dev/null

Que es REST -> Representational State Transfer, es básicamente una pequeña capa de complejidad agregada al HTTP. Es un protocolo de intercamio de recursos. Por tanto una API RESTful es una a API que esta diseñada alrededor de los conceptos de REST.

Una petición REST se basa en: cuales el RECURSO sobre el que quiero realizar una acción y cuál es esa acción que quiero realizar. Una peticion REST completa se basa en una URL y un verbo HTTP(GET, PUT, POST, DELETE). Un recurso puede ser cualquier cosa literalmente. 

El flujo de una petición REST funciona similar a HTTP, pero con ligeras modificaciones. El cliente hace una petición HTTP al servidor, el servidor interpreta la petición y genera la respuesta, en algún momento el servidor se da cuenta que ciertos recursos solicitados no son propios o no viven en su ubicación, sino que tiene que pedirselos a otro servidor, por lo cual genera otra petición HTTP al otro servidor para obtener dicho recurso, el otro servidor genera una respuesta al primer servidor (esta es la petición REST), una vez este primer servidor tiene los datos del otro servidor, continua con su la respuesta de su petición original y se la devuelve al cliente para que éste haga lo que tenga que hacer con ella.

¿Cuándo conviene usar REST?
En interacciones simples
Cuando se tienen recursos limitados (generalmente los de hardware)

¿Cómo se realizan peticiones REST?
El consumo de web services via REST se basa en la utilización de los verbos HTTP. A través de ellos puedo buscar recursos, crear recursos, modificar o borrar recursos. (CRUD)

¿Cómo hacer mis propios servicios REST?
Para ello necesitamos un servidor capaz de interpretar peticiones HTTP y dar respuestas HTTP.
Usualmente estas comunicaciones se realizan por medio de formatos JSON.
La estructura básica seria:
1. Saber que tipo o método de REQUEST recibe el servidor.
2. Si es GET haga esto (por ejemplo codificar en JSON lo que estoy solitando)
3. Si es POST haga esto
4. Si es PUT haga esto
5. Si es DELETE haga esto.

Debemos definir que tipo de recursos queremos exponer o vamos a permitir consumir. Por ejemplo en nuestro servidor tenemos una base de datos de una libreria. 

Para indicar que vamos a usar POST, PUT o PUT usamos la bandera -X de la siguiente manera curl -X 'POST' http://example.com -d {lo que quiero ingresar en formato JSON}