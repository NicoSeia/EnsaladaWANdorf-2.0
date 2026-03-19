## EJERCICIOS

### 2.1

- **Capa de aplicación**
  - El invitado decide qué pizza quiere.
  - El cocinero prepara la pizza según el pedido.
  - Se define qué se quiere hacer, el contenido del pedido.

- **Capa de servicio**
  - El anfitrión toma el pedido del invitado.
  - El encargado de pedidos recibe la solicitud y coordina la preparación
  - Se encargan de gestionar el pedido.

- **Capa de transporte**
  - El pedido se transmite.
  - Se establece una comunicación confiable.
  - Se asegura que el pedido llegue correctamente.

- **Capa física** 
  - Se envía mediante una furgoneta de reparto.
  - La carretera actúa como el medio físico de transmisión.

### 2.2

### a.

IMG

- **Capa de aplicación**
  - Cada primer ministro formula el mensaje en su idioma nativo (chino / francés).

- **Capa de presentacion**
  - Esta capa se encarga de que ambos lados interpreten correctamente el mensaje.
  - Se realiza una traducción intermedia común (inglés).

- **Capa de transporte**
  - Se establece una comunicación telefónica.

- **Capa física** 
  - Medio físico que transporta la señal.

### b.

IMG 

- **Flujo de la conversación**
  - China habla en chino y se traduce a japonés.
  - Se envía a Alemania.
  - En Alemania se traduce a alemán.
  - Se envía a Francia.
  - En Francia se traduce a francés y el primer ministro francés recibe el mensaje.

*El proceso inverso ocurre para la respuesta.*

### 2.3

1. **Sobrecarga:**
   Cada capa añade cabeceras, lo que incrementa el tamaño de los datos transmitidos.

2. **Procesamiento adicional:**
   El paso de datos por múltiples capas implica más operaciones, aumentando el uso de CPU y la latencia.

3. **Ineficiencia en casos específicos:**
   La estricta separación por capas puede impedir optimizaciones globales, ya que cada capa opera con información limitada.

4. **Complejidad de implementación:**
   Aunque conceptualmente ordenado, el modelo puede volverse complejo de implementar.

5. **Latencia acumulada:**
   Cada capa introduce retardos adicionales, lo que puede afectar aplicaciones sensibles al tiempo.

### 2.4

**¿Existe algún protocolo que pueda utilizar el ejército azul para evitar la derrota?**

No, no existe un protocolo que garantice la coordinación perfecta, dado que el canal de comunicación no es fiable. Pero se puede utilizar un enfoque que minimize la incertidumbre a un nivel aceptable.

El comandante azul puede enviar múltiples mensajeros portando el mensaje de ataque, numerados (mensajero 1 de n, 2 de n...), de modo que la probabilidad de que todos sean interceptados sea muy baja. El segundo cuerpo atacará si recibe al menos uno. A su vez, cada confirmación recibida por el primer comandante aumenta su confianza en la coordinación.

Sin embargo, esto no elimina el problema teorico ya que siempre existirá la posibilidad de que uno ataque sin el otro, por que el último mensaje enviado nunca puede ser confirmado con certeza.
En conclusión, el ejército azul no puede garantizar la victoria, pero puede maximizar sus probabilidades de coordinación mediante redundancia y numeración de mensajes.
