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

> En la discusión sobre IP, se mencionó que el identificador, el indicador de no fragmentar y el tiempo de vida se hallan presentes en la primitiva Send pero no en la primitiva Deliver, ya que esos parámetros no son competencia de IP. Indique, para cada una de estas primitivas, si es competencia de la entidad IP en el origen, de la entidad IP en cada dispositivo de encaminamiento intermedio o de la entidad IP en el sistema final destino. Justifique su respuesta.

La primitiva **Send** actúa como la interfaz entre el nivel de Transporte y el nivel de Red en el origen, mientras que **Deliver** representa el paso de los datos del nivel de Red al de Transporte en el destino.

| Parámetro | Competencia de la entidad IP en... | Justificación |
| :--- | :--- | :--- |
| **Identificador (ID)** | Origen y Destino | El **Origen** lo asigna para identificar fragmentos de un mismo datagrama. El **Destino** lo usa para el reensamblado. Los routers intermedios solo lo copian. |
| **Indicador DF (Don't Fragment)** | Origen y Routers intermedios | El **Origen** lo setea según la necesidad de la aplicación. Los **Routers** deben obedecerlo: si el paquete es muy grande y DF=1, deben descartarlo y enviar un error ICMP. |
| **Tiempo de Vida (TTL)** | Origen, Routers y Destino | El **Origen** fija el valor inicial. Cada **Router** debe decrementarlo en 1. El **Destino** verifica que no haya llegado a 0. |

**¿Por qué no están presentes en la primitiva Deliver?**
Esto se debe a que, una vez que la entidad IP en el destino ha reensamblado el datagrama y verificado su integridad, esa información de "control de tráfico" (ID, fragmentación, TTL) pierde relevancia para la capa de Transporte (TCP/UDP). Estas capas superiores solo requieren recibir los datos de usuario puros y validados.

### 18.2

> ¿Cuál es la información suplementaria de la cabecera en el protocolo IP?

En el protocolo IP, la información suplementaria se refiere principalmente al campo de Opciones. Aunque la cabecera base es fija (20 bytes), el campo de opciones permite funciones adicionales que no siempre son necesarias, como:

- Security: Clasificación de seguridad del paquete.
- Source Routing: Especificar la ruta exacta que debe seguir el paquete.
- Route Recording: Registrar las direcciones IP de los routers por los que pasa.
- Timestamping: Registrar la hora en que el paquete pasa por cada nodo.

### 18.3

> Describa algunas circunstancias en las que sería deseable utilizar encaminamiento en el origen en lugar de dejar a los dispositivos de encaminamiento que realicen la decisión de encaminamiento.

Normalmente, el router decide el camino basándose en sus tablas. Sin embargo, el Source Routing (donde el origen dicta la ruta) es útil en:

1. Diagnóstico y pruebas de red: Para forzar a un paquete a pasar por un enlace específico y verificar si está fallando.
2. Seguridad: Obligar al tráfico a pasar por un nodo de inspección o Firewall específico antes de llegar al destino.
3. Evitar nodos congestionados: Si el emisor sabe que un nodo intermedio está saturado, puede definir una ruta alternativa manualmente.
4. Redes con políticas específicas: Evitar pasar por la infraestructura de ciertos países o proveedores por razones legales o de privacidad.

### 18.5

> Un datagrama de 4.480 octetos se va a transmitir y se necesita fragmentar ya que va a pasar por una red Ethernet con un campo máximo de carga útil de 1.500 octetos. Muestre los valores de los campos longitud total, indicador de más segmentos y desplazamiento de fragmento en cada uno de los fragmentos resultantes.

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

### 18.7

> Se va a segmentar un datagrama. ¿Qué opciones del campo de opción se necesitan copiar en la cabecera de cada fragmento y cuáles se necesitan copiar sólo en el primer fragmento? Justifique el tratamiento de cada opción.

En el protocolo IPv4, cuando un datagrama debe ser fragmentado para adaptarse a la MTU de una red, no todas las opciones presentes en la cabecera original se replican en todos los fragmentos. El diseño de IP utiliza un bit específico (el bit de Copiado o Copy flag) en el primer octeto de cada opción para determinar este comportamiento.

#### 1. Opciones que deben copiarse en todos los fragmentos

Estas opciones son críticas para que los routers intermedios traten cada fragmento de manera idéntica y aseguren que lleguen al destino.
- Seguridad: Permite incorporar una etiqueta de seguridad al datagrama. Si un fragmento no tuviera esta etiqueta, un router que aplique políticas de seguridad basadas en el nivel de clasificación de los datos podría descartar los fragmentos "anónimos" o tratarlos de forma incorrecta, impidiendo el reensamblado.
- Source Routing: Especifica la ruta secuencial de routers que debe seguir el paquete. Dado que cada fragmento es una PDU independiente que se encamina por separado en la capa de red , todos deben contener la lista de saltos para poder navegar a través de la red hasta el destino final.

#### 2. Opciones que se copian solamente en el primer fragmento

Estas opciones suelen tener fines de diagnóstico o control y su repetición en cada fragmento generaría una sobrecarga innecesaria (overhead) sin aportar valor al reensamblado.
- Registro de la ruta: Se utiliza para registrar la secuencia de routers visitados. Es suficiente con que el primer fragmento registre el camino para fines de depuración. Registrar la ruta en cada fragmento consumiría espacio valioso en la cabecera de todas las PDU fragmentadas.
- Timestamp: Registra el tiempo en milisegundos al pasar por los routers. Al igual que el registro de ruta, es una herramienta de medición. Repetir esta operación en cada fragmento aumentaría el tiempo de procesamiento en los routers y la latencia total sin beneficio para la entrega de los datos originales.

### 18.8

> Un mensaje de la capa de transporte, que contiene 1.500 bits de datos y 160 bits de cabecera, se envía a la capa internet, la cual incorpora otros 160 bits de cabecera. El resultado se transmite a través de dos redes que utilizan cada una 24 bits de cabecera de paquete. La red destino tiene un tamaño de paquete máximo de 800 bits. ¿Cuántos bits, incluyendo cabeceras, se entregan al protocolo de la capa de red en el destino?

#### Datos Iniciales

- Mensaje de transporte ($M_T$): 1500 bits (datos) + 160 bits (cabecera de transporte) = 1660 bits
- Datagrama Original ($D_{IP}$): 1600 bits + 160 bits (cabecera IP) = 1820 bits
- Restricciones de la red de destino:
  - MTU: 800 bits
  - Cabecera de Red (H_{net}): 24 bits

#### Restricciones de Fragmentación e IP

Para que el datagrama atraviese la red destino, el paquete total (incluyendo la cabecera de red) no debe superar los 800 bits.

1. Espacio disponible para la PDU de IP: $MTU - H_{net} = 800 - 24 = $ 776 bits
2. Espacio para Payload: como cada fragmento requiere de su propia cabecera IP de 160 bits, el espacio es $776 - 160 = $ 616 bits
3. Regla de los 64 bits: en IPv4, la carga util de cada fragmento (excepto el ultimo) debe ser un multiplo de 8 octetos (64 bits) para poder representarse correctamente en el campo Fragment Offset
   - Carga maxima alineada (se hace ajuste por truncamiento): $\lfloor \frac{616}{64} \rfloor \times 64 = $ 576 bits

#### Desglose de Fragmentos y Composicion

El payload original de la capa de transporte (1660 bits) se divide en fragmentos de maximo 576 bits:

| Fragmento | Carga Útil (Transporte) | Cabecera IP | Cabecera Red | Total Bits |
| :--- | :---: | :---: | :---: | :---: |
| **Fragmento 1** | 576 bits | 160 bits | 24 bits | 760 bits |
| **Fragmento 2** | 576 bits | 160 bits | 24 bits | 760 bits |
| **Fragmento 3** | 508 bits (1660 - 1152) | 160 bits | 24 bits | 692 bits |

#### Bits Totales Entregados

La cantidad total de bits que se entregan al protocolo de red en el destino es la suma de todos los fragmentos transmitidos a través de la interfaz física para completar el mensaje original:

$$Total = 760 + 760 + 692 = 2212 \text{ bits}$$

Este incremento (de 1820 a 2212 bits) representa la overhead introducida por la duplicación de cabeceras IP y la adición de cabeceras de red necesarias para gestionar la fragmentación en el camino.

### 18.11

> Compare los campos individuales de la cabecera IPv4 con los de la cabecera IPv6. Compare las posibilidades proporcionadas por cada uno de los campos de IPv4 con los de IPv6.

| Campo IPv4 | Campo IPv6 | Estado | Justificación y Cambios Funcionales |
| :--- | :---: | :---: | :--- |
| **Versión** | **Versión** | Igual | Se mantiene para identificar la versión del protocolo; el valor cambia de 4 a 6. |
| **IHL** | --- | **Eliminado** | La cabecera IPv6 es de longitud fija (40 octetos), eliminando la necesidad de este campo. |
| **Tipo de Servicio (TOS)** | **Clase de Tráfico** | **Renombrado** | Se utiliza para identificar prioridades y clases de paquetes; incluye campos DS y ECN. |
| **Longitud Total** | **Longitud de Carga Útil** | **Modificado** | IPv4 mide cabecera + datos. IPv6 mide solo las cabeceras de extensión y la PDU de transporte. |
| **Identificación** | --- | **Eliminado*** | Se movió a la "Cabecera de Fragmentación" opcional. Solo se usa si hay fragmentación. |
| **Indicadores (Flags)** | --- | **Eliminado*** | Se movieron a la "Cabecera de Fragmentación". |
| **Desplazamiento** | --- | **Eliminado*** | Se movió a la "Cabecera de Fragmentación". |
| **Tiempo de Vida (TTL)** | **Límite de Saltos** | **Renombrado** | Simplificación funcional; se trata estrictamente como un contador de saltos. |
| **Protocolo** | **Cabecera Siguiente** | **Modificado** | Identifica el protocolo superior o la primera cabecera de extensión de IPv6. |
| **Suma de Comprobación** | --- | **Eliminado** | Se eliminó para agilizar el encaminamiento, confiando en las capas de enlace y transporte. |
| **Dirección Origen** | **Dirección Origen** | **Modificado** | Se expande de 32 bits a 128 bits. |
| **Dirección Destino** | **Dirección Destino** | **Modificado** | Se expande de 32 bits a 128 bits. |
| **Opciones** | --- | **Eliminado** | Se reemplazaron por "Cabeceras de Extensión" que se procesan solo en los extremos. |
| --- | **Etiqueta de Flujo** | **Nuevo** | Identifica paquetes que requieren tratamiento especial por flujos específicos (ej. tiempo real). |

La cabecera de IPv6 posee una longitud fija de 40 octetos, el doble que la parte obligatoria de IPv4, pero contiene menos campos (8 frente a 12). Esta aparente contradicción se explica por la expansión de las direcciones: mientras que en IPv4 las direcciones ocupan el 40% de la cabecera (8 de 20 octetos), en IPv6 ocupan el 80% (32 de 40 octetos). Esto tiene el siguiente impacto:

1. Longitud Fija y Alineación: Al ser siempre de 40 octetos, los routers no necesitan calcular dónde terminan las opciones y empiezan los datos en cada salto. Esto permite que el hardware (ASICs) procese los paquetes de forma paralela y predecible.
2. Eliminación de la Suma de Comprobación: En IPv4, cada router debe recalcular el checksum porque el campo TTL cambia. IPv6 elimina este proceso, reduciendo drásticamente la carga de CPU en los dispositivos intermedios.
3. Procesamiento de Opciones: Las cabeceras de extensión (excepto la hop by hop) no son examinadas por los routers intermedios. Esto evita el análisis detallado de la PDU en el núcleo de la red, acelerando el tránsito del paquete hacia el destino.
4. Fragmentación en el Origen: IPv6 prohíbe que los routers fragmenten paquetes; es responsabilidad del sistema origen conocer la MTU de la ruta. Esto elimina una de las tareas más costosas computacionalmente para un router.

### 18.12

> Justifique el orden recomendado de las cabeceras de extensión de IPv6 (por ejemplo, ¿por qué va
primero la cabecera de opciones salto-a-salto?, ¿por qué la cabecera de encaminamiento está antes que la
cabecera de fragmentación?, y así hasta la cabecera final).

En IPv6, a diferencia de IPv4, las opciones adicionales de cabeceras no van dentro de la cabecera principal sino en "cabeceras de extensión", las cuales se encadenan una tras otra. En este contexto, existe un orden jerárquico en el cual deben colocarse dichas cabeceras. Este orden existe con el objetivo de que los nodos intermedios o routers trabajen lo menos posible en el proceso de envio de datos y para que las funciones se apliquen en la secuencia lógica correcta. El orden es el siguiente:

1. Opciones salto a salto: Va siempre en primer lugar después de la cabecera IPv6 porque es la única que todos los dispositivos de encaminamiento deben examinar y procesar. Permite que el router la identifique de inmediato.
2. Cabecera de encaminamiento: Esta es la segunda cabecera y va previa a la cabecera de fragmentación porque el encaminamiento determina la ruta y los nodos intermedios por los que pasará el paquete.
3. Cabecera de fragmentación: Está en tercer lugar ya que, luego de saber por qué nodos intermedios pasa la ruta, el nodo de origen se fragmenta. El nodo destino usa esta cabecera para reensamblar el paquete.
4. Cabecera de seguridad: Protege el contenido reensamblado o valida la integridad de lo que realmente llega al destino.
5. Cabeceras de destino: Contienen información que solo debe ser examinada por el nodo de destino final.

### 18.16

> Las especificaciones originales de IPv6 combinaban los campos de etiqueta de flujo y prioridad en un solo
campo de etiqueta de flujo de 28 bits. Esto permitía a los flujos redefinir la interpretación de los diferentes
valores de prioridad. Sugiera una razón por la que la especificación final incluye un campo de prioridad en un
campo distinto.

En un principio las combinaciones originales de IPv6 combinaban campos de etiqueta de flujo y prioridad en un solo campo de etiqueta de 28 bits, pero actualmente estos campos se separan. Esto se definió por razones de flexibilidad y eficiencia en la gestión de tráfico, en donde podemos destacar lo siguiente:

1. Hay paquetes sin flujo, los cuales si bien no pertenecen a un flujo específico, siguen necesitando una prioridad. Si las etiquetas de flujo y prioridad estuvieran juntas, se requeriria generar nuevos flujos para estos casos.
2. Un router puede leer los 8 bits de prioridad de forma estándar para poder decidir qué paquete enviar primero en caso de que haya congestión, sin tener que leer los 20 bits de etiqueta de flujo, logrando asi una mejora en la velocidad.
3. Tener estas etiquetas separadas permite que la red gestione la calidad del servicio de forma global (etiqueta de prioridad), y por otro lado la etiqueta de flujo se usa para tratamientos más personalizados.

### 18.17

> Para el encaminamiento IPv6 tipo 0, especifique el algoritmo para actualizar las cabeceras IPv6 y de
encaminamiento en los nodos intermedios.

Cuando un paquete con encamintamiento IPv6 tipo 0 llega a un nodo intermedio, se sigue el siguiente algoritmo:

1. Verificación de segmentos restantes: El nodo examina el campo de "Segmentos restantes" en la cabecera de encaminamiento. Si es 0, el nodo no vuelve a procesar la cabecera.
2. Actualización de dirección de destino: Si aún quedan segmentos restantes, el nodo decrementa en 1 el valor del campo, luego busca en la lista de direcciones de la cabecera de encaminamiento la siguiente dirección a visitar y por último intercambia la dirección de destino de la cabecera IPv6 con la dirección obtenida de la lista.
3. Reenvío: El paquete se reenvía hacia la nueva dirección de destino colodada en la cabecera principal.

El proceso se repite hasta que el paquete llegue al destino final.
