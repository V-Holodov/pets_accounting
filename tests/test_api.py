import tempfile

import pytest

from api.models import Pet, PetPhoto


class TesterPetsRestAPI:
    @pytest.mark.django_db(transaction=True, reset_sequences=True)
    def test_add_pet(self, client):
        """Тестирует добавление питомца."""
        valid_data = {"name": "Testdog", "age": 5, "type": "dog"}
        count_pets_before = Pet.objects.count()
        response = client.post(
            "/api/v1/pets",
            data=valid_data,
        )
        assert response.status_code == 201, (
            "при добавлении питомца"
            f" получен неверный статус код: {response.status_code}"
        )

        count_pets_after = Pet.objects.count()
        assert count_pets_after == count_pets_before + 1, "питомец не добавляется в БД"

        invalid_data = {"name": "Adel", "age": "str", "type": "dog"}
        response = client.post(
            "/api/v1/pets",
            data=invalid_data,
        )
        assert response.status_code == 400, (
            "при добавлении питомца с невалидными данными"
            f" получен неверный статус код: {response.status_code}"
        )

    @pytest.mark.django_db(transaction=True, reset_sequences=True)
    def test_add_photo(self, client):
        """Тестирует добавление фото питомца."""
        count_photo_before = PetPhoto.objects.count()
        with tempfile.NamedTemporaryFile(mode="w+b", suffix=".gif") as img:
            img.write(
                b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9"
                b"\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00"
                b"\x00\x02\x02\x4c\x01\x00\x3b"
            )
            img.seek(0)
            valid_data = {"file": img}
            pet = Pet.objects.create(name="Testdog", age=5, type="dog")
            response = client.post(
                f"/api/v1/pets/{pet.id}/photo",
                data=valid_data,
            )
            assert response.status_code == 200, (
                "при добавлении фото питомца"
                f" получен неверный статус код: {response.status_code}"
            )

        count_photo_after = PetPhoto.objects.count()
        assert (
            count_photo_after == count_photo_before + 1
        ), "фото питомеца не добавляется в БД"

        with tempfile.NamedTemporaryFile(mode="w+b", suffix=".gif") as img:
            img.write(b"Hello world!")
            img.seek(0)
            invalid_data = {"file": img}
            Pet.objects.create(name="Testdog", age=5, type="dog")
            response = client.post(
                f"/api/v1/pets/{pet.id}/photo",
                data=invalid_data,
            )
            assert response.status_code == 400, (
                "при добавлении фото питомца в неправильном формате"
                f" получен неверный статус код: {response.status_code}"
            )

    @pytest.mark.django_db(transaction=True, reset_sequences=True)
    def test_list_pet(self, client):
        """Тестирует получение списка питомцев."""
        response = client.get(
            "/api/v1/pets",
        )
        assert response.status_code == 200, (
            "при добавлении питомца"
            f" получен неверный статус код: {response.status_code}"
        )

    @pytest.mark.django_db(transaction=True, reset_sequences=True)
    def test_delete_pet(self, client):
        """Тестирует удаление питомцев по списку."""
        pet = Pet.objects.create(name="Testdog", age=5, type="dog")
        count_pets_before = Pet.objects.count()
        valid_data = {"ids": [pet.id]}
        response = client.delete(
            "/api/v1/pets",
            data=valid_data,
        )
        assert response.status_code == 200, (
            "при удалении питомца"
            f" получен неверный статус код: {response.status_code}"
        )

        count_pets_after = Pet.objects.count()
        assert count_pets_after == count_pets_before - 1, "питомец не удаляется из БД"
