def get_file_location(response):
    splited_url = response.url.split('/')

    name = splited_url[-1]
    name += '.html' if not name.endswith('.html') else ''
    name = 'index.html' if name == '.html' else name

    folder = ''.join([str(elem) + '/' for elem in splited_url[2:-1]])
    return f'{folder}/{name}'
