import time

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def user_data(key):
    data = {
        "userid": "wangwu",
        "name": "王五",
        "alias": "jackzhang",
        "mobile": "13800000010",
        "department": "1",
        "order": "",
        "position": "测试经理",
        "gender": "1",
        "email": "wangwu@gzdev.com",
        "is_leader_in_dept": "1",
        "enable": "1",
        "avatar_mediaid": "",
        "telephone": "020-123456",
        "address": "广州市海珠区新港中路",
        "main_department": "1"
    }
    if key == 'all':
        return data
    else:
        data = data[key]
        return data


def department_data(key):
    data = {
        "name": "广州研发中心",
        "name_en": "RDGZ",
        "parentid": 1,
        "order": 1,
        "id": 2
    }
    if key == 'all':
        return data
    else:
        data = data[key]
        return data


def tag_data(key):
    data = {
        "tagname": "UI",
        "tagid": 1
    }
    if key == 'all':
        return data
    else:
        data = data[key]
        return data
