import cv2

print("Iniciando prueba de cámara para ArgosIA...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
else:
    print("¡Cámara abierta con éxito! Presioná Ctrl+C en la terminal para salir.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("No se pudo leer el fotograma.")
            break
        
        # Mostramos la ventana de video
        cv2.imshow("ArgosIA - Deteccion de Movimiento", frame)
        
        # Si presionan la tecla 'q', salimos del bucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
