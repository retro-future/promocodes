from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from promocodes.promo_code import PromoCodesContext


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('check', type=str, help="Pass the code to check if it's exists", )

    def handle(self, *args, **kwargs):
        code = kwargs['check']
        PromoCodesContext().check(code)

