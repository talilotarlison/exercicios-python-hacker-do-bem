# Encryption Key (16,24, or 32 bytes)
$encryptionKey = [Text.Encoding]::UTF8.GetBytes("MySecretEncryptionKey")

# Text to encrypt
$textToEncrypt = "SENAI 123."

# Convert the text to bytes
$bytesToEncrypt = [Text.Encoding]::UTF8.GetBytes($textToEncrypt)

# Create AES encryption object
$aes = [System.Security.Cryptography.Aes]::Create()
$aes.Mode = [System.Security.Cryptography.CipherMode]::CBC
$aes.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7

$aes = [System.Security.Cryptography.Aes]::Create()

$aes.Mode = [System.Security.Cryptography.CipherMode]::CBC
$aes.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7

# generate a randon IV (initialization Vector)
$aes.GenerateIV()

# create an encryption stream
$encryptor = $aes.CreateEncryptor()

#encrypt the bytes
$encryptedBytes = $encryptor.TransformFinalBlock($bytesToEncrypt, 0, $bytesToEncrypt.Length)

#convert the encrypted bytes to Base64 for storage
$encryptedText = [Convert]::ToBase64String($aes.IV + $encryptedBytes)

#Display the encrypted text
write-host "Encrypted text: $encryptedText"
