# Trabajo Practico N3

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

En este trabajo práctico se abordan conceptos fundamentales relacionados con la infraestructura de servicios web desde una perspectiva de redes. Se exploran herramientas y protocolos clave utilizados en la administración y comunicación entre sistemas, como SSH, TCP/UDP, HTTP y utilidades como Wireshark y netcat.

El objetivo principal es comprender cómo se establecen conexiones seguras y no seguras entre equipos, analizar el tráfico de red generado en distintos escenarios y reflexionar sobre la importancia de la confidencialidad en las comunicaciones digitales.

## Introducción

En este trabajo se investigaron conceptos clave relacionados con la seguridad en redes, como el uso de SSH para conexiones remotas seguras, la diferencia entre autenticación y cifrado, y el funcionamiento de claves públicas y privadas. Luego, se realizaron prácticas sobre máquinas virtuales para establecer conexiones y verificar el acceso remoto.

Mediante el uso de Wireshark, se capturó y analizó el tráfico de red generado en distintos escenarios. Se observó que el tráfico SSH no puede ser interpretado debido a su cifrado, mientras que en protocolos como TCP, UDP y especialmente HTTP, la información puede visualizarse en texto plano, lo que representa un riesgo de seguridad.

Además, se utilizó netcat para simular comunicaciones cliente-servidor y para intercambiar mensajes entre distintas máquinas, lo que permitió analizar el comportamiento de los protocolos y sus diferencias. Finalmente, se desplegó un servidor web simple y se comprobó su acceso desde un navegador, capturando el tráfico HTTP y reflexionando sobre la posibilidad de interceptar y modificar los datos transmitidos.

En conjunto, el trabajo permitió comprender la importancia del cifrado, la confidencialidad de la información y la necesidad de aplicar buenas prácticas de seguridad en redes.

## Parte 1

**a) ¿Qué es SSH y qué problema resuelve?**

Antes de SSH existían protocolos como Telnet o rsh para conectarse remotamente a otras máquinas, pero transmitían todo en texto plano, incluyendo contraseñas. Cualquiera con acceso a la red podía interceptar esa información fácilmente. SSH (Secure Shell) es un protocolo de red que permite conectarse y controlar una computadora remota de forma segura. 

**b) Diferencia entre autenticación y cifrado**

- Cifrado: es asegurar el canal, es decir que aunque alguien intercepte los datos, no los pueda ver. Es decir que protege el contenido de la comunicación.
- Autenticación: es verificar que la máquina del otro lado es realmente quien dice ser. Es como pedir el documento antes de abrir la puerta.

**c) ¿Qué es una clave pública y una clave privada?**

Son un par de claves matemáticamente relacionadas:

- Clave pública: podés compartirla con cualquiera. Se usa para cifrar mensajes o verificar tu identidad.
- Clave privada: solo la tenés vos. Se usa para descifrar mensajes o firmar tu identidad.

Lo que una cifra, solo la otra puede descifrarlo. La magia está en que conocer la clave pública no te permite deducir la privada.

**d) ¿Por qué la clave privada no debe compartirse?**

La clave privada es literalmente tu identidad digital. Si alguien la obtiene:

- Puede hacerse pasar por vos ante cualquier servidor
- Puede descifrar todo el tráfico que te enviaron cifrado con tu clave pública
- No hay forma de distinguir al atacante de vos

**e) ¿Qué ventajas tienen las claves SSH frente a contraseñas?**

| | Contraseñas | Claves SSH |
|---|---|---|
| **Viajan por la red** | Sí (aunque cifradas) | No, nunca |
| **Vulnerables a fuerza bruta** | Sí | Prácticamente no |
| **Pueden ser adivinadas** | Sí | No |
| **Automatización** | Complicado | Muy fácil |
| **Pueden filtrarse** | Sí (phishing, etc.) | No (la privada nunca sale de tu máquina) |

## Parte 2
Se validó la conectividad y administración remota de una VM mediante el protocolo SSH. Se consideran tres aspectos importantes:
1. Se ajustaron los privilegios de la clave privada utilizando el comando chmod 400, de modo que solo el propietario tenga permisos de escritura.
2. Se estableció una sesión hacia la dirección IP 4.174.129.188 utilizando el puerto por defecto.
3. Una vez dentro del entorno remoto se utilizó la consola y el comando mkdir para crear nuestra carpeta "EnsaladaWandorf2.0".

<img width="774" height="467" alt="WhatsApp Image 2026-04-22 at 17 57 47" src="https://github.com/user-attachments/assets/8335f744-7f34-4ed2-8ee3-752399915c29" />


## Parte 3
En la interfaz de WireShark podemos ver la metadata, es decir IPs de origen y destino, puertos, tamaño de los paquetes y versión del SSH. Por otro lado, el contenido de los datos es inaccesible debido a que el SSH utiliza el cifrado de extremo a extremo, cuya finalidad es justamente proteger la integridad y confidencialidad de la sesión frente a algun tipo de ataque.

<img width="1302" height="602" alt="ce47481a-fea8-4ec7-9d8a-b44613537ce2" src="https://github.com/user-attachments/assets/b23ac037-fddc-45b2-a313-bdaab23131dd" />

## Parte 4
### 4.a
Se observa la comunicación mediante el protocolo TCP. A diferencia del protocolo SSH, TCP no implementa capas de cifrado por si solo. Se realiza un handshake para establecer la sesión antes de enviar algun dato. Se observa que el mensaje no está cifrado y el mensaje se puede leer. 
<img width="1285" height="141" alt="Screenshot from 2026-04-22 18-32-08" src="https://github.com/user-attachments/assets/279648cb-73e4-46a2-9c03-b0698c1bbb44" />


<img width="1304" height="551" alt="image" src="https://github.com/user-attachments/assets/16ded297-7300-49a5-9cd1-47b18f3ce1b3" />

### 4.b
Se configuró un chat bidireccional con el protocolo UDP. Se utilizó el comando ncat -u para escuchar y enviar mensajes. En WireShark vemos que no hay handshake, característica propia del protocolo UDP. Los mensajes, al igual que en TCP, viajan como texto plano, siendo legibles.
<img width="1171" height="547" alt="47e70ddc-0dc7-47e9-8ede-28d071d2dcc5" src="https://github.com/user-attachments/assets/677cb69a-3476-4585-8623-2a8017c99047" />


<img width="1306" height="563" alt="image" src="https://github.com/user-attachments/assets/df452260-0a31-4eed-bf26-c4e975b6c38b" />


<img width="1306" height="563" alt="image" src="https://github.com/user-attachments/assets/f8973ebf-9e78-4f14-a95c-dc4843c797a4" />

### 4.c
Por último se estableció una sesión de chat entre dos máquinas virtuales independientes, en este caso pc-alumnos-1 y pc-alumnos-4. Una de las máquinas actuó como servidor escuchando el puerto 8080 y la otra inició la conexión apuntando a la IP correspondiente. Se logra ver la ida y vuelta de mensajes, confirmando que la comunicación se estableció de manera efectiva.
<img width="1160" height="452" alt="Screenshot from 2026-04-22 18-16-48" src="https://github.com/user-attachments/assets/0d89373a-d0b9-475c-a1bf-df6a05aaef9c" />


<img width="1171" height="547" alt="Screenshot from 2026-04-22 18-25-30" src="https://github.com/user-attachments/assets/87c02a53-0e3f-4d4c-a86f-3fb4246ff9ca" />


<img width="1285" height="141" alt="Screenshot from 2026-04-22 18-32-08" src="https://github.com/user-attachments/assets/56ee9251-2066-417c-8d02-95c688f01c44" />

### 5
En esta actividad se capturó la interacción entre el cliente y el servidor utilizando el protocolo HTTP. A diferencia del protocolo SSH, este es un protocolo que transmite la información sin cifrar por ende lo podemos ver en WireShark sin problema.
<img width="1298" height="682" alt="image" src="https://github.com/user-attachments/assets/d9e416bd-d7dc-4925-847e-af81f90b8b68" />

### 6.a Relación con los TPs

El ataque de "Man-in-the-Middle" (MitM) realizado al iPhone se conecta directamente con los pilares que hemos trabajado en clase:

#### TP N°1: Manipulación de Bits y el Rol del "Salto" (Hop)

- **Modificación de la Payload:** En la Parte 2 del TP1, realizamos ejercicios de inyección de errores modificando bits de la payload para probar técnicas de detección (EDAC). El hack de Veritasium hace exactamente eso:
  - Cambian un bit específico (de 0 a 1) para engañar al teléfono y que crea que es una transacción "offline".
  - Cambian otro bit para marcar una transacción de $10,000 como de "bajo valor".

- **Comportamiento Hop-by-Hop:** En el TP1 analizamos cómo los routers procesan los paquetes en cada salto. Aquí, el dispositivo Proxmark y la laptop actúan como "nodos" o saltos maliciosos intermedios que decodifican, modifican y vuelven a encapsular la información antes de enviarla al destino final (el lector de tarjetas).

#### TP N°2: Comunicación Cliente-Servidor y Herramientas de Red

- **Flujo de Datos:** El uso de un script de Python para retransmitir datos entre el teléfono "víctima" y el lector es conceptualmente idéntico a lo que hicimos con Netcat en el TP2 para establecer un chat bidireccional. El atacante establece un "puente" de comunicación donde el cliente (iPhone) cree que habla con un servidor (Lector), pero hay un intermediario procesando los mensajes.

#### TP N°3: Criptografía, Wireshark y el dilema de la Seguridad

- **Captura de Tráfico (Wireshark):** En el TP3 usamos Wireshark para intentar "ver" qué hay dentro de un paquete. Los investigadores del video deben haber hecho algo parecido en el Metro de Londres para "escanear los códigos" que las terminales enviaban a los teléfonos.

- **Autenticación vs. Cifrado:** El video explica que el hack es posible porque la comunicación NFC no está cifrada (por razones de compatibilidad). Esto es lo opuesto a lo que vimos con SSH en el TP3: mientras que en SSH el contenido es ilegible sin la clave, en el protocolo de Visa/Apple Pay los datos viajan "en claro", permitiendo que el atacante lea y modifique los bits de control.

- **Claves Públicas y Privadas (RSA):** El video menciona que MasterCard evita este ataque usando firmas digitales (RSA). En el TP3 estudiamos que las claves públicas/privadas sirven para garantizar que un mensaje no fue alterado. El hack de Visa funciona porque el lector no verifica la firma digital de la transacción cuando está online, omitiendo el paso de seguridad que estudiamos en la teoría de SSH.

### 6.b Consideraciones sobre Confidencialidad y Resultados del Laboratorio

Basándonos en el Principio de Confidencialidad y lo aprendido en nuestros laboratorios, debemos tener en cuenta los siguientes puntos críticos:

1. **La falacia de la "seguridad por oscuridad":** El video demuestra que confiar en que un protocolo es "complejo" o "propietario" no garantiza confidencialidad. Al igual que en el TP3 vimos que el tráfico Telnet o HTTP simple puede ser capturado, cualquier protocolo que no implemente cifrado de extremo a extremo (como el NFC de este caso) es vulnerable a la intercepción.
2. **Integridad como requisito de la Confidencialidad:** Un resultado clave de nuestro laboratorio (especialmente TP1 y TP3) es que la confidencialidad no sirve de nada si no hay Integridad. En el video, el atacante puede no saber quién es el dueño del teléfono, pero al poder alterar el mensaje (integridad), rompe la seguridad del sistema. Si los datos estuvieran firmados digitalmente (como las claves de SSH), cualquier cambio en un solo bit invalidaría la transacción.
3. **El riesgo de la "Compatibilidad hacia atrás":** El video menciona que la información se envía sin cifrar para ser compatible con miles de dispositivos viejos. 

En el TP3, al intentar descifrar un paquete SSH, confirmamos que sin la clave privada, el contenido es ruido. La recomendación técnica (y lo que Apple/Visa deberían corregir) es forzar el uso de esa criptografía asimétrica que estudiamos, eliminando los modos "relajados" de verificación que permiten las mentiras del atacante.

En resumen, el hack es una demostración de que, aunque tengamos hardware avanzado (iPhone con FaceID), si los protocolos de red subyacentes permiten el envío de datos sin cifrar y sin verificación de firma (como vimos que sí hace SSH), la seguridad física puede ser totalmente bypassada por un ataque en la capa de comunicación.
