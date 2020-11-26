import os


def static_structure(path_pattern, file_type, local_dir):
    path_folder = ''.join([str(folder) + '/' for folder in path_pattern[1::]])
    try:
        os.makedirs(f'{local_dir}/../../{path_pattern[0]}/static_files/{file_type}/{path_folder}')
    except FileExistsError:
        pass


def create_structure(response):
    local_dir = os.path.dirname(os.path.abspath(__file__))
    pattern = response.url.split('/')
    html_structure = ''.join([str(elem) + '/' for elem in pattern[2:-1]])

    static_structure(pattern[2:-1], 'css', local_dir)
    static_structure(pattern[2:-1], 'js', local_dir)
    static_structure(pattern[2:-1], 'img', local_dir)

    try:
        os.makedirs(f'{local_dir}/../../{html_structure}')
    except FileExistsError:
        pass
