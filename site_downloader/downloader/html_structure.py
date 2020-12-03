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

    for img in bs.find_all('img'):
        if 'src' in img.attrs:
            root_path = ''
            for i in response.url.split('/')[3:-1]:
                root_path += '../'
            root_path = './' if root_path == '' else root_path
            file_path = 'static_files/img/' + ''.join([str(img_path) + '/' for img_path in response.url.split('/')[3:-1]])
            file = img['src'].split('/')[-1]
            img['src'] = root_path + file_path + file

    return str(bs)
