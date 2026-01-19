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

# SoR Overhaul Mod Overview (quick)

### **Air**
- **Accuracy**: casts mass 'Precision' spell at the begenning of a battle. Drains mana. Lasts until next week.

### Global
- **Arcane Protection**: casts mass 'Spellguard' spell at the beginning of a battle (it adds 5/10/15/20 spell immunity, known from Golems). Drains mana. Lasts until next week.

### **Water**
- **Benediction**: A Hero can cast all spells at Basic/Basic/Advanced/Expert proficiency. Drains mana and 'Power'. Lasts until next week.


# Known Issues

- Lacks proper indication in the unit window about true effects of a spell. This also applies to updates, if a spell has a cumulating effect. Currently only base stats are displayed.
- Currently there is no way to indicate that spells' duration ended. Partially solved with the durations set to - until next week.
- A player can cast a spell which drains resources even if there is nothing to drain. Partially solved with variety of costs.
- The AI doesn't use the spells.
- Casts per day bug: [#6659](https://github.com/vcmi/vcmi/issues/6659).

---

## TODO

1. Bug Fixes (see client log)
- [ ] `WARN [initialize] mod - Spell: target type empty - assumed NO_TARGET.`
- [ ] `ERROR [initialize] mod - Spell: no positiveness specified, assumed NEUTRAL.`
- [ ] redundancy in target types
2. Support for more towns (if neccessary).
3. Add restrictions to the spells - eg. 'Call the Legion' restricted to a Knight, 'Benediction' prohibited to a Death Knight and so on (will it crash the game?). Also check out are there should be restrictions to creatures.

# Changelog

## Version 2.0

### Adventure Spells

- [ ] Duration of the spells changed to ONE_WEEK in most cases, but it doesn't mean 7 days everytime. Entering a new week should be a signal to renew the spells,
- [ ] Changed behavior and effects of the spells, with preserving their original characer. Most of them can now be dispelled in a battle.
- [ ] Variety of spell costs implemented: mana costs, movement costs, primary skills costs, resources costs. Read the description, before casting.
- [ ] Disguise spell duration also elongated,
- [ ] The spells are rare to find (max. gain chance = 3; default 0),
- [ ] New battle spells added to simulate some effects. Unavailable as default, but can be enabled.
- [ ] Whatever possible is kept optional.
- [ ] Preserved original mechanic of the spells (for dependencies, different variants and further development).

### Mod structure

- [x] Simplified directory three, any unnecessary directories deleted. Schools indications moved to description.
- [ ] Redundancy reduced in the code by using "base" object, which was not present.
- [ ] Changed main catalog name name from 'adventure-spell-pack' to 'ams' (from Adventure Map Spells) for shorter object chains.
- [ ] Changed 'Raise Demons' name to 'Call the Legion', due to potential conflicts.

### Other

- [ ] some sound effects louder, some replaced, plus fixed metas,
- [ ] update mod.json descriptions
- [ ] documentation on GitHub and in the Launcher.

### Translations

- [ ] Fixed paths.
- [x] Some translations lost due structural changes.
- [ ] Chineese, complete, autogenerated.
- [ ] Spanish, complete, autogenerated.
- [ ] Polish, complete.
- 

---

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
