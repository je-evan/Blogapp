from os.path import exists, basename
from os import remove
from django.http import HttpResponse, Http404
from mimetypes import guess_type

def download_file(file_path):
    if exists(file_path):
        with open(file_path, 'rb') as file:
            file_content = file.read()
        remove(file_path)
        response = HttpResponse(file_content, content_type=guess_type(file_path)[0])
        response['Content-Disposition'] =  'inline; filename=' + basename(file_path)
        return response
    raise Http404