# The Voynich Transcription Tool (TVTT)
Create your own Voynich Manuscript transcription or translation based on the v101 transcription.

## Features:
  - Positional context mapping at the front and end of words using syntax (see below).
  - Multi-character input and output mapping (Eg. "55=4o")
  - Syntax features for functionality purposes. (Note: The same character can be mapped multiple times if you have different syntax on each line(s).)

## Tutorial:
  **NOTE:** Do not touch v101.txt and v101_cleaned.txt!<br />
  **NOTE:** Each mapping must be on a new line!

  **Syntax:** (Note: Special syntax only works in the number_mapping.txt file, not the output_mapping.txt file.)<br />
  - @ at the end of a line means use that mapping if the character is at the start of the line (Eg. "56=9@").<br />
  - / at the end of a line means use that mapping if the character is at the end of the line (Eg. "57=9/").<br />
  - ) at the beginning of a line in the input_mapping.txt file means that line will be ignored (Essentially commented out) (Eg. ")58=9").<br />
  - Nothing special in the line just works normally for any position in the transcription (Note: Multiple of the same character can be used if you put special syntax on the line.)

  **Instructions:**
  
  &emsp;1. Remap the number_mapping.txt file for each v101.txt transcription character (Can be mulitple letters corrosponding to one number, Eg. "60=4o") (Optionally using the special syntax, Eg. "59=9/")<br />
  
  &emsp;2. Remap the output_mapping.txt file with the corosponding output letter(s) (Can be mulitple letters, Eg. "59=us")<br />
  
  &emsp;3. Run the main.py program and open the output.txt file to see your transcription (Using the examples above, setting "59=9/" in the number_mapping.txt and "59=us" in the output_mapping.txt file will replace all the "9" characters at the end of words with "us" in the output.txt file.)

  **Notes:**
      Thanks for checking this tool out (or at least reading this post)! If you have feature requests or ideas, please comment! This is a work in progress and I'd love suggestions!
