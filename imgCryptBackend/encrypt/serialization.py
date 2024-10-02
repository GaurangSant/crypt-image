# encrypt/serializers.py
from rest_framework import serializers

# Serializer for encryption (image input)
class ImageEncryptSerializer(serializers.Serializer):
    image = serializers.ImageField()

# Serializer for decryption (encrypted image + key input)
class ImageDecryptSerializer(serializers.Serializer):
    encrypted_image = serializers.CharField()  # This will receive base64 encoded string of the encrypted image
    key = serializers.CharField(max_length=32)  # Key for decryption
