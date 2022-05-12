import pytest

from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


# проверка получения 1го курса


@pytest.mark.django_db
def test_get_course(client, course_factory):
    courses = course_factory(_quantity=1)
    course_id = courses[Course.objects.count() - 1].id
    url = f'/api/v1/courses/{course_id}/'
    response = client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert data['id'] == course_id


# проверка получения списка курсов (list-логика)


@pytest.mark.django_db
def test_get_list_course(client, course_factory):
    courses = course_factory(_quantity=10)

    url = f'/api/v1/courses/'
    response = client.get(url)
    data = response.json()

    assert len(data) == len(courses)


# проверка фильтрации списка курсов по id


@pytest.mark.django_db
def test_filter_course_id(client, course_factory):
    count = Course.objects.count()
    courses = course_factory(_quantity=1, name='TestText')
    temp_id = courses[count-1].id
    temp_url = f'/api/v1/courses/?id={temp_id}'

    # Act
    response = client.get(temp_url)
    data = response.json()
    assert response.status_code == 200
    for m in data:
        assert m['id'] == temp_id


@pytest.mark.django_db
def test_filter_by_name(client):

    response = client.get('/api/v1/courses/?name=TestText')
    data = response.json()
    assert response.status_code == 200
    for m in data:
        assert m['name'] == 'TestText'



# тест успешного создания курса
#     здесь фабрика не нужна, готовим JSON-данные и создаем курс



@pytest.mark.django_db
def test_create_json_course(client):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'test text json create'})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1



# тест успешного обновления курса


@pytest.mark.django_db
def test_update_course(client, course_factory):

    count = Course.objects.count()
    courses = course_factory(_quantity=1)
    assert Course.objects.count() == count + 1

    temp_id = courses[count].id
    temp_url = f'/api/v1/courses/{temp_id}/'
    response = client.put(temp_url, data={'name': 'test json update'})

    assert response.status_code == 200



# тест успешного удаления курса


@pytest.mark.django_db
def test_delete_course(client, course_factory):

    count = Course.objects.count()
    courses = course_factory(_quantity=1)
    assert Course.objects.count() == count + 1

    temp_id = courses[count].id
    temp_url = f'/api/v1/courses/{temp_id}/'
    response = client.delete(temp_url)

    assert response.status_code == 204