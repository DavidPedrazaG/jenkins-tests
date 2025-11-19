Write-Host "🚀 Levantando Jenkins con Docker..."
docker compose up -d

Write-Host "⏳ Esperando 10 segundos a que el contenedor arranque..."
Start-Sleep -Seconds 10

Write-Host "🔧 Instalando Python dentro del contenedor..."
docker exec -it jenkins bash -c "
    apt-get update &&
    apt-get install -y python3 python3-pip python3-venv
"

Write-Host "🔑 Contraseña inicial de Jenkins:"
docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword

Write-Host ""
Write-Host "✔ Listo. Abre Jenkins en: http://localhost:8080"
Write-Host "👉 Copia la contraseña de arriba para iniciar sesión."
