from django.urls import path
from .views import Home, CreateUserView, LoginView, VerifyUserView, CatList, CatDetail, FeedingListCreate, FeedingDetail, ToyList, ToyDetail, AddToyToCat, RemoveToyFromCat

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('users/register/', CreateUserView.as_view(), name='register'),
  path('users/login/', LoginView.as_view(), name='login'),
  path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
  path('cats/', CatList.as_view(), name='cat-list'),
  path('cats/<int:id>/', CatDetail.as_view(), name='cat-detail'),
  path('cats/<int:cat_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
  path('cats/<int:cat_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),
  path('toys/', ToyList.as_view(), name='toy-list'),
  path('toys/<int:id>/', ToyDetail.as_view(), name='toy-detail'),
  path('cats/<int:cat_id>/add_toy/<int:toy_id>/', AddToyToCat.as_view(), name='add-toy-to-cat'),
  path('cats/<int:cat_id>/remove_toy/<int:toy_id>/', RemoveToyFromCat.as_view(), name='remove-toy-from-cat'),
]
