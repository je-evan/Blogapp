from pdfkit import from_file
from django.conf import settings
from os.path import splitext, join
from django.core.files.storage import FileSystemStorage
from os import remove


def html2pdf(html_file):
    FileSystemStorage(location=settings.MEDIA_ROOT).save(html_file.name, html_file)
    input_file = join(settings.MEDIA_ROOT,html_file.name)
    output_file = join(settings.MEDIA_ROOT, splitext(html_file.name)[0]  + ".pdf")
    with open(input_file) as file:
        from_file(file, output_file)
    remove(input_file)
    return output_file