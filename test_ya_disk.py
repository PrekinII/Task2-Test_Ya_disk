import pytest
import requests
from connection import URL, headers


@pytest.fixture()
def fix_path():
    params = {'path': "Нетология"}
    response = requests.get(URL, headers=headers, params=params)
    if response == 404:
        requests.put(URL, headers=headers, params=params)
        return

@pytest.mark.usefixtures
@pytest.mark.parametrize("name_path, result", [("Нетология", 200),
                                               ("Netology", 404)])
def test_check_path(name_path, result, fix_path):
    params = {'path': name_path}
    response = requests.get(URL, headers=headers, params=params)
    print(response)
    assert response.status_code == result


@pytest.mark.parametrize("name_path, result", [("Нетология", 204),
                                               ("Netology", 404)])
def test_del_path(name_path, result):
    params = {'path': name_path}
    response = requests.delete(URL, headers=headers, params=params)
    print(response)
    assert response.status_code == result


@pytest.mark.parametrize("name_path, result", [("Нетология", 201)])
def test_put_path(name_path, result):
    params = {'path': name_path}
    response = requests.put(URL, headers=headers, params=params)
    print(response)
    assert response.status_code == result

if __name__ == '__main__':
    fix_path()