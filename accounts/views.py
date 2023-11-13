from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm, ActualizarUsuarioForm, ActualizarPerfilForm


def registrar(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada con éxito. Ahora puedes Iniciar Sesión.')
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'accounts/registrar.html', {'register_form': form, 'title': 'Registro'})


@login_required()
def actualizar_perfil(request):
    if request.method == 'POST':
        user_form = ActualizarUsuarioForm(request.POST, instance=request.user)
        profile_form = ActualizarPerfilForm(request.POST, request.FILES, instance=request.user.perfil)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, 'Datos de la cuenta actualizados con éxito.')
            return redirect('perfil')

    else:
        user_form = ActualizarUsuarioForm(instance=request.user)
        profile_form = ActualizarPerfilForm(instance=request.user.perfil)

    context_form = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'accounts/actualizar_perfil.html', context_form)
