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

## Punto 2 - Tabla de Clasificación de Tipos de Tráfico

| Tipo de Tráfico | Ejemplo Real | Componente Recomendado | Riesgo si se procesa incorrectamente |
| --- | --- | --- | --- |
| **STATIC** | Logotipos, archivos CSS de estilos, frameworks JavaScript (`.js`), fuentes tipográficas o páginas HTML fijas. | **CDN** | Si impacta directo en el server, se desperdicia ancho de banda y ciclos de CPU esenciales entregando archivos pesados y repetitivos, ralentizando la lógica del backend. |
| **READ** | Consultar el feed de publicaciones de una red social, listar productos disponibles en una tienda, o ver el perfil público de un usuario. | **Storage** (Réplicas de Lectura / Caché si existiera) | Si todas las consultas pesadas van directo al nodo de almacenamiento principal, se satura el disco con operaciones repetitivas, aumentando la latencia general del sistema. |
| **WRITE** | Registrar un nuevo usuario, realizar una compra (crear una factura) o dar "me gusta" a una publicación. | **Servidor** + **Storage** (Base de datos transaccional principal) | Si no se procesa mediante una cola o directamente en un almacenamiento consistente, se pueden duplicar transacciones, corromper registros concurrentes o perder datos críticos por bloqueos de tablas. |
| **UPLOAD** | Subir una foto de perfil en alta resolución, adjuntar un archivo PDF en un formulario o subir un video corto. | **Storage** | Si el archivo se guarda en el disco local de la instancia del servidor, el disco rígido se llenará rápidamente, degradando el sistema operativo y haciendo imposible el escalado horizontal. |
| **SEARCH** | Buscar un producto por palabras clave en la barra de búsqueda empleando filtros por precio, categoría y ubicación en tiempo real. | **Search Engine** (ej. Elasticsearch) | Si se obliga al almacenamiento relacional común (`Storage`) a procesar búsquedas semánticas o de texto completo, la base de datos se congela por el alto consumo de CPU. |
| **MALICIOUS** | Ataques de inyección SQL, scripts automatizados para adivinar contraseñas (fuerza bruta) o ataques de denegación de servicio (DDoS). | **Firewall** (o WAF / Reglas de filtrado perimetral) | Si el tráfico malicioso pasa de largo y llega a los componentes de cómputo, consumirá todos los recursos disponibles, tirando el sistema abajo para los usuarios reales. |

## Punto 3 - Testeando queues

Distribución de trafico:

| STATIC |	READ |	WRITE |	UPLOAD |	SEARCH |	ATTACK |
| --- | --- | --- | --- | --- | --- |
| 30% |	20%	| 15% |	5% |	10% |	20% |

#### ¿Qué sucede al incrementar el rate? Después de la queue

Al aumentar el throughput, la cantidad de tráfico que llega supera la capacidad de procesamiento inmediato de los nodos siguientes o del enlace. Al no dar abasto, los paquetes empiezan a acumularse en la queue. La cola sirve justamente como un "buffer" o colchón de memoria.

#### Si mantenemos el rate alto y luego lo bajamos a cero, ¿qué sucede?

A pesar de que el generador de tráfico ya está en cero (no entran más paquetes nuevos al firewall), después de la queue se siguen observando paquetes avanzando hacia la instancia final

- Rate alto
<img width="515" height="327" alt="image" src="https://github.com/user-attachments/assets/6e88191c-c3b8-4a8e-8164-a2fec6e84c0b" />

- Drenado de queue
<img width="516" height="347" alt="image" src="https://github.com/user-attachments/assets/629fd174-03c6-432e-ac3a-d305b0eb9a86" />

## Punto 4 - Primera arquitectura

- a) La arquitectura inicial, b) El presupuesto inicial, c) El estado de salud de los servicios

<img width="1394" height="659" alt="image" src="https://github.com/user-attachments/assets/070f8bd8-59de-47bc-b7f1-a048b942f702" />

- d) El momento que empieza a fallar, si es que falla

<img width="1386" height="696" alt="image" src="https://github.com/user-attachments/assets/ddb5af93-8a6a-470c-9490-bf078195cc2a" />

¿Qué componente falló primero?

Los primeros componentes en mostrar signos de saturación y fallar de forma inminente fueron el nodo de Compute y la Message Queue. En la simulación se puede observar claramente que ambos cambiaron su color a naranja, lo que indica que entraron en un estado crítico de cuello de botella antes que el resto de los servicios de almacenamiento o bases de datos.

¿Por qué creés que falló?

El nodo de Compute falló porque alcanzó su límite absoluto de procesamiento, operando a Load: 4/4 (100%). Al estar este servidor completamente saturado, dejó de procesar las solicitudes a la velocidad que ingresaban. Esto provocó un efecto dominó inmediato sobre la Message Queue: como el servicio de cómputo no podía recibir más datos, la cola no pudo descargar sus paquetes y empezó a llenarse de forma crítica, pasando también a estado de alerta naranja por acumulación de tráfico.

¿Fue un problema de capacidad, diseño, costo o seguridad?

Fue principalmente un problema de capacidad. El diseño de la arquitectura es correcto porque delegó el tráfico a los servicios correspondientes (base de datos, almacenamiento, etc.) y usó una cola como buffer. Sin embargo, el nodo de Compute T1 resultó ser demasiado chico para el volumen de rate configurado.

## Punto 5 - Escalabilidad y balanceo

### Estrategia 1:

<img width="754" height="425" alt="image" src="https://github.com/user-attachments/assets/f81da0e8-677d-433d-ac41-2c0af52822cd" />

Se implementó un Load Balancer para distribuir el tráfico horizontalmente hacia tres instancias de Compute. Esto busca eliminar el cuello de botella del servidor único repartiendo la carga.

### Estrategia 2:

<img width="962" height="533" alt="image" src="https://github.com/user-attachments/assets/13ed85c6-9f02-4a9a-9964-b07cc284608a" />

Se mantuvo el balanceador y los tres servidores, pero se agregó Cachés. Esto intenta interceptar las consultas repetitivas antes de que saturen los nodos de almacenamiento final.

#### ¿Escalar horizontalmente siempre mejora el sistema?

Estrategia 1: Al incrementar el rate a un valor mayor o igual a 30, los tres nodos de cómputo volvieron a fallar (se los ve en naranja/crítico). Aunque distribuir la carga ayuda a soportar más tráfico que antes, el escalado horizontal de la capa de aplicación no sirve si el volumen de solicitudes supera la capacidad de procesamiento combinada de los nuevos nodos, o si el cuello de botella se traslada a otro punto común.

Estrategia 2: En la segunda imagen, a pesar de haber agregado nodos de caché y componentes adicionales para aliviar la carga, los tres servidores de cómputo volvieron a encender sus alertas en rojo (círculos rojos en la base de los cilindros). Esto demuestra que si la tasa de ingreso de datos es masiva, los servidores de cómputo se saturan de todas formas intentando procesar la lógica de negocio, los uploads o las escrituras en la base de datos, las cuales no se pueden cachear fácilmente.

## Punto 6 - Sobrevivir



---

## **Fuentes Bibliográficas de Referencia**
