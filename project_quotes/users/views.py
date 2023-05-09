from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import RegisterForm


class RegisterView(View):
    form_class = RegisterForm
    template_name = 'users/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(to="quotes:main")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        print('Hey---------------------------')
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Вітаємо {username}. Ваш акаунт успішно створено!")
            return redirect(to="users:signin")
        return render(request, self.template_name, {"form": form})

# Create your views here.
#
# def signup(request):
#     if request.user.is_authenticated:
#         return redirect(to='quotes:root')
#
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("Save")
#             return redirect(to='quotes:root')
#         else:
#             print("Not Save")
#             return render(request, 'users/signup.html', context={"form": form})
#
#     return render(request, 'users/signup.html', context={"form": RegisterForm()})
#

# def login(request):
#     if request.user.is_authenticated:
#         return redirect(to='quotes:root')
#
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             # form.save()
#             print("login ------------------------------")
#             return redirect(to='quotes:root')
#         else:
#             print("------------------------ Not login")
#             return render(request, 'users/signin.html', context={"form": form})
#
#     return render(request, 'users/signin.html', context={"form": LoginForm()})
