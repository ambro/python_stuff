import re

from bs4 import BeautifulSoup


ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
            <p class="star-rating Three">
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
            </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>

        In stock

</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>

</body></html>
'''


class ParsedItemLocators:
    NAME_LOCATOR = 'article.product_pod h3 a'
    URL_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'p.price_color'


def find_item_name():
    item_link = soup.select_one(ParsedItemLocators.NAME_LOCATOR)
    item_name = item_link.attrs.get('title')
    print(item_name)


def find_item_url():
    item_link = soup.select_one(ParsedItemLocators.URL_LOCATOR)
    item_url = item_link.attrs.get('href')
    print(item_url)


def find_price():
    price_paragraph = soup.select_one(ParsedItemLocators.PRICE_LOCATOR).string
    matches = re.findall('[0-9.]+', price_paragraph)
    price = float(matches[0])
    print(price)


def find_rating():
    locator = 'article.product_pod p.star-rating'
    item = soup.select_one(locator)
    rating_str = item.attrs.get('class')[-1]
    print(rating_str)


soup = BeautifulSoup(ITEM_HTML, 'html.parser')
find_item_name()
find_item_url()
find_price()
find_rating()


