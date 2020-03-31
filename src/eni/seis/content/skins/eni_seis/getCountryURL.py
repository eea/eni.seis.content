##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=country_code=""

countries = {
    "am": "Armenia",
    "az": "Azerbaijan",
    "by": "Belarus",
    "ge": "Georgia",
    "md": "Moldova",
    "ua": "Ukraine"
    }

country = countries.get(country_code, '')
country_url = "/east/countries/" + country.lower()
return "<a href='" + country_url + "'>" + \
        "<img class='flag-img' src='lang-flag-" + country_code.upper() + \
        ".png' />" + \
        country + \
        "</a>"
