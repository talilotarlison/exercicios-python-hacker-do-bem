$chaveMaliciosa= "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run\EncryptorMalicioso"
if (Test-Path $chaveMaliciosa){
 Write-Host " Removendo chave maliciosa do Registro... "
 Remove-Item -Path $chaveMaliciosa -Force
 Write-Host "Chave maliciosa removida com sucesso."
 }else{
 Write-Host "Nenhuma chave maliciosa encontrada do Registro."}
