## Cuestiones de Repaso

### 18.1 - Razones para usar fragmentación y reensamblado

- **Limitación de tamaño de las redes:** Algunas redes solo aceptan bloques de datos hasta cierto tamaño, por lo que es necesario dividir los datos grandes en fragmentos más pequeños para poder transmitirlos. 
- **Mayor eficiencia en el control de errores:** Con unidades de datos más pequeñas, si ocurre un error, se retransmite una menor cantidad de bits, lo que mejora la eficiencia del sistema. 
- **Menor requerimiento de memoria en los receptores:** Los dispositivos receptores pueden trabajar con buffers más pequeños al manejar fragmentos en lugar de bloques grandes. 
- **Facilitar controles intermedios y recuperación:** Permite que durante la transferencia se puedan realizar verificaciones, reinicios o mecanismos de recuperación en puntos intermedios. 

### 18.2 - Enumere los requisitos de un mecanismo de interconexión de redes.

1. Proporcionar un enlace entre redes, debe existir al menos una conexión física y control del enlace que permita interconectar las redes. 

2. Proporcionar el encaminamiento y entrega de los datos entre procesos en diferentes redes.

3. Proporcionar un servicio de contabilidad que realice un seguimiento de la utilización de las diferentes redes y dispositivos de encaminamiento y mantenga información de estado. 

4. Proporcionar los servicios mencionados de forma que no se requiera la modificación de la arquitectura de red de cualquiera de las redes interconectadas. Algunas de estas diferencias son:
   * Diferentes esquemas de direccionamiento.
   * Diferentes tamaños máximos de paquete.
   * Diferentes mecanismos de acceso a la red.
   * Diferentes capacidades de recuperación de errores.
   * Diferentes formas de reportar estado y rendimiento.
   * Diferentes técnicas de encaminamiento.
   * Diferencias entre servicios orientados a conexión y no orientados a conexión. 

### 18.3 - ¿Cuáles son los pros y los contras de limitar el reensamblado a los sistemas finales en lugar de permitirlo en los dispositivos de encaminamiento?

**Ventajas de reensamblar solo en los sistemas finales**
- Los routers no necesitan implementar lógica de reensamblado ni gestionar estados complejos.
- Se evita la necesidad de grandes buffers para almacenar fragmentos parciales.
- No es necesario que todos los fragmentos sigan la misma ruta ni pasen por el mismo dispositivo intermedio.

**Desventajas de reensamblar solo en los sistemas finales**
- Los fragmentos pueden seguir dividiéndose a lo largo del camino, lo que reduce la eficiencia global.
- El sistema final debe encargarse completamente del reensamblado.
- Al no recomponerse en el camino, aumenta la cantidad de fragmentos circulando, lo que puede impactar en el rendimiento.

### 18.4 - Explique la función de los tres indicadores en la cabecera de IPv4.

- *1. El bit de «no fragmentación»* prohíbe la fragmentación cuando es 1.

- *2. El bit de «más datos»* se utiliza para la fragmentación y el reensamblado.

- *3. Tercer bit (Reservado)* no está definido para uso actual.

### 18.5 - ¿Cómo se calcula la suma de comprobación de la cabecera de IPv4?

Ya que algunos campos de la cabecera pueden cambiar durante el viaje, este valor se verifica y recalcula en cada dispositivo de encaminamiento. 
El campo suma de comprobación es el complemento a uno de la suma complemento a uno de todas las palabras de 16 bits en la cabecera. 
Por motivos de cálculo, este campo se inicializa a sí mismo a un valorde todo cero.

### 18.6 - ¿Qué diferencia existe entre los campos clase de tráfico y etiqueta de flujo en la cabecera de IPv6?

**Clase de tráfico (8 bits):** Disponible para su uso por el nodo origen y/o los dispositivos de encaminamiento para identificar y distinguir entre clases o prioridades de paquete IPv6.
Es un campo orientado a política de tratamiento por paquete.

**Etiqueta de flujo (20 bits):** Se puede utilizar por un computador para etiquetar aquellos paquetes para los que requiere un tratamiento especial en los dispositivos de encaminamiento
dentro de la red.
Es un campo orientado a identificar y agrupar paquetes de una misma comunicación.

### 18.7 - Explique brevemente los tres tipos de direcciones IPv6.

- **Unidifusión (unicast):** Un paquete enviado a una dirección de este tipo se entrega a la interfaz identificada por esa dirección. Representa comunicación uno a uno.
- **Monodifusión (anycast):** Un paquete enviado a una dirección monodifusión se entrega a una de las interfaces identificadas por esa dirección la más cercana, de acuerdo a la medida de distancia de los protocolos de encaminamiento. Representa comunicación uno al más cercano de varios.
- **Multidifusión (multicast):** Un paquete enviado a una dirección multidifusión se en trega a todas las interfaces identificadas por esa dirección. Representa comunicación uno a muchos.

### 18.8 - ¿Cuál es el propósito de cada uno de los tipos de cabeceras presentes en IPv6?

**Opciones salto a salto:** transporta información que debe ser examinada por cada dispositivo de encaminamiento a lo largo de la ruta, no solo en el destino.

**Encaminamiento:** permite al nodo origen especificar una lista de nodos intermedios por los que debe pasar obligatoriamente el paquete en su camino al destino, funcionando de manera similar al encaminamiento en el origen de IPv4.

**Fragmentación:** contiene la información necesaria para fragmentar y reensamblar paquetes.

**Opciones para el destino:** lleva información opcional que solo necesita ser examinada por el nodo destino final del paquete.

| Cabecera            | Quién la procesa    | Función            |
| ------------------- | ------------------- | ------------------ |
| Opciones salto a salto   | Todos los routers   | Opciones por salto |
| Encaminamiento           | Routers específicos | Ruta explícita     |
| Fragmentacion            | Origen/Destino      | Fragmentación      |
| Opciones para el destino | Destino             | Opciones finales   |

## EJERCICIOS

### 18.1

La primitiva **Send** actúa como la interfaz entre el nivel de Transporte y el nivel de Red en el origen, mientras que **Deliver** representa el paso de los datos del nivel de Red al de Transporte en el destino.

| Parámetro | Competencia de la entidad IP en... | Justificación |
| :--- | :--- | :--- |
| **Identificador (ID)** | Origen y Destino | El **Origen** lo asigna para identificar fragmentos de un mismo datagrama. El **Destino** lo usa para el reensamblado. Los routers intermedios solo lo copian. |
| **Indicador DF (Don't Fragment)** | Origen y Routers intermedios | El **Origen** lo setea según la necesidad de la aplicación. Los **Routers** deben obedecerlo: si el paquete es muy grande y DF=1, deben descartarlo y enviar un error ICMP. |
| **Tiempo de Vida (TTL)** | Origen, Routers y Destino | El **Origen** fija el valor inicial. Cada **Router** debe decrementarlo en 1. El **Destino** verifica que no haya llegado a 0. |

**¿Por qué no están presentes en la primitiva Deliver?**
Esto se debe a que, una vez que la entidad IP en el destino ha reensamblado el datagrama y verificado su integridad, esa información de "control de tráfico" (ID, fragmentación, TTL) pierde relevancia para la capa de Transporte (TCP/UDP). Estas capas superiores solo requieren recibir los datos de usuario puros y validados.

### 18.2

En el protocolo IP, la información suplementaria se refiere principalmente al campo de Opciones. Aunque la cabecera base es fija (20 bytes), el campo de opciones permite funciones adicionales que no siempre son necesarias, como:

- Security: Clasificación de seguridad del paquete.
- Source Routing: Especificar la ruta exacta que debe seguir el paquete.
- Route Recording: Registrar las direcciones IP de los routers por los que pasa.
- Timestamping: Registrar la hora en que el paquete pasa por cada nodo.

### 18.3

Normalmente, el router decide el camino basándose en sus tablas. Sin embargo, el Source Routing (donde el origen dicta la ruta) es útil en:

1. Diagnóstico y pruebas de red: Para forzar a un paquete a pasar por un enlace específico y verificar si está fallando.
2. Seguridad: Obligar al tráfico a pasar por un nodo de inspección o Firewall específico antes de llegar al destino.
3. Evitar nodos congestionados: Si el emisor sabe que un nodo intermedio está saturado, puede definir una ruta alternativa manualmente.
4. Redes con políticas específicas: Evitar pasar por la infraestructura de ciertos países o proveedores por razones legales o de privacidad.

### 18.5

Datos iniciales:

Datagrama total: 4.480 octetos (incluye 20 de cabecera)

Carga útil total (Data): 4.480 - 20 = 4.460 octetos

MTU Ethernet: 1.500 octetos

Carga útil máxima por fragmento: 1.500 - 20 = 1.480 octetos

| Fragmento | Longitud Total (Bytes) | Indicador MF (More Fragments) | Desplazamiento (Offset) |
| :--- | :---: | :---: | :---: |
| **1** | 1.500 | 1 | 0 |
| **2** | 1.500 | 1 | 185 |
| **3** | 1.500 | 1 | 370 |
| **4** | 40 | 0 | 555 |

Cálculo del último fragmento: 

Data restante = 4.460 - (1.480 x 3) = 4.460 - 4.440 = 20 octetos

Longitud total = 20 (data) + 20 (cabecera) = 40 octetos

Offset = (1.480 x 3) / 8 = 555

