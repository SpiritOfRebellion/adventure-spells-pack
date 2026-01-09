# Table of Contents

- [Adventure Map Spells Overview](#adventure-map-spells-overview)
- [Known Issues](#known-issues)
- [TODOs](#todos)
- [Changelog](#changelog)

---

# Adventure Map Spells Overview

![Spells](https://raw.githubusercontent.com/vcmi-mods/adventure-spells-pack/refs/heads/vcmi-1.7/screenshots/screen05.png)

### **Air**
- **Accuracy**: All creatures receive +5/10/15% Damage when attacking at range until the end of the day.
- **Clarity**: All creatures receive mind spell immunity until the end of the day/day/week.
- **Darkness**: Creates a 1/2/3 tile radius of shroud for non-allied players with hero movement until the end of the day.
- **Divine Spirit**: All creatures receive +1/2/3 Morale until the end of the day.
- **Fleet Foot**: Gain +200/300/400 max movement points in next day.
- **Power of Haste**: All creatures receive +1/2/3 Speed until the end of the day.

### **Earth**
- **Dead Luck**: Reduces maximum Luck in combat to +2/+1/negates positive until the end of the day.
- **Death Call**: Increases Necromancy skill by 10/15/20% until the end of the day.
- **Dwarven Luck**: All creatures receive +1/2/3 Luck until the end of the day.
- **Herald of Death**: Reduces maximum Morale in combat to +2/+1/negates positive until the end of the day.
- **Hold Ground**: Creatures receive +3/6/9 Defense when defending in combat until the end of the day.
- **Power of Stone**: Creatures ignore 5/10/15% of enemy Attack until the end of the day.

### **Fire**
- **Demonic Power**: Creatures receive +5/10/15% Damage until the end of the day.
- **Raise Demons**: Necromancy raises Demons/Horned Demons/Horned Demons until the end of the day/day/week.
- **Shattering Strike**: Creatures' attacks ignore 5/10/15% of enemy Defense until the end of the day.

### **Water**
- **Benediction**: Cast all spells at Basic/Advanced/Expert proficiency until the end of the day.
- **Channel Power**: Gain +5/10/15% spell damage until the end of the day.
- **Seafaring**: Removes the boarding and unboarding penalties of ships until the end of the day/day/week.
- **Whirlpool Protection**: Protects the army from whirlpools until the end of the day/day/week.

### Global
- **Arcane Protection**: Creatures receive +5/10/15% spell damage reduction until the end of the day.
- **Empathy**: Nullifies the Morale penalty of mixing good and neutral units until the end of the day/day/week.
- **Griffin Eye**: See 1/2/3 square further into the shroud until the end of the day.
- **Magic Cushion**: Creatures receive +5/10/15% magical resistance until the end of the day.
- **Negotiations**: Reduces the cost of surrendering by -10/20/30% until the end of the day.

---

# Known Issues

- Lacks indication in the unit window that spells are in use;
- Casts per day bug: [#6659](https://github.com/vcmi/vcmi/issues/6659).

---

## TODO

1. Bug Fixes (see client log)

- [ ] `WARN [initialize] mod - Spell: target type empty - assumed NO_TARGET.`
- [ ] `ERROR [initialize] mod - Spell: no positiveness specified, assumed NEUTRAL.`
- [ ] redundancy in target types

2. Different file organization method

- [ ] Consider withdrawing the separation of mods into magic school catalogs, as new magic schools, let's say Demonology or Necromancy, may appear. The current division will make further rearrangements harder. The place for spell's school may be in description. 

# Changelog

## Version 1.5

### Modularization

- [x] Spells are now fully "pickable" in the Launcher.

### Casting sounds

- [x] Added 24 .ogg files.

### Documentation

- [x] Added a solid **README.md** to the GitHub repository.
- [x] Included html documentation for the mod in the VCMI Launcher (in English).

### Naming Conventions

- [x] Standardized all file and directory names to begin with lowercase letters. Names with multiple words are now using camelCase for improved clarity.

### Path Fixes

- [x] Configs
- [x] Spells
- [x] Icons
- [x] Translations

---
