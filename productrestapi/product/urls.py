from .views import product_list,product_URD,product_mixin_listcreate,product_mixin_retriveupdatedelete
from django.urls import path
urlpatterns=[
    path('prod1/', product_mixin_listcreate.as_view()),#product_list),
    path('prod1/<int:pk>',product_mixin_retriveupdatedelete.as_view())#product_URD)
]