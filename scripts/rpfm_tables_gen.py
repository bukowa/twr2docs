import json

if __name__ == '__main__':
    headers_filename = './rpfm_dbtsv_getheader.json'

    with open(headers_filename, 'r') as f:
        headers = json.load(f)

    filename = '../.deps/rpfm_schema/schema_rom2.json'
    # read as json
    with open(filename, 'r') as f:
        data = json.load(f)

    markdown_content = ["""---
title: schema
summary: A brief description of my document.
---

# Introduction
Database schema extracted from RPFM.
Required a few scripts to setup but seems pretty usable.

"""]
    # Iterate over the tables and fields
    for table_name, fields_list in data['definitions'].items():

        # if there are not fields in the table, skip it
        if len(fields_list) == 0:
            print(f"!!!Table {table_name} has no fields")
            continue

        # skip if table not found in headers (we cant determine version)
        if table_name not in headers:
            print(f"!!!Table {table_name} not found in headers")
            continue

        # skip if headers len for table is 0 (there are no files)
        if len(headers[table_name]) == 0:
            print(f"!!!Table {table_name} has no headers")
            continue

        # skip if there are multiple files for the table (too hard)
        if len(headers[table_name]) > 1:
            print(f"!!!Table {table_name} has multiple headers")
            continue

        # look for the latest version entry
        # if theres only one entry, use it
        if len(fields_list) == 1:
            entry = fields_list[0]

        # if there are multiple entries, find the version that matches the header
        else:
            version = int(headers[table_name][0]['version'])
            # find the entry with the same version
            entries = [e for e in fields_list if int(e['version']) == version]

        markdown_content.append(f"  ")
        markdown_content.append(f"## {table_name}\n")

        # Start the table with headers
        markdown_table = [
            "| Field Name | Description | Is Key |"]
        markdown_table.append(
            "|------------|-------------|--------|")

        # Add rows for each field entry
        # grab the entry with proper version

        for field in entry['fields']:

            row = [
                field.get('name', ''),
                field.get('description', ''),
                field.get('is_key', '')
            ]
            markdown_table.append(f"| {' | '.join(str(val) for val in row)} |")



        # Join the table rows and append to the markdown content
        markdown_content.append("\n".join(markdown_table))

    # write to file
    with open('tables.md', 'w') as f:
        f.write('\n'.join(markdown_content))
