from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('ciclos/',views.listar_ciclos,name='listar_ciclos'),
    path('ciclos/crear',views.crear_ciclo,name='crear_ciclos'),
    path('ciclos/editar/<int:ciclo_id>',views.editar_ciclo,name='editar_ciclo'),
    path('ciclos/eliminar/<int:ciclo_id>',views.eliminar_ciclo,name='eliminar_ciclo'),
    path('ciclos/<int:ciclo_id>/',views.detalles_ciclo,name='detalles_ciclo'),
    path('ciclos/<int:ciclo_id>/agregar-participante/',views.agregar_participante,name='agregar_participante'),
    path('ciclos/<int:ciclo_id>/sortear/', views.sortear_orden, name='sortear_orden'),
    path('ciclos/participante/<int:participante_id>/modificar/', views.modificar_orden, name='modificar_orden'),
    path('ciclos/<int:ciclo_id>/registrar-pago/', views.registrar_pago, name='registrar_pago'),
    path('ciclos/<int:ciclo_id>/reporte_pdf/',views.generar_reporte_pdf, name='reporte_pdf'),
    path('ciclos/<int:ciclo_id>/reporte_excel/',views.generar_reporte_excel, name='reporte_excel'),


    path('participantes/<int:participante_id>/modificar/', views.modificar_orden, name='modificar_orden'),
    path('participantes/<int:participante_id>/eliminar/', views.eliminar_participante, name='eliminar_participante'),

    path('aportes/',views.listar_aportes,name='listar_aportes'),
    path('aportes/crear',views.listar_aportes,name='listar_aportes'),

    path('',views.inicio,name='inicio'),

    #path('login/',auth_views.LoginView.as_view(),name='login'),
    path('login/',auth_views.LoginView.as_view(template_name = 'silva/login.html'),name='login'),
    path('logout/',auth_views.LoginView.as_view(template_name = 'gestion/logout.html'),name='logout'),
    #path('logout/',auth_views.LoginView.as_view(),name='logout'),


]