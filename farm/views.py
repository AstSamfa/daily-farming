from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse

from django.views.generic import (ListView, CreateView,
                                  DetailView, UpdateView, DeleteView)

from .forms import RequisitoForm
from .models import ColeccionCultivo, Cultivo, Requisito, Cuidado


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

    def get_queryset(self):
        user = self.request.user
        return ColeccionCultivo.objects.filter(usuario=user)


class EliminarColeccionCultivo(DeleteView):
    model = ColeccionCultivo
    context_object_name = 'coleccion'
    template_name = 'farm/eliminar_objeto.html'

    def get_success_url(self):
        return reverse('perfil')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Eliminar Cultivo'
        context['objeto'] = 'cultivo'

        return context


class CrearCultivo(CreateView):
    model = Cultivo
    fields = ['nombre_cultivo', 'tipo_alimento', 'tipo_propagacion']
    template_name = 'farm/crear_actualizar_objeto.html'

    def get_success_url(self):
        return reverse('crear-requisito',
                       kwargs={'pk': self.object.coleccioncultivo.id})

    def form_valid(self, form):
        nuevo_cultivo = form.save()
        nuevo_usuario = self.request.user

        coleccion_cultivo = ColeccionCultivo(cultivo=nuevo_cultivo, usuario=nuevo_usuario)
        coleccion_cultivo.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Nuevo Cultivo'
        context['form_title'] = '1. Crear Cultivo'
        context['btn_label'] = 'Siguiente'

        return context


class ActualizarCultivo(UpdateView):
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Actualizar Cultivo'
        context['form_title'] = '1. Actualizar Cultivo'
        context['btn_label'] = 'Siguiente'

        return context


class CrearRequisito(CreateView):
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


class ActualizarRequisito(UpdateView):
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


class CrearCuidado(CreateView):
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


class ActualizarCuidado(UpdateView):
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Actualizar Cuidado'
        context['form_title'] = 'Actualizar Cuidado del Cultivo'
        context['btn_label'] = 'Actualizar'

        return context


class EliminarCuidado(DeleteView):
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Eliminar Cuidado'
        context['objeto'] = 'cuidado'
        context['ccpk'] = self.kwargs['ccpk']

        return context
