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

## Working Payloads

#### `money`
```lua
"payload { money 5000; }"
```

#### `unit_restriction`
```lua
"payload { unit_restriction { unit_key Rom_Hastati; disable;  } }"
```

#### `effect_bundle`
```lua
"payload { effect_bundle { bundle_key wealth_local_commerce_15_plus; turns 379; } }"
```

#### `grant_agent`
```lua
"payload { grant_agent { agent_key dignitary; location capital; } }"
```

#### `rebellion`
```lua
"payload { rebellion rom_italia_latium; }"
```

#### `set_capital`
```lua
"payload { set_capital rom_italia_latium; }"
```

## Probably working

#### `issue_mission`


## To be done / Unconfirmed

#### `honour`
#### `town_wealth`
#### `clan_fame`
#### `game_victory`
#### `demolish_chain`
#### `damage_buildings`
#### `building_restriction`
#### `grant_unit`
