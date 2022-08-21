"""Extract data on NEOs and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the
command line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""

from models import NearEarthObject, CloseApproach
import json
import csv


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth
    objects.
    :return: A collection of `NearEarthObject`s.
    """
    # Load NEO data from the given CSV file.
    # neos object to collect list of neos.
    neos = []

    # Create DictReader to capture each row with headers
    with open(neo_csv_path) as f:
        reader = csv.DictReader(f)

        # Iterate through each row and pass the neo with headers for all
        # columns
        for elem in reader:
            # The class will extract the required entries and make an object
            elem["pdes"] = NearEarthObject(pdes=elem["pdes"],
                                           name=elem["name"],
                                           diameter=elem["diameter"],
                                           pha=elem["pha"])
            # Append the object to the list of neos
            neos.append(elem["pdes"])
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close
    approaches.
    :return: A collection of `CloseApproach`es.
    """
    # Load close approach data from the given JSON file.
    # Close approaches object to collect a list of each entry
    approaches = []

    # Open json path for reading and store contents
    with open(cad_json_path) as f:
        contents = json.load(f)

    # Iterate through each list in data
    for content in contents["data"]:
        # Create a new close approach called the same name as the des
        content[0] = CloseApproach(des=content[0],
                                   cd=content[3],
                                   dist=content[4],
                                   v_rel=content[7])
        approaches.append(content[0])

    return approaches
