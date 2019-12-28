from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


