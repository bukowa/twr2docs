---
title: conditions
summary: A brief description of my document.
---

# Introduction
Not all conditions are documented.  
Not all conditions are expected to work.  

Below list is result of extracting the game decompiled code.  
You should not rely 100% on the below list, as it may contain errors or missing conditions.

## AdjacentRegionRebelling

**Example:** `AdjacentRegionRebelling()`

**Arguments:** `DAT_1173e900`

**Description:**  
Are any of the regions adjacent to the region rebelling

**Author:** `DAT_117a1590`

**Function:** `FUN_108109c0`



## AnyFactionDestroyedLastTurn

**Example:** `AnyFactionDestroyedLastTurn()`

**Arguments:** `DAT_1173e900`

**Description:**  
Has any faction been destroyed since the last turn

**Author:** `DAT_1179b680`

**Function:** `FUN_10810a80`



## ArmyIsAlliedCampaign

**Example:** `ArmyIsAlliedCampaign()`

**Arguments:** `DAT_1173e900`

**Description:**  
Does the army belong to a faction allied to the player faction

**Author:** `DAT_117a1590`

**Function:** `FUN_10810af0`



## ArmyIsLocalCampaign

**Example:** `ArmyIsLocalCampaign()`

**Arguments:** `DAT_1173e900`

**Description:**  
Does the army belong to the player faction?

**Author:** `DAT_117a1590`

**Function:** `FUN_10810bb0`



## BattleAllianceHasDeployables

**Example:** `BattleAllianceHasDeployables()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if the alliance has deployables

**Author:** `Dylan`

**Function:** `FUN_10163ca0`



## BattleAllianceIsAttacker

**Example:** `BattleAllianceIsAttacker()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if the alliance is the attacker from the campaign map

**Author:** `Ingimar`

**Function:** `FUN_10163d60`



## BattleAllianceIsPlayers

**Example:** `BattleAllianceIsPlayers()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if the alliance contains the players army

**Author:** `Ingimar`

**Function:** `LAB_10163e20`



## BattleAllianceNumberOfShips

**Example:** `BattleAllianceNumberOfShips()`

**Arguments:** `No parameters needed`

**Description:**  
Returns the number of ships in all the armies of the alliance

**Author:** `Ingimar`

**Function:** `FUN_10163f10`



## BattleAllianceNumberOfUnits

**Example:** `BattleAllianceNumberOfUnits()`

**Arguments:** `No parameters needed`

**Description:**  
Returns the number of units in all the armies of the alliance

**Author:** `Ingimar`

**Function:** `FUN_10163ff0`



## BattleCommanderIsGeneral

**Example:** `BattleCommanderIsGeneral()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if the the alliance has a general and not just a colonel

**Author:** `Ingimar`

**Function:** `LAB_10164060`



## BattleEnemyAlliancePercentageCanHide

**Example:** `BattleEnemyAlliancePercentageCanHide()`

**Arguments:** `No parameters needed`

**Description:**  
Checks the percentage of enemy units ( in alliance ) that can hide, returns a percentage

**Author:** `Ingimar`

**Function:** `FUN_10164150`



## BattleEnemyAlliancePercentageOfClassAndCategory

**Example:** `BattleEnemyAlliancePercentageOfClassAndCategory(\"class\", \"category\")`

**Arguments:** `Two lowercase strings, first being the particular class string ( see unit_stats_land table ) and second being the category string ( see units table )`

**Description:**  
Takes in class and category of a particular unit and goes through every enemy army, returning the percentage of units that match the class and category

**Author:** `Ingimar`

**Function:** `FUN_10164240`



## BattleEnemyAlliancePercentageOfMountType

**Example:** `BattleEnemyAlliancePercentageOfMountType(\"mount_type\")`

**Arguments:** `A lowercase string with the unit\'s mount type to be checked ( see type in battle_entities table )`

**Description:**  
Determine the percentage of units in the enemies army that have the type of mount passed to the condition

**Author:** `Ingimar`

**Function:** `FUN_101643e0`



## BattleEnemyAlliancePercentageOfSpecialAbility

**Example:** `BattleEnemyAlliancePercentageOfSpecialAbility(\"ability\")`

**Arguments:** `Special Ability string : pike_square_formation, pike_wall_formation, square_formation, wedge_formation, diamond_formation, light_infantry_behaviour, loose_formation, fire_and_advance, plug_bayonets, dismount, unlimber, none`

**Description:**  
Checks all of the Armies in the enemy alliances for the particular special ability

**Author:** `Ingimar`

**Function:** `FUN_10164530`



## BattleEnemyAlliancePercentageOfUnitCategory

**Example:** `BattleEnemyAlliancePercentageOfUnitCategory(\"category\")`

**Arguments:** `One lowercase string with the unit\'s category name ( see units table )`

**Description:**  
Take in the name of the unit\'s category and returns the percentage of units in the alliance that match the given category

**Author:** `Ingimar`

**Function:** `FUN_10164650`



## BattleEnemyAlliancePercentageOfUnitClass

**Example:** `BattleEnemyAlliancePercentageOfUnitClass(\"class\")`

**Arguments:** `One lowercase string with the unit\'s class name ( see unit_stats_land table )`

**Description:**  
Takes in the name of the unit\'s class and returns the percentage of units in the alliance that match the given class

**Author:** `Ingimar`

**Function:** `FUN_101647f0`



## BattleEnemyDirectionOfMeleeAttack

**Example:** `BattleEnemyDirectionOfMeleeAttack(\"left_flank\")`

**Arguments:** `Possible string paramaters are \"front\", \"left_flank\", \"right_flank\" and \"behind\`

**Description:**  
Returns true if the passed parameter matches the direction of melee attack for the enemy unit

**Author:** `Ingimar`

**Function:** `FUN_10164990`



## BattleEnemyHasMissileSuperiority

**Example:** `BattleEnemyHasMissileSuperiority()`

**Arguments:** `No paramaters needed`

**Description:**  
Returns true if the combined missile streangth of the enemy is greater than the missile streangth of the player

**Author:** `Ingimar`

**Function:** `FUN_10164ab0`



## BattleEnemyShipActionStatus

**Example:** `BattleEnemyShipActionStatus`

**Arguments:** `Single string with action status`

**Description:**  
Returns true if the action status of the enemy ship matches : dismasted, firing, hull_damaged, routing, sinking, wavering.

**Author:** `Ingimar`

**Function:** `LAB_10164e60`



## BattleEnemyShipOnFire

**Example:** `BattleEnemyShipOnFire()`

**Arguments:** `No parameters needed`

**Description:**  
Checks whether any of the enemies ships are on fire, returns true or false

**Author:** `Ingimar`

**Function:** `FUN_10164f50`



## BattleEnemyUnitActionStatus

**Example:** `BattleEnemyUnitActionStatus(\"hiding\")`

**Arguments:** `Single string with action status`

**Description:**  
Returns true if the action status of the enemy unit matches : charging, exhausted, fighting_melee, firing, hiding, idling moving, moving_fast, pursue_routers, rallying, routing, wavering.

**Author:** `Ingimar`

**Function:** `FUN_10165080`



## BattleEnemyUnitCategory

**Example:** `BattleEnemyUnitCategory(\"category\")`

**Arguments:** `One lowercase string with the enemies unit\'s category name ( see units table )`

**Description:**  
Takes in a unit category string and returns true if there is an enemy and it matches the category of the enemy unit

**Author:** `Ingimar`

**Function:** `FUN_10165150`



## BattleEnemyUnitClass

**Example:** `BattleEnemyUnitClass(\"class\")`

**Arguments:** `One lowercase string with the unit\'s class name ( see unit_stats_land table )`

**Description:**  
Takes in a unit class string and returns true if it matches the unit class of the enemy unit

**Author:** `Ingimar`

**Function:** `FUN_10165230`



## BattleEnemyUnitCurrentFormation

**Example:** `DAT_1173dad0`

**Arguments:** `Takes in a single string which can be one of the following : block_formation, pike_square_formation, pike_wall_formation, square_formation, diamond_formation, wedge_formation, light_infantry_behaviour.`

**Description:**  
Returns true if the unit has an enemy and the string matches the current formation employed by the enemy, otherwise it returns false

**Author:** `Ingimar`

**Function:** `FUN_10165300`



## BattleEnemyUnitOnLeftFlank

**Example:** `BattleEnemyUnitOnLeftFlank()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if there\'s an enemy unit on the left flank

**Author:** `Ingimar`

**Function:** `FUN_101653f0`



## BattleEnemyUnitOnRightFlank

**Example:** `BattleEnemyUnitOnRightFlank()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if there\'s an enemy unit on the right flank

**Author:** `Ingimar`

**Function:** `FUN_10165470`



## BattleEnemyUnitSpecialAbilitySupported

**Example:** `BattlePlayerUnitSpecialAbilitySupported(\"ability\")`

**Arguments:** `Special Ability string : pike_square_formation, pike_wall_formation, square_formation, wedge_formation, diamond_formation, light_infantry_behaviour,  loose_formation, fire_and_advance, plug_bayonets, fougasse_improved, fougasse_basic, wooden_stakes, chevaux_de_frise, gabionade, earthworks, dismount, unlimber, none`

**Description:**  
If there is an enemy unit then the condition checks all of the enemy unit\'s special abilities and returns true if the unit has the special ability

**Author:** `Ingimar`

**Function:** `FUN_101654f0`



## BattleEnemyUnitTechnologySupported

**Example:** `BattleEnemyUnitTechnologySupported(\"ring_bayonets\")`

**Arguments:** `Technology string : ring_bayonets, socket_bayonets, fire_mounted`

**Description:**  
Checks whether the unit has the technology passed in and returns true if the unit has the technology

**Author:** `Ingimar`

**Function:** `FUN_101655e0`



## BattleHasCoverBuildings

**Example:** `BattleHasCoverBuildings()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if it finds an occupiable building

**Author:** `Ingimar`

**Function:** `FUN_10165690`



## BattleHasCoverWalls

**Example:** `BattleHasCoverWalls()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if the battlefield has walls that the men can take cover against

**Author:** `Ingimar`

**Function:** `FUN_10165740`



## BattleIsAmbushConflict

**Example:** `BattleIsAmbushConflict()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if there is a fort in the battle

**Author:** `Ingimar`

**Function:** `FUN_101657c0`



## BattleIsLandConflict

**Example:** `BattleIsLandConflict()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if battle is being fought on land (this will NOT return true for fort battles)

**Author:** `Ingimar`

**Function:** `FUN_10165830`



## BattleIsNavalConflict

**Example:** `BattleIsNavalConflict()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if battle is being fought on sea

**Author:** `Ingimar`

**Function:** `FUN_101658d0`



## BattleIsSiegeConflict

**Example:** `BattleIsSiegeConflict()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if there is a fort in the battle

**Author:** `Ingimar`

**Function:** `FUN_10165960`



## BattlePlayerAllianceDefendingHill

**Example:** `BattlePlayerAllianceDefendingHill()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if a unit in the alliance is stationed on a hill

**Author:** `Ingimar`

**Function:** `FUN_101659f0`



## BattlePlayerAlliancePercentageCanHide

**Example:** `BattlePlayerAlliancePercentageCanHide()`

**Arguments:** `No parameters needed`

**Description:**  
Checks the percentage of player units ( in alliance ) that can hide, returns a percentage

**Author:** `Ingimar`

**Function:** `FUN_10165b40`



## BattlePlayerAlliancePercentageGuerrillas

**Example:** `BattlePlayerAlliancePercentageGuerrillas`

**Arguments:** `A single string representing the class of a unit ( see unit_stats_land table )`

**Description:**  
Goes through the players alliance and searches for all the units that have guerrilla deployment

**Author:** `Scott`

**Function:** `LAB_10165bb0`



## BattlePlayerAlliancePercentageOfAmmoType

**Example:** `BattlePlayerAlliancePercentageOfAmmoType(\"bullet\")`

**Arguments:** `Takes in a string describing the shottype ( see projectile_shot_type_enum_table )`

**Description:**  
Returns the percentage of units in the alliance that have the specified ammo type

**Author:** `Ingimar`

**Function:** `FUN_10165ce0`



## BattlePlayerAlliancePercentageOfClassAndCategory

**Example:** `BattlePlayerAlliancePercentageOfClassAndCategory(\"class\", \"category\")`

**Arguments:** `Two lowercase strings, first being the particular class string (see unit_stats_land table ) and second being the category string ( see units table )`

**Description:**  
Takes in Class and Category of a particular unit and goes through players army and returns the percentage that match the class and category

**Author:** `Ingimar`

**Function:** `FUN_10165e60`



## BattlePlayerAlliancePercentageOfMountType

**Example:** `BattlePlayerPercentageOfMountType(\"mount_type\")`

**Arguments:** `A lowercase string with the unit\'s mount type to be checked ( see type in battle_entities table )`

**Description:**  
Determine the percentage of units in the players army that have the type of mount passed to the condition

**Author:** `Ingimar`

**Function:** `FUN_10165fd0`



## BattlePlayerAlliancePercentageOfSpecialAbility

**Example:** `BattlePlayerAlliancePercentageOfSpecialAbility(\"ability\")`

**Arguments:** `Special Ability string : pike_square_formation, pike_wall_formation, square_formation, wedge_formation, diamond_formation, light_infantry_behaviour, loose_formation, fire_and_advance, plug_bayonets, dismount, unlimber, none`

**Description:**  
Checks all of the Armies in the players alliance for the special ability

**Author:** `Ingimar`

**Function:** `FUN_101660d0`



## BattlePlayerAlliancePercentageOfTechnology

**Example:** `BattlePlayerAlliancePercentageOfTechnology(\"ring_bayonets\")`

**Arguments:** `Technology string : ring_bayonets, socket_bayonets, fire_mounted`

**Description:**  
Checks all of the Armies in the players alliance for the technology and returns the percentage of those that have it

**Author:** `Ingimar`

**Function:** `FUN_10166170`



## BattlePlayerAlliancePercentageOfUnitCategory

**Example:** `BattlePlayerAlliancePercentageOfUnitCategory(\"category\")`

**Arguments:** `A single string representing the category of a unit ( see units table )`

**Description:**  
Goes through the players alliance and searches for all the units that fit the given category description

**Author:** `Ingimar`

**Function:** `FUN_101661f0`



## BattlePlayerAlliancePercentageOfUnitClass

**Example:** `BattlePlayerAlliancePercentageOfUnitClass(\"class\")`

**Arguments:** `A single string representing the class of a unit ( see unit_stats_land table )`

**Description:**  
Goes through the players alliance and searches for all the units that fit the given class description

**Author:** `Ingimar`

**Function:** `FUN_10166350`



## BattlePlayerAllianceToEnemyAllianceRatio

**Example:** `BattlePlayerAllianceToEnemyAllianceRatio() > 0.5 would mean that the players alliance has half as many men as the enemy\'s alliance`

**Arguments:** `No parameters needed`

**Description:**  
Returns the ratio PlayersAlliance/EnemyAlliance in terms of men on the battlefield

**Author:** `Ingimar`

**Function:** `FUN_101664b0`



## BattlePlayerDefendingFort

**Example:** `BattlePlayerDefendingFort()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if player is still in control of the fort and is tasked to defend it.

**Author:** `Ingimar`

**Function:** `FUN_10166720`



## BattlePlayerDirectionOfMeleeAttack

**Example:** `BattlePlayerDirectionOfMeleeAttack(\"left_flank\")`

**Arguments:** `Possible string paramaters are \"front\", \"left_flank\", \"right_flank\" and \"behind\`

**Description:**  
Returns true if the passed parameter matches the direction of melee attack for the unit

**Author:** `Ingimar`

**Function:** `FUN_10166810`



## BattlePlayerDirectionOfMissileAttack

**Example:** `BattlePlayerDirectionOfMissileAttack(\"right_flank\")`

**Arguments:** `Possible string paramaters are \"front\", \"left_flank\", \"right_flank\" and \"behind\`

**Description:**  
Returns true if the passed parameter matches the direction of missile attack for the unit

**Author:** `Ingimar`

**Function:** `FUN_10166900`



## BattlePlayerSailsPercentageDamaged

**Example:** `BattlePlayerSailsPercentageDamaged()`

**Arguments:** `No parameters needed`

**Description:**  
Returns the floating point value of percentage damaged in the range 0.0 to 100.0

**Author:** `Ingimar`

**Function:** `FUN_10166a20`



## BattlePlayerShipActionStatus

**Example:** `BattlePlayerShipActionStatus(\"hiding\")`

**Arguments:** `Single string with action status`

**Description:**  
Returns true if the action status of the ship : dismasted, firing, hull_damaged, routing, sinking, wavering.

**Author:** `Ingimar`

**Function:** `FUN_10166aa0`



## BattlePlayerShipClass

**Example:** `BattlePlayerShipClass(\"class\")`

**Arguments:** `One lowercase string with the unit\'s class name ( see unit_stats_naval table )`

**Description:**  
Takes in a ship class and returns true if it matches the ship class of the ship

**Author:** `Ingimar`

**Function:** `FUN_10166b40`



## BattlePlayerUnitActionStatus

**Example:** `BattlePlayerUnitActionStatus(\"hiding\")`

**Arguments:** `Single string with action status`

**Description:**  
Returns true if the action status of the unit matches UNIT: charging, exhausted, fighting_melee, firing, hiding, idling moving, moving_fast, pursue_routers, rallying, routing, wavering.

**Author:** `Ingimar`

**Function:** `FUN_10166b80`



## BattlePlayerUnitAmmoType

**Example:** `BattlePlayerUnitAmmoType(\"bullet\")`

**Arguments:** `Takes in a string describing the shottype ( see projectile_shot_type_enum table )`

**Description:**  
Returns true if the unit has the ammo type

**Author:** `Ingimar`

**Function:** `FUN_10166c20`



## BattlePlayerUnitCategory

**Example:** `BattlePlayerUnitCategory(\"category\")`

**Arguments:** `One lowercase string with the unit\'s category name ( see units table )`

**Description:**  
Takes in a unit category string and returns true if it matches the unit category of the unit

**Author:** `Ingimar`

**Function:** `FUN_10166cd0`



## BattlePlayerUnitClass

**Example:** `BattlePlayerUnitClass(\"class\")`

**Arguments:** `One lowercase string with the unit\'s class name ( see unit_stats_land table )`

**Description:**  
Takes in a unit class string and returns true if it matches the unit class of the unit

**Author:** `Ingimar`

**Function:** `LAB_10166d70`



## BattlePlayerUnitCurrentFormation

**Example:** `BattlePlayerUnitCurrentFormation( \"pike_square_formation\" )`

**Arguments:** `Takes in a single string which can be one of the following : block_formation, pike_square_formation, pike_wall_formation, square_formation, diamond_formation, wedge_formation, light_infantry_behaviour.`

**Description:**  
Returns true if the string matches the current formation employed, otherwise it returns false

**Author:** `Ingimar`

**Function:** `LAB_10166e10`



## BattlePlayerUnitDefendingHill

**Example:** `BattlePlayerUnitDefendingHill()`

**Arguments:** `No paramaters needed`

**Description:**  
Returns true if a unit is stationed on a hill

**Author:** `Ingimar`

**Function:** `LAB_10166ec0`



## BattlePlayerUnitEngaged

**Example:** `BattlePlayerUnitEngaged()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if a unit is either in a firefight or melee

**Author:** `Ingimar`

**Function:** `LAB_10167010`



## BattlePlayerUnitEngagedInMelee

**Example:** `BattlePlayerUnitEngagedInMelee()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if a unit is in a melee fight

**Author:** `Ingimar`

**Function:** `FUN_10166fa0`



## BattlePlayerUnitMountType

**Example:** `BattlePlayerUnitMountClass(\"mount_type\")`

**Arguments:** `A lowercase string with the unit\'s mount type to be checked ( see type in battle_entities ) table`

**Description:**  
Determines whether the unit is mounted on the type of mount passed to the condition

**Author:** `Ingimar`

**Function:** `FUN_101670e0`



## BattlePlayerUnitMovingFast

**Example:** `BattlePlayerUnitMovingFast()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if the unit is moving fast, otherwise false

**Author:** `Ingimar`

**Function:** `FUN_10167190`



## BattlePlayerUnitSpecialAbilityActive

**Example:** `BattlePlayerUnitSpecialAbilityActive()`

**Arguments:** `Special Ability string : pike_square_formation, pike_wall_formation, square_formation, wedge_formation, diamond_formation, light_infantry_behaviour,  loose_formation, fire_and_advance, plug_bayonets, dismount, unlimber, none`

**Description:**  
Checks whether the specified unit ability is active

**Author:** `Ingimar`

**Function:** `FUN_101672b0`



## BattlePlayerUnitSpecialAbilitySupported

**Example:** `BattlePlayerUnitSpecialAbilitySupported(\"ability\")`

**Arguments:** `Special Ability string : pike_square_formation, pike_wall_formation, square_formation, wedge_formation, diamond_formation, light_infantry_behaviour,  loose_formation, fire_and_advance, plug_bayonets, dismount, unlimber, none`

**Description:**  
Checks all of the units special abilities and returns true if the unit has ability

**Author:** `Ingimar`

**Function:** `FUN_10167390`



## BattlePlayerUnitTechnologySupported

**Example:** `BattlePlayerUnitTechnologySupported(\"ring_bayonets\")`

**Arguments:** `Technology string : ring_bayonets, socket_bayonets, fire_mounted`

**Description:**  
Checks whether the unit has the technology passed in and returns true if the unit has the technology

**Author:** `Ingimar`

**Function:** `FUN_10167450`



## BattleResult

**Example:** `BattleResult(\"decisive_victory\")`

**Arguments:** `Result of the battle, e.g. \"crushing_defeat\", \"major_victory\", \"pyrrhic_victory\`

**Description:**  
Returns true if the battle result matches the one supplied

**Author:** `DAT_117a159c`

**Function:** `FUN_10810db0`



## BattleShipIsPlayers

**Example:** `BattleShipIsPlayers`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if the unit is part of the players army

**Author:** `Ingimar`

**Function:** `FUN_101674c0`



## BattleShipSailsPercentageDamage

**Example:** `BattlePlayerShipSailsPercentageDamage()`

**Arguments:** `No parameters needed`

**Description:**  
Returns the percentile of damage the sails have recieved in the range 0.0 to 100.0

**Author:** `Ingimar`

**Function:** `FUN_10166a20`



## BattleTimeLimitSet

**Example:** `BattleTimeLimitSet()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if there\'s an alliance in a the battle that will win on a timeout

**Author:** `Ingimar`

**Function:** `FUN_10167670`



## BattleType

**Example:** `BattleType(\"normal\")`

**Arguments:** `Battle type string : normal, land_normal, land_bridge, fort_standard, fort_sally, fort_relief, settlement_standard, settlement_sally, settlement_relief settlement_unfortified, town_normal, naval_normal, naval_blockade, naval_breakout. Please see designers for which of these are supported.`

**Description:**  
Returns true if the battle type matches the one supplied

**Author:** `Ingimar`

**Function:** `FUN_10167700`



## BattleUnitIsAllied

**Example:** `BattleUnitIsAllied()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if the unit is part of the players alliance

**Author:** `Ingimar`

**Function:** `FUN_101677b0`



## BattleUnitIsPlayers

**Example:** `BattleUnitIsPlayers()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if the unit is part of the players army

**Author:** `Ingimar`

**Function:** `FUN_101678b0`



## BattlesFought

**Example:** `BattlesFought()`

**Arguments:** `DAT_1178eec8`

**Description:**  
How many battles has this character fought in?

**Author:** `DAT_117a159c`

**Function:** `FUN_10810f20`



## BuildingLevelName

**Example:** `BuildingLevelName(corn_peasant_farms)`

**Arguments:** `String corresponding to level_name of supplied building level record`

**Description:**  
Flags whether or not the context contains the supplied building level record

**Author:** `DAT_1173e50c`

**Function:** `FUN_108b6e30`



## BuildingTypeExistsAtSettlement

**Example:** `BuildingTypeExistsAtSettlement(\"barracks\")`

**Arguments:** `The key of the building level you are querying from the building_levels table`

**Description:**  
Tests if a building of the specified type exists in the region settlement

**Author:** `DAT_117a1590`

**Function:** `LAB_10810f70`



## BuildingTypeExistsAtSlot

**Example:** `BuildingTypeExistsAtSlot(\"barracks\")`

**Arguments:** `The key of the building level you are querying from the building_levels table`

**Description:**  
Tests if a building of the specified type exists in the region slot

**Author:** `DAT_117a1590`

**Function:** `FUN_10811040`



## CampaignBattleType

**Example:** `CampaignBattleType(\"normal\")`

**Arguments:** `Battle type string : normal, land_normal, land_bridge, fort_standard, fort_sally, fort_relief, settlement_standard, settlement_sally, settlement_relief settlement_unfortified, town_normal, naval_normal, naval_blockade, naval_breakout. Please see designers for which of these are supported.`

**Description:**  
Returns true if the battle type matches the one supplied

**Author:** `DAT_117a159c`

**Function:** `FUN_108116f0`



## CampaignName

**Example:** `CampaignName(\'main\')`

**Arguments:** `Name of the campaign to compare against, from the campaigns table`

**Description:**  
Returns whether or not the current campaign name matches the supplied parameter

**Author:** `DAT_1173e50c`

**Function:** `FUN_108117d0`



## CampaignNumberOfUnitsInEnemyAlliance

**Example:** `CampaignNumberOfUnitsInEnemyAlliance()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Number of units in the alliance opposing character in context

**Author:** `DAT_1179b680`

**Function:** `FUN_108118d0`



## CampaignNumberOfUnitsInEnemyArmy

**Example:** `CampaignNumberOfUnitsInEnemyArmy()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Number of units in the primary army of the primary faction of the force opposing the army commanded by the character in context

**Author:** `DAT_1179b680`

**Function:** `FUN_108119c0`



## CampaignNumberOfUnitsInPlayerAlliance

**Example:** `CampaignNumberOfUnitsInPlayerAlliance()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Number of units in the alliance containing character in context

**Author:** `DAT_1179b680`

**Function:** `FUN_10811ad0`



## CampaignNumberOfUnitsInPlayerArmy

**Example:** `CampaignNumberOfUnitsInPlayerArmy()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Number of units in the army commanded by the character in context

**Author:** `DAT_1179b680`

**Function:** `FUN_10811bc0`



## CampaignPercentageOfOwnCaptured

**Example:** `CampaignPercentageOfOwnCaptured()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Percentage of own men/ships captured in the battle that just took place

**Author:** `DAT_117a159c`

**Function:** `FUN_10811cf0`



## CampaignPercentageOfOwnKilled

**Example:** `CampaignPercentageOfOwnKilled()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Percentage of own men/ships killed in the battle that just took place

**Author:** `DAT_117a159c`

**Function:** `FUN_10811dc0`



## CampaignPercentageOfOwnRouted

**Example:** `CampaignPercentageOfOwnRouted()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Percentage of own men/ships that routed in the battle that just took place

**Author:** `DAT_117a159c`

**Function:** `FUN_10811ef0`



## CampaignPercentageOfThemCaptured

**Example:** `CampaignPercentageOfThemCaptured()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Percentage of opposing men/ships captured in the battle that just took place

**Author:** `DAT_117a159c`

**Function:** `FUN_10812030`



## CampaignPercentageOfThemKilled

**Example:** `CampaignPercentageOfThemKilled()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Percentage of opposing men/ships killed in the battle that just took place

**Author:** `DAT_117a159c`

**Function:** `FUN_10812100`



## CampaignPercentageOfThemRouted

**Example:** `CampaignPercentageOfThemRouted()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Percentage of opposing men/ships that routed in the battle that just took place

**Author:** `DAT_117a159c`

**Function:** `FUN_10812230`



## CampaignPercentageOfUnitCategory

**Example:** `CampaignPercentageOfUnitCategory(\"naval_frigate\")`

**Arguments:** `DAT_1178eec8`

**Description:**  
Percentage of type of ships/units under an admirals/generals command

**Author:** `DAT_117a159c`

**Function:** `FUN_10812370`



## CanGenerateHistoricalCharacter

**Example:** `CanGenerateHistoricalCharacter(\"abraham_de_moivre\")`

**Arguments:** `Historical character record key`

**Description:**  
DAT_1173dad0

**Author:** `DAT_1179b680`

**Function:** `FUN_10970f80`



## CharacterAbility

**Example:** `CharacterAbility(\"can_assassinate\")`

**Arguments:** `Ability name (valid key from abilities table)`

**Description:**  
Returns whether a character can perform the ability specified

**Author:** `DAT_117a2ecc`

**Function:** `FUN_108124f0`



## CharacterArmyCouldReplenishFromBattle

**Example:** `CharacterArmyCouldReplenishFromBattle()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Test to see if an army involved in the current pending battle and belonging to the player can replenish

**Author:** `DAT_1179b680`

**Function:** `FUN_10812580`



## CharacterArmyUsedCoverBuildings

**Example:** `CharacterArmyUsedCoverBuildings()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Did the characters army use buildings for conver?

**Author:** `DAT_1179b680`

**Function:** `FUN_10812630`



## CharacterArmyUsedCoverWalls

**Example:** `CharacterArmyUsedCoverWalls()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Did the characters army use walls for cover?

**Author:** `DAT_1179b680`

**Function:** `FUN_10812740`



## CharacterAttribute

**Example:** `CharacterAttribute(\"command_land\") >= 2`

**Arguments:** `Attribute name (valid key from agent_attributes table)`

**Description:**  
Returns the value of the attribute specified.  This doesn\'t account for any given situation bonuses

**Author:** `DAT_117a2ecc`

**Function:** `LAB_10812850`



## CharacterBattleWallsBreached

**Example:** `CharacterBattleWallsBreached()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Did the characters army breach the walls of a fort?

**Author:** `DAT_1179b680`

**Function:** `FUN_10812870`



## CharacterBuildingConstructed

**Example:** `CharacterBuildingConstructed(\"vineyards\")`

**Arguments:** `The building type`

**Description:**  
Did this building type just get constructed?

**Author:** `DAT_117a159c`

**Function:** `FUN_10812980`



## CharacterCapturedEnemyShip

**Example:** `CharacterCapturedEnemyShip()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Did the given character capture an enemy ship?

**Author:** `DAT_117a159c`

**Function:** `FUN_10812a10`



## CharacterCommandsNavy

**Example:** `CharacterCommandsNavy()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Does a character command a navy?

**Author:** `DAT_117a1590`

**Function:** `FUN_10812aa0`



## CharacterCultureType

**Example:** `CharacterCultureType(\"tribal\")`

**Arguments:** `Valid entry from \'key\' field from cultures table in Empire.mdb`

**Description:**  
Returns true if the character context is of the culture specified

**Author:** `DAT_117a2ecc`

**Function:** `FUN_10812b10`



## CharacterDuelWeapon

**Example:** `CharacterDuelWeapon(\"duelling_pistols\")`

**Arguments:** `DAT_1173e900`

**Description:**  
Did the given character use the given weapon in the duel?

**Author:** `DAT_117a159c`

**Function:** `FUN_10166b40`



## CharacterDuelsFought

**Example:** `CharacterDuelsFought()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Number of duels a character has fought. Character context

**Author:** `DAT_117a1590`

**Function:** `FUN_10812bc0`



## CharacterDuelsLost

**Example:** `CharacterDuelsLost()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Number of duels a character has lost. Character context

**Author:** `DAT_117a1590`

**Function:** `FUN_10812c30`



## CharacterDuelsWon

**Example:** `CharacterDuelsWon()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Number of duels a character has won. Character context

**Author:** `DAT_117a1590`

**Function:** `FUN_10812ca0`



## CharacterEndedInAmbushPosition

**Example:** `CharacterEndedInAmbushPosition()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns true if the character is in an ambush position, as used in conjunction with out of mp this has just happened

**Author:** `DAT_117a159c`

**Function:** `FUN_10812d10`



## CharacterFactionAdmiralCount

**Example:** `CharacterFactionAdmiralCount()`

**Arguments:** `DAT_1173e900`

**Description:**  
How many admirals does this characters faction have?

**Author:** `DAT_117a159c`

**Function:** `FUN_10812d70`



## CharacterFactionGeneralCount

**Example:** `CharacterFactionGeneralCount()`

**Arguments:** `DAT_1173e900`

**Description:**  
How many generals does this characters faction have?

**Author:** `DAT_117a159c`

**Function:** `FUN_10812d70`



## CharacterFactionHasTechType

**Example:** `CharacterFactionHasTechType(\"enlightenment_abolition_of_slavery\")`

**Arguments:** `A valid key from the technologies table.`

**Description:**  
Does the characters faction have the specified technology

**Author:** `DAT_117a159c`

**Function:** `FUN_10812e20`



## CharacterFactionMinisterAncillary

**Example:** `CharacterFactionMinisterAncillary(\"Ancillary_Boxer\")`

**Arguments:** `Ancillary name`

**Description:**  
Tests whether any minister in the characters faction has the specified ancillary

**Author:** `DAT_1179b680`

**Function:** `FUN_10812ef0`



## CharacterFactionMinisterTrait

**Example:** `CharacterFactionMinisterTrait(\"drunkard\")`

**Arguments:** `Trait name`

**Description:**  
Tests whether any minister in the characters faction has the named trait

**Author:** `DAT_1179b680`

**Function:** `FUN_10812ff0`



## CharacterFactionName

**Example:** `CharacterFactionName(\"britain\")`

**Arguments:** `The db record key for the faction`

**Description:**  
Is characters faction the one specified?

**Author:** `DAT_117a159c`

**Function:** `FUN_108130f0`



## CharacterFactionReligion

**Example:** `CharacterFactionReligion(\"rel_buddhist\")`

**Arguments:** `religion key from region table`

**Description:**  
Returns whether the religion of the character context\'s faction matches the specified religion

**Author:** `DAT_1179b680`

**Function:** `FUN_108131a0`



## CharacterFactionSubcultureType

**Example:** `CharacterFactionSubcultureType(\"sc_indian_islamic\")`

**Arguments:** `Subculture key`

**Description:**  
Is the character part of the given subculture?

**Author:** `DAT_117a159c`

**Function:** `FUN_10813260`



## CharacterForename

**Example:** `CharacterForename(\"names_name_names_irishAlan\")`

**Arguments:** `The forename\'s db key`

**Description:**  
Does the character have this forename?

**Author:** `DAT_117a2ed8`

**Function:** `LAB_108132f0`



## CharacterFoughtCulture

**Example:** `CharacterFoughtCulture(\"tribal\")`

**Arguments:** `DAT_1178eec8`

**Description:**  
Has this character just fought this culture?

**Author:** `DAT_117a159c`

**Function:** `FUN_108133a0`



## CharacterHasAncillary

**Example:** `CharacterHasAncillary(\"Ancillary_Boxer\")`

**Arguments:** `Ancillary name`

**Description:**  
Tests whether the character has the specified ancillary

**Author:** `DAT_1179b680`

**Function:** `FUN_108134a0`



## CharacterHasTrait

**Example:** `CharacterHasTrait(\"drunkard\")`

**Arguments:** `The name of the trait`

**Description:**  
Does this character have the given trait?

**Author:** `DAT_117a159c`

**Function:** `FUN_10813550`



## CharacterHoldsPost

**Example:** `CharacterHoldsPost()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Is this character a minister with a post?

**Author:** `DAT_117a159c`

**Function:** `LAB_108135f0`



## CharacterHusbandHasTrait

**Example:** `CharacterHusbandHasTrait(\"drunkard\")`

**Arguments:** `The name of the trait`

**Description:**  
Does this character\'s husband have the given trait?

**Author:** `DAT_1179b680`

**Function:** `FUN_10813660`



## CharacterInBuildingOfChain

**Example:** `CharacterInBuildingOfChain(\"tobacco\")`

**Arguments:** `DAT_1173dad0`

**Description:**  
Is the character in a building of this chain type?

**Author:** `DAT_117a159c`

**Function:** `LAB_10813720`



## CharacterInBuildingType

**Example:** `CharacterInBuildingType(\"naval_college\")`

**Arguments:** `DAT_1173dad0`

**Description:**  
Is the character in a building of this type?

**Author:** `DAT_117a159c`

**Function:** `FUN_10813870`



## CharacterInEnemyLands

**Example:** `CharacterInEnemyLands()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Is the character in enemy lands?

**Author:** `DAT_117a159c`

**Function:** `FUN_108139b0`



## CharacterInHomeRegion

**Example:** `CharacterInHomeRegion()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Is the character in their home region?

**Author:** `DAT_117a159c`

**Function:** `FUN_10813a40`



## CharacterInOwnFactionLands

**Example:** `CharacterInOwnFactionLands()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Is the character in their own factions lands?

**Author:** `DAT_117a159c`

**Function:** `FUN_10813ad0`



## CharacterInRegion

**Example:** `CharacterInRegion(\"england\")`

**Arguments:** `The region key`

**Description:**  
Is the character in the given region?

**Author:** `DAT_117a159c`

**Function:** `FUN_10813b60`



## CharacterInTheatre

**Example:** `CharacterInTheatre(\"-1133129049\")`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character in the specified theatre

**Author:** `DAT_117a1590`

**Function:** `FUN_10813c00`



## CharacterIsAlliedCampaign

**Example:** `CharacterIsAllied()`

**Arguments:** `DAT_1178eec8`

**Description:**  
The character is allied to the local faction?

**Author:** `DAT_117a1590`

**Function:** `FUN_10813ce0`



## CharacterIsEnemyCampaign

**Example:** `CharacterIsEnemy()`

**Arguments:** `DAT_1178eec8`

**Description:**  
The character is an enemy of the local faction?

**Author:** `DAT_117a1590`

**Function:** `FUN_10813d90`



## CharacterIsFemale

**Example:** `CharacterIsFemale()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Returns whether the character in context is female

**Author:** `DAT_1179b680`

**Function:** `FUN_10813e40`



## CharacterIsLocalCampaign

**Example:** `CharacterIsLocalCampaign()`

**Arguments:** `DAT_1173e900`

**Description:**  
Does the character belong to the player faction?

**Author:** `DAT_117a1590`

**Function:** `FUN_10813eb0`



## CharacterMPPercentageRemaining

**Example:** `CharacterMPPercentageRemaining() < 50`

**Arguments:** `DAT_1178eec8`

**Description:**  
Returns the percentage of movement points remaining as in integer value

**Author:** `DAT_117a2ecc`

**Function:** `FUN_10813f60`



## CharacterMinisterialPosition

**Example:** `CharacterMinisterialPosition(\"governor_europe\")`

**Arguments:** `Ministerial position`

**Description:**  
Does the character hold the specified ministerial position?

**Author:** `DAT_117a159c`

**Function:** `FUN_10814000`



## CharacterNumberOfChildren

**Example:** `CharacterNumberOfChildren()`

**Arguments:** `DAT_1178eec8`

**Description:**  
How many children does this character have?

**Author:** `DAT_1179b680`

**Function:** `FUN_108140a0`



## CharacterOlderThan

**Example:** `CharacterOlderThan(16)`

**Arguments:** `DAT_117aab60`

**Description:**  
Returns whether the character is older than the given age

**Author:** `DAT_1179b680`

**Function:** `FUN_108140f0`



## CharacterRallied

**Example:** `CharacterRallied()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Did the general rally at least one unit?

**Author:** `DAT_1179b680`

**Function:** `FUN_10814170`



## CharacterRank

**Example:** `CharacterRank()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Rank of character (1-6)

**Author:** `DAT_117a2ed8`

**Function:** `FUN_108142c0`



## CharacterRouted

**Example:** `CharacterRouted()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Has the character routed? in the last battle?

**Author:** `DAT_117a159c`

**Function:** `FUN_10814330`



## CharacterRunsSpyNetwork

**Example:** `CharacterRunsSpyNetwork()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Test to see if the character runs a spy network

**Author:** `DAT_1179b680`

**Function:** `FUN_10814470`



## CharacterSpouseHasTrait

**Example:** `CharacterSpouseHasTrait(\"drunkard\")`

**Arguments:** `The name of the trait`

**Description:**  
Does this character\'s spouse have the given trait?

**Author:** `DAT_1179b680`

**Function:** `FUN_108144c0`



## CharacterStationaryForOneTurn

**Example:** `CharacterStationaryForOneTurn()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Was the character stationary last turn (or longer)

**Author:** `DAT_117a1590`

**Function:** `FUN_10814570`



## CharacterSurname

**Example:** `CharacterSurname(\"names_name_names_irishBlair\")`

**Arguments:** `The surname\'s db key`

**Description:**  
Does the character have this surname?

**Author:** `DAT_117a2ed8`

**Function:** `FUN_108145e0`



## CharacterTrait

**Example:** `CharacterTrait(\"drunkard\") > 2`

**Arguments:** `Trait name`

**Description:**  
Returns the value of the specified trait (0 if not present)

**Author:** `DAT_117a2ecc`

**Function:** `FUN_10814690`



## CharacterTurnsAtHome

**Example:** `CharacterTurnsAtHome()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Returns the number of turns in home regions exclusively

**Author:** `DAT_117a159c`

**Function:** `FUN_10814740`



## CharacterTurnsAtSea

**Example:** `CharacterTurnsAtSea()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Returns the number of turns at sea exclusively

**Author:** `DAT_117a159c`

**Function:** `LAB_10814790`



## CharacterTurnsInEnemyLands

**Example:** `CharacterTurnsInEnemyLands()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Returns the number of turns in enemy regions exclusively

**Author:** `DAT_117a159c`

**Function:** `LAB_108147e0`



## CharacterType

**Example:** `CharacterType(\"spy\")`

**Arguments:** `Valid entry from \'key\' field from Agents table in Empire.mdb`

**Description:**  
Returns true if the character context is of the agent type specified

**Author:** `DAT_117a2ecc`

**Function:** `LAB_10814830`



## CharacterWasAttacker

**Example:** `CharacterWasAttacker()`

**Arguments:** `DAT_1173e900`

**Description:**  
Was the character the attacker in the last battle?

**Author:** `DAT_117a159c`

**Function:** `FUN_108148c0`



## CharacterWifeHasTrait

**Example:** `CharacterWifeHasTrait(\"drunkard\")`

**Arguments:** `The name of the trait`

**Description:**  
Does this character\'s wife have the given trait?

**Author:** `DAT_1179b680`

**Function:** `FUN_10814950`



## CharacterWithdrewFromBattle

**Example:** `CharacterWithdrewFromBattle()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Did the characters army withdraw from battle?

**Author:** `DAT_1179b680`

**Function:** `LAB_10814a10`



## CharacterWonBattle

**Example:** `CharacterWonBattle()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Is the character part of the winning alliance in a battle

**Author:** `DAT_117a1590`

**Function:** `FUN_10814b20`



## CharacterWonDuel

**Example:** `CharacterWonDuel()`

**Arguments:** `DAT_1173e900`

**Description:**  
Did the given character win the Duel?

**Author:** `DAT_117a159c`

**Function:** `FUN_10166b40`



## CharactersUnitRallied

**Example:** `CharactersUnitRallied()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Did the generals unit rally?

**Author:** `DAT_1179b680`

**Function:** `FUN_10814bb0`



## CommanderAncillary

**Example:** `CommanderAncillary(\"Ancillary_Boxer\")`

**Arguments:** `Ancillary name`

**Description:**  
Returns whether the commander has the specified ancillary

**Author:** `DAT_117a159c`

**Function:** `FUN_10814d00`



## CommanderFoughtInBattle

**Example:** `CommanderFoughtInBattle()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Did the characters unit fight in the battle? (melee or missile)

**Author:** `DAT_117a159c`

**Function:** `FUN_10814dc0`



## CommanderFoughtInMelee

**Example:** `CommanderFoughtInMelee()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Did the characters unit engage in melee in the battle?

**Author:** `DAT_117a159c`

**Function:** `FUN_10814f00`



## CommanderTrait

**Example:** `CommanderTrait(\"C_General_Mad\") > 2`

**Arguments:** `Trait name`

**Description:**  
Returns the value of the specified trait (0 if not present)

**Author:** `DAT_117a159c`

**Function:** `FUN_10815040`



## DateAndWeekInRange

**Example:** `DateAndWeekInRange(0, 1066, 47, 2001)`

**Arguments:** `Start Week, Start Year, End Week, End Year (Inclusive)`

**Description:**  
Test to see if the current calendar year and week in year is within the years and weeks specified.  Week should be 0 <= week < 48.  start <= current <= end

**Author:** `DAT_1179b680`

**Function:** `FUN_10815100`



## DateInRange

**Example:** `DateInRange(1066, 2001)`

**Arguments:** `Start Year, End Year (Inclusive)`

**Description:**  
Test to see if the current calendar year is within the years specified.  start <= current <= end

**Author:** `DAT_1179b680`

**Function:** `FUN_10815260`



## DefensiveSiegesFought

**Example:** `DefensiveSiegesFought()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the number of siege defences a general has attempted

**Author:** `DAT_117a1590`

**Function:** `FUN_10815310`



## DefensiveSiegesWon

**Example:** `DefensiveSiegesWon()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the number of siege defences a general has won

**Author:** `DAT_117a1590`

**Function:** `FUN_10815380`



## DifficultyLevel

**Example:** `DifficultyLevel()`

**Arguments:** `DAT_1173e900`

**Description:**  
What is the local faction\'s difficulty level?

**Author:** `DAT_1179b680`

**Function:** `FUN_108153f0`



## EnemyArmyGreaterCombatStrength

**Example:** `EnemyArmyGreaterCombatStrength()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Is the enemies army stronger than ours?

**Author:** `DAT_117a159c`

**Function:** `FUN_10815490`



## FactionAllyCount

**Example:** `FactionAllyCount() > 2`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the number of allies the characters faction has

**Author:** `DAT_1179b680`

**Function:** `FUN_10815660`



## FactionBuildingExists

**Example:** `FactionBuildingExists(\"britain\", \"admiralty\")`

**Arguments:** `Parameter 1: A valid key from the factions table.  Parameter 2: A valid key from the building_levels table.`

**Description:**  
Does the specified faction have at least one of the specified building

**Author:** `Paul K`

**Function:** `LAB_10815770`



## FactionBuildingUnderConstruction

**Example:** `FactionBuildingUnderConstruction(\"tut_chosokabe\", \"SHO_Farming_1_Rice_Paddies\", \"jap_tut_tosa\")`

**Arguments:** `Parameter 1: A valid key from the factions table.  Parameter 2: A valid key from the building_levels table.  Parameter 3: A valid key from the regions table or the empty string.`

**Description:**  
Does the specified faction have at least one of the specified building under construction

**Author:** `Paul K`

**Function:** `FUN_108158c0`



## FactionCanBuildBuilding

**Example:** `FactionCanBuildBuilding(\"admiralty\")`

**Arguments:** `The building key from the building levels table`

**Description:**  
Can the faction build the specified building at this point

**Author:** `DAT_117a1590`

**Function:** `FUN_10815ac0`



## FactionCashFlow

**Example:** `FactionCashFlow() > 10`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the percentage surplus/loss of the factions regular income and expenditure

**Author:** `DAT_1179b680`

**Function:** `FUN_10815cb0`



## FactionDestroyedByCharacterFaction

**Example:** `FactionDestroyedByCharacterFaction()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Did this characters faction destroy another faction this turn?

**Author:** `DAT_117a159c`

**Function:** `FUN_10815da0`



## FactionExists

**Example:** `FactionExists(\"britain\")`

**Arguments:** `The db record for the faction`

**Description:**  
Does the given faction exist?

**Author:** `DAT_117a159c`

**Function:** `FUN_10815e10`



## FactionGovernmentType

**Example:** `FactionGovernmentType(\"gov_republic\")`

**Arguments:** `The government key from the government_types table`

**Description:**  
Is the faction\'s government type equal to the passed government type

**Author:** `DAT_117a1590`

**Function:** `FUN_10815eb0`



## FactionHasAllies

**Example:** `FactionHasAllies()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns whether or not the characters faction has any allies

**Author:** `DAT_1179b680`

**Function:** `FUN_10815fa0`



## FactionHasRecruitedAnyAgents

**Example:** `FactionHasRecruitedAnyAgents()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Checks whether a faction has ever recruited any agents

**Author:** `DAT_1179b680`

**Function:** `FUN_108160a0`



## FactionHasTradeShipNotInTradeNode

**Example:** `FactionHasTradeShipNotInTradeNode()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Does the faction in context have a trade ship that is not in a trade node. Requires faction context

**Author:** `DAT_117a1590`

**Function:** `FUN_10816110`



## FactionIsAlliedCampaign

**Example:** `FactionIsAlliedCampaign()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Is the faction allied to the player faction?

**Author:** `DAT_117a1590`

**Function:** `FUN_108161f0`



## FactionIsEnemyCampaign

**Example:** `FactionIsEnemy(\"france\")`

**Arguments:** `Faction to query`

**Description:**  
Is the specified faction at war with the player faction?

**Author:** `DAT_117a1590`

**Function:** `FUN_10816270`



## FactionIsHuman

**Example:** `FactionIsHuman()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the faction human?

**Author:** `DAT_117a2ed8`

**Function:** `FUN_10816330`



## FactionIsLocal

**Example:** `FactionIsLocal()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the faction the local faction?

**Author:** `DAT_117a1590`

**Function:** `FUN_108163c0`



## FactionKeyIsLocal

**Example:** `FactionKeyIsLocal()`

**Arguments:** `Faction key`

**Description:**  
Is the faction the local player (and human)?

**Author:** `DAT_117a2ed8`

**Function:** `LAB_10816440`



## FactionLeadersAttribute

**Example:** `FactionLeadersAttribute(\"management\")`

**Arguments:** `The attribute which you wish to check on the factions leader`

**Description:**  
Gets the level of the faction leaders attribute specified as a parameter

**Author:** `DAT_117a159c`

**Function:** `LAB_10812850`



## FactionLeadersTrait

**Example:** `FactionLeadersTrait(\"drunkard\") > 2`

**Arguments:** `Trait name`

**Description:**  
Returns the value of the specified trait for the characters faction leader (0 if not present)

**Author:** `DAT_117a2ecc`

**Function:** `FUN_108164f0`



## FactionName

**Example:** `FactionName(\"britain\")`

**Arguments:** `The db record for the faction`

**Description:**  
Is the faction the one specified?

**Author:** `DAT_117a2ed8`

**Function:** `FUN_108165d0`



## FactionParticipatedInBattle

**Example:** `FactionParticipatedInBattle(\"ita_french_republic\")`

**Arguments:** `Faction key of the faction to be queried`

**Description:**  
Did the specified faction participate in the battle?

**Author:** `DAT_117a1590`

**Function:** `FUN_10816670`



## FactionPatrioticFervour

**Example:** `FactionPatrioticFervour()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Does this faction have patriotic fervour?

**Author:** `DAT_117a159c`

**Function:** `FUN_10816730`



## FactionSupportCostsPercentage

**Example:** `FactionSupportCostsPercentage()`

**Arguments:** `DAT_1173e900`

**Description:**  
What percentage of the factions expenditure is spent on army upkeep

**Author:** `DAT_117a1590`

**Function:** `FUN_108167a0`



## FactionTaxLevel

**Example:** `FactionTaxLevel() < TaxLevel(\"extortionate\")`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the average tax level for the faction

**Author:** `DAT_1179b680`

**Function:** `FUN_10816830`



## FactionTechExists

**Example:** `FactionTechExists(\"britain\", \"enlightenment_abolition_of_slavery\")`

**Arguments:** `Parameter 1: A valid key from the factions table.  Parameter 2: A valid key from the technologies table.`

**Description:**  
Does the specified faction have the specified technology

**Author:** `Paul K`

**Function:** `FUN_108168b0`



## FactionTradeResourceExists

**Example:** `FactionTradeResourceExists(\"res_gold\")`

**Arguments:** `Valid entry from \'key\' field from resources table in Empire.mdb`

**Description:**  
Returns whether the faction has access to the trade resource

**Author:** `DAT_1179b680`

**Function:** `FUN_108169b0`



## FactionTradeValue

**Example:** `FactionTradeValue() > 1000`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the absolute value of the factions global trade

**Author:** `DAT_1179b680`

**Function:** `FUN_10816d70`



## FactionTradeValuePercentage

**Example:** `FactionTradeValuePercentage() > 25`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the percentage value of global trade owned by the faction

**Author:** `DAT_1179b680`

**Function:** `FUN_10816b80`



## FactionTreasury

**Example:** `FactionTreasury() > 100`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the factions treasury value

**Author:** `DAT_1179b680`

**Function:** `LAB_10817020`



## FactionTreasuryWorldPercentage

**Example:** `FactionTreasuryWorldPercentage() > 10`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the characters factions treasury value as a percentage of the sum of all factions treasury values

**Author:** `DAT_1179b680`

**Function:** `FUN_10816f10`



## FactionWarWeariness

**Example:** `FactionWarWeariness()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Does this faction have war weariness?

**Author:** `DAT_117a159c`

**Function:** `FUN_10816730`



## FactionwideAncillaryTypeExists

**Example:** `FactionwideAncillaryTypeExists(\"unkillable_cat\") == true`

**Arguments:** `Ancillary name`

**Description:**  
Returns whether the named ancillary exists in the faction somewhere

**Author:** `DAT_117a2ecc`

**Function:** `FUN_10817090`



## ForcesComposedOf

**Example:** `ForcesComposedOf()`

**Arguments:** `A single string of semi-colon separated unit keys`

**Description:**  
Returns whether the two commanded forces combined match the list of unit keys provided

**Author:** `DAT_1179b680`

**Function:** `LAB_10817130`



## GarrisonIsLocal

**Example:** `GarrisonIsLocal()`

**Arguments:** `DAT_1173e900`

**Description:**  
Does the garrison belong to the player faction?

**Author:** `DAT_1179b680`

**Function:** `FUN_10817420`



## GarrisonUnitCount

**Example:** `GarrisonUnitCount()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the number of units in the garrison context

**Author:** `DAT_1179b680`

**Function:** `FUN_108174a0`



## GovernorTaxLevel

**Example:** `GovernorTaxLevel() >= 90`

**Arguments:** `DAT_1173e900`

**Description:**  
If the character is the governor returns the tax level set for that governorship.  Returns -1 if not.

**Author:** `DAT_117a2ecc`

**Function:** `FUN_10817520`



## GovernorshipEquals

**Example:** `GovernorshipEquals(\"europe\")`

**Arguments:** `Key of the governorship to be queried `

**Description:**  
Does the context\'s governorship key match the parameter

**Author:** `DAT_117a1590`

**Function:** `FUN_10166b40`



## GovernorshipTaxLevel

**Example:** `GovernorshipTaxLevel(\"europe\")`

**Arguments:** `Valid entry from \'governorship\' field from governorships table in Empire.mdb`

**Description:**  
Returns the governorships tax level

**Author:** `DAT_1179b680`

**Function:** `FUN_10817560`



## GovernorshipsTaxLevel

**Example:** `GovernorshipsTaxLevel() >= 90`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the current tax level for this govenorship

**Author:** `Shane`

**Function:** `FUN_108175a0`



## HasUnspecialisedPort

**Example:** `HasUnspecialisedPort()`

**Arguments:** `DAT_1173e900`

**Description:**  
Does the region have a port with no building?

**Author:** `DAT_1179b680`

**Function:** `FUN_10817600`



## InPort

**Example:** `InPort()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character in a port?

**Author:** `DAT_117a1590`

**Function:** `FUN_10817690`



## InSettlement

**Example:** `InSettlement()`

**Arguments:** `DAT_1173e900`

**Description:**  
Checks that a character is in a settlement

**Author:** `DAT_117a2ecc`

**Function:** `FUN_10817730`



## InsurrectionCrushed

**Example:** `InsurrectionCrushed()`

**Arguments:** `DAT_1173e900`

**Description:**  
Has the characters faction put down a rebellion in this turn (or the turn that is just ending)

**Author:** `DAT_117a159c`

**Function:** `FUN_10817770`



## IsAdmiral

**Example:** `IsAdmiral()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character an admiral?

**Author:** `DAT_1179b680`

**Function:** `FUN_108177e0`



## IsBesieging

**Example:** `IsBesieging()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character besieging?

**Author:** `DAT_117a1590`

**Function:** `FUN_10817880`



## IsBlockading

**Example:** `IsBlockading()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character blockading?

**Author:** `DAT_117a1590`

**Function:** `FUN_108178f0`



## IsBuildingInChain

**Example:** `IsBuildingInChain(\"army-admin\")`

**Arguments:** `The key of the building chain you are querying from the building_chains table`

**Description:**  
Is garrison residence\'s building (all slots and fortifications for settlements) in the building chain specified by the parameter?

**Author:** `DAT_117a1590`

**Function:** `FUN_10817960`



## IsBuildingOfType

**Example:** `IsBuildingOfType(\"admiralty\")`

**Arguments:** `The key of the building level you are querying from the building_levels table`

**Description:**  
Is garrison residence\'s building type (all slots and fortifications for settlements) equal to the parameter?

**Author:** `DAT_117a1590`

**Function:** `FUN_10817ac0`



## IsCarryingTroops

**Example:** `IsCarryingTroops()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character transporting an army?

**Author:** `DAT_117a1590`

**Function:** `FUN_10817c00`



## IsChildOf

**Example:** `IsChildOf(\"tax_slider\")`

**Arguments:** `Component id`

**Description:**  
Returns true if the components parent, (or parent\'s parent, or parent\'s parent\'s parent etc) has the id specified 

**Author:** `DAT_117b0390`

**Function:** `FUN_116c8160`



## IsColony

**Example:** `IsColony()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the region a colony

**Author:** `DAT_117a1590`

**Function:** `FUN_10817ca0`



## IsComponentType

**Example:** `IsComponentType(\"government_screens\")`

**Arguments:** `Component id`

**Description:**  
Returns true if the event was fired by the component named

**Author:** `DAT_117b0390`

**Function:** `FUN_116c8200`



## IsFactionBesiegingSettlement

**Example:** `IsFactionBesiegingSettlement(\"settlement:region:settlement_id\")`

**Arguments:** `Settlement key`

**Description:**  
Is the context faction besieging the specified settlement? Intended for use with faction start of turn event.

**Author:** `DAT_117a1590`

**Function:** `FUN_10817d50`



## IsFactionLeader

**Example:** `IsFactionLeader()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character the faction leader?

**Author:** `DAT_1179b680`

**Function:** `FUN_10817ee0`



## IsFactionLeaderFemale

**Example:** `IsFactionLeaderFemale()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is this character the faction leader and are they female? (Queen)

**Author:** `DAT_117a159c`

**Function:** `FUN_10817e20`



## IsFamilyMember

**Example:** `IsFamilyMember()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character a family member?

**Author:** `DAT_1179b680`

**Function:** `FUN_10817f50`



## IsGarrisoned

**Example:** `IsGarrisoned()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is garrison residence garrisoned?

**Author:** `DAT_117a1590`

**Function:** `LAB_10817fd0`



## IsHomeRegion

**Example:** `IsHomeRegion()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is this region the home region of the owning faction

**Author:** `DAT_117a1590`

**Function:** `FUN_10818040`



## IsMessageType

**Example:** `IsMessageType(\"unit_routs_in_battle\")`

**Arguments:** `Message id`

**Description:**  
Returns true if the event that triggered the condition check was for the message named

**Author:** `DAT_117b0390`

**Function:** `FUN_116c8200`



## IsMultiplayer

**Example:** `IsMultiplayer()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Returns true when in multiplayer campaign

**Author:** `DAT_1179ebf0`

**Function:** `FUN_108180e0`



## IsNightBattle

**Example:** `IsNightBattle()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Was the battle a night battle

**Author:** `DAT_1179b680`

**Function:** `FUN_10818150`



## IsPlayerTurn

**Example:** `IsPlayerTurn()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Is this the players turn?

**Author:** `DAT_117a159c`

**Function:** `FUN_108181d0`



## IsPortGarrisoned

**Example:** `IsPortGarrisoned()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the port garrisoned by a navy?

**Author:** `DAT_117a1590`

**Function:** `FUN_10818260`



## IsTheatreGovernor

**Example:** `IsTheatreGovernor()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns whether the character is a governor

**Author:** `DAT_117a159c`

**Function:** `FUN_10166b40`



## IsTriggerableHistoricalEvent

**Example:** `IsTriggerableHistoricalEvent(\"3_colour_printing\")`

**Arguments:** `Historical event record key`

**Description:**  
DAT_1173dad0

**Author:** `DAT_1179b680`

**Function:** `FUN_109e20a0`



## IsUnderBlockade

**Example:** `IsUnderBlockade()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character under blockade?

**Author:** `DAT_117a1590`

**Function:** `FUN_108182d0`



## IsUnderSiege

**Example:** `IsUnderSiege()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character under siege?

**Author:** `DAT_117a1590`

**Function:** `FUN_10818380`



## LosingMoney

**Example:** `LosingMoney()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns whether or not the factions regular expenditure exceeds their regular income

**Author:** `DAT_1179b680`

**Function:** `FUN_10818440`



## MapPosition

**Example:** `MapPosition(x, y)`

**Arguments:** `Location on the map`

**Description:**  
check to see if a map location matches the one return by the context

**Author:** `DAT_1179ebf0`

**Function:** `FUN_107e7c00`



## MapPositionNear

**Example:** `MapPositionNear(x, y, distance)`

**Arguments:** `Location on the map`

**Description:**  
check to see if a map location is near the one returned by the context

**Author:** `DAT_1179b680`

**Function:** `LAB_107e7b40`



## NoActionThisTurn

**Example:** `NoActionThisTurn()`

**Arguments:** `DAT_1173e900`

**Description:**  
Has an action occured this turn for this character?

**Author:** `DAT_117a159c`

**Function:** `FUN_108184d0`



## OffensiveSiegesFought

**Example:** `OffensiveSiegesFought()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the number of siege offences a general has attempted

**Author:** `DAT_117a1590`

**Function:** `FUN_10818530`



## OffensiveSiegesWon

**Example:** `OffensiveSiegesWon()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the number of siege offences a general has won

**Author:** `DAT_117a1590`

**Function:** `FUN_108185a0`



## OnAWarFooting

**Example:** `OnAWarFooting()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns whether or not the characters faction is at war with anyone

**Author:** `DAT_1179b680`

**Function:** `FUN_10818610`



## ParentId

**Example:** `ParentId(\"tax_slider\")`

**Arguments:** `Component id`

**Description:**  
Returns true if the name of the Components parent matches the id specified

**Author:** `DAT_117b0390`

**Function:** `LAB_116c8280`



## PercentageUnspentIncome

**Example:** `PercentageUnspentIncome()`

**Arguments:** `DAT_1178eec8`

**Description:**  
What percentage of the characters factions income remains unspent?

**Author:** `DAT_117a159c`

**Function:** `FUN_10818980`



## PlayerFactionIsAttacker

**Example:** `PlayerFactionIsAttacker()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the attackers faction the local faction?

**Author:** `DAT_117a159c`

**Function:** `FUN_10818ad0`



## PortBlockaded

**Example:** `PortBlockaded()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the port blockaded, and did it start in the last round?

**Author:** `DAT_117a159c`

**Function:** `FUN_10818c50`



## PortBlockadedLocal

**Example:** `PortBlockadedLocal()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the port blockaded by the local faction, and did it start in the last round?

**Author:** `DAT_117a159c`

**Function:** `FUN_10818b60`



## RandomPercentCampaign

**Example:** `RandomPercentCampaign(50)`

**Arguments:** `Number between 0 and 100 to test against`

**Description:**  
Returns true parameter-value-percent of the time

**Author:** `DAT_117a1590`

**Function:** `FUN_10818e30`



## RegionBuildableSlotEmpty

**Example:** `RegionBuildableSlotEmpty()`

**Arguments:** `DAT_1173e900`

**Description:**  
Has the slot not been developed?

**Author:** `DAT_117a1590`

**Function:** `FUN_10818f20`



## RegionBuildingFinished

**Example:** `RegionBuildingFinished()`

**Arguments:** `DAT_1173e900`

**Description:**  
Gets the key of the last building constructed in the region

**Author:** `DAT_117a1590`

**Function:** `FUN_10819050`



## RegionClamoursReform

**Example:** `RegionClamoursReform()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the population in this region clamouring for reform

**Author:** `DAT_117a1590`

**Function:** `FUN_108190d0`



## RegionCultureIsFactionCulture

**Example:** `RegionCultureIsFactionCulture()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the region\'s originating culture the same as the owning factions culture

**Author:** `DAT_117a1590`

**Function:** `FUN_10819140`



## RegionDemands

**Example:** `RegionDemands()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the population in this region writing letters of demand

**Author:** `DAT_117a1590`

**Function:** `FUN_108191f0`



## RegionEconomicGrowthLow

**Example:** `RegionEconomicGrowthLow()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is this regions economic growth low?

**Author:** `DAT_117a159c`

**Function:** `FUN_10819260`



## RegionGovernorAttribute

**Example:** `RegionGovernorAttribute(\"management\")`

**Arguments:** `The attribute which you wish to check on the regions governor`

**Description:**  
Gets the level of the regions governers attribute specified as a parameter

**Author:** `DAT_117a159c`

**Function:** `LAB_10812850`



## RegionIsLocal

**Example:** `RegionIsLocal()`

**Arguments:** `DAT_1173e900`

**Description:**  
Does the region belong to the player faction?

**Author:** `DAT_117a1590`

**Function:** `FUN_108192d0`



## RegionIsRebelling

**Example:** `RegionIsRebelling(\"ita_alpes_maritimes\")`

**Arguments:** `Key of the region to query`

**Description:**  
Is the specified region rebelling. Requires faction context.

**Author:** `DAT_117a1590`

**Function:** `FUN_10819380`



## RegionMajorityReligion

**Example:** `RegionMajorityReligion(\"rel_buddhist\")`

**Arguments:** `religion key from region table`

**Description:**  
Returns whether the region context\'s religion with largest percentage matches the specified religion

**Author:** `DAT_1179b680`

**Function:** `FUN_10819420`



## RegionName

**Example:** `RegionName(\"jap_owari\")`

**Arguments:** `The db record for the region`

**Description:**  
Is the region the one specified?

**Author:** `DAT_1179b680`

**Function:** `FUN_10819550`



## RegionPopulationLow

**Example:** `RegionPopulationLow()`

**Arguments:** `DAT_1173e900`

**Description:**  
Tests if the population of a region is has dropped below the previous town spawn threshold e.g. region has 5 towns but has dropped below the population requirement for 4 towns

**Author:** `DAT_117a1590`

**Function:** `FUN_108195f0`



## RegionPopulationMaxReached

**Example:** `RegionPopulationMaxReached()`

**Arguments:** `DAT_1173e900`

**Description:**  
Tests if the population of a region the maximum population

**Author:** `DAT_117a1590`

**Function:** `FUN_108196a0`



## RegionRebels

**Example:** `RegionRebels()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the region rebelling

**Author:** `DAT_117a1590`

**Function:** `FUN_10819720`



## RegionReligionIsStateReligion

**Example:** `RegionReligionIsStateReligion()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the region\'s religion the same as the owning factions religion

**Author:** `DAT_117a1590`

**Function:** `FUN_10819790`



## RegionResourceExists

**Example:** `RegionResourceExists(\"res_gold\")`

**Arguments:** `Valid entry from \'key\' field from resources table in Empire.mdb`

**Description:**  
Returns whether the resource exists in the region

**Author:** `DAT_1179b680`

**Function:** `LAB_10819830`



## RegionResourceExploited

**Example:** `RegionResourceExploited(\"res_gold\")`

**Arguments:** `Valid entry from \'key\' field from resources table in Empire.mdb`

**Description:**  
Returns whether the resource is produced in the region

**Author:** `DAT_1179b680`

**Function:** `FUN_10819990`



## RegionRiots

**Example:** `RegionRiots()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the population in this region rioting

**Author:** `DAT_117a1590`

**Function:** `FUN_10819a50`



## RegionSlotBuildingCount

**Example:** `RegionSlotBuildingCount()`

**Arguments:** `DAT_1173e900`

**Description:**  
Counts the number of buildings in the region slots in the region

**Author:** `DAT_117a1590`

**Function:** `FUN_10819ac0`



## RegionSlotBuildingCultureExists

**Example:** `RegionSlotBuildingCultureExists(\"european\")`

**Arguments:** `The key of the culture from the cultures table`

**Description:**  
Tests if the region has a building from the given culture

**Author:** `DAT_117a1590`

**Function:** `FUN_10819b60`



## RegionSlotBuildingTypeCount

**Example:** `RegionSlotBuildingTypeCount(\"barracks\")`

**Arguments:** `The key of the building level you are querying from the building_levels table`

**Description:**  
Counts the number of buildings in the region slots in the region of the specified type

**Author:** `DAT_117a1590`

**Function:** `FUN_10819c90`



## RegionSlotBuildingTypeExists

**Example:** `RegionSlotBuildingTypeExists(\"barracks\")`

**Arguments:** `The key of the building level you are querying from the building_levels table`

**Description:**  
Tests if a building of the specified type exists in the region

**Author:** `DAT_117a1590`

**Function:** `FUN_10819db0`



## RegionSlotCount

**Example:** `RegionSlotCount()`

**Arguments:** `DAT_1173e900`

**Description:**  
Counts the number of slots in a region including settlement slots

**Author:** `DAT_117a1590`

**Function:** `FUN_10819e80`



## RegionSlotEmptyCount

**Example:** `RegionSlotEmptyCount()`

**Arguments:** `DAT_1173e900`

**Description:**  
Counts the number of empty (no building) slots in a region including settlement slots

**Author:** `DAT_117a1590`

**Function:** `FUN_10819f20`



## RegionSlotTypeExists

**Example:** `RegionSlotTypeExists(\"fish\")`

**Arguments:** `The key of the slot type you wish to find from the slots table`

**Description:**  
Tests to see if the region has a slot (in any status) whose type matches the parameter

**Author:** `DAT_117a1590`

**Function:** `FUN_1081a010`



## RegionTaxExempt

**Example:** `RegionTaxExempt()`

**Arguments:** `DAT_117af218`

**Description:**  
Gets whether the region is tax exempt or not

**Author:** `DAT_117a159c`

**Function:** `FUN_1081a0d0`



## RegionTaxLevel

**Example:** `RegionTaxLevel()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the regions tax level

**Author:** `DAT_1179b680`

**Function:** `FUN_1081a130`



## RegionTaxTownWealthGrowthReduction

**Example:** `RegionTaxTownWealthGrowthReduction() > 1`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the percentage of the regions town wealth growth lost due to taxes

**Author:** `DAT_1179b680`

**Function:** `FUN_1081a1c0`



## RegionTownWealthGrowth

**Example:** `RegionTownWealthGrowth() > 50`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the town wealth growth of the region

**Author:** `DAT_1179b680`

**Function:** `FUN_1081a240`



## RegionWealthDecrease

**Example:** `RegionWealthDecrease()`

**Arguments:** `DAT_1173e900`

**Description:**  
How much has the regions wealth decreased?

**Author:** `DAT_117a159c`

**Function:** `FUN_1081a2b0`



## RegionWealthIncrease

**Example:** `RegionWealthIncrease()`

**Arguments:** `DAT_1173e900`

**Description:**  
How much has the regions wealth increased?

**Author:** `DAT_117a159c`

**Function:** `LAB_1081a350`



## RegionWouldBeHappyWithNoTaxExemption

**Example:** `RegionWouldBeHappyWithNoTaxExemption()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Checks whether the region happiness would be zero or greater if it was not exempt from tax

**Author:** `DAT_1179b680`

**Function:** `FUN_10166b40`



## ResearchCategory

**Example:** `ResearchCategory(\"enlightenment\")`

**Arguments:** `Category`

**Description:**  
Is the research just completed of this category?

**Author:** `DAT_117a159c`

**Function:** `LAB_1081a3f0`



## ResearchQueueIdle

**Example:** `ResearchQueueIdle()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is faction not researching any tech evn though they could be

**Author:** `DAT_117a1590`

**Function:** `FUN_1081a4a0`



## ResearchType

**Example:** `ResearchType(\"military_navy_flintlock_cannon\")`

**Arguments:** `Research type`

**Description:**  
Is the technology just researched of this type?

**Author:** `DAT_117a159c`

**Function:** `FUN_1081a5f0`



## ResearchTypeUniqueToFaction

**Example:** `ResearchTypeUniqueToFaction()`

**Arguments:** `Research type`

**Description:**  
Are we the first faction to research this technology type?

**Author:** `DAT_117a159c`

**Function:** `FUN_1081a510`



## SeaTradeRouteRaided

**Example:** `SeaTradeRouteRaided()`

**Arguments:** `DAT_1173e900`

**Description:**  
Was one of this factions sea trade routes has been raided in the last round?

**Author:** `DAT_117a159c`

**Function:** `FUN_1081a680`



## SettlementBuildingQueueIdleDespiteCash

**Example:** `SettlementBuildingQueueIdleDespiteCash()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the settlement\'s building queue empty even though the faction can afford to build the cheapest building in any of its slot?

**Author:** `DAT_117a1590`

**Function:** `FUN_1081a6e0`



## SettlementFortificationsBuildingQueueIdleDespiteCash

**Example:** `SettlementFortificationsBuildingQueueIdleDespiteCash()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the settlements\'s fortification building queue empty even though the faction can afford to build the cheapest building?

**Author:** `DAT_117a1590`

**Function:** `LAB_1081a7d0`



## SettlementIsLocal

**Example:** `SettlementIsLocal()`

**Arguments:** `DAT_1173e900`

**Description:**  
Does the settlement belong to the player faction?

**Author:** `DAT_117a1590`

**Function:** `FUN_1081a870`



## SettlementName

**Example:** `SettlementName(\"settlement:acadia:fort_nashwaak\")`

**Arguments:** `The unique id of the settlement from the campaign_map_settlements table or a character, in which case it looks at the settlement the character is in`

**Description:**  
Is the settlement\'s unique id equal to the parameter?

**Author:** `DAT_117a1590`

**Function:** `FUN_1081a8f0`



## SlotBuildingQueueIdleDespiteCash

**Example:** `SlotBuildingQueueIdleDespiteCash()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the slot\'s building queue empty even though the faction can afford to build the cheapest building?

**Author:** `DAT_117a1590`

**Function:** `FUN_1081a9c0`



## SlotIsAlliedCampaign

**Example:** `SlotIsAlliedCampaign()`

**Arguments:** `DAT_1173e900`

**Description:**  
Does the slot belong to a faction allied to the player faction?

**Author:** `DAT_117a159c`

**Function:** `LAB_1081aa50`



## SlotIsLocal

**Example:** `SlotIsLocal()`

**Arguments:** `DAT_1173e900`

**Description:**  
Does the slot belong to the player faction?

**Author:** `DAT_117a1590`

**Function:** `FUN_1081aad0`



## SlotName

**Example:** `SlotName(\"port:england:portsmouth\")`

**Arguments:** `The name of the slot to check for`

**Description:**  
Returns if the passed slot name is equal to the slot\'s name

**Author:** `DAT_117a1590`

**Function:** `FUN_1081ab50`



## SlotSuperchain

**Example:** `SlotType(\"wheat\")`

**Arguments:** `The slot superchain type (key from the building superchains table)`

**Description:**  
Is the slot\'s superchain from the building superchains table equal to the parameter?

**Author:** `DAT_117a1594`

**Function:** `FUN_1081ac00`



## SlotType

**Example:** `SlotType(\"wheat\")`

**Arguments:** `The slot type (key from the slots table)`

**Description:**  
Is the slot\'s type from the slots table equal to the parameter?

**Author:** `DAT_117a1590`

**Function:** `FUN_1081acc0`



## SupportCostsPercentage

**Example:** `SupportCostsPercentage()`

**Arguments:** `DAT_1173e900`

**Description:**  
The percentage of outgoings used for upkeep in the recent turns for the given faction

**Author:** `DAT_117a159c`

**Function:** `FUN_1081ad60`



## TargetArmyGreaterCombatStrength

**Example:** `TargetArmyGreaterCombatStrength()`

**Arguments:** `DAT_1178eec8`

**Description:**  
The does the target army have greater combat strength than the character?

**Author:** `DAT_117a1590`

**Function:** `FUN_1081ae70`



## TargetCharacterIsAlliedCampaign

**Example:** `TargetCharacterIsAlliedCampaign()`

**Arguments:** `DAT_1178eec8`

**Description:**  
The target character is allied to the character?

**Author:** `DAT_117a1590`

**Function:** `FUN_1081af10`



## TargetCharacterIsEnemyCampaign

**Example:** `TargetCharacterIsEnemyCampaign()`

**Arguments:** `DAT_1178eec8`

**Description:**  
The target character is an enemy of the character?

**Author:** `DAT_117a1590`

**Function:** `FUN_1081afb0`



## TargetInStrikingRangeOfEnemy

**Example:** `CharacterIsEnemy()`

**Arguments:** `DAT_1178eec8`

**Description:**  
The character is an enemy of the local faction?

**Author:** `DAT_117a1590`

**Function:** `FUN_1081b050`



## TaxCollectionLimited

**Example:** `TaxCollectionLimited()`

**Arguments:** `DAT_1173e900`

**Description:**  
Are all the factions government building at the maximum level (and thus impossible to upgrade)?

**Author:** `DAT_1179b680`

**Function:** `FUN_1081b0f0`



## TaxLevel

**Example:** `FactionTaxLevel() < TaxLevel(\"extortionate\")`

**Arguments:** `Valid entry from \'key\' field from taxes_levels table in Empire.mdb`

**Description:**  
Returns the tax level for the given tax key

**Author:** `DAT_1179b680`

**Function:** `FUN_1081b1e0`



## TradeNodeAvailableWorldwide

**Example:** `TradeNodeAvailableWorldwide()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Is there an unoccupied trade node (worldwide). Requires faction context

**Author:** `DAT_117a1590`

**Function:** `FUN_1081b2c0`



## TradePortsAtMaxLevel

**Example:** `TradePortsAtMaxLevel()`

**Arguments:** `DAT_1173e900`

**Description:**  
Are all of the regions trade ports at the maximum level (and thus impossible to upgrade)?

**Author:** `DAT_1179b680`

**Function:** `FUN_1081b350`



## TradeRouteIsEnemy

**Example:** `TradeRouteIsEnemy()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Returns whether the trade route attacked is used by an enemy of the local faction

**Author:** `DAT_117a159c`

**Function:** `FUN_1081b410`



## TradeRouteIsLocal

**Example:** `TradeRouteIsLocal()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Returns whether the trade route attacked is used by the local faction

**Author:** `DAT_117a159c`

**Function:** `FUN_1081b540`



## TradeRouteLimitReached

**Example:** `TradeRouteLimitReached()`

**Arguments:** `DAT_1173e900`

**Description:**  
Has the faction reached its limit of trade routes?

**Author:** `DAT_1179b680`

**Function:** `FUN_1081b690`



## TurnNumber

**Example:** `TurnNumber()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Returns the number of the turn currently being taken, starting at 1

**Author:** `DAT_1173e50c`

**Function:** `FUN_1081b780`



## TurnsSinceThreadLastAdvanced

**Example:** `TurnsSinceThreadLastAdvanced(\"0001_Battle_Advice_Friendly_Fire_Thread\")`

**Arguments:** `Key from advice_threads table`

**Description:**  
The number of turns since the advice thread was last advanced - 0 signifies that the thread is unadvanced or the number of turns cannot be established

**Author:** `DAT_1173e50c`

**Function:** `FUN_100e2390`



## UnitCategory

**Example:** `UnitCategory(\"naval_frigate\")`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the unit of this category type?

**Author:** `DAT_117a159c`

**Function:** `FUN_1081b930`



## UnitClass

**Example:** `UnitClass(\"cavalry_missile\")`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the unit of this class?

**Author:** `DAT_117a159c`

**Function:** `FUN_1081b9e0`



## UnitCrushedInsurrection

**Example:** `UnitCrushedInsurrection()`

**Arguments:** `DAT_1173e900`

**Description:**  
Did the given unit crush an insurrection in the last turn?

**Author:** `DAT_117a159c`

**Function:** `FUN_10166b40`



## UnitCultureType

**Example:** `UnitCultureType(\"tribal\")`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the unit of this culture type?

**Author:** `DAT_117a159c`

**Function:** `FUN_1081ba90`



## UnitFoughtInBattle

**Example:** `UnitFoughtInBattle()`

**Arguments:** `DAT_1173e900`

**Description:**  
Did the unit fight in the last battle?

**Author:** `DAT_117a159c`

**Function:** `FUN_1081bb50`



## UnitFoughtInMelee

**Example:** `UnitFoughtInMelee()`

**Arguments:** `DAT_1173e900`

**Description:**  
Did the unit melee fight in the last battle?

**Author:** `DAT_117a159c`

**Function:** `FUN_1081bc80`



## UnitInTheatre

**Example:** `UnitInTheatre(\"-1133129049\")`

**Arguments:** `DAT_1173e900`

**Description:**  
Is this unit within the specified theatre?

**Author:** `DAT_117a159c`

**Function:** `FUN_1081bdb0`



## UnitOnContinent

**Example:** `UnitOnContinent(\"cont_africa_south\")`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the given unit on the specified continent?

**Author:** `DAT_117a159c`

**Function:** `FUN_10166b40`



## UnitRouted

**Example:** `UnitRouted()`

**Arguments:** `DAT_1173e900`

**Description:**  
Did the given unit rout?

**Author:** `DAT_117a159c`

**Function:** `FUN_1081bea0`



## UnitSufferedCasualties

**Example:** `UnitSufferedCasualties()`

**Arguments:** `DAT_1173e900`

**Description:**  
What percentage of casualties did this unit suffer?

**Author:** `DAT_117a159c`

**Function:** `FUN_1081bfd0`



## UnitTrait

**Example:** `UnitTrait(\"U_Infected_Dysentry\") > 2`

**Arguments:** `Trait name`

**Description:**  
Returns the value of the specified trait (0 if not present)

**Author:** `DAT_117a159c`

**Function:** `FUN_1081c190`



## UnitType

**Example:** `UnitType(\"euro_line_infantry\")`

**Arguments:** `The unit key from the units table`

**Description:**  
Is the unit\'s unit record key equal to the parameter?

**Author:** `DAT_117a1590`

**Function:** `FUN_1081c220`



## UnitWonBattle

**Example:** `UnitWonBattle()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Is the unit part of the winning alliance in a battle?

**Author:** `DAT_117a159c`

**Function:** `FUN_1081c2d0`



## UnusedInternationalTradeRoute

**Example:** `UnusedInternationalTradeRoute()`

**Arguments:** `DAT_1173e900`

**Description:**  
Could the faction establish a new international trade route?

**Author:** `DAT_1179b680`

**Function:** `FUN_1081c360`



## WarEndedCharacterFaction

**Example:** `WarEndedCharacterFaction()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Was peace declared between this faction and another faction this turn?

**Author:** `DAT_117a159c`

**Function:** `FUN_1081c450`



## WarStartedCharacterFaction

**Example:** `WarStartedCharacterFaction()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Did a war start between this faction and another faction this turn?

**Author:** `DAT_117a159c`

**Function:** `FUN_1081c4c0`



## WorldResourceExists

**Example:** `WorldResourceExists(\"res_gold\")`

**Arguments:** `Valid entry from \'key\' field from resources table in Empire.mdb`

**Description:**  
Returns whether the resource exists anywhere

**Author:** `DAT_1179b680`

**Function:** `FUN_1081c530`



## WorldResourceExploited

**Example:** `WorldResourceExploited(\"res_gold\")`

**Arguments:** `Valid entry from \'key\' field from resources table in Empire.mdb`

**Description:**  
Returns whether the resource is produced by any faction

**Author:** `DAT_1179b680`

**Function:** `FUN_1081c6e0`



## WorldwideAncillaryTypeExists

**Example:** `WorldwideAncillaryTypeExists(\"unkillable_cat\") == true`

**Arguments:** `Ancillary name`

**Description:**  
Returns whether the named ancillary exists in the world somewhere

**Author:** `DAT_117a2ecc`

**Function:** `FUN_1081c7c0`



## is_advice_audio_playing

**Example:** `is_advice_audio_playing()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns whether audio for any advice is currently playing

**Author:** `DAT_1173e71c`

**Function:** `LAB_100eab40`


