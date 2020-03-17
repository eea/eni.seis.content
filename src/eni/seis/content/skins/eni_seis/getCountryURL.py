##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=country_code=""

return {
    "am": "/east/countries/armenia",
    "az": "/east/countries/azerbaijan",
    "by": "/east/countries/belarus",
    "ge": "/east/countries/georgia",
    "md": "/east/countries/moldova",
    "ua": "/east/countries/ukraine"
    }.get(country_code, None)
