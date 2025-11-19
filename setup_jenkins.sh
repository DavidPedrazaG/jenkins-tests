#!/bin/bash

echo "🚀 Levantando Jenkins con Docker..."
docker compose up -d

echo "⏳ Esperando 10 segundos a que el contenedor arranque..."
sleep 10

echo "🔧 Instalando Python dentro del contenedor..."
docker exec -it jenkins bash -c "
    apt-get update &&
    apt-get install -y python3 python3-pip python3-venv
"

echo "🔑 Contraseña inicial de Jenkins:"
docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword

echo ""
echo "✔ Listo. Abre Jenkins en: http://localhost:8080"
echo "👉 Copia la contraseña de arriba para iniciar sesión."
