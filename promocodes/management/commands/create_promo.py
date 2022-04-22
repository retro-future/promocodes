from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from promocodes.promo_code import PromoCode, PromoCodesContext


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, help='Indicates the number of codes to be created')
        parser.add_argument('group', type=str, help='Indicates the group of codes to be created')

    def handle(self, *args, **kwargs):
        amount = kwargs['amount']
        group = kwargs['group']
        promo_code = PromoCode(amount, group)
        promo_context = PromoCodesContext()
        promo_context.add(promo_code)
