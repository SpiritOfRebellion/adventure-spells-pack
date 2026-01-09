# For Modders

## Pitfalls
1. Mod is standarized for **camelCase naming convention** also to files and folders, to avoid future typos and make easier to edit and generate (e.g. shell scripts). While working on the project, I noticed that naming files like `spellIcon.png` instead of `spellIconBenediction.png` could create more recognizable patterns.


2. **Icons** will replace each other if won't be placed in an additional folder, for example: 
- accuracy/content/sprites/**accuracy**/*.png 
- clarity/content/sprites/**clarity**/*.png

Correct paths expample:

```
// herealdOfDeath.json example
...
"graphics": {
      "iconBook": "heraldOfDeath/spellBook",
    	"iconScroll": "heraldOfDeath/spellScroll",
    	"iconScenarioBonus": "heraldOfDeath/spellBonus",
    	"iconEffect": "heraldOfDeath/spellEffect"
    },
...
```
3. Object chains in translation files looks like this: `spell.adventure-spells-pack.air.divinespirit.divineSpirit.description.advanced` notice that **divinespirit** has no capital letter, while the second **divineSpirit** has.

---

## Data sets

Were helpful for AI prompts and documentation.

### Spells added
```
json_data='{
    "air": ["accuracy", "clarity", "darkness", "divineSpirit", "fleetFoot", "powerOfHaste"],
    "earth": ["deadLuck", "deathCall", "dwarvenLuck", "heraldOfDeath", "holdGround", "powerOfStone"],
    "fire": ["demonicPower", "raiseDemons", "shatteringStrike"],
    "water": ["benediction", "channelPower", "seafaring", "whirlpoolProtection"],
    "global": ["arcaneProtection", "empathy", "griffinEye", "magicCushion", "negotiations"]
}'
```

### Submods filesystem pattern

```
/{$element} 
/{$element}/mod.json 
/{$element}/mods/{$spell}
/{$element}/mods/{$spell}/mod.json
/{$element}/mods/{$spell}/content/sprites/*.png
/{$element}/mods/{$spell}/content/sounds/*.ogg
/{$element}/mods/{$spell}/content/config/spells/{$spell}.json
```
