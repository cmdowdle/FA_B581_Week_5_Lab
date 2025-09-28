from pprint import pprint
import requests

BASE_HERMES_URL = 'http://159.203.121.13:8080/v1/snomed'


def constraint_1():
    # Search all clinical findings that has an associated morphology of caries and finding site that is a tooth part
    constraint = """
< 404684003 |Clinical finding (finding)| :

<< 116676008 |Associated morphology (attribute)| = << 65413006 |Caries (morphologic abnormality)|

AND << 363698007 |Finding site (attribute)| = << 410613002 |Tooth part (body structure)|
    """
    return constraint


def expression_constraint(search_string):
    response = requests.get(f'{BASE_HERMES_URL}/search?constraint={search_string}&maxHits=10')
    data = response.json()
    pprint(data)


if __name__ == '__main__':
    string_value = constraint_1().strip()
    print()
    expression_constraint(search_string=string_value)