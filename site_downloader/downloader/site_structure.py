import os


def create_structure(response):
    pattern = response.url.split('/')
    folder = ''.join([str(elem) + '/' for elem in pattern[2:-1]])
    local_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        os.makedirs(f'{local_dir}/../../{folder}')
    except FileExistsError:
        pass
g