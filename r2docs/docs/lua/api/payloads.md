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
