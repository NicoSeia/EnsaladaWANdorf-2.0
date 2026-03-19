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

## Resumen

El presente informe documenta la simulación práctica de una infraestructura de red WAN y el análisis de mecanismos de detección de errores en la capa de enlace. En la primera etapa, se recreó el flujo de datos entre subredes locales (LAN) mediante una topología en estrella, validando los protocolos ARP para la resolución de direcciones físicas y el ruteo hop-by-hop para la interconexión de redes. Se analizó el proceso de encapsulamiento y la mutabilidad de las tramas Ethernet frente a la inmutabilidad de los paquetes IP. En la segunda fase, se aplicaron técnicas de EDAC (Paridad Par y Checksum) para evaluar la integridad de los payloads transmitidos, complementando el análisis con la implementación de algoritmos en Python para la detección y posible recuperación de errores de bit.

*Palabras clave*: Ruteo Hop-by-Hop, IP, MAC, Encapsulamiento, EDAC, Checksum, Paridad, LAN.

## Introducción

La comprensión de las redes de computadoras exige una visión clara de la interacción entre las capas del modelo OSI, específicamente entre la capa de Enlace (Capa 2) y la de Red (Capa 3). Este trabajo práctico se propone como un laboratorio didáctico para desglosar la complejidad del transporte de datos en un entorno multirred.

A través de una simulación física, se busca que el estudiante experimente el "caos" inherente a la transmisión de datos, comprendiendo el rol crítico de los routers como nodos de decisión y la necesidad de mecanismos de control como el TTL  para garantizar la estabilidad del sistema. Asimismo, se aborda la problemática de la corrupción de datos, explorando técnicas de redundancia que permiten asegurar que la información recibida coincida con la emitida, sentando las bases de la comunicación confiable en redes digitales.

## Desarrollo Parte 1. Repaso general didáctico: Simulación de envío de paquetes, ARP y ruteo entre redes.

Para comenzar con el trabajo, fue necesario realizar la topografía de la red que íbamos a simular; para ello, entre todos los grupos fuimos armando su topología. Se planteó el problema de tener tres routers, los cuales son los nodos centrales encargados de reenviar los paquetes a su destino correcto. Por otro lado, definimos hosts que estaban comunicados únicamente con alguno de los routers centrales.

A continuación, se detalla la red:

![Red topologica](red.png)

### 1) Identificación de dispositivos y armado de la topología

En esta fase, cada integrante configura su **NIC (Network Interface Card)**. Hemos cruzado los datos de red del Grupo 4 con las direcciones físicas (MAC) únicas de cada legajo proporcionado.

#### Tarjeta de Identificación de Red (Configuración NIC)

| Rol | Nombre del Dispositivo | Legajo | Dirección IP | Máscara de Subred | Gateway (GW) | Dirección MAC |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Router** | Router-Ensalada | - | **10.4.0.1** | 255.255.255.0 | N/A | AD:71:88 |
| **Host 1** | Host-Ignacio | 44346001 | **10.4.0.101** | 255.255.255.0 | 10.4.0.1 | **AD:44:00** |
| **Host 2** | Host-Tomas | 43692641 | **10.4.0.102** | 255.255.255.0 | 10.4.0.1 | **AB:43:64** |
| **Host 3** | Host-Gaston | 43365894 | **10.4.0.103** | 255.255.255.0 | 10.4.0.1 | **AD:43:89** |
| **Host 4** | Host-Nicolas | 43366980 | **10.4.0.104** | 255.255.255.0 | 10.4.0.1 | **AD:43:98** |

> **Nota:** Se utiliza una máscara de subred `/24` (255.255.255.0) para permitir hasta 254 hosts dentro de la LAN `10.4.0.0`.

### 2) Armado de topología

En este paso, cada grupo asignó un router por defecto (default gateway), el cual era el encargado de comunicarse con el router central. Es decir, cada host debía estar vinculado a su router y, a su vez, este debía contar con una tabla con las direcciones internas conocidas del host. En el caso del router central, este debía tener la referencia de la dirección IP de su respectivo host.

La red se estructura de forma física mediante una **topología en estrella**. El Router centraliza las conexiones de Ignacio, Tomás y Gastón, permitiendo la comunicación interna y la salida hacia la WAN (otras redes 10.x).

#### Rutina de descubrimiento ARP

Para que el Router pueda entregar paquetes a los hosts, debe resolver las direcciones físicas. Se simula el envío de un **ARP Request** por broadcast y la recepción de un **ARP Reply** unicast desde cada host.

#### Tabla ARP (Mapa de Direcciones IP vs. Físicas)

Esta es la tabla resultante que el Router almacena en su memoria tras el proceso de descubrimiento:

| Dispositivo | Dirección IP | Dirección MAC | Interfaz del Router |
| :--- | :--- | :--- | :--- |
| Host-Ignacio | 10.4.0.101 | **AD:44:00** | FastEthernet 0/1 |
| Host-Tomas | 10.4.0.102 | **AB:43:64** | FastEthernet 0/2 |
| Host-Gaston | 10.4.0.103 | **AD:43:89** | FastEthernet 0/3 |
| Host-Nicolas | 10.4.0.104 | **AD:43:98** | FastEthernet 0/4 |

#### Tabla de Ruteo Básica del Router

Para interactuar con la WAN, el router gestiona hacia dónde enviar los paquetes que no pertenecen a la red local `10.4.0.0`:

| Red Destino | Máscara | Próximo Salto | Interfaz |
| :--- | :--- | :--- | :--- |
| 10.4.0.0 | 255.255.255.0 | Conectada directamente | LAN |
| 0.0.0.0 (Default) | 0.0.0.0 | 10.x.x.x (Router Vecino) | WAN |

### 3) Conformación de paquetes

Para esta actividad, se configuró un paquete de red que permita la comunicación desde nuestra subred local (**EnsaladaWANdorf-2.0**) hacia un host externo de la red vecina del grupo "The Lords of Pings".

#### Datos de Origen (Nicolas)

* **IP Origen:** `10.4.0.104` (Host 4 del Grupo 4)
* **MAC Origen:** `AD:43:98`
* **Payload (Hex):** `1e0b`

#### Datos de Destino (Enzo - The Lords of Pings)
* **IP Destino:** `10.5.0.104` (Host 4 del Grupo 5)
* **MAC Destino:** `AC:44:52`

#### Detalle de Encapsulamiento

A continuación, se detalla cómo queda conformado el frame para ser enviado al medio físico:

**FRAME ETHERNET**: 

| Campo | Valor | Justificación |
| :--- | :--- | :--- |
| **MAC DESTINO** | **AD:71:88** | **MAC del Gateway (Router)**|
| **MAC ORIGEN** | **AD:43:98** | Dirección física de la NIC de Nicolas. |

**PAQUETE IP**
| Campo | Valor | Justificación |
| :--- | :--- | :--- |
| **IP ORIGEN** | `10.4.0.104` | Identidad lógica de Nicolas en la LAN. |
| **IP DESTINO** | `10.5.0.104` | IP de Enzo en el grupo "The Lords of Pings". |
| **TTL** | `6` | Tiempo de vida definido por consigna. |
| **PAYLOAD** | **`0001 1110 0000 1011`** | Conversión binaria de `1e0b` (Hex). |
| **CRC** | `<vacío>` | Se autogenera en la transmisión. |

#### Ejemplo del recorrido (Nicolas $\rightarrow$ Enzo)

La IP es "extremo a extremo" (end-to-end) y por eso no cambian nunca durante todo el viaje, en cambio la MAC es "salto a salto" (hop-by-hop), lo que quiere decir que va a ir cambiando a medida que el paquete se traslada por la red, porque el router se encarga de "encaminarlo" por diferentes nodos. Ambas direcciones fisicas (MAC de destino y origen) van a ir cambiando, siendo el Frame Ethernet mostrado anteriormente el que está al inicio del tráfico del paquete. 

| Tramo del viaje | MAC Origen | MAC Destino | ¿Qué sucede? |
| :--- | :--- | :--- | :--- |
| **Salto 1:** De Nicolas al Router-Ensalada | `AD:43:98` (Nicolas) | **`AD:71:88`** (Router G4) | Nicolas entrega el paquete a su gateway para que lo saque de la LAN. |
| **Salto 2:** Del Router-Ensalada al Router-Lords | `MAC-WAN-G4` | **`MAC-WAN-G5`** | El router cambia el "sobre". Ahora la MAC destino es la del router del grupo de Enzo. |
| **Salto 3:** Del Router-Lords a Enzo | `AD:44:02` (Router G5) | **`AD:44:64`** (Enzo) | El router final usa su **Tabla ARP** para saber la MAC física de Enzo y entregarle el paquete. |

### 4) Simular las transmisiones y recepciones

Esta fase consistió en la ejecución física del flujo de datos a través de la red WAN simulada en el aula. Se documentó el comportamiento de los paquetes desde su origen en una LAN hasta su recepción final.

#### A. Generación y Encapsulamiento (Origen - LAN)

Cada integrante del grupo asumió el rol de host en una LAN, iniciando la construcción del paquete en formato físico (papel). Se definieron los siguientes parámetros críticos:

1. **Direccionamiento de Capa 2:** Se asignó la dirección MAC de origen.
2. **Direccionamiento de Capa 3:** Se establecieron las IP de origen y destino.
3. **Construccion:** Se fijó el TTL (Time to Live) en 6 y se cargó el Payload en formato binario.

#### B. Entrega al Gateway (Salida de la Red Local)

Una vez conformado el paquete, este se entregó al Default Gateway. Este nodo actuó como el intermediario necesario para que el tráfico local pudiera alcanzar el núcleo de la red (los routers centrales).

1.  **Determinación de Ruta:** Mediante la máscara de subred (`255.255.255.0`), el host determinó que la IP destino pertenecía a una red remota (ej. `10.9.0.0`).
2.  **Resolución ARP:** Al ser un destino remoto, el host resolvió la dirección MAC de su **Gateway por defecto** (`AD:71:88`) para encapsular el paquete.

#### C. Conmutación y Ruteo (Core de la Red)
Al recibir los paquetes físicos, los routers centrales aplicaron la lógica de conmutación de paquetes. El proceso de decisión se basó en:

- **Consulta de Tablas de Ruteo:** Los tres routers centrales se comunicaron entre sí para determinar cuál de ellos tenía conexión directa con la IP de destino.
- **Procesamiento del Paquete:**
   - **Desencapsulamiento:** El router recibió el frame, verificó que la MAC destino fuera la suya y procedió a leer la cabecera IP.
   - **Decremento de TTL:** Como medida de control para evitar bucles, cada router restó una unidad al TTL.
   - **Re-encapsulamiento:** Tras consultar su tabla de ruteo y determinar el siguiente salto (Next Hop), el router descartó el frame Ethernet anterior y construyó uno nuevo con su propia MAC como origen y la MAC del siguiente nodo como destino.
- **Manejo de Errores (Destino Inalcanzable):** Si la IP de destino no existía en ninguna tabla, el paquete se devolvió al emisor con una notificación de error (simulando un mensaje ICMP Destination Unreachable).

#### D. Entrega Final (Destino)

Si el router central lograba localizar la red del host de destino, el paquete era reenviado exitosamente, completando el ciclo de comunicación al llegar a la interfaz del receptor final.

Se detallan capturas del proceso:

![RecDU](paqueteRecibido.jpeg)

![RecCorrect](pauqeteRecibido2.jpeg)

![PaquetesLost](paquetesSinTerminar.jpeg)

Como se observa en las capturas de la simulación, el proceso de "salto a salto" queda evidenciado por las correcciones manuales en los campos de **Capa 2 (MAC)** y el **TTL**:
* **MAC Origen/Destino:** Se aprecia el cambio constante de direcciones físicas mientras que las **direcciones IP permanecen inmutables**, confirmando la teoría de ruteo extremo a extremo.
* **Validación en Destino:** El host receptor final comparó la MAC destino del frame con la suya propia y, al coincidir, procesó el paquete IP para leer el payload binario.

### 5) Reflexiones y documentación

**a)** Durante el laboratorio, la dirección IP destino del paquete se mantuvo constante mientras que la dirección MAC destino cambió en cada salto. ¿Por qué ocurre esto y qué nos dice sobre la diferencia entre direccionamiento lógico (IP) y direccionamiento físico (MAC)?

> Podemos decir que el "direccionamiento lógico" (IP), se mantiene constante ya que identifica el punto final de la comunicación a nivel global, permitiendo una comunicación extremo a extremo (end-to-end) en la Capa 3. En constrante, el "direccionamiento físico" (MAC) es un identificador local de la Capa 2 que solo tiene validez dentro de un mismo segmento de red. Su cambio en cada salto nos indica que la MAC no sirve para ubicar un dispositivo en Internet, sino para gestionar la entrega del paquete entre nodos adyacentes dentro de un mismo enlace físico.

**b)** Cuando un host quiere enviar un paquete a un dispositivo en otra red, no intenta descubrir directamente la MAC del host destino, sino la del default gateway. ¿Por qué se utiliza este mecanismo y qué problema resolvería el gateway que el host no puede resolver por sí solo?

> Un host solo puede descubrir direcciones MAC de dispositivos que están en su propia red local. No buscan descubrir la MAC de destino final porque, como comentamos anteriormente, va de salto en salto entre los nodos de un mismo enlace. 
> 
> Cuando el host determina (mediante su máscara de subred) que el destino es remoto, utiliza el mecanismo de Default Gateway para delegar la entrega. El gateway resuelve el problema de la visibilidad y ruteo: el host no necesita conocer el mapa de la red externa; solo necesita saber que, para salir de su LAN, debe encapsular el paquete hacia la MAC del router, quien sí posee las tablas necesarias para encaminar el tráfico hacia otras redes.

**c)** Cada router toma decisiones basándose únicamente en su tabla de ruteo local y no en el camino completo
hacia el destino. ¿Qué ventajas tiene este modelo de ruteo hop-by-hop para redes grandes como Internet?

> Este modelo, hop-by-hop, es fundamental por diferentes razones como:
> 
> - Eficiencia de memoria: Eficiencia de recursos: Los routers no requieren almacenar la ruta completa de cada paquete, sino únicamente el "próximo salto" hacia la red de destino, optimizando el uso de memoria.
> - Flexibilidad: Permite una red dinámica; si un enlace intermedio falla, cada router puede recalcular su tabla local para desviar el tráfico sin que los hosts de origen deban reconfigurarse.
> - Descentralización: Reduce la complejidad del procesamiento, ya que la responsabilidad del éxito de la transmisión se distribuye entre todos los nodos del trayecto.

**d)** En el laboratorio observamos que los routers desencapsulan y vuelven a encapsular el paquete en cada
enlace. ¿Por qué es necesario reconstruir el frame Ethernet en cada salto y qué ocurriría si los routers
intentaran reenviar exactamente el mismo frame?

> El re-encapsulamiento es imprescindible porque la cabecera Ethernet (Capa 2) es específica del enlace físico actual y "muere" al llegar a la interfaz del router. El router debe desencapsular para examinar la IP de destino en la Capa 3 y, tras decidir la ruta, debe re-encapsular el paquete en un nuevo frame con las direcciones MAC correspondientes al siguiente segmento. Si no se reconstruyera el frame, el siguiente dispositivo descartaría la trama, ya que la MAC de destino seguiría apuntando al router anterior y no a sí mismo, impidiendo que el paquete avance.

**e)** El campo TTL se decrementa en cada router. ¿Qué problema de la red previene este mecanismo y qué
podría suceder si el TTL no existiera?

> El campo TTL actúa como un mecanismo de seguridad que previene la existencia de paquetes "huérfanos" circulando infinitamente debido a bucles de ruteo o tablas mal configuradas. Sin el TTL, un error en la red podría generar un consumo exponencial de ancho de banda y procesamiento, saturando la red muy rapido y colapsando los enlaces. Al decrementarse en cada salto, el TTL garantiza que el paquete sea descartado si no alcanza su destino en un $N$ número razonable de saltos ($TTL = 0$), liberando así los recursos de la infraestructura.

### Desarrollo Parte 2. Inyección y detección de errores.

Esta es una propuesta de desarrollo para la **Parte 2** de tu informe, estructurada de forma técnica y académica, integrando los cálculos manuales que hicieron en papel y la lógica de programación que aplicaron para automatizar la detección.

---

## Parte 2: Inyección y detección de errores

En esta etapa del laboratorio, se trabajó sobre la integridad de los datos en la capa de enlace. El objetivo fue aplicar técnicas de **EDAC (Error Detection and Correction)** para identificar alteraciones en el Payload durante el tránsito por la red.

### 1. Metodología y Roles

El aula se dividió en dos grandes bloques operativos para generar un esquema de "emisión y recepción cruzada". Cada sector utilizó un método de generación de redundancia de 4 bits para un payload de 16 bits[cite: 1].

#### Sector 1: Paridad Par por Nibble

Este fue el método utilizado por nuestro grupo para la **emisión** de paquetes.

* **Concepto:** Se basa en contar la cantidad de bits en estado "1" dentro de un conjunto de datos.
* **Funcionamiento:** El payload de 16 bits se divide en **4 nibbles** (grupos de 4 bits). Para cada nibble, se calcula un bit de paridad tal que el total de unos sea un número par.
* **Generación del EDAC:** Los 4 bits resultantes (uno por cada nibble) se agrupan para formar el código de detección de 4 bits que acompaña a la trama.

#### Sector 2: Checksum (Suma de Verificación) por Nibble

Este fue el protocolo que debimos manejar para la **recepción y validación** de los paquetes provenientes de otros grupos.

* **Concepto:** Utiliza la aritmética binaria para generar una "huella digital" del contenido basada en su suma total.
* **Funcionamiento:** Se realiza una *Suma de Complemento a Uno*. Los 4 nibbles del payload se suman aritméticamente.
* **End-around carry:** Si la suma genera un acarreo (un bit extra que excede los 4 bits), este no se descarta, sino que se suma al bit menos significativo del resultado final.
* **Generación del EDAC:** El resultado final de esta suma circular de 4 bits constituye el Checksum que debe coincidir en el destino para validar la integridad.

#### Diferencia Clave en la Detección

| Característica | Paridad Par | Checksum |
| :--- | :--- | :--- |
| **Nivel de detección** | Detecta errores de bits impares por nibble. | Detecta cambios aritméticos en la carga útil. |
| **Complejidad** | Muy baja (conteo de bits). | Media (requiere suma y manejo de acarreo). |

### 2. Análisis del Paquete Recibido

<img width="1824" height="184" alt="image" src="https://github.com/user-attachments/assets/37a0d8c5-e9a6-4d55-8b7b-4fc472a822b5" />

Recibimos un paquete físico desde la IP de origen **10.7.0.1** destinado a nuestra red **10.4.0.1**.

**Datos del Paquete:**
| Campo | Valor |
| :--- | :--- |
| **IP Origen** | 10.7.0.1 |
| **IP Destino** | 10.4.0.1 |
| **Payload Recibido** | `0000 1111 0101 1111` |
| **EDAC Recibido** | `0101` |

#### Verificación Manual (Checksum por Nibble)

Para comprobar la integridad, fragmentamos el payload de 16 bits en 4 nibbles ($N_n$) de 4 bits cada uno y aplicamos la suma con acarreo circular:

1.  **Conversión y Suma:**
    * $N_1 (0000) = 0$
    * $N_2 (1111) = 15$
    * $N_3 (0101) = 5$
    * $N_4 (1111) = 15$
    * **Suma Total:** $0 + 15 + 5 + 15 = 35_{10}$

2.  **Aplicación de Acarreo Circular:**
    Convertimos el resultado a binario: $35_{10} = 100011_2$. Como el sistema es de 4 bits, tomamos los bits excedentes (`10`) y los sumamos al valor principal (`0011`):
    $$0011_2 + 10_2 = 0101_2 = 5_{10}$$

3.  **Conclusión de Integridad:**
    El valor calculado (**`0101`**) coincide exactamente con el EDAC recibido (**`0101`**). Por lo tanto, se documenta que el paquete **no fue modificado** durante la intervención del profesor.

<img width="900" height="890" alt="image" src="https://github.com/user-attachments/assets/21717000-e32f-4b59-9f05-ec50214a3d12" />

### 3. Automatización y Recuperación (Python)

Desarrollamos una herramienta en Python para agilizar la verificación y permitir la recuperación de la trama original ante errores de 1 bit.

* **Lógica de Verificación:** El script fragmenta la cadena binaria y calcula el Checksum (en el código implementado como XOR para pruebas de redundancia cíclica o Checksum según el caso) para validar el estado del paquete. Se asume que el EDAC no fue modificado.
* **Recuperación de Errores:** En caso de discrepancia, el algoritmo invierte sistemáticamente cada uno de los bits de la Payload hasta encontrar una combinación que satisfaga la condición del Checksum, identificando así el bit erróneo.

```python
def calcular_checksum_xor(payload_bin: str) -> str:
    """Calcula el checksum XOR de 4 bits para un payload de 16 bits."""
    # Separar el payload en 4 nibbles
    n1 = int(payload_bin[0:4], 2)
    n2 = int(payload_bin[4:8], 2)
    n3 = int(payload_bin[8:12], 2)
    n4 = int(payload_bin[12:16], 2)
    
    # Aplicar XOR entre todos los nibbles
    checksum = n1 ^ n2 ^ n3 ^ n4
    
    # Devolver como string binario de 4 caracteres (ej: '0101')
    return format(checksum, '04b')

def verificar_y_recuperar_trama(payload_bin: str, edac_bin: str) -> dict:
    """
    Verifica si el payload coincide con su EDAC. 
    Asume que el EDAC recibido es correcto. Si hay error en el payload, 
    calcula las posibles tramas originales asumiendo un error de 1 bit.
    """
    if len(payload_bin) != 16 or len(edac_bin) != 4:
        raise ValueError("El payload debe tener 16 bits y el EDAC 4 bits.")

    edac_calculado = calcular_checksum_xor(payload_bin)
    
    if edac_calculado == edac_bin:
        return {
            "estado": "OK",
            "mensaje": "El payload es válido. No se detectaron errores.",
            "posibles_soluciones": []
        }

    # Si llegamos acá, HAY UN ERROR. 
    posibles_soluciones = []

    # Invertimos 1 bit a la vez SOLO en el payload (16 bits)
    for i in range(16):
        # Cambiamos un '0' por '1' o un '1' por '0'
        bit_invertido = '1' if payload_bin[i] == '0' else '0'
        payload_prueba = payload_bin[:i] + bit_invertido + payload_bin[i+1:]
        
        # Calculamos el EDAC de este nuevo payload modificado
        edac_prueba = calcular_checksum_xor(payload_prueba)
        
        # Si el EDAC de esta prueba coincide con el EDAC original (que asumimos correcto), 
        # encontramos una posible solución válida.
        if edac_prueba == edac_bin:
            posibles_soluciones.append({
                "bit_modificado": i, # Índice del 0 al 15
                "payload_sugerido": payload_prueba,
                "edac": edac_bin  # El EDAC se mantiene intacto
            })

    return {
        "estado": "ERROR",
        "mensaje": f"EDAC recibido ({edac_bin}) no coincide con el calculado ({edac_calculado}).",
        "posibles_soluciones": posibles_soluciones
    }


# ==========================================
# Ejemplos de uso
# ==========================================
if __name__ == "__main__":
    
    payload = "0000111101011111" 
    edac = "0101"
    
    resultado = verificar_y_recuperar_trama(payload, edac)
    
    print(f"Estado: {resultado['estado']}")
    print(f"Mensaje: {resultado['mensaje']}\n")
    
    print("Posibles paquetes originales (asumiendo que el EDAC es correcto):")
    for sol in resultado['posibles_soluciones']:
        print(f" - Cambiando bit {sol['bit_modificado']} -> Payload Sugerido: {sol['payload_sugerido']}")
```

---

## Conclusiones

### 1. Dinámica del Tránsito de Datos entre Redes

Se validó empíricamente que la comunicación entre hosts de distintas LANs depende de una jerarquía de direccionamiento clara. Mientras que la **dirección IP** actúa como un identificador global persistente que define el origen y el destino final (comunicación *end-to-end*), las **direcciones MAC** son efímeras y cambian en cada salto del ruteo (*hop-by-hop*). Este mecanismo de re-encapsulamiento es el que permite que Internet sea escalable; un host solo necesita conocer a su **Default Gateway** para acceder al resto del mundo, delegando la complejidad del camino completo a la inteligencia colectiva de las tablas de ruteo locales de los nodos centrales.

### 2. Eficacia de los Métodos EDAC: Checksum vs. Paridad

La comparativa entre los métodos de detección utilizados revela un compromiso entre simplicidad y robustez:

* **Paridad Par por Nibble:** Es el método más elemental. Su principal ventaja es el bajo costo computacional, ideal para hardware de baja potencia o comunicaciones seriales simples. Sin embargo, su gran desventaja es su limitada capacidad de detección: solo identifica errores si el número de bits alterados es impar. Si dos bits cambian simultáneamente dentro de un mismo nibble, el error resulta invisible para este protocolo.
* **Checksum (Suma de Verificación):** Ofrece una robustez superior al basarse en la suma aritmética de los datos. Su ventaja radica en que detecta no solo cambios de bits individuales, sino también alteraciones en la estructura aritmética del mensaje. Es el estándar utilizado en cabeceras de protocolos como **IP y TCP**, ya que equilibra una buena tasa de detección con un procesamiento eficiente mediante sumas de complemento a uno.

> En conclusión, este trabajo práctico permitió transformar conceptos abstractos en experiencias tangibles, demostrando que la arquitectura de Internet no es un bloque rígido, sino un sistema fluido de capas que colaboran para llevar la información de forma segura y eficiente de un extremo a otro del globo.
