import pandas as pd

from rdflib import Graph, term

geography_codes_register = "https://statistics.gov.scot/downloads/graph?uri=http://statistics.gov.scot/graph/standard-geography-code-register"
geography_codes = Graph()
official_name_predicate = term.URIRef("http://statistics.data.gov.uk/def/statistical-geography#officialname")


def init_graph():
    """ Initialise the graph with latest geography codes from scot gov. """
    geography_codes.parse(geography_codes_register, "nt")


def get_official_name(feature_code: str):
    """ Function extracts a feature codes official name from the Scot Gov geography register"""
    subject = term.URIRef(f"http://statistics.gov.scot/id/statistical-geography/{feature_code}")
    return geography_codes.value(subject, official_name_predicate)


def write_geo_names_csv(filename: str):
    """ Parse csv file, and lookup official names for each featurecode in the file """
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 400)
    covid_csv = pd.read_csv(filename)
    print(covid_csv.head())

    # Add new official_name column and lookup each featurecode
    for index, row in covid_csv.iterrows():
        covid_csv.loc[index, "official_name"] = get_official_name(row["FeatureCode"])

    print(covid_csv.head())
    part_name = filename.replace(".csv", "")
    covid_csv.to_csv(f"{part_name}_geo_names.csv", index=False)


if __name__ == "__main__":
    print("Initialising Geography Register this can take circa 20 seconds")
    init_graph()
    write_geo_names_csv("all_covid_deaths.csv")
