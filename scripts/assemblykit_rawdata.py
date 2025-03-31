import os
from pathlib import Path

from lxml import etree

non_table_xml_filename_filters = [
    lambda x: x.endswith(".xml"),
    lambda x: not any((
        x.startswith("TWaD_"),
        x.startswith("TWaDFORMDESCR_"),
        x.startswith("TWaDQUERY"),
        x.startswith("TWADFORMDESCR_"),
    )),
]

if __name__ == '__main__':
    path_assemblykit \
        = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Total War Rome II\assembly_kit")
    db_files = list(filter(
        lambda x: all(_f(x) for _f in non_table_xml_filename_filters),
        os.listdir(path_assemblykit / "raw_data/db")
    ))

    print(f"Length of db_files: {len(db_files)}")
    tables = {}
    for filename in db_files:
        # append 'TWaD_' to the Path filename
        try:
            with open(path_assemblykit / "raw_data/db" / ("TWaD_" + filename), 'rb') as f:
                raw_content = f.read()
                # parse as xml with library
                xml_content = etree.fromstring(raw_content)
                fields = []
                for _each in xml_content.iter('field'):
                    fields.append({
                        'name': _each.find('name').text if _each.find('name') is not None else None,
                        'primary': True if _each.find(
                            'primary_key').text == "1" else False if _each.find(
                            'primary_key') is not None else None,
                        'type': _each.find('field_type').text if _each.find(
                            'field_type') is not None else None,
                        'required': True if _each.find('required').text == "1" else False if _each.find(
                            'required') is not None else None,
                        'max_length': _each.find('max_length').text if _each.find(
                            'max_length') is not None else None,
                        'ref_table': _each.find('column_source_table').text if _each.find(
                            'column_source_table') is not None else None,
                        'ref_column': _each.find('column_source_column').text if _each.find(
                            'column_source_column') is not None else None,
                    })
                    # if ref_table is not None convert to markdown fragment on the same page
                    # like ref_table = f"[{table}](#{table})"
                    if fields[-1]['ref_table'] is not None:
                        fields[-1]['ref_table'] = f"[{fields[-1]['ref_table']}_tables](#{fields[-1]['ref_table']}_tables)"

                tables[filename.replace('.xml', '')+'_tables'] = fields
        except Exception as e:
            print(f"!!!Error reading file {path_assemblykit / 'raw_data/db' / filename}: {e}")
            continue

    print(len(tables))
    # build a markdown table
    markdown_content = ["""---
title: assemblykit
summary: A brief description of my document.
---

# Assembly Kit Database
---
Database schemas extracted from the assembly kit `TWaD_` files.  

"""]

    for table, fields in tables.items():
        # Create a header for the table
        markdown_content.append(f"  \n## {table}\n")
        # Create a header row
        header_row = "| " + " | ".join(fields[0].keys()) + " |"
        markdown_content.append(header_row)
        # Create a separator row
        separator_row = "| " + " | ".join(["---"] * len(fields[0].keys())) + " |"
        markdown_content.append(separator_row)
        # Create a row for each field
        for field in fields:
            row = "| " + " | ".join(str(val) for val in field.values()) + " |"
            markdown_content.append(row)


    # Join the table rows and append to the markdown content
    markdown_content.append("\n".join(markdown_content))
    # Write the markdown content to a file
    with open("../r2docs/docs/database/assemblykit_db.md", 'w', encoding='utf-8') as f:
        f.write("\n".join(markdown_content))
