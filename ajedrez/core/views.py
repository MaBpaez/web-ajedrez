from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mass_mail
from django.utils import timezone
from django.conf import settings
from .models import Torneo
from .forms import TournamentRegistrationForm

import requests


def home(request):

    return render(request, 'core/agenda2.html')


def agenda(request):
    """¿crear manager personalizados?"""

    # torneos_nuevos = Torneo.objects.filter(status='nuevo')
    # torneos_finalizados = Torneo.objects.filter(status='finalizado')
    # torneos_curso = Torneo.objects.filter(status='en curso')
    # utilizamos date para comprobar solo fechas con el formato Y-m-d
    # Refe:https://docs.djangoproject.com/en/3.2/ref/models/querysets/#date

    torneos = Torneo.objects.all()
    torneos_nuevos = Torneo.objects.filter(
        start__date__gt=timezone.now().strftime('%Y-%m-%d')
    )
    torneos_curso = Torneo.objects.filter(
        start__date__lte=timezone.now().strftime('%Y-%m-%d'),
        finish__date__gte=timezone.now().strftime('%Y-%m-%d'),
    )
    torneos_finalizados = Torneo.objects.filter(
        finish__date__lt=timezone.now().strftime('%Y-%m-%d')
    )

    return render(
        request,
        'core/agenda.html',
        {
            'torneos': torneos,
            'torneos_nuevos': torneos_nuevos,
            'torneos_curso': torneos_curso,
            'torneos_finalizados': torneos_finalizados,
        },
    )


def torneo_detail(request, year, month, day, torneo):
    torneo = get_object_or_404(
        Torneo, slug=torneo, publish__year=year, publish__month=month, publish__day=day
    )
    allow_registration = False
    submitted_form = False

    if not torneo.quantity and not torneo.registre:  # organiza delegación y no aforo
        allow_registration = False
    elif timezone.now().strftime('%Y-%m-%d') >= torneo.end_registration.strftime(
        '%Y-%m-%d'
    ):  # para todos organize quien organize
        allow_registration = False
    elif torneo.quantity and not torneo.registre:  # organiza delegación y hay aforo
        allow_registration = True
    elif not torneo.quantity and torneo.registre:
        # organiza 3 parte y fecha actual < fecha fin registro
        allow_registration = True

    if request.method == 'POST':
        form = TournamentRegistrationForm(request.POST)
        # print(request.POST)

        if form.is_valid():
            '''reCAPTCHA validation'''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response,
            }
            r = requests.post(
                'https://www.google.com/recaptcha/api/siteverify', data=data
            )
            result = r.json()

            print(result)

            ''' if reCAPTCHA returns True '''
            if result['success']:
                print('FORMULARIO ENVIADO CON EXITO')
                new_tournamentregistration = form.save(commit=False)
                new_tournamentregistration.tournament = torneo
                # new_tournamentregistration.status = request.POST.get('status')
                new_tournamentregistration.save()

                torneo.quantity = torneo.quantity - 1  # update
                torneo.save()
                # print('Torneo despues de grabar', torneo.quantity)

                # envio correo electronico a la delegación y al registrado
                # para ello utilizaremos send_mass_mail()
                # https://docs.djangoproject.com/en/3.2/topics/email/#send-mass-mail
                cd = form.cleaned_data

                message1 = (
                    'Inscripción en torneo',
                    f"Enhorabuena {cd['name']} te has registrado en el torneo {torneo.title}",
                    'info@ajedrezmalaga.org',
                    [f"{cd['mail']}"],
                )
                message2 = (
                    'Inscripción en torneo',
                    f"{cd['name']} {cd['surnames']} se ha registrado en el torneo {torneo.title}",
                    'info@ajedrezmalaga.org',
                    ['admin@ajedrezmalaga.org'],
                )

                send_mass_mail((message1, message2), fail_silently=False)

                submitted_form = True
                form = TournamentRegistrationForm()  # borrar campos crear form nuevo
    else:
        form = TournamentRegistrationForm()

    return render(
        request,
        'core/torneo-detail.html',
        {
            'torneo': torneo,
            'allow_registration': allow_registration,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
            'form': form,
            'submitted_form': submitted_form,
        },
    )
