What is Barnum?
===============

Barnum is a python-based application for quickly and easily creating 
pseudo-random data typically used for application testing.

Why did you create Barnum?
==========================

I am developing a shopping cart application in Django and realized that I 
needed a bunch of data to simulate the store's behavior under somewhat normal 
production usage.  

I got tired of always trying to think of names and addresses for customers and 
so decided to automate the process a little bit.  Such was born Barnum.

This looks kind of old, what's the deal?
========================================

I created this in 2007 and hosted it on Google Code. After a while I forgot
about it. The code sat in obscurity until I received an email from Google
about the eventually closing of Google Code. I decided I would migrate it
to github to see if it is useful to anyone else.

Why is Barnum unique?
=====================

I was able to find some online systems for generating large amounts of test 
data.  I could not find any application that had the breadth of data generation 
capabilities nor the ability to easily interface with Django in the way I 
wanted to.

One of the most unique aspects of Barnum is that the data is what I'll call
"plausible."  For example, here's an example "identity" randomly generated
from Barnum -
    Sid Seymour
    10 Kimbrough Grove Drive
    Arthur ND, 58006
    (701)642-6471

    Who works at:
    Network Hardware Co as a Personnel Clerk Senior

You should notice a couple of things about this data.
 - There's a realistic first and last name
 - The street names are also plausible
 - Arthur, ND is a real city and the zip code is 58006
 - 701 is an area code used for North Dakota 
 - The fictional company is somewhat reasonable.
 - The job position also makes sense.

Why not just use Random to create strings of letters?
=====================================================

Well, I find that when testing applications, if it's just a random string
of numbers of letters, it gets hard to tell if something is out of place
or "looks wrong."  If you'd like to just generate totally random information,
then you probably don't need Barnum!

What other alternatives are there?
==================================

I originally created this in 2007 and it sat idle for a while. In that
time there have been some other python solutions.

I think `fake factory <https://pypi.python.org/pypi/fake-factory>`_ is one of
the best out there and provides a lot more options than barnum.

However, Barnum still has some unique aspects, specifically having some
"intelligence" as to how the data is related and the flexibility you have
to easily customize the data by adding or subtracting to the data in the
**source-data** directory.


What type of information does Barnum generate?
==============================================

Here's a list of types of dummy data Barnum can create:
 - First name and/or last name in either gender
 - Job title
 - Phone number
 - Street number and name
 - Zip code plus city & state
 - Company name
 - Credit card number and type (with valid checksum)
 - Dates
 - Email addresses
 - Sample password
 - Words (latin)
 - Sentences and/or paragraphs of random latin words

What version of python do I need?
=================================
Barnum should work on python 2.7.x and python 3.x

How do I install it?
====================

pip install barnum

How do I use it?
================

The gen_data.py script is the primary showcase for how to create random data
using Barnum.  If you run it from the command line:

 python gen_data.py
 
You'll see some sample data output.

If you'd like to call it from another script, here's an example or two from the
interpreter::

    Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from barnum import gen_data
    >>> gen_data.create_name()
    ('Dianna', 'Macpherson')
    >>> gen_data.create_name()
    ('Dessie', 'Badillo')
    >>> gen_data.create_name()
    ('Dorsey', 'Knox')
    >>> gen_data.create_city_state_zip()
    ('36874', 'Salem', 'AL')
    >>> gen_data.create_city_state_zip()
    ('33034', 'Homestead', 'FL')
    >>> gen_data.create_phone()
    '(802)560-6944'
    >>> gen_data.create_phone()
    '(959)430-3436'
    >>> gen_data.create_phone('38138')
    '(931)679-1579'
    >>> gen_data.create_sentence()
    'Ut feugiat feugait vero consequatvel ex ullamcorper.'
    >>> gen_data.create_sentence()
    'Qui exerci molestie augue consequat lorem iusto ut duis ea veniam vel.'
    >>> gen_data.cc_number()
    ('mastercard', ['5245893611343643'])
    >>> gen_data.cc_number()
    ('discover', ['6011818325460433'])
    >>> gen_data.create_nouns()
    'eyebrow scraper'
    >>> gen_data.create_nouns()
    'loan comics'
    >>> gen_data.create_date()
    datetime.datetime(2024, 12, 27, 20, 1, 10, 343660)
    >>> gen_data.create_date(past=True)
    datetime.datetime(2014, 10, 13, 20, 1, 20, 159341)
    >>> gen_data.create_email()
    'Carrol.Zavala@facilisisiusto.tv'
    >>> gen_data.create_company_name()
    'Design International'
    >>> gen_data.create_pw()
    'vm6qV2iR'


You can see that it should be trivial to incorporate this data into any python script.
The possibilities of creating CSV's, raw SQL, Python Objects, etc are practically
endless!

Where does the data come from?
==============================

I pulled sample data and existing scripts from a bunch of different sources. It looks like a lot
of the sources are now dead links.  
 - The names are from 1990 US Census data
 - The street names are from real us streets in a few locales.
 - Company names are randomly generated by me.
 - Job Titles were taken from another census site that I can't seem to find now.
 - Zip Codes from another dead site.
 - Random latin text came from http://www.4guysfromrolla.com/webtech/052800-1.shtml
 - Credit Card generator is from Graham King - http://www.darkcoding.net/index.php/credit-card-numbers/
 - Password generator is from Pradeep Kishore Gowda via the Python Cookbook

How can I add more data?
========================

If all you'd like to do is add some more seed data to an existing source, edit the appropriate
file in the source-data directory and execute the convert_data.py script to create a new
pickle file.

How can I contribute?
=====================

I've moved the code to github to make it easier for others to contribute. Feel
free to send pull requests or submit tickets.

Why is this so US focused?
==========================

I needed info for the US only.  I had access to this data and knew what I wanted.  If you
would like to add other countries or info, feel free to contribute!


Can this be used for evil?
==========================

Ummm.  Probably not.  All of the data is random.  The credit card numbers conform to the
Luhn 10 checksum formula but are not necessarily valid numbers.  Even if they were, you would
need to know the real name, address and phone number before you could do anything illegal
with the data.  I think we're all pretty safe.

Where did this name come from?
==============================

Choosing names for projects is kind of fun but kind of a hassle.  There needs to be a name
but it can't be anything too stupid.  I started off thinking of an acronym and ended up with
PT ("Python Testing") and immediately thought of P.T. Barnum.  I really liked the name 
because I was using this for Satchmo and project made in Django.  Single word names seemed
cool.  Also, I like the fact that P.T. Barnum was really a master at making people think
something was real that wasn't.  Which is exactly what this little script does.


Why is it licensed under the GPL?
=================================

I use a couple of other python scripts that were licensed under the GPL.  So, I figured it
was best to just release under the GPL.  If you would like another license arrangement,
let me know and I'll see if there's something we can do.
