# La_Casa_De_Papel

![prof]()

To see what this repo can do just decrypt the Readme from the next paragraph onwards. Instructions for decryption can be found somewhere in the code :P

El profesor es una de las personas más inteligentes. Él ha estado planeando el robo durante meses. Tokio, Nairobi, Río, Moscú, Denver, Helsinki, Oslo y Berlín son los que estarán dentro de la casa de moneda real y el profesor estará en una casa de seguridad cerca donde usará el disfraz de un fabricante de sidra como tapadera. Ahora el profesor necesita 2 formas de redes separadas. En primer lugar, una conexión confiable y persistente para negociar con el inspector Raquel Murillo y, en segundo lugar, una red poco confiable pero segura para comunicarse con el equipo.

Para negociar necesita una red confiable, por lo que nuestra elección obvia será una conexión TCP a través de sockets. Como no se requiere cifrado, podemos usar una conexión TCP básica.

Para la conexión con el equipo, dado que requerimos una red no confiable pero segura, podemos optar por UDP pero con algún tipo de cifrado. Si el profesor decide una transmisión de paquetes UDP cifrada AES, su trabajo puede hacerse. La clave ya se puede intercambiar para cifrar y descifrar el mensaje. Como son los únicos que conocen la clave (intercambiada de antemano), no será necesario el método de intercambio de claves. Ahora el profesor puede intercambiar mensajes a través de mensajes de audio junto con capas para ocultar la voz real. Dado que los mensajes de audio son medios, UDP sería una combinación perfecta. Esto garantizará una entrega segura incluso cuando la señal sea débil, incluso si la calidad de la llamada disminuye.

Ahora, incluso si alguien intenta capturar la conversación entre el profesor y su equipo, solo recibirá mensajes cifrados que solo el profesor y su equipo pueden descifrar.

Incluso si alguien intenta capturarlo, tendrá: IP de origen, IP de destino, protocolo, longitud, puerto, pero aún no recibirá el mensaje.
Tendrán algunos otros detalles, como el tamaño del marco y todo, pero nada que pueda dañar al profesor.

Ahora, como puede ver, la suma de verificación no está verificada, ya que es un protocolo UDP. Se puede ver la longitud de los datos. Además, dado que el profesor utiliza el cifrado AES, debe asegurarse de antemano de que la clave es un múltiplo de 16 bits (que solo él y su equipo pueden saber). 

Now you can understand what the code is about and what it can do. Good job professor !