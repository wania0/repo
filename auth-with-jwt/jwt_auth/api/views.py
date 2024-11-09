from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

# @api_view(['GET', 'POST'])
# def create_or_get_users(request : Request):
    
#     if request.method == 'GET':
#         data = User.objects.all()
#         users = []
#         for user in data:
#             users.append({
#             "email" : user.email,
#             "username" : user.username,
#             "is_staff" : user.is_staff,
#             "is_superuser" : user.is_superuser
#         })
#         return Response(users)
    
#     if request.method == ['POST']:
        
#         User.objects.create(
#             email="danish@gmail.com", 
#             username="danish", 
#             password=make_password("admin"),
#             is_staff=True,            # Grants access to the admin interface
#             is_superuser=True         # Grants all permissions and unrestricted access
#         )
        
#         # User can only login to the admin, but can only perform actions they have specific permissions for
#         user = User(
#             email="fahad@gmail.com", 
#             username="fahad",
#             is_staff=True              # Grants access to the admin interface, but permissions are needed for specific actions
#         )
#         user.set_password("admin")      # Securely hashes and sets the password
#         user.save()

        
#         # Improper configuration: This user cannot log in to the admin because 'is_staff' is missing
#         User.objects.create(
#             email="shoaib@gmail.com", 
#             username="shoaib", 
#             password=make_password("admin"),
#             is_superuser=True          # Grants all permissions, but without 'is_staff', they cannot log in
#         )
    
#     return Response("success", status=status.HTTP_200_OK)

        
        
@api_view(['GET', 'POST'])
def create_or_get_users(request: Request):
    if request.method == 'GET':
        data = User.objects.all()
        users = []
        for user in data:
            users.append({
                "username": user.username,
                "is_staff": user.is_staff,
                "is_superuser": user.is_superuser
            })
        return Response(users)

    if request.method == 'POST':
        # Get user data from the request body
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        is_staff = request.data.get('is_staff', False)  # Defaults to False if not provided
        is_superuser = request.data.get('is_superuser', False)  # Defaults to False if not provided

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            return Response(f"User '{username}' already exists.", status=status.HTTP_400_BAD_REQUEST)

        # Create the user
        User.objects.create(
            username=username,
            email=email,
            password=make_password(password),
            is_staff=is_staff,
            is_superuser=is_superuser
        )

        return Response(f"User '{username}' created successfully.", status=status.HTTP_201_CREATED)

    return Response("Method not allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def create_or_get_posts(request: Request):
    if request.user.is_authenticated == False:
        return Response("please login")
    
    data = {
        "is_authenticated": request.user.is_authenticated,
        "is_staff": request.user.is_staff,
        "is_superuser": request.user.is_superuser,
        "email": request.user.email,
    }
    return Response(data)


@api_view(['POST'])
def login_view(request: Request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    
    user = authenticate(request , username=username, password=password)
    
    if User is not None:
        refresh_token = RefreshToken.for_user(user)
        return Response({
            "access_token": str(refresh_token.access_token),
            "refresh_token": str(refresh_token)
            }, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)