from django.shortcuts import render
from django.views import View

from .forms import RegisterForm


# Create your views here.

class RegisterView(View):
    form_class = RegisterForm
    template_name = 'users/signup.html'

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        ...
