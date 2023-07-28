* Tutorial de uso FastAPI
Una de las formas para correr una aplicación *FastAPI* usando un sevidor es con el comando: 

> uvicorn main:app

sin embargo para cada cambio se tendria que volver inicializar el servidor, esto se evita agregando lo siguiente: 

> uvicorn main:app --reload