from pdfkit import from_file
from django.conf import settings
from os.path import splitext, join
from django.core.files.storage import FileSystemStorage
from os import remove


def html2pdf(html_file):
    options = {
        'page-size': 'A4',
        'margin-top': '0.3in',
        'margin-right': '0in',
        'margin-bottom': '0.5in',
        'margin-left': '0in',
    }
    FileSystemStorage(location=settings.MEDIA_ROOT).save(html_file.name, html_file)
    input_file = join(settings.MEDIA_ROOT,html_file.name)
    output_file = join(settings.MEDIA_ROOT, splitext(html_file.name)[0]  + ".pdf")
    with open(input_file) as file:
        from_file(file, output_file, options=options)
    remove(input_file)
    return output_file