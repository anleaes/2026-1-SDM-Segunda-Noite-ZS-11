from django.core.management.base import BaseCommand

from notifications.services import generate_system_notifications


class Command(BaseCommand):
    help = 'Gera notificacoes de contratos proximos do fim e pagamentos atrasados.'

    def handle(self, *args, **options):
        created_count = generate_system_notifications()
        self.stdout.write(
            self.style.SUCCESS(f'{created_count} notificacao(oes) criada(s).')
        )
