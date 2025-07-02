### List of contents

* **day01**: Contains a program `helloworld.py` that prints "Hello World!"
* **day02**: Contains `circle.py` and `rectangle.py` that print the area and circumference/perimeter of the shapes when prompted for their required parameters
* **day03**: Contains the following:
1. Scripts `circle_user.py` and `rectangle_user.py` that calculate the area and circumference/perimeter like the scripts in **day02**, but now instead take values directly from the command line. \
   These can be executed by running the following command in any terminal (Command Prompt for Windows, Terminal for Linux, equivalent for Mac, provided Python is installed in the system): 
   ```ruby
   python <working-directory>\circle_user.py <radius>
   ```
   or
   ```ruby
   python <working-directory>\rectangle_user.py <height> <width>
   ```
2. Script `number_guessing_game_0.py`, wherein the user tries to guess a number the computer thinks up between 1 and 20. The user is told if their guess was greater or smaller than the guess (and by how much), or if their guess was correct.

* **day04**: Contains 7 scripts `number_guessing_game_0-6.py` in accordance to the [number guessing game exercise](https://slides.code-maven.com/python/exercise-number-guessing-game.html)

* **day05**: Contains the following scripts:
1. Scripts `dna_sequencing.py` and `extended_dna_sequencing.py` according to [this exercise](https://slides.code-maven.com/python/exercise-dna-sequencing.html) that extracts continuous sequences of DNA bases (A, C, T, G) from a string and returns an array of them sorted by length.
2. Scripts `count_digits_in_lists.py` and `count_words_in_lists.py` for the [count digits](https://slides.code-maven.com/python/exercise-count-digits.html) and [count words](https://slides.code-maven.com/python/exercise-count-words-in-list.html) exercises that count either the number of digits or words in a given list respectively.
3. Script `create_list.py` according to [this exercise](https://slides.code-maven.com/python/exercise-create-list.html) that creates a list of individual words from a given list of strings.
4. Script `is_prime.py` that checks if a number taken as input from the command line is prime or not.
5. Script `color_selecter_menu.py` that on taking user input (either through the command line or as a prompt) returns the name of the color they chose.
   
* **day06**: Contains the following scripts:
1. Script `color_selector_file.py` which adds the feature of providing an input file via the command line to the existing program `color_selector_menu.py`. To supply an input file:
   ```ruby
   python <working-directory>\color_selector_file.py colors.text
   ```
2. Script `count_digits_in_file.py` which similarly adds the input reading feature to the existing program. Example file for this is `numbers.txt`, and the program generates an output `report.txt`.
3. Script `rot13_file.py` which, given an input file (example given is `rot13-example.txt`), replaces the contents of the file with the [ROT 13 cipher](https://en.wikipedia.org/wiki/ROT13) of them.

* **day09**: Contains the following files:
1. Main script `timelog.py` that converts a schedule-like log `timelog.log` into a report `timelog.txt`.
2. Script `funcs.py` that contains functions which `timelog.py` uses.
3. Script `test_funcs_pytest.py` that tests the functions within `funcs.py`. Specifically, it tests the programmer-provided examples for the `hhmm_to_minutes()` function.

The user is encouraged to also check the documentation using `doctest` by running the following in the command line:
```ruby
python -m doctest funcs.py
```
There should ideally be no output i.e. the functions are working as intended for the provided examples.
