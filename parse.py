from urllib.request import urlopen
from xml.etree import ElementTree as etree


def btc():
    with urlopen("https://blockchain.info/ru/ticker", timeout=5) as r:
        return etree.parse(r).findtext('"RUB"{"last"}:')


def usd():
    with urlopen("https://www.cbr.ru/scripts/XML_daily.asp", timeout=5) as r:
        return etree.parse(r).findtext('.//Valute[@ID="R01235"]/Value')


def eur():
    with urlopen("https://www.cbr.ru/scripts/XML_daily.asp", timeout=5) as r:
        return etree.parse(r).findtext('.//Valute[@ID="R01239"]/Value')


def gbp():
    with urlopen("https://www.cbr.ru/scripts/XML_daily.asp", timeout=5) as r:
        return etree.parse(r).findtext('.//Valute[@ID="R01035"]/Value')


def cny():
    with urlopen("https://www.cbr.ru/scripts/XML_daily.asp", timeout=5) as r:
        return etree.parse(r).findtext('.//Valute[@ID="R01375"]/Value')


def jpy():
    with urlopen("https://www.cbr.ru/scripts/XML_daily.asp", timeout=5) as r:
        return etree.parse(r).findtext('.//Valute[@ID="R01820"]/Value')


def chf():
    with urlopen("https://www.cbr.ru/scripts/XML_daily.asp", timeout=5) as r:
        return etree.parse(r).findtext('.//Valute[@ID="R01775"]/Value')


def uah():
    with urlopen("https://www.cbr.ru/scripts/XML_daily.asp", timeout=5) as r:
        return etree.parse(r).findtext('.//Valute[@ID="R01720"]/Value')


def byn():
    with urlopen("https://www.cbr.ru/scripts/XML_daily.asp", timeout=5) as r:
        return etree.parse(r).findtext('.//Valute[@ID="R01090B"]/Value')


def kzt():
    with urlopen("https://www.cbr.ru/scripts/XML_daily.asp", timeout=5) as r:
        return etree.parse(r).findtext('.//Valute[@ID="R01335"]/Value')
