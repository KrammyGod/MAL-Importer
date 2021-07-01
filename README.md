# MAL-Importer

Easily fast import anime to MAL (My Anime List)

## Installation

- Download all the files as a zip.
- Install Selenium for python by pasting `python -m pip install selenium` into the terminal.
- Add export.txt according to the rules in [formatting rules](#format).
- Enter username and password in settings.py (replace 'USERNAME' and 'PASSWORD').
- Run mal import.py by copying `python "mal.py"` into the terminal.

## <a name="format"></a> Formatting export.txt
Default will mark anime as "Completed" (all episodes watched).

Begin the list of "watching" by adding "# watching" (without the quotations) at the beginning of the anime(s) that you want to mark as "watching".

Switch to "completed" anytime you want by adding "# watched" above the anime(s).

See `export_example.txt` for an example of how to format it.

## Warnings
This only works with myanimelist.net links.

Using invalid myanimelist links will result in errors, please check the link again if it crashes.

In the case that MAL buttons change, I will update upon notice.

PS: You can watch the automation with an actual browser by toggling `_options.headless` and setting it to `False`.

## Code used
This is completely written in python, using selenium automation.

Fun little project I created with a bit of knowledge I obtained from working as QA Analyst at Axonify Inc.

## Support

For support, email shi.mark10@gmail.com or post in issues.

## Author

- [@KrammyGod](https://www.github.com/KrammyGod)
