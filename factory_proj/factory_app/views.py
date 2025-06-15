from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from .models import Method, Man, Machine, Material

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.views import View
from .forms import CustomUserCreationForm


# Home page

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["methods"] = Method.objects.all()
        context["machines"] = Machine.objects.all()
        context["materials"] = Material.objects.all()
        return context
    
# Signup page

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('login')


# method views


class MethodListView(LoginRequiredMixin, ListView):
    model = Method
    template_name = 'method/methodList.html'
    context_object_name = 'methods'

    def get_queryset(self):
        queryset = Method.objects.all()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset



class MethodCreateView(LoginRequiredMixin,CreateView):
    model = Method
    fields = ['name', 'description']
    template_name = 'method/addMethod.html'
    success_url = reverse_lazy('method-list')

class MethodUpdateView(LoginRequiredMixin,UpdateView):
    model = Method
    fields = ['name', 'description']
    template_name = 'method/addMethod.html'
    success_url = reverse_lazy('method-list')

class MethodDeleteView(LoginRequiredMixin, DeleteView):
    model = Method
    success_url = reverse_lazy('method-list')

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(self.success_url)


# machine viewsss

class MachineListView(LoginRequiredMixin, ListView):
    model = Machine
    template_name = 'machine/machineList.html'
    context_object_name = 'machines'

class MachineCreateView(LoginRequiredMixin, CreateView):
    model = Machine
    fields = ['name', 'machine_id', 'type', 'status']
    template_name = 'machine/addMachine.html'
    success_url = reverse_lazy('machine-list')

class MachineUpdateView(LoginRequiredMixin, UpdateView):
    model = Machine
    fields = ['name', 'machine_id', 'type', 'status']
    template_name = 'machine/addMachine.html'
    success_url = reverse_lazy('machine-list')

class MachineDeleteView(LoginRequiredMixin, DeleteView):
    model = Machine
    success_url = reverse_lazy('machine-list')

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(self.success_url)


# material views
class MaterialListView(LoginRequiredMixin, ListView):
    model = Material
    template_name = 'material/materialList.html'
    context_object_name = 'materials'

class MaterialCreateView(LoginRequiredMixin, CreateView):
    model = Material
    fields = ['name', 'material_id', 'category']
    template_name = 'material/addMaterial.html'
    success_url = reverse_lazy('material-list')

class MaterialUpdateView(LoginRequiredMixin, UpdateView):
    model = Material
    fields = ['name', 'material_id', 'category']
    template_name = 'material/addMaterial.html'
    success_url = reverse_lazy('material-list')

class MaterialDeleteView(LoginRequiredMixin, DeleteView):
    model = Material
    success_url = reverse_lazy('material-list')

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(self.success_url)




