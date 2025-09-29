---
title: battle
summary: How you can script campaign battle.
---


When the battle starts in campaign mode, following events are triggered, in order:
- PanelOpenedBattle
- BattleDeploymentPhaseCommenced (twice: for Attacker and Defender):
```lua
-- this is probably first place to gather some information about the battle
table.insert(events.BattleDeploymentPhaseCommenced, function(context)
    consul.log:info(tostring(conditions.BattleAllianceIsAttacker(context)))
    consul.log:info(tostring(conditions.BattleAllianceIsPlayers(context)))
end)
```
