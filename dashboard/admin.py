from django.contrib import admin, messages
from openpyxl import load_workbook
from .models.evento import Evento, tipo_de_evento
import os


def get_cell(sheet, column, row):
    value = sheet["{}{}".format(str(column), str(row))].value
    if type(value) == str:
        return value.strip()
    return value


class EventoAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'tipo', 'risco', 'oportunidades', 'ocorrencias', 'ponto', 'lower', 'upper'
    list_filter = 'tipo',
    actions = 'importar_planilha',

    def importar_planilha(modeladmin, request, queryset):
        path = 'dashboard/exames.xlsx'
        if os.path.exists(path):
            workbook = spreadsheet = load_workbook('dashboard/exames.xlsx', data_only=True)
            sheet = workbook.active
            count = 0
            errors = 0
            row = 2
            for i in range(200):
                nome = get_cell(sheet, 'A', row)
                tipo = get_cell(sheet, 'B', row)
                risco = get_cell(sheet, 'C', row)
                oportunidades = get_cell(sheet, 'D', row)
                ocorrencias = get_cell(sheet, 'E', row)
                ponto = get_cell(sheet, 'F', row)
                upper = get_cell(sheet, 'G', row)
                lower = get_cell(sheet, 'H', row)

                if nome:
                    try:
                        tipo_de_evento_reversed = dict(map(reversed, tipo_de_evento))
                        found = list(filter(lambda key: key.lower() == tipo.lower(), tipo_de_evento_reversed.keys()))
                        if found:
                            tipo = tipo_de_evento_reversed.get(found[0])
                        else:
                            tipo = 'EXAME'

                        ponto = float(ponto.split('(', 1)[0].strip())
                        upper = float(upper.split('(', 1)[1].split('-')[0].strip())
                        lower = float(lower.split('-', 1)[1].split(')')[0].strip())
                        
                        Evento.objects.create(nome=nome, tipo=tipo, risco=risco,
                                              oportunidades=oportunidades, ocorrencias=ocorrencias, ponto=ponto, upper=upper, lower=lower)
                        count += 1
                    except Exception as e:
                        print(e)
                        errors += 1

                    finally:
                        row += 1
                else:
                    break
            messages.success(request, f'Foram importados {count} eventos. Houveram {errors} erros')
            return
        messages.warning(request, f'O arquivo `{path}` não existe')


admin.site.register(Evento, EventoAdmin)
