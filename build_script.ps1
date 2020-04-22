$zip_folder = mkdir ("build" + " " +($(get-date -f MM-dd-yyyy-HH-mm-ss)))
Move-Item -Path "dist/app.exe" -Destination $zip_folder
Compress-Archive -Path $zip_folder -DestinationPath $zip_folder
jfrog rt u "build*.zip" generic-local
