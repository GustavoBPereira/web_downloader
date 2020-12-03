import os

def get_file_location(response):
    splited_url = response.url.split('/')

    name = splited_url[-1]
    name += '.html' if not name.endswith('.html') else ''
    name = 'index.html' if name == '.html' else name

    folder = ''.join([str(elem) + '/' for elem in splited_url[2:-1]])
    return f'{folder}/{name}'


def static_path(response, static_type):
    splited_url = response.url.split('/')
    root_path = os.path.dirname(os.path.abspath(__file__)) + '/../../' + splited_url[2]
    path = ''.join(f + '/' for f in splited_url[3:-1])
    return f'{root_path}/static_files/{static_type}/{path}'
