# Disable Achievements

Modification for Crusader Kings 3 that disables all achievements.

## Technical requirements

* Crusader Kings version Crown 1.18.*.

## Language support

All.

## Motivation

Some code implementing achievements in base game version 1.15.0.2 is buggy.

I only play in Elder Kings universe. I usually have my own targets, such as

* most of my dynasty are witches, some are vampires;
* most of my dynasty have pureblood and other good genes;
* most of my dynasty are of my custom religion and my custom culture;
* all powerful dynasties such as dark elves houses are dead or landless;
* I control a good piece of land.

Those targets are not accounted for in achievements.

Achievements accounting is nothing useful for me, it just spams my `error.log` (at least on 1.15.0.2) and wastes CPU and RAM resources. Since the game engine is not fully parallelized, it is CPU-hungry (especially late-game). Calculaing values no one needs is a luxury I cannot afford.

I therefore decided to completely disable achievements.

## Warning

There will be some extra messages in `error.log`, like `Variable 'ce1_canonized_achievement_unlocked' is set but is never used` or `Variable 'ep2_im_in_my_elements_achievement_terrain_list' is used but is never set`. Those only appear at game load but not during gameplay.

## Installation

1. Unpack to mod directory, omitting `readme.md` (this file).
2. Activate via launcher called `dowser.exe`.

For more details on mod installation, see [wiki](https://ck3.paradoxwikis.com/Modding#Installing_mods_manually).

## My mods

List of my modifications for CK3, and my load order is [here](https://gist.github.com/krisk0/3c51136a877afd606c184a575400922f).
