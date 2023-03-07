from rest_framework_simplejwt.tokens import RefreshToken

#add data in jwt token
def get_custom_jwt_token(user):
    refresh = RefreshToken.for_user(user)

    refresh['id'] = user.id
    refresh['unique_id'] = user.unique_id
    refresh['is_active'] = user.is_active
    refresh['is_admin'] = user.is_admin


    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }