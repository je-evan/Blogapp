from django.views.generic import View
from django.shortcuts import render
from .password_generator import GeneratePassword
from .json2csv import json2csv
from django.contrib import messages
from .download import download_file
from .html2pdf import html2pdf


class PasswordGeneratorView(View):
    template_name = "password_generator.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        length = int(request.POST.get("length"))
        generate_password = GeneratePassword(char_length=length)
        return render(request, self.template_name, {"password": generate_password.generate()['password']})


class FileConverterView(View):
    template_name = "file_converter.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        converter_type = request.POST.get("type")
        print(converter_type)
        file = request.FILES.get("file")
        try:
            if converter_type:
                if converter_type == "json2csv":
                    output_file = json2csv(file)
                elif converter_type == "html2pdf":
                    output_file = html2pdf(file)
                return download_file(output_file)
            else:
                messages.warning(self.request, 'choose converter type first')
        except Exception as e:
            messages.warning(self.request, 'error while converting file')
            print("Error while converting json file to csv:", e)
        return render(request, self.template_name)
