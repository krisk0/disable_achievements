# Disable Achievements

Modification for Crusader Kings 3 that disables all achievements.

## Technical requirements

* Crusader Kings version Crown 1.15.0.2.

Do not know if the mod works for other versions.

## Motivation

I recently discovered that some of the code implementing achievements in base game is buggy.

I usually have my own targets, such as

* most of my dynasty are witches;
* most of my dynasty have scarab blood and pureblood and other good genes;
* most of my dynasty are of my custom religion and my custom culture;
* all dark elves houses' members are dead or landless;
* I am the emperor of Morrowind.

Achievements accounting is just a waste of CPU resources for me.

I therefore decided to completely disable achievements.

## Implementation note

To get rid of scripts, file `common/scripted_effects/00_achievement_effects.txt` need to be sanitized. For copyright issues, I do not publish the sanitized file. Instead, I publish a script that empties the file.

## Installation

1. Install Python3 interpreter.
2. Unpack .zip.
3. Change to directory containing `readme.md` (this file), run script: `<PYTHON3> crunch.py <SEARCH_PATH>` where <PYTHON3> is the name of the interpreter and <SEARCH_PATH> is the path to base game directory (any directory that contains base game .txt will do, even whole disk).
4. On success you will see message like `Success, 9 empty effects`.
5. Put all files except `readme.md` and `crunch.py` into mod directory.
6. Activate the mod via launcher called `dowser.exe`.

For more details on mod installation, see [wiki](https://ck3.paradoxwikis.com/Modding#Installing_mods_manually).
