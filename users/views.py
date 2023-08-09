import pandas as pd
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from users.forms import UserRegisterForm, FileUploadForm, UserUpdateForm
from users.models import UserUploadedData
from users.validators import validate_file_data


class HomeView(TemplateView):
    template_name = 'users/home.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            data = UserUploadedData.objects.filter(user=self.request.user)
            return render(request, self.template_name, context={'user_uploaded_data': data})
        return redirect('user-login')


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('user-home')
        else:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Your account has been created successfully.')
            return redirect('user-login')
        return render(request, self.template_name, {'form': form})


class UserUpdateView(UpdateView):
    form_class = UserUpdateForm
    template_name = 'users/update_user.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('user-login')
        else:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your details have updated successfully.')
            return redirect('user-update')
        return render(request, self.template_name, {'form': form})


class UploadUserDataView(CreateView):
    form_class = FileUploadForm
    template_name = 'users/file_upload.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})
        return redirect('user-login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, user=self.request.user)
        if form.is_valid():
            errors = validate_file_data(request.FILES)
            if not len(errors):
                form.save()
                messages.success(request, 'File has uploaded successfully.')
                return redirect('user-home')
            form.add_error('file', errors)
            return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})


class UserUploadedBarChartView(DetailView):
    model = UserUploadedData
    template_name = 'users/user_bar_chart.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            data = UserUploadedData.objects.get(id=kwargs["pk"])
            df = pd.read_csv(data.file).head()
            result = df.to_json(orient='records')
            return render(request, self.template_name, context={'chart_data': str(result)})
        return redirect('user-login')


class UserUploadedPieChartView(DetailView):
    model = UserUploadedData
    template_name = 'users/user_pie_chart.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            data = UserUploadedData.objects.get(id=kwargs["pk"])
            df = pd.read_csv(data.file).head()
            result = df.to_json(orient='records')
            return render(request, self.template_name, context={'chart_data': str(result)})
        return redirect('user-login')
