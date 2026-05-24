# Trabajo Practico N4

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

**22/04/2026**   

---

### Información de los autores
 
- gaston.capdevila@mi.unc.edu.ar
- nicolas.seia@unc.edu.ar
- iledesma@mi.unc.edu.ar
- tomas.viberti@mi.unc.edu.ar

## Resumen

## Introducción

## Referencias

## Punto 1

### a) ¿Qué es la serialización en redes de computadoras?

En el contexto de las redes de computadoras y sistemas distribuidos, la serialización es el proceso técnico de transformar una estructura de datos o un objeto complejo en memoria (como diccionarios, listas, clases o structs de un lenguaje de programación) en una secuencia o flujo de bytes.

El propósito fundamental de este proceso radica en que los datos en memoria poseen referencias internas y punteros abstractos que solo tienen sentido dentro del proceso local que los creó. Al transmitir información a través de un canal físico o de red de datos, estos datagramas o cargas útiles deben representarse de forma lineal y unificada para viajar a través de los protocolos de transporte y enlace.

El proceso inverso se denomina deserialización, mediante el cual el nodo receptor toma ese flujo continuo de bytes recibido desde la red y lo reconstruye en una estructura de datos idéntica en su propia memoria, permitiendo así una interpretación correcta de su significado lógico.

### b) ¿Cuál es la diferencia entre serialización binaria y no binaria? Buscar ejemplos, ventajas y desventajas de cada una.

La diferencia esencial entre ambas metodologías radica en el **formato de representación física** del flujo de bytes resultante: mientras que la serialización no binaria traduce la información a texto legible por humanos (caracteres ASCII/Unicode), la serialización binaria compacta la información directamente en secuencias binarias optimizadas para las máquinas.

#### 1. Serialización No Binaria (Formatos de Texto)

* **Concepto:** Transforma las estructuras de datos en cadenas de texto plano estructuradas bajo reglas gramaticales estrictas legibles tanto por humanos como por sistemas informáticos.
* **Ejemplos:** 
  * **JSON (JavaScript Object Notation):** Formato basado en pares clave-valor (ej. `{"group": "Grupo 1", "payload": "hola"}`) ampliamente utilizado en servicios web y APIs.
  * **XML (Extensible Markup Language):** Formato basado en etiquetas jerárquicas (ej. `<group>Grupo 1</group>`).
* **Ventajas:**
  * **Legibilidad:** Facilita enormemente las tareas de depuración (debugging) y auditoría técnica de paquetes, ya que un desarrollador puede inspeccionar el tráfico en tránsito (por ejemplo, mediante Wireshark o consolas) y comprender su significado al instante.
  * **Interoperabilidad Universal:** Al basarse en estándares de texto comunes, es completamente independiente del lenguaje de programación, sistema operativo o arquitectura de hardware de los nodos emisores y receptores.
* **Desventajas:**
  * **Overhead:** Al incluir delimitadores textuales, comillas, llaves y nombres de claves repetidas en cada mensaje, los paquetes resultantes son significativamente más grandes.
  * **Mayor consumo de procesamiento:** El parseo y análisis sintáctico de texto (string manipulation) requiere ciclos de reloj adicionales de CPU para convertir caracteres a variables lógicas tanto al codificar como al decodificar.

#### **2. Serialización Binaria**

* **Concepto:** Codifica las estructuras de datos directamente en un flujo continuo de bits y bytes densamente empaquetados bajo esquemas fijos de posición o codificaciones eficientes, perdiendo toda legibilidad directa para el ojo humano.


* **Ejemplos:**
  * **Protocol Buffers (Protobuf):** Desarrollado por Google, define esquemas mediante archivos `.proto` y serializa los campos de forma binaria compacta mediante identificadores numéricos simples.
  * **MessagePack o BSON:** Extensiones binarias que compactan estructuras similares a JSON en formatos de bits optimizados.
  * **Estructuras nativas de bajo nivel:** Formatos de cabeceras de red nativas encapsuladas en tramas estándar (como los campos binarios fijos de los mensajes BGP u OSPF).

* **Ventajas:**
  * **Eficiencia extrema en el ancho de banda:** Elimina metadatos redundantes y nombres de variables repetidos, reduciendo al mínimo indispensable el tamaño de la carga útil (*payload*) transmitida por el canal.
  * **Alto rendimiento de procesamiento:** La conversión entre los datos binarios de la red y las variables de memoria nativas de la máquina es casi directa, lo que acelera de forma drástica los tiempos de serialización y deserialización (ideal para sistemas embebidos o redes saturadas).

* **Desventajas:**
  * **Complejidad en la depuración:** El flujo de bytes es ilegible sin una herramienta específica que conozca el esquema de codificación exacto (mapeo de bits); en un analizador de tráfico ordinario, solo se apreciará como "ruido" o caracteres extraños.
  * **Acoplamiento de Esquemas:** Requiere rigidez y sincronización entre el cliente y el servidor. Si el esquema de datos cambia (por ejemplo, se añade un campo), ambos extremos deben conocer la actualización para interpretar de forma correcta los offsets de bits correspondientes.

---

## **Fuentes Bibliográficas de Referencia**

* **Comer, D. E. (2014).** *Internetworking with TCP/IP Vol. I: Principles, Protocols, and Architecture* (6th ed.). Pearson Education. *(Capítulos referenciales sobre encapsulamiento en la capa de transporte, stream de datos y delimitación lógica de mensajes a nivel de aplicación).* 

* **Stallings, W. (2004).** *Comunicaciones y redes de computadores*. Pearson Educación. *(Capítulo 12 y secciones de soporte técnico sobre eficiencia arquitectónica, overhead de control y requisitos funcionales en el intercambio de datos).* 
