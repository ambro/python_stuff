from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():
    h1 = simple_soup.find('h1')
    print(h1.string)


def find_list_items():
    list_items = simple_soup.find_all('li')
    print(
        [item.string
         for item in list_items]
    )


def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)


def find_other_paragraphs():
    paragraphs = simple_soup.find_all('p')
    none_subtitle_paragraphs = [
        paragraph.string
        for paragraph in paragraphs
        if 'subtitle' not in paragraph.attrs.get('class', [])
    ]
    print(none_subtitle_paragraphs)


find_title()
find_list_items()
find_subtitle()
find_other_paragraphs()