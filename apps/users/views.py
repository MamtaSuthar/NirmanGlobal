from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

def register_view(request):
    form = CustomUserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully! Please login.")
        return redirect("login")

    return render(request, "auth/register.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        user = self.request.user

        if user.is_superuser:
            return reverse_lazy('admin:index')  # Django admin dashboard
        else:
            return reverse_lazy('home')  # normal user