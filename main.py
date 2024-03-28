import requests
from requests.structures import CaseInsensitiveDict
import os
import time
import json
import gspread
import datetime


with open("creds.json") as creds:
    creads = {}

token = "sfrkckngnfbxuhy2zj59"
company_id = "123456"
url = "https://api.alteg.io/api/v1/reports/z_report/{company_id}"
katusenapi = set()
narva = set()
narva2 = set()
tartuyaama = set()
tartutyaha = set()
parnohomiku = set()
narvakerase =set()
mehaanika = set()


def get_data_from_api(token, company_id, url):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Autoritation"] = "Bearer {token}"
    

    r = requests.get(url, headers=headers, date_from="2024-03-01", date_to =datetime.today())

    print(r.status_code)


def dump_to_json(data_from_api):
    data = json.dump(data_from_api)
    return(data)
    

my_bad_query = "SeLEct  *, 1, blah as  fOO  from mySchema.myTable"

# Lint the given string and return an array of violations in JSON representation.
lint_result = sqlfluff.lint(my_bad_query, dialect="bigquery")
# lint_result =
# [
#     {
#         "code": "CP01",
#         "line_no": 1,
#         "line_pos": 1,
#         "description": "Keywords must be consistently upper case.",
#     }
#     ...
# ]

#  -------- FIXING ----------

# Fix the given string and get a string back which has been fixed.
fix_result_1 = sqlfluff.fix(my_bad_query, dialect="bigquery")
# fix_result_1 = 'SELECT  *, 1, blah AS  foo  FROM myschema.mytable\n'

# We can also fix just specific rules.
fix_result_2 = sqlfluff.fix(my_bad_query, rules=["CP01"])
# fix_result_2 = 'SELECT  *, 1, blah AS  fOO  FROM mySchema.myTable'

# Or a subset of rules...
fix_result_3 = sqlfluff.fix(my_bad_query, rules=["CP01", "CP02"])
# fix_result_3 = 'SELECT  *, 1, blah AS  fOO  FROM myschema.mytable'

#  -------- PARSING ----------

# Parse the given string and return a JSON representation of the parsed tree.
parse_result = sqlfluff.parse(my_bad_query)
# parse_result = {'file': {'statement': {...}, 'newline': '\n'}}

# This JSON structure can then be parsed as required.
# An example usage is shown below:


def get_json_segment(
    parse_result: Dict[str, Any], segment_type: str
) -> Iterator[Union[str, Dict[str, Any], List[Dict[str, Any]]]]:
    """Recursively search JSON parse result for specified segment type.

    Args:
        parse_result (Dict[str, Any]): JSON parse result from `sqlfluff.fix`.
        segment_type (str): The segment type to search for.

    Yields:
        Iterator[Union[str, Dict[str, Any], List[Dict[str, Any]]]]:
        Retrieves children of specified segment type as either a string for a raw
        segment or as JSON or an array of JSON for non-raw segments.
    """
    for k, v in parse_result.items():
        if k == segment_type:
            yield v
        elif isinstance(v, dict):
            yield from get_json_segment(v, segment_type)
        elif isinstance(v, list):
            for s in v:
                yield from get_json_segment(s, segment_type)


# e.g. Retrieve array of JSON for table references.
table_references = list(get_json_segment(parse_result, "table_reference"))
print(table_references)
# [[{'identifier': 'mySchema'}, {'dot': '.'}, {'identifier': 'myTable'}]]

# Retrieve raw table name from last identifier in the table reference.
for table_reference in table_references:
    table_name = list(get_json_segment(parse_result, "naked_identifier"))[-1]
    print(f"table_name: {table_name}")
# table_name: myTable



if __name__ == "__main__":
    print("exporting data to google sheets...")

