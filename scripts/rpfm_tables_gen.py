import json
import os
from pathlib import Path
from lxml import etree

if __name__ == '__main__':

    headers_filename = './rpfm_dbtsv_getheader_game.json'
    with open(headers_filename, 'r') as f:
        headers = json.load(f)

    schema_filename = '../.deps/rpfm_schema/schema_rom2.json'
    with open(schema_filename, 'r') as f:
        data = json.load(f)

    path_assemblykit_db = r"C:\Program Files (x86)\Steam\steamapps\common\Total War Rome II\assembly_kit\raw_data\db"
    assemblykit_files = os.listdir(path_assemblykit_db)

    markdown_content = ["""---
title: schema
summary: A brief description of my document.
---

# Tables
---
Database schema extracted from RPFM.
Required a few scripts to setup but seems pretty usable.


"""]

    unrefed_tables = {}
    problematic_tables = {}

    # remove tables that are not in headers
    for table_name, fields_list in data['definitions'].copy().items():
        if table_name not in headers:
            del data['definitions'][table_name]
            print(f"!!!Table {table_name} not found in headers")

    # Iterate over the tables and fields
    for table_name, fields_list in data['definitions'].items():

        # if this is a start_pos table, skip it
        if table_name.startswith('start_pos'):
            print(f"!!!Table {table_name} is a start_pos table")
            problematic_tables[table_name] = {}
            continue

        # if there are not fields in the table, skip it
        if len(fields_list) == 0:
            print(f"!!!Table {table_name} has no fields")
            problematic_tables[table_name] = {}
            continue

        # skip if table not found in headers (we cant determine version)
        # if table_name not in headers:
        #     print(f"!!!Table {table_name} not found in headers")
        # continue

        # skip if headers len for table is 0 (there are no files)
        if len(headers[table_name]) == 0:
            # print(f"!!!Table {table_name} has no headers")
            problematic_tables[table_name] = {}
            continue

        # skip if there are multiple files for the table (too hard)
        if len(headers[table_name]) > 1:
            # print(f"!!!Table {table_name} has multiple files")
            # just grab the first file...
            headers[table_name] = [headers[table_name][0]]

        # look for the latest version entry
        # if theres only one entry, use it
        if len(fields_list) == 1:
            entry = fields_list[0]

        # if there are multiple entries, find the version that matches the header
        else:
            version = int(headers[table_name][0]['version'])
            # find the entry with the same version
            entries = [e for e in fields_list if int(e['version']) == version]
            entry = entries[0]

        markdown_content.append(f"  ")
        markdown_content.append(f"## {table_name}\n")

        # Start the table with headers
        markdown_table = [
            "| Name | Key | Type | Description | RefTable | RefKey", ]
        markdown_table.append(
            "|------|---------|--------|--------|--------|--------|")

        # Add rows for each field entry
        # grab the entry with proper version

        for field in entry['fields']:
            refs = field.get('is_reference', '')
            if refs:
                # first is the table name we can make a link on
                # the current page with # fragment # second is the key
                # build a link to the table, and display key after the link
                table = refs[0] + '_tables'
                key = refs[1]
                ref_table = f"[{table}](#{table})"
                ref_key = key

                if table not in data['definitions']:
                    # we have to build it
                    print(f"!!!Table {table} not found in definitions")
                    try:
                        with open(path_assemblykit_db + '\\' + "TWaD_" + refs[0] + ".xml", 'rb') as f:
                            raw_content = f.read()
                            # parse as xml with library
                            xml_content = etree.fromstring(raw_content)
                            fields = []
                            for _each in xml_content.iter('field'):
                                fields.append({
                                    'name': _each.find('name').text if _each.find('name') is not None else None,
                                    'primary_key': True if _each.find(
                                        'primary_key').text == "1" else False if _each.find(
                                        'primary_key') is not None else None,
                                    'field_type': _each.find('field_type').text if _each.find(
                                        'field_type') is not None else None,
                                    'required': True if _each.find('required').text == "1" else False if _each.find(
                                        'required') is not None else None,
                                    'max_length': _each.find('max_length').text if _each.find(
                                        'max_length') is not None else None,
                                    'column_source_column': _each.find('column_source_column').text if _each.find(
                                        'column_source_column') is not None else None,
                                    'column_source_table': _each.find('column_source_table').text if _each.find(
                                        'column_source_table') is not None else None,
                                })
                            unrefed_tables[table] = fields
                    except Exception as e:
                        print(f"!!!Error reading file {path_assemblykit_db + '\\' + refs[0] + '.xml'}: {e}")
                        continue

            else:
                ref_table, ref_key = '', ''
            row = [
                field.get('name', ''),
                field.get('is_key', ''),
                field.get('field_type', ''),
                field.get('description', ''),
                ref_table,
                ref_key
            ]
            markdown_table.append(f"| {' | '.join(str(val) for val in row)} |")

        # Join the table rows and append to the markdown content
        markdown_content.append("\n".join(markdown_table))

    markdown_content.append("""  \n
## Tables Not Found in the RPFM Schema
---
The following tables were not found in the RPFM schema but were found in the assembly kit.  
Game tables can reference them, but they are (probably) not editable in RPFM.  
We used the TWaD_ definition file to extract the fields.  
  \n
""")

    for table, fields in unrefed_tables.items():
        markdown_content.append(f"  \n## {table}\n")

        # Start the table with headers
        markdown_table = ["""
/// admonition | Attention
    type: attention
This table was not found in the RPFM schema. [See for more details](#tables-not-found-in-the-rpfm-schema).
///
  \n
""", "| Name | Key | Type | Description | RefTable | RefKey", "|------|---------|--------|--------|--------|--------|"]

        # Add rows for each field entry
        # grab the entry with proper version

        for field in fields:
            row = [
                field.get('name', ''),
                field.get('primary_key', ''),
                field.get('field_type', ''),
                field.get('description', ''),
                field.get('column_source_table', ''),
                field.get('column_source_column', '')
            ]
            markdown_table.append(f"| {' | '.join(str(val) for val in row)} |")

        # Join the table rows and append to the markdown content
        markdown_content.append("\n  ".join(markdown_table))

    markdown_content.append("""  \n
## Problematic Tables
---
The following tables had problems / or there were other reasons
for not including them. They are still here for reference.
  \n
""")

    for table_name, fields_list in problematic_tables.items():
        markdown_content.append(f"  \n## {table_name}\n")

        # Start the table with headers
        markdown_content.append("""
/// admonition | Warning
    type: warning
This table had problems in RPFM / other reasons. [See for more details](#problematic-tables).
///
  \n
""")

    # write to file
    with open('../r2docs/docs/database/tables.md', 'w') as f:
        f.write('\n'.join(markdown_content))
