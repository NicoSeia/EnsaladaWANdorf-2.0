import socket
import json

# 3.a) Configuración de IP y Puerto con valores por defecto al presionar Enter
host_input = input("Ingrese la IP del servidor [Por defecto: 127.0.0.1]: ")
HOST = host_input.strip() if host_input.strip() else "127.0.0.1"

port_input = input("Ingrese el puerto del servidor [Por defecto: 5000]: ")
PORT = int(port_input.strip()) if port_input.strip() else 5000

# Configuración del tipo de conexión (Persistente o Única)
print("\nSeleccione el modo de conexión:")
print("1) Conexión única (Enviar un mensaje y cerrar)")
print("2) Conexión persistente (Mantener canal abierto para múltiples mensajes)")
modo = input("Seleccione una opción (1 o 2) [Por defecto: 1]: ").strip()
es_persistente = modo == "2"

# Solicitar el identificador del grupo una sola vez
grupo = input("\nIngrese el nombre de su grupo: ")

if not es_persistente:
    # --- MODO CONEXIÓN ÚNICA ---
    contenido = input("Ingrese el mensaje/payload a enviar: ")
    message = {"group": grupo, "payload": contenido}

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        print(f"[CONECTADO] Enlace único establecido con {HOST}:{PORT}")

        client.sendall(json.dumps(message).encode("utf-8"))
        print("[ENVIADO] Paquete transmitido con éxito.")
    except Exception as e:
        print(f"[ERROR] No se pudo completar la comunicación: {e}")
    finally:
        client.close()
        print("[DESCONECTADO] Conexión finalizada de manera ordenada.")

else:
    # --- MODO CONEXIÓN PERSISTENTE ---
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
        print(f"[CONECTADO] Canal persistente abierto con {HOST}:{PORT}")
        print(
            "Escriba sus mensajes a continuación. Presione CTRL+C para finalizar y salir."
        )
        print("-" * 60)

        while True:
            try:
                contenido = input("\nPayload a enviar > ")
                if not contenido.strip():
                    continue

                # Reutiliza el mismo socket estructurando la morfología JSON requerida
                message = {"group": grupo, "payload": contenido}

                client.sendall(json.dumps(message).encode("utf-8"))
                print("[ENVIADO] Paquete inyectado en el socket activo.")

            except KeyboardInterrupt:
                # Captura el CTRL+C de forma limpia dentro del bucle de envío
                print("\n\n[INTERRUPCIÓN] Detectado CTRL+C por el operador.")
                break

    except Exception as e:
        print(f"[ERROR] Falla en la estructura de la conexión persistente: {e}")
    finally:
        client.close()
        print("[DESCONECTADO] Socket persistente cerrado de forma segura.")
