---
title: payloads
summary: A brief description of my document.
---

Confirmed payloads that are working.
They can be executed like that:
```lua
scripting.game_interface:trigger_custom_dilemma(
        'rom_rome',
        "move_capital_rome",
        "payload { rebellion rom_italia_latium; }",
        "",
        true
)
```

```lua
"payload { money 5000; }"
"payload { unit_restriction { unit_key Rom_Hastati; disable;  } }"
"payload { effect_bundle { bundle_key wealth_local_commerce_15_plus; turns 379; } }"
"payload { grant_agent { agent_key dignitary; location capital; } }"
"payload { rebellion rom_italia_latium; }"
"payload { set_capital rom_italia_latium; }"
```


To be done
```
money
honour
town_wealth
clan_fame
game_victory
rebellion
issue_mission
demolish_chain
damage_buildings
diplomacy_change
building_restriction
unit_restriction
grant_agent
effect_bundle
kill_character
adjust_loyalty_for_character
set_capital
Failed parsing clan fame change
grant_unit
effect_bundle
Unhandled payload token
issue_mission requires an argument
game_victory does not take an argument - ignoring the argument
adjust_loyalty_for_character payload currently unsupported via direct scripting
kill_character payload currently unsupported via direct scripting
diplomacy_change payload currently unsupported via direct scripting
unit_key
enable
disable
global
Neither enable or disable specified
Both enable and disable specified
Unrecognised unit key
building_level_key
event_restricted_only
Unrecognised building level key
damage_buildings not permitted in front-end victory condition payloads
location
Failed parsing location
Failed parsing building chain
Failed parsing town wealth change
Payload not supported in front-end victory condition
Failed setting rebellion location
bundle_key
turns
Invalid effect bundle key
Invalid turns specified
grant_agent not permitted in front-end victory condition payloads
agent_key
Failed parsing agent_key
Failed parsing location
unit_key
Failed parsing unit_key
Failed setting payload honour change
Failed setting payload treasury change
```