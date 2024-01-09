from demo.views import create_car

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new_car/', create_car),
]
