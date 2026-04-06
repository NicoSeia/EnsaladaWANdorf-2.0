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

