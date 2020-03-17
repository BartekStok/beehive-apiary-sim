from unittest import TestCase

import pytest
from django.urls import reverse
from pytest_django.fixtures import client

from beehive.models import Apiary, BeeHive, BeeFamily, BeeMother


# path('', IndexView.as_view(), name="home"),
@pytest.mark.django_db
def test_index_view(client):
    response = client.get('/')
    assert response.status_code == 200


# path('apiary_create/', ApiaryCreateView.as_view(), name="apiary-create-form"),
@pytest.mark.django_db
def test_apiary_create(client):
    response = client.get('/apiary_create/')
    assert response.status_code == 200


# path('apiary_view/', ApiaryListView.as_view(), name="apiary-list-view"),
@pytest.mark.django_db
def test_apiary_list_view(client, set_up_apiary):
    response = client.get('/apiary_view/')
    apiary = Apiary.objects.all()
    assert response.status_code == 200
    assert len(response.context['apiary']) == 5


# path('apiary_view/<int:apiary_id>', ApiaryView.as_view(), name="apiary-view"),
@pytest.mark.django_db
def test_apiary_view(client, set_up_apiary):
    apiary = Apiary.objects.first()
    apiary_count = Apiary.objects.count()
    response = client.get(f'/apiary_view/{apiary.id}')
    assert response.status_code == 200
    assert apiary_count == 5
    assert response.context['apiary'] == apiary


# path('apiary_update/<pk>/', ApiaryUpdateView.as_view(), name="apiary-update-form"),
# @pytest.mark.django_db
# def test_apiary_update_view(client, set_up_apiary):
#     apiary = Apiary.objects.first()
#     response = client.post(
#     assert response.status_code == 302
#     assert response.context['apiary'] == apiary

# @pytest.mark.django_db
# class ApiaryUpdateView(TestCase, client):
#     def test_update_apiary(self):
#         apiary = Apiary.objects.create(name='Moja pasieka', description='Opis', location='lokalizacja', area=51)
#         response = self.client.post(
#             reverse('apiary-update-form', kwargs={'pk': apiary.id}),
#                 {'name': 'Dobra', 'description': 'Opis', 'location': 'lokalizacja', 'area': 51})
#         self.assertEqual(response.status_code, 302)
#
#         apiary.refresh_from_db()
#         self.assertEqual(apiary.name, 'Dobra')


# path('apiary_delete/<pk>/', ApiaryDeleteView.as_view(), name="apiary-delete-form"),
# @pytest.mark.django_db
# def test_apiary_delete_view(client, set_up_apiary):
#     apiary = Apiary.objects.first()
#     response = client.post(f'/apiary_delete/{apiary.id}')
#     assert response.status_code == 200
#     assert response.context['apiary'] == apiary


# path('beehive_create/', BeeHiveCreateView.as_view(), name="beehive-create-form"),
@pytest.mark.django_db
def test_beehive_create(client):
    response = client.get('/beehive_create/')
    assert response.status_code == 200


# path('beehive_view/', BeeHiveListView.as_view(), name="beehive-list-view"),
@pytest.mark.django_db
def test_beehive_list_view(client, set_up_beehive):
    response = client.get('/beehive_view/')
    beehive = BeeHive.objects.all()
    assert response.status_code == 200
    assert len(response.context['beehive']) == 5


# path('beehive_view/<int:beehive_id>', BeeHiveView.as_view(), name="beehive-view"),
@pytest.mark.django_db
def test_beehive_view(client, set_up_beehive):
    beehive = BeeHive.objects.first()
    response = client.get(f'/beehive_view/{beehive.id}')
    assert response.status_code == 200


# path('beehive_update/<pk>', BeeHiveUpdateView.as_view(), name="beehive-update-form"),
# path('beehive_delete/<pk>', BeeHiveDeleteView.as_view(), name="beehive-delete-form"),
# path('beehive_service/<pk>', BeeHiveMakeService.as_view(), name="beehive-make-service"),
# path('beehive_take_honey/<pk>', BeeHiveTakeHoney.as_view(), name="beehive-take-honey"),


# path('beefamily_create/', BeeFamilyCreateView.as_view(), name="beefamily-create-form"),
@pytest.mark.django_db
def test_beefamily_create(client):
    response = client.get('/beefamily_create/')
    assert response.status_code == 200


# path('beefamily_view/', BeeFamilyListView.as_view(), name="beefamily-list-view"),
@pytest.mark.django_db
def test_beefamily_list_view(client, set_up_beefamily):
    response = client.get('/beefamily_view/')
    beefamily = BeeFamily.objects.all()
    assert response.status_code == 200
    assert len(response.context['beefamily']) == 5


# path('beefamily_view/<int:beefamily_id>', BeeFamilyView.as_view(), name="beefamily-view"),
# path('beefamily_update/<pk>', BeeFamilyUpdateView.as_view(), name="beefamily-update-view"),
# path('beefamily_delete/<pk>', BeeFamilyDeleteView.as_view(), name="beefamily-delete-view"),


# path('beemother_create/', BeeMotherCreateView.as_view(), name="beemother-create-form"),
@pytest.mark.django_db
def test_beemother_create(client):
    response = client.get('/beemother_create/')
    assert response.status_code == 200


# path('beemother_view/', BeeMotherListView.as_view(), name="beemother-list-view"),
@pytest.mark.django_db
def test_beemother_list_view(client, set_up_beefamily):
    response = client.get('/beemother_view/')
    beemother = BeeMother.objects.all()
    assert response.status_code == 200
    assert len(response.context['beemother']) == 5


# path('beemother_view/<int:beemother_id>', BeeMotherView.as_view(), name="beemother-view"),
# path('beemother_update/<pk>', BeeMotherUpdateView.as_view(), name="beemother-update-view"),
# path('beemother_delete/<pk>', BeeMotherDeleteView.as_view(), name="beemother-delete-view"),


# path('dashboard/', DashboardService.as_view(), name="dashboard"),
@pytest.mark.django_db
def test_dashboard_view(client):
    response = client.get('/dashboard/')
    assert response.status_code == 200


# path('login_view/', LoginView.as_view(), name="login-view"),
@pytest.mark.django_db
def test_login_view(client):
    response = client.get('/login_view/')
    assert response.status_code == 200


# path('add_user/', AddUserView.as_view(), name="add-user-form"),
@pytest.mark.django_db
def test_add_user_view(client):
    response = client.get('/add_user/')
    assert response.status_code == 200

# path('logout_view/', LogutView.as_view(), name="logout-view"),
