"""
This application converts the various text files stored in the source-data
directory into a pickled python object to be used by the random data
generator scripts

Copyright (C) 2007 Chris Moffitt
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""

from builtins import input
import csv
import string
import pickle
import os

try:
    DIRNAME = os.path.dirname(__file__)
except NameError:
    DIRNAME = os.path.dirname(sys.argv[0])

data_dir = os.path.join(DIRNAME, "source-data")
simple_files_to_process = ['street-names.txt', 'street-types.txt', 'latin-words.txt',
                           'email-domains.txt', 'job-titles.txt', 'company-names.txt',
                           'company-types.txt', 'nounlist.txt']


def _load_files():
    # Process Zip Codes
    all_zips = {}
    reader = csv.reader(open(os.path.join(data_dir, "zip-codes.txt"), "r"))
    for row in reader:
        data = [string.capwords(row[3]), row[4]]
        all_zips[row[0]] = data
    output = open('source-data.pkl', 'wb')
    pickle.dump(all_zips, output)

    #Process area codes
    area_code_file = open(os.path.join(data_dir, "area-codes.txt"), "r")
    state_area_codes = {}
    for line in area_code_file:
        clean_line = line.replace(' ', '').rstrip('\n')
        state_area_codes[line.split(':')[0]] = clean_line[3:].split(',')
    pickle.dump(state_area_codes, output)
    area_code_file.close()

    #Process Last Names
    last_names = []
    last_name_file = open(os.path.join(data_dir, "last-name.txt"), "r")
    for line in last_name_file:
        clean_line = line.rstrip('\n')
        last_names.append(string.capwords(clean_line.split(' ')[0]))
    pickle.dump(last_names, output)
    last_name_file.close()

    #Process Male First Names
    male_first_names = []
    male_first_name_file = open(os.path.join(data_dir, "male-first-name.txt"), "r")
    for line in male_first_name_file:
        clean_line = line.rstrip('\n')
        male_first_names.append(string.capwords(clean_line.split(' ')[0]))
    pickle.dump(male_first_names, output)
    male_first_name_file.close()

    #Process Female First Names
    female_first_names = []
    female_first_name_file = open(os.path.join(data_dir, "female-first-name.txt"), "r")
    for line in female_first_name_file:
        clean_line = line.rstrip('\n')
        female_first_names.append(string.capwords(clean_line.split(' ')[0]))
    pickle.dump(female_first_names, output)
    female_first_name_file.close()

    #Process the simple files
    for f in simple_files_to_process:
        temp = []
        sample_file = open(os.path.join(data_dir, f), "r")
        for line in sample_file:
            clean_line = line.rstrip('\n')
            temp.append(clean_line)
        pickle.dump(temp, output)
        sample_file.close()
        temp = []
    output.close()

def rebuild_pkl_file():
    """ Rebuild the pickle file that contains the source data
    """
    response = input("Type 'yes' to reload the data from source files and create a new source file: ")
    if response.lower() == 'yes':
        _load_files()
