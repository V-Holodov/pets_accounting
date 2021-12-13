from rest_framework import mixins, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView

from api.models import Pet, PetPhoto
from api.serializers import PetSerializer, PetPhotoSerializer, PhotoLoadSerializer, IdsSerializer


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
        

    # @action(detail=False, methods=['delete'])
    # def bulk_destroy(self, request, format=None):
    #     serializer = IdsSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     data = serializer.validated_data
    #     orders_ids = data.get("ids")
        # try:
        #     response = order_manager.delete_orders_by_ids(orders_ids)
        #     if "errors" in response:
        #         raise CustomError(
        #             detail=response.get("errors"),
        #             status_code=response.get("status"),
        #         )
        # except Exception:
        #     raise
        # return_dict = {"message": response.get("message")}
        # return Response(return_dict, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def photo(self, request, pk=None,  format=None):
        pet = get_object_or_404(Pet, pk=pk)
        serializer = PhotoLoadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        pet_photo = PetPhoto.objects.create(photo=serializer.validated_data['file'], pet=pet)
        photo = get_object_or_404(PetPhoto, id=pet_photo.id)
        return Response(PetPhotoSerializer(photo).data)

class OrderListDeleteView(APIView):
    """Удаление списка заказов по списку идентификаторов."""

    def delete(self, request, format=None):
        serializer = IdsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        ids = data.get("ids")
        try:
            for id in ids:
                
        except Exception:
            raise
        return_dict = {"message": response.get("message")}
        return Response(status=status.HTTP_200_OK)