---
title: battle
summary: How you can script campaign battle.
---


When the battle starts in campaign mode, following events are triggered, in order:
- PanelOpenedBattle
- BattleDeploymentPhaseCommenced (twice: for Attacker and Defender):
- BattleConflictPhaseCommenced
```lua
-- this is probably first place to gather some information about the battle
table.insert(events.BattleDeploymentPhaseCommenced, function(context)
    consul.log:info(tostring(conditions.BattleAllianceIsAttacker(context)))
    consul.log:info(tostring(conditions.BattleAllianceIsPlayers(context)))
end)
```

Events that trigger during battle:
- BattleUnitRouts
- BattleUnitAttacksEnemyUnit
- BattleCommandingUnitRouts

Theres "BattleUnitAttacksEnemyUnit" that can be checked like:
```lua
-- Check directions
table.insert(events.BattleUnitAttacksEnemyUnit, function(context)
    local directions = { "front", "left_flank", "right_flank", "behind" }

    for _, dir in ipairs(directions) do
        if conditions.BattleEnemyDirectionOfMeleeAttack(dir, context) then
            pwrite("enemy_direction_attack " .. dir)
        end
        if conditions.BattlePlayerDirectionOfMeleeAttack(dir, context) then
            pwrite("player_direction_attack " .. dir)
        end
    end
end)

-- Check action statuses
table.insert(events.BattleUnitAttacksEnemyUnit, function(context)
    local statuses = {
        "charging", "exhausted", "fighting_melee", "firing",
        "hiding", "idling", "moving", "moving_fast",
        "pursue_routers", "rallying", "routing", "wavering"
    }

    local player_states = {}
    local enemy_states = {}

    for _, status in ipairs(statuses) do
        if conditions.BattlePlayerUnitActionStatus(status, context) then
            table.insert(player_states, status)
        end
        if conditions.BattleEnemyUnitActionStatus(status, context) then
            table.insert(enemy_states, status)
        end
    end

    if #player_states > 0 then
        pwrite("player_action_status: " .. table.concat(player_states, ", "))
    end
    if #enemy_states > 0 then
        pwrite("enemy_action_status: " .. table.concat(enemy_states, ", "))
    end
end)

```