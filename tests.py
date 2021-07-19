import requests


def url_for(data):
    siteroot = 'http://127.0.0.1:8000'
    url = f'{siteroot}/{data}'
    print("="*30 + ' ' + url + ' ' + "="*30)
    return url

def generate_student():
    url = url_for('generate-student/')
    r = requests.get(url)
    print(r.request.method, url)
    print(r.text, '\n')

def generate_students(count):
    url = url_for(f'generate-students/')
    data = {'count': count}
    r = requests.post(url, data=data)
    print(r.request.method, url, data)
    print(r.text, '\n')

def generate_teachers(count):
    url = url_for(f'generate-teachers/')
    data = {'count': count}
    r = requests.post(url, data=data)
    print(r.request.method, url, data)
    print(r.text, '\n')

def generate_groups(count):
    url = url_for(f'generate-groups/')
    data = {'count': count}
    r = requests.post(url, data=data)
    print(r.request.method, url, data)
    print(r.text, '\n')

def get_students(**query):
    url = url_for(f'students/')
    r = requests.get(url, data=query)
    print(r.request.method, url, query)
    print(r.text, '\n')

def get_groups(**query):
    url = url_for(f'groups/')
    r = requests.get(url, data=query)
    print(r.request.method, url, query)
    print(r.text, '\n')

def get_teachers(**query):
    url = url_for(f'teachers/')
    r = requests.get(url, data=query)
    print(r.request.method, url, query)
    print(r.text, '\n')

if __name__ == '__main__':
    generate_student()
    generate_students(count=30)
    generate_teachers(count=5)
    generate_groups(count=4)
    get_students()
    get_teachers()
    get_groups()
    