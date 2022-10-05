# prototype webscrapping from command line

# D:\mypy\bls>cd blswebscrape

# D:\mypy\bls\blswebscrape>cd..

# D:\mypy\bls>blswebscrape\scripts\activate

# (blswebscrape) D:\mypy\bls>cd webscraping

# (blswebscrape) D:\mypy\bls\webscraping>python --version
# Python 3.9.7

# (blswebscrape) D:\mypy\bls\webscraping>python
# Python 3.9.7 (default, Sep 16 2021, 16:59:28) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32

>>> from urllib.request import urlopen as uReq
>>> from bs4 import BeautifulSoup
>>> quotes_page ='https://bluelimelearning.github.io/my-fav-quotes/'
>>> uClient =uReq(quotes_page)
>>> page_html = uClient.read()
>>> uClient.close()
>>> page_soup = BeautifulSoup(page_html, "html.parser")
>>> quotes = page_soup.findAll("div", {"class" :"quotes"})
>>> len(quotes)
19
>>> quotes[1]
<div class="quotes">
<p class="aquote">
                    Feeling gratitude and not<br/> expressing it is like wrapping<br/> a present and not giving it.
                </p>
<p class="author">
                    William Arthur Ward
                </p>
</div>
>>> quotes[1].text.strip()
'Feeling gratitude and not expressing it is like wrapping a present and not giving it.\n                \n\n                    William Arthur Ward'
>>> page_soup.h1
<h1>Words of Wisdom</h1>
>>> page_soup.h1.text.strip()
'Words of Wisdom'
>>> fav_quotes = page_soup.findAll("p", {"class":"aquote"})
>>> fav_authors = page_soup.findAll("p", {"class":"author"})
>>> fav_quotes[2].text.strip()
'Our greatest glory is not in never falling but in rising every time we fall.'
>>> fav_authors[2].text.strip()
'Confucious'
>>> fav_authors
[<p class="author">
                Confucious
            </p>, <p class="author">
                    William Arthur Ward
                </p>, <p class="author">
                    Confucious
                </p>, <p class="author">
                    Mark Twain
                </p>, <p class="author">
                    Theodore Roosevelt
                </p>, <p class="author">
                    Nelson Mandela
                </p>, <p class="author">
                    Confucius
                </p>, <p class="author">
                    Mahatma Gandhi
                </p>, <p class="author">
                    Martin Luther King Jnr
                </p>, <p class="author">
                    Lao Tzu
                </p>, <p class="author">
                    Mahatma Gandhi
                </p>, <p class="author">
                    Lyndon B Johnson
                </p>, <p class="author">
                    Epictetus
                </p>, <p class="author">
                    Jim Rohn
                </p>, <p class="author">
                    Frank Sinatra
                </p>, <p class="author">
                    Elbert Hubbard
                </p>, <p class="author">
                    Robert Loius Stevenson
                </p>, <p class="author">
                    Zig Ziglar
                </p>, <p class="author">
                    Albert Einstein
                </p>]
>>>
# (blswebscrape) D:\mypy\bls\webscraping>python quotes.py >myquotes.txt