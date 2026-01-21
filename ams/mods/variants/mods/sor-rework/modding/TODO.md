# Update 1.6

- [ ] Cast once per day is now an optional submod (there may be other solutions). Nah, it's a good change.
- [x] Simplify spells directory.
- [ ] School type separation now in spell's description.
- [ ] Make most off the spells under ONE_WEEK or N_DAYS type (figure out how this one works) duration type.
- [ ] Make casting adventure spells drain some movement points (known from Town Portal).
- [ ] Include core Disguise spell to the changes.
- [ ] Fix some sounds and it's metadata.
- [ ] Try to do automatic translations at least the ones which will be lost due to rearrangement of mod structure: Chineese, Spanish, Polish, Russian, Portuguese, Czech, German, French, Ukrainian
- [ ] Try to change how spells are working with OPENING_BATTLE_SPELL
- [ ] Change name from raiseDemons to Dark Ritual

# Examples 

--- 
"adventureEffect" : {
    "type" : "generic",
    "castsPerDay" : 0,
    "castsPerDayXL" : 0,
    "bonuses" : {
        "fly" : {
            "type" : "FLYING_MOVEMENT",
            "duration" : "ONE_DAY",
            "val" : 40,
            "valueType" : "INDEPENDENT_MIN"
        }
    }
}

--- 
OPENING_BATTLE_SPELL

In battle, army affected by this bonus will cast spell at the very start of the battle. Spell is always cast at expert level.

    subtype: spell identifier
    val: duration of the spell, in rounds
    addInfo - spell mastery level (1 - Basic, 3 - Expert)

castExpertBloodlust {
	"type": "OPENING_BATTLE_SPELL",
	"subtype": "bloodlust",
	"value": 999,
	"addInfo": 3
}


--- 
GROWS_WITH_LEVEL

Effect: Updates val to ceil(valPer20 * floor(heroLevel / stepSize) / 20)

Example: The following updater will cause a bonus to grow by 6 for every 40 levels. At first level, rounding will cause the bonus to be 0.

"updater" : {
    "type" : "GROWS_WITH_LEVEL",
    "valPer20" : 6,
    "stepSize" : 2
}

Example: The following updater will cause a bonus to grow by 3 for every 20 levels. At first level, rounding will cause the bonus to be 1.

"updater" : {
    "type" : "GROWS_WITH_LEVEL",
    "valPer20" : 3,
    "stepSize" : 1
}
---
MANA_REGENERATION

Restores specific amount of mana points for affected heroes on new turn

    val: amount of spell points to restore

MANA_PERCENTAGE_REGENERATION

Restores specific percentage of mana pool for affected heroes on new turn. If hero has both MANA_REGENERATION and MANA_PERCENTAGE_REGENERATION, only bonus that gives more mana points will be active

    val: percentage of spell points to restore
---
"effects" : {
					"primarySkill" : {
						"val" : 3,
						"type" : "PRIMARY_SKILL",
						"subtype" : "primarySkill.attack",
						
adventureEffect" : {
					"type" : "dimensionDoor",
					"movementPointsRequired" : 0,
					"movementPointsTaken" : 300,
---
"mysticism" : {
		"index" : 8,
		"specialty" : [
			"main"
		],
		"base" : {
			"effects" : {
				"main" : {
					"type" : "MANA_REGENERATION",
					"valueType" : "BASE_NUMBER"
				}
			}
		},
		"basic" : {
			"effects" : {
				"main" : { "val" : 1 }
			}
		},
		"advanced" : {
			"effects" : {
				"main" : { "val" : 2 }
			}
		},
		"expert" : {
			"effects" : {
				"main" : { "val" : 3 }
			}
		}
	},
---
"offence" : {
		"index" : 22,
		"specialty" : [
			"main"
		],
		"base" : {
			"effects" : {
				"main" : {
					"subtype" : "damageTypeMelee",
					"type" : "PERCENTAGE_DAMAGE_BOOST",
					"valueType" : "BASE_NUMBER"
				}
			}
		},
		"basic" : {
			"effects" : {
				"main" : { "val" : 10 }
			}
		},
		"advanced" : {
			"effects" : {
				"main" : { "val" : 20 }
			}
		},
		"expert" : {
			"effects" : {
				"main" : { "val" : 30 }
			}
		}
	},
--- 

"learning" : {
		"index" : 21,
		"specialty" : [
			"main"
		],
		"base" : {
			"effects" : {
				"main" : {
					"type" : "HERO_EXPERIENCE_GAIN_PERCENT",
					"valueType" : "PERCENT_TO_BASE"
				}
			}
		},
		"basic" : {
			"effects" : {
				"main" : { "val" : 5 }
			}
		},
		"advanced" : {
			"effects" : {
				"main" : { "val" : 10 }
			}
		},
		"expert" : {
			"effects" : {
				"main" : { "val" : 15 }
			}
		}
	},
