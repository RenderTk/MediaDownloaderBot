# Media Downloader Bot

Un bot de Telegram que permite descargar videos y audios de múltiples plataformas de redes sociales, con API REST incluida y soporte completo para despliegue en Docker.

## 🚀 Funcionalidades

- **Descargas de YouTube**: Videos y audios en la máxima calidad
- **Soporte multi-plataforma**: Instagram y TikTok 
- **API REST**: Endpoint HTTP para integración con otros servicios
- **Despliegue en Docker**: Configuración completa para contenedores
- **Interfaz de Telegram**: Bot interactivo y fácil de usar
- **App móvil**: Aplicación móvil que se integra con la API REST

## 📋 Requisitos

### Software Base
- **Python 3.8+**: Versión mínima recomendada
- **Docker** (opcional): Para despliegue en contenedores
- **FFmpeg**: Debe estar instalado y disponible en el PATH del sistema

### Dependencias
Todas las librerías de Python están especificadas en `requirements.txt` y se instalan automáticamente.

## 🔧 Configuración

### Variables de Entorno

Crea un archivo `.env` en el directorio raíz con las siguientes variables:

```env
# Token del bot de Telegram
BOT_TOKEN=tu_token_de_telegram_aqui (Requerido)

# Configuración del API (Opcional)
API_HOST=0.0.0.0
API_PORT=8002
```

### Obtener Token de Telegram

1. Abre Telegram y busca [@BotFather](https://t.me/BotFather)
2. Envía `/newbot` y sigue las instrucciones
3. Guarda el token proporcionado en tu archivo `.env`

## 🚀 Despliegue

### Desarrollo Local

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/media-downloader-bot.git
   cd media-downloader-bot
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno**
   ```bash
   cp .env.example .env
   # Editar .env con tus valores
   ```

4. **Ejecutar el bot**
   ```bash
   python3 app.py
   ```

### Despliegue con Docker

#### Construir la imagen
```bash
docker build -t media-downloader-bot .
```

#### Ejecutar el contenedor
```bash
docker run -d \
  --name mdw-bot \
  --restart always \
  -e BOT_TOKEN=tu_token_aqui \
  -e API_PORT=8002 \
  -p 8002:8002 \
  media-downloader-bot
```

## 📚 Uso

### Bot de Telegram
1. Busca tu bot en Telegram usando su username
2. Envía `/start` para comenzar
3. Envía `/youtube`, `/instagram` o `/tiktok`
4. Envía un enlace de YouTube, Instagram o TikTok
5. Selecciona el formato deseado (video/audio)
6. Descarga el archivo

### API REST

#### Endpoints disponibles
- `GET /health_check` - Estado del servicio
- `GET /youtube?file_type="video o audio"&url="Url del video"`
- `GET /instagram?url="Url del video"` 
- `GET /tiktok?url="Url del video"`

## 📱 App Móvil

Para una experiencia más completa, también está disponible una aplicación móvil que se integra con la API REST de este bot:

**Repositorio**: [FdDownloaderApp](https://github.com/RenderTk/FdDownloaderApp.git)

La app móvil permite usar todas las funcionalidades del bot desde una interfaz nativa para dispositivos móviles.

---

**⚠️ Disclaimer**: Este bot es para uso educativo y personal. Respeta los términos de servicio de las plataformas y las leyes de derechos de autor de tu jurisdicción.