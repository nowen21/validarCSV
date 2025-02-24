import csv
from django.shortcuts import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .forms import CargarArchivoCSV


def index(request):
    context = {
        'class': 'fixed-top',
        'principal': False,
        'classbody': 'index-page',
        'page_title': 'Blog'
       
    }
    # sticky-top
    return render(request,'index.html',context)

def pruetecn(request):
    result = None
    if request.method=='POST':
        form = CargarArchivoCSV(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file, delimiter=',')
            row_number = 0
            error_found = False
            error_msg = ""
            for row in reader:
                row_number += 1
                # Validar número de columnas
                if len(row) != 5:
                    error_msg = f"Error en fila {row_number}: se encontraron {len(row)} columnas en lugar de 5."
                    error_found = True
                    break

                # Columna 1: Números enteros entre 3 y 10 caracteres
                col1 = row[0].strip()
                if not col1.isdigit() or not (3 <= len(col1) <= 10):
                    error_msg = f"Error en fila {row_number}, columna 1: debe ser un entero de 3 a 10 dígitos."
                    error_found = True
                    break

                # Columna 2: Correo electrónico
                col2 = row[1].strip()
                try:
                    validate_email(col2)
                except ValidationError:
                    error_msg = f"Error en fila {row_number}, columna 2: correo electrónico inválido."
                    error_found = True
                    break

                # Columna 3: Solo valores "CC" o "TI"
                col3 = row[2].strip()
                if col3 not in ["CC", "TI"]:
                    error_msg = f"Error en fila {row_number}, columna 3: debe ser 'CC' o 'TI'."
                    error_found = True
                    break

                # Columna 4: Valores entre 500000 y 1500000
                col4 = row[3].strip()
                try:
                    col4_value = int(col4)
                    if not (500000 <= col4_value <= 1500000):
                        error_msg = f"Error en fila {row_number}, columna 4: debe estar entre 500000 y 1500000."
                        error_found = True
                        break
                except ValueError:
                    error_msg = f"Error en fila {row_number}, columna 4: debe ser un número entero."
                    error_found = True
                    break

                # Columna 5: Se acepta cualquier valor (no se valida)
            
            if error_found:
                result = error_msg
            else:
                result = "Archivo validado."
    else:
        form = CargarArchivoCSV()

    context = {
    'class': 'sticky-top',
    'principal': True,
    'classbody': 'blog-page', 
    'page_title': 'Prueba Técnica',
    'form': form,
    'result': result,
    }
    return render(request,'pruetecn.html',context)

    #return render(request, 'upload_csv.html', {'form': form, 'result': result})






