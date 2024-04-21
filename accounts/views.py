from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from .forms import (
    CustomUserCreationForm,
    UserUpdateForm,
)
from django.contrib.auth import get_user_model
from django.views.generic import (
    DetailView,
    UpdateView,
)
from django.urls import reverse
User = get_user_model()

class UserUpdate(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'accounts/user_edit.html'

    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk': self.kwargs['pk']})
class UserCreateAndLoginView(CreateView):
    form_class = CustomUserCreationForm
    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        raw_pw = form.cleaned_data.get("password1")
        user = authenticate(email=email, password=raw_pw)
        login(self.request, user)
        return response
class UserDetail(DetailView):
    model = User
    template_name = 'accounts/user_detail.html'