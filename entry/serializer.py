from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        print(data)
        token = self.get_token(self.user)
        print(token)
        data['user'] = str(self.user)
        data['id'] = self.user.id
        return data