from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Pet, PetPhoto
from api.serializers import (
    IdsSerializer,
    PetPhotoSerializer,
    PetSerializer,
    PhotoLoadSerializer,
)

ERROR = "Pet with the matching ID was not found."


class PetViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """ViewSet for viewing and editing pets."""

    serializer_class = PetSerializer

    def get_queryset(self):
        queryset = Pet.objects.all()
        has_photos = self.request.query_params.get("has_photos")
        if has_photos == "True":
            queryset = queryset.filter(photos__isnull=False)
        elif has_photos == "False":
            queryset = queryset.filter(photos__isnull=True)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        pets = {"count": queryset.count(), "items": serializer.data}
        return Response(pets, status=status.HTTP_200_OK)

    def destroy(self, request, format=None):
        serializer = IdsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        ids = data.get("ids")
        count_del = 0
        errors = []
        for id in ids:
            try:
                result = Pet.objects.get(id=id)
                result.delete()
                count_del += 1
            except ObjectDoesNotExist:
                error = {"id": id, "error": ERROR}
                errors.append(error)
        return_dict = {"deleted": count_del}
        if errors:
            return_dict["errors"] = errors
        return Response(return_dict)

    @action(detail=True, methods=["post"])
    def photo(self, request, pk=None, format=None):
        pet = get_object_or_404(Pet, pk=pk)
        serializer = PhotoLoadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        pet_photo = PetPhoto.objects.create(
            photo=serializer.validated_data["file"], pet=pet
        )
        photo = get_object_or_404(PetPhoto, id=pet_photo.id)
        return Response(PetPhotoSerializer(photo).data)
