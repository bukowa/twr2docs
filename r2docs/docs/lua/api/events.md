---
title: events
summary: A brief description of my document.
---

# Events
Not all conditions are documented.  
Not all conditions are expected to work.  

Below list is result of extracting the game decompiled code.  
You should not rely 100% on the below list, as it may contain errors or missing conditions.

## AdviceFinishedTrigger

**Code:** `ADVICE_FINISHED_EVENT`  

**Context:** `Sound`  


**Description:**  
Notify scripters when current advice has finished playing

**Author:** `DAT_117afd64`

## AreaCameraEntered

**Code:** `AREA_TRIGGER_CAMERA_ENTER_EVENT`  

**Context:** `UniString trigger name`  


**Description:**  
Fired when the camera enters an area trigger

**Author:** `DAT_1179b680`

## AreaCameraExited

**Code:** `AREA_TRIGGER_CAMERA_EXIT_EVENT`  

**Context:** `UniString trigger name`  


**Description:**  
Fired when the camera exits an area trigger

**Author:** `DAT_1179b680`

## AreaEntered

**Code:** `AREA_TRIGGER_ENTER_EVENT`  

**Context:** `UniString trigger name, CHARACTER character who entered`  


**Description:**  
Fired when a piece enters an area trigger

**Author:** `DAT_1179b680`

## AreaExited

**Code:** `AREA_TRIGGER_EXIT_EVENT`  

**Context:** `UniString trigger name, CHARACTER character who exited`  


**Description:**  
Fired when a piece exits an area trigger

**Author:** `DAT_1179b680`

## BattleBoardingActionCommenced

**Code:** `BATTLE_BOARDING_ACTION_COMMENCED`  

**Context:** `Battle`  


**Description:**  
Fired each time a ship commences the boarding of an enemy vessel

**Author:** `Ingimar`

## BattleBoardingShip

**Code:** `BATTLE_BOARDING_SHIP`  

**Context:** `Battle`  


**Description:**  
Gets triggered when the order to board a ship is issued

**Author:** `Ingimar`

## BattleCommandingShipRouts

**Code:** `BATTLE_COMMANDING_SHIP_ROUTS`  

**Context:** `Naval Battle`  


**Description:**  
The ship containing the fleet admiral has just routed

**Author:** `Ingimar`

## BattleCommandingUnitRouts

**Code:** `BATTLE_COMMANDING_UNIT_ROUTS`  

**Context:** `Land Battle`  


**Description:**  
Fires off an event for when a unit that has a commanding general attached to it routs

**Author:** `Ingimar`

## BattleCompleted

**Code:** `BATTLE_COMPLETED`  

**Context:** `Campaign model`  


**Description:**  
A battle has been completed on the campaign map

**Author:** `DAT_117a1590`

## BattleConflictPhaseCommenced

**Code:** `BATTLE_CONFLICT_PHASE_COMMENCED`  

**Context:** `Battle`  


**Description:**  
Fired once at the start of conflict

**Author:** `Ingimar`

## BattleDeploymentPhaseCommenced

**Code:** `BATTLE_DEPLOYMENT_PHASE_COMMENCED`  

**Context:** `Battle`  


**Description:**  
Fired once at the start of deployment

**Author:** `Ingimar`

## BattleFortPlazaCaptureCommenced

**Code:** `BATTLE_FORT_PLAZA_CAPTURE_COMMENCED`  

**Context:** `Battle`  


**Description:**  
Fired each time an attacking unit starts capturing the capture location inside a fort

**Author:** `Ingimar`

## BattleShipAttacksEnemyShip

**Code:** `BATTLE_SHIP_ATTACKS_ENEMY_SHIP`  

**Context:** `Battle`  


**Description:**  
Gets fired off for every attack order executed by a ship

**Author:** `Ingimar`

## BattleShipCaughtFire

**Code:** `BATTLE_SHIP_CAUGHT_FIRE`  

**Context:** `Battle`  


**Description:**  
A ship just caught fire

**Author:** `Ingimar`

## BattleShipMagazineExplosion

**Code:** `BATTLE_SHIP_MAGAZINE_EXPLOSION`  

**Context:** `Battle`  


**Description:**  
Fired off when a ship explodes

**Author:** `Ingimar`

## BattleShipRouts

**Code:** `BATTLE_SHIP_ROUTS`  

**Context:** `Naval Battle`  


**Description:**  
Fires off whenever a ship enters the rout state of morale

**Author:** `Ingimar`

## BattleShipRunAground

**Code:** `BATTLE_SHIP_RUN_AGROUND`  

**Context:** `Naval Battle`  


**Description:**  
Fired off when a ship collides with the terrain

**Author:** `Ingimar`

## BattleShipSailingIntoWind

**Code:** `BATTLE_SHIP_SAILING_INTO_WIND`  

**Context:** `Naval Battle`  


**Description:**  
Fired off when a ship is sailing approximately into the wind

**Author:** `Ingimar`

## BattleShipSurrendered

**Code:** `BATTLE_SHIP_SURRENDERED`  

**Context:** `Naval Battle`  


**Description:**  
Fired off when a ship surrenders

**Author:** `Ingimar`

## BattleUnitAttacksBuilding

**Code:** `BATTLE_UNIT_ATTACKS_BUILDING`  

**Context:** `Battle`  


**Description:**  
Gets fired off for every attack order executed by a unit

**Author:** `Ingimar`

## BattleUnitAttacksEnemyUnit

**Code:** `BATTLE_UNIT_ATTACKS_ENEMY_UNIT`  

**Context:** `Battle`  


**Description:**  
Gets fired off for every attack order executed by a unit

**Author:** `Ingimar`

## BattleUnitAttacksWalls

**Code:** `BATTLE_UNIT_ATTACKS_WALLS`  

**Context:** `Battle`  


**Description:**  
Gets fired off for every attack order executed by a unit when attacking a fort building

**Author:** `Ingimar`

## BattleUnitCapturesBuilding

**Code:** `BATTLE_UNIT_CAPTURES_BUILDING`  

**Context:** `Battle`  


**Description:**  
Gets fired each time a building has a new alliance as an owner, initiated by a unit

**Author:** `Ingimar`

## BattleUnitDestroysBuilding

**Code:** `BATTLE_UNIT_DESTROYS_BUILDING`  

**Context:** `Battle`  


**Description:**  
Gets fired each time a building gets destroyed by a unit

**Author:** `Ingimar`

## BattleUnitRouts

**Code:** `BATTLE_UNIT_ROUTS`  

**Context:** `Land Battle`  


**Description:**  
Fires off an event for when a unit enters rout.

**Author:** `Ingimar`

## BattleUnitUsingWall

**Code:** `BATTLE_UNIT_USING_WALL`  

**Context:** `Battle`  


**Description:**  
Fires off when a unit attaches itself to a wall

**Author:** `Ingimar`

## BuildingCardSelected

**Code:** `BUILDING_CARD_SELECTED`  

**Context:** `String (building record key)`  


**Description:**  
Fires when a building card is clicked on on the hud

**Author:** `DAT_117a2ecc`

## BuildingCompleted

**Code:** `BUILDING_COMPLETED_EVENT`  

**Context:** `Building level record`  


**Description:**  
A building has been completed

**Author:** `DAT_1179b680`

## BuildingConstructionIssuedByPlayer

**Code:** `BUILDING_CONSTRUCTION_ISSUED_BY_PLAYER`  

**Context:** `building level`  


**Description:**  
Fired when the player adds a building to the queue

**Author:** `DAT_117a1590`

## BuildingInfoPanelOpenedCampaign

**Code:** `BUILDING_INFO_PANEL_OPEN_EVENT_CAMPAIGN`  

**Context:** `string`  


**Description:**  
triggers when the building info panel is opened by the user in the campaign game

**Author:** `shane`

## CameraMoverCancelled

**Code:** `CAMERA_MOVER_CANCELLED`  

**Context:** `MAP_LOCATION`  


**Description:**  
When the camera controller is cancelled before completion

**Author:** `DAT_1179b680`

## CameraMoverFinished

**Code:** `CAMERA_MOVER_FINISHED`  

**Context:** `MAP_LOCATION`  


**Description:**  
When the camera reaches the end of its path, or when another camera transition cuts in

**Author:** `DAT_1179ebf0`

## CampaignArmiesMerge

**Code:** `MILITARY_FORCE_MERGE_EVENT`  

**Context:** `Character, character target`  


**Description:**  
Two campaign armies merge

**Author:** `DAT_117a1590`

## CampaignBuildingDamaged

**Code:** `BUILDING_DAMAGED_EVENT`  

**Context:** `Region slot`  


**Description:**  
A building is damaged

**Author:** `DAT_117a1590`

## CampaignCoastalAssaultOnCharacter

**Code:** `CHARACTER_COASTAL_CHARACTER_ASSAULT`  

**Context:** `Character`  


**Description:**  
Fired when a character initiates a coastal assault on a character

**Author:** `DAT_1179b680`

## CampaignCoastalAssaultOnGarrison

**Code:** `CHARACTER_COASTAL_GARRISON_ASSAULT`  

**Context:** `Character`  


**Description:**  
Fired when a character initiates a coastal assault on a garrison

**Author:** `DAT_1179b680`

## CampaignEffectsBundleAwarded

**Code:** `FACTION_AWARDED_EFFECT_BUNDLE`  

**Context:** `Faction`  


**Description:**  
A faction has gained an effect bundle

**Author:** `DAT_1179b680`

## CharacterAttacksAlly

**Code:** `CHARACTER_ATTACKS_ALLY_EVENT`  

**Context:** `Character`  


**Description:**  
A character has attacked an ally

**Author:** `DAT_117a159c`

## CharacterBecomesFactionLeader

**Code:** `CHARACTER_BECOMES_FACTION_LEADER`  

**Context:** `Character`  


**Description:**  
A character has become faction leader

**Author:** `DAT_1179b680`

## CharacterBesiegesSettlement

**Code:** `CHARACTER_BESIEGES_SETTLEMENT`  

**Context:** `Character`  


**Description:**  
Fired when a character besieges a settlement

**Author:** `Chris Budd`

## CharacterBlockadedPort

**Code:** `CHARACTER_BLOCKADED_PORT_EVENT`  

**Context:** `Character`  


**Description:**  
A character successfully blockades a port

**Author:** `DAT_1179b680`

## CharacterBrokePortBlockade

**Code:** `CHARACTER_BROKE_PORT_BLOCKADE_EVENT`  

**Context:** `Character`  


**Description:**  
A character successfully broke a port blockade

**Author:** `DAT_1179b680`

## CharacterBuildingCompleted

**Code:** `CHARACTER_BUILDING_COMPLETED_EVENT`  

**Context:** `Building level record, Character`  


**Description:**  
A building has been completed

**Author:** `DAT_117a159c`

## CharacterCanLiberate

**Code:** `CHARACTER_CAN_LIBERATE_EVENT`  

**Context:** `Character`  


**Description:**  
A character was given the opportunity to liberate a region

**Author:** `DAT_1179b680`

## CharacterCandidateBecomesMinister

**Code:** `CHARACTER_CANDIDATE_BECOMES_MINISER`  

**Context:** `Character`  


**Description:**  
Fired when a candidate becomes a minister

**Author:** `DAT_1179b680`

## CharacterCharacterTargetAction

**Code:** `CHARACTER_CHARACTER_TARGET_ACTION_EVENT`  

**Context:** `Character`  


**Description:**  
A character has performed an agent action against a character

**Author:** `DAT_117a1590`

## CharacterComesOfAge

**Code:** `CHARACTER_COMES_OF_AGE`  

**Context:** `Character`  


**Description:**  
An agent has failed to bribe an enemy army

**Author:** `DAT_1179b680`

## CharacterCompletedBattle

**Code:** `CHARACTER_COMPLETED_BATTLE`  

**Context:** `Character`  


**Description:**  
A character took part in a battle and didn\'t die

**Author:** `DAT_117a1590`

## CharacterCreated

**Code:** `CHARACTER_CREATION`  

**Context:** `Character`  


**Description:**  
Fired when a character is created

**Author:** `DAT_117a2ecc`

## CharacterDeselected

**Code:** `CHARACTER_DESELECTED_EVENT`  

**Context:** `Empty string`  


**Description:**  
triggers when a character has been deselected on the campaign map

**Author:** `Christian`

## CharacterDiscovered

**Code:** `CHARACTER_DISCOVERED`  

**Context:** `Character`  


**Description:**  
Fired when an character is discovered

**Author:** `Chris Budd`

## CharacterDisembarksNavy

**Code:** `CHARACTER_DISEMBARKS_NAVY`  

**Context:** `Character`  


**Description:**  
A character disembarks a navy

**Author:** `DAT_117a1590`

## CharacterEmbarksNavy

**Code:** `CHARACTER_EMBARKS_NAVY`  

**Context:** `Character`  


**Description:**  
A character embarks on a navy

**Author:** `DAT_117a1590`

## CharacterEntersAttritionalArea

**Code:** `CHARACTER_ENTERS_ATTRITIONAL_AREA`  

**Context:** `Character`  


**Description:**  
Fired when a characters ends its movement in a position where it will suffer attrition

**Author:** `DAT_1179b680`

## CharacterEntersGarrison

**Code:** `CHARACTER_ENTERS_GARRISON`  

**Context:** `Garrison, Character`  


**Description:**  
A character enters a garrison (settlement, slot or fort)

**Author:** `DAT_117a1590`

## CharacterFactionCompletesResearch

**Code:** `CHARACTER_FACTION_COMPLETES_RESEARCH`  

**Context:** `Characters faction has research a technology`  


**Description:**  
research completed

**Author:** `Chris Budd`

## CharacterFamilyRelationDied

**Code:** `CHARACTER_FAMILY_RELATION_DIED_EVENT`  

**Context:** `Character`  


**Description:**  
A character\'s immediate family member has died

**Author:** `Chris Budd`

## CharacterGarrisonTargetAction

**Code:** `CHARACTER_GARRISON_TARGET_ACTION_EVENT`  

**Context:** `Character`  


**Description:**  
A character has performed an agent action against a garrison

**Author:** `DAT_117a1590`

## CharacterGeneralDiedInBattle

**Code:** `CHARACTER_GENERAL_DIED_IN_BATTLE`  

**Context:** `Character`  


**Description:**  
A character took part in a battle as a general and died

**Author:** `DAT_117ac470`

## CharacterInfoPanelOpened

**Code:** `CHARACTER_INFO_PANEL_OPENED`  

**Context:** `character, faction`  


**Description:**  
triggers the character information panel has been opened

**Author:** `DAT_117b0390`

## CharacterLeavesGarrison

**Code:** `CHARACTER_LEAVES_GARRISON`  

**Context:** `Garrison, Character`  


**Description:**  
A character leaves a garrison (settlement, slot or fort)

**Author:** `DAT_1179b680`

## CharacterLootedSettlement

**Code:** `CHARACTER_LOOTS_SETTLEMENT`  

**Context:** `Character`  


**Description:**  
A character loots a settlement

**Author:** `DAT_117a1590`

## CharacterMarriage

**Code:** `CHARACTER_MARRIES`  

**Context:** `Character`  


**Description:**  
A character has married

**Author:** `DAT_1179b680`

## CharacterMilitaryForceTraditionPointAllocated

**Code:** `CHARACTER_MILITARY_FORCE_TRADITION_POINT_ALLOCATED`  

**Context:** `Character`  


**Description:**  
Fired when a military force is assigned a tradition point

**Author:** `Chris Budd`

## CharacterParticipatedAsSecondaryGeneralInBattle

**Code:** `CHARACTER_PARTICIPATED_AS_SECONDARY_GENERAL_IN_BATTLE`  

**Context:** `Character`  


**Description:**  
A character took part in a battle as a secondary general and didn\'t die

**Author:** `DAT_117a2ed8`

## CharacterPerformsActionAgainstFriendlyTarget

**Code:** `CHARACTER_PERFORMS_ACTION_AGAINST_FRIENDLY_TARGET`  

**Context:** `Character`  


**Description:**  
Fired when an agent ends turn in a settlement or army

**Author:** `DAT_117a1590`

## CharacterPoliticalAction

**Code:** `CHARACTER_POLITICAL_ACTION`  

**Context:** `Character`  


**Description:**  
Fired when a character performs a political action

**Author:** `Oleg Zlatarski`

## CharacterPoliticalActionPoliticalMariage

**Code:** `CHARACTER_POLITICAL_ACTION_POLITICAL_MARRIAGE`  

**Context:** `Character`  


**Description:**  
Fired when a character is married politically

**Author:** `Chris Budd`

## CharacterPoliticalAdoption

**Code:** `CHARACTER_POLITICAL_ADOPTION`  

**Context:** `Character`  


**Description:**  
Fired when a character is adopted

**Author:** `Chris Budd`

## CharacterPoliticalAssassination

**Code:** `CHARACTER_POLITICAL_ASSASSINATION`  

**Context:** `Character`  


**Description:**  
Fired when a character is assassinated

**Author:** `Oleg Zlatarski`

## CharacterPoliticalBribe

**Code:** `CHARACTER_POLITICAL_BRIBE`  

**Context:** `Character`  


**Description:**  
Fired when a character is bribed

**Author:** `Veli Mollov`

## CharacterPoliticalDivorce

**Code:** `CHARACTER_POLITICAL_DIVORCE`  

**Context:** `Character`  


**Description:**  
Fired when a character is divorced politically

**Author:** `Chris Budd`

## CharacterPoliticalEmbezzleFunds

**Code:** `CHARACTER_POLITICAL_EMBEZZLE_FUNDS`  

**Context:** `Character`  


**Description:**  
Fired when Embezzle Funds political action executed

**Author:** `Veli Mollov`

## CharacterPoliticalEntice

**Code:** `CHARACTER_POLITICAL_ENTICE`  

**Context:** `Character`  


**Description:**  
Fired when Entice political action executed

**Author:** `Veli Mollov`

## CharacterPoliticalFlirt

**Code:** `CHARACTER_POLITICAL_FLIRT`  

**Context:** `Character`  


**Description:**  
Fired when Flirt political action executed

**Author:** `Veli Mollov`

## CharacterPoliticalGatherSupport

**Code:** `CHARACTER_POLITICAL_GATHER_SUPPORT`  

**Context:** `Character`  


**Description:**  
Fired when Gather Support political action executed

**Author:** `Oleg Zlatarski`

## CharacterPoliticalInsult

**Code:** `CHARACTER_POLITICAL_INSULT`  

**Context:** `Character`  


**Description:**  
Fired when Insult political action executed

**Author:** `Veli Mollov`

## CharacterPoliticalOrganizeGames

**Code:** `CHARACTER_POLITICAL_ORGANIZE_GAMES`  

**Context:** `Character`  


**Description:**  
Fired when Organize Games political action executed

**Author:** `Veli Mollov`

## CharacterPoliticalPartyProvoke

**Code:** `CHARACTER_POLITICAL_PARTY_PROVOKE`  

**Context:** `Character`  


**Description:**  
Fired when Party Provoke political action executed

**Author:** `Veli Mollov`

## CharacterPoliticalPartyPurge

**Code:** `CHARACTER_POLITICAL_PARTY_PURGE`  

**Context:** `Character`  


**Description:**  
Fired when Party Purge political action executed

**Author:** `Veli Mollov`

## CharacterPoliticalPartySecureLoyalty

**Code:** `CHARACTER_POLITICAL_PARTY_SECURE_LOYALTY`  

**Context:** `Character`  


**Description:**  
Fired when Party Secure Loyalty political action executed

**Author:** `Veli Mollov`

## CharacterPoliticalPraise

**Code:** `CHARACTER_POLITICAL_PRAISE`  

**Context:** `Character`  


**Description:**  
Fired when Praise political action executed

**Author:** `Veli Mollov`

## CharacterPoliticalPromotion

**Code:** `CHARACTER_POLITICAL_PROMOTION`  

**Context:** `Character`  


**Description:**  
Fired when character secure promoted

**Author:** `Veli Mollov`

## CharacterPoliticalProvoke

**Code:** `CHARACTER_POLITICAL_PROVOKE`  

**Context:** `Character`  


**Description:**  
Fired when Provoke political action executed

**Author:** `Oleg Zlatarski`

## CharacterPoliticalRumours

**Code:** `CHARACTER_POLITICAL_RUMOURS`  

**Context:** `Character`  


**Description:**  
Fired when rumours are spread about a character

**Author:** `Chris Budd`

## CharacterPoliticalSecureLoyalty

**Code:** `CHARACTER_POLITICAL_SECURE_LOYALTY`  

**Context:** `Character`  


**Description:**  
Fired when Insult political action executed

**Author:** `Oleg Zlatarski`

## CharacterPoliticalSendDiplomat

**Code:** `CHARACTER_POLITICAL_SEND_DIPLOMAT`  

**Context:** `Character`  


**Description:**  
Fired when Organize Games political action executed

**Author:** `Veli Mollov`

## CharacterPoliticalSendEmissary

**Code:** `CHARACTER_POLITICAL_SEND_EMISSARY`  

**Context:** `Character`  


**Description:**  
Fired when Send Emissary political action executed

**Author:** `Veli Mollov`

## CharacterPoliticalSendGift

**Code:** `CHARACTER_POLITICAL_SEND_GIFT`  

**Context:** `Character`  


**Description:**  
Fired when Send Gift political action executed

**Author:** `Veli Mollov`

## CharacterPoliticalSuicide

**Code:** `CHARACTER_POLITICAL_SUICIDE`  

**Context:** `Character`  


**Description:**  
Fired when a character suicides

**Author:** `Veli Mollov`

## CharacterPostBattleEnslave

**Code:** `CHARACTER_POSTBATTLE_ENSLAVE_EVENT`  

**Context:** `User is selecting fate of prisoners`  


**Description:**  
Occurs when a user selects to enslave prisoners after a battle

**Author:** `Chris Budd`

## CharacterPostBattleRelease

**Code:** `CHARACTER_POSTBATTLE_RELEASE_EVENT`  

**Context:** `User is selecting fate of prisoners`  


**Description:**  
Occurs when a user selects to release prisoners after a battle

**Author:** `Chris Budd`

## CharacterPostBattleSlaughter

**Code:** `CHARACTER_POSTBATTLE_SLAUGHTER_EVENT`  

**Context:** `User is selecting fate of prisoners`  


**Description:**  
Occurs when a user selects to slaughter prisoners after a battle

**Author:** `Chris Budd`

## CharacterPromoted

**Code:** `CHARACTER_PROMOTED_EVENT`  

**Context:** `Character`  


**Description:**  
A character has been promoted

**Author:** `DAT_117a159c`

## CharacterRankUp

**Code:** `CHARACTER_RANK_UP`  

**Context:** `Character`  


**Description:**  
Fired when a character ranks up

**Author:** `DAT_117a2ed8`

## CharacterRankUpNeedsAncillary

**Code:** `CHARACTER_RANK_UP_NEEDS_ANCILLARY`  

**Context:** `Character`  


**Description:**  
Fired when a character ranks up and needs an ancillary generated

**Author:** `DAT_117a2ed8`

## CharacterRelativeKilled

**Code:** `CHARACTER_RELATIVE_KILLED`  

**Context:** `Character`  


**Description:**  
An agent has failed to bribe an enemy army

**Author:** `DAT_1179b680`

## CharacterSelected

**Code:** `CHARACTER_SELECTED_EVENT`  

**Context:** `Character`  


**Description:**  
Fired when a character is selected

**Author:** `DAT_117a1590`

## CharacterSettlementBesieged
---
WORKS
```
empty context :(
```
**Code:** `SETTLEMENT_BESIEGED`  

**Context:** `Garrison Residence`  


**Description:**  
Fired when a settlement garrisoned by a character is besieged

**Author:** `Chris Budd`

## CharacterSettlementBlockaded
---
WORKS
```
empty context :(
```
**Code:** `SETTLEMENT_BLOCKADED`  

**Context:** `Garrison Residence`  


**Description:**  
Fired when a settlement garrisoned by a character is besieged

**Author:** `Chris Budd`

## CharacterSkillPointAllocated

**Code:** `CHARACTER_SKILL_POINT_ALLOCATED`  

**Context:** `Character`  


**Description:**  
Fired when an character has a skill point allocated

**Author:** `Chris Budd`

## CharacterTurnEnd

**Code:** `CHARACTER_END_TURN_EVENT`  

**Context:** `Character`  


**Description:**  
Fired for every character at the start of their turn

**Author:** `DAT_117a2ecc`

## CharacterTurnStart

**Code:** `CHARACTER_START_TURN_EVENT`  

**Context:** `Character`  


**Description:**  
Fired for every character at the start of their turn

**Author:** `DAT_117a2ecc`

## CharacterTurnStartCarthage

**Code:** `CHARACTER_START_TURN_EVENT_CARTHAGE`  

**Context:** `Character`  


**Description:**  
Fired for every character at the start of their turn

**Author:** `DAT_117a2ecc`

## CharacterTurnStartRome

**Code:** `CHARACTER_START_TURN_EVENT_ROME`  

**Context:** `Character`  


**Description:**  
Fired for every character at the start of their turn

**Author:** `DAT_117a2ecc`

## ClanBecomesVassal

**Code:** `FACTION_BECOMES_VASSAL`  

**Context:** `Faction`  


**Description:**  
A clan has become a vassal

**Author:** `DAT_1179b680`

## ComponentCreated

**Code:** `COMPONENT_CREATED_EVENT`  

**Context:** `String (name of the Component), Component ( this )`  


**Description:**  
Fires when a Component is first created (at end of RunScript)

**Author:** `Krishna`

## ComponentLClickUp

**Code:** `COMPONENT_LCLICK_EVENT`  

**Context:** `String (ComponentType condition), Component`  


**Description:**  
Triggered when a user clicks on any component

**Author:** `DAT_117a2ecc`

## ComponentMouseOn

**Code:** `COMPONENT_MOUSEON_EVENT`  

**Context:** `String (ComponentType condition), Component`  


**Description:**  
Triggered when a user mouses over any component

**Author:** `Shane`

## ComponentMoved

**Code:** `COMPONENT_MOVED_EVENT`  

**Context:** `String (ComponentType condition), Component`  


**Description:**  
Triggered when a user releases the left button after dragging an item

**Author:** `Shane`

## CustomMission

**Code:** `CUSTOM_MISSION_EVENT`  

**Context:** `Cannot be used in LUA`  


**Description:**  
Internal event: does not fire and cannot be used in the script

**Author:** `DAT_1179ebf0`

## EncylopediaEntryRequested

**Code:** `ENCYCLOPEDIA_ENTRY_REQUESTED`  

**Context:** `String`  


**Description:**  
Fired when an advice button is pressed.

**Author:** `Shane`

## EventMessageOpenedBattle

**Code:** `MESSAGE_OPENED_EVENT_BATTLE`  

**Context:** `string (event name)`  


**Description:**  
triggers when a dropdown message is opened by the user

**Author:** `DAT_117b0390`

## EventMessageOpenedCampaign

**Code:** `MESSAGE_OPENED_EVENT_CAMPAIGN`  

**Context:** `string (event name)`  


**Description:**  
triggers when a dropdown message is opened by the user

**Author:** `DAT_117b0390`

## FactionAboutToEndTurn

**Code:** `FACTION_ABOUT_TO_END_TURN`  

**Context:** `Faction`  


**Description:**  
Faction about to end it\'s turn

**Author:** `DAT_1179b680`

## FactionBattleDefeat

**Code:** `FACTION_BATTLE_DEFEAT`  

**Context:** `Faction`  


**Description:**  
Fired when faction lose a battle

**Author:** `Veli Mollov`

## FactionBattleVictory

**Code:** `FACTION_BATTLE_VICTORY`  

**Context:** `Faction`  


**Description:**  
Fired when faction wins a battle

**Author:** `Veli Mollov`

## FactionBecomesLiberationVassal

**Code:** `FACTION_BECOMES_LIBERATION_VASSAL_EVENT`  

**Context:** `Faction`  


**Description:**  
A faction has liberated another faction

**Author:** `DAT_1179b680`

## FactionBecomesWorldLeader

**Code:** `FACTION_BECOMES_WORLD_LEADER_EVENT`  

**Context:** `Faction`  


**Description:**  
A faction has become world leader

**Author:** `DAT_1179b680`

## FactionBeginTurnPhaseNormal

**Code:** `FACTION_BEGIN_TURN_PHASE_NORMAL`  

**Context:** `Faction`  


**Description:**  
Faction begins its Normal turn phase

**Author:** `DAT_1179b680`

## FactionCapturesWorldCapital

**Code:** `FACTION_CAPTURES_WORLD_CAPITAL_EVENT`  

**Context:** `Faction`  


**Description:**  
A faction has captured the world capital

**Author:** `DAT_1179b680`

## FactionCivilWarEnd

**Code:** `FACTION_CIVIL_WAR_END`  

**Context:** `Faction`  


**Description:**  
Fired when civil war in faction ends

**Author:** `Veli Mollov`

## FactionEncountersOtherFaction

**Code:** `FACTION_ENCOUNTERS_OTHER_FACTION`  

**Context:** `Faction`  


**Description:**  
A faction encounters another faction

**Author:** `DAT_117a1590`

## FactionFameLevelUp

**Code:** `FACTION_FAME_LEVELUP`  

**Context:** `Faction`  


**Description:**  
Faction fame as gone up a level

**Author:** `Chris Budd`

## FactionGovernmentTypeChanged

**Code:** `FACTION_GOVERNMENT_TYPE_CHANGED`  

**Context:** `Faction`  


**Description:**  
The factions government type has changed

**Author:** `DAT_117a159c`

## FactionLeaderDeclaresWar

**Code:** `FACTION_LEADER_DECLARES_WAR`  

**Context:** `Character`  


**Description:**  
War has been declared

**Author:** `DAT_1179b680`

## FactionLeaderIssuesEdict

**Code:** `FACTION_LEADER_ISSUES_EDICT`  

**Context:** `Faction`  


**Description:**  
Fired when a faction issues an edict

**Author:** `Chris Budd`

## FactionLeaderSignsPeaceTreaty

**Code:** `FACTION_LEADER_SIGNS_PEACE_TREATY`  

**Context:** `Character`  


**Description:**  
A peace treaty has been signed

**Author:** `DAT_1179b680`

## FactionPoliticsGovernmentActionTriggered

**Code:** `FACTION_POLITICS_GOVERNMENT_ACTION_TRIGGERED`  

**Context:** `Faction`  


**Description:**  
Fired when a custom scripted action must be executed for a particular politics government type 

**Author:** `Mihail Balabanov`

## FactionPoliticsGovernmentTypeChanged

**Code:** `FACTION_POLITICS_GOVERNMENT_TYPE_CHANGED`  

**Context:** `Faction`  


**Description:**  
Fired when politics government type has changed

**Author:** `Veli Mollov`

## FactionRoundStart

**Code:** `FACTION_START_ROUND`  

**Context:** `Faction`  


**Description:**  
Faction starts the round

**Author:** `DAT_117a159c`

## FactionSecessionEnd

**Code:** `FACTION_SECESSION_END`  

**Context:** `Faction`  


**Description:**  
Fired when secession in faction ends

**Author:** `Veli Mollov`

## FactionSubjugatesOtherFaction

**Code:** `FACTION_SUBJUGATES_OTHER_FACTION`  

**Context:** `Faction`  


**Description:**  
A faction subjugates another faction

**Author:** `DAT_117a2ed8`

## FactionTurnEnd

**Code:** `FACTION_END_TURN`  

**Context:** `Faction`  


**Description:**  
Faction ends it\'s turn

**Author:** `DAT_117a1590`

## FactionTurnStart

**Code:** `FACTION_START_TURN`  

**Context:** `Faction`  


**Description:**  
Faction starts it\'s turn

**Author:** `DAT_117a1590`

## FirstTickAfterNewCampaignStarted

**Code:** `FIRST_TICK_AFTER_NEW_CAMPAIGN_STARTED`  

**Context:** `DAT_1173e900`  


**Description:**  
A new campaign game has being started and the first tick is just being done - not triggered when processing startpos. Guarantees UI is open.

**Author:** `DAT_117a2ed8`

## FirstTickAfterWorldCreated

**Code:** `FIRST_TICK_AFTER_WORLD_CREATED`  

**Context:** `DAT_1173e900`  


**Description:**  
First tick after a game was started or loaded

**Author:** `DAT_117a2ed8`

## ForceAdoptsStance
---
WORKS
```
{military_force: force_interface, stance_adopted: int}
```
**Code:** `FORCE_ADOPTS_STANCE`  

**Context:** `Character`  

**Description:**  
Fired when an characters military force changes stance

**Author:** `Chris Budd`

## FrontendScreenTransition
**Code:** `FRONTEND_TRANSITION_EVENT`  

**Context:** `string (name of layout transitioned to)`  


**Description:**  
triggers we change screens in the frontend

**Author:** `DAT_117b0390`

## GarrisonAttackedEvent

**Code:** `GARRISON_ATTACKED_EVENT`  

**Context:** `DAT_1173dad0`  


**Description:**  
DAT_1173dad0

**Author:** `DAT_1173dad0`

## GarrisonOccupiedEvent

**Code:** `GARRISON_OCCUPIED_EVENT`  

**Context:** `DAT_1173dad0`  


**Description:**  
DAT_1173dad0

**Author:** `DAT_1173dad0`

## GarrisonResidenceCaptured

**Code:** `GARRISON_RESIDENCE_CAPTURED`  

**Context:** `Garrison residence`  


**Description:**  
A garrison residence (settlement, fort, port &c.) has been captured

**Author:** `DAT_1173e50c`

## GovernorshipTaxRateChanged

**Code:** `GOVERNORSHIP_TAX_RATE_CHANGE`  

**Context:** `Governorship`  


**Description:**  
A tax rate in a governorship has changed

**Author:** `DAT_117a1590`

## HistoricBattleEvent

**Code:** `HISTORIC_BATTLE_EVENTS`  

**Context:** `String`  


**Description:**  
Events fired from Historic battle, will send the name of next battle to be played !

**Author:** `Krishna`

## HistoricalCharacters

**Code:** `HISTORICAL_CHARACTER_GENERATION_EVENT`  

**Context:** `List of possible historical characters`  


**Description:**  
DAT_1173dad0

**Author:** `DAT_1179b680`

## HistoricalEvents

**Code:** `HISTORICAL_EVENTS_EVENT`  

**Context:** `List of possible historical events`  


**Description:**  
DAT_1173dad0

**Author:** `DAT_1179b680`

## HudRefresh

**Code:** `HUD_REFRESH_EVENT`  

**Context:** `Empty string`  


**Description:**  
triggers when the HUD is reconstructed

**Author:** `Shane`

## IncomingMessage

**Code:** `INCOMING_MESSAGE_EVENT`  

**Context:** `string (event name)`  


**Description:**  
triggers when a dropdown message first starts falling down the screen

**Author:** `DAT_117b0390`

## LandTradeRouteRaided

**Code:** `LAND_TRADE_ROUTE_ATTACKED_EVENT`  

**Context:** `Character, Position`  


**Description:**  
A character has raided a land trade route

**Author:** `DAT_117a159c`

## LoadingGame

**Code:** `LOAD_GAME_EVENT`  

**Context:** `FileHandle`  


**Description:**  
A game is being loaded

**Author:** `DAT_1179ebf0`

## LoadingScreenDismissed

**Code:** `LOADING_SCREEN_DISMISSED_EVENT`  

**Context:** `Empty string`  


**Description:**  
triggers when loading screen dismissed by player

**Author:** `ScottB`

## LocationEntered

**Code:** `LOCATION_ENTERED_EVENT`  

**Context:** `MAP_LOCATION, the piece that entered`  


**Description:**  
When a piece enters a location trigger, fire ony once per trigger

**Author:** `DAT_1179ebf0`

## LocationUnveiled

**Code:** `LOCATION_UNVEILED_EVENT`  

**Context:** `MAP_LOCATION, the piece that unveiled the area`  


**Description:**  
When the location becomes visible for the first time

**Author:** `DAT_1179ebf0`

## MissionCancelled

**Code:** `MISSION_CANCELLED`  

**Context:** `Mission, mission manager, faction of mission manager, campaign model`  


**Description:**  
A mission has been cancelled - ie is no longer viable

**Author:** `DAT_117a2ed8`

## MissionFailed

**Code:** `MISSION_FAILED`  

**Context:** `Mission, mission manager, faction of mission manager, campaign model`  


**Description:**  
The player has failed a mission

**Author:** `DAT_1173e50c`

## MissionIssued

**Code:** `MISSION_ISSUED`  

**Context:** `Mission, mission manager, faction of mission manager, campaign model`  


**Description:**  
A mission has been issued to the player

**Author:** `DAT_1173e50c`

## MissionNearingExpiry

**Code:** `MISSION_NEARING_EXPIRY`  

**Context:** `Mission, mission manager, faction of mission manager, campaign model`  


**Description:**  
A mission only has a quarter of its time left before its too late to complete it

**Author:** `DAT_1173e50c`

## MissionSucceeded

**Code:** `MISSION_SUCCEEDED`  

**Context:** `Mission, mission manager, faction of mission manager, campaign model`  


**Description:**  
A mission has been successfully completed

**Author:** `DAT_1173e50c`

## ModelCreated

**Code:** `MODEL_CREATED`  

**Context:** `DAT_1173e900`  


**Description:**  
A game is being started or loaded, at this point the most vital parts pf the game are initialized

**Author:** `DAT_1179b680`

## MovementPointsExhausted

**Code:** `CHARACTER_ACTION_POINTS_EXHAUSTED`  

**Context:** `Character`  


**Description:**  
A general can move no more

**Author:** `DAT_117a1590`

## MultiTurnMove

**Code:** `CHARACTER_MULTITURN_MOVE_ISSUED_EVENT`  

**Context:** `Character`  


**Description:**  
A character has been issued a movement that will take more than one turn

**Author:** `DAT_117a159c`

## NewCampaignStarted

**Code:** `NEW_CAMPAIGN_STARTED`  

**Context:** `DAT_1173e900`  


**Description:**  
A new campaign game is being started - called exactly once during a campaign, when it is created for the first time - NOT called when loading, NOT called when processing startpos

**Author:** `DAT_117a2ed8`

## NewSession

**Code:** `NEW_GAME_EVENT`  

**Context:** `model access`  


**Description:**  
A game is being started, could be a new game or loading a save game

**Author:** `DAT_1179ebf0`

## PanelAdviceRequestedBattle

**Code:** `PANEL_ADVICE_EVENT_BATTLE`  

**Context:** `string`  


**Description:**  
triggers when the user clicks on the request advice button on a panel in battle

**Author:** `DAT_117b0390`

## PanelAdviceRequestedCampaign

**Code:** `PANEL_ADVICE_EVENT_CAMPAIGN`  

**Context:** `string`  


**Description:**  
triggers when the user clicks on the request advice button on a panel in the campaign game

**Author:** `DAT_117b0390`

## PanelClosedBattle

**Code:** `PANEL_CLOSED_EVENT_BATTLE`  

**Context:** `string`  


**Description:**  
triggers when a ui panel is closed by the user in battle

**Author:** `DAT_117b0390`

## PanelClosedCampaign

**Code:** `PANEL_CLOSED_EVENT_CAMPAIGN`  

**Context:** `string`  


**Description:**  
triggers when a ui panel is closed by the user in the campaign game

**Author:** `DAT_117b0390`

## PanelOpenedBattle

**Code:** `PANEL_OPEN_EVENT_BATTLE`  

**Context:** `string`  


**Description:**  
triggers when a ui panel is opened by the user in battle

**Author:** `DAT_117b0390`

## PanelOpenedCampaign

**Code:** `PANEL_OPEN_EVENT_CAMPAIGN`  

**Context:** `string`  


**Description:**  
triggers when a ui panel is opened by the user in the campaign game

**Author:** `DAT_117b0390`

## PendingBankruptcy

**Code:** `FACTION_PENDING_BANKRUPTCY_EVENT`  

**Context:** `Faction`  


**Description:**  
The faction is about to go bankrupt

**Author:** `DAT_1179b680`

## PendingBattle

**Code:** `PENDING_BATTLE_EVENT`  

**Context:** `The character and faction initiating the battle`  


**Description:**  
A battle is about to occur

**Author:** `DAT_1179b680`

## PositiveDiplomaticEvent

**Code:** `POSITIVE_DIPLOMATIC_EVENT`  

**Context:** `DAT_1173e900`  


**Description:**  
Fires when a user performs a positive diplomatic action

**Author:** `Chris Budd`

## RecruitmentItemIssuedByPlayer

**Code:** `RECRUITMENT_ITEM_ISSUED_BY_PLAYER`  

**Context:** `unit record`  


**Description:**  
Fired when the player selects adds a unit to the queue

**Author:** `DAT_1179ebf0`

## RegionChangedFaction

**Code:** `REGION_CHANGED_FACTION`  

**Context:** `Region`  


**Description:**  
Fired when a region changes faction

**Author:** `Tsvetan`

## RegionGainedDevlopmentPoint

**Code:** `REGION_GAINED_DEVELOPMENT_POINT`  

**Context:** `Region`  


**Description:**  
Region gained a development point

**Author:** `Chris Budd`

## RegionIssuesDemands

**Code:** `REGION_ISSUES_DEMANDS`  

**Context:** `Region`  


**Description:**  
This region has issued demands

**Author:** `DAT_117a159c`

## RegionRebels

**Code:** `REGION_REBELS`  

**Context:** `Region`  


**Description:**  
This region has started rebelling

**Author:** `DAT_117a159c`

## RegionRiots

**Code:** `REGION_RIOTS`  

**Context:** `Region`  


**Description:**  
This region has started riots

**Author:** `DAT_117a159c`

## RegionSelected

**Code:** `REGION_SELECTED_EVENT`  

**Context:** `Region`  


**Description:**  
Fired when a region is selected

**Author:** `DAT_1179b680`

## RegionStrikes

**Code:** `REGION_STRIKES`  

**Context:** `Region`  


**Description:**  
This region has started striking

**Author:** `DAT_117a1590`

## RegionTurnEnd

**Code:** `REGION_END_TURN`  

**Context:** `Region`  


**Description:**  
Region ends it\'s turn

**Author:** `DAT_117a1590`

## RegionTurnStart

**Code:** `REGION_START_TURN`  

**Context:** `Region`  


**Description:**  
Region starts it\'s turn

**Author:** `DAT_117a1590`

## ResearchCompleted

**Code:** `RESEARCH_COMPLETED_EVENT`  

**Context:** `Technology record, faction`  


**Description:**  
Research has been completed in this slot

**Author:** `Luke, modified by Alan`

## ResearchStarted

**Code:** `RESEARCH_STARTED_EVENT`  

**Context:** `Technology record, faction`  


**Description:**  
Research has been started

**Author:** `DAT_117a1590`

## SavingGame

**Code:** `SAVE_GAME_EVENT`  

**Context:** `FileHandle`  


**Description:**  
A game is being saveed

**Author:** `DAT_1179ebf0`

## ScriptedAgentCreated

**Code:** `SCRIPTED_AGENT_CREATED`  

**Context:** `String`  


**Description:**  
Fired when the an agent is created through script

**Author:** `DAT_1179b680`

## ScriptedAgentCreationFailed

**Code:** `SCRIPTED_AGENT_CREATION_FAILED`  

**Context:** `String`  


**Description:**  
Fired when the an agent is unable to be created through script

**Author:** `DAT_1179b680`

## ScriptedCharacterUnhidden

**Code:** `SCRIPTED_CHARACTER_UNHIDDEN`  

**Context:** `Character`  


**Description:**  
Fired when a character is sucessfully unhidden by script

**Author:** `DAT_1179b680`

## ScriptedCharacterUnhiddenFailed

**Code:** `SCRIPTED_CHARACTER_UNHIDDEN_FAILED`  

**Context:** `Character`  


**Description:**  
Fired when a character is unsucessfully unhidden by script

**Author:** `DAT_1179b680`

## ScriptedForceCreated

**Code:** `SCRIPTED_FORCE_CREATED`  

**Context:** `String`  


**Description:**  
Fired when the a force is created through script

**Author:** `DAT_1179b680`

## SeaTradeRouteRaided

**Code:** `SEA_TRADE_ROUTE_ATTACKED_EVENT`  

**Context:** `Character, Position`  


**Description:**  
A character has raided a sea trade route

**Author:** `DAT_117a159c`

## SettlementDeselected

**Code:** `SETTLEMENT_DESELECTED_EVENT`  

**Context:** `Empty string`  


**Description:**  
triggers when a settlement has been deselected on the campaign map

**Author:** `Christian`

## SettlementSelected

**Code:** `SETTLEMENT_SELECTED_EVENT`  

**Context:** `Settlement`  


**Description:**  
Fired when the player selects a settlement on the map

**Author:** `DAT_117a2ecc`

## ShortcutTriggered

**Code:** `SHORTCUT_TRIGGERED`  

**Context:** `String`  


**Description:**  
Fired when a keyboard shortcut is triggered

**Author:** `DAT_1179b680`

## SlotOpens

**Code:** `REGION_SLOT_POPPED_EVENT`  

**Context:** `Slot, Region`  


**Description:**  
A slot has just opened

**Author:** `DAT_117a159c`

## SlotRoundStart

**Code:** `REGION_SLOT_ROUND_START_EVENT`  

**Context:** `Slot, Region`  


**Description:**  
The start of round for this slot

**Author:** `DAT_117a159c`

## SlotSelected

**Code:** `SLOT_SELECTED_EVENT`  

**Context:** `DAT_117a5ac0`  


**Description:**  
Fired when the player selects a settlement slot on the map

**Author:** `DAT_117a2ecc`

## SlotTurnStart

**Code:** `REGION_SLOT_START_TURN_EVENT`  

**Context:** `Slot, Region`  


**Description:**  
The start of turn for this slot

**Author:** `DAT_117a159c`

## TechnologyInfoPanelOpenedCampaign

**Code:** `TECHNOLOGY_INFO_PANEL_OPEN_EVENT_CAMPAIGN`  

**Context:** `string`  


**Description:**  
triggers when the technology info panel is opened by the user in the campaign game

**Author:** `shane`

## TestEvent

**Code:** `TEST_EVENT`  

**Context:** `model`  


**Description:**  
Test event

**Author:** `DAT_117a1590`

## TooltipAdvice

**Code:** `TOOLTIP_ADVICE_EVENT`  

**Context:** `string`  


**Description:**  
triggers when a tooltip cycles though all of it\'s available lines (only happens at end of first sequence

**Author:** `DAT_117b0390`

## TouchUsed

**Code:** `TOUCH_USED_EVENT`  

**Context:** `battle_ui`  


**Description:**  
Trigger when touch controls have been used

**Author:** `Petr Tomicek`

## TradeNodeConnected

**Code:** `CHARACTER_ESTABLISHED_DOMESTIC_TRADE_ROUTE`  

**Context:** `Character`  


**Description:**  
Fired when a character enters a trade node and establishes a trade route

**Author:** `DAT_1179b680`

## TradeRouteEstablished

**Code:** `TRADE_ROUTE_ESTABLISHED`  

**Context:** `Faction`  


**Description:**  
A trade route has been established with this faction

**Author:** `DAT_117a159c`

## UICreated

**Code:** `UI_CREATED_EVENT`  

**Context:** `String (name of the UI), Component (root component of the ui)`  


**Description:**  
Fires when the UI is first created

**Author:** `DAT_117a2ecc`

## UIDestroyed

**Code:** `UI_DESTROYED_EVENT`  

**Context:** `String (name of the UI)`  


**Description:**  
Fires when the UI is destroyed

**Author:** `DAT_117a2ecc`

## UnitCompletedBattle

**Code:** `UNIT_COMPLETED_BATTLE_EVENT`  

**Context:** `DAT_117af86c`  


**Description:**  
A unit has completed the battle

**Author:** `DAT_117a159c`

## UnitCreated

**Code:** `UNIT_CREATION_EVENT`  

**Context:** `DAT_117af86c`  


**Description:**  
A unit has been created

**Author:** `DAT_117a159c`

## UnitSelectedCampaign

**Code:** `UNIT_SELECTED_EVENT_CAMPAIGN`  

**Context:** `Unit (campaign)`  


**Description:**  
Fires when a unit card is selected on the campaign map

**Author:** `DAT_117a2ecc`

## UnitTrained

**Code:** `UNIT_RECRUITED_EVENT`  

**Context:** `DAT_117af86c`  


**Description:**  
A unit is trained

**Author:** `DAT_117a1590`

## UnitTurnEnd

**Code:** `UNIT_TURN_END_EVENT`  

**Context:** `DAT_117af86c`  


**Description:**  
A unit has ended its turn

**Author:** `DAT_117a159c`

## WorldCreated

**Code:** `WORLD_CREATED`  

**Context:** `DAT_1173e900`  


**Description:**  
A game is being started or loaded, at this point the most vital parts of the game are initialized

**Author:** `DAT_117a1590`
