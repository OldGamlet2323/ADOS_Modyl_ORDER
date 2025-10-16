from django.shortcuts import render
from .forms import DutyOfficerForm


def duty_schedule_view(request):
    form = DutyOfficerForm()

    # Оновлена структура для бічної панелі


    context = {
        'form': form,
    }
    return render(request, 'api/base.html', context)