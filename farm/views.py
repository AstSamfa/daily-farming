from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse
from django.views.generic import (ListView, CreateView,
                                  DetailView, UpdateView, DeleteView)

from .forms import RequisitoForm, CultivoForm
from .models import ColeccionCultivo, Cultivo, Requisito, Cuidado
from .utils import validar


class ListadoColeccionesCultivos(ListView):
    model = ColeccionCultivo
    template_name = 'farm/colecciones_cultivos.html'
    context_object_name = 'coleccion'
    ordering = ['cultivo__nombre_cultivo']


class ListadoColeccionCultivo(LoginRequiredMixin, ListView):
    model = ColeccionCultivo
    template_name = 'farm/perfil.html'
    context_object_name = 'coleccion'
    ordering = ['cultivo__nombre_cultivo']

    def get_queryset(self):
        user = self.request.user
        return ColeccionCultivo.objects.filter(usuario=user)


class DetallesColeccionCultivo(DetailView):
    model = ColeccionCultivo
    template_name = 'farm/detalles_cultivo.html'
    context_object_name = 'coleccion'

    def test_func(self):
        coleccion = self.get_object()

        return coleccion.usuario == self.request.user


class EliminarColeccionCultivo(LoginRequiredMixin,  UserPassesTestMixin, DeleteView):
    model = ColeccionCultivo
    context_object_name = 'coleccion'
    template_name = 'farm/eliminar_objeto.html'

    def get_success_url(self):
        return reverse('perfil')

    def test_func(self):
        coleccion = self.get_object()

        return coleccion.usuario == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Eliminar Cultivo'
        context['objeto'] = 'cultivo'

        return context


class CrearCultivo(LoginRequiredMixin, CreateView):
    model = Cultivo
    form_class = CultivoForm
    template_name = 'farm/crear_actualizar_objeto.html'

    def get_success_url(self):
        return reverse('crear-requisito',
                       kwargs={'pk': self.object.coleccioncultivo.id})

    def form_valid(self, form):
        nuevo_cultivo = form.save()
        nuevo_usuario = self.request.user

        coleccion_cultivo = ColeccionCultivo(cultivo=nuevo_cultivo, usuario=nuevo_usuario)
        coleccion_cultivo.save()

        departamento = form.cleaned_data['departamento']
        municipio = form.cleaned_data['municipio']
        cultivo = nuevo_cultivo.nombre_cultivo.lower()

        resultado_validacion = validar(departamento, municipio, cultivo)

        if resultado_validacion:
            messages.warning(self.request, f'Según tu zona, la viabilidad del cultivo es: {resultado_validacion}')
        else:
            messages.warning(self.request, f'No se ha encontrado datos para el Departamento y Municipio registrados.'
                                           f' Se sugiere verificar esta información de manera externa.')

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Nuevo Cultivo'
        context['form_title'] = '1. Crear Cultivo'
        context['btn_label'] = 'Siguiente'

        return context


class ActualizarCultivo(LoginRequiredMixin,  UserPassesTestMixin, UpdateView):
    model = Cultivo
    fields = ['nombre_cultivo', 'tipo_alimento', 'tipo_propagacion']
    template_name = 'farm/crear_actualizar_objeto.html'

    def get_success_url(self):
        return reverse('actualizar-requisito',
                       kwargs={'ccpk': self.object.coleccioncultivo.id,
                               'pk': self.object.coleccioncultivo.requisito.id})

    def form_valid(self, form):
        cultivo_actualizado = form.save()

        coleccion_id = self.kwargs['ccpk']
        coleccion_cultivo = ColeccionCultivo.objects.get(id=coleccion_id)

        coleccion_cultivo.cultivo = cultivo_actualizado

        coleccion_cultivo.save()

        return super().form_valid(form)

    def test_func(self):
        coleccion_id = self.kwargs['ccpk']
        coleccion_cultivo = ColeccionCultivo.objects.get(id=coleccion_id)

        return coleccion_cultivo.usuario == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Actualizar Cultivo'
        context['form_title'] = '1. Actualizar Cultivo'
        context['btn_label'] = 'Siguiente'

        return context


class CrearRequisito(LoginRequiredMixin, CreateView):
    model = Requisito
    form_class = RequisitoForm
    template_name = 'farm/crear_actualizar_objeto.html'

    def get_success_url(self):
        return reverse('detalles-cultivo',
                       kwargs={'pk': self.object.coleccioncultivo.id})

    def form_valid(self, form):
        nuevo_requisito = form.save()

        coleccion_id = self.kwargs['pk']
        coleccion_cultivo = ColeccionCultivo.objects.get(id=coleccion_id)

        coleccion_cultivo.requisito = nuevo_requisito

        coleccion_cultivo.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Nuevo Cultivo'
        context['form_title'] = '2. Requisito del Cultivo'
        context['btn_label'] = 'Añadir'

        return context


class ActualizarRequisito(LoginRequiredMixin,  UserPassesTestMixin, UpdateView):
    model = Requisito
    form_class = RequisitoForm
    template_name = 'farm/crear_actualizar_objeto.html'

    def get_success_url(self):
        return reverse('detalles-cultivo',
                       kwargs={'pk': self.object.coleccioncultivo.id})

    def form_valid(self, form):
        requisito_actualizado = form.save()

        coleccion_id = self.kwargs['ccpk']
        coleccion_cultivo = ColeccionCultivo.objects.get(id=coleccion_id)

        coleccion_cultivo.requisito = requisito_actualizado

        coleccion_cultivo.save()

        return super().form_valid(form)

    def test_func(self):
        coleccion_id = self.kwargs['ccpk']
        coleccion_cultivo = ColeccionCultivo.objects.get(id=coleccion_id)

        return coleccion_cultivo.usuario == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Actualizar Requisito'
        context['form_title'] = '2. Actualizar requisito del Cultivo'
        context['btn_label'] = 'Actualizar'

        return context


class CrearCuidado(LoginRequiredMixin, CreateView):
    model = Cuidado
    fields = ['estado_crecimiento', 'descripcion']
    template_name = 'farm/crear_actualizar_objeto.html'

    def get_success_url(self):
        coleccion_id = self.kwargs['pk']
        return reverse('detalles-cultivo',
                       kwargs={'pk': coleccion_id})

    def form_valid(self, form):
        nuevo_cuidado = form.save()

        coleccion_id = self.kwargs['pk']
        coleccion_cultivo = ColeccionCultivo.objects.get(id=coleccion_id)

        coleccion_cultivo.cuidado.add(nuevo_cuidado)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Añadir Cuidado'
        context['form_title'] = 'Añadir Cuidado del Cultivo'
        context['btn_label'] = 'Añadir'

        return context


class ActualizarCuidado(LoginRequiredMixin,  UserPassesTestMixin, UpdateView):
    model = Cuidado
    fields = ['estado_crecimiento', 'descripcion']
    template_name = 'farm/crear_actualizar_objeto.html'

    def get_success_url(self):
        coleccion_id = self.kwargs['ccpk']
        return reverse('detalles-cultivo',
                       kwargs={'pk': coleccion_id})

    def form_valid(self, form):
        nuevo_cuidado = form.save()

        coleccion_id = self.kwargs['ccpk']
        coleccion_cultivo = ColeccionCultivo.objects.get(id=coleccion_id)

        coleccion_cultivo.cuidado.add(nuevo_cuidado)

        return super().form_valid(form)

    def test_func(self):
        coleccion_id = self.kwargs['ccpk']
        coleccion_cultivo = ColeccionCultivo.objects.get(id=coleccion_id)

        return coleccion_cultivo.usuario == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Actualizar Cuidado'
        context['form_title'] = 'Actualizar Cuidado del Cultivo'
        context['btn_label'] = 'Actualizar'

        return context


class EliminarCuidado(LoginRequiredMixin,  UserPassesTestMixin, DeleteView):
    model = Cuidado
    template_name = 'farm/eliminar_objeto.html'

    def get_success_url(self):
        coleccion_id = self.kwargs['ccpk']
        return reverse('detalles-cultivo', kwargs={'pk': coleccion_id})

    def delete(self, request, *args, **kwargs):

        coleccion_id = self.kwargs['ccpk']
        coleccion_cultivo = ColeccionCultivo.objects.get(id=coleccion_id)

        coleccion_cultivo.cuidado = None
        coleccion_cultivo.save()

        return super().delete(request, *args, **kwargs)

    def test_func(self):
        coleccion_id = self.kwargs['ccpk']
        coleccion_cultivo = ColeccionCultivo.objects.get(id=coleccion_id)

        return coleccion_cultivo.usuario == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Eliminar Cuidado'
        context['objeto'] = 'cuidado'
        context['ccpk'] = self.kwargs['ccpk']

        return context
