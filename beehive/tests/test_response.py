import pytest

from beehive.models import Apiary, BeeHive, BeeFamily, BeeMother


#   path('', IndexView.as_view(), name="home"),
@pytest.mark.django_db
def test_index_view(client):
    response = client.get('/')
    assert response.status_code == 200

#    path('apiary_create/', ApiaryCreateView.as_view(), name="apiary-create-form"),
@pytest.mark.django_db
def test_apiary_create(client):
    response = client.get('/apiary_create/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_apiary_list_view(client, set_up_apiary):
    response = client.get('/apiary_view/')
    apiary = Apiary.objects.all()
    assert response.status_code == 200
    assert len(response.context['apiary']) == 5


@pytest.mark.django_db
def test_apiary_view(client, set_up_apiary):
    apiary = Apiary.objects.first()
    apiary_count = Apiary.objects.count()
    response = client.get(f'/apiary_view/{apiary.id}')
    assert response.status_code == 200
    assert apiary_count == 5
    assert response.context['apiary'] == apiary

@pytest.mark.django_db
def test_beehive_create(client):
    response = client.get('/beehive_create/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_beehive_list_view(client, set_up_beehive):
    response = client.get('/beehive_view/')
    beehive = BeeHive.objects.all()
    assert response.status_code == 200
    assert len(response.context['beehive']) == 5


@pytest.mark.django_db
def test_beehive_view(client, set_up_beehive):
    beehive = BeeHive.objects.first()
    response = client.get(f'/beehive_view/{beehive.id}')
    assert response.status_code == 200


@pytest.mark.django_db
def test_beefamily_create(client):
    response = client.get('/beefamily_create/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_beefamily_view(client, set_up_beefamily):
    response = client.get('/beefamily_view/')
    beefamily = BeeFamily.objects.all()
    assert response.status_code == 200
    assert len(response.context['beefamily']) == 5


@pytest.mark.django_db
def test_beemother_create(client):
    response = client.get('/beemother_create/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_beemother_view(client, set_up_beefamily):
    response = client.get('/beemother_view/')
    beemother = BeeMother.objects.all()
    assert response.status_code == 200
    assert len(response.context['beemother']) == 5


@pytest.mark.django_db
def test_dashboard_view(client):
    response = client.get('/dashboard/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_view(client):
    response = client.get('/login_view/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_user_view(client):
    response = client.get('/add_user/')
    assert response.status_code == 200
