from django.http import HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from .password_generator import GeneratePassword

class PasswordGeneratorView(View):
    template_name = "password_generator.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        length = int(request.POST.get("length"))
        generate_password = GeneratePassword(char_length=length)
        return render(request, self.template_name, {"password": generate_password.generate()['password']})


class FileConverterView(View):
    template_name = "file_convertor.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/success/")

        return render(request, self.template_name, {"form": form})