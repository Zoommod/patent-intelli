from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Inicia o processo de coleta e extração de patentes'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Gatilho acionado: O rôbo de extração começará a rodar aqui."))