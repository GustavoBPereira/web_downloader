from bs4 import BeautifulSoup


def fix_links(response):
    bs = BeautifulSoup(response.text, 'html.parser')

    for link in bs.find_all('a'):
        if 'href' in link.attrs:
            # pattern to check if is internal link
            if link.attrs['href'][0] == '/':
                root_path = ''
                for i in response.url.split('/')[3:-1]:
                    root_path += '../'
                root_path = './' if root_path == '' else root_path
                file = 'index' if link['href'] == '/' else link['href']
                file = file[1::] if file.startswith('/') else file
                link['href'] = root_path + file + '.html'
    return str(bs)
