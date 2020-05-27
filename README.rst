.. image:: https://img.shields.io/pypi/dw/barnum?style=flat-square   :alt: PyPI - Downloads

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
from Barnum:

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
There has been a change in the most recent version of barnum to make the
code more pythonic.

The recommended method is to import barnum and call the functions from your
own script.

If you'd like to call it from another script, here's an example or two from the
interpreter::

    Python 3.5.1 |Continuum Analytics, Inc.| (default, Dec  7 2015, 11:16:01)
    [GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import barnum
    >>> barnum.create_name()
    ('Isabel', 'Madigan')
    >>> barnum.create_name()
    ('Jesica', 'Loveless')
    >>> barnum.create_city_state_zip()
    ('54666', 'Warrens', 'WI')
    >>> barnum.create_city_state_zip()
    ('55113', 'Saint Paul', 'MN')
    >>> barnum.create_phone()
    '(716)248-1703'
    >>> barnum.create_phone()
    '(603)502-8450'
    >>> barnum.create_phone('38138')
    '(615)564-2637'
    >>> barnum.create_sentence()
    'In lobortis ut te at et feugiat ipsum vel ex feugiat eros.'
    >>> barnum.create_sentence()
    'In erat hendrerit at odio eu tincidunt exerci.'
    >>> barnum.create_cc_number()
    ('mastercard', ['5231056277792200'])
    >>> barnum.create_cc_number()
    ('visa', ['4929064950922570'])
    >>> barnum.create_nouns()
    'place blue'
    >>> barnum.create_nouns()
    'Steven clarinet'
    >>> barnum.create_date()
    datetime.datetime(2024, 2, 4, 9, 51, 38, 971944)
    >>> barnum.create_date(past=True)
    datetime.datetime(2006, 9, 23, 9, 51, 46, 927690)
    >>> barnum.create_email()
    'Dalton.Segal@luptatumdelenitaugue.org'
    >>> barnum.create_pw()
    'naPTg67M'


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
