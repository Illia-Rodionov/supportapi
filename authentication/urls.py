from django.urls import path
from authentication.views import (
    UserCrateViews,
    UserDeleteViews,
    UserDetailViews,
    UserUpdateViews,
)

app_name = "authentication"

urlpatterns = [
    path("usercreate/", UserCrateViews.as_view(), name="create_user"),
    path("userupdate/<int:pk>/", UserUpdateViews.as_view(), name="update_user"),
    path("userdetail/<int:pk>/", UserDetailViews.as_view(), name="detail_user"),
    path("userdelete/<int:pk>/", UserDeleteViews.as_view(), name="delete_user"),
]
