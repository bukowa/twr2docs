import re

def add_missing_events(filename, new_events_list):
    """
    Adds missing events to a markdown file, sorted alphabetically within the existing list, without duplication.

    Args:
        filename (str): The path to the markdown file.
        new_events_list (list): A list of new event names to add.
    """

    with open(filename, 'r') as f:
        original_content_lines = f.readlines()

    # --- Step 1: Separate header and existing event blocks ---
    header_lines = []
    event_blocks = {} # {event_name: list_of_lines_for_this_event}
    existing_event_names_set = set()

    current_block_lines = []
    current_event_name = None
    
    # Find the end of the header (before the first '##' event)
    header_end_index = 0
    for i, line in enumerate(original_content_lines):
        if line.strip().startswith('##'):
            header_end_index = i
            break
        header_lines.append(line)
    
    # Parse existing event blocks
    for line in original_content_lines[header_end_index:]:
        if line.strip().startswith('##'):
            if current_event_name: # Save the previous block
                event_blocks[current_event_name] = current_block_lines
                existing_event_names_set.add(current_event_name)
            
            current_event_name = line.strip().replace('##', '').strip()
            current_block_lines = [line]
        else:
            current_block_lines.append(line)
    
    # Add the last event block if it exists
    if current_event_name:
        event_blocks[current_event_name] = current_block_lines
        existing_event_names_set.add(current_event_name)

    # --- Step 2: Identify truly missing events ---
    missing_events_to_add = sorted(list(set(new_events_list) - existing_event_names_set))

    # --- Step 3: Merge existing and missing events alphabetically ---
    all_event_names_sorted = sorted(list(existing_event_names_set) + missing_events_to_add)

    # --- Step 4: Reconstruct the file content ---
    final_content_lines = list(header_lines) # Start with the header

    for event_name in all_event_names_sorted:
        if event_name in existing_event_names_set:
            # Add existing event's original block
            final_content_lines.extend(event_blocks[event_name])
        else:
            # Add new event block with placeholders
            final_content_lines.append(f'## {event_name}\n\n')
            final_content_lines.append(f'**Code:** ``\n\n')
            final_content_lines.append(f'**Context:** ``\n\n')
            final_content_lines.append(f'**Description:** ``\n\n')
            final_content_lines.append(f'**Author:** ``\n\n')

    # --- Step 5: Write the modified content back to the file ---
    with open(filename, 'w') as f:
        f.writelines(final_content_lines)


if __name__ == "__main__":
    # Read new events from inputx
    with open('scripts/inputx', 'r') as f:
        new_events_from_file = [line.strip() for line in f.readlines()]

    filename = 'r2docs/docs/lua/api/events.md'
    add_missing_events(filename, new_events_from_file)