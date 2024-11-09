from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    # Define required fields
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    
    # Read-only fields
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)