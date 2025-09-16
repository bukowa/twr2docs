---
title: cdir events options
summary: A brief description of my document.
---

This is from Attila
```

option_key	notes
#cdir_events_options_tables;0;db/cdir_events_options_tables/cdir_events_options
CND_ALLIED_WITH	Is the player faction ALLIED with the key-specified FACTION? Multiple use operator: AND.
CND_ALLIED_WITH_SUBCULTURE	Is the player faction ALLIED with AT LEAST ONE FACTION belonging to the key-specified SUBCULTURE? Multiple use operator: UNSURE!
CND_ALLY_SHOGUN	[OBSOLETE] Is the player faction allied with whichever clan rules the Shogunate?
CND_ARMY_CAP_FREE	Can the player faction sustain ADDITIONAL ARMIES?
CND_ARMY_IN_ENEMY_REGION	Does the player faction have AT LEAST ONE ARMY in an ENEMY REGION?
CND_ASHIKAGA_SHOGUN	[OBSOLETE] Does the Ashikaga clan rules the Shogunate?
CND_BUILDING_CHAIN	Does the player faction have AT LEAST ONE instance of the key-specified BUILDING CHAIN? Multiple use operator: AND.
CND_BUILDING_CHAIN_AVAILABLE	Is the player faction currently able to CONSTRUCT the key-specified BUILDING CHAIN in one of their settlements? Multiple use operator: AND.
CND_BUILDING_LEVEL	Does the player faction have AT LEAST ONE instance of the key-specified BUILDING LEVEL? Multiple use operator: AND.
CND_BUILDING_LEVEL_AVAILABLE	Is the player faction currently able to CONSTRUCT the key-specified BUILDING LEVEL in one of their settlements? Multiple use operator: AND.
CND_BUILDING_LEVEL_HALF_REGIONS	Does the player faction have an instance of the key-specified BUILDING LEVEL in at least HALF of their REGIONS? Multiple use operator: UNSURE!
CND_BUILDING_LEVEL_ONE_QUARTER_REGIONS	Does the player faction have an instance of the key-specified BUILDING LEVEL in AT LEAST ONE-QUARTER of their REGIONS? Multiple use operator: UNSURE!
CND_BUILDING_LEVEL_THREE_QUARTER_REGIONS	Does the player faction have an instance of the key-specified BUILDING LEVEL in at least THREE-QUARTERS of their REGIONS? Multiple use operator: UNSURE!
CND_CAMPAIGN	Is the CAMPAIGN being played this key-specified one? Multiple use operator: OR.
CND_CAN_RECRUIT_UNIT	Can the player faction currently RECRUIT the unit_key-specified UNIT? Multiple use operator: UNSURE!
CND_CAN_RECRUIT_UNIT_CASTE	Can the player faction currently RECRUIT the unit_caste-specified UNIT? Multiple use operator: UNSURE!
CND_CAN_RECRUIT_UNIT_CATEGORY	Can the player faction currently RECRUIT the unit_category-specified UNIT? Multiple use operator: UNSURE!
CND_CAN_RECRUIT_UNIT_CLASS	Can the player faction currently RECRUIT the unit_class-specified UNIT? Multiple use operator: UNSURE!
CND_CONSTRUCTING_BUILDING_CHAIN	Is the player faction currently CONSTRUCTING a building from the key-specified BUILDING CHAIN? Multiple use operator: AND.
CND_CONSTRUCTING_BUILDING_LEVEL	Is the player faction currently CONSTRUCTING the key-specified BUILDING LEVEL? Multiple use operator: AND.
CND_CONSTRUCTING_NOT_BUILDING_CHAIN	Is the player faction currently NOT CONSTRUCTING a building from the key-specified BUILDING CHAIN? Multiple use operator: AND.
CND_CONSTRUCTING_NOT_BUILDING_LEVEL	Is the player faction currently NOT CONSTRUCTING the key-specified BUILDING LEVEL? Multiple use operator: AND.
CND_DILEMMA_CHOSEN_FIRST	Did the player choose the FIRST OPTION when faced with the key-specified DILEMMA? Multiple use operator: OR. [NOTE: We require additional options for CHOSEN_THIRD and CHOSEN_FOURTH]
CND_DILEMMA_CHOSEN_SECOND	Did the player choose the SECOND OPTION when faced with the key-specified DILEMMA? Multiple use operator: OR. [NOTE: We require additional options for CHOSEN_THIRD and CHOSEN_FOURTH]
CND_DILEMMA_GENERATED	Has the key-specified DILEMMA been GENERATED for the player during this campaign? Multiple use operator: OR.
CND_DILEMMA_NOT_CHOSEN_FIRST	Did the player NOT choose the FIRST OPTION when faced with the key-specified DILEMMA? Multiple use operator: OR. [NOTE: We require additional options for CHOSEN_THIRD and CHOSEN_FOURTH]
CND_DILEMMA_NOT_CHOSEN_SECOND	Did the player NOT choose the SECOND OPTION when faced with the key-specified DILEMMA? Multiple use operator: OR. [NOTE: We require additional options for CHOSEN_THIRD and CHOSEN_FOURTH]
CND_DILEMMA_NOT_GENERATED	Has the key-specified DILEMMA NOT been GENERATED for the player during this campaign? Multiple use operator: OR.
CND_ENEMY_ARMY_IN_REGION	Is there an ENEMY ARMY in any of the player faction's REGIONS?
CND_FACTION	Is the player currently playing as this FACTION? Multiple use operator: OR.
CND_FIRST_ROUND	Specify the FIRST ROUND that a random event may be GENERATED during a campaign.
CND_HAS_AGENT	Does the player faction have AT LEAST ONE instance of the key-specified AGENT? Multiple use operator: UNSURE!
CND_HAS_ARMY	Does the player faction have AT LEAST ONE ARMY?
CND_HAS_NAVY	Does the player faction have AT LEAST ONE NAVY?
CND_INCIDENT_GENERATED	Has the key-specified INCIDENT been GENERATED for the player during this campaign? Multiple use operator: OR.
CND_INCIDENT_NOT_GENERATED	Has the key-specified INCIDENT NOT been GENERATED for the player during this campaign? Multiple use operator: OR.
CND_IS_BECOMING_SHOGUN	[OBSOLETE] Is the player faction in the process of assuming control of the Shogunate?
CND_IS_SHOGUN	[OBSOLETE] Does the player faction rule the Shogunate?
CND_LAST_ROUND	Specify the LAST ROUND that a random event may be GENERATED during a campaign.
CND_MAX_ALLIED	Is the player faction ALLIED with NO MORE THAN the specified number of FACTIONS?
CND_MAX_ARTILLERY_CATEGORY_RATIO	Of all the player faction's UNITS, do NO MORE THAN the specified proportion of them belong to the ARTILLERY category?
CND_MAX_BUDDHIST_RATIO	[OBSOLETE] Does the player faction have NO MORE THAN the specified average proportion of Buddhism across their territory?
CND_MAX_CAVALRY_CATEGORY_RATIO	Of all the player faction's UNITS, do NO MORE THAN the specified proportion of them belong to the CAVALRY category?
CND_MAX_CHRISTIAN_RATIO	[OBSOLETE] Does the player faction have NO MORE THAN the specified average proportion of Christianity across their territory?
CND_MAX_CIVIL_TECHNOLOGY_RATIO	[BROKEN?] Of all the player faction's researched TECHNOLOGIES, are NO MORE THAN the specified proportion CIVIL TECHNOLOGIES?
CND_MAX_COASTAL_REGIONS_OWNED	[BROKEN?] Does the player faction own NO MORE THAN the specified number of COASTAL REGIONS?
CND_MAX_DAIMYO_HONOUR	[OBSOLETE] Does the player faction's daimyo have NO MORE THAN the specified amount of Honour.
CND_MAX_ENGINEERING_TECHNOLOGY_RATIO	[BROKEN?] Of all the player faction's researched TECHNOLOGIES, are NO MORE THAN the specified proportion ENGINEERING TECHNOLOGIES?
CND_MAX_FACTION_NEIGHBOUR_ALLIED	Is the player faction ALLIED with NO MORE THAN the specified number of NEIGHBOURING FACTIONS?
CND_MAX_FACTION_NEIGHBOUR_MILITARY_ACCESS_GIVEN	[BROKEN?] Has the player faction GIVEN MILITARY ACCESS to NO MORE THAN the specified number of NEIGHBOURING FACTIONS?
CND_MAX_FACTION_NEIGHBOUR_MILITARY_ACCESS_RECEIVED	[BROKEN?] Has the player faction RECEIVED MILITARY ACCESS from NO MORE THAN the specified number of NEIGHBOURING FACTIONS?
CND_MAX_FACTION_NEIGHBOUR_NEUTRAL	Is the player faction NEUTRAL towards NO MORE THAN the specified number of NEIGHBOURING FACTIONS?
CND_MAX_FACTION_NEIGHBOUR_PROTECTORATES	[BROKEN?] Is the player faction the OVERLORD of NO MORE THAN the specified number of NEIGHBOURING FACTIONS?
CND_MAX_FACTION_NEIGHBOUR_TRADE	Is the player faction TRADING with NO MORE THAN the specified number of NEIGHBOURING FACTIONS?
CND_MAX_FACTION_NEIGHBOUR_WAR	Is the player faction AT WAR with NO MORE THAN the specified number of NEIGHBOURING FACTIONS?
CND_MAX_FAME	Does the player faction have NO MORE THAN the specified amount of FAME / PRESTIGE / IMPERIUM.
CND_MAX_FAME_LEVEL	[OBSOLETE] Is the player faction's  FAME / PRESTIGE / IMPERIUM level NO HIGHER THAN the given Shogun-specific fame level?
CND_MAX_FAME_RANK	Is the player faction's  FAME / PRESTIGE / IMPERIUM level NO HIGHER THAN the value specified?
CND_MAX_FORCE_COUNT	Does the player faction have NO MORE THAN the specified number of MILITARY FORCES.
CND_MAX_HIGHEST_FAME_LEVEL	[OBSOLETE] Was the player faction's  highest ever FAME / PRESTIGE / IMPERIUM level NO HIGHER THAN the given Shogun-specific fame level?
CND_MAX_INFANTRY_MELEE_CATEGORY_RATIO	Of all the player faction's UNITS, do NO MORE THAN the specified proportion of them belong to the MELEE INFANTRY category?
CND_MAX_INFANTRY_RANGED_CATEGORY_RATIO	Of all the player faction's UNITS, do NO MORE THAN the specified proportion of them belong to the RANGED INFANTRY category?
CND_MAX_LAND_UNIT_COUNT	Does the player faction have NO MORE THAN the specified number of LAND UNITS?
CND_MAX_MERCENARY_UNIT_COUNT	Does the player faction have NO MORE THAN the specified number of MERCENARY UNITS?
CND_MAX_MILITARY_ACCESS_GIVEN	[BROKEN?] Has the player faction GIVEN MILITARY ACCESS to NO MORE THAN the specified number of FACTIONS?
CND_MAX_MILITARY_ACCESS_RECEIVED	[BROKEN?] Has the player faction RECEIVED MILITARY ACCESS from NO MORE THAN the specified number of FACTIONS?
CND_MAX_MILITARY_TECHNOLOGY_RATIO	[BROKEN?] Of all the player faction's researched TECHNOLOGIES, are NO MORE THAN the specified proportion MILITARY TECHNOLOGIES?
CND_MAX_NAVAL_HEAVY_CATEGORY_RATIO	Of all the player faction's UNITS, do NO MORE THAN the specified proportion of them belong to the HEAVY NAVAL category?
CND_MAX_NAVAL_LIGHT_CATEGORY_RATIO	Of all the player faction's UNITS, do NO MORE THAN the specified proportion of them belong to the LIGHT NAVAL category?
CND_MAX_NAVAL_MEDIUM_CATEGORY_RATIO	Of all the player faction's UNITS, do NO MORE THAN the specified proportion of them belong to the MEDIUM NAVAL category?
CND_MAX_NAVAL_UNIT_COUNT	Does the player faction have NO MORE THAN the specified number of NAVAL UNITS?
CND_MAX_NEUTRAL	Is the player faction NEUTRAL towards NO MORE THAN the specified number of FACTIONS?
CND_MAX_PROTECTORATES	[BROKEN?] Is the player faction the OVERLORD of NO MORE THAN the specified number of FACTIONS?
CND_MAX_PROVINCES_FULLY_OWNED	Does the player faction fully own NO MORE THAN the specified number of PROVINCES?
CND_MAX_REGIONS_OWNED	Does the player faction own NO MORE THAN the specified number of REGIONS?
CND_MAX_REGION_NEIGHBOUR_ALLIED	Is the player faction ALLIED with the owners of NO MORE THAN the specified number of NEIGHBOURING REGIONS?
CND_MAX_REGION_NEIGHBOUR_MILITARY_ACCESS_GIVEN	[BROKEN?] Has the player faction GIVEN MILITARY ACCESS to the owners of NO MORE THAN the specified number of NEIGHBOURING REGIONS?
CND_MAX_REGION_NEIGHBOUR_MILITARY_ACCESS_RECEIVED	[BROKEN?] Has the player faction RECEIVED MILITARY ACCESS from the owners of NO MORE THAN the specified number of NEIGHBOURING REGIONS?
CND_MAX_REGION_NEIGHBOUR_NEUTRAL	Is the player faction NEUTRAL towards the owners of NO MORE THAN the specified number of NEIGHBOURING REGIONS?
CND_MAX_REGION_NEIGHBOUR_PROTECTORATES	[BROKEN?] Is the player faction the OVERLORD of the owners of NO MORE THAN the specified number of NEIGHBOURING REGIONS?
CND_MAX_REGION_NEIGHBOUR_TRADE	Is the player faction TRADING with the owners of NO MORE THAN the specified number of NEIGHBOURING REGIONS?
CND_MAX_REGION_NEIGHBOUR_WAR	Is the player faction AT WAR with the owners of NO MORE THAN the specified number of NEIGHBOURING REGIONS?
CND_MAX_REGULAR_EXPENDITURE	Is the player faction SPENDING NO MORE THAN the specified amount every turn?
CND_MAX_REGULAR_EXPENDITURE_DIPLOMACY	[BROKEN?] Is the player faction SPENDING NO MORE THAN the specified amount on DIPLOMACY every turn?
CND_MAX_REGULAR_EXPENDITURE_POLICING	[BROKEN?] Is the player faction SPENDING NO MORE THAN the specified amount on POLICING every turn?
CND_MAX_REGULAR_EXPENDITURE_PROTECTORATE	[BROKEN?] Is the player faction SPENDING NO MORE THAN the specified amount on PROTECTORATES / VASSALS / CLIENTS / SATRAPIES every turn?
CND_MAX_REGULAR_EXPENDITURE_UPKEEP	Is the player faction SPENDING NO MORE THAN the specified amount on TOTAL UPKEEP every turn?
CND_MAX_REGULAR_EXPENDITURE_UPKEEP_ARMY	Is the player faction SPENDING NO MORE THAN the specified amount on ARMY UPKEEP every turn?
CND_MAX_REGULAR_EXPENDITURE_UPKEEP_NAVY	Is the player faction SPENDING NO MORE THAN the specified amount on NAVY UPKEEP every turn?
CND_MAX_REGULAR_INCOME	Is the player faction EARNING NO MORE THAN the specified amount every turn?
CND_MAX_REGULAR_INCOME_DIPLOMACY	[BROKEN?] Is the player faction EARNING NO MORE THAN the specified amount from DIPLOMACY every turn?
CND_MAX_REGULAR_INCOME_PROTECTORATE	[BROKEN?] Is the player faction EARNING NO MORE THAN the specified amount from PROTECTORATES / VASSALS / CLIENTS / SATRAPIES every turn?
CND_MAX_REGULAR_INCOME_RAIDING	[BROKEN?] Is the player faction EARNING NO MORE THAN the specified amount from RAIDING every turn?
CND_MAX_REGULAR_INCOME_TAXES	[BROKEN?] Is the player faction EARNING NO MORE THAN the specified amount from TAXES every turn?
CND_MAX_REGULAR_INCOME_TRADE	[BROKEN?] Is the player faction EARNING NO MORE THAN the specified amount from TRADE every turn?
CND_MAX_TRADE	Is the player faction TRADING with NO MORE THAN the specified number of FACTIONS?
CND_MAX_TRADE_NODE_OCCUPIED	[OBSOLETE] Is the player faction occupying NO MORE THAN the specified number of TRADE NODES?
CND_MAX_TREASURY	Does the player faction have NO MORE THAN the specified amount of money in its coffers?
CND_MAX_WAR	Is the player faction AT WAR with NO MORE THAN the specified number of FACTIONS?
CND_MIN_ALLIED	Is the player faction ALLIED with AT LEAST the specified number of FACTIONS?
CND_MIN_ARTILLERY_CATEGORY_RATIO	Of all the player faction's UNITS, do AT LEAST the specified proportion of them belong to the ARTILLERY category?
CND_MIN_BUDDHIST_RATIO	[OBSOLETE] Does the player faction have AT LEAST the specified average proportion of Buddhism across their territory?
CND_MIN_CAVALRY_CATEGORY_RATIO	Of all the player faction's UNITS, do AT LEAST the specified proportion of them belong to the CAVALRY category?
CND_MIN_CHRISTIAN_RATIO	[OBSOLETE] Does the player faction have AT LEAST the specified average proportion of Christianity across their territory?
CND_MIN_CIVIL_TECHNOLOGY_RATIO	[BROKEN?] Of all the player faction's researched TECHNOLOGIES, are AT LEAST the specified proportion CIVIL TECHNOLOGIES?
CND_MIN_COASTAL_REGIONS_OWNED	[BROKEN?] Does the player faction own AT LEAST the specified number of COASTAL REGIONS?
CND_MIN_DAIMYO_HONOUR	[OBSOLETE] Does the player faction's daimyo have AT LEAST the specified amount of Honour.
CND_MIN_ENGINEERING_TECHNOLOGY_RATIO	[BROKEN?] Of all the player faction's researched TECHNOLOGIES, are AT LEAST the specified proportion ENGINEERING TECHNOLOGIES?
CND_MIN_FACTION_NEIGHBOUR_ALLIED	Is the player faction ALLIED with AT LEAST the specified number of NEIGHBOURING FACTIONS?
CND_MIN_FACTION_NEIGHBOUR_MILITARY_ACCESS_GIVEN	[BROKEN?] Has the player faction GIVEN MILITARY ACCESS to AT LEAST the specified number of NEIGHBOURING FACTIONS?
CND_MIN_FACTION_NEIGHBOUR_MILITARY_ACCESS_RECEIVED	[BROKEN?] Has the player faction RECEIVED MILITARY ACCESS from AT LEAST the specified number of NEIGHBOURING FACTIONS?
CND_MIN_FACTION_NEIGHBOUR_NEUTRAL	Is the player faction NEUTRAL towards AT LEAST the specified number of NEIGHBOURING FACTIONS?
CND_MIN_FACTION_NEIGHBOUR_PROTECTORATES	[BROKEN?] Is the player faction the OVERLORD of AT LEAST the specified number of NEIGHBOURING FACTIONS?
CND_MIN_FACTION_NEIGHBOUR_TRADE	Is the player faction TRADING with AT LEAST the specified number of NEIGHBOURING FACTIONS?
CND_MIN_FACTION_NEIGHBOUR_WAR	Is the player faction AT WAR with AT LEAST the specified number of NEIGHBOURING FACTIONS?
CND_MIN_FAME	Does the player faction have AT LEAST the specified amount of FAME / PRESTIGE / IMPERIUM.
CND_MIN_FAME_LEVEL	[OBSOLETE] Is the player faction's  FAME / PRESTIGE / IMPERIUM level NO HIGHER THAN the given Shogun-specific fame level?
CND_MIN_FAME_RANK	Is the player faction's  FAME / PRESTIGE / IMPERIUM level NO HIGHER THAN the value specified?
CND_MIN_FORCE_COUNT	Does the player faction have AT LEAST the specified number of MILITARY FORCES.
CND_MIN_HIGHEST_FAME_LEVEL	[OBSOLETE] Was the player faction's  highest ever FAME / PRESTIGE / IMPERIUM level NO HIGHER THAN the given Shogun-specific fame level?
CND_MIN_INFANTRY_MELEE_CATEGORY_RATIO	Of all the player faction's UNITS, do AT LEAST the specified proportion of them belong to the MELEE INFANTRY category?
CND_MIN_INFANTRY_RANGED_CATEGORY_RATIO	Of all the player faction's UNITS, do AT LEAST the specified proportion of them belong to the RANGED INFANTRY category?
CND_MIN_LAND_UNIT_COUNT	Does the player faction have AT LEAST the specified number of LAND UNITS?
CND_MIN_MERCENARY_UNIT_COUNT	Does the player faction have AT LEAST the specified number of MERCENARY UNITS?
CND_MIN_MILITARY_ACCESS_GIVEN	[BROKEN?] Has the player faction GIVEN MILITARY ACCESS to AT LEAST the specified number of FACTIONS?
CND_MIN_MILITARY_ACCESS_RECEIVED	[BROKEN?] Has the player faction RECEIVED MILITARY ACCESS from AT LEAST the specified number of FACTIONS?
CND_MIN_MILITARY_TECHNOLOGY_RATIO	[BROKEN?] Of all the player faction's researched TECHNOLOGIES, are AT LEAST the specified proportion MILITARY TECHNOLOGIES?
CND_MIN_NAVAL_HEAVY_CATEGORY_RATIO	Of all the player faction's UNITS, do AT LEAST the specified proportion of them belong to the HEAVY NAVAL category?
CND_MIN_NAVAL_LIGHT_CATEGORY_RATIO	Of all the player faction's UNITS, do AT LEAST the specified proportion of them belong to the LIGHT NAVAL category?
CND_MIN_NAVAL_MEDIUM_CATEGORY_RATIO	Of all the player faction's UNITS, do AT LEAST the specified proportion of them belong to the MEDIUM NAVAL category?
CND_MIN_NAVAL_UNIT_COUNT	Does the player faction have AT LEAST the specified number of NAVAL UNITS?
CND_MIN_NEUTRAL	Is the player faction NEUTRAL towards AT LEAST the specified number of FACTIONS?
CND_MIN_PROTECTORATES	[BROKEN?] Is the player faction the OVERLORD of AT LEAST the specified number of FACTIONS?
CND_MIN_PROVINCES_FULLY_OWNED	Does the player faction fully own AT LEAST the specified number of PROVINCES?
CND_MIN_REGIONS_OWNED	Does the player faction own AT LEAST the specified number of REGIONS?
CND_MIN_REGION_NEIGHBOUR_ALLIED	Is the player faction ALLIED with the owners of AT LEAST the specified number of NEIGHBOURING REGIONS?
CND_MIN_REGION_NEIGHBOUR_MILITARY_ACCESS_GIVEN	[BROKEN?] Has the player faction GIVEN MILITARY ACCESS to the owners of AT LEAST the specified number of NEIGHBOURING REGIONS?
CND_MIN_REGION_NEIGHBOUR_MILITARY_ACCESS_RECEIVED	[BROKEN?] Has the player faction RECEIVED MILITARY ACCESS from the owners of AT LEAST the specified number of NEIGHBOURING REGIONS?
CND_MIN_REGION_NEIGHBOUR_NEUTRAL	Is the player faction NEUTRAL towards the owners of AT LEAST the specified number of NEIGHBOURING REGIONS?
CND_MIN_REGION_NEIGHBOUR_PROTECTORATES	[BROKEN?] Is the player faction the OVERLORD of the owners of AT LEAST the specified number of NEIGHBOURING REGIONS?
CND_MIN_REGION_NEIGHBOUR_TRADE	Is the player faction TRADING with the owners of AT LEAST the specified number of NEIGHBOURING REGIONS?
CND_MIN_REGION_NEIGHBOUR_WAR	Is the player faction AT WAR with the owners of AT LEAST the specified number of NEIGHBOURING REGIONS?
CND_MIN_REGULAR_EXPENDITURE	Is the player faction SPENDING AT LEAST the specified amount every turn?
CND_MIN_REGULAR_EXPENDITURE_DIPLOMACY	[BROKEN?] Is the player faction SPENDING AT LEAST the specified amount on DIPLOMACY every turn?
CND_MIN_REGULAR_EXPENDITURE_POLICING	[BROKEN?] Is the player faction SPENDING AT LEAST the specified amount on POLICING every turn?
CND_MIN_REGULAR_EXPENDITURE_PROTECTORATE	[BROKEN?] Is the player faction SPENDING AT LEAST the specified amount on PROTECTORATES / VASSALS / CLIENTS / SATRAPIES every turn?
CND_MIN_REGULAR_EXPENDITURE_UPKEEP	Is the player faction SPENDING AT LEAST the specified amount on TOTAL UPKEEP every turn?
CND_MIN_REGULAR_EXPENDITURE_UPKEEP_ARMY	Is the player faction SPENDING AT LEAST the specified amount on ARMY UPKEEP every turn?
CND_MIN_REGULAR_EXPENDITURE_UPKEEP_NAVY	Is the player faction SPENDING AT LEAST the specified amount on NAVY UPKEEP every turn?
CND_MIN_REGULAR_INCOME	Is the player faction EARNING AT LEAST the specified amount every turn?
CND_MIN_REGULAR_INCOME_DIPLOMACY	[BROKEN?] Is the player faction EARNING AT LEAST the specified amount from DIPLOMACY every turn?
CND_MIN_REGULAR_INCOME_PROTECTORATE	[BROKEN?] Is the player faction EARNING AT LEAST the specified amount from PROTECTORATES / VASSALS / CLIENTS / SATRAPIES every turn?
CND_MIN_REGULAR_INCOME_RAIDING	[BROKEN?] Is the player faction EARNING AT LEAST the specified amount from RAIDING every turn?
CND_MIN_REGULAR_INCOME_TAXES	[BROKEN?] Is the player faction EARNING AT LEAST the specified amount from TAXES every turn?
CND_MIN_REGULAR_INCOME_TRADE	[BROKEN?] Is the player faction EARNING AT LEAST the specified amount from TRADE every turn?
CND_MIN_TRADE	Is the player faction TRADING with AT LEAST the specified number of FACTIONS?
CND_MIN_TRADE_NODE_OCCUPIED	[OBSOLETE] Is the player faction occupying AT LEAST the specified number of TRADE NODES?
CND_MIN_TREASURY	Does the player faction have AT LEAST the specified amount of money in its coffers?
CND_MIN_WAR	Is the player faction AT WAR with AT LEAST the specified number of FACTIONS?
CND_MISSION_ACTIVE	Is the key-specified MISSION currently in play?
CND_MISSION_FAILED	Has the key-specified MISSION been FAILED by the player during this campaign?
CND_MISSION_GENERATED	Has the key-specified MISSION been GENERATED for the player during this campaign? Multiple use operator: OR.
CND_MISSION_ISSUER_ROUNDS_UNTIL_NEXT	Specify the number of ROUNDS that must elapse before another MISSION associated with the same MISSION ISSUER as this one can be GENERATED.
CND_MISSION_NOT_ACTIVE	Is the key-specified MISSION NOT currently in play?
CND_MISSION_NOT_GENERATED	Has the key-specified MISSION NOT been GENERATED for the player during this campaign? Multiple use operator: OR.
CND_MISSION_SUCCEEDED	Has the key-specified MISSION been SUCCEEDED by the player during this campaign?
CND_MISSION_TYPE_ROUNDS_UNTIL_NEXT	Specify the number of ROUNDS that must elapse before another MISSION associated with the same MISSION TYPE as this one can be GENERATED.
CND_MULTIPLAYER	Is the CAMPAIGN being played a MULTIPLAYER one?
CND_NAVY_CAP_FREE	Can the player faction sustain ADDITIONAL NAVIES?
CND_NEUTRAL_WITH	Is the player faction NEUTRAL towards the key-specified FACTION? Multiple use operator: AND.
CND_NOT_ALLIED_WITH	Is the player faction NOT ALLIED with the key-specified FACTION? Multiple use operator: AND.
CND_NOT_ALLIED_WITH_SUBCULTURE	Is the player faction NOT ALLIED with AT LEAST ONE FACTION belonging to the key-specified SUBCULTURE? Multiple use operator: UNSURE!
CND_NOT_ALLY_SHOGUN	[OBSOLETE] Is the player faction not allied with whichever clan rules the Shogunate?
CND_NOT_ARMY_CAP_FREE	Can the player faction NOT sustain ADDITIONAL ARMIES?
CND_NOT_ARMY_IN_ENEMY_REGION	Does the player faction NOT have AT LEAST ONE ARMY in an ENEMY REGION?
CND_NOT_ASHIKAGA_SHOGUN	[OBSOLETE] Does the Ashikaga clan not rule the Shogunate?
CND_NOT_BUILDING_CHAIN	Does the player faction NOT have AT LEAST ONE instance of the key-specified BUILDING CHAIN? Multiple use operator: AND.
CND_NOT_BUILDING_CHAIN_AVAILABLE	Is the player faction NOT currently able to CONSTRUCT the key-specified BUILDING CHAIN in one of their settlements? Multiple use operator: AND.
CND_NOT_BUILDING_LEVEL	Does the player faction NOT have AT LEAST ONE instance of the key-specified BUILDING LEVEL? Multiple use operator: AND.
CND_NOT_BUILDING_LEVEL_AVAILABLE	Is the player faction NOT currently able to CONSTRUCT the key-specified BUILDING LEVEL in one of their settlements? Multiple use operator: AND.
CND_NOT_CAN_RECRUIT_UNIT	Can the player faction currently NOT RECRUIT the unit_key-specified UNIT? Multiple use operator: UNSURE!
CND_NOT_CAN_RECRUIT_UNIT_CASTE	Can the player faction currently NOT RECRUIT the unit_caste-specified UNIT? Multiple use operator: UNSURE!
CND_NOT_CAN_RECRUIT_UNIT_CATEGORY	Can the player faction currently NOT RECRUIT the unit_category-specified UNIT? Multiple use operator: UNSURE!
CND_NOT_CAN_RECRUIT_UNIT_CLASS	Can the player faction currently NOT RECRUIT the unit_class-specified UNIT? Multiple use operator: UNSURE!
CND_NOT_ENEMY_ARMY_IN_REGION	Is there NOTan ENEMY ARMY in any of the player faction's REGIONS?
CND_NOT_HAS_AGENT	Does the player faction NOT have AT LEAST ONE instance of the key-specified AGENT? Multiple use operator: UNSURE!
CND_NOT_HAS_ARMY	Does the player faction NOT have AT LEAST ONE ARMY?
CND_NOT_HAS_NAVY	Does the player faction NOT have AT LEAST ONE NAVY?
CND_NOT_IS_BECOMING_SHOGUN	[OBSOLETE] Is the player faction not in the process of assuming control of the Shogunate?
CND_NOT_IS_SHOGUN	[OBSOLETE] Does the player faction not rule the Shogunate?
CND_NOT_MULTIPLAYER	Is the CAMPAIGN being played NOT a MULTIPLAYER one?
CND_NOT_NAVY_CAP_FREE	Can the player faction NOT sustain ADDITIONAL NAVIES?
CND_NOT_NEUTRAL_WITH	Is the player faction NOT NEUTRAL towards the key-specified FACTION? Multiple use operator: AND.
CND_NOT_OWNS_HOME_REGION	Does the player faction NOT OWN their HOME REGION?
CND_NOT_OWNS_REGION	Does the player faction NOT OWN the key-specified REGION?
CND_NOT_POLITICAL_PARTY	Does the player NOT belong to the key-specified POLITICAL PARTY?
CND_NOT_PORT_BLOCKADED	Is the player faction NOT currently suffering from a BLOCKADE somewhere?
CND_NOT_REALM_DIVIDE	[OBSOLETE] Has the player faction NOT experienced realm divide yet?
CND_NOT_REBELLION	Is the player faction NOT currently experiencing a REBELLION somewhere?
CND_NOT_RELIGION	Does the player faction NOT belong to a key-specified RELIGION? Multiple use operator: OR.
CND_NOT_RESEARCHING_TECHNOLOGY_CIVIL	Is the player faction NOT currently RESEARCHING a CIVIL TECHNOLOGY?
CND_NOT_RESEARCHING_TECHNOLOGY_ENGINEERING	Is the player faction NOT currently RESEARCHING an ENGINEERING TECHNOLOGY?
CND_NOT_RESEARCHING_TECHNOLOGY_MILITARY	Is the player faction NOT currently RESEARCHING a MILITARY TECHNOLOGY?
CND_NOT_SEASON	Is it NOT currently the key-specified SEASON? Multiple use operator: OR.
CND_NOT_SLOT_TYPE	[OBSOLETE?] Does the player faction own an instance of the key-specified slot type?
CND_NOT_TECHNOLOGY_RESEARCHED	Has the player NOT RESEARCHED the key-specified TECHNOLOGY?
CND_NOT_TRADE_NODE_GROUP_OCCUPIED	[OBSOLETE] Is the player NOT currently occupying a key-specified trade node group?
CND_NOT_TRADE_NODE_OCCUPIED	[OBSOLETE] Is the player NOT currently occupying a key-specified trade node?
CND_NOT_TRADE_WITH	Is the player faction NOT TRADING with the key-specified FACTION? Multiple use operator: AND.
CND_NOT_WAR_SHOGUN	[OBSOLETE] Is the player faction NOT at war with the Shogunate?
CND_NOT_WAR_WITH	Is the player faction NOT AT WAR with the key-specified FACTION? Multiple use operator: AND.
CND_OWNS_HOME_REGION	Does the player faction OWN their HOME REGION?
CND_OWNS_REGION	Does the player faction OWN the key-specified REGION?
CND_POLITICAL_PARTY	Does the player belong to the key-specified POLITICAL PARTY?
CND_PORT_BLOCKADED	Is the player faction currently suffering from a BLOCKADE somewhere?
CND_PROTECTED	[BROKEN?] Is the player faction currently somebody else's PROTECTORATE?
CND_RANDOM	Specify a further PERCENTAGE CHANCE that this EVENT will be GENERATED in spite of all its OPTIONS / CONDITIONS being satisfied. Used mainly for PRIORITISED EVENTS (always triggering).
CND_REALM_DIVIDE	[OBSOLETE] Has the player faction experienced realm divide yet?
CND_REBELLION	Is the player faction currently experiencing a REBELLION somewhere?
CND_RELIGION	Does the player faction belong to a key-specified RELIGION? Multiple use operator: OR.
CND_RESEARCHING_TECHNOLOGY_CIVIL	Is the player faction currently RESEARCHING a CIVIL TECHNOLOGY?
CND_RESEARCHING_TECHNOLOGY_ENGINEERING	Is the player faction currently RESEARCHING an ENGINEERING TECHNOLOGY?
CND_RESEARCHING_TECHNOLOGY_MILITARY	Is the player faction currently RESEARCHING a MILITARY TECHNOLOGY?
CND_ROUNDS_UNTIL_NEXT	Specify the number of ROUNDS that must elapse before the SAME EVENT can be GENERATED again. The EVENT cannot be UNIQUE.
CND_SEASON	Is it NOT currently the key-specified SEASON? Multiple use operator: OR.
CND_SLOT_TYPE	[OBSOLETE?] Does the player faction own an instance of the key-specified slot type?
CND_TECHNOLOGY_RESEARCHED	Has the player NOT RESEARCHED the key-specified TECHNOLOGY?
CND_TRADE_NODE_GROUP_OCCUPIED	[OBSOLETE] Is the player NOT currently occupying a key-specified trade node group?
CND_TRADE_NODE_OCCUPIED	[OBSOLETE] Is the player NOT currently occupying a key-specified trade node?
CND_TRADE_WITH	Is the player faction TRADING with the key-specified FACTION? Multiple use operator: AND.
CND_UNIQUE	Specify that the EVENT is UNIQUE. Once GENERATED, it will NEVER be GENERATED again.
CND_WAR_SHOGUN	[OBSOLETE] Is the player faction at war with the Shogunate?
CND_WAR_WITH	Is the player faction AT WAR with the key-specified FACTION? Multiple use operator: AND.
GEN_CND_AGENT	Is the EVENT TARGET CHARACTER an AGENT?
GEN_CND_AGENT_METSUKE	[OBSOLETE] Is the EVENT TARGET CHARACTER a Metsuke?
GEN_CND_AGENT_MISSIONARY	[OBSOLETE] Is the EVENT TARGET CHARACTER a Missionary?
GEN_CND_AGENT_MONK	[OBSOLETE] Is the EVENT TARGET CHARACTER a Monk?
GEN_CND_AGENT_NINJA	[OBSOLETE] Is the EVENT TARGET CHARACTER a Ninja?
GEN_CND_ALLIED_WITH_ALLY	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) ALLIED with AN ALLY of the player faction?
GEN_CND_ALLIED_WITH_ENEMY	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) ALLIED with AN ENEMY of the player faction?
GEN_CND_ALLY_SHOGUN	[OBSOLETE] Is the event target or its owner an ally of the Shogunate?
GEN_CND_ARMY_IN_REGION	Does the player have at least ONE ARMY in the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) ?
GEN_CND_BECOMING_SHOGUN	[OBSOLETE] Is the EVENT TARGET FACTION assuming control of the Shogunate?
GEN_CND_CAPITAL_REGION	Does the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED)  contain a FACTION CAPITAL?
GEN_CND_CHARACTER_BATTLE_VICTORY_PERCENT	Of the BATTLES FOUGHT by this EVENT TARGET CHARACTER, have the specified PERCENTAGE of VICTORIES been achieved?
GEN_CND_CHARACTER_NOT_TRAIT	Does the EVENT TARGET CHARACTER NOT have the key-specified TRAIT.
GEN_CND_CHARACTER_TRAIT	Does the EVENT TARGET CHARACTER have the key-specified TRAIT.
GEN_CND_CHARACTER_TYPE	Specify that a EVENT TARGET CHARACTER must be a key-specified CHARACTER TYPE.
GEN_CND_DAIMYO	[OBSOLETE] Is the event target character a Daimyo?
GEN_CND_DEFENSIVE_ALLIED	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) DEFENSIVE ALLIES with the player faction?
GEN_CND_DIPLOMACY_AVAILABLE	Can the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) engage in diplomacy with the player faction?
GEN_CND_EMBARKED	Is the EVENT TARGET embarked upon the sea? Used primarily for ARMY targets.
GEN_CND_ENEMY_OF_YOUR_ALLY_WITH_SUBCULTURE	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) an ENEMY of one of the player faction's ALLIES that belongs to the key-specified SUBCULTURE.
GEN_CND_FACTION_BUILDING_CHAIN	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) possess an instance of the key-specified BUILDING CHAIN? Multiple use operator: AND.
GEN_CND_FACTION_BUILDING_CHAIN_AVAILABLE	Can the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently CONSTRUCT the key-specified BUILDING CHAIN? Multiple use operator: AND.
GEN_CND_FACTION_BUILDING_LEVEL	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) possess an instance of the key-specified BUILDING LEVEL? Multiple use operator: AND.
GEN_CND_FACTION_COASTAL	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently hold a COASTAL REGION?
GEN_CND_FACTION_CONSTRUCTING	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently in the process of CONSTRUCTING a BUILDING?
GEN_CND_FACTION_HAS_ARMY	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently have an ARMY?
GEN_CND_FACTION_HAS_NAVY	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently have a NAVY?
GEN_CND_FACTION_LEADER	Is the EVENT TARGET CHARACTER a FACTION LEADER?
GEN_CND_FACTION_MAXED_BUILDING_CHAIN	Has the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) managed to CONSTRUCT the maximum level of the key-specified BUILDING CHAIN? Multiple use operator: AND.
GEN_CND_FACTION_NEIGHBOURS	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) a NEIGHBOUR of the player faction?
GEN_CND_FACTION_NOT_BUILDING_CHAIN	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT possess an instance of the key-specified BUILDING CHAIN? Multiple use operator: AND.
GEN_CND_FACTION_NOT_BUILDING_CHAIN_AVAILABLE	Can the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently NOT CONSTRUCT the key-specified BUILDING CHAIN? Multiple use operator: AND.
GEN_CND_FACTION_NOT_BUILDING_LEVEL	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT possess an instance of the key-specified BUILDING LEVEL? Multiple use operator: AND.
GEN_CND_FACTION_NOT_COASTAL	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently NOT hold a COASTAL REGION?
GEN_CND_FACTION_NOT_CONSTRUCTING	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently NOT in the process of CONSTRUCTING a BUILDING?
GEN_CND_FACTION_NOT_HAS_ARMY	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently NOT have an ARMY?
GEN_CND_FACTION_NOT_HAS_NAVY	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently NOT have a NAVY?
GEN_CND_FACTION_NOT_MAXED_BUILDING_CHAIN	Has the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT managed to CONSTRUCT the maximum level of the key-specified BUILDING CHAIN? Multiple use operator: AND.
GEN_CND_FACTION_NOT_NEIGHBOURS	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT a NEIGHBOUR of the player faction?
GEN_CND_FACTION_NOT_REBELLION	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT currently experiencing a REBELLION somewhere?
GEN_CND_FACTION_NOT_RECRUITING	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently NOT RECRUITING any UNITS?
GEN_CND_FACTION_NOT_RELIGION	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT belong to the key-specified RELIGION?
GEN_CND_FACTION_NOT_SAME_RELIGION	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT the same RELIGION as the player faction?
GEN_CND_FACTION_NOT_SLOT_TYPE	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT possess an instance of the key-specified SLOT TYPE. Multiple use operator: AND.
GEN_CND_FACTION_REBELLION	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently experiencing a REBELLION somewhere?
GEN_CND_FACTION_RECORD	Specify that the EVENT TARGET must be be key-specified FACTION
GEN_CND_FACTION_RECRUITING	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently RECRUITING any UNITS?
GEN_CND_FACTION_RELIGION	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) belong to the key-specified RELIGION?
GEN_CND_FACTION_SAME_RELIGION	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) the same RELIGION as the player faction?
GEN_CND_FACTION_SLOT_TYPE	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) possess an instance of the key-specified SLOT TYPE. Multiple use operator: AND.
GEN_CND_FEMALE	Is the EVENT TARGET CHARACTER a FEMALE?
GEN_CND_FORCE_HAS_EFFECT_BUNDLE	Does the EVENT TARGET MILITARY FORCE (or a MILITARY FORCE within the EVENT TARGET REGION) currently have a key-specified EFFECT BUNDLE applied to it?
GEN_CND_FORCE_IN_PROVINCE	Does the EVENT TARGET REGION contain a MILITARY FORCE belonging to the player faction? Note that despite referring to PROVINCE, I think that this only works with REGIONS - we can't yet target PROVINCES.
GEN_CND_HOME_REGION	Is the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED)  a FACTION'S HOME REGION?
GEN_CND_HUMAN	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) a HUMAN player?
GEN_CND_IN_ENEMY_REGION	Is the EVENT TARGET CHARACTER or MILITARY FORCE currently standing within an ENEMY REGION?
GEN_CND_MALE	Is the EVENT TARGET CHARACTER a MALE?
GEN_CND_MARRIED	Specify that a CHARACTER event requires a married character
GEN_CND_MAX_BATTLES	Has the EVENT TARGET CHARACTER fought NO MORE THAN the specified number of BATTLES?
GEN_CND_MAX_BATTLES_LOST	Has the EVENT TARGET CHARACTER fought NO MORE THAN the specified number of LOSING BATTLES?
GEN_CND_MAX_BATTLES_WON	Has the EVENT TARGET CHARACTER fought and NO MORE THAN the specified number of WINNING BATTLES?
GEN_CND_MAX_CHARACTER_AMBITION	Does the EVENT TARGET CHARACTER have NO MORE THAN the specified amount of AMBITION?
GEN_CND_MAX_CHARACTER_GRAVITAS	Does the EVENT TARGET CHARACTER have NO MORE THAN the specified amount of GRAVITAS?
GEN_CND_MAX_CHARACTER_LEVEL	Is the EVENT TARGET CHARACTER of RANK NO HIGHER THAN that specified?
GEN_CND_MAX_CHARACTER_LOYALTY	[OBSOLETE PENDING RE-USE FOR FAMILY GAMEPLAY] Does the EVENT TARGET CHARACTER have NO MORE THAN the specified amount of LOYALTY / FAMILY ATTITUDE?
GEN_CND_MAX_CHARACTER_PARTY_POWER_PERCENTAGE	Does the EVENT TARGET CHARACTER'S POLITICAL PARTY have NO MORE THAN the specified PERCENTAGE of POLITICAL POWER / INFLUENCE?
GEN_CND_MAX_DAIMYO_HONOUR	[OBSOLETE] Does the event target faction or owning faction's daimyo have NO MORE THAN the specified amount of honour?
GEN_CND_MAX_DIPLOMATIC_RELATION	[BROKEN?] Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) have a DIPLOMATIC STANDING of NO MORE THAN the specified amount with the player faction?
GEN_CND_MAX_FAME	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) have NO MORE THAN the specified amount of FAME / PRESTIGE / IMPERIUM?
GEN_CND_MAX_FAME_LEVEL	[OBSOLETE] Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) have NO MORE THAN the given Shogun-specific fame level?
GEN_CND_MAX_FAME_RANK	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) have a FAME / PRESTIGE / IMPERIUM LEVEL which is NO HIGHER THAN the specified amount?
GEN_CND_MAX_HIGHEST_FAME_LEVEL	Has the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) had a FAME / PRESTIGE / IMPERIUM LEVEL which is NO HIGHER THAN that specified ever during the course of a campaign?
GEN_CND_MAX_ORIGINAL_HOME_REGION_DISTANCE	Is the EVENT TARGET'S distance (in terms of NUMBER OF REGIONS) from the player faction's ORIGINAL HOME REGION NO FURTHER THAN that specified?
GEN_CND_MAX_PLAYER_BATTLES	Has the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) fought NO MORE THAN the specified number of BATTLES against the player faction?
GEN_CND_MAX_PLAYER_BATTLES_LOST	Has the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) fought NO MORE THAN the specified number of LOSING BATTLES against the player faction?
GEN_CND_MAX_PLAYER_BATTLES_WON	Has the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) fought NO MORE THAN the specified number of WINNING BATTLES against the player faction?
GEN_CND_MAX_PROVINCE_SLAVE_PERCENTAGE	Does the PROVINCE to which the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) belongs have NO MORE THAN the specified SLAVE PERCENTAGE?
GEN_CND_MAX_REGIONS_OWNED	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) OWN NO MORE THAN the specified number of REGIONS?
GEN_CND_MAX_REGION_DISTANCE	Is the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) NO FURTHER THAN the specified distance (in terms of NUMBER OF REGIONS) from the player faction's BORDERS (0 = neighbouring).
GEN_CND_MAX_REGION_PUBLIC_ORDER	[BROKEN?] Does the PROVINCE to which the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) belongs have NO MORE THAN the specified amount of PUBLIC ORDER?
GEN_CND_MAX_SETTLEMENT_UNITS	Does the SETTLEMENT within the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) contain NO MORE THAN the specified NUMBER OF UNITS.
GEN_CND_MAX_UNITS_IN_REGION	Does the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) contain NO MORE THAN the specified NUMBER OF UNITS.
GEN_CND_MILITARY_ACCESS_GIVEN	[BROKEN?] Has the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) GIVEN MILITARY ACCESS to the player faction?
GEN_CND_MILITARY_ACCESS_RECEIVED	[BROKEN?] Has the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) RECEIVED MILITARY ACCESS from the player faction?
GEN_CND_MILITARY_ALLIED	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) MILITARY ALLIES with the player faction?
GEN_CND_MIN_BATTLES	Has the EVENT TARGET CHARACTER fought AT LEAST the specified number of BATTLES?
GEN_CND_MIN_BATTLES_LOST	Has the EVENT TARGET CHARACTER fought AT LEAST the specified number of LOSING BATTLES?
GEN_CND_MIN_BATTLES_WON	Has the EVENT TARGET CHARACTER fought and AT LEAST the specified number of WINNING BATTLES?
GEN_CND_MIN_CHARACTER_AMBITION	Does the EVENT TARGET CHARACTER have AT LEAST the specified amount of AMBITION?
GEN_CND_MIN_CHARACTER_GRAVITAS	Does the EVENT TARGET CHARACTER have AT LEAST the specified amount of GRAVITAS?
GEN_CND_MIN_CHARACTER_LEVEL	Is the EVENT TARGET CHARACTER of RANK NO HIGHER THAN that specified?
GEN_CND_MIN_CHARACTER_LOYALTY	[OBSOLETE PENDING RE-USE FOR FAMILY GAMEPLAY] Does the EVENT TARGET CHARACTER have AT LEAST the specified amount of LOYALTY / FAMILY ATTITUDE?
GEN_CND_MIN_CHARACTER_PARTY_POWER_PERCENTAGE	Does the EVENT TARGET CHARACTER'S POLITICAL PARTY have AT LEAST the specified PERCENTAGE of POLITICAL POWER / INFLUENCE?
GEN_CND_MIN_DAIMYO_HONOUR	[OBSOLETE] Does the event target faction or owning faction's daimyo have AT LEAST the specified amount of honour?
GEN_CND_MIN_DIPLOMATIC_RELATION	[BROKEN?] Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) have a DIPLOMATIC STANDING of AT LEAST the specified amount with the player faction?
GEN_CND_MIN_FAME	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) have AT LEAST the specified amount of FAME / PRESTIGE / IMPERIUM?
GEN_CND_MIN_FAME_LEVEL	[OBSOLETE] Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) have AT LEAST the given Shogun-specific fame level?
GEN_CND_MIN_FAME_RANK	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) have a FAME / PRESTIGE / IMPERIUM LEVEL which is NO HIGHER THAN the specified amount?
GEN_CND_MIN_HIGHEST_FAME_LEVEL	Has the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) had a FAME / PRESTIGE / IMPERIUM LEVEL which is NO HIGHER THAN that specified ever during the course of a campaign?
GEN_CND_MIN_ORIGINAL_HOME_REGION_DISTANCE	Is the EVENT TARGET'S distance (in terms of NUMBER OF REGIONS) from the player faction's ORIGINAL HOME REGION NO FURTHER THAN that specified?
GEN_CND_MIN_PLAYER_BATTLES	Has the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) fought AT LEAST the specified number of BATTLES against the player faction?
GEN_CND_MIN_PLAYER_BATTLES_LOST	Has the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) fought AT LEAST the specified number of LOSING BATTLES against the player faction?
GEN_CND_MIN_PLAYER_BATTLES_WON	Has the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) fought AT LEAST the specified number of WINNING BATTLES against the player faction?
GEN_CND_MIN_PROVINCE_SLAVE_PERCENTAGE	Does the PROVINCE to which the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) belongs have AT LEAST the specified SLAVE PERCENTAGE?
GEN_CND_MIN_REGIONS_OWNED	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) OWN AT LEAST the specified number of REGIONS?
GEN_CND_MIN_REGION_DISTANCE	Is the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) NO FURTHER THAN the specified distance (in terms of NUMBER OF REGIONS) from the player faction's BORDERS (0 = neighbouring).
GEN_CND_MIN_REGION_PUBLIC_ORDER	[BROKEN?] Does the PROVINCE to which the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) belongs have AT LEAST the specified amount of PUBLIC ORDER?
GEN_CND_MIN_SETTLEMENT_UNITS	Does the SETTLEMENT within the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) contain AT LEAST the specified NUMBER OF UNITS.
GEN_CND_MIN_UNITS_IN_REGION	Does the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) contain AT LEAST the specified NUMBER OF UNITS.
GEN_CND_NEUTRAL	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NEUTRAL towards the player faction?
GEN_CND_NOT_ALLIED_WITH_ALLY	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT ALLIED with AN ALLY of the player faction?
GEN_CND_NOT_ALLIED_WITH_ENEMY	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT ALLIED with AN ENEMY of the player faction?
GEN_CND_NOT_ALLY_SHOGUN	[OBSOLETE] Is the event target or its owner NOT an ally of the Shogunate?
GEN_CND_NOT_ARMY_IN_REGION	Does the player faction NOT have at least ONE ARMY in the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) ?
GEN_CND_NOT_BECOMING_SHOGUN	[OBSOLETE] Is the EVENT TARGET FACTION NOT assuming control of the Shogunate?
GEN_CND_NOT_CAPITAL_REGION	Does the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) NOT contain a FACTION CAPITAL?
GEN_CND_NOT_CHARACTER_TYPE	Specify that a EVENT TARGET CHARACTER must NOT be a key-specified CHARACTER TYPE.
GEN_CND_NOT_DAIMYO	[OBSOLETE] Is the event target character not a Daimyo?
GEN_CND_NOT_DEFENSIVE_ALLIED	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT DEFENSIVE ALLIES with the player faction?
GEN_CND_NOT_DIPLOMACY_AVAILABLE	Can the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT engage in DIPLOMACY with the player faction?
GEN_CND_NOT_EMBARKED	Is the EVENT TARGET NOT embarked upon the sea? Used primarily for ARMY targets.
GEN_CND_NOT_ENEMY_OF_YOUR_ALLY_WITH_SUBCULTURE	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET)NOT an ENEMY of one of the player faction's ALLIES that belongs to the key-specified SUBCULTURE.
GEN_CND_NOT_FACTION_LEADER	Is the EVENT TARGET CHARACTER NOT a FACTION LEADER?
GEN_CND_NOT_FACTION_RECORD	Specify that the EVENT TARGET must not be be key-specified FACTION
GEN_CND_NOT_FORCE_HAS_EFFECT_BUNDLE	Does the EVENT TARGET MILITARY FORCE (or a MILITARY FORCE within the EVENT TARGET REGION) NOT currently have a key-specified EFFECT BUNDLE applied to it?
GEN_CND_NOT_FORCE_IN_PROVINCE	Does the EVENT TARGET REGION NOT contain a MILITARY FORCE belonging to the player faction? Note that despite referring to PROVINCE, I think that this only works with REGIONS - we can't yet target PROVINCES.
GEN_CND_NOT_HOME_REGION	Is the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) NOT a FACTION'S HOME REGION?
GEN_CND_NOT_HUMAN	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT a HUMAN player?
GEN_CND_NOT_IN_ENEMY_REGION	Is the EVENT TARGET CHARACTER or MILITARY FORCE NOT currently standing within an ENEMY REGION?
GEN_CND_NOT_MARRIED	Specify that a CHARACTER event requires a not married character
GEN_CND_NOT_MILITARY_ACCESS_GIVEN	[BROKEN?] Has the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT GIVEN MILITARY ACCESS to the player faction?
GEN_CND_NOT_MILITARY_ACCESS_RECEIVED	[BROKEN?] Has the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT RECEIVED MILITARY ACCESS from the player faction?
GEN_CND_NOT_MILITARY_ALLIED	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT MILITARY ALLIES with the player faction?
GEN_CND_NOT_NEUTRAL	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT NEUTRAL towards the player faction?
GEN_CND_NOT_OWNS	Does the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) NOT belong to the player faction?
GEN_CND_NOT_OWNS_HOME_REGION	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT currently OWN their HOME REGION?
GEN_CND_NOT_OWNS_REGION	Does the REGION where an EVENT TARGET CHARACTER or MILITARY FORCE is located NOT belong to the player faction?
GEN_CND_NOT_PLAYER_ARMY_IN_ANY_REGION	Does the player faction NOT currently have an ARMY within a REGION belonging to the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET)?
GEN_CND_NOT_POLITICAL_PARTY	Does the EVENT TARGET CHARACTER NOT belong to the key-specified POLITICAL PARTY?
GEN_CND_NOT_PORT_BLOCKADED	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT currently experiencing a BLOCKADE?
GEN_CND_NOT_PROTECTED	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT currently a PROTECTORATE / CLIENT / VASSAL / SATRAPY of the player faction?
GEN_CND_NOT_PROTECTOR	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT currently the OVERLORD of the player faction?
GEN_CND_NOT_PROVINCE_COMPLETE	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT belong to a PROVINCE which is ENTIRELY OWNED by the player faction?
GEN_CND_NOT_REGION	Is the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) NOT the key-specified REGION? Multiple use operator: UNSURE! Should be AND, I guess?
GEN_CND_NOT_REGION_HAS_EFFECT_BUNDLE	Does the EVENT TARGET REGION (or a REGION where the EVENT TARGET MILITARY FORCE IS LOCATED) NOT currently have a key-specified EFFECT BUNDLE applied to it?
GEN_CND_NOT_REGION_NEIGHBOURING_HAS_EFFECT_BUNDLE	Does the EVENT TARGET REGION (or a REGION where the EVENT TARGET IS LOCATED) NOT have a NEIGHBOURING REGION which currently has a key-specified EFFECT BUNDLE applied to it?
GEN_CND_NOT_REGION_NEIGHBOURS	Is the EVENT TARGET REGION (or a REGION where the EVENT TARGET IS LOCATED) NOT NEIGHBOURING the player faction?
GEN_CND_NOT_RESEARCHABLE	Is the EVENT TARGET TECHNOLOGY NOT currently RESEARCHABLE?
GEN_CND_NOT_RESEARCHED	Has the EVENT TARGET TECHNOLOGY NOT yet been RESEARCHED?
GEN_CND_NOT_RESEARCHING	Is the EVENT TARGET TECHNOLOGY NOT currently being RESEARCHED?
GEN_CND_NOT_SHOGUN	[OBSOLETE] Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT currently rule the shogunate?
GEN_CND_NOT_SLOT_TYPE	[OBSOLETE?] Is the EVENT TARGET SLOT NOT of the key-specified SLOT TYPE?
GEN_CND_NOT_STANCE	Is the EVENT TARGET MILITARY FORCE NOT currently in the key-specified STANCE?
GEN_CND_NOT_TARGET_ARMY_IN_ANY_REGION	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT currently have an ARMY in one of the player faction's REGIONS?
GEN_CND_NOT_TARGET_ARMY_NEAR_ORIGINAL_HOME_REGION	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT currently have an ARMY in the palyer faction's HOME REGION or one of its NEIGHBOURING REGIONS?
GEN_CND_NOT_TRADE	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT TRADING with the player faction?
GEN_CND_NOT_VISIBLE	Can the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT be seen by the player faction?
GEN_CND_NOT_WAR	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT AT WAR with the player faction?
GEN_CND_NOT_WAR_SHOGUN	[OBSOLETE] Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT AT WAR with the Shogunate?
GEN_CND_NOT_WAR_WITH_ALLY	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT AT WAR with an ALLY of the player faction?
GEN_CND_NOT_WAR_WITH_ENEMY	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) NOT AT WAR with an ENEMY of the player faction?
GEN_CND_OWNS	Does the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) belong to the player faction?
GEN_CND_OWNS_HOME_REGION	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently OWN their HOME REGION?
GEN_CND_OWNS_REGION	Does the REGION where an EVENT TARGET CHARACTER or MILITARY FORCE is located belong to the player faction?
GEN_CND_PLAYER_ARMY_IN_ANY_REGION	Does the player faction currently have an ARMY within a REGION belonging to the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET)?
GEN_CND_POLITICAL_PARTY	Does the EVENT TARGET CHARACTER belong to the key-specified POLITICAL PARTY?
GEN_CND_PORT_BLOCKADED	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently experiencing a BLOCKADE?
GEN_CND_PROTECTED	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently a PROTECTORATE / CLIENT / VASSAL / SATRAPY of the player faction?
GEN_CND_PROTECTOR	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently the OVERLORD of the player faction?
GEN_CND_PROVINCE_COMPLETE	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) belong to a PROVINCE which is ENTIRELY OWNED by the player faction?
GEN_CND_REGION	Is the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) the key-specified REGION? Multiple use operator: UNSURE! Should be OR, I guess?
GEN_CND_REGION_ANY_OF	Is the EVENT TARGET REGION one of the many key-specified (and semicolon-separated) REGIONS? OPTION_VALUE example: rom_italia_etruria; rom_italia_latium; rom_italia_picenum; etc...
GEN_CND_REGION_BUILDING_CHAIN	Does the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) possess an instance of the key-specified BUILDING CHAIN? Multiple use operator: AND.
GEN_CND_REGION_BUILDING_CHAIN_AVAILABLE	Can the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) currently CONSTRUCT the key-specified BUILDING CHAIN? Multiple use operator: AND.
GEN_CND_REGION_BUILDING_LEVEL	Does the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) possess an instance of the key-specified BUILDING LEVEL? Multiple use operator: AND.
GEN_CND_REGION_COASTAL	Is the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) a COASTAL REGION?
GEN_CND_REGION_CONSTRUCTING	Is the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) currently in the process of CONSTRUCTING a BUILDING?
GEN_CND_REGION_CONTAINS_OFFICIAL	Does the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) currently contain a CHARACTER with the ket-defined MINISTERIAL POSITION.
GEN_CND_REGION_ENEMY_NEIGHBOURS	Is the EVENT TARGET REGION (or a REGION where the EVENT TARGET MILITARY FORCE IS LOCATED) NEIGHBOURING an ENEMY FACTION?
GEN_CND_REGION_HAS_EFFECT_BUNDLE	Does the EVENT TARGET REGION (or a REGION where the EVENT TARGET MILITARY FORCE IS LOCATED) currently have a key-specified EFFECT BUNDLE applied to it?
GEN_CND_REGION_MAXED_BUILDING_CHAIN	Has the EVENT TARGET REGION (or a REGION where the EVENT TARGET IS LOCATED)  managed to CONSTRUCT the maximum level of the key-specified BUILDING CHAIN? Multiple use operator: AND.
GEN_CND_REGION_MAX_FACTION_RELIGION_RATIO	Does the EVENT TARGET REGION (or a REGION where the EVENT TARGET MILITARY FORCE IS LOCATED) contain a ratio of the player faction's RELIGION which is NO GREATER THAN that specified?
GEN_CND_REGION_MIN_FACTION_RELIGION_RATIO	Does the EVENT TARGET REGION (or a REGION where the EVENT TARGET MILITARY FORCE IS LOCATED) contain a ratio of the player faction's RELIGION which is AT LEAST that specified?
GEN_CND_REGION_NEIGHBOURING_HAS_EFFECT_BUNDLE	Does the EVENT TARGET REGION (or a REGION where the EVENT TARGET IS LOCATED) have a NEIGHBOURING REGION which currently has a key-specified EFFECT BUNDLE applied to it?
GEN_CND_REGION_NEIGHBOURS	Is the EVENT TARGET REGION (or a REGION where the EVENT TARGET IS LOCATED) NEIGHBOURING the player faction?
GEN_CND_REGION_NOT_ALL_OF	Is the EVENT TARGET REGION NOT one of the many key-specified (and semicolon-separated) REGIONS? OPTION_VALUE example: rom_italia_etruria; rom_italia_latium; rom_italia_picenum; etc...
GEN_CND_REGION_NOT_BUILDING_CHAIN	Does the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) NOT possess an instance of the key-specified BUILDING CHAIN? Multiple use operator: AND.
GEN_CND_REGION_NOT_BUILDING_CHAIN_AVAILABLE	Can the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) NOT currently CONSTRUCT the key-specified BUILDING CHAIN? Multiple use operator: AND.
GEN_CND_REGION_NOT_BUILDING_LEVEL	Does the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) NOT possess an instance of the key-specified BUILDING LEVEL? Multiple use operator: AND.
GEN_CND_REGION_NOT_COASTAL	Is the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) NOT a COASTAL REGION?
GEN_CND_REGION_NOT_CONSTRUCTING	Is the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) NOT currently in the process of CONSTRUCTING a BUILDING?
GEN_CND_REGION_NOT_CONTAINS_OFFICIAL	Does the EVENT TARGET REGION (or the REGION where the EVENT TARGET IS LOCATED) NOT currently contain a CHARACTER with the ket-defined MINISTERIAL POSITION.
GEN_CND_REGION_NOT_ENEMY_NEIGHBOURS	Is the EVENT TARGET REGION (or a REGION where the EVENT TARGET MILITARY FORCE IS LOCATED) NOT NEIGHBOURING an ENEMY FACTION?
GEN_CND_REGION_NOT_MAXED_BUILDING_CHAIN	Has the EVENT TARGET REGION (or a REGION where the EVENT TARGET IS LOCATED) NOT managed to CONSTRUCT the maximum level of the key-specified BUILDING CHAIN? Multiple use operator: AND.
GEN_CND_REGION_NOT_REBELLION	Is the EVENT TARGET REGION (or a REGION where the EVENT TARGET IS LOCATED) NOT currently experiencing a REBELLION?
GEN_CND_REGION_NOT_RECRUITING	Is the EVENT TARGET REGION (or a REGION where the EVENT TARGET IS LOCATED) NOT currently RECRUITING any UNITS?
GEN_CND_REGION_NOT_RELIGION	Does the EVENT TARGET REGION (or a REGION where the EVENT TARGET IS LOCATED) NOT belong to the key-specified RELIGION?
GEN_CND_REGION_NOT_SAME_RELIGION	Does the EVENT TARGET REGION (or a REGION where the EVENT TARGET IS LOCATED) NOT belong to the SAME RELIGION as the player faction?
GEN_CND_REGION_NOT_SLOT_TYPE	Does the EVENT TARGET REGION (or a REGION where the EVENT TARGET IS LOCATED) NOT possess an instance of the key-specified SLOT TYPE. Multiple use operator: AND.
GEN_CND_REGION_REBELLION	Is the EVENT TARGET REGION (or a REGION where the EVENT TARGET IS LOCATED) currently experiencing a REBELLION?
GEN_CND_REGION_RECRUITING	Is the EVENT TARGET REGION (or a REGION where the EVENT TARGET IS LOCATED)  currently RECRUITING any UNITS?
GEN_CND_REGION_RELIGION	Does the EVENT TARGET REGION (or a REGION where the EVENT TARGET IS LOCATED) belong to the key-specified RELIGION?
GEN_CND_REGION_SAME_RELIGION	Does the EVENT TARGET REGION (or a REGION where the EVENT TARGET IS LOCATED) belong to the SAME RELIGION as the player faction?
GEN_CND_REGION_SLOT_TYPE	Does the EVENT TARGET REGION (or a REGION where the EVENT TARGET IS LOCATED) possess an instance of the key-specified SLOT TYPE. Multiple use operator: AND.
GEN_CND_RESEARCHABLE	Is the EVENT TARGET TECHNOLOGY currently RESEARCHABLE?
GEN_CND_RESEARCHED	Has the EVENT TARGET TECHNOLOGY been RESEARCHED?
GEN_CND_RESEARCHING	Is the EVENT TARGET TECHNOLOGY currently being RESEARCHED?
GEN_CND_SELF	Specify that a event targets the owners faction
GEN_CND_SHOGUN	[OBSOLETE] Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently rule the shogunate?
GEN_CND_SLOT_TYPE	[OBSOLETE?] Is the EVENT TARGET SLOT of the key-specified SLOT TYPE?
GEN_CND_STANCE	Is the EVENT TARGET MILITARY FORCE currently in the key-specified STANCE?
GEN_CND_TARGET_ARMY_IN_ANY_REGION	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently have an ARMY in one of the player faction's REGIONS?
GEN_CND_TARGET_ARMY_NEAR_ORIGINAL_HOME_REGION	Does the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) currently have an ARMY in the palyer faction's HOME REGION or one of its NEIGHBOURING REGIONS?
GEN_CND_TECHNOLOGY_CIVIL	Is the EVENT TARGET TECHNOLOGY a CIVIL TECHNOLOGY?
GEN_CND_TECHNOLOGY_ENGINEERING	Is the EVENT TARGET TECHNOLOGY an ENGINEERING TECHNOLOGY?
GEN_CND_TECHNOLOGY_MILITARY	Is the EVENT TARGET TECHNOLOGY a MILITARY TECHNOLOGY?
GEN_CND_TECHNOLOGY_NOT_CIVIL	Is the EVENT TARGET TECHNOLOGY NOT a CIVIL TECHNOLOGY?
GEN_CND_TECHNOLOGY_NOT_ENGINEERING	Is the EVENT TARGET TECHNOLOGY NOT an ENGINEERING TECHNOLOGY?
GEN_CND_TECHNOLOGY_NOT_MILITARY	Is the EVENT TARGET TECHNOLOGY NOT a MILITARY TECHNOLOGY?
GEN_CND_TRADE	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) TRADING with the player faction?
GEN_CND_VISIBLE	Can the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) be seen by the player faction?
GEN_CND_WAR	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) AT WAR with the player faction?
GEN_CND_WAR_SHOGUN	[OBSOLETE] Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) AT WAR with the Shogunate?
GEN_CND_WAR_WITH_ALLY	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) AT WAR with an ALLY of the player faction?
GEN_CND_WAR_WITH_ENEMY	Is the EVENT TARGET FACTION (or the FACTION that OWNS the EVENT TARGET) AT WAR with an ENEMY of the player faction?
GEN_TARGET_CHARACTER	Specifies that the EVENT TARGET must be a CHARACTER. (May not be used in conjunction with other GEN_TARGET OPTIONS. All EVENTS must have a GEN_TARGET OPTION.)
GEN_TARGET_FACTION	Specifies that the EVENT TARGET must be a FACTION. (May not be used in conjunction with other GEN_TARGET OPTIONS. All EVENTS must have a GEN_TARGET OPTION.)
GEN_TARGET_MILITARY_FORCE	Specifies that the EVENT TARGET must be a MILITARY FORCE. (May not be used in conjunction with other GEN_TARGET OPTIONS. All EVENTS must have a GEN_TARGET OPTION.)
GEN_TARGET_NONE	Specifies that there is NO EVENT TARGET. (May not be used in conjunction with other GEN_TARGET OPTIONS. All EVENTS must have a GEN_TARGET OPTION.)
GEN_TARGET_PARENT	Specifies that the EVENT TARGET is INHERITED from the PARENT EVENT. This is only applicable to FOLLOWUP EVENTS. (May not be used in conjunction with other GEN_TARGET OPTIONS. All EVENTS must have a GEN_TARGET OPTION.)
GEN_TARGET_POLITICAL_EVENT	Specifies that the EVENT TARGET comes from a political event (CAN ONLY BE USED WITH POLITICAL EVENT GENERATED EVENTS)
GEN_TARGET_POLITICAL_EVENT_ACTOR	Specifies that the EVENT TARGET must be an actor in a political event (CAN ONLY BE USED WITH POLITICAL EVENT GENERATED EVENTS)
GEN_TARGET_POLITICAL_EVENT_TARGET	Specifies that the EVENT TARGET must be a target in a political event (CAN ONLY BE USED WITH POLITICAL EVENT GENERATED EVENTS)
GEN_TARGET_REGION	Specifies that the EVENT TARGET must be a REGION. (May not be used in conjunction with other GEN_TARGET OPTIONS. All EVENTS must have a GEN_TARGET OPTION.)
GEN_TARGET_SETTLEMENT	Specifies that the EVENT TARGET must be a SETTLEMENT. (May not be used in conjunction with other GEN_TARGET OPTIONS. All EVENTS must have a GEN_TARGET OPTION.)
GEN_TARGET_SLOT	Specifies that the EVENT TARGET must be a SLOT. (May not be used in conjunction with other GEN_TARGET OPTIONS. All EVENTS must have a GEN_TARGET OPTION.)
GEN_TARGET_TECHNOLOGY	Specifies that the EVENT TARGET must be a TECHNOLOGY. (May not be used in conjunction with other GEN_TARGET OPTIONS. All EVENTS must have a GEN_TARGET OPTION.)
VAR_CHANCE	Specifies the relative chance that an EVENT that satisfies its EVENT OPTIONS will be GENERATED. A WEIGHTING, NOT an actual PERCENTAGE.
VAR_DELAY_MAX	Specifies the MAXIMUM number of turns before a FOLLOWUP EVENT will be triggered after its PARENT EVENT has fired. I *think* this is a required parameter.
VAR_DELAY_MIN	Specifies the MINIMUM number of turns before a FOLLOWUP EVENT will be triggered after its PARENT EVENT has fired. I *think* this is a required parameter.
VAR_FOLLOWUP_CHANCE	Specifies the PERCENTAGE CHANCE of GENERATING one of the associated FOLLOWUP EVENTS.
VAR_MISSION_LENGTH_ADDITIONAL_MAX	Specifies the MAXIMUM number of turns which may be RANDOMLY ADDED to a MISSION turn allowance.
VAR_MISSION_LENGTH_ADDITIONAL_MIN	Specifies the MINIMUM number of turns which must be RANDOMLY ADDED to a MISSION turn allowance.
VAR_MISSION_LENGTH_MAX	Specifies a MISSION's MAXIMUM turn allowance.
VAR_MISSION_LENGTH_MIN	Specifies a MISSION's MINIMUM turn allowance.
VAR_MISSION_LENGTH_MOD_EASY	Multiplies the final MISSION turn allowance for EASY CAMPAIGNS. MUST have a decimal (1.0, 1.5, 2.0, etc).
VAR_MISSION_LENGTH_MOD_HARD	Multiplies the final MISSION turn allowance for HARD CAMPAIGNS.  MUST have a decimal (1.0, 1.5, 2.0, etc).
VAR_MISSION_LENGTH_MOD_NORMAL	Multiplies the final MISSION turn allowance for NORMAL CAMPAIGNS.  MUST have a decimal (1.0, 1.5, 2.0, etc).
VAR_MISSION_LENGTH_MOD_VERY_HARD	Multiplies the final MISSION turn allowance for VERY HARD and LEGENDARY CAMPAIGNS.  MUST have a decimal (1.0, 1.5, 2.0, etc).
VAR_OBJECTIVE_AGENT	Specify that a CHARACTER-RELATED MISSION OBJECTIVE must be a key-specified AGENT.
VAR_OBJECTIVE_ARMIES_ONLY	Specify that an FORCE-RELATED MISSION OBJECTIVE must be an ARMY.
VAR_OBJECTIVE_BUILDING_CHAIN	Specify that a BUILDING-RELATED MISSION OBJECTIVE must be a key-specified BUILDING CHAIN.
VAR_OBJECTIVE_BUILDING_LEVEL	Specify that a BUILDING-RELATED MISSION OBJECTIVE must be a key-specified BUILDING LEVEL.
VAR_OBJECTIVE_CUSTOM_COMPLETION_STATUS	Specify a localized key for a custom mission objective string.
VAR_OBJECTIVE_INVADING_ONLY	Specify that a FORCE-RELATED MISSION OBJECTIVE must be invading the PLAYER FACTION's REGIONS.
VAR_OBJECTIVE_NAVIES_ONLY	Specify that an FORCE-RELATED MISSION OBJECTIVE must be an NAVY.
VAR_OBJECTIVE_RELIGION_PCT	Specify that a RELIGION-RELATED MISSION OBJECTIVE must be the specified percentage of the PLAYER FACTION'S RELIGION.
VAR_OBJECTIVE_REQUIRES_VICTORY	Specify that a FORCE-RELATED MISSION OBJECTIVE must conclude in a VICTORY.
VAR_OBJECTIVE_TECH_CATEGORY	Specify that a TECHNOLOGY-RELATED MISSION OBJECTIVE must involve research of a TECHNOLOGY from the key-specified CATEGORY.
VAR_OBJECTIVE_UNIT	Specify that a RECRUITMENT-RELATED MISSION OBJECTIVE must involve recruitment of a key-specified UNIT.
VAR_OBJECTIVE_UNIT_CASTE	Specify that a RECRUITMENT-RELATED MISSION OBJECTIVE must involve recruitment of a UNIT from a key-specified CASTE.
VAR_OBJECTIVE_UNIT_CATEGORY	Specify that a RECRUITMENT-RELATED MISSION OBJECTIVE must involve recruitment of a UNIT from a key-specified CATEGORY.
VAR_OBJECTIVE_UNIT_CLASS	Specify that a RECRUITMENT-RELATED MISSION OBJECTIVE must involve recruitment of a UNIT from a key-specified CLASS.

```