import sys
import pandas as pd

from rdflib import Graph, term

geography_codes_register = "https://statistics.gov.scot/downloads/graph?uri=http://statistics.gov.scot/graph/standard-geography-code-register"
geography_codes = Graph()
official_name_predicate = term.URIRef("http://statistics.data.gov.uk/def/statistical-geography#officialname")


def init_graph():
    """ Initialise the graph with latest geography codes from scot gov. """
    print("Initialising Geography Register this can take circa 20 seconds")
    geography_codes.parse(geography_codes_register, "nt")


def get_official_name(feature_code: str):
    """ Function extracts a feature codes official name from the Scot Gov geography register"""
    subject = term.URIRef(f"http://statistics.gov.scot/id/statistical-geography/{feature_code}")
    return geography_codes.value(subject, official_name_predicate)


def write_geo_names_csv(filename: str):
    """ Parse csv file, and lookup official names for each featurecode in the file """
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 400)
    stats_df = pd.read_csv(filename)
    print(stats_df.head())

    # Add new official_name column and lookup each featurecode
    for index, row in stats_df.iterrows():
        stats_df.loc[index, "official_name"] = get_official_name(row["FeatureCode"])

    print(stats_df.head())
    part_name = filename.replace(".csv", "")
    stats_df.to_csv(f"{part_name}_geo_names.csv", index=False)


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        raise ValueError("Must supply filename of csv you want to parse, eg python gen_geo_names.py test.csv")

    init_graph()
    write_geo_names_csv(filename)
