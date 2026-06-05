# Trabajo Practico N5

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

## Punto 1 - Reconocimiento de Arquitectura

### 1. Firewall

* **a) ¿Qué problema resuelve?:** Protege la infraestructura filtrando el tráfico no deseado. Evita que ataques maliciosos (como inundaciones de requests o exploits conocidos) lleguen a los servidores internos consumiendo sus recursos o rompiendo la base de datos.
* **b) Capa del modelo TCP/IP:** Tradicionalmente opera en la **Capa de Internet (Red)** y **Capa de Transporte** (filtrando por IPs y puertos). Sin embargo, un firewall moderno o WAF (Web Application Firewall) actúa en la **Capa de Aplicación**, analizando el contenido del protocolo HTTP/HTTPS.
* **c) ¿Qué pasaría si falta?:** El sistema quedaría expuesto a ataques DDoS o inyecciones de código. Un atacante podría saturar los servidores muy fácilmente enviando peticiones basura que consuman toda la CPU o el ancho de banda.

### 2. Load Balancer

* **a) ¿Qué problema resuelve?:** Distribuye de forma equitativa el tráfico entrante entre múltiples servidores disponibles. Resuelve el cuello de botella de tener un único servidor saturado mientras los demás están libres, permitiendo escalar de forma horizontal.
* **b) Capa del modelo TCP/IP:** Puede operar en la **Capa de Transporte** (balanceo de Capa 4 basado en TCP y puertos) o en la **Capa de Aplicación** (balanceo de Capa 7 basado en cookies, URLs o cabeceras HTTP).
* **c) ¿Qué pasaría si falta?:** Habría un único punto de entrada directo a un servidor específico. Si ese servidor se cae por sobrecarga o mantenimiento, toda la aplicación se vuelve inaccesible para los usuarios, perdiendo disponibilidad.

### 3. Message Queue (Cola de Mensajes)

* **a) ¿Qué problema resuelve?:** Permite la comunicación asincrónica entre servicios. Resuelve el problema de los procesos pesados o lentos (como procesar un video o enviar mil mails) que bloquean la respuesta al usuario. El servidor web mete la tarea en la cola y le responde al cliente "en proceso", liberándose para atender otra request.
* **b) Capa del modelo TCP/IP:** Opera en la **Capa de Aplicación**, utilizando protocolos de transporte subyacentes para mantener la cola.
* **c) ¿Qué pasaría si falta?:** Todo el procesamiento tendría que ser sincrónico. Si un usuario realiza una acción pesada, su conexión HTTP quedaría abierta y bloqueada esperando que termine. Si entran muchas tareas pesadas juntas, los servidores web se quedarían sin hilos disponibles y el sistema se congelaría por completo, lo que se conoce como Timeouts.

### 4. Compute (Servidor Tradicional)

* **a) ¿Qué problema resuelve?:** Proporciona un entorno persistente y continuo de CPU y memoria RAM para ejecutar la lógica principal de la aplicación, mantener servidores activos, procesar peticiones y gestionar conexiones de red constantes de forma dedicada.
* **b) Capa del modelo TCP/IP:** Su función principal e interpretación de las reglas de negocio operan en la **Capa de Aplicación** (ej. ejecutando un servidor HTTP/HTTPS).
* **c) ¿Qué pasaría si falta?:** No habría un núcleo operativo estable para alojar el código persistente del backend. El sistema no tendría una infraestructura base donde mantener procesos corriendo de forma permanente a la espera de solicitudes.

### 5. Serverless Function (Función Lambda)

* **a) ¿Qué problema resuelve?:** Ejecuta pequeños bloques de código de forma aislada e instantánea en respuesta a eventos específicos (como cuando se sube un archivo o un usuario dispara una acción concreta). Evita tener que pagar por un servidor encendido las 24 horas cuando se trata de tareas esporádicas o picos de tráfico impredecibles, ya que escala a cero automáticamente.
* **b) Capa del modelo TCP/IP:** Se encuentra en la **Capa de Aplicación**.
* **c) ¿Qué pasaría si falta?:** El sistema perdería flexibilidad y optimización de costos. Todas las tareas secundarias o bajo demanda (como redimensionar una imagen que subió un usuario) tendrían que cargarse obligatoriamente sobre las instancias fijas del servidor, corriendo el riesgo de saturar el servidor principal con microtareas pesadas.

### 6. SQL Database (Base de Datos Relacional)

* **a) ¿Qué problema resuelve?:** Resuelve la persistencia de datos estructurados garantizando consistencia estricta mediante propiedades ACID (Atomicidad, Consistencia, Aislamiento y Durabilidad). Es ideal para manejar transacciones complejas y datos fuertemente relacionados (como cuentas de usuarios, dinero o compras).
* **b) Capa del modelo TCP/IP:** Pertenece a la **Capa de Aplicación**.
* **c) ¿Qué pasaría si falta?:** No habria forma de guardar información de manera persistente y confiable. Cualquier dato guardado se perdería al reiniciar el sistema o, si usaran archivos planos, se correria el riesgo de que los datos se corrompan ante accesos concurrentes.

### 7. NoSQL Database (Base de Datos No Relacional)

* **a) ¿Qué problema resuelve?:** Maneja volúmenes masivos de datos no estructurados o semiestructurados (como logs, chats o sesiones) con una velocidad de escritura extremadamente alta y gran facilidad para escalar horizontalmente.
* **b) Capa del modelo TCP/IP:** Pertenece a la **Capa de Aplicación**.
* **c) ¿Qué pasaría si falta?:** Habria que meter toda la información pesada o de cambio rápido en una base de datos SQL. Esto degradaría el rendimiento general de la base de datos principal, ya que el motor relacional se ahogaría indexando millones de registros simples por segundo.

### 8. Cache

* **a) ¿Qué problema resuelve?:** Almacena en una memoria ultrarrápida las respuestas a las consultas más frecuentes. Evita que el servidor tenga que procesar la misma lógica una y otra vez o que tenga que consultar repetitivamente a la base de datos (que es mucho más lenta).
* **b) Capa del modelo TCP/IP:** Se ubica principalmente en la **Capa de Aplicación**.
* **c) ¿Qué pasaría si falta?:** Cada request de cada usuario obligaría al sistema a realizar todo el camino de cómputo y lectura de discos. Ante un pico de tráfico masivo (por ejemplo, muchos usuarios queriendo ver el mismo producto en oferta), la base de datos colapsaría de inmediato por la cantidad de lecturas redundantes.

### 9. CDN (Content Delivery Network / Red de Distribución de Contenido)

* **a) ¿Qué problema resuelve?:** Almacena en caché y sirve el contenido estático (imágenes, scripts, páginas HTML fijas) en servidores distribuidos geográficamente por todo el mundo, lo más cerca posible del usuario final. Resuelve los problemas de alta latencia de red y evita que todo el tráfico mundial tenga que viajar hasta el servidor central, ahorrando un enorme ancho de banda.
* **b) Capa del modelo TCP/IP:** Opera en la **Capa de Aplicación** interceptando peticiones web (HTTP/HTTPS), aunque optimiza drásticamente el rendimiento del transporte al acortar la distancia física que recorren los paquetes.
* **c) ¿Qué pasaría si falta?:** Cada solicitud de cada archivo estático impactaría directo en la infraestructura central. Un usuario que está a miles de kilómetros experimentaría una lentitud extrema (mucha latencia por ruteo) y el servidor central colapsaría de inmediato ante cualquier pico de visitas por la sobrecarga de despachar archivos pesados y repetitivos.

### 10. Storage (Almacenamiento Persistente)

* **a) ¿Qué problema resuelve?:** Soluciona el problema de la persistencia de los datos. Proporciona un lugar seguro y permanente para almacenar información estructurada o archivos del sistema, garantizando que los datos no desaparezcan cuando los servidores de cómputo se reinician, escalan o se apagan.
* **b) Capa del modelo TCP/IP:** Pertenece a la **Capa de Aplicación**.
* **c) ¿Qué pasaría si falta?:** La aplicación sería completamente "volátil" o sin estado. El sistema no podría guardar perfiles de usuarios, registros de transacciones ni ningún tipo de progreso; todo se borraría por completo al instante de cerrar la sesión o actualizar el servidor.

### 11. Search Engine (Motor de Búsqueda Avanzada)

* **a) ¿Qué problema resuelve?:** Permite realizar búsquedas masivas, complejas y de texto completo con filtros avanzados e indexación ultrarrápida (en milisegundos). Resuelve la ineficiencia de las bases de datos tradicionales cuando tienen que buscar patrones de palabras o datos desestructurados entre millones de registros en tiempo real.
* **b) Capa del modelo TCP/IP:** Se ubica en la **Capa de Aplicación**.
* **c) ¿Qué pasaría si falta?:** Las funciones de búsqueda dentro de la aplicación se volverían extremadamente lentas o limitadas. Si obligasemos al componente de `Storage` común a procesar búsquedas semánticas o filtrados complejos de texto en grandes volúmenes de datos, el motor de almacenamiento se saturaría, elevando los tiempos de respuesta del sistema y degradando la experiencia del usuario.

### 12. Replica

* **a) ¿Qué problema resuelve?:** Alivia la carga de la base de datos principal (Master). Al copiar en tiempo real los datos del Master a otras instancias dedicadas exclusivamente a responder consultas de lectura (SELECTs), permite que la base de datos principal se enfoque sólo en escribir y modificar datos.
* **b) Capa del modelo TCP/IP:** Se gestiona íntegramente en la **Capa de Aplicación**.
* **c) ¿Qué pasaría si falta?:** Todo el tráfico del sistema (tanto el usuario que se registra como los miles de usuarios que solo están navegando y mirando contenido) impactaría sobre la misma base de datos. En aplicaciones con alto porcentaje de lectura, la base de datos se convertiría rápidamente en el cuello de botella central del sistema.

---

## **Fuentes Bibliográficas de Referencia**