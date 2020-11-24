import os


def create_structure(response):
    pattern = response.url.split('/')
    local_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        os.makedirs(f'{local_dir}/../../{pattern[2]}')
    except FileExistsError:
        pass
