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



## AnyFactionDestroyedLastTurn

**Example:** `AnyFactionDestroyedLastTurn()`

**Arguments:** `DAT_1173e900`

**Description:**  
Has any faction been destroyed since the last turn



## ArmyIsAlliedCampaign

**Example:** `ArmyIsAlliedCampaign()`

**Arguments:** `DAT_1173e900`

**Description:**  
Does the army belong to a faction allied to the player faction



## ArmyIsLocalCampaign

**Example:** `ArmyIsLocalCampaign()`

**Arguments:** `DAT_1173e900`

**Description:**  
Does the army belong to the player faction?



## BattleAllianceHasDeployables

**Example:** `BattleAllianceHasDeployables()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if the alliance has deployables



## BattleAllianceIsAttacker

**Example:** `BattleAllianceIsAttacker()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if the alliance is the attacker from the campaign map



## BattleAllianceIsPlayers

**Example:** `BattleAllianceIsPlayers()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if the alliance contains the players army



## BattleAllianceNumberOfShips

**Example:** `BattleAllianceNumberOfShips()`

**Arguments:** `No parameters needed`

**Description:**  
Returns the number of ships in all the armies of the alliance



## BattleAllianceNumberOfUnits

**Example:** `BattleAllianceNumberOfUnits()`

**Arguments:** `No parameters needed`

**Description:**  
Returns the number of units in all the armies of the alliance



## BattleCommanderIsGeneral

**Example:** `BattleCommanderIsGeneral()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if the the alliance has a general and not just a colonel



## BattleEnemyAlliancePercentageCanHide

**Example:** `BattleEnemyAlliancePercentageCanHide()`

**Arguments:** `No parameters needed`

**Description:**  
Checks the percentage of enemy units ( in alliance ) that can hide, returns a percentage



## BattleEnemyAlliancePercentageOfClassAndCategory

**Example:** `BattleEnemyAlliancePercentageOfClassAndCategory(\"class\", \"category\")`

**Arguments:** `Two lowercase strings, first being the particular class string ( see unit_stats_land table ) and second being the category string ( see units table )`

**Description:**  
Takes in class and category of a particular unit and goes through every enemy army, returning the percentage of units that match the class and category



## BattleEnemyAlliancePercentageOfMountType

**Example:** `BattleEnemyAlliancePercentageOfMountType(\"mount_type\")`

**Arguments:** `A lowercase string with the unit\'s mount type to be checked ( see type in battle_entities table )`

**Description:**  
Determine the percentage of units in the enemies army that have the type of mount passed to the condition



## BattleEnemyAlliancePercentageOfSpecialAbility

**Example:** `BattleEnemyAlliancePercentageOfSpecialAbility(\"ability\")`

**Arguments:** `Special Ability string : pike_square_formation, pike_wall_formation, square_formation, wedge_formation, diamond_formation, light_infantry_behaviour, loose_formation, fire_and_advance, plug_bayonets, dismount, unlimber, none`

**Description:**  
Checks all of the Armies in the enemy alliances for the particular special ability



## BattleEnemyAlliancePercentageOfUnitCategory

**Example:** `BattleEnemyAlliancePercentageOfUnitCategory(\"category\")`

**Arguments:** `One lowercase string with the unit\'s category name ( see units table )`

**Description:**  
Take in the name of the unit\'s category and returns the percentage of units in the alliance that match the given category



## BattleEnemyAlliancePercentageOfUnitClass

**Example:** `BattleEnemyAlliancePercentageOfUnitClass(\"class\")`

**Arguments:** `One lowercase string with the unit\'s class name ( see unit_stats_land table )`

**Description:**  
Takes in the name of the unit\'s class and returns the percentage of units in the alliance that match the given class



## BattleEnemyDirectionOfMeleeAttack

**Example:** `BattleEnemyDirectionOfMeleeAttack(\"left_flank\")`

**Arguments:** `Possible string paramaters are \"front\", \"left_flank\", \"right_flank\" and \"behind\`

**Description:**  
Returns true if the passed parameter matches the direction of melee attack for the enemy unit



## BattleEnemyHasMissileSuperiority

**Example:** `BattleEnemyHasMissileSuperiority()`

**Arguments:** `No paramaters needed`

**Description:**  
Returns true if the combined missile streangth of the enemy is greater than the missile streangth of the player



## BattleEnemyShipActionStatus

**Example:** `BattleEnemyShipActionStatus`

**Arguments:** `Single string with action status`

**Description:**  
Returns true if the action status of the enemy ship matches : dismasted, firing, hull_damaged, routing, sinking, wavering.



## BattleEnemyShipOnFire

**Example:** `BattleEnemyShipOnFire()`

**Arguments:** `No parameters needed`

**Description:**  
Checks whether any of the enemies ships are on fire, returns true or false



## BattleEnemyUnitActionStatus

**Example:** `BattleEnemyUnitActionStatus(\"hiding\")`

**Arguments:** `Single string with action status`

**Description:**  
Returns true if the action status of the enemy unit matches : charging, exhausted, fighting_melee, firing, hiding, idling moving, moving_fast, pursue_routers, rallying, routing, wavering.



## BattleEnemyUnitCategory

**Example:** `BattleEnemyUnitCategory(\"category\")`

**Arguments:** `One lowercase string with the enemies unit\'s category name ( see units table )`

**Description:**  
Takes in a unit category string and returns true if there is an enemy and it matches the category of the enemy unit



## BattleEnemyUnitClass

**Example:** `BattleEnemyUnitClass(\"class\")`

**Arguments:** `One lowercase string with the unit\'s class name ( see unit_stats_land table )`

**Description:**  
Takes in a unit class string and returns true if it matches the unit class of the enemy unit



## BattleEnemyUnitCurrentFormation

**Example:** `DAT_1173dad0`

**Arguments:** `Takes in a single string which can be one of the following : block_formation, pike_square_formation, pike_wall_formation, square_formation, diamond_formation, wedge_formation, light_infantry_behaviour.`

**Description:**  
Returns true if the unit has an enemy and the string matches the current formation employed by the enemy, otherwise it returns false



## BattleEnemyUnitOnLeftFlank

**Example:** `BattleEnemyUnitOnLeftFlank()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if there\'s an enemy unit on the left flank



## BattleEnemyUnitOnRightFlank

**Example:** `BattleEnemyUnitOnRightFlank()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if there\'s an enemy unit on the right flank



## BattleEnemyUnitSpecialAbilitySupported

**Example:** `BattlePlayerUnitSpecialAbilitySupported(\"ability\")`

**Arguments:** `Special Ability string : pike_square_formation, pike_wall_formation, square_formation, wedge_formation, diamond_formation, light_infantry_behaviour,  loose_formation, fire_and_advance, plug_bayonets, fougasse_improved, fougasse_basic, wooden_stakes, chevaux_de_frise, gabionade, earthworks, dismount, unlimber, none`

**Description:**  
If there is an enemy unit then the condition checks all of the enemy unit\'s special abilities and returns true if the unit has the special ability



## BattleEnemyUnitTechnologySupported

**Example:** `BattleEnemyUnitTechnologySupported(\"ring_bayonets\")`

**Arguments:** `Technology string : ring_bayonets, socket_bayonets, fire_mounted`

**Description:**  
Checks whether the unit has the technology passed in and returns true if the unit has the technology



## BattleHasCoverBuildings

**Example:** `BattleHasCoverBuildings()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if it finds an occupiable building



## BattleHasCoverWalls

**Example:** `BattleHasCoverWalls()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if the battlefield has walls that the men can take cover against



## BattleIsAmbushConflict

**Example:** `BattleIsAmbushConflict()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if there is a fort in the battle



## BattleIsLandConflict

**Example:** `BattleIsLandConflict()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if battle is being fought on land (this will NOT return true for fort battles)



## BattleIsNavalConflict

**Example:** `BattleIsNavalConflict()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if battle is being fought on sea



## BattleIsSiegeConflict

**Example:** `BattleIsSiegeConflict()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if there is a fort in the battle



## BattlePlayerAllianceDefendingHill

**Example:** `BattlePlayerAllianceDefendingHill()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if a unit in the alliance is stationed on a hill



## BattlePlayerAlliancePercentageCanHide

**Example:** `BattlePlayerAlliancePercentageCanHide()`

**Arguments:** `No parameters needed`

**Description:**  
Checks the percentage of player units ( in alliance ) that can hide, returns a percentage



## BattlePlayerAlliancePercentageGuerrillas

**Example:** `BattlePlayerAlliancePercentageGuerrillas`

**Arguments:** `A single string representing the class of a unit ( see unit_stats_land table )`

**Description:**  
Goes through the players alliance and searches for all the units that have guerrilla deployment



## BattlePlayerAlliancePercentageOfAmmoType

**Example:** `BattlePlayerAlliancePercentageOfAmmoType(\"bullet\")`

**Arguments:** `Takes in a string describing the shottype ( see projectile_shot_type_enum_table )`

**Description:**  
Returns the percentage of units in the alliance that have the specified ammo type



## BattlePlayerAlliancePercentageOfClassAndCategory

**Example:** `BattlePlayerAlliancePercentageOfClassAndCategory(\"class\", \"category\")`

**Arguments:** `Two lowercase strings, first being the particular class string (see unit_stats_land table ) and second being the category string ( see units table )`

**Description:**  
Takes in Class and Category of a particular unit and goes through players army and returns the percentage that match the class and category



## BattlePlayerAlliancePercentageOfMountType

**Example:** `BattlePlayerPercentageOfMountType(\"mount_type\")`

**Arguments:** `A lowercase string with the unit\'s mount type to be checked ( see type in battle_entities table )`

**Description:**  
Determine the percentage of units in the players army that have the type of mount passed to the condition



## BattlePlayerAlliancePercentageOfSpecialAbility

**Example:** `BattlePlayerAlliancePercentageOfSpecialAbility(\"ability\")`

**Arguments:** `Special Ability string : pike_square_formation, pike_wall_formation, square_formation, wedge_formation, diamond_formation, light_infantry_behaviour, loose_formation, fire_and_advance, plug_bayonets, dismount, unlimber, none`

**Description:**  
Checks all of the Armies in the players alliance for the special ability



## BattlePlayerAlliancePercentageOfTechnology

**Example:** `BattlePlayerAlliancePercentageOfTechnology(\"ring_bayonets\")`

**Arguments:** `Technology string : ring_bayonets, socket_bayonets, fire_mounted`

**Description:**  
Checks all of the Armies in the players alliance for the technology and returns the percentage of those that have it



## BattlePlayerAlliancePercentageOfUnitCategory

**Example:** `BattlePlayerAlliancePercentageOfUnitCategory(\"category\")`

**Arguments:** `A single string representing the category of a unit ( see units table )`

**Description:**  
Goes through the players alliance and searches for all the units that fit the given category description



## BattlePlayerAlliancePercentageOfUnitClass

**Example:** `BattlePlayerAlliancePercentageOfUnitClass(\"class\")`

**Arguments:** `A single string representing the class of a unit ( see unit_stats_land table )`

**Description:**  
Goes through the players alliance and searches for all the units that fit the given class description



## BattlePlayerAllianceToEnemyAllianceRatio

**Example:** `BattlePlayerAllianceToEnemyAllianceRatio() > 0.5 would mean that the players alliance has half as many men as the enemy\'s alliance`

**Arguments:** `No parameters needed`

**Description:**  
Returns the ratio PlayersAlliance/EnemyAlliance in terms of men on the battlefield



## BattlePlayerDefendingFort

**Example:** `BattlePlayerDefendingFort()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if player is still in control of the fort and is tasked to defend it.



## BattlePlayerDirectionOfMeleeAttack

**Example:** `BattlePlayerDirectionOfMeleeAttack(\"left_flank\")`

**Arguments:** `Possible string paramaters are \"front\", \"left_flank\", \"right_flank\" and \"behind\`

**Description:**  
Returns true if the passed parameter matches the direction of melee attack for the unit



## BattlePlayerDirectionOfMissileAttack

**Example:** `BattlePlayerDirectionOfMissileAttack(\"right_flank\")`

**Arguments:** `Possible string paramaters are \"front\", \"left_flank\", \"right_flank\" and \"behind\`

**Description:**  
Returns true if the passed parameter matches the direction of missile attack for the unit



## BattlePlayerSailsPercentageDamaged

**Example:** `BattlePlayerSailsPercentageDamaged()`

**Arguments:** `No parameters needed`

**Description:**  
Returns the floating point value of percentage damaged in the range 0.0 to 100.0



## BattlePlayerShipActionStatus

**Example:** `BattlePlayerShipActionStatus(\"hiding\")`

**Arguments:** `Single string with action status`

**Description:**  
Returns true if the action status of the ship : dismasted, firing, hull_damaged, routing, sinking, wavering.



## BattlePlayerShipClass

**Example:** `BattlePlayerShipClass(\"class\")`

**Arguments:** `One lowercase string with the unit\'s class name ( see unit_stats_naval table )`

**Description:**  
Takes in a ship class and returns true if it matches the ship class of the ship



## BattlePlayerUnitActionStatus

**Example:** `BattlePlayerUnitActionStatus(\"hiding\")`

**Arguments:** `Single string with action status`

**Description:**  
Returns true if the action status of the unit matches UNIT: charging, exhausted, fighting_melee, firing, hiding, idling moving, moving_fast, pursue_routers, rallying, routing, wavering.



## BattlePlayerUnitAmmoType

**Example:** `BattlePlayerUnitAmmoType(\"bullet\")`

**Arguments:** `Takes in a string describing the shottype ( see projectile_shot_type_enum table )`

**Description:**  
Returns true if the unit has the ammo type



## BattlePlayerUnitCategory

**Example:** `BattlePlayerUnitCategory(\"category\")`

**Arguments:** `One lowercase string with the unit\'s category name ( see units table )`

**Description:**  
Takes in a unit category string and returns true if it matches the unit category of the unit



## BattlePlayerUnitClass

**Example:** `BattlePlayerUnitClass(\"class\")`

**Arguments:** `One lowercase string with the unit\'s class name ( see unit_stats_land table )`

**Description:**  
Takes in a unit class string and returns true if it matches the unit class of the unit



## BattlePlayerUnitCurrentFormation

**Example:** `BattlePlayerUnitCurrentFormation( \"pike_square_formation\" )`

**Arguments:** `Takes in a single string which can be one of the following : block_formation, pike_square_formation, pike_wall_formation, square_formation, diamond_formation, wedge_formation, light_infantry_behaviour.`

**Description:**  
Returns true if the string matches the current formation employed, otherwise it returns false



## BattlePlayerUnitDefendingHill

**Example:** `BattlePlayerUnitDefendingHill()`

**Arguments:** `No paramaters needed`

**Description:**  
Returns true if a unit is stationed on a hill



## BattlePlayerUnitEngaged

**Example:** `BattlePlayerUnitEngaged()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if a unit is either in a firefight or melee



## BattlePlayerUnitEngagedInMelee

**Example:** `BattlePlayerUnitEngagedInMelee()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if a unit is in a melee fight



## BattlePlayerUnitMountType

**Example:** `BattlePlayerUnitMountClass(\"mount_type\")`

**Arguments:** `A lowercase string with the unit\'s mount type to be checked ( see type in battle_entities ) table`

**Description:**  
Determines whether the unit is mounted on the type of mount passed to the condition



## BattlePlayerUnitMovingFast

**Example:** `BattlePlayerUnitMovingFast()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if the unit is moving fast, otherwise false



## BattlePlayerUnitSpecialAbilityActive

**Example:** `BattlePlayerUnitSpecialAbilityActive()`

**Arguments:** `Special Ability string : pike_square_formation, pike_wall_formation, square_formation, wedge_formation, diamond_formation, light_infantry_behaviour,  loose_formation, fire_and_advance, plug_bayonets, dismount, unlimber, none`

**Description:**  
Checks whether the specified unit ability is active



## BattlePlayerUnitSpecialAbilitySupported

**Example:** `BattlePlayerUnitSpecialAbilitySupported(\"ability\")`

**Arguments:** `Special Ability string : pike_square_formation, pike_wall_formation, square_formation, wedge_formation, diamond_formation, light_infantry_behaviour,  loose_formation, fire_and_advance, plug_bayonets, dismount, unlimber, none`

**Description:**  
Checks all of the units special abilities and returns true if the unit has ability



## BattlePlayerUnitTechnologySupported

**Example:** `BattlePlayerUnitTechnologySupported(\"ring_bayonets\")`

**Arguments:** `Technology string : ring_bayonets, socket_bayonets, fire_mounted`

**Description:**  
Checks whether the unit has the technology passed in and returns true if the unit has the technology



## BattleResult

**Example:** `BattleResult(\"decisive_victory\")`

**Arguments:** `Result of the battle, e.g. \"crushing_defeat\", \"major_victory\", \"pyrrhic_victory\`

**Description:**  
Returns true if the battle result matches the one supplied



## BattleShipIsPlayers

**Example:** `BattleShipIsPlayers`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if the unit is part of the players army



## BattleShipSailsPercentageDamage

**Example:** `BattlePlayerShipSailsPercentageDamage()`

**Arguments:** `No parameters needed`

**Description:**  
Returns the percentile of damage the sails have recieved in the range 0.0 to 100.0



## BattleTimeLimitSet

**Example:** `BattleTimeLimitSet()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if there\'s an alliance in a the battle that will win on a timeout



## BattleType

**Example:** `BattleType(\"normal\")`

**Arguments:** `Battle type string : normal, land_normal, land_bridge, fort_standard, fort_sally, fort_relief, settlement_standard, settlement_sally, settlement_relief settlement_unfortified, town_normal, naval_normal, naval_blockade, naval_breakout. Please see designers for which of these are supported.`

**Description:**  
Returns true if the battle type matches the one supplied



## BattleUnitIsAllied

**Example:** `BattleUnitIsAllied()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if the unit is part of the players alliance



## BattleUnitIsPlayers

**Example:** `BattleUnitIsPlayers()`

**Arguments:** `No parameters needed`

**Description:**  
Returns true if the unit is part of the players army



## BattlesFought

**Example:** `BattlesFought()`

**Arguments:** `DAT_1178eec8`

**Description:**  
How many battles has this character fought in?



## BuildingLevelName

**Example:** `BuildingLevelName(corn_peasant_farms)`

**Arguments:** `String corresponding to level_name of supplied building level record`

**Description:**  
Flags whether or not the context contains the supplied building level record



## BuildingTypeExistsAtSettlement

**Example:** `BuildingTypeExistsAtSettlement(\"barracks\")`

**Arguments:** `The key of the building level you are querying from the building_levels table`

**Description:**  
Tests if a building of the specified type exists in the region settlement



## BuildingTypeExistsAtSlot

**Example:** `BuildingTypeExistsAtSlot(\"barracks\")`

**Arguments:** `The key of the building level you are querying from the building_levels table`

**Description:**  
Tests if a building of the specified type exists in the region slot



## CampaignBattleType

**Example:** `CampaignBattleType(\"normal\")`

**Arguments:** `Battle type string : normal, land_normal, land_bridge, fort_standard, fort_sally, fort_relief, settlement_standard, settlement_sally, settlement_relief settlement_unfortified, town_normal, naval_normal, naval_blockade, naval_breakout. Please see designers for which of these are supported.`

**Description:**  
Returns true if the battle type matches the one supplied



## CampaignName

**Example:** `CampaignName(\'main\')`

**Arguments:** `Name of the campaign to compare against, from the campaigns table`

**Description:**  
Returns whether or not the current campaign name matches the supplied parameter



## CampaignNumberOfUnitsInEnemyAlliance

**Example:** `CampaignNumberOfUnitsInEnemyAlliance()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Number of units in the alliance opposing character in context



## CampaignNumberOfUnitsInEnemyArmy

**Example:** `CampaignNumberOfUnitsInEnemyArmy()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Number of units in the primary army of the primary faction of the force opposing the army commanded by the character in context



## CampaignNumberOfUnitsInPlayerAlliance

**Example:** `CampaignNumberOfUnitsInPlayerAlliance()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Number of units in the alliance containing character in context



## CampaignNumberOfUnitsInPlayerArmy

**Example:** `CampaignNumberOfUnitsInPlayerArmy()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Number of units in the army commanded by the character in context



## CampaignPercentageOfOwnCaptured

**Example:** `CampaignPercentageOfOwnCaptured()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Percentage of own men/ships captured in the battle that just took place



## CampaignPercentageOfOwnKilled

**Example:** `CampaignPercentageOfOwnKilled()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Percentage of own men/ships killed in the battle that just took place



## CampaignPercentageOfOwnRouted

**Example:** `CampaignPercentageOfOwnRouted()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Percentage of own men/ships that routed in the battle that just took place



## CampaignPercentageOfThemCaptured

**Example:** `CampaignPercentageOfThemCaptured()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Percentage of opposing men/ships captured in the battle that just took place



## CampaignPercentageOfThemKilled

**Example:** `CampaignPercentageOfThemKilled()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Percentage of opposing men/ships killed in the battle that just took place



## CampaignPercentageOfThemRouted

**Example:** `CampaignPercentageOfThemRouted()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Percentage of opposing men/ships that routed in the battle that just took place



## CampaignPercentageOfUnitCategory

**Example:** `CampaignPercentageOfUnitCategory(\"naval_frigate\")`

**Arguments:** `DAT_1178eec8`

**Description:**  
Percentage of type of ships/units under an admirals/generals command



## CanGenerateHistoricalCharacter

**Example:** `CanGenerateHistoricalCharacter(\"abraham_de_moivre\")`

**Arguments:** `Historical character record key`

**Description:**  
DAT_1173dad0



## CharacterAbility

**Example:** `CharacterAbility(\"can_assassinate\")`

**Arguments:** `Ability name (valid key from abilities table)`

**Description:**  
Returns whether a character can perform the ability specified



## CharacterArmyCouldReplenishFromBattle

**Example:** `CharacterArmyCouldReplenishFromBattle()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Test to see if an army involved in the current pending battle and belonging to the player can replenish



## CharacterArmyUsedCoverBuildings

**Example:** `CharacterArmyUsedCoverBuildings()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Did the characters army use buildings for conver?



## CharacterArmyUsedCoverWalls

**Example:** `CharacterArmyUsedCoverWalls()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Did the characters army use walls for cover?



## CharacterAttribute

**Example:** `CharacterAttribute(\"command_land\") >= 2`

**Arguments:** `Attribute name (valid key from agent_attributes table)`

**Description:**  
Returns the value of the attribute specified.  This doesn\'t account for any given situation bonuses



## CharacterBattleWallsBreached

**Example:** `CharacterBattleWallsBreached()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Did the characters army breach the walls of a fort?



## CharacterBuildingConstructed

**Example:** `CharacterBuildingConstructed(\"vineyards\")`

**Arguments:** `The building type`

**Description:**  
Did this building type just get constructed?



## CharacterCapturedEnemyShip

**Example:** `CharacterCapturedEnemyShip()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Did the given character capture an enemy ship?



## CharacterCommandsNavy

**Example:** `CharacterCommandsNavy()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Does a character command a navy?



## CharacterCultureType

**Example:** `CharacterCultureType(\"tribal\")`

**Arguments:** `Valid entry from \'key\' field from cultures table in Empire.mdb`

**Description:**  
Returns true if the character context is of the culture specified



## CharacterDuelWeapon

**Example:** `CharacterDuelWeapon(\"duelling_pistols\")`

**Arguments:** `DAT_1173e900`

**Description:**  
Did the given character use the given weapon in the duel?



## CharacterDuelsFought

**Example:** `CharacterDuelsFought()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Number of duels a character has fought. Character context



## CharacterDuelsLost

**Example:** `CharacterDuelsLost()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Number of duels a character has lost. Character context



## CharacterDuelsWon

**Example:** `CharacterDuelsWon()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Number of duels a character has won. Character context



## CharacterEndedInAmbushPosition

**Example:** `CharacterEndedInAmbushPosition()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns true if the character is in an ambush position, as used in conjunction with out of mp this has just happened



## CharacterFactionAdmiralCount

**Example:** `CharacterFactionAdmiralCount()`

**Arguments:** `DAT_1173e900`

**Description:**  
How many admirals does this characters faction have?



## CharacterFactionGeneralCount

**Example:** `CharacterFactionGeneralCount()`

**Arguments:** `DAT_1173e900`

**Description:**  
How many generals does this characters faction have?



## CharacterFactionHasTechType

**Example:** `CharacterFactionHasTechType(\"enlightenment_abolition_of_slavery\")`

**Arguments:** `A valid key from the technologies table.`

**Description:**  
Does the characters faction have the specified technology



## CharacterFactionMinisterAncillary

**Example:** `CharacterFactionMinisterAncillary(\"Ancillary_Boxer\")`

**Arguments:** `Ancillary name`

**Description:**  
Tests whether any minister in the characters faction has the specified ancillary



## CharacterFactionMinisterTrait

**Example:** `CharacterFactionMinisterTrait(\"drunkard\")`

**Arguments:** `Trait name`

**Description:**  
Tests whether any minister in the characters faction has the named trait



## CharacterFactionName

**Example:** `CharacterFactionName(\"britain\")`

**Arguments:** `The db record key for the faction`

**Description:**  
Is characters faction the one specified?



## CharacterFactionReligion

**Example:** `CharacterFactionReligion(\"rel_buddhist\")`

**Arguments:** `religion key from region table`

**Description:**  
Returns whether the religion of the character context\'s faction matches the specified religion



## CharacterFactionSubcultureType

**Example:** `CharacterFactionSubcultureType(\"sc_indian_islamic\")`

**Arguments:** `Subculture key`

**Description:**  
Is the character part of the given subculture?



## CharacterForename

**Example:** `CharacterForename(\"names_name_names_irishAlan\")`

**Arguments:** `The forename\'s db key`

**Description:**  
Does the character have this forename?



## CharacterFoughtCulture

**Example:** `CharacterFoughtCulture(\"tribal\")`

**Arguments:** `DAT_1178eec8`

**Description:**  
Has this character just fought this culture?



## CharacterHasAncillary

**Example:** `CharacterHasAncillary(\"Ancillary_Boxer\")`

**Arguments:** `Ancillary name`

**Description:**  
Tests whether the character has the specified ancillary



## CharacterHasTrait

**Example:** `CharacterHasTrait(\"drunkard\")`

**Arguments:** `The name of the trait`

**Description:**  
Does this character have the given trait?



## CharacterHoldsPost

**Example:** `CharacterHoldsPost()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Is this character a minister with a post?



## CharacterHusbandHasTrait

**Example:** `CharacterHusbandHasTrait(\"drunkard\")`

**Arguments:** `The name of the trait`

**Description:**  
Does this character\'s husband have the given trait?



## CharacterInBuildingOfChain

**Example:** `CharacterInBuildingOfChain(\"tobacco\")`

**Arguments:** `DAT_1173dad0`

**Description:**  
Is the character in a building of this chain type?



## CharacterInBuildingType

**Example:** `CharacterInBuildingType(\"naval_college\")`

**Arguments:** `DAT_1173dad0`

**Description:**  
Is the character in a building of this type?



## CharacterInEnemyLands

**Example:** `CharacterInEnemyLands()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Is the character in enemy lands?



## CharacterInHomeRegion

**Example:** `CharacterInHomeRegion()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Is the character in their home region?



## CharacterInOwnFactionLands

**Example:** `CharacterInOwnFactionLands()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Is the character in their own factions lands?



## CharacterInRegion

**Example:** `CharacterInRegion(\"england\")`

**Arguments:** `The region key`

**Description:**  
Is the character in the given region?



## CharacterInTheatre

**Example:** `CharacterInTheatre(\"-1133129049\")`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character in the specified theatre



## CharacterIsAlliedCampaign

**Example:** `CharacterIsAllied()`

**Arguments:** `DAT_1178eec8`

**Description:**  
The character is allied to the local faction?



## CharacterIsEnemyCampaign

**Example:** `CharacterIsEnemy()`

**Arguments:** `DAT_1178eec8`

**Description:**  
The character is an enemy of the local faction?



## CharacterIsFemale

**Example:** `CharacterIsFemale()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Returns whether the character in context is female



## CharacterIsLocalCampaign

**Example:** `CharacterIsLocalCampaign()`

**Arguments:** `DAT_1173e900`

**Description:**  
Does the character belong to the player faction?



## CharacterMPPercentageRemaining

**Example:** `CharacterMPPercentageRemaining() < 50`

**Arguments:** `DAT_1178eec8`

**Description:**  
Returns the percentage of movement points remaining as in integer value



## CharacterMinisterialPosition

**Example:** `CharacterMinisterialPosition(\"governor_europe\")`

**Arguments:** `Ministerial position`

**Description:**  
Does the character hold the specified ministerial position?



## CharacterNumberOfChildren

**Example:** `CharacterNumberOfChildren()`

**Arguments:** `DAT_1178eec8`

**Description:**  
How many children does this character have?



## CharacterOlderThan

**Example:** `CharacterOlderThan(16)`

**Arguments:** `DAT_117aab60`

**Description:**  
Returns whether the character is older than the given age



## CharacterRallied

**Example:** `CharacterRallied()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Did the general rally at least one unit?



## CharacterRank

**Example:** `CharacterRank()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Rank of character (1-6)



## CharacterRouted

**Example:** `CharacterRouted()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Has the character routed? in the last battle?



## CharacterRunsSpyNetwork

**Example:** `CharacterRunsSpyNetwork()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Test to see if the character runs a spy network



## CharacterSpouseHasTrait

**Example:** `CharacterSpouseHasTrait(\"drunkard\")`

**Arguments:** `The name of the trait`

**Description:**  
Does this character\'s spouse have the given trait?



## CharacterStationaryForOneTurn

**Example:** `CharacterStationaryForOneTurn()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Was the character stationary last turn (or longer)



## CharacterSurname

**Example:** `CharacterSurname(\"names_name_names_irishBlair\")`

**Arguments:** `The surname\'s db key`

**Description:**  
Does the character have this surname?



## CharacterTrait

**Example:** `CharacterTrait(\"drunkard\") > 2`

**Arguments:** `Trait name`

**Description:**  
Returns the value of the specified trait (0 if not present)



## CharacterTurnsAtHome

**Example:** `CharacterTurnsAtHome()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Returns the number of turns in home regions exclusively



## CharacterTurnsAtSea

**Example:** `CharacterTurnsAtSea()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Returns the number of turns at sea exclusively



## CharacterTurnsInEnemyLands

**Example:** `CharacterTurnsInEnemyLands()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Returns the number of turns in enemy regions exclusively



## CharacterType

**Example:** `CharacterType(\"spy\")`

**Arguments:** `Valid entry from \'key\' field from Agents table in Empire.mdb`

**Description:**  
Returns true if the character context is of the agent type specified



## CharacterWasAttacker

**Example:** `CharacterWasAttacker()`

**Arguments:** `DAT_1173e900`

**Description:**  
Was the character the attacker in the last battle?



## CharacterWifeHasTrait

**Example:** `CharacterWifeHasTrait(\"drunkard\")`

**Arguments:** `The name of the trait`

**Description:**  
Does this character\'s wife have the given trait?



## CharacterWithdrewFromBattle

**Example:** `CharacterWithdrewFromBattle()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Did the characters army withdraw from battle?



## CharacterWonBattle

**Example:** `CharacterWonBattle()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Is the character part of the winning alliance in a battle



## CharacterWonDuel

**Example:** `CharacterWonDuel()`

**Arguments:** `DAT_1173e900`

**Description:**  
Did the given character win the Duel?



## CharactersUnitRallied

**Example:** `CharactersUnitRallied()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Did the generals unit rally?



## CommanderAncillary

**Example:** `CommanderAncillary(\"Ancillary_Boxer\")`

**Arguments:** `Ancillary name`

**Description:**  
Returns whether the commander has the specified ancillary



## CommanderFoughtInBattle

**Example:** `CommanderFoughtInBattle()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Did the characters unit fight in the battle? (melee or missile)



## CommanderFoughtInMelee

**Example:** `CommanderFoughtInMelee()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Did the characters unit engage in melee in the battle?



## CommanderTrait

**Example:** `CommanderTrait(\"C_General_Mad\") > 2`

**Arguments:** `Trait name`

**Description:**  
Returns the value of the specified trait (0 if not present)



## DateAndWeekInRange

**Example:** `DateAndWeekInRange(0, 1066, 47, 2001)`

**Arguments:** `Start Week, Start Year, End Week, End Year (Inclusive)`

**Description:**  
Test to see if the current calendar year and week in year is within the years and weeks specified.  Week should be 0 <= week < 48.  start <= current <= end



## DateInRange

**Example:** `DateInRange(1066, 2001)`

**Arguments:** `Start Year, End Year (Inclusive)`

**Description:**  
Test to see if the current calendar year is within the years specified.  start <= current <= end



## DefensiveSiegesFought

**Example:** `DefensiveSiegesFought()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the number of siege defences a general has attempted



## DefensiveSiegesWon

**Example:** `DefensiveSiegesWon()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the number of siege defences a general has won



## DifficultyLevel

**Example:** `DifficultyLevel()`

**Arguments:** `DAT_1173e900`

**Description:**  
What is the local faction\'s difficulty level?



## EnemyArmyGreaterCombatStrength

**Example:** `EnemyArmyGreaterCombatStrength()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Is the enemies army stronger than ours?



## FactionAllyCount

**Example:** `FactionAllyCount() > 2`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the number of allies the characters faction has



## FactionBuildingExists

**Example:** `FactionBuildingExists(\"britain\", \"admiralty\")`

**Arguments:** `Parameter 1: A valid key from the factions table.  Parameter 2: A valid key from the building_levels table.`

**Description:**  
Does the specified faction have at least one of the specified building



## FactionBuildingUnderConstruction

**Example:** `FactionBuildingUnderConstruction(\"tut_chosokabe\", \"SHO_Farming_1_Rice_Paddies\", \"jap_tut_tosa\")`

**Arguments:** `Parameter 1: A valid key from the factions table.  Parameter 2: A valid key from the building_levels table.  Parameter 3: A valid key from the regions table or the empty string.`

**Description:**  
Does the specified faction have at least one of the specified building under construction



## FactionCanBuildBuilding

**Example:** `FactionCanBuildBuilding(\"admiralty\")`

**Arguments:** `The building key from the building levels table`

**Description:**  
Can the faction build the specified building at this point



## FactionCashFlow

**Example:** `FactionCashFlow() > 10`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the percentage surplus/loss of the factions regular income and expenditure



## FactionDestroyedByCharacterFaction

**Example:** `FactionDestroyedByCharacterFaction()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Did this characters faction destroy another faction this turn?



## FactionExists

**Example:** `FactionExists(\"britain\")`

**Arguments:** `The db record for the faction`

**Description:**  
Does the given faction exist?



## FactionGovernmentType

**Example:** `FactionGovernmentType(\"gov_republic\")`

**Arguments:** `The government key from the government_types table`

**Description:**  
Is the faction\'s government type equal to the passed government type



## FactionHasAllies

**Example:** `FactionHasAllies()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns whether or not the characters faction has any allies



## FactionHasRecruitedAnyAgents

**Example:** `FactionHasRecruitedAnyAgents()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Checks whether a faction has ever recruited any agents



## FactionHasTradeShipNotInTradeNode

**Example:** `FactionHasTradeShipNotInTradeNode()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Does the faction in context have a trade ship that is not in a trade node. Requires faction context



## FactionIsAlliedCampaign

**Example:** `FactionIsAlliedCampaign()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Is the faction allied to the player faction?



## FactionIsEnemyCampaign

**Example:** `FactionIsEnemy(\"france\")`

**Arguments:** `Faction to query`

**Description:**  
Is the specified faction at war with the player faction?



## FactionIsHuman

**Example:** `FactionIsHuman()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the faction human?



## FactionIsLocal

**Example:** `FactionIsLocal()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the faction the local faction?



## FactionKeyIsLocal

**Example:** `FactionKeyIsLocal()`

**Arguments:** `Faction key`

**Description:**  
Is the faction the local player (and human)?



## FactionLeadersAttribute

**Example:** `FactionLeadersAttribute(\"management\")`

**Arguments:** `The attribute which you wish to check on the factions leader`

**Description:**  
Gets the level of the faction leaders attribute specified as a parameter



## FactionLeadersTrait

**Example:** `FactionLeadersTrait(\"drunkard\") > 2`

**Arguments:** `Trait name`

**Description:**  
Returns the value of the specified trait for the characters faction leader (0 if not present)



## FactionName

**Example:** `FactionName(\"britain\")`

**Arguments:** `The db record for the faction`

**Description:**  
Is the faction the one specified?



## FactionParticipatedInBattle

**Example:** `FactionParticipatedInBattle(\"ita_french_republic\")`

**Arguments:** `Faction key of the faction to be queried`

**Description:**  
Did the specified faction participate in the battle?



## FactionPatrioticFervour

**Example:** `FactionPatrioticFervour()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Does this faction have patriotic fervour?



## FactionSupportCostsPercentage

**Example:** `FactionSupportCostsPercentage()`

**Arguments:** `DAT_1173e900`

**Description:**  
What percentage of the factions expenditure is spent on army upkeep



## FactionTaxLevel

**Example:** `FactionTaxLevel() < TaxLevel(\"extortionate\")`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the average tax level for the faction



## FactionTechExists

**Example:** `FactionTechExists(\"britain\", \"enlightenment_abolition_of_slavery\")`

**Arguments:** `Parameter 1: A valid key from the factions table.  Parameter 2: A valid key from the technologies table.`

**Description:**  
Does the specified faction have the specified technology



## FactionTradeResourceExists

**Example:** `FactionTradeResourceExists(\"res_gold\")`

**Arguments:** `Valid entry from \'key\' field from resources table in Empire.mdb`

**Description:**  
Returns whether the faction has access to the trade resource



## FactionTradeValue

**Example:** `FactionTradeValue() > 1000`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the absolute value of the factions global trade



## FactionTradeValuePercentage

**Example:** `FactionTradeValuePercentage() > 25`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the percentage value of global trade owned by the faction



## FactionTreasury

**Example:** `FactionTreasury() > 100`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the factions treasury value



## FactionTreasuryWorldPercentage

**Example:** `FactionTreasuryWorldPercentage() > 10`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the characters factions treasury value as a percentage of the sum of all factions treasury values



## FactionWarWeariness

**Example:** `FactionWarWeariness()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Does this faction have war weariness?



## FactionwideAncillaryTypeExists

**Example:** `FactionwideAncillaryTypeExists(\"unkillable_cat\") == true`

**Arguments:** `Ancillary name`

**Description:**  
Returns whether the named ancillary exists in the faction somewhere



## ForcesComposedOf

**Example:** `ForcesComposedOf()`

**Arguments:** `A single string of semi-colon separated unit keys`

**Description:**  
Returns whether the two commanded forces combined match the list of unit keys provided



## GarrisonIsLocal

**Example:** `GarrisonIsLocal()`

**Arguments:** `DAT_1173e900`

**Description:**  
Does the garrison belong to the player faction?



## GarrisonUnitCount

**Example:** `GarrisonUnitCount()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the number of units in the garrison context



## GovernorTaxLevel

**Example:** `GovernorTaxLevel() >= 90`

**Arguments:** `DAT_1173e900`

**Description:**  
If the character is the governor returns the tax level set for that governorship.  Returns -1 if not.



## GovernorshipEquals

**Example:** `GovernorshipEquals(\"europe\")`

**Arguments:** `Key of the governorship to be queried `

**Description:**  
Does the context\'s governorship key match the parameter



## GovernorshipTaxLevel

**Example:** `GovernorshipTaxLevel(\"europe\")`

**Arguments:** `Valid entry from \'governorship\' field from governorships table in Empire.mdb`

**Description:**  
Returns the governorships tax level



## GovernorshipsTaxLevel

**Example:** `GovernorshipsTaxLevel() >= 90`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the current tax level for this govenorship



## HasUnspecialisedPort

**Example:** `HasUnspecialisedPort()`

**Arguments:** `DAT_1173e900`

**Description:**  
Does the region have a port with no building?



## InPort

**Example:** `InPort()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character in a port?



## InSettlement

**Example:** `InSettlement()`

**Arguments:** `DAT_1173e900`

**Description:**  
Checks that a character is in a settlement



## InsurrectionCrushed

**Example:** `InsurrectionCrushed()`

**Arguments:** `DAT_1173e900`

**Description:**  
Has the characters faction put down a rebellion in this turn (or the turn that is just ending)



## IsAdmiral

**Example:** `IsAdmiral()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character an admiral?



## IsBesieging

**Example:** `IsBesieging()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character besieging?



## IsBlockading

**Example:** `IsBlockading()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character blockading?



## IsBuildingInChain

**Example:** `IsBuildingInChain(\"army-admin\")`

**Arguments:** `The key of the building chain you are querying from the building_chains table`

**Description:**  
Is garrison residence\'s building (all slots and fortifications for settlements) in the building chain specified by the parameter?



## IsBuildingOfType

**Example:** `IsBuildingOfType(\"admiralty\")`

**Arguments:** `The key of the building level you are querying from the building_levels table`

**Description:**  
Is garrison residence\'s building type (all slots and fortifications for settlements) equal to the parameter?



## IsCarryingTroops

**Example:** `IsCarryingTroops()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character transporting an army?



## IsChildOf

**Example:** `IsChildOf(\"tax_slider\")`

**Arguments:** `Component id`

**Description:**  
Returns true if the components parent, (or parent\'s parent, or parent\'s parent\'s parent etc) has the id specified 



## IsColony

**Example:** `IsColony()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the region a colony



## IsComponentType

**Example:** `IsComponentType(\"government_screens\")`

**Arguments:** `Component id`

**Description:**  
Returns true if the event was fired by the component named



## IsFactionBesiegingSettlement

**Example:** `IsFactionBesiegingSettlement(\"settlement:region:settlement_id\")`

**Arguments:** `Settlement key`

**Description:**  
Is the context faction besieging the specified settlement? Intended for use with faction start of turn event.



## IsFactionLeader

**Example:** `IsFactionLeader()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character the faction leader?



## IsFactionLeaderFemale

**Example:** `IsFactionLeaderFemale()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is this character the faction leader and are they female? (Queen)



## IsFamilyMember

**Example:** `IsFamilyMember()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character a family member?



## IsGarrisoned

**Example:** `IsGarrisoned()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is garrison residence garrisoned?



## IsHomeRegion

**Example:** `IsHomeRegion()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is this region the home region of the owning faction



## IsMessageType

**Example:** `IsMessageType(\"unit_routs_in_battle\")`

**Arguments:** `Message id`

**Description:**  
Returns true if the event that triggered the condition check was for the message named



## IsMultiplayer

**Example:** `IsMultiplayer()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Returns true when in multiplayer campaign



## IsNightBattle

**Example:** `IsNightBattle()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Was the battle a night battle



## IsPlayerTurn

**Example:** `IsPlayerTurn()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Is this the players turn?



## IsPortGarrisoned

**Example:** `IsPortGarrisoned()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the port garrisoned by a navy?



## IsTheatreGovernor

**Example:** `IsTheatreGovernor()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns whether the character is a governor



## IsTriggerableHistoricalEvent

**Example:** `IsTriggerableHistoricalEvent(\"3_colour_printing\")`

**Arguments:** `Historical event record key`

**Description:**  
DAT_1173dad0



## IsUnderBlockade

**Example:** `IsUnderBlockade()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character under blockade?



## IsUnderSiege

**Example:** `IsUnderSiege()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the character under siege?



## LosingMoney

**Example:** `LosingMoney()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns whether or not the factions regular expenditure exceeds their regular income



## MapPosition

**Example:** `MapPosition(x, y)`

**Arguments:** `Location on the map`

**Description:**  
check to see if a map location matches the one return by the context



## MapPositionNear

**Example:** `MapPositionNear(x, y, distance)`

**Arguments:** `Location on the map`

**Description:**  
check to see if a map location is near the one returned by the context



## NoActionThisTurn

**Example:** `NoActionThisTurn()`

**Arguments:** `DAT_1173e900`

**Description:**  
Has an action occured this turn for this character?



## OffensiveSiegesFought

**Example:** `OffensiveSiegesFought()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the number of siege offences a general has attempted



## OffensiveSiegesWon

**Example:** `OffensiveSiegesWon()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the number of siege offences a general has won



## OnAWarFooting

**Example:** `OnAWarFooting()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns whether or not the characters faction is at war with anyone



## ParentId

**Example:** `ParentId(\"tax_slider\")`

**Arguments:** `Component id`

**Description:**  
Returns true if the name of the Components parent matches the id specified



## PercentageUnspentIncome

**Example:** `PercentageUnspentIncome()`

**Arguments:** `DAT_1178eec8`

**Description:**  
What percentage of the characters factions income remains unspent?



## PlayerFactionIsAttacker

**Example:** `PlayerFactionIsAttacker()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the attackers faction the local faction?



## PortBlockaded

**Example:** `PortBlockaded()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the port blockaded, and did it start in the last round?



## PortBlockadedLocal

**Example:** `PortBlockadedLocal()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the port blockaded by the local faction, and did it start in the last round?



## RandomPercentCampaign

**Example:** `RandomPercentCampaign(50)`

**Arguments:** `Number between 0 and 100 to test against`

**Description:**  
Returns true parameter-value-percent of the time



## RegionBuildableSlotEmpty

**Example:** `RegionBuildableSlotEmpty()`

**Arguments:** `DAT_1173e900`

**Description:**  
Has the slot not been developed?



## RegionBuildingFinished

**Example:** `RegionBuildingFinished()`

**Arguments:** `DAT_1173e900`

**Description:**  
Gets the key of the last building constructed in the region



## RegionClamoursReform

**Example:** `RegionClamoursReform()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the population in this region clamouring for reform



## RegionCultureIsFactionCulture

**Example:** `RegionCultureIsFactionCulture()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the region\'s originating culture the same as the owning factions culture



## RegionDemands

**Example:** `RegionDemands()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the population in this region writing letters of demand



## RegionEconomicGrowthLow

**Example:** `RegionEconomicGrowthLow()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is this regions economic growth low?



## RegionGovernorAttribute

**Example:** `RegionGovernorAttribute(\"management\")`

**Arguments:** `The attribute which you wish to check on the regions governor`

**Description:**  
Gets the level of the regions governers attribute specified as a parameter



## RegionIsLocal

**Example:** `RegionIsLocal()`

**Arguments:** `DAT_1173e900`

**Description:**  
Does the region belong to the player faction?



## RegionIsRebelling

**Example:** `RegionIsRebelling(\"ita_alpes_maritimes\")`

**Arguments:** `Key of the region to query`

**Description:**  
Is the specified region rebelling. Requires faction context.



## RegionMajorityReligion

**Example:** `RegionMajorityReligion(\"rel_buddhist\")`

**Arguments:** `religion key from region table`

**Description:**  
Returns whether the region context\'s religion with largest percentage matches the specified religion



## RegionName

**Example:** `RegionName(\"jap_owari\")`

**Arguments:** `The db record for the region`

**Description:**  
Is the region the one specified?



## RegionPopulationLow

**Example:** `RegionPopulationLow()`

**Arguments:** `DAT_1173e900`

**Description:**  
Tests if the population of a region is has dropped below the previous town spawn threshold e.g. region has 5 towns but has dropped below the population requirement for 4 towns



## RegionPopulationMaxReached

**Example:** `RegionPopulationMaxReached()`

**Arguments:** `DAT_1173e900`

**Description:**  
Tests if the population of a region the maximum population



## RegionRebels

**Example:** `RegionRebels()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the region rebelling



## RegionReligionIsStateReligion

**Example:** `RegionReligionIsStateReligion()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the region\'s religion the same as the owning factions religion



## RegionResourceExists

**Example:** `RegionResourceExists(\"res_gold\")`

**Arguments:** `Valid entry from \'key\' field from resources table in Empire.mdb`

**Description:**  
Returns whether the resource exists in the region



## RegionResourceExploited

**Example:** `RegionResourceExploited(\"res_gold\")`

**Arguments:** `Valid entry from \'key\' field from resources table in Empire.mdb`

**Description:**  
Returns whether the resource is produced in the region



## RegionRiots

**Example:** `RegionRiots()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the population in this region rioting



## RegionSlotBuildingCount

**Example:** `RegionSlotBuildingCount()`

**Arguments:** `DAT_1173e900`

**Description:**  
Counts the number of buildings in the region slots in the region



## RegionSlotBuildingCultureExists

**Example:** `RegionSlotBuildingCultureExists(\"european\")`

**Arguments:** `The key of the culture from the cultures table`

**Description:**  
Tests if the region has a building from the given culture



## RegionSlotBuildingTypeCount

**Example:** `RegionSlotBuildingTypeCount(\"barracks\")`

**Arguments:** `The key of the building level you are querying from the building_levels table`

**Description:**  
Counts the number of buildings in the region slots in the region of the specified type



## RegionSlotBuildingTypeExists

**Example:** `RegionSlotBuildingTypeExists(\"barracks\")`

**Arguments:** `The key of the building level you are querying from the building_levels table`

**Description:**  
Tests if a building of the specified type exists in the region



## RegionSlotCount

**Example:** `RegionSlotCount()`

**Arguments:** `DAT_1173e900`

**Description:**  
Counts the number of slots in a region including settlement slots



## RegionSlotEmptyCount

**Example:** `RegionSlotEmptyCount()`

**Arguments:** `DAT_1173e900`

**Description:**  
Counts the number of empty (no building) slots in a region including settlement slots



## RegionSlotTypeExists

**Example:** `RegionSlotTypeExists(\"fish\")`

**Arguments:** `The key of the slot type you wish to find from the slots table`

**Description:**  
Tests to see if the region has a slot (in any status) whose type matches the parameter



## RegionTaxExempt

**Example:** `RegionTaxExempt()`

**Arguments:** `DAT_117af218`

**Description:**  
Gets whether the region is tax exempt or not



## RegionTaxLevel

**Example:** `RegionTaxLevel()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the regions tax level



## RegionTaxTownWealthGrowthReduction

**Example:** `RegionTaxTownWealthGrowthReduction() > 1`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the percentage of the regions town wealth growth lost due to taxes



## RegionTownWealthGrowth

**Example:** `RegionTownWealthGrowth() > 50`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns the town wealth growth of the region



## RegionWealthDecrease

**Example:** `RegionWealthDecrease()`

**Arguments:** `DAT_1173e900`

**Description:**  
How much has the regions wealth decreased?



## RegionWealthIncrease

**Example:** `RegionWealthIncrease()`

**Arguments:** `DAT_1173e900`

**Description:**  
How much has the regions wealth increased?



## RegionWouldBeHappyWithNoTaxExemption

**Example:** `RegionWouldBeHappyWithNoTaxExemption()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Checks whether the region happiness would be zero or greater if it was not exempt from tax



## ResearchCategory

**Example:** `ResearchCategory(\"enlightenment\")`

**Arguments:** `Category`

**Description:**  
Is the research just completed of this category?



## ResearchQueueIdle

**Example:** `ResearchQueueIdle()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is faction not researching any tech evn though they could be



## ResearchType

**Example:** `ResearchType(\"military_navy_flintlock_cannon\")`

**Arguments:** `Research type`

**Description:**  
Is the technology just researched of this type?



## ResearchTypeUniqueToFaction

**Example:** `ResearchTypeUniqueToFaction()`

**Arguments:** `Research type`

**Description:**  
Are we the first faction to research this technology type?



## SeaTradeRouteRaided

**Example:** `SeaTradeRouteRaided()`

**Arguments:** `DAT_1173e900`

**Description:**  
Was one of this factions sea trade routes has been raided in the last round?



## SettlementBuildingQueueIdleDespiteCash

**Example:** `SettlementBuildingQueueIdleDespiteCash()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the settlement\'s building queue empty even though the faction can afford to build the cheapest building in any of its slot?



## SettlementFortificationsBuildingQueueIdleDespiteCash

**Example:** `SettlementFortificationsBuildingQueueIdleDespiteCash()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the settlements\'s fortification building queue empty even though the faction can afford to build the cheapest building?



## SettlementIsLocal

**Example:** `SettlementIsLocal()`

**Arguments:** `DAT_1173e900`

**Description:**  
Does the settlement belong to the player faction?



## SettlementName

**Example:** `SettlementName(\"settlement:acadia:fort_nashwaak\")`

**Arguments:** `The unique id of the settlement from the campaign_map_settlements table or a character, in which case it looks at the settlement the character is in`

**Description:**  
Is the settlement\'s unique id equal to the parameter?



## SlotBuildingQueueIdleDespiteCash

**Example:** `SlotBuildingQueueIdleDespiteCash()`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the slot\'s building queue empty even though the faction can afford to build the cheapest building?



## SlotIsAlliedCampaign

**Example:** `SlotIsAlliedCampaign()`

**Arguments:** `DAT_1173e900`

**Description:**  
Does the slot belong to a faction allied to the player faction?



## SlotIsLocal

**Example:** `SlotIsLocal()`

**Arguments:** `DAT_1173e900`

**Description:**  
Does the slot belong to the player faction?



## SlotName

**Example:** `SlotName(\"port:england:portsmouth\")`

**Arguments:** `The name of the slot to check for`

**Description:**  
Returns if the passed slot name is equal to the slot\'s name



## SlotSuperchain

**Example:** `SlotType(\"wheat\")`

**Arguments:** `The slot superchain type (key from the building superchains table)`

**Description:**  
Is the slot\'s superchain from the building superchains table equal to the parameter?



## SlotType

**Example:** `SlotType(\"wheat\")`

**Arguments:** `The slot type (key from the slots table)`

**Description:**  
Is the slot\'s type from the slots table equal to the parameter?



## SupportCostsPercentage

**Example:** `SupportCostsPercentage()`

**Arguments:** `DAT_1173e900`

**Description:**  
The percentage of outgoings used for upkeep in the recent turns for the given faction



## TargetArmyGreaterCombatStrength

**Example:** `TargetArmyGreaterCombatStrength()`

**Arguments:** `DAT_1178eec8`

**Description:**  
The does the target army have greater combat strength than the character?



## TargetCharacterIsAlliedCampaign

**Example:** `TargetCharacterIsAlliedCampaign()`

**Arguments:** `DAT_1178eec8`

**Description:**  
The target character is allied to the character?



## TargetCharacterIsEnemyCampaign

**Example:** `TargetCharacterIsEnemyCampaign()`

**Arguments:** `DAT_1178eec8`

**Description:**  
The target character is an enemy of the character?



## TargetInStrikingRangeOfEnemy

**Example:** `CharacterIsEnemy()`

**Arguments:** `DAT_1178eec8`

**Description:**  
The character is an enemy of the local faction?



## TaxCollectionLimited

**Example:** `TaxCollectionLimited()`

**Arguments:** `DAT_1173e900`

**Description:**  
Are all the factions government building at the maximum level (and thus impossible to upgrade)?



## TaxLevel

**Example:** `FactionTaxLevel() < TaxLevel(\"extortionate\")`

**Arguments:** `Valid entry from \'key\' field from taxes_levels table in Empire.mdb`

**Description:**  
Returns the tax level for the given tax key



## TradeNodeAvailableWorldwide

**Example:** `TradeNodeAvailableWorldwide()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Is there an unoccupied trade node (worldwide). Requires faction context



## TradePortsAtMaxLevel

**Example:** `TradePortsAtMaxLevel()`

**Arguments:** `DAT_1173e900`

**Description:**  
Are all of the regions trade ports at the maximum level (and thus impossible to upgrade)?



## TradeRouteIsEnemy

**Example:** `TradeRouteIsEnemy()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Returns whether the trade route attacked is used by an enemy of the local faction



## TradeRouteIsLocal

**Example:** `TradeRouteIsLocal()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Returns whether the trade route attacked is used by the local faction



## TradeRouteLimitReached

**Example:** `TradeRouteLimitReached()`

**Arguments:** `DAT_1173e900`

**Description:**  
Has the faction reached its limit of trade routes?



## TurnNumber

**Example:** `TurnNumber()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Returns the number of the turn currently being taken, starting at 1



## TurnsSinceThreadLastAdvanced

**Example:** `TurnsSinceThreadLastAdvanced(\"0001_Battle_Advice_Friendly_Fire_Thread\")`

**Arguments:** `Key from advice_threads table`

**Description:**  
The number of turns since the advice thread was last advanced - 0 signifies that the thread is unadvanced or the number of turns cannot be established



## UnitCategory

**Example:** `UnitCategory(\"naval_frigate\")`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the unit of this category type?



## UnitClass

**Example:** `UnitClass(\"cavalry_missile\")`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the unit of this class?



## UnitCrushedInsurrection

**Example:** `UnitCrushedInsurrection()`

**Arguments:** `DAT_1173e900`

**Description:**  
Did the given unit crush an insurrection in the last turn?



## UnitCultureType

**Example:** `UnitCultureType(\"tribal\")`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the unit of this culture type?



## UnitFoughtInBattle

**Example:** `UnitFoughtInBattle()`

**Arguments:** `DAT_1173e900`

**Description:**  
Did the unit fight in the last battle?



## UnitFoughtInMelee

**Example:** `UnitFoughtInMelee()`

**Arguments:** `DAT_1173e900`

**Description:**  
Did the unit melee fight in the last battle?



## UnitInTheatre

**Example:** `UnitInTheatre(\"-1133129049\")`

**Arguments:** `DAT_1173e900`

**Description:**  
Is this unit within the specified theatre?



## UnitOnContinent

**Example:** `UnitOnContinent(\"cont_africa_south\")`

**Arguments:** `DAT_1173e900`

**Description:**  
Is the given unit on the specified continent?



## UnitRouted

**Example:** `UnitRouted()`

**Arguments:** `DAT_1173e900`

**Description:**  
Did the given unit rout?



## UnitSufferedCasualties

**Example:** `UnitSufferedCasualties()`

**Arguments:** `DAT_1173e900`

**Description:**  
What percentage of casualties did this unit suffer?



## UnitTrait

**Example:** `UnitTrait(\"U_Infected_Dysentry\") > 2`

**Arguments:** `Trait name`

**Description:**  
Returns the value of the specified trait (0 if not present)



## UnitType

**Example:** `UnitType(\"euro_line_infantry\")`

**Arguments:** `The unit key from the units table`

**Description:**  
Is the unit\'s unit record key equal to the parameter?



## UnitWonBattle

**Example:** `UnitWonBattle()`

**Arguments:** `DAT_1178eec8`

**Description:**  
Is the unit part of the winning alliance in a battle?



## UnusedInternationalTradeRoute

**Example:** `UnusedInternationalTradeRoute()`

**Arguments:** `DAT_1173e900`

**Description:**  
Could the faction establish a new international trade route?



## WarEndedCharacterFaction

**Example:** `WarEndedCharacterFaction()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Was peace declared between this faction and another faction this turn?



## WarStartedCharacterFaction

**Example:** `WarStartedCharacterFaction()`

**Arguments:** `DAT_1173dad0`

**Description:**  
Did a war start between this faction and another faction this turn?



## WorldResourceExists

**Example:** `WorldResourceExists(\"res_gold\")`

**Arguments:** `Valid entry from \'key\' field from resources table in Empire.mdb`

**Description:**  
Returns whether the resource exists anywhere



## WorldResourceExploited

**Example:** `WorldResourceExploited(\"res_gold\")`

**Arguments:** `Valid entry from \'key\' field from resources table in Empire.mdb`

**Description:**  
Returns whether the resource is produced by any faction



## WorldwideAncillaryTypeExists

**Example:** `WorldwideAncillaryTypeExists(\"unkillable_cat\") == true`

**Arguments:** `Ancillary name`

**Description:**  
Returns whether the named ancillary exists in the world somewhere



## is_advice_audio_playing

**Example:** `is_advice_audio_playing()`

**Arguments:** `DAT_1173e900`

**Description:**  
Returns whether audio for any advice is currently playing

