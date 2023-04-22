from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from .models import Profile
from .forms import UserForm, ProfilePicForm
from insta_app.models import Post


class ProfileListView(LoginRequiredMixin, View):
    def get(self, request):
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {'profiles': profiles})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.success(request, 'Need to be logged in')
            return redirect('post_list')
        return super().dispatch(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, pk):
        profile = Profile.objects.get(user_id=pk)
        posts = Post.objects.filter(user_id=pk)
        return render(request, 'profile.html', {"profile": profile, "posts": posts})

    def post(self, request, pk):
        current_user_profile = request.user.profile
        profile = Profile.objects.get(user_id=pk)
        action = request.POST['follow']
        if action == 'unfollow':
            current_user_profile.follows.remove(profile)
        elif action == 'follow':
            current_user_profile.follows.add(profile)
        current_user_profile.save()

        return redirect('profile', pk=pk)


class RegisterUserView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You've registered")
            return redirect('post_list')
        return render(request, 'register.html', {'form': form})


class UpdateUserView(LoginRequiredMixin, UpdateView):
    template_name = 'update_user.html'
    model = Profile
    form_class = ProfilePicForm
    success_url = reverse_lazy('post_list')

    def get_object(self):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserForm(instance=self.request.user)
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        user_form = UserForm(self.request.POST, instance=self.request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(self.request, "Updated successfully")
        else:
            messages.error(self.request, "Failed to update")
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, "Failed to update")
        return response


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        messages.success(self.request, "You've Logged In")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Password or Username does not match")
        return super().form_invalid(form)


def logout_user(request):
    logout(request)
    messages.success(request, "You've been Logged Out")
    return redirect('post_list')
