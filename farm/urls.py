from django.urls import path
from .views import (ListadoColeccionesCultivos,
                    ListadoColeccionCultivo, DetallesColeccionCultivo, EliminarColeccionCultivo,
                    CrearCultivo, ActualizarCultivo,
                    CrearRequisito, ActualizarRequisito,
                    CrearCuidado, ActualizarCuidado, EliminarCuidado, )

urlpatterns = [
    path('', ListadoColeccionesCultivos.as_view(), name='farm-cultivos'),

    path('perfil/', ListadoColeccionCultivo.as_view(), name='perfil'),
    path('cultivo/<int:pk>/', DetallesColeccionCultivo.as_view(), name='detalles-cultivo'),
    path('cultivo/eliminar/<int:pk>/', EliminarColeccionCultivo.as_view(), name='eliminar-cultivo'),

    path('cultivo/nuevo/', CrearCultivo.as_view(), name='crear-cultivo'),
    path('cultivo/actualizar/<int:ccpk>/<int:pk>', ActualizarCultivo.as_view(), name='actualizar-cultivo'),

    path('cultivo/nuevo/<int:pk>/requisito/', CrearRequisito.as_view(), name='crear-requisito'),
    path('cultivo/actualizar/<int:ccpk>/requisito/<int:pk>', ActualizarRequisito.as_view(), name='actualizar-requisito'),

    path('cultivo/nuevo/<int:pk>/cuidado/', CrearCuidado.as_view(), name='crear-cuidado'),
    path('cultivo/actualizar/<int:ccpk>/cuidado/<int:pk>', ActualizarCuidado.as_view(), name='actualizar-cuidado'),
    path('cultivo/eliminar/<int:ccpk>/cuidado/<int:pk>', EliminarCuidado.as_view(), name='eliminar-cuidado'),

]
