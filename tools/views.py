from django.views.generic import View
from django.shortcuts import render
from .password_generator import GeneratePassword
from .json2csv import json2csv
from django.contrib import messages
from .download import download_file
from .html2pdf import html2pdf

from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .email import send_email
import json


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


@csrf_exempt
def subscribe(request):
    if request.method == "GET":
        data = {"message": "method not allowed!"}
        return JsonResponse(data, safe=False)

    if (request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
            send_email(name, message, email)
            data = {"message": "Email was sent. I'll contact you back later."}
        except:
            data = {"message": "something went wrong, email was not sent!"}
       
        # send json response with new object
        return JsonResponse(data, safe=False)