from urllib.request import urlopen

from bs4 import BeautifulSoup

from .models import Employee


def scrape_employee_page(vokal_employee_url):
    try:
        page = urlopen(vokal_employee_url)
    except urllib.HTTPError:
        return False

    soup = BeautifulSoup(page.read(), 'html.parser')
    li_list = [li for li in soup.findAll('li')]
    for li in li_list:
        if li.find("div", {"id": "profile-image-wrap"}):
            name = li.find("h5").get_text()
            title = li.find("p", {"class": "job-title"}).get_text()
            image_url = li.find('img', {'class': 'image1'})['src'][2:]

            name = name.split(' ')
            employee, created = Employee.objects.get_or_create(
                first_name=name[0],
                last_name=name[1],
                title=title,
                image_url=image_url
            )
            employee.save()

    return True
