# Power BI Embedded App (Flask)

Este proyecto permite incrustar (embed) un informe de Power BI en una aplicación web desarrollada con Flask, sin necesidad de iniciar sesión (modelo App Owns Data con F64 o Embedded Capacity).

---

## 📁 Estructura

```
powerbi_embed_app/
├── app.py                # Backend Flask que genera el embed token automáticamente
├── .env                  # Variables de entorno (rellenar con tus credenciales)
├── templates/
│   └── index.html        # Página HTML que renderiza el informe incrustado
├── static/
│   └── script.js         # Script JS que incrusta el informe usando Power BI Client SDK
```

---

## ⚙️ Requisitos

- Python 3.8 o superior
- Cuenta en Azure con Power BI Embedded (por ejemplo, F64)
- App registrada en Azure Portal con permisos API para Power BI

---

## 📦 Instalación

1. **Clona o descarga el proyecto**  
   *(si tienes el ZIP, simplemente descomprímelo)*

2. **Instala las dependencias**:

```bash
pip install flask python-dotenv requests
```

3. **Edita el archivo `.env`** con tus datos:

```env
TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
CLIENT_SECRET=tu_client_secret
WORKSPACE_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
REPORT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
DATASET_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

> 📌 Puedes obtener el `DATASET_ID` desde Power BI Service, accediendo al área de trabajo y consultando el dataset vinculado al informe.

---

## 🚀 Ejecutar el proyecto

```bash
python app.py
```

Abre tu navegador en:

👉 [http://localhost:10000](http://localhost:10000)

---

## ❓ ¿Qué hace?

- El backend genera automáticamente un `access_token` de Azure
- Con él, pide un `embed_token` para ver el informe sin login
- El frontend usa ese token para mostrar el informe incrustado

---

## 🛡 Seguridad y duración

- El token se genera en el momento (válido 55 min)
- Si alguien entra más tarde, se genera uno nuevo automáticamente

---

## 🧠 Modelo usado

✅ **App Owns Data** (Embed for your customers)  
Esto permite que cualquier usuario vea el informe sin necesidad de iniciar sesión en Power BI.

---

## 📩 ¿Dudas?

Puedes escribirme directamente o compartir este README con tu equipo técnico.

