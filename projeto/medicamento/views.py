from __future__ import unicode_literals

from django.contrib import messages

from django.shortcuts import redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin, EnfermeiroRequiredMixin

from .models import Medicamento


class MedicamentoListView(LoginRequiredMixin, ListView):
    model = Medicamento
 

class MedicamentoCreateView(LoginRequiredMixin, EnfermeiroRequiredMixin, CreateView):
    model = Medicamento
    fields = ['nome_real', 'nome_fantasia', 'tarja', 'tipo', 'quantidade', 'is_active']
    success_url = 'medicamento_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Medicamento cadastrado com sucesso na plataforma!')
        return reverse(self.success_url)


class MedicamentoUpdateView(LoginRequiredMixin, EnfermeiroRequiredMixin, UpdateView):
    model = Medicamento
    fields = ['nome_real', 'nome_fantasia', 'tarja', 'tipo', 'quantidade', 'is_active']
    success_url = 'medicamento_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Medicamento atualizado com sucesso na plataforma!')
        return reverse(self.success_url) 


class MedicamentoDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Medicamento
    success_url = 'medicamento_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à esse Medicamento, permissão negada!')
        return redirect(self.success_url)