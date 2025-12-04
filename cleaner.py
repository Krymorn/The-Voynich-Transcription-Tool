import re
import argparse
import sys

# This program cleans the original v101 transcription. It's already ran and saved to v101_cleaned.txt

def clean_transcription(text):
    """
    Cleans the Voynich v101 transcription text.
    - Removes all text between and including < and >.
    - Replaces all periods (.) with a space.
    """
    # Remove all text between and including <...>
    # This regex finds '<', then any characters (non-greedy), then '>'
    cleaned_text = re.sub(r'<.*?>', '', text)

    # Replace periods with spaces
    cleaned_text = cleaned_text.replace('.', '#')
    #cleaned_text = cleaned_text.replace(',', '%')

    return cleaned_text

def replace_characters(text, mapping):
    """
    Replaces characters in the text based on a provided mapping.
    """
    # We build the new text string character by character
    translated_text = []
    for char in text:
        # We use .get() to avoid an error if a character is not in the map.
        # If the character is found, its replacement is used.
        # If not, the original character is kept (as specified by the 2nd argument).
        translated_text.append(mapping.get(char, char))

    return "".join(translated_text)

def process_file(input_path, output_path, character_map):
    """
    Main function to read, clean, replace, and write the text.
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            raw_text = f.read()
    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_path}'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{input_path}': {e}", file=sys.stderr)
        sys.exit(1)

    # Step 1: Clean the text (remove <...>, replace .)
    cleaned_text = clean_transcription(raw_text)

    # Step 2: Replace characters based on the map
    final_text = replace_characters(cleaned_text, character_map)

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_text)
        print(f"Successfully processed file.")
        print(f"Input:  {input_path}")
        print(f"Output: {output_path}")
    except Exception as e:
        print(f"Error writing to file '{output_path}': {e}", file=sys.stderr)
        sys.exit(1)

#
# *** IMPORTANT ***
# YOU MUST EDIT THIS DICTIONARY WITH YOUR CHARACTER MAPPINGS
#
# Add your Voynich characters as keys and their corresponding
# replacement letters as values.
# Example: If the symbol 'c' (from the v101) should be 'a',
# you would write: 'c': 'a',
#
# The keys are case-sensitive.
#
VOYNICH_TO_LATIN_MAP = {
    # --- ADD YOUR MAPPINGS HERE ---
    # Example mappings (replace with your actual ones):
    'a': 'a',
    'b': 'b',
    'c': 'c',  
    'd': 'd',
    'e': 'e',
    'o': 'o',
    'y': 'y',
    # Add all other symbols from the v101 transcription
    # 'k': 'k',
    # 't': 't',
    # 'l': 'l',
    # 'r': 'r',
    # 's': 's',
    # 'm': 'm',
    # 'n': 'n',
    # 'f': 'f',
    # 'p': 'p',
    # 'h': 'h',
    # 'q': 'q',
    # 'g': 'g',
    # 'x': 'x',
    # ... etc.
}

def main():
    """
    Argument parser for command-line use.
    """
    parser = argparse.ArgumentParser(
        description="Clean and transliterate a Voynich v101 transcription file."
    )

    parser.add_argument(
        "input_file", 
        help="The path to the input v101 transcription file (e.g., 'v101.txt')."
    )

    parser.add_argument(
        "output_file", 
        help="The path to write the cleaned and replaced text (e.g., 'cleaned.txt')."
    )

    args = parser.parse_args()

    # Pass the defined mapping to the processing function
    process_file(args.input_file, args.output_file, VOYNICH_TO_LATIN_MAP)

if __name__ == "__main__":
    main()