"""
Завершіть функцію/метод, щоб він повернув URL-адресу з будь-яким після видалення зв’язку (#).
Що то таке HTML Anchor - https://www.semrush.com/blog/html-anchor/

Examples
"lms.ithillel.ua#about" --> "lms.ithillel.ua"
"lms.ithillel.ua?page=1" -->lms.ithillel.ua?page=1"

"""
import re


def remove_url_anchor(url):
    # return re.sub('#\w{1,}', '', url)
    return re.sub("#.*", "", url)


assert remove_url_anchor("lms.ithillel.ua#about") == "lms.ithillel.ua"
assert remove_url_anchor("lms.ithillel.ua/groups/?page=1#example") == "lms.ithillel.ua/groups/?page=1"
assert remove_url_anchor("lms.ithillel.ua/groups/") == "lms.ithillel.ua/groups/"

print('Assert went well')
