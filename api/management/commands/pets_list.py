import io

from django.core.management.base import BaseCommand
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from api.models import Pet
from api.serializers import PetSerializer


class Command(BaseCommand):
    """Uploading pets from the command line to stdout in JSON format."""

    help = "Displaying a list of pets in stdout"

    def add_arguments(self, parser):
        parser.add_argument(
            "--has-photos",
            action="store_true",
            help="Returns entries with photos"
        )

    def handle(self, *args, **kwargs):
        has_photos = kwargs["has_photos"]

        if has_photos:
            pets = Pet.objects.filter(photos__isnull=False)
        else:
            pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        stream = io.BytesIO(JSONRenderer().render(serializer.data))
        data = {"pets": JSONParser().parse(stream)}
        self.stdout.write(f"{data}")
