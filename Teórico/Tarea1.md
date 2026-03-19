# Trabajo Practico N1

- **Gastón E. Capdevila**
- **Nicolas Seia**
- **Ignacio Ledesma**
- **Tomas Viberti**  
 
## Ensalada WANdorf 2.0

**Facultad de ciencias Exactas Fisicas y Naturales**  

**Redes de Computadoras**

**Profesores:**
- SANTIAGO MARTIN HENN
- OLIVA CUNEO FACUNDO NICOLAS 

**16/3/2026**   

---

### Información de los autores
 
- gaston.capdevila@mi.unc.edu.ar
- nicolas.seia@unc.edu.ar
- iledesma@mi.unc.edu.ar
- tomas.viberti@mi.unc.edu.ar

## Desarrollo 

### 1) ¿Cuál es la función principal de la capa de acceso a la red?

 La capa de acceso a la red está vinculada al intercambio de datos entre la computadora y la red a la que está conectada. La computadora emisora debe proporcionarle a la red la dirección de destino a la que pretende enviar datos. Sabiendo esto, la función que cumple la capa de red es la de encaminar los datos que se transmiten al destino apropiado. La computadora emisora utiliza los servicios de la capa de acceso a la red, por ejemplo la gestión de prioridades.

### 2) ¿Qué tareas realiza la capa de transporte?

 La capa de transporte se encarga de proveer confiabilidad y seguridad durante el intercambio de datos, es decir, asegura que los datos lleguen de manera correcta a destino y en el mismo orden en el que fueron enviados por el emisor. 

### 3) ¿Qué es un protocolo?

 Un protocolo es una serie de reglas o convenciones necesarias para que haya comunicación entre dos entidades. Dicha comunicación, la cual está dividida en capas o pares, se logra haciendo que las mismas intercambien información. Dichas capas pares deben seguir el protocolo al momento de intercambiar datos.
 Un protocolo está caracterizado por:
 - La sintaxis: establece el formato de los bloques de datos.
 - La semántica: incluye información de control para la coordinación y gestión de errores.
 - La temporización: considera aspectos relativos a la sintonización de velocidades y secuenciación.

 ### 4) ¿Qué es una unidad de datos del protocolo (PDU)?

 Cuando una aplicación genera datos estos no se envian de la manera en que se generaron, sino que cada capa por la que dicho dato viaja le agrega información de control al mismo. Este dato con información de control agregada por cada capa es lo que llamamos unidad de datos del protocolo. Específicamente es la unión de los datos generados por la capa superior, junto con la información de control de la capa actual. Entonces dependiendo de la capa actual en donde de encuentre un dato, podemos denominar al PDU de cada una, por ejemplo, PDU de transporte. 

 ### 5) ¿Qué es una arquitectura de protocolos?

 Al momento de transferir datos se trabaja con módulos. Cada módulo tiene su propia función durante la transmisión, pero todos deben funcionar cohesivamente para lograr que el envío de datos sea fiable y seguro. Trabajando de esta manera nos aseguramos que en caso de necesitar cambios en cierto momento de la transmisión solo haya que modificar el módulo que se encarga de dicha tarea, sin afectar a los demás. En este contexto podemos definir a la arquitectura de protocolos como la estructura consistente en un conjunto de módulos que realizarán todas las funciones.

### 6) ¿Qué es TCP/IP?

TCP/IP es el tipo de arquitectura de protocolo más usada en la actualidad. Esta arquitectura divide el problema de la comunicación en cinco etapas relativamente independientes entre sí:
- Capa física
- Capa de acceso a la red
- Capa de internet
- Capa extremo a extremo o de transporte
- Capa de aplicación.

### 7) ¿Qué ventajas aporta una arquitectura en capas como la usada en TCP/IP?

Las ventajas que podemos mencionar sobre las arquitecturas de capas son:
- Modularidad y División de Tareas: El problema de la comunicación es demasiado complejo para un solo módulo. Al dividirlo, cada capa se encarga de un subconjunto de tareas relacionadas
- Independencia y Abstracción: Los cambios en una capa no deberían obligar a cambiar las demás.
- Servicios y Primitivas: Cada capa N ofrece un conjunto de servicios a la capa superior (N+1). 
- Encapsulamiento y PDUs: Permite que cada nivel añada su propia información de control a los datos sin que las capas inferiores necesiten entender el contenido de las capas superiores. 
- Facilidad para la Normalización: Al tener límites bien definidos, los fabricantes pueden desarrollar estándares para una capa específica de forma independiente y simultánea, lo que acelera la innovación tecnológica.

### 8) ¿Qué es un encaminador?

Un encaminador es un procesador que conecta dos redes y cuya funcion principal es retransmitir datos desde una red a otra siguiendo la ruta adecuada para alcanzar al destino.

---

## Ejercicios

### 2.1)

### 2.2)

### 2.3)

### 2.4)

### 2.5)

En teoría, no seria necesaria, ya que en una red de difusión pura (como un viejo concentrador/hub o un solo segmento de Wi-Fi), todas las estaciones "escuchan" todo. Si la Estación A quiere hablar con la B, solo necesita la dirección física (MAC) de B. El nivel de enlace (Capa 2) es suficiente para que B reconozca que el paquete es para ella y lo procese.

Pero en la práctica, si es necesaria porque nos brinda lo siguiente:
1.  Escalabilidad: Sin Capa 3, no podrías dividir la red en subredes. Te quedarías atrapado en un dominio de colisión/difusión gigante donde el tráfico de control (como el protocolo ARP) saturaría la red.
2.  Interconexión: Si quieres salir de esa red de difusión (ir a Internet, por ejemplo), necesitas una dirección lógica (IP) para que los enrutadores sepan cómo llegar a otros destinos que no están en tu cable o señal de aire.
3.  Independencia del hardware: La Capa 3 permite que las aplicaciones usen direcciones IP, sin importar si abajo hay Ethernet, Fibra Óptica o Wi-Fi.

### 2.6)

#### a) 

Arquitectura de 8 capas (Enfoque en Usuario)

En este modelo, dividimos la capa de aplicación para separar la lógica del negocio de la interfaz visual.

1. Física: Transmisión de bits.
2. Enlace de Datos: Control de errores punto a punto.
3. Red: Enrutamiento y direccionamiento global.
4. Transporte: Confiabilidad extremo a extremo.
5. Sesión: Gestión de diálogos y persistencia.
6. Presentación: Formato de datos (JSON, XML, Cifrado).
7. Lógica de Aplicación: Reglas del sistema (ej. procesar una compra).
8. Interfaz de Usuario (UI): Renderizado y experiencia del usuario.

Ejemplo de uso: Una Plataforma de Streaming de Video (como Netflix). La Capa 7 gestiona tu perfil y recomendaciones, mientras que la Capa 8 es la app que ves en tu TV o teléfono.

#### b) 

Arquitectura de 6 capas (Enfoque en Eficiencia/IoT)

Aquí simplificamos el nivel inferior, fusionando el acceso al medio físico y lógico, común en sistemas integrados.

1. Acceso al Medio (Hardware): Fusión de Física y Enlace.
2. Red: Direccionamiento.
3. Transporte: Transferencia de datos.
4. Gestión de Datos: Fusión de Sesión y Presentación.
5. Servicios: Funciones comunes (autenticación, logs).
6. Aplicación: Función específica del dispositivo.

Ejemplo de uso: Sensores de una Smart City (IoT). Al ser dispositivos con poca potencia, se prefiere una pila más delgada donde la gestión de datos y la sesión se manejan juntas para ahorrar batería y procesamiento.

### 2.7) 

#### a)

No, no es necesario. Cuando la capa $N-1$ recibe una PDU de la capa $N$, la trata como un bloque de datos puros (payload), sin distinguir entre lo que es la cabecera $N$ y los datos de usuario.

- Si la capa $N-1$ decide segmentar esa unidad porque es demasiado grande para su nivel, simplemente divide el bloque completo en trozos.
- La cabecera del nivel $N$ quedará incluida únicamente en el primer segmento del nivel $N-1$.
- Los segmentos restantes solo contendrán las partes subsiguientes de los datos originales. Cada uno de estos segmentos llevará, eso sí, su propia cabecera de nivel $N-1$ para permitir el reensamblado en el destino.

#### b)

Sí, es necesario que cada PDU conserve su propia cabecera.Si decides agrupar varias PDUs del nivel $N$ dentro de una sola PDU del nivel $N-1$, cada una debe mantener su identidad.

- Las cabeceras del nivel $N$ contienen información de control crítica y específica para cada unidad (como números de secuencia, puertos de destino o sumas de comprobación).
- Si se eliminaran las cabeceras individuales para dejar una sola cabecera de nivel $N$ "global", se perdería la capacidad de identificar y procesar correctamente cada mensaje independiente al llegar al receptor. El nivel $N$ en el destino no sabría dónde termina un mensaje y empieza el siguiente, ni a qué proceso específico pertenece cada uno si fueran a puertos distintos.
