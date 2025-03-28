import re
from r2doclib.parsecfunc import extract_function_params_from_code


def _extract_functions_from_ghidra_dump(_filepath):
    """
    Extract functions from the Ghidra dump.
    A file which has multiple functions separated by
    ### FUNCTION START ###
    ### FUNCTION END ###
    """
    with open(_filepath, "r") as f:
        content = f.read()

    _functions = content.split("\n### FUNCTION START ###\n")
    _functions = [fn.split("\n### FUNCTION END ###\n")[0] for fn in _functions if "### FUNCTION END ###" in fn]
    return _functions


def make_events_markdown(_funcs):
    """
    Given Ghidra extracted function list, create a Markdown file
    with properly documented conditions for MkDocs.
    """
    print("Creating events markdown file...")
    _collection = []

    for _f in _funcs:
        _p = _f[0][1]
        _p = [_.strip('"') for _ in _p]
        _event_name = _p[1]
        _event_code = _p[0]
        _event_desc = _p[2]
        _event_context = _p[3]
        _collection.append(dict(
            name=_event_name,
            code=_event_code,
            description=_event_desc,
            context=_event_context,
        ))

    # Convert to dict
    _collection = {event["name"]: event for event in _collection}

    # Fix map of event names
    _fix_map = {
        "battle_ship_sunk": None,
        "battle_commanding_ship_routs": "BattleCommandingShipRouts",
    }

    # Apply fixes and filter out None values
    _collection = [
        {**event, "name": _fix_map.get(event["name"], event["name"])}
        for event in _collection.values()
        if _fix_map.get(event["name"], event["name"]) is not None
    ]

    # Sort list by name
    _collection.sort(key=lambda x: x["name"])

    md_content = ["# Events Reference\n"]
    for event in _collection:
        md_content.append(f"## {event['name']}\n")
        md_content.append(f"**Code:** `{event['code']}`  \n")
        md_content.append(f"**Context:** `{event['context']}`  \n\n")
        md_content.append(f"**Description:**  \n{event['description']}\n")

    with open("events.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md_content))

    print("Markdown file generated: events.md")


def make_conditions_markdown(_funcs):
    """
    Given Ghidra extracted function list, create a Markdown file
    with properly documented conditions for MkDocs.
    """
    print("Creating conditions markdown file...")
    _collection = []
    for _f in _funcs:
        _p = _f[0][1]
        _p = [_.strip('"') for _ in _p]
        _condition_name = _p[0]
        _condition_arg_desc = _p[1]
        _condition_desc = _p[2]
        _condition_example = _p[3]
        _collection.append(dict(
            name=_condition_name,
            args=_condition_arg_desc,
            description=_condition_desc,
            example=_condition_example,
        ))
    # convert to  dict
    _collection = {condition["name"]: condition for condition in _collection}

    # fix map of condition names
    _fix_map = {
    }

    # apply fixes and filter out None values
    _collection = [
        {**condition, "name": _fix_map.get(condition["name"], condition["name"])}
        for condition in _collection.values()
        if _fix_map.get(condition["name"], condition["name"]) is not None
    ]

    # sort list by name
    _collection.sort(key=lambda x: x["name"])

    md_content = ["# Conditions Reference\n"]

    for condition in _collection:
        md_content.append(f"## {condition['name']}\n")
        md_content.append(f"**Example:** `{condition['example']}`\n")
        md_content.append(f"**Arguments:** `{condition['args']}`\n")
        md_content.append(f"**Description:**  \n{condition['description']}\n")
        md_content.append("\n")

    with open("conditions.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md_content))

if __name__ == '__main__':
    make_events_markdown(
        map(extract_function_params_from_code, _extract_functions_from_ghidra_dump("./data/events.txt")))

    make_conditions_markdown(
        map(extract_function_params_from_code, _extract_functions_from_ghidra_dump("./data/conditions.txt")))
