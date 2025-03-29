---
title: schema
summary: A brief description of my document.
---

# Tables
Database schema extracted from RPFM.
Required a few scripts to setup but seems pretty usable.



  
## _kv_experience_bonuses_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| value | False | F32 |  |  |  |
  
## _kv_fatigue_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| value | False | F32 |  |  |  |
  
## _kv_key_buildings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| value | False | F32 |  |  |  |
  
## _kv_morale_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| value | False | F32 |  |  |  |
  
## _kv_naval_morale_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| value | False | F32 |  |  |  |
  
## _kv_rules_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| value | False | F32 |  |  |  |
  
## abilities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| value | False | F32 |  |  |  |
  
## achievements_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| value | False | F32 |  |  |  |
  
## action_results_additional_outcomes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| outcome | False | StringU8 |  | [action_results_additional_outcomes_enums_tables](#action_results_additional_outcomes_enums_tables) | key |
| action_result_key | False | StringU8 |  | [action_results_tables](#action_results_tables) | key |
| value | False | F32 |  |  |  |
| effect_record | False | OptionalStringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope_record | False | OptionalStringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| key | True | StringU8 |  |  |  |
| opportune_failure_weighting | False | OptionalStringU8 |  |  |  |
| authority_value_coefficient | False | F32 | final_value = value + (authority_value_coefficient * agent.attribute_level(ATTRIBUTE_AUTHORITY) |  |  |
| subterfuge_value_coefficient | False | F32 | final_value = value + (subterfuge_value_coefficient * agent.attribute_level(ATTRIBUTE_SUBTERFUGE) |  |  |
| zeal_value_coefficient | False | F32 | final_value = value + (zeal_value_coefficient * agent.attribute_level(ATTRIBUTE_ZEAL) |  |  |
  
## action_results_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| outcome | False | StringU8 |  | [action_results_additional_outcomes_enums_tables](#action_results_additional_outcomes_enums_tables) | key |
| action_result_key | False | StringU8 |  | [action_results_tables](#action_results_tables) | key |
| value | False | F32 |  |  |  |
| effect_record | False | OptionalStringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope_record | False | OptionalStringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| key | True | StringU8 |  |  |  |
| opportune_failure_weighting | False | OptionalStringU8 |  |  |  |
| authority_value_coefficient | False | F32 | final_value = value + (authority_value_coefficient * agent.attribute_level(ATTRIBUTE_AUTHORITY) |  |  |
| subterfuge_value_coefficient | False | F32 | final_value = value + (subterfuge_value_coefficient * agent.attribute_level(ATTRIBUTE_SUBTERFUGE) |  |  |
| zeal_value_coefficient | False | F32 | final_value = value + (zeal_value_coefficient * agent.attribute_level(ATTRIBUTE_ZEAL) |  |  |
  
## advice_info_texts_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| outcome | False | StringU8 |  | [action_results_additional_outcomes_enums_tables](#action_results_additional_outcomes_enums_tables) | key |
| action_result_key | False | StringU8 |  | [action_results_tables](#action_results_tables) | key |
| value | False | F32 |  |  |  |
| effect_record | False | OptionalStringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope_record | False | OptionalStringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| key | True | StringU8 |  |  |  |
| opportune_failure_weighting | False | OptionalStringU8 |  |  |  |
| authority_value_coefficient | False | F32 | final_value = value + (authority_value_coefficient * agent.attribute_level(ATTRIBUTE_AUTHORITY) |  |  |
| subterfuge_value_coefficient | False | F32 | final_value = value + (subterfuge_value_coefficient * agent.attribute_level(ATTRIBUTE_SUBTERFUGE) |  |  |
| zeal_value_coefficient | False | F32 | final_value = value + (zeal_value_coefficient * agent.attribute_level(ATTRIBUTE_ZEAL) |  |  |
  
## advice_levels_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| advice_thread | False | StringU8 |  | [advice_threads_tables](#advice_threads_tables) | thread |
| advice_thread_level | False | I32 |  |  |  |
| points_needed | False | I32 |  |  |  |
| game_area | False | StringU8 |  |  |  |
| category | False | StringU8 |  |  |  |
| sub_category | False | StringU8 |  |  |  |
| max_repeat_count | False | I32 |  |  |  |
| repeat_interval | False | I32 |  |  |  |
| pause_battle | False | Boolean | Does this advice pause the battle |  |  |
| priority_level | False | I32 |  |  |  |
| high_verbosity_only | False | Boolean |  |  |  |
| locatable | False | Boolean |  |  |  |
| parameter | False | StringU8 |  |  |  |
| on_display_script | False | OptionalStringU8 |  |  |  |
| on_click_script | False | OptionalStringU8 |  |  |  |
| suppressible | False | Boolean |  |  |  |
| uninhibitable | False | Boolean |  |  |  |
| audio_clip | False | StringU8 | Audio to play for this advice |  |  |
| advisor_name | False | StringU8 | Name of advisor, determines advisor that presents advice | [advisors_tables](#advisors_tables) | advisor_name |
| for_loading_screen | False | Boolean | Specifies whether this bit of advice text should be shown in loading screen AS WELL. |  |  |
| movie_link | False | OptionalStringU8 | Link to a movie url in encyclopedia to play |  |  |
  
## advice_threads_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| advice_thread | False | StringU8 |  | [advice_threads_tables](#advice_threads_tables) | thread |
| advice_thread_level | False | I32 |  |  |  |
| points_needed | False | I32 |  |  |  |
| game_area | False | StringU8 |  |  |  |
| category | False | StringU8 |  |  |  |
| sub_category | False | StringU8 |  |  |  |
| max_repeat_count | False | I32 |  |  |  |
| repeat_interval | False | I32 |  |  |  |
| pause_battle | False | Boolean | Does this advice pause the battle |  |  |
| priority_level | False | I32 |  |  |  |
| high_verbosity_only | False | Boolean |  |  |  |
| locatable | False | Boolean |  |  |  |
| parameter | False | StringU8 |  |  |  |
| on_display_script | False | OptionalStringU8 |  |  |  |
| on_click_script | False | OptionalStringU8 |  |  |  |
| suppressible | False | Boolean |  |  |  |
| uninhibitable | False | Boolean |  |  |  |
| audio_clip | False | StringU8 | Audio to play for this advice |  |  |
| advisor_name | False | StringU8 | Name of advisor, determines advisor that presents advice | [advisors_tables](#advisors_tables) | advisor_name |
| for_loading_screen | False | Boolean | Specifies whether this bit of advice text should be shown in loading screen AS WELL. |  |  |
| movie_link | False | OptionalStringU8 | Link to a movie url in encyclopedia to play |  |  |
  
## advisors_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| advisor_name | True | StringU8 |  |  |  |
| advisor_icon_path | False | StringU16 | This path specifies what model will get loaded to advisor |  |  |
  
## agent_action_message_events_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| critical_failure | False | OptionalStringU8 |  | [message_events_tables](#message_events_tables) | event |
| critical_success | False | OptionalStringU8 |  | [message_events_tables](#message_events_tables) | event |
| failure | False | OptionalStringU8 |  | [message_events_tables](#message_events_tables) | event |
| key | True | StringU8 |  |  |  |
| opportune_failure | False | OptionalStringU8 |  | [message_events_tables](#message_events_tables) | event |
| success | False | OptionalStringU8 |  | [message_events_tables](#message_events_tables) | event |
  
## agent_actions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| critical_failure | False | OptionalStringU8 |  | [message_events_tables](#message_events_tables) | event |
| critical_success | False | OptionalStringU8 |  | [message_events_tables](#message_events_tables) | event |
| failure | False | OptionalStringU8 |  | [message_events_tables](#message_events_tables) | event |
| key | True | StringU8 |  |  |  |
| opportune_failure | False | OptionalStringU8 |  | [message_events_tables](#message_events_tables) | event |
| success | False | OptionalStringU8 |  | [message_events_tables](#message_events_tables) | event |
  
## agent_attributes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## agent_culture_details_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## agent_localisations_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## agent_string_faction_overrides_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## agent_string_subculture_overrides_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## agent_subculture_gender_overrides_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| agent | True | StringU8 |  | [agents_tables](#agents_tables) | key |
| gender | True | StringU8 |  | [genders_tables](#genders_tables) | gender |
| subculture | True | StringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## agent_to_agent_abilities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| agent | True | StringU8 |  | [agents_tables](#agents_tables) | key |
| gender | True | StringU8 |  | [genders_tables](#genders_tables) | gender |
| subculture | True | StringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## agent_to_agent_attributes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| attribute | True | StringU8 |  | [agent_attributes_tables](#agent_attributes_tables) | key |
| agent | True | StringU8 |  | [agents_tables](#agents_tables) | key |
| default_value | False | I32 |  |  |  |
  
## agent_uniforms_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| attribute | True | StringU8 |  | [agent_attributes_tables](#agent_attributes_tables) | key |
| agent | True | StringU8 |  | [agents_tables](#agents_tables) | key |
| default_value | False | I32 |  |  |  |
  
## agents_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| attribute | True | StringU8 |  | [agent_attributes_tables](#agent_attributes_tables) | key |
| agent | True | StringU8 |  | [agents_tables](#agents_tables) | key |
| default_value | False | I32 |  |  |  |
  
## aide_de_camp_speeches_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| attribute | True | StringU8 |  | [agent_attributes_tables](#agent_attributes_tables) | key |
| agent | True | StringU8 |  | [agents_tables](#agents_tables) | key |
| default_value | False | I32 |  |  |  |
  
## ancillaries_categories_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| attribute | True | StringU8 |  | [agent_attributes_tables](#agent_attributes_tables) | key |
| agent | True | StringU8 |  | [agents_tables](#agents_tables) | key |
| default_value | False | I32 |  |  |  |
  
## ancillaries_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| attribute | True | StringU8 |  | [agent_attributes_tables](#agent_attributes_tables) | key |
| agent | True | StringU8 |  | [agents_tables](#agents_tables) | key |
| default_value | False | I32 |  |  |  |
  
## ancillary_included_subcultures_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| ancillary | True | StringU8 |  | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
| subculture | True | StringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## ancillary_info_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| ancillary | True | StringU8 |  |  |  |
  
## ancillary_to_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| ancillary | True | StringU8 |  | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| value | False | F32 |  |  |  |
  
## ancillary_to_included_agents_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| ancillary | True | StringU8 |  | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
| agent | True | StringU8 |  | [agents_tables](#agents_tables) | key |
  
## ancillary_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| type | True | StringU8 |  |  |  |
| ui_icon | False | StringU8 |  |  |  |
  
## anim_reference_poses_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| path | False | StringU8 |  |  |  |
| root_node | False | StringU8 |  |  |  |
  
## animals_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| animation | False | StringU8 |  | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| armour | False | OptionalStringU8 |  | [unit_armour_types_tables](#unit_armour_types_tables) | key |
| charge_bonus | False | I32 |  |  |  |
| entity | False | StringU8 |  | [battle_entities_tables](#battle_entities_tables) | key |
| key | True | StringU8 |  |  |  |
| melee_attack | False | I32 |  |  |  |
| melee_defence | False | I32 |  |  |  |
  
## armed_citizenry_unit_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| unit_group | True | StringU8 |  |  |  |
  
## armed_citizenry_units_to_unit_groups_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | I64 |  |  |  |
| priority | False | I32 |  |  |  |
| unit | False | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
| unit_group | False | StringU8 |  | [armed_citizenry_unit_groups_tables](#armed_citizenry_unit_groups_tables) | unit_group |
  
## audio_campaign_building_enums_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## audio_projectiles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## audio_vo_actor_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## banditry_events_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## battle_animations_table_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| skeleton | False | StringU8 | This creates an AGF dependency. | [battle_skeletons_tables](#battle_skeletons_tables) | name |
  
## battle_autoresolver_balances_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| melee_potential_multiplier | False | F32 |  |  |  |
| missile_potential_multiplier | False | F32 |  |  |  |
| source_unit_class | True | StringU8 |  | [unit_class_tables](#unit_class_tables) | key |
| target_unit_class | True | StringU8 |  | [unit_class_tables](#unit_class_tables) | key |
  
## battle_cameras_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| melee_potential_multiplier | False | F32 |  |  |  |
| missile_potential_multiplier | False | F32 |  |  |  |
| source_unit_class | True | StringU8 |  | [unit_class_tables](#unit_class_tables) | key |
| target_unit_class | True | StringU8 |  | [unit_class_tables](#unit_class_tables) | key |
  
## battle_cinematic_event_categories_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## battle_cinematic_events_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| filename | False | StringU8 | Name of camera.txt file that specifies shots to be used |  |  |
| key | True | StringU8 |  |  |  |
| level | False | StringU8 |  |  |  |
| priority | False | I32 | Priority determines if shown as important event and which shots take precedence when selecting shot |  |  |
| window_in | False | I32 | Start of window to trigger, where imagine 0 is when event happens. So if want to start playing/notifying of shot 10 seconds before happens, this should be 10. |  |  |
| window_out | False | I32 | End of window to trigger, where imagine 0 is when event happens. So if closest time can play is 5 seconds before, this should be 5. |  |  |
| repeat_wait_ms | False | I32 | After a cinematic event is played, it waits this duration until can be played again |  |  |
| event_category | False | StringU8 | This is the event category, so the type of event the shot gets played for | [battle_cinematic_event_categories_tables](#battle_cinematic_event_categories_tables) | key |
| time_after_event | False | I32 | in seconds after trigger event |  |  |
  
## battle_cities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| city | True | StringU8 |  |  |  |
| minimum_building_scale | False | F32 |  |  |  |
| maximum_building_scale | False | F32 |  |  |  |
| town_min_distance | False | F32 |  |  |  |
| city_min_distance | False | F32 |  |  |  |
| town_radius | False | F32 |  |  |  |
| city_radius | False | F32 |  |  |  |
| number_of_town_buildings | False | I32 |  |  |  |
| number_of_city_buildings | False | I32 |  |  |  |
  
## battle_city_buildings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building | True | StringU8 |  | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| city | False | StringU8 |  | [battle_cities_tables](#battle_cities_tables) | city |
| amount_in_town | False | I32 |  |  |  |
| amount_in_city | False | I32 |  |  |  |
  
## battle_climate_weather_descriptions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | False | StringU8 |  |  |  |
| climate_type | True | StringU8 |  | [climates_tables](#climates_tables) | climate_type |
| season | True | StringU8 |  | [seasons_tables](#seasons_tables) | season |
| weather_type | True | StringU8 |  | [battle_weather_types_tables](#battle_weather_types_tables) | key |
| probability | False | I32 |  |  |  |
| heat_fatigue | False | I32 |  |  |  |
| cold_fatigue | False | I32 |  |  |  |
| spotting_scalar | False | F32 |  |  |  |
  
## battle_difficulty_modifiers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| difficulty_level | True | StringU8 |  |  |  |
| human | True | Boolean |  |  |  |
| stat | True | StringU8 |  |  |  |
| value | False | OptionalStringU8 |  | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
  
## battle_entities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| difficulty_level | True | StringU8 |  |  |  |
| human | True | Boolean |  |  |  |
| stat | True | StringU8 |  |  |  |
| value | False | OptionalStringU8 |  | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
  
## battle_entity_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| difficulty_level | True | StringU8 |  |  |  |
| human | True | Boolean |  |  |  |
| stat | True | StringU8 |  |  |  |
| value | False | OptionalStringU8 |  | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
  
## battle_misc_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| name | True | StringU8 |  |  |  |
  
## battle_personalities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| name | True | StringU8 |  |  |  |
  
## battle_siege_vehicle_permissions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| faction | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| vehicle | True | StringU8 |  | [battlefield_siege_vehicles_tables](#battlefield_siege_vehicles_tables) | key |
  
## battle_skeletons_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| faction | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| vehicle | True | StringU8 |  | [battlefield_siege_vehicles_tables](#battlefield_siege_vehicles_tables) | key |
  
## battle_sky_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| season | False | StringU8 |  | [seasons_tables](#seasons_tables) | season |
| weather_type | False | StringU8 |  | [battle_weather_types_tables](#battle_weather_types_tables) | key |
| time_of_day | False | StringU8 |  |  |  |
| climate | False | OptionalStringU8 |  | [climates_tables](#climates_tables) | climate_type |
| sky_file | False | StringU8 |  |  |  |
| supports_ambient_fog | False | Boolean |  |  |  |
| supports_volumetric_fog | False | Boolean |  |  |  |
  
## battle_terrain_farms_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| farm | True | StringU16 |  |  |  |
| tile_model | False | StringU16 |  |  |  |
| blend_map_model | False | StringU16 |  |  |  |
| alternate_blend_map_model | False | StringU16 |  |  |  |
| road_blend_map_model | False | StringU16 |  |  |  |
| colour_map_model | False | StringU16 |  |  |  |
| alternate_colour_map_model | False | StringU16 |  |  |  |
| road_colour_map_model | False | StringU16 |  |  |  |
| grass_map_model | False | StringU16 |  |  |  |
| alternate_grass_map_model | False | StringU16 |  |  |  |
| road_grass_map_model | False | StringU16 |  |  |  |
| tile_map | False | OptionalStringU16 |  |  |  |
| wall_texture | False | StringU16 |  |  |  |
| wall_end | False | StringU16 |  | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| wall_cross_section | False | StringU16 |  |  |  |
  
## battle_type_setup_limits_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| battle_type | True | StringU8 |  | [battle_types_tables](#battle_types_tables) | type |
| weighting_type | True | StringU8 |  |  |  |
| army_size | True | StringU8 |  |  |  |
| era | True | StringU8 |  |  |  |
| max_infantry | False | I32 |  |  |  |
| max_cavalry | False | I32 |  |  |  |
| max_artillery | False | I32 |  |  |  |
| max_small_ship | False | I32 |  |  |  |
| max_frigate | False | I32 |  |  |  |
| max_line_of_battle | False | I32 |  |  |  |
| id | False | I64 |  |  |  |
  
## battle_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| type | True | StringU8 |  |  |  |
| sort_order | False | I32 | Order put in ui |  |  |
| defender_funds_ratio | False | F32 | Ratio of funds defender gets as opposed to attacker for this battle type |  |  |
| max_teamsize | False | I32 | Maximum number of armies per alliance for this battle type |  |  |
  
## battle_types_to_victory_conditions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| battle_type | True | StringU16 |  | [battle_types_tables](#battle_types_tables) | type |
| attacker_victory_condition | True | OptionalStringU8 |  | [victory_conditions_tables](#victory_conditions_tables) | condition |
| defender_victory_condition | True | OptionalStringU8 |  | [victory_conditions_tables](#victory_conditions_tables) | condition |
  
## battle_weather_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| stat | True | StringU8 |  | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| value | False | I32 |  |  |  |
| weather_type | True | StringU8 |  | [battle_weather_types_tables](#battle_weather_types_tables) | key |
  
## battle_weather_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| stat | True | StringU8 |  | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| value | False | I32 |  |  |  |
| weather_type | True | StringU8 |  | [battle_weather_types_tables](#battle_weather_types_tables) | key |
  
## battlefield_building_categories_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| category | True | StringU8 |  |  |  |
| default_destruction_effect | False | StringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| icon_path | False | StringU8 | Icon path used for any related building icons for radar, etc |  |  |
  
## battlefield_building_transformations_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| transformation | True | StringU8 |  |  |  |
  
## battlefield_buildings_names_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| onscreen_name | False | StringU8 |  |  |  |
| global_effects_description | False | OptionalStringU8 |  |  |  |
| local_effects_description | False | OptionalStringU8 |  |  |  |
  
## battlefield_buildings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| onscreen_name | False | StringU8 |  |  |  |
| global_effects_description | False | OptionalStringU8 |  |  |  |
| local_effects_description | False | OptionalStringU8 |  |  |  |
  
## battlefield_buildings_with_projectiles_names_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building_category | True | StringU8 |  | [battlefield_building_categories_tables](#battlefield_building_categories_tables) | category |
| name | False | StringU8 |  | [battlefield_buildings_names_tables](#battlefield_buildings_names_tables) | key |
| projectile | True | StringU8 |  | [projectiles_tables](#projectiles_tables) | key |
  
## battlefield_chariots_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| battle_entity | False | StringU8 |  | [battle_entities_tables](#battle_entities_tables) | key |
| chariot_animation_table | False | StringU8 |  | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| chariot_type | False | StringU8 |  | [chariot_types_enums_tables](#chariot_types_enums_tables) | key |
| destroyed_model | False | StringU8 |  | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| destruction_animation | False | StringU8 |  | [warscape_animated_tables](#warscape_animated_tables) | key |
| key | True | StringU8 |  |  |  |
| model | False | StringU8 |  | [warscape_animated_tables](#warscape_animated_tables) | key |
  
## battlefield_deployable_siege_items_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| battle_entity | False | StringU8 |  | [battle_entities_tables](#battle_entities_tables) | key |
| chariot_animation_table | False | StringU8 |  | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| chariot_type | False | StringU8 |  | [chariot_types_enums_tables](#chariot_types_enums_tables) | key |
| destroyed_model | False | StringU8 |  | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| destruction_animation | False | StringU8 |  | [warscape_animated_tables](#warscape_animated_tables) | key |
| key | True | StringU8 |  |  |  |
| model | False | StringU8 |  | [warscape_animated_tables](#warscape_animated_tables) | key |
  
## battlefield_engines_autonomous_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| autonomous_engine_type | False | StringU8 |  | [battlefield_engines_tables](#battlefield_engines_tables) | key |
| engine_crew_anims | False | StringU8 |  | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| engine_crew_entity | False | StringU8 |  | [battle_entities_tables](#battle_entities_tables) | key |
| key | True | StringU8 |  |  |  |
| num_ammo | False | I32 |  |  |  |
  
## battlefield_engines_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| autonomous_engine_type | False | StringU8 |  | [battlefield_engines_tables](#battlefield_engines_tables) | key |
| engine_crew_anims | False | StringU8 |  | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| engine_crew_entity | False | StringU8 |  | [battle_entities_tables](#battle_entities_tables) | key |
| key | True | StringU8 |  |  |  |
| num_ammo | False | I32 |  |  |  |
  
## battlefield_siege_vehicles_custom_battles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| cap | False | I32 |  |  |  |
| probability | False | F32 |  |  |  |
| vehicle | True | StringU8 |  | [battlefield_siege_vehicles_tables](#battlefield_siege_vehicles_tables) | key |
  
## battlefield_siege_vehicles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| cap | False | I32 |  |  |  |
| probability | False | F32 |  |  |  |
| vehicle | True | StringU8 |  | [battlefield_siege_vehicles_tables](#battlefield_siege_vehicles_tables) | key |
  
## battlefield_siege_vehicles_to_autonomous_engines_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| engine | True | StringU8 |  | [battlefield_engines_autonomous_tables](#battlefield_engines_autonomous_tables) | key |
| vehicle | True | StringU8 |  | [battlefield_siege_vehicles_tables](#battlefield_siege_vehicles_tables) | key |
  
## battles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| engine | True | StringU8 |  | [battlefield_engines_autonomous_tables](#battlefield_engines_autonomous_tables) | key |
| vehicle | True | StringU8 |  | [battlefield_siege_vehicles_tables](#battlefield_siege_vehicles_tables) | key |
  
## battles_to_battle_sky_types_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| battle_key | True | StringU8 |  | [battles_tables](#battles_tables) | key |
| battle_sky_type_key | True | StringU8 |  | [battle_sky_types_tables](#battle_sky_types_tables) | key |
  
## bribe_actions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | False | StringU8 |  |  |  |
| name | False | StringU8 |  |  |  |
  
## building_chain_availabilities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| set_id | False | StringU8 |  | [building_chain_availability_set_ids_tables](#building_chain_availability_set_ids_tables) | id |
| culture | False | OptionalStringU8 |  | [cultures_tables](#cultures_tables) | key |
| faction | False | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| id | True | StringU8 |  |  |  |
| sub_culture | False | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| campaign | False | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## building_chain_availability_set_ids_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | StringU8 |  |  |  |
  
## building_chain_availability_sets_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building_chain | True | StringU8 |  | [building_chains_tables](#building_chains_tables) | key |
| id | True | StringU8 |  | [building_chain_availability_set_ids_tables](#building_chain_availability_set_ids_tables) | id |
  
## building_chain_to_slots_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| chain | True | StringU8 |  | [building_chains_tables](#building_chains_tables) | key |
| slot | True | StringU8 |  | [slots_tables](#slots_tables) | slot |
  
## building_chains_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| chain | True | StringU8 |  | [building_chains_tables](#building_chains_tables) | key |
| slot | True | StringU8 |  | [slots_tables](#slots_tables) | slot |
  
## building_culture_variants_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| chain | True | StringU8 |  | [building_chains_tables](#building_chains_tables) | key |
| slot | True | StringU8 |  | [slots_tables](#slots_tables) | slot |
  
## building_effects_junction_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building | True | StringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| value | False | F32 |  |  |  |
| value_damaged | False | F32 |  |  |  |
| value_ruined | False | F32 |  |  |  |
  
## building_instances_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| num_instances | False | I32 |  |  |  |
  
## building_level_armed_citizenry_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building_level | False | StringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| id | True | I64 |  |  |  |
| unit_group | False | StringU8 |  | [armed_citizenry_unit_groups_tables](#armed_citizenry_unit_groups_tables) | unit_group |
  
## building_level_required_technology_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building_level_key | True | StringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| technology_key | True | StringU8 |  | [technologies_tables](#technologies_tables) | key |
  
## building_levels_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building_level_key | True | StringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| technology_key | True | StringU8 |  | [technologies_tables](#technologies_tables) | key |
  
## building_set_to_building_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building_chain | True | OptionalStringU8 |  | [building_chains_tables](#building_chains_tables) | key |
| building_level | True | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| building_set | True | StringU8 |  | [building_sets_tables](#building_sets_tables) | key |
| exclude | False | Boolean |  |  |  |
  
## building_sets_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building_chain | True | OptionalStringU8 |  | [building_chains_tables](#building_chains_tables) | key |
| building_level | True | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| building_set | True | StringU8 |  | [building_sets_tables](#building_sets_tables) | key |
| exclude | False | Boolean |  |  |  |
  
## building_states_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## building_superchains_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## building_units_allowed_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## building_upgrades_junction_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| from | True | StringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| to | True | StringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
  
## cai_agent_distribution_profiles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_agent_distribution_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_agent_record_to_cai_agent_type_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_agent_recruitment_profiles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_agent_recruitment_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_agent_type_distribution_profile_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| agent_type_key | True | StringU8 |  | [cai_agent_types_tables](#cai_agent_types_tables) | key |
| distribution_profile_key | True | StringU8 |  | [cai_agent_distribution_profiles_tables](#cai_agent_distribution_profiles_tables) | key |
| distribution_type_key | True | StringU8 |  | [cai_agent_distribution_types_tables](#cai_agent_distribution_types_tables) | key |
  
## cai_agent_type_recruitment_profile_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| agent_type_key | True | StringU8 |  | [cai_agent_types_tables](#cai_agent_types_tables) | key |
| recruitment_profile_key | True | StringU8 |  | [cai_agent_recruitment_profiles_tables](#cai_agent_recruitment_profiles_tables) | key |
| recruitment_type_key | True | StringU8 |  | [cai_agent_recruitment_types_tables](#cai_agent_recruitment_types_tables) | key |
  
## cai_agent_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_base_building_context_values_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building_key | True | StringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| economic_value | False | F32 |  |  |  |
| prestige_value | False | F32 |  |  |  |
| happiness_value | False | F32 |  |  |  |
| military_value | False | F32 |  |  |  |
| education_value | False | F32 |  |  |  |
| existing_buildings_apply_discount_over_limit | False | F32 |  |  |  |
| existing_buildings_discount_per_building | False | F32 |  |  |  |
| existing_buildings_maximum_discount | False | F32 |  |  |  |
  
## cai_construction_system_building_values_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building_chain | True | OptionalStringU8 |  | [building_chains_tables](#building_chains_tables) | key |
| building_instance | True | OptionalStringU8 |  | [building_instances_tables](#building_instances_tables) | key |
| building_or_building_range_start_inclusive | True | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| building_range_end_inclusive | True | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| building_super_chain | True | OptionalStringU8 |  | [building_superchains_tables](#building_superchains_tables) | key |
| cai_construction_system_category | True | OptionalStringU8 |  | [cai_construction_system_categories_tables](#cai_construction_system_categories_tables) | key |
| cai_construction_system_category_group | True | OptionalStringU8 |  | [cai_construction_system_category_groups_tables](#cai_construction_system_category_groups_tables) | key |
| campaign | True | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| culture | True | OptionalStringU8 |  | [cultures_tables](#cultures_tables) | key |
| faction | True | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| per_faction_building_limit_start | False | I32 |  |  |  |
| per_faction_building_limit_end | False | I32 |  |  |  |
| per_faction_building_minimum_discount_when_exceeding_limit_start | False | I32 |  |  |  |
| per_faction_building_maximum_discount_when_exceeding_limit_start | False | I32 |  |  |  |
| per_faction_building_minimum_discount_when_exceeding_limit_end | False | I32 |  |  |  |
| per_faction_building_maximum_discount_when_exceeding_limit_end | False | I32 |  |  |  |
| per_faction_per_building_discount_increment_when_exceeding_limit_start | False | I32 |  |  |  |
| per_faction_per_building_discount_increment_when_exceeding_limit_end | False | I32 |  |  |  |
| per_province_building_limit_start | False | I32 |  |  |  |
| per_province_building_limit_end | False | I32 |  |  |  |
| per_province_building_minimum_discount_when_exceeding_limit_start | False | I32 |  |  |  |
| per_province_building_maximum_discount_when_exceeding_limit_start | False | I32 |  |  |  |
| per_province_building_minimum_discount_when_exceeding_limit_end | False | I32 |  |  |  |
| per_province_building_maximum_discount_when_exceeding_limit_end | False | I32 |  |  |  |
| per_province_per_building_discount_increment_when_exceeding_limit_start | False | I32 |  |  |  |
| per_province_per_building_discount_increment_when_exceeding_limit_end | False | I32 |  |  |  |
| score_end_inclusive | False | I32 |  |  |  |
| score_or_score_start_inclusive | False | I32 |  |  |  |
| sub_culture | True | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## cai_construction_system_categories_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| cai_construction_system_category_group | False | StringU8 |  | [cai_construction_system_category_groups_tables](#cai_construction_system_category_groups_tables) | key |
| cdir_military_generator_unit_group | False | OptionalStringU8 |  | [cdir_military_generator_unit_groups_tables](#cdir_military_generator_unit_groups_tables) | key |
| key | True | StringU8 |  |  |  |
  
## cai_construction_system_category_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_construction_system_province_template_assignment_policies_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_construction_system_strategic_context_template_policies_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| default_cai_construction_system_template | False | StringU8 |  | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| key | True | StringU8 |  |  |  |
  
## cai_construction_system_strategic_context_template_policy_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| cai_construction_system_strategic_context_policy | True | StringU8 |  | [cai_construction_system_strategic_context_template_policies_tables](#cai_construction_system_strategic_context_template_policies_tables) | key |
| cai_construction_system_template | True | StringU8 |  | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| cai_strategic_context | True | StringU8 |  | [cai_strategic_context_types_tables](#cai_strategic_context_types_tables) | key |
  
## cai_construction_system_superchain_hints_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| economic_specialisation_recommended | False | Boolean |  |  |  |
| military_specialisation_recommended | False | Boolean |  |  |  |
| super_chain_key | True | StringU8 |  | [building_superchains_tables](#building_superchains_tables) | key |
  
## cai_construction_system_synergies_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| economic_specialisation_recommended | False | Boolean |  |  |  |
| military_specialisation_recommended | False | Boolean |  |  |  |
| super_chain_key | True | StringU8 |  | [building_superchains_tables](#building_superchains_tables) | key |
  
## cai_construction_system_synergy_levels_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| absolute_effect | False | I32 |  |  |  |
| key | True | StringU8 |  |  |  |
| priority | False | I32 |  |  |  |
| relative_effect | False | F32 |  |  |  |
  
## cai_construction_system_synergy_policies_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_construction_system_templates_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| cai_construction_system_category | True | OptionalStringU8 |  | [cai_construction_system_categories_tables](#cai_construction_system_categories_tables) | key |
| cai_construction_system_category_group | True | OptionalStringU8 |  | [cai_construction_system_category_groups_tables](#cai_construction_system_category_groups_tables) | key |
| cai_construction_system_template | True | StringU8 |  | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| value | False | F32 |  |  |  |
  
## cai_construction_system_templates_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| default_category_and_group_value | False | F32 |  |  |  |
| key | True | StringU8 |  |  |  |
  
## cai_diplomacy_complex_treacheries_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| first_event | True | StringU8 |  | [cai_personality_diplomatic_events_tables](#cai_personality_diplomatic_events_tables) | id |
| max_turn_difference | False | I32 |  |  |  |
| second_event | True | StringU8 |  | [cai_personality_diplomatic_events_tables](#cai_personality_diplomatic_events_tables) | id |
| value | False | F32 |  |  |  |
  
## cai_diplomacy_simple_treacheries_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| event | True | StringU8 |  | [cai_personality_diplomatic_events_tables](#cai_personality_diplomatic_events_tables) | id |
| value | False | F32 |  |  |  |
  
## cai_military_aggressiveness_policies_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| event | True | StringU8 |  | [cai_personality_diplomatic_events_tables](#cai_personality_diplomatic_events_tables) | id |
| value | False | F32 |  |  |  |
  
## cai_military_behaviour_policies_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_personalities_budget_allocation_policy_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_personalities_budget_allocations_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| agents_funding_cap | False | I32 |  |  |  |
| agents_funds_allocation_percentage | False | I32 |  |  |  |
| agents_percentage_of_pool_to_save_on_fail | False | I32 |  |  |  |
| agents_turns_of_inactivity_until_cap | False | I32 |  |  |  |
| army_funding_cap | False | I32 |  |  |  |
| army_funds_allocation_percentage | False | I32 |  |  |  |
| army_percentage_of_pool_to_save_on_fail | False | I32 |  |  |  |
| army_turns_of_inactivity_until_cap | False | I32 |  |  |  |
| construction_funding_cap | False | I32 |  |  |  |
| construction_funds_allocation_percentage | False | I32 |  |  |  |
| construction_percentage_of_pool_to_save_on_fail | False | I32 |  |  |  |
| construction_turns_of_inactivity_until_cap | False | I32 |  |  |  |
| diplomacy_funding_cap | False | I32 |  |  |  |
| diplomacy_funds_allocation_percentage | False | I32 |  |  |  |
| diplomacy_percentage_of_pool_to_save_on_fail | False | I32 |  |  |  |
| diplomacy_turns_of_inactivity_until_cap | False | I32 |  |  |  |
| key | True | StringU8 |  |  |  |
| navy_funding_cap | False | I32 |  |  |  |
| navy_funds_allocation_percentage | False | I32 |  |  |  |
| navy_percentage_of_pool_to_save_on_fail | False | I32 |  |  |  |
| navy_turns_of_inactivity_until_cap | False | I32 |  |  |  |
| minimum_settable_tax_level | False | StringU8 |  | [taxes_levels_tables](#taxes_levels_tables) | tax_level |
| maximum_settable_tax_level | False | StringU8 |  | [taxes_levels_tables](#taxes_levels_tables) | tax_level |
| technology_funds_allocation_percentage | False | I32 |  |  |  |
| technology_turns_of_inactivity_until_cap | False | I32 |  |  |  |
| technology_funding_cap | False | I32 |  |  |  |
| technology_percentage_of_pool_to_save_on_fail | False | I32 |  |  |  |
  
## cai_personalities_budget_policies_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| agents_funding_cap | False | I32 |  |  |  |
| agents_funds_allocation_percentage | False | I32 |  |  |  |
| agents_percentage_of_pool_to_save_on_fail | False | I32 |  |  |  |
| agents_turns_of_inactivity_until_cap | False | I32 |  |  |  |
| army_funding_cap | False | I32 |  |  |  |
| army_funds_allocation_percentage | False | I32 |  |  |  |
| army_percentage_of_pool_to_save_on_fail | False | I32 |  |  |  |
| army_turns_of_inactivity_until_cap | False | I32 |  |  |  |
| construction_funding_cap | False | I32 |  |  |  |
| construction_funds_allocation_percentage | False | I32 |  |  |  |
| construction_percentage_of_pool_to_save_on_fail | False | I32 |  |  |  |
| construction_turns_of_inactivity_until_cap | False | I32 |  |  |  |
| diplomacy_funding_cap | False | I32 |  |  |  |
| diplomacy_funds_allocation_percentage | False | I32 |  |  |  |
| diplomacy_percentage_of_pool_to_save_on_fail | False | I32 |  |  |  |
| diplomacy_turns_of_inactivity_until_cap | False | I32 |  |  |  |
| key | True | StringU8 |  |  |  |
| navy_funding_cap | False | I32 |  |  |  |
| navy_funds_allocation_percentage | False | I32 |  |  |  |
| navy_percentage_of_pool_to_save_on_fail | False | I32 |  |  |  |
| navy_turns_of_inactivity_until_cap | False | I32 |  |  |  |
| minimum_settable_tax_level | False | StringU8 |  | [taxes_levels_tables](#taxes_levels_tables) | tax_level |
| maximum_settable_tax_level | False | StringU8 |  | [taxes_levels_tables](#taxes_levels_tables) | tax_level |
| technology_funds_allocation_percentage | False | I32 |  |  |  |
| technology_turns_of_inactivity_until_cap | False | I32 |  |  |  |
| technology_funding_cap | False | I32 |  |  |  |
| technology_percentage_of_pool_to_save_on_fail | False | I32 |  |  |  |
  
## cai_personalities_construction_preference_policies_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_personalities_construction_system_policies_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building_synergies_policy | False | StringU8 |  | [cai_construction_system_synergy_policies_tables](#cai_construction_system_synergy_policies_tables) | key |
| key | True | StringU8 |  |  |  |
| province_specialisation_template_assignment_policy | False | StringU8 |  | [cai_construction_system_province_template_assignment_policies_tables](#cai_construction_system_province_template_assignment_policies_tables) | key |
| strategic_context_template_assignment_policy | False | StringU8 |  | [cai_construction_system_strategic_context_template_policies_tables](#cai_construction_system_strategic_context_template_policies_tables) | key |
  
## cai_personalities_income_allocation_policies_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building_synergies_policy | False | StringU8 |  | [cai_construction_system_synergy_policies_tables](#cai_construction_system_synergy_policies_tables) | key |
| key | True | StringU8 |  |  |  |
| province_specialisation_template_assignment_policy | False | StringU8 |  | [cai_construction_system_province_template_assignment_policies_tables](#cai_construction_system_province_template_assignment_policies_tables) | key |
| strategic_context_template_assignment_policy | False | StringU8 |  | [cai_construction_system_strategic_context_template_policies_tables](#cai_construction_system_strategic_context_template_policies_tables) | key |
  
## cai_personalities_income_allocation_policy_strategic_context_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building_synergies_policy | False | StringU8 |  | [cai_construction_system_synergy_policies_tables](#cai_construction_system_synergy_policies_tables) | key |
| key | True | StringU8 |  |  |  |
| province_specialisation_template_assignment_policy | False | StringU8 |  | [cai_construction_system_province_template_assignment_policies_tables](#cai_construction_system_province_template_assignment_policies_tables) | key |
| strategic_context_template_assignment_policy | False | StringU8 |  | [cai_construction_system_strategic_context_template_policies_tables](#cai_construction_system_strategic_context_template_policies_tables) | key |
  
## cai_personalities_random_group_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| personality_key | True | StringU8 |  | [cai_personalities_tables](#cai_personalities_tables) | key |
| random_personality_group_key | True | StringU8 |  | [cai_personalities_random_groups_tables](#cai_personalities_random_groups_tables) | random_personality_group_key |
  
## cai_personalities_random_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| random_personality_group_key | True | StringU8 |  |  |  |
  
## cai_personalities_randomisation_policies_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| randomisation_policy_key | True | StringU8 |  |  |  |
  
## cai_personalities_reliability_policies_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| randomisation_policy_key | True | StringU8 |  |  |  |
  
## cai_personalities_religious_conversion_policies_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_personalities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_personalities_task_management_system_task_generator_profiles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_personality_cultural_components_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_personality_cultural_multipliers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| component_id | True | StringU8 |  | [cai_personality_cultural_components_tables](#cai_personality_cultural_components_tables) | id |
| negative_attitude_multiplier | False | F32 |  |  |  |
| positive_attitude_multiplier | False | F32 |  |  |  |
| source | True | StringU8 |  | [religions_tables](#religions_tables) | religion_key |
| target | True | StringU8 |  | [religions_tables](#religions_tables) | religion_key |
| attitude_base | False | F32 |  |  |  |
  
## cai_personality_deal_evaluation_component_overrides_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| component | True | StringU8 |  | [cai_personality_deal_evaluation_components_tables](#cai_personality_deal_evaluation_components_tables) | id |
| parent | False | StringU8 |  | [cai_personality_deal_evaluation_components_tables](#cai_personality_deal_evaluation_components_tables) | id |
  
## cai_personality_deal_evaluation_components_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| component | True | StringU8 |  | [cai_personality_deal_evaluation_components_tables](#cai_personality_deal_evaluation_components_tables) | id |
| parent | False | StringU8 |  | [cai_personality_deal_evaluation_components_tables](#cai_personality_deal_evaluation_components_tables) | id |
  
## cai_personality_deal_evaluation_deal_component_names_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | StringU8 |  |  |  |
  
## cai_personality_deal_evaluation_deal_component_values_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | StringU8 |  |  |  |
  
## cai_personality_deal_generation_components_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | StringU8 |  |  |  |
  
## cai_personality_deal_generation_generator_priorities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| component_key | True | StringU8 |  | [cai_personality_deal_generation_components_tables](#cai_personality_deal_generation_components_tables) | id |
| generator_key | True | StringU8 |  | [cai_personality_deal_generation_generators_tables](#cai_personality_deal_generation_generators_tables) | id |
| last_stand_priority | False | F32 |  |  |  |
| param1 | False | F32 |  |  |  |
| param2 | False | F32 |  |  |  |
| param3 | False | F32 |  |  |  |
| param4 | False | F32 |  |  |  |
| peace_priority | False | F32 |  |  |  |
| tension_priority | False | F32 |  |  |  |
| war_priority | False | F32 |  |  |  |
| total_war_priority | False | F32 |  |  |  |
| failure_timeout | False | I32 |  |  |  |
| min_payment_cap | False | I32 |  |  |  |
| max_payment_cap | False | I32 |  |  |  |
| max_payment_pct | False | F32 |  |  |  |
  
## cai_personality_deal_generation_generators_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | StringU8 |  |  |  |
  
## cai_personality_diplomatic_component_overrides_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| component | True | StringU8 |  | [cai_personality_diplomatic_components_tables](#cai_personality_diplomatic_components_tables) | id |
| parent | False | StringU8 |  | [cai_personality_diplomatic_components_tables](#cai_personality_diplomatic_components_tables) | id |
  
## cai_personality_diplomatic_components_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| component | True | StringU8 |  | [cai_personality_diplomatic_components_tables](#cai_personality_diplomatic_components_tables) | id |
| parent | False | StringU8 |  | [cai_personality_diplomatic_components_tables](#cai_personality_diplomatic_components_tables) | id |
  
## cai_personality_diplomatic_event_values_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| component_id | True | StringU8 |  | [cai_personality_diplomatic_components_tables](#cai_personality_diplomatic_components_tables) | id |
| event_id | True | StringU8 |  | [cai_personality_diplomatic_events_tables](#cai_personality_diplomatic_events_tables) | id |
| falloff | False | I32 |  |  |  |
| value | False | F32 |  |  |  |
  
## cai_personality_diplomatic_events_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | StringU8 |  |  |  |
| diplomatic_factor_group_active | False | OptionalStringU8 |  | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| diplomatic_factor_group_inactive | False | OptionalStringU8 |  | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
  
## cai_personality_diplomatic_treaty_values_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | StringU8 |  |  |  |
| diplomatic_factor_group_active | False | OptionalStringU8 |  | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| diplomatic_factor_group_inactive | False | OptionalStringU8 |  | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
  
## cai_personality_negotiation_components_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | StringU8 |  |  |  |
| diplomatic_factor_group_active | False | OptionalStringU8 |  | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| diplomatic_factor_group_inactive | False | OptionalStringU8 |  | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
  
## cai_personality_occupation_decision_components_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | StringU8 |  |  |  |
| diplomatic_factor_group_active | False | OptionalStringU8 |  | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| diplomatic_factor_group_inactive | False | OptionalStringU8 |  | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
  
## cai_personality_occupation_decision_priorities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | StringU8 |  |  |  |
| diplomatic_factor_group_active | False | OptionalStringU8 |  | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| diplomatic_factor_group_inactive | False | OptionalStringU8 |  | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
  
## cai_personality_strategic_components_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | StringU8 |  |  |  |
| diplomatic_factor_group_active | False | OptionalStringU8 |  | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| diplomatic_factor_group_inactive | False | OptionalStringU8 |  | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
  
## cai_personality_strategic_desired_attitudes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| best_friends_attitude | False | F32 |  |  |  |
| best_friends_positive_factor | False | F32 |  |  |  |
| bitter_enemies_attitude | False | F32 |  |  |  |
| bitter_enemies_positive_factor | False | F32 |  |  |  |
| friendly_attitude | False | F32 |  |  |  |
| friendly_positive_factor | False | F32 |  |  |  |
| neutral_attitude | False | F32 |  |  |  |
| neutral_positive_factor | False | F32 |  |  |  |
| strategic_component | True | StringU8 |  | [cai_personality_strategic_components_tables](#cai_personality_strategic_components_tables) | id |
| unfriendly_attitude | False | F32 |  |  |  |
| unfriendly_positive_factor | False | F32 |  |  |  |
| very_friendly_attitude | False | F32 |  |  |  |
| very_friendly_positive_factor | False | F32 |  |  |  |
| very_unfriendly_attitude | False | F32 |  |  |  |
| very_unfriendly_positive_factor | False | F32 |  |  |  |
| best_friends_negative_factor | False | F32 |  |  |  |
| very_friendly_negative_factor | False | F32 |  |  |  |
| friendly_negative_factor | False | F32 |  |  |  |
| neutral_negative_factor | False | F32 |  |  |  |
| unfriendly_negative_factor | False | F32 |  |  |  |
| very_unfriendly_negative_factor | False | F32 |  |  |  |
| bitter_enemies_negative_factor | False | F32 |  |  |  |
  
## cai_personality_strategic_resource_values_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| trade_falloff | False | F32 |  |  |  |
| trade_value | False | F32 |  |  |  |
| resource | True | StringU8 |  | [resources_tables](#resources_tables) | key |
| strategic_component | True | StringU8 |  | [cai_personality_strategic_components_tables](#cai_personality_strategic_components_tables) | id |
| ownership_falloff | False | F32 |  |  |  |
| ownership_value | False | F32 |  |  |  |
  
## cai_siege_strength_modifiers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| defence_strength_modifier | False | F32 |  |  |  |
| assault_strength_modifier | False | F32 |  |  |  |
| subculture | True | StringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## cai_strategic_context_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_task_management_system_task_generator_groups_generators_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| priority | False | F32 | Priority of the generator within the group. Generally scalled between 0.0 and 1.0 |  |  |
| task_generator_group_key | True | StringU8 |  | [cai_task_management_system_task_generator_groups_tables](#cai_task_management_system_task_generator_groups_tables) | key |
| task_generator_key | True | StringU8 |  | [cai_task_management_system_task_generators_tables](#cai_task_management_system_task_generators_tables) | key |
  
## cai_task_management_system_task_generator_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 | The name of the Task Generator Group |  |  |
  
## cai_task_management_system_task_generators_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 | The DB name of this CAI Task Management System Task Genertaor |  |  |
  
## cai_variables_overides_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| cai_variable_key | True | StringU8 | Campaign AI Variable to override | [cai_variables_tables](#cai_variables_tables) | key |
| campaign_key | True | StringU8 | Campaign Key | [campaigns_tables](#campaigns_tables) | campaign_name |
| optional_campaign_type | True | OptionalStringU8 | (Optional) Long/Short |  |  |
| optional_difficulty_level | True | OptionalStringU8 | (Optional) Integer value campaign difficulty |  |  |
| value | False | F32 | Override value |  |  |
  
## cai_variables_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 | Campaign AI Control Variable Key |  |  |
| value | False | F32 | Campaign AI Control Variable Base Value |  |  |
| description | False | StringU8 | Campaign AI Variable Description |  |  |
  
## campaign_ai_character_skill_tree_distribution_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| distribution_key | True | StringU8 |  | [campaign_ai_character_skill_tree_distributions_tables](#campaign_ai_character_skill_tree_distributions_tables) | key |
| agent_manager_key | True | StringU8 |  | [campaign_ai_character_skill_tree_agent_managers_tables](#campaign_ai_character_skill_tree_agent_managers_tables) | key |
| priority | False | I32 |  |  |  |
  
## campaign_ai_character_skill_tree_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| agent_manager_key | True | StringU8 |  | [campaign_ai_character_skill_tree_agent_managers_tables](#campaign_ai_character_skill_tree_agent_managers_tables) | key |
| priority | False | I32 |  |  |  |
| skill_key | True | StringU8 |  | [character_skills_tables](#character_skills_tables) | key |
  
## campaign_ai_character_skill_tree_manager_agent_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| agent_key | True | StringU8 |  | [character_skill_node_sets_tables](#character_skill_node_sets_tables) | key |
| agent_manager_key | False | StringU8 |  | [campaign_ai_character_skill_tree_agent_managers_tables](#campaign_ai_character_skill_tree_agent_managers_tables) | key |
| manager_key | True | StringU8 |  | [campaign_ai_character_skill_tree_managers_tables](#campaign_ai_character_skill_tree_managers_tables) | key |
  
## campaign_ai_manager_behaviour_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| manager | True | StringU8 |  | [campaign_ai_managers_tables](#campaign_ai_managers_tables) | manager |
| behaviour | True | StringU8 |  | [campaign_ai_behaviours_tables](#campaign_ai_behaviours_tables) | behaviour |
| priority | False | F32 |  |  |  |
  
## campaign_ai_managers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| manager | True | StringU8 |  |  |  |
  
## campaign_ai_personalities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| personality | True | StringU8 |  |  |  |
| is_default | False | Boolean |  |  |  |
  
## campaign_ai_personality_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| personality | True | StringU8 |  | [campaign_ai_personalities_tables](#campaign_ai_personalities_tables) | personality |
| property | True | StringU8 |  | [campaign_ai_personality_properties_tables](#campaign_ai_personality_properties_tables) | property |
| property_value | False | F32 |  |  |  |
  
## campaign_ai_technology_manager_path_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| manager_key | True | StringU8 |  | [campaign_ai_technology_managers_tables](#campaign_ai_technology_managers_tables) | key |
| path_key | True | StringU8 |  | [campaign_ai_technology_paths_tables](#campaign_ai_technology_paths_tables) | key |
| priority | False | I32 |  |  |  |
  
## campaign_ai_technology_managers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## campaign_ai_technology_path_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| path_key | True | StringU8 |  | [campaign_ai_technology_paths_tables](#campaign_ai_technology_paths_tables) | key |
| priority | False | I32 |  |  |  |
| technology_key | True | StringU8 |  | [technologies_tables](#technologies_tables) | key |
  
## campaign_ambush_ground_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| ambush_chance_of_success | False | F32 |  |  |  |
| key | True | StringU8 |  | [campaign_ground_types_tables](#campaign_ground_types_tables) | type |
  
## campaign_autoresolver_battle_situations_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| ambush_chance_of_success | False | F32 |  |  |  |
| key | True | StringU8 |  | [campaign_ground_types_tables](#campaign_ground_types_tables) | type |
  
## campaign_autoresolver_mod_group_modifier_values_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| group_id | False | StringU8 |  | [campaign_autoresolver_mod_groups_tables](#campaign_autoresolver_mod_groups_tables) | id |
| id | True | I64 |  |  |  |
| modification_id | False | StringU8 |  | [campaign_autoresolver_modifiers_tables](#campaign_autoresolver_modifiers_tables) | id |
| value | False | F32 |  |  |  |
  
## campaign_autoresolver_mod_group_targets_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| alliance_target | False | OptionalStringU8 |  |  |  |
| id | True | StringU8 |  |  |  |
| mechanic_target | False | OptionalStringU8 |  |  |  |
| player_target | False | OptionalStringU8 |  |  |  |
  
## campaign_autoresolver_mod_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | StringU8 |  |  |  |
  
## campaign_autoresolver_modifiers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| class | False | OptionalStringU8 |  | [unit_class_tables](#unit_class_tables) | key |
| id | True | StringU8 |  |  |  |
| stat_variable_id | False | StringU8 |  | [campaign_autoresolver_stat_variables_tables](#campaign_autoresolver_stat_variables_tables) | id |
| vs_class | False | OptionalStringU8 |  | [unit_class_tables](#unit_class_tables) | key |
  
## campaign_autoresolver_situation_mod_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| group_id | False | StringU8 |  | [campaign_autoresolver_mod_groups_tables](#campaign_autoresolver_mod_groups_tables) | id |
| group_target_id | False | StringU8 |  | [campaign_autoresolver_mod_group_targets_tables](#campaign_autoresolver_mod_group_targets_tables) | id |
| id | True | I64 |  |  |  |
| situation_id | False | StringU8 |  | [campaign_autoresolver_battle_situations_tables](#campaign_autoresolver_battle_situations_tables) | id |
  
## campaign_autoresolver_stat_variables_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| description | False | OptionalStringU8 |  |  |  |
| id | True | StringU8 |  |  |  |
  
## campaign_battle_presets_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| description | False | OptionalStringU8 |  |  |  |
| id | True | StringU8 |  |  |  |
  
## campaign_bonus_value_battle_context_battle_type_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| battle_context_key | True | StringU8 |  | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| battle_type_key | True | StringU8 |  | [campaign_battle_type_enums_tables](#campaign_battle_type_enums_tables) | key |
  
## campaign_bonus_value_battle_context_culture_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| battle_context_key | True | StringU8 |  | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| culture_key | True | StringU8 |  | [cultures_tables](#cultures_tables) | key |
  
## campaign_bonus_value_battle_context_faction_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| battle_context_key | True | StringU8 |  | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| faction_key | True | StringU8 |  | [factions_tables](#factions_tables) | key |
  
## campaign_bonus_value_battle_context_force_status_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| battle_context_key | True | StringU8 |  | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| force_status_key | True | StringU8 |  | [campaign_bonus_value_battle_context_force_status_tables](#campaign_bonus_value_battle_context_force_status_tables) | key |
| is_yours | False | Boolean |  |  |  |
  
## campaign_bonus_value_battle_context_ground_type_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| battle_context_key | True | StringU8 |  | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| ground_type_key | True | StringU8 |  | [campaign_ground_types_tables](#campaign_ground_types_tables) | type |
  
## campaign_bonus_value_battle_context_specifiers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| night_battles_only | False | Boolean |  |  |  |
  
## campaign_bonus_value_battle_context_territory_status_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| battle_context_key | True | StringU8 |  | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| territory_status_key | True | StringU8 |  | [campaign_bonus_value_battle_context_territory_status_tables](#campaign_bonus_value_battle_context_territory_status_tables) | key |
  
## campaign_character_art_sets_campaign_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## campaign_character_art_sets_group_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign | True | StringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| group | True | StringU8 |  | [campaign_character_art_sets_campaign_groups_tables](#campaign_character_art_sets_campaign_groups_tables) | key |
  
## campaign_character_art_sets_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign | True | StringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| group | True | StringU8 |  | [campaign_character_art_sets_campaign_groups_tables](#campaign_character_art_sets_campaign_groups_tables) | key |
  
## campaign_character_arts_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign | True | StringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| group | True | StringU8 |  | [campaign_character_art_sets_campaign_groups_tables](#campaign_character_art_sets_campaign_groups_tables) | key |
  
## campaign_character_attribute_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| agent_record | True | StringU8 |  | [agents_tables](#agents_tables) | key |
| attribute_level | True | I32 |  |  |  |
| attribute_record | True | StringU8 |  | [agent_attributes_tables](#agent_attributes_tables) | key |
| culture_record | True | OptionalStringU8 |  | [cultures_tables](#cultures_tables) | key |
| effect_record | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | True | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| effect_value | False | F32 |  |  |  |
| faction_record | True | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| subculture_record | True | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| campaign_record | True | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## campaign_difficulty_handicap_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_difficulty_handicap | True | I32 |  |  |  |
| human | True | Boolean |  |  |  |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| effect_value | False | F32 |  |  |  |
| optional_campaign_key | False | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## campaign_effect_scope_agent_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| agent_key | True | StringU8 |  | [agents_tables](#agents_tables) | key |
| campaign_effect_scope_key | True | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## campaign_effect_scope_character_force_relationship_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_effect_scope_key | True | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| force_relationship_key | True | StringU8 |  | [campaign_effect_scope_character_force_relationships_tables](#campaign_effect_scope_character_force_relationships_tables) | key |
  
## campaign_effect_scopes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_effect_scope_key | True | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| force_relationship_key | True | StringU8 |  | [campaign_effect_scope_character_force_relationships_tables](#campaign_effect_scope_character_force_relationships_tables) | key |
  
## campaign_ground_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_effect_scope_key | True | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| force_relationship_key | True | StringU8 |  | [campaign_effect_scope_character_force_relationships_tables](#campaign_effect_scope_character_force_relationships_tables) | key |
  
## campaign_map_attrition_damages_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_effect_scope_key | True | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| force_relationship_key | True | StringU8 |  | [campaign_effect_scope_character_force_relationships_tables](#campaign_effect_scope_character_force_relationships_tables) | key |
  
## campaign_map_attrition_faction_immunities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| attrition | True | StringU8 |  | [campaign_map_attritions_tables](#campaign_map_attritions_tables) | key |
| faction | True | StringU8 |  | [factions_tables](#factions_tables) | key |
  
## campaign_map_attrition_unit_immunities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| attrition | True | StringU8 |  | [campaign_map_attritions_tables](#campaign_map_attritions_tables) | key |
| unit | True | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
  
## campaign_map_attritions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| attrition | True | StringU8 |  | [campaign_map_attritions_tables](#campaign_map_attritions_tables) | key |
| unit | True | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
  
## campaign_map_playable_areas_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| attrition | True | StringU8 |  | [campaign_map_attritions_tables](#campaign_map_attritions_tables) | key |
| unit | True | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
  
## campaign_map_regions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_map | True | StringU8 |  | [campaign_maps_tables](#campaign_maps_tables) | mapname |
| region | True | StringU8 |  | [regions_tables](#regions_tables) | key |
  
## campaign_map_roads_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign | False | StringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| key | True | StringU8 |  |  |  |
| movement_cost | False | I32 |  |  |  |
| threshold | False | F32 |  |  |  |
| turns_required_to_upgrade_to | False | I32 |  |  |  |
| turns_required_to_downgrade_from | False | I32 |  |  |  |
  
## campaign_map_settlements_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign | False | StringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| key | True | StringU8 |  |  |  |
| movement_cost | False | I32 |  |  |  |
| threshold | False | F32 |  |  |  |
| turns_required_to_upgrade_to | False | I32 |  |  |  |
| turns_required_to_downgrade_from | False | I32 |  |  |  |
  
## campaign_map_tooltips_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| select_context | True | StringU8 |  | [campaign_map_tooltip_select_contexts_tables](#campaign_map_tooltip_select_contexts_tables) | select_context |
| over_context | True | StringU8 |  | [campaign_map_tooltip_over_contexts_tables](#campaign_map_tooltip_over_contexts_tables) | over_contexts |
| tooltip_line | False | OptionalStringU8 |  | [campaign_map_tooltip_texts_tables](#campaign_map_tooltip_texts_tables) | key |
| advice_line | False | OptionalStringU8 |  | [campaign_map_tooltip_texts_tables](#campaign_map_tooltip_texts_tables) | key |
| main_line | False | OptionalStringU8 | first line in the tooltip | [campaign_map_tooltip_texts_tables](#campaign_map_tooltip_texts_tables) | key |
  
## campaign_mp_coop_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## campaign_mp_coop_groups_to_factions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| faction_key | True | StringU8 | A faction to be added to a Multiplayer Coop Group | [factions_tables](#factions_tables) | key |
| mp_coop_group | True | StringU8 | The Multiplayer Coop Group to which the specified faction belongs. | [campaign_mp_coop_groups_tables](#campaign_mp_coop_groups_tables) | key |
  
## campaign_politics_strings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## campaign_public_order_populace_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| culture | True | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| effect_bundle | False | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| populace_happiness | True | StringU8 |  |  |  |
  
## campaign_settlement_display_aqueducts_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building_path | False | OptionalStringU8 |  |  |  |
| position_x_map | False | F32 |  |  |  |
| position_y_map | False | F32 |  |  |  |
| position_z_height | False | F32 |  |  |  |
| region_key | True | StringU8 |  | [regions_tables](#regions_tables) | key |
| rotation_cw_radians | False | F32 |  |  |  |
  
## campaign_settlement_display_building_constructions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building_path | False | OptionalStringU8 |  |  |  |
| position_x_map | False | F32 |  |  |  |
| position_y_map | False | F32 |  |  |  |
| position_z_height | False | F32 |  |  |  |
| region_key | True | StringU8 |  | [regions_tables](#regions_tables) | key |
| rotation_cw_radians | False | F32 |  |  |  |
  
## campaign_settlement_display_building_ids_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building_path | False | OptionalStringU8 |  |  |  |
| position_x_map | False | F32 |  |  |  |
| position_y_map | False | F32 |  |  |  |
| position_z_height | False | F32 |  |  |  |
| region_key | True | StringU8 |  | [regions_tables](#regions_tables) | key |
| rotation_cw_radians | False | F32 |  |  |  |
  
## campaign_settlement_display_building_trees_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| rigid_lookup_key | False | OptionalStringU8 |  |  |  |
| building_path | False | OptionalStringU8 |  |  |  |
| climate_type | False | StringU8 |  | [climates_tables](#climates_tables) | climate_type |
| id | True | I64 |  |  |  |
  
## campaign_settlement_display_buildings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| rigid_lookup_key | False | OptionalStringU8 |  |  |  |
| building_path | False | OptionalStringU8 |  |  |  |
| climate_type | False | StringU8 |  | [climates_tables](#climates_tables) | climate_type |
| id | True | I64 |  |  |  |
  
## campaign_settlement_display_siege_item_ids_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| battlefield_deployable_siege_item | True | StringU8 |  | [battlefield_deployable_siege_items_tables](#battlefield_deployable_siege_items_tables) | key |
| sprawl_piece | False | StringU8 |  | [campaign_settlement_display_sprawl_pieces_tables](#campaign_settlement_display_sprawl_pieces_tables) | key |
  
## campaign_settlement_display_sprawl_pieces_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## campaign_stance_effects_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## campaign_stances_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## campaign_statistics_categories_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| category_order | False | I32 |  |  |  |
| key | True | StringU8 |  |  |  |
  
## campaign_statistics_strings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_statistic | True | StringU8 |  | [campaign_statistics_enums_tables](#campaign_statistics_enums_tables) | key |
| campaign_statistic_category | False | StringU8 |  | [campaign_statistics_categories_tables](#campaign_statistics_categories_tables) | key |
| statistic_order | False | I32 |  |  |  |
  
## campaign_subject_evolutions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| arrival_message | False | OptionalStringU8 |  | [campaign_subject_messages_tables](#campaign_subject_messages_tables) | key |
| campaign_subject_key | False | StringU8 |  | [campaign_subjects_tables](#campaign_subjects_tables) | key |
| departure_message | False | OptionalStringU8 |  | [campaign_subject_messages_tables](#campaign_subject_messages_tables) | key |
| effect_bundle_key | False | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| flavour_text | False | OptionalStringU8 |  | [campaign_subject_strings_tables](#campaign_subject_strings_tables) | key |
| key | True | StringU8 |  |  |  |
| max_turns | False | I32 |  |  |  |
| min_turns | False | I32 |  |  |  |
| weighting | False | F32 |  |  |  |
  
## campaign_subject_faction_restriction_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_subject_key | True | StringU8 |  | [campaign_subjects_tables](#campaign_subjects_tables) | key |
| faction_key | True | StringU8 |  | [factions_tables](#factions_tables) | key |
  
## campaign_subject_messages_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| message_type | False | StringU8 |  | [message_events_tables](#message_events_tables) | event |
  
## campaign_subject_strings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## campaign_subjects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| flavour_text | False | StringU8 |  | [campaign_subject_strings_tables](#campaign_subject_strings_tables) | key |
| key | True | StringU8 |  |  |  |
| male | False | Boolean |  |  |  |
| optional_name | False | OptionalStringU8 |  | [campaign_subject_strings_tables](#campaign_subject_strings_tables) | key |
| optional_name_source_faction | False | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| ui_image | False | StringU8 |  |  |  |
  
## campaign_unit_stat_bonuses_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| bonus | True | StringU8 |  |  |  |
| icon_path | False | StringU8 |  |  |  |
| level | True | I32 |  |  |  |
| threshold | False | I32 |  |  |  |
| upgrade_cost_new | False | I32 |  |  |  |
| upgrade_cost_from_previous_level | False | I32 |  |  |  |
  
## campaign_variables_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| variable_key | True | StringU8 |  |  |  |
| value | False | F32 |  |  |  |
  
## campaign_vfx_descriptions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| variable_key | True | StringU8 |  |  |  |
| value | False | F32 |  |  |  |
  
## campaign_vfx_lookups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| agent_filter | False | OptionalStringU8 |  | [agents_tables](#agents_tables) | key |
| culture_filter | False | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| faction_filter | False | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| key | True | I64 |  |  |  |
| vfx_description | False | StringU8 |  | [campaign_vfx_descriptions_tables](#campaign_vfx_descriptions_tables) | key |
| vfx_event | False | StringU8 |  | [campaign_vfx_campaign_vfx_event_ids_tables](#campaign_vfx_campaign_vfx_event_ids_tables) | campaign_vfx_event |
  
## campaigns_campaign_variables_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| variable_key | True | StringU8 |  | [campaign_variables_tables](#campaign_variables_tables) | variable_key |
| campaign_name | True | StringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| value | False | F32 |  |  |  |
| optional_difficulty_level | True | OptionalStringU8 |  |  |  |
| optional_campaign_type | True | OptionalStringU8 |  |  |  |
  
## campaigns_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_name | True | StringU8 |  |  |  |
| map_name | False | StringU8 |  | [campaign_maps_tables](#campaign_maps_tables) | mapname |
| is_grand | False | Boolean |  |  |  |
| campaign_order | False | I32 |  |  |  |
| exportable | False | Boolean |  |  |  |
| display_location | False | OptionalStringU8 |  |  |  |
| is_tutorial | False | Boolean |  |  |  |
| banner_icon | False | OptionalStringU8 |  |  |  |
| banner_image | False | OptionalStringU8 |  |  |  |
| available_for_mp | False | Boolean |  |  |  |
| mp_sort_order | False | I32 | Sort order for MPC selection drop down |  |  |
  
## capture_point_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_name | True | StringU8 |  |  |  |
| map_name | False | StringU8 |  | [campaign_maps_tables](#campaign_maps_tables) | mapname |
| is_grand | False | Boolean |  |  |  |
| campaign_order | False | I32 |  |  |  |
| exportable | False | Boolean |  |  |  |
| display_location | False | OptionalStringU8 |  |  |  |
| is_tutorial | False | Boolean |  |  |  |
| banner_icon | False | OptionalStringU8 |  |  |  |
| banner_image | False | OptionalStringU8 |  |  |  |
| available_for_mp | False | Boolean |  |  |  |
| mp_sort_order | False | I32 | Sort order for MPC selection drop down |  |  |
  
## cdir_army_template_ratios_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| ratio | False | I32 |  |  |  |
| template | True | StringU8 |  |  |  |
| unit | True | StringU8 |  |  |  |
  
## cdir_campaign_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| campaign | False | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## cdir_configs_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_key | True | StringU8 |  | [cdir_campaign_junctions_tables](#cdir_campaign_junctions_tables) | key |
| faction_key | True | OptionalStringU8 |  | [cdir_faction_junctions_tables](#cdir_faction_junctions_tables) | key |
| cdir_config_key | True | StringU8 |  | [cdir_config_values_tables](#cdir_config_values_tables) | key |
| value | False | OptionalStringU8 |  |  |  |
  
## cdir_desire_priorities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_key | True | StringU8 |  | [cdir_campaign_junctions_tables](#cdir_campaign_junctions_tables) | key |
| desire_key | True | StringU8 |  | [cdir_desires_tables](#cdir_desires_tables) | key |
| priority | False | I32 |  |  |  |
  
## cdir_events_dilemma_choice_details_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| choice_key | True | StringU8 |  | [cdir_events_dilemma_choices_tables](#cdir_events_dilemma_choices_tables) | choice_key |
| dilemma_key | True | StringU8 |  | [dilemmas_tables](#dilemmas_tables) | key |
  
## cdir_events_dilemma_followup_dilemmas_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| choice_key | True | StringU8 |  | [cdir_events_dilemma_choices_tables](#cdir_events_dilemma_choices_tables) | choice_key |
| dilemma_key | True | StringU8 |  | [dilemmas_tables](#dilemmas_tables) | key |
| followup_dilemma_key | True | StringU8 |  | [dilemmas_tables](#dilemmas_tables) | key |
  
## cdir_events_dilemma_followup_missions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| dilemma_key | True | StringU8 |  | [dilemmas_tables](#dilemmas_tables) | key |
| choice_key | True | StringU8 |  | [cdir_events_dilemma_choices_tables](#cdir_events_dilemma_choices_tables) | choice_key |
| followup_mission_key | True | StringU8 |  | [missions_tables](#missions_tables) | key |
  
## cdir_events_dilemma_incidents_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| choice_key | True | StringU8 |  | [cdir_events_dilemma_choices_tables](#cdir_events_dilemma_choices_tables) | choice_key |
| dilemma_key | True | StringU8 |  | [dilemmas_tables](#dilemmas_tables) | key |
| incident_key | True | StringU8 |  | [incidents_tables](#incidents_tables) | key |
  
## cdir_events_dilemma_option_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| choice_key | True | StringU8 |  | [cdir_events_dilemma_choices_tables](#cdir_events_dilemma_choices_tables) | choice_key |
| dilemma_key | True | StringU8 |  | [dilemmas_tables](#dilemmas_tables) | key |
| incident_key | True | StringU8 |  | [incidents_tables](#incidents_tables) | key |
  
## cdir_events_dilemma_payloads_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| choice_key | False | StringU8 |  | [cdir_events_dilemma_choices_tables](#cdir_events_dilemma_choices_tables) | choice_key |
| dilemma_key | False | StringU8 |  | [dilemmas_tables](#dilemmas_tables) | key |
| id | True | I64 |  |  |  |
| payload_key | False | StringU8 |  | [cdir_events_payloads_tables](#cdir_events_payloads_tables) | payload_key |
| value | False | OptionalStringU8 |  |  |  |
  
## cdir_events_incident_followup_dilemmas_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| incident_key | True | StringU8 |  | [incidents_tables](#incidents_tables) | key |
| followup_dliemma_key | True | StringU8 |  | [dilemmas_tables](#dilemmas_tables) | key |
  
## cdir_events_incident_followup_incidents_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| incident_key | True | StringU8 |  | [incidents_tables](#incidents_tables) | key |
| followup_incident_key | True | StringU8 |  | [incidents_tables](#incidents_tables) | key |
  
## cdir_events_incident_followup_missions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| incident_key | True | StringU8 |  | [incidents_tables](#incidents_tables) | key |
| followup_mission_key | True | StringU8 |  | [missions_tables](#missions_tables) | key |
  
## cdir_events_incident_option_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| incident_key | True | StringU8 |  | [incidents_tables](#incidents_tables) | key |
| followup_mission_key | True | StringU8 |  | [missions_tables](#missions_tables) | key |
  
## cdir_events_incident_payloads_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| incident_key | True | StringU8 |  | [incidents_tables](#incidents_tables) | key |
| followup_mission_key | True | StringU8 |  | [missions_tables](#missions_tables) | key |
  
## cdir_events_mission_followup_dilemmas_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| mission_key | True | StringU8 |  | [missions_tables](#missions_tables) | key |
| status_key | True | StringU8 |  | [cdir_events_mission_statuses_tables](#cdir_events_mission_statuses_tables) | status_key |
| followup_dilemma_key | True | StringU8 |  | [dilemmas_tables](#dilemmas_tables) | key |
  
## cdir_events_mission_followup_missions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| mission_key | True | StringU8 |  | [missions_tables](#missions_tables) | key |
| status_key | True | StringU8 |  | [cdir_events_mission_statuses_tables](#cdir_events_mission_statuses_tables) | status_key |
| followup_mission_key | True | StringU8 |  | [missions_tables](#missions_tables) | key |
  
## cdir_events_mission_incidents_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| incident_key | True | StringU8 |  | [incidents_tables](#incidents_tables) | key |
| mission_key | True | StringU8 |  | [missions_tables](#missions_tables) | key |
| status_key | True | StringU8 |  | [cdir_events_mission_statuses_tables](#cdir_events_mission_statuses_tables) | status_key |
  
## cdir_events_mission_issuer_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| issuer_key | True | StringU8 |  | [mission_issuers_tables](#mission_issuers_tables) | issuer_key |
| mission_key | True | StringU8 |  | [missions_tables](#missions_tables) | key |
  
## cdir_events_mission_option_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| issuer_key | True | StringU8 |  | [mission_issuers_tables](#mission_issuers_tables) | issuer_key |
| mission_key | True | StringU8 |  | [missions_tables](#missions_tables) | key |
  
## cdir_events_mission_payloads_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | I64 |  |  |  |
| mission_key | False | StringU8 |  | [missions_tables](#missions_tables) | key |
| payload_key | False | StringU8 |  | [cdir_events_payloads_tables](#cdir_events_payloads_tables) | payload_key |
| status_key | False | StringU8 |  | [cdir_events_mission_statuses_tables](#cdir_events_mission_statuses_tables) | status_key |
| value | False | StringU8 |  |  |  |
  
## cdir_events_payloads_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect_bundle_key | False | OptionalStringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| payload_key | True | StringU8 |  |  |  |
  
## cdir_faction_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| faction | False | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
  
## cdir_military_generator_configs_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cdir_military_generator_template_priorities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| config_key | True | StringU8 |  | [cdir_military_generator_configs_tables](#cdir_military_generator_configs_tables) | key |
| priority | False | I32 |  |  |  |
| template_key | True | StringU8 |  | [cdir_military_generator_templates_tables](#cdir_military_generator_templates_tables) | key |
  
## cdir_military_generator_template_ratios_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| ratio | False | I32 |  |  |  |
| template_key | True | StringU8 |  | [cdir_military_generator_templates_tables](#cdir_military_generator_templates_tables) | key |
| unit_group_key | True | StringU8 |  | [cdir_military_generator_unit_groups_tables](#cdir_military_generator_unit_groups_tables) | key |
  
## cdir_military_generator_templates_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cdir_military_generator_unit_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cdir_military_generator_unit_qualities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| group_key | True | StringU8 |  | [cdir_military_generator_unit_groups_tables](#cdir_military_generator_unit_groups_tables) | key |
| quality | False | I32 |  |  |  |
| unit_key | True | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
  
## cdir_unit_balance_group_qualities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| config_key | False | StringU8 |  |  |  |
| group_key | False | StringU8 |  |  |  |
| quality_group_key | False | StringU8 |  |  |  |
| quality | False | I32 |  |  |  |
  
## cdir_unit_balance_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | False | StringU8 |  |  |  |
| army | False | Boolean |  |  |  |
  
## cdir_unit_balance_template_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| config_key | False | StringU8 |  |  |  |
| template_key | False | StringU8 |  |  |  |
| priority | False | I32 |  |  |  |
  
## cdir_unit_balances_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| template_key | False | StringU8 |  |  |  |
| min_units | False | I32 |  |  |  |
| max_units | False | I32 |  |  |  |
| group_key | False | StringU8 |  |  |  |
| ideal_pct | False | F32 |  |  |  |
| variance | False | F32 |  |  |  |
| min_required | False | I32 |  |  |  |
  
## cdir_unit_qualities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| config_key | False | StringU8 |  |  |  |
| group_key | False | StringU8 |  |  |  |
| unit_key | False | StringU8 |  |  |  |
| quality | False | I32 |  |  |  |
  
## centralised_upgrade_building_level_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| upgraded_building_level | True | StringU8 | The level to which the dependent buildings will be upgraded. | [building_levels_tables](#building_levels_tables) | level_name |
| central_building_level | False | StringU8 | The required level of the central building. | [building_levels_tables](#building_levels_tables) | level_name |
| priority | True | I32 | Used when more than one central building is in effect. |  |  |
  
## character_experience_skill_tiers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| agent_key | True | OptionalStringU8 |  | [agents_tables](#agents_tables) | key |
| experience_threshold | False | I32 |  |  |  |
| skill_points | False | I32 |  |  |  |
| skill_rank | True | I32 |  |  |  |
| optional_campaign_key | True | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| for_army | True | Boolean |  |  |  |
| for_navy | True | Boolean |  |  |  |
  
## character_skill_level_details_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_key | True | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| faction_key | True | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| image_path | False | StringU8 |  |  |  |
| level | True | I32 |  |  |  |
| skill_key | True | StringU8 |  | [character_skills_tables](#character_skills_tables) | key |
| subculture_key | True | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| unlocked_at_rank | False | I32 |  |  |  |
  
## character_skill_level_to_effects_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| character_skill_key | True | StringU8 |  | [character_skills_tables](#character_skills_tables) | key |
| effect_key | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| level | True | I32 |  |  |  |
| value | False | F32 |  |  |  |
  
## character_skill_node_links_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| character_skill_key | True | StringU8 |  | [character_skills_tables](#character_skills_tables) | key |
| effect_key | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| level | True | I32 |  |  |  |
| value | False | F32 |  |  |  |
  
## character_skill_node_sets_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| character_skill_key | True | StringU8 |  | [character_skills_tables](#character_skills_tables) | key |
| effect_key | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| level | True | I32 |  |  |  |
| value | False | F32 |  |  |  |
  
## character_skill_nodes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| character_skill_key | True | StringU8 |  | [character_skills_tables](#character_skills_tables) | key |
| effect_key | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| level | True | I32 |  |  |  |
| value | False | F32 |  |  |  |
  
## character_skills_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| character_skill_key | True | StringU8 |  | [character_skills_tables](#character_skills_tables) | key |
| effect_key | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| level | True | I32 |  |  |  |
| value | False | F32 |  |  |  |
  
## character_trait_levels_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| character_skill_key | True | StringU8 |  | [character_skills_tables](#character_skills_tables) | key |
| effect_key | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| level | True | I32 |  |  |  |
| value | False | F32 |  |  |  |
  
## character_traits_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| character_skill_key | True | StringU8 |  | [character_skills_tables](#character_skills_tables) | key |
| effect_key | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| level | True | I32 |  |  |  |
| value | False | F32 |  |  |  |
  
## chariot_types_enums_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## chat_shortcuts_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| game_area | False | StringU8 |  | [game_area_enums_tables](#game_area_enums_tables) | key |
| key | True | StringU8 |  |  |  |
  
## climates_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| game_area | False | StringU8 |  | [game_area_enums_tables](#game_area_enums_tables) | key |
| key | True | StringU8 |  |  |  |
  
## commander_unit_permissions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| culture_key | True | OptionalStringU8 |  | [cultures_tables](#cultures_tables) | key |
| faction_key | True | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| subculture_key | True | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| unit_key | True | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
  
## commodities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| culture_key | True | OptionalStringU8 |  | [cultures_tables](#cultures_tables) | key |
| faction_key | True | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| subculture_key | True | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| unit_key | True | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
  
## commodity_unit_names_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| unit | True | StringU8 |  |  |  |
  
## culture_settlement_occupation_options_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| unit | True | StringU8 |  |  |  |
  
## culture_subculture_character_portraits_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| culture | True | OptionalStringU8 |  | [cultures_tables](#cultures_tables) | key |
| faction | True | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| path | False | StringU8 |  |  |  |
| portrait_type | True | StringU8 |  | [portrait_types_tables](#portrait_types_tables) | key |
| subculture | True | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## culture_subculture_politics_government_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| culture | True | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| government_type | True | StringU8 |  | [politics_government_types_tables](#politics_government_types_tables) | government_type |
| on_screen_name_faction_leader | False | OptionalStringU8 |  |  |  |
| on_screen_name_government_type | False | StringU8 |  |  |  |
| faction | True | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| effect_bundle | False | OptionalStringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| is_default | False | Boolean |  |  |  |
| faction_leader_trait | False | StringU8 |  | [trait_info_tables](#trait_info_tables) | trait |
| on_screen_name_faction_female_leader | False | OptionalStringU8 |  |  |  |
| faction_leader_trait_female | False | StringU8 |  | [trait_info_tables](#trait_info_tables) | trait |
| on_screen_name_government_actions | False | OptionalStringU8 |  |  |  |
| on_screen_descr_government_actions | False | OptionalStringU8 |  |  |  |
  
## cultures_subcultures_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| culture | True | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| government_type | True | StringU8 |  | [politics_government_types_tables](#politics_government_types_tables) | government_type |
| on_screen_name_faction_leader | False | OptionalStringU8 |  |  |  |
| on_screen_name_government_type | False | StringU8 |  |  |  |
| faction | True | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| effect_bundle | False | OptionalStringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| is_default | False | Boolean |  |  |  |
| faction_leader_trait | False | StringU8 |  | [trait_info_tables](#trait_info_tables) | trait |
| on_screen_name_faction_female_leader | False | OptionalStringU8 |  |  |  |
| faction_leader_trait_female | False | StringU8 |  | [trait_info_tables](#trait_info_tables) | trait |
| on_screen_name_government_actions | False | OptionalStringU8 |  |  |  |
| on_screen_descr_government_actions | False | OptionalStringU8 |  |  |  |
  
## cultures_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| culture | True | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| government_type | True | StringU8 |  | [politics_government_types_tables](#politics_government_types_tables) | government_type |
| on_screen_name_faction_leader | False | OptionalStringU8 |  |  |  |
| on_screen_name_government_type | False | StringU8 |  |  |  |
| faction | True | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| effect_bundle | False | OptionalStringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| is_default | False | Boolean |  |  |  |
| faction_leader_trait | False | StringU8 |  | [trait_info_tables](#trait_info_tables) | trait |
| on_screen_name_faction_female_leader | False | OptionalStringU8 |  |  |  |
| faction_leader_trait_female | False | StringU8 |  | [trait_info_tables](#trait_info_tables) | trait |
| on_screen_name_government_actions | False | OptionalStringU8 |  |  |  |
| on_screen_descr_government_actions | False | OptionalStringU8 |  |  |  |
  
## cursor_transitions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| initiating_cursor | True | StringU8 |  | [cursors_tables](#cursors_tables) | key |
| mouse_event | True | StringU8 | Event that triggers transition | [cursor_mouse_events_tables](#cursor_mouse_events_tables) | key |
| resulting_cursor | False | StringU8 |  | [cursors_tables](#cursors_tables) | key |
  
## cursors_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| initiating_cursor | True | StringU8 |  | [cursors_tables](#cursors_tables) | key |
| mouse_event | True | StringU8 | Event that triggers transition | [cursor_mouse_events_tables](#cursor_mouse_events_tables) | key |
| resulting_cursor | False | StringU8 |  | [cursors_tables](#cursors_tables) | key |
  
## cursus_honorum_level_requirements_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| age | False | I32 |  |  |  |
| level | True | I32 |  |  |  |
| rank | False | I32 |  |  |  |
| subculture_key | True | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| faction_key | True | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
  
## cursus_honorum_trait_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| subculture_key | True | StringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| trait_info_key | True | StringU8 |  | [trait_info_tables](#trait_info_tables) | trait |
| faction_key | True | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| trait_info_key_female | True | OptionalStringU8 |  | [trait_info_tables](#trait_info_tables) | trait |
  
## death_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| subculture_key | True | StringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| trait_info_key | True | StringU8 |  | [trait_info_tables](#trait_info_tables) | trait |
| faction_key | True | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| trait_info_key_female | True | OptionalStringU8 |  | [trait_info_tables](#trait_info_tables) | trait |
  
## deployables_custom_battles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| cap | False | I32 |  |  |  |
| deployable | True | StringU8 |  | [deployables_tables](#deployables_tables) | key |
| probability | False | I32 |  |  |  |
  
## deployables_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| cap | False | I32 |  |  |  |
| deployable | True | StringU8 |  | [deployables_tables](#deployables_tables) | key |
| probability | False | I32 |  |  |  |
  
## dilemma_to_campaign_subject_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_subject_key | True | StringU8 |  | [campaign_subjects_tables](#campaign_subjects_tables) | key |
| dilemma_key | True | StringU8 |  | [dilemmas_tables](#dilemmas_tables) | key |
| weighting | False | F32 |  |  |  |
  
## dilemmas_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_subject_key | True | StringU8 |  | [campaign_subjects_tables](#campaign_subjects_tables) | key |
| dilemma_key | True | StringU8 |  | [dilemmas_tables](#dilemmas_tables) | key |
| weighting | False | F32 |  |  |  |
  
## diplomacy_current_treaties_to_diplomatic_options_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| can_be_cancelled | False | Boolean |  |  |  |
| current_treaty_key | True | StringU8 |  | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| diplomatic_option_key | False | StringU8 |  | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
  
## diplomacy_keys_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## diplomacy_negotiation_attitude_override_strings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| attitude | True | StringU8 |  | [diplomacy_negotiation_attitudes_tables](#diplomacy_negotiation_attitudes_tables) | key |
| culture | True | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| government_type | True | StringU8 |  | [government_types_tables](#government_types_tables) | government_type |
| key | True | StringU8 |  | [diplomacy_keys_tables](#diplomacy_keys_tables) | key |
| option | True | I32 |  |  |  |
| string | False | StringU8 |  | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
  
## diplomacy_negotiation_attitudes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| maximum_attitude | False | I32 |  |  |  |
| minimum_attitude | False | I32 |  |  |  |
  
## diplomacy_negotiation_faction_attitude_override_strings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| attitude | True | StringU8 |  | [diplomacy_negotiation_attitudes_tables](#diplomacy_negotiation_attitudes_tables) | key |
| culture | True | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| faction | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| government_type | True | StringU8 |  | [government_types_tables](#government_types_tables) | government_type |
| key | True | StringU8 |  | [diplomacy_keys_tables](#diplomacy_keys_tables) | key |
| option | True | I32 |  |  |  |
| string | False | StringU8 |  | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
  
## diplomacy_negotiation_faction_override_strings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  | [diplomacy_keys_tables](#diplomacy_keys_tables) | key |
| culture | True | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| government_type | True | StringU8 |  | [government_types_tables](#government_types_tables) | government_type |
| faction | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| string | False | StringU8 |  | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| option | True | I32 |  |  |  |
  
## diplomacy_negotiation_string_options_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  | [diplomacy_keys_tables](#diplomacy_keys_tables) | key |
| culture | True | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| government_type | True | StringU8 |  | [government_types_tables](#government_types_tables) | government_type |
| faction | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| string | False | StringU8 |  | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| option | True | I32 |  |  |  |
  
## diplomacy_negotiation_strings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| culture | True | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| government_type | True | StringU8 |  | [government_types_tables](#government_types_tables) | government_type |
| key | True | StringU8 |  | [diplomacy_keys_tables](#diplomacy_keys_tables) | key |
  
## diplomacy_strings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## diplomatic_action_faction_restrictions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| can_make_client_states | False | Boolean |  |  |  |
| can_make_confederations | False | Boolean |  |  |  |
| can_make_vassals | False | Boolean |  |  |  |
| faction | True | StringU8 |  | [factions_tables](#factions_tables) | key |
  
## diplomatic_action_subculture_restrictions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| can_make_client_states | False | Boolean |  |  |  |
| can_make_confederations | False | Boolean |  |  |  |
| can_make_vassals | False | Boolean |  |  |  |
| subculture | True | StringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## diplomatic_relations_attitudes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| attitude | True | StringU8 |  |  |  |
| value | False | I32 |  |  |  |
  
## diplomatic_relations_religion_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| attitude | True | StringU8 |  |  |  |
| value | False | I32 |  |  |  |
  
## effect_bonus_value_agent_junction_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | StringU8 |  | [campaign_bonus_value_ids_agent_tables](#campaign_bonus_value_ids_agent_tables) | key |
| agent | True | StringU8 |  | [agents_tables](#agents_tables) | key |
  
## effect_bonus_value_basic_junction_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | StringU8 |  | [campaign_bonus_value_ids_basic_tables](#campaign_bonus_value_ids_basic_tables) | key |
  
## effect_bonus_value_battle_context_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| battle_context_key | False | StringU8 |  | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| bonus_value_id | True | StringU8 |  | [campaign_bonus_value_ids_battle_contexts_tables](#campaign_bonus_value_ids_battle_contexts_tables) | key |
| effect_key | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
  
## effect_bonus_value_battlefield_deployables_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| battlefield_deployable | True | StringU8 |  | [deployables_tables](#deployables_tables) | key |
| bonus_value_id | True | StringU8 |  | [campaign_bonus_value_ids_battlefield_deployables_tables](#campaign_bonus_value_ids_battlefield_deployables_tables) | key |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
  
## effect_bonus_value_building_chain_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | StringU8 |  | [campaign_bonus_value_ids_building_chain_tables](#campaign_bonus_value_ids_building_chain_tables) | key |
| building_chain | True | StringU8 |  | [building_chains_tables](#building_chains_tables) | key |
  
## effect_bonus_value_building_set_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| bonus_value_id | True | StringU8 |  | [campaign_bonus_value_ids_building_sets_tables](#campaign_bonus_value_ids_building_sets_tables) | key |
| building_set | True | StringU8 |  | [building_sets_tables](#building_sets_tables) | key |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
  
## effect_bonus_value_id_action_results_additional_outcomes_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| action_results_additional_outcome_record | True | StringU8 |  | [action_results_additional_outcomes_tables](#action_results_additional_outcomes_tables) | key |
| bonus_value_id | True | StringU8 |  | [campaign_bonus_value_ids_action_results_additional_outcomes_tables](#campaign_bonus_value_ids_action_results_additional_outcomes_tables) | key |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
  
## effect_bonus_value_ids_unit_sets_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| bonus_value_id | True | StringU8 |  | [campaign_bonus_value_ids_unit_sets_tables](#campaign_bonus_value_ids_unit_sets_tables) | key |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| unit_set | True | StringU8 |  | [unit_sets_tables](#unit_sets_tables) | key |
  
## effect_bonus_value_projectile_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| bonus_value | True | StringU8 |  | [campaign_bonus_value_ids_projectile_tables](#campaign_bonus_value_ids_projectile_tables) | key |
| projectile | True | StringU8 |  | [projectiles_tables](#projectiles_tables) | key |
  
## effect_bonus_value_provincial_initiative_effect_record_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| bonus_value_id | True | StringU8 |  | [campaign_bonus_value_ids_provincial_initiative_effect_records_tables](#campaign_bonus_value_ids_provincial_initiative_effect_records_tables) | key |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_bonus_will_modify | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
  
## effect_bonus_value_religion_junction_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | StringU8 |  | [campaign_bonus_value_ids_religion_tables](#campaign_bonus_value_ids_religion_tables) | key |
| religion | True | StringU8 |  | [religions_tables](#religions_tables) | religion_key |
  
## effect_bonus_value_resource_junction_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | StringU8 |  | [campaign_bonus_value_ids_resource_tables](#campaign_bonus_value_ids_resource_tables) | key |
| resource | True | StringU8 |  | [resources_tables](#resources_tables) | key |
  
## effect_bonus_value_siege_item_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| bonus_value_id | True | StringU8 |  | [campaign_bonus_value_ids_siege_items_tables](#campaign_bonus_value_ids_siege_items_tables) | key |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| siege_item | True | StringU8 |  | [battlefield_deployable_siege_items_tables](#battlefield_deployable_siege_items_tables) | key |
  
## effect_bonus_value_technology_category_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| bonus_value_id | True | StringU8 |  | [campaign_bonus_value_ids_technology_categories_tables](#campaign_bonus_value_ids_technology_categories_tables) | key |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| technology_category | True | StringU8 |  | [technology_categories_tables](#technology_categories_tables) | key |
  
## effect_bonus_value_unit_ability_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | StringU8 |  | [campaign_bonus_value_ids_unit_ability_tables](#campaign_bonus_value_ids_unit_ability_tables) | key |
| unit_ability | True | StringU8 |  | [unit_abilities_tables](#unit_abilities_tables) | key |
  
## effect_bonus_value_unit_caste_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| bonus_value_id | True | StringU8 |  | [campaign_bonus_value_ids_unit_caste_tables](#campaign_bonus_value_ids_unit_caste_tables) | key |
| caste | True | StringU8 |  | [unit_castes_tables](#unit_castes_tables) | caste |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
  
## effect_bonus_value_unit_category_junction_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | StringU8 |  | [campaign_bonus_value_ids_unit_category_tables](#campaign_bonus_value_ids_unit_category_tables) | key |
| unit_category | True | StringU8 |  | [unit_category_tables](#unit_category_tables) | key |
  
## effect_bonus_value_unit_class_junction_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | StringU8 |  | [campaign_bonus_value_ids_unit_class_tables](#campaign_bonus_value_ids_unit_class_tables) | key |
| unit_class | True | StringU8 |  | [unit_class_tables](#unit_class_tables) | key |
  
## effect_bonus_value_unit_record_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| bonus_value_id | True | StringU8 |  | [campaign_bonus_value_ids_unit_records_tables](#campaign_bonus_value_ids_unit_records_tables) | key |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| unit_record_key | True | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
  
## effect_bundle_advancement_stages_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## effect_bundles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| localised_description | False | StringU8 |  |  |  |
| localised_title | False | StringU8 |  |  |  |
| ui_icon | False | StringU8 |  |  |  |
| bundle_target | False | StringU8 |  | [effect_bundle_targets_tables](#effect_bundle_targets_tables) | key |
  
## effect_bundles_to_effects_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect_bundle_key | True | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| effect_key | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| value | False | F32 |  |  |  |
| advancement_stage | False | OptionalStringU8 |  | [effect_bundle_advancement_stages_tables](#effect_bundle_advancement_stages_tables) | key |
  
## effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect_bundle_key | True | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| effect_key | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| value | False | F32 |  |  |  |
| advancement_stage | False | OptionalStringU8 |  | [effect_bundle_advancement_stages_tables](#effect_bundle_advancement_stages_tables) | key |
  
## encyclopedia_blocks_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| block_key | True | StringU8 |  |  |  |
| class | False | StringU8 |  |  |  |
| image | False | OptionalStringU8 |  |  |  |
| image_class | False | StringU8 |  |  |  |
| order | False | I32 |  |  |  |
| page_key | False | StringU8 |  | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
  
## encyclopedia_building_redirects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building | True | StringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| redirect_building | False | StringU8 | building to redirect the user to if 'building' was clicked on | [building_levels_tables](#building_levels_tables) | level_name |
  
## encyclopedia_page_linkages_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| next_key | False | OptionalStringU8 |  | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
| page_key | True | StringU8 |  | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
| parent_key | False | OptionalStringU8 |  | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
  
## encyclopedia_page_related_links_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| page_key | True | StringU8 |  | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
| target | True | StringU8 |  | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
  
## encyclopedia_pages_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| page_key | True | StringU8 |  |  |  |
| template | False | StringU8 |  |  |  |
  
## encyclopedia_template_strings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| string_key | True | StringU8 |  |  |  |
  
## encyclopedia_unit_redirects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| redirect_unit | False | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
| unit | True | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
  
## entity_training_levels_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| training_level | True | StringU8 |  |  |  |
| max_offset_distance | False | F32 |  |  |  |
  
## event_log_descriptions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| event_key | True | StringU8 |  |  |  |
| optional_campaign_key | False | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| has_position | False | Boolean |  |  |  |
| icon | False | StringU8 |  |  |  |
| is_region_position | False | Boolean |  |  |  |
| movie_id | False | I32 |  |  |  |
  
## experience_triggers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| event_key | True | StringU8 |  |  |  |
| optional_campaign_key | False | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| has_position | False | Boolean |  |  |  |
| icon | False | StringU8 |  |  |  |
| is_region_position | False | Boolean |  |  |  |
| movie_id | False | I32 |  |  |  |
  
## faction_banners_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| primary_blue | False | I32 |  |  |  |
| primary_green | False | I32 |  |  |  |
| primary_red | False | I32 |  |  |  |
| secondary_blue | False | I32 |  |  |  |
| secondary_green | False | I32 |  |  |  |
| secondary_red | False | I32 |  |  |  |
| symbol | False | OptionalStringU8 |  |  |  |
| tertiary_blue | False | I32 |  |  |  |
| tertiary_green | False | I32 |  |  |  |
| tertiary_red | False | I32 |  |  |  |
  
## faction_civil_war_setups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| primary_faction | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| secondary_faction | False | StringU8 |  | [factions_tables](#factions_tables) | key |
| secessionist_faction | False | StringU8 |  | [factions_tables](#factions_tables) | key |
  
## faction_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| primary_faction | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| secondary_faction | False | StringU8 |  | [factions_tables](#factions_tables) | key |
| secessionist_faction | False | StringU8 |  | [factions_tables](#factions_tables) | key |
  
## faction_political_parties_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| faction_key | False | StringU8 |  | [factions_tables](#factions_tables) | key |
| political_party_key | True | StringU8 |  | [political_parties_tables](#political_parties_tables) | key |
  
## faction_politics_government_actions_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| description | False | StringU8 |  |  |  |
| faction | True | StringU8 | The faction for which this action is defined. | [factions_tables](#factions_tables) | key |
| id | True | StringU8 | An id for the action. Will be passed to lua for TRIGGER_EVENT-type actions. |  |  |
| image_path | False | StringU8 |  |  |  |
| title | False | StringU8 |  |  |  |
| type | True | StringU8 | One of the hardcoded action types. | [politics_government_actions_tables](#politics_government_actions_tables) | key |
| cost | False | I32 | Fixed cost in gold for this action. |  |  |
| cost_per_region | False | I32 | Cost per owned region, used to make the action more expensive for large factions. |  |  |
| cooldown | False | I32 | Cooldown in turns. The cooldown counter is shared for all actions. |  |  |
  
## faction_rebellion_units_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| faction_key | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| unit_key | True | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
  
## faction_resource_consumptions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| number_of_regions | True | I32 |  |  |  |
| resource_consumption | False | I32 |  |  |  |
  
## faction_to_campaign_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign | False | StringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| faction | True | StringU8 |  | [factions_tables](#factions_tables) | key |
  
## faction_to_faction_groups_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| faction_group_key | False | StringU8 |  | [faction_groups_tables](#faction_groups_tables) | key |
| faction_key | True | StringU8 |  | [factions_tables](#factions_tables) | key |
  
## faction_to_mercenary_set_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| faction | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| mercenary_set | True | StringU8 |  | [mercenary_pools_tables](#mercenary_pools_tables) | key |
  
## faction_uniform_colours_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| faction | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| mercenary_set | True | StringU8 |  | [mercenary_pools_tables](#mercenary_pools_tables) | key |
  
## faction_variables_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| description | False | OptionalStringU8 |  |  |  |
| faction_variable_key | True | StringU8 |  |  |  |
| value | False | StringU8 |  |  |  |
  
## factions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| description | False | OptionalStringU8 |  |  |  |
| faction_variable_key | True | StringU8 |  |  |  |
| value | False | StringU8 |  |  |  |
  
## fame_levels_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| description | False | OptionalStringU8 |  |  |  |
| faction_variable_key | True | StringU8 |  |  |  |
| value | False | StringU8 |  |  |  |
  
## family_relationship_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| relationship_type | True | StringU8 |  |  |  |
  
## famous_battle_pools_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| relationship_type | True | StringU8 |  |  |  |
  
## female_character_culture_details_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| chance_to_spawn | False | I32 | values: (>= 0) - chance to spawn female character (in percent). If not set (value < 0) -> the value is read from female_character_faction_spawn_rates. |  |  |
| culture | True | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| general | False | StringU8 | values: ("y" / "n") - the ability to "raise a force" from a settlement. |  |  |
| public_office | False | StringU8 | values: ("y" / "n") - access to the "Secure Promotion" action, as well as the ability to be faction and party leader. |  |  |
| missions | False | StringU8 | values: ("y" / "n") - access to any and all actions listed as missions (Diplomat, Administrator, Organize Feast + the new Political Marriage, Diplomatic Marriage, Dynastic Marriage). |  |  |
| trait | False | OptionalStringU8 | special trait gives females bonus to missions. | [trait_info_tables](#trait_info_tables) | trait |
  
## female_character_faction_details_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| chance_to_spawn | False | I32 | values: (>= 0) - chance to spawn female character (in percent). If not set (value < 0) -> the value is read from female_character_subculture_details |  |  |
| faction | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| general | False | OptionalStringU8 | values: ("y" / "n" / not set ) - the ability to "raise a force" from a settlement. If not set -> the value is read from female_character_subculture_details |  |  |
| public_office | False | OptionalStringU8 | values: ("y" / "n" / not set ) - access to the "Secure Promotion" action, as well as the ability to be faction and party leader. If not set -> the value is read from female_character_subculture_details |  |  |
| missions | False | OptionalStringU8 | values: ("y" / "n" / not set ) - access to any and all actions listed as missions (Diplomat, Administrator, Organize Feast + the new Political Marriage, Diplomatic Marriage, Dynastic Marriage). If not set -> the value is read from female_character_subculture_details |  |  |
| trait | False | OptionalStringU8 | special trait gives females bonus to missions. If not set the value is read from female_character_subculture_details | [trait_info_tables](#trait_info_tables) | trait |
  
## female_character_subculture_details_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| chance_to_spawn | False | I32 | values: (>= 0) - chance to spawn female character (in percent). If not set (value < 0) -> the value is read from female_character_culture_details |  |  |
| general | False | OptionalStringU8 | values: ("y" / "n" / not set ) - the ability to "raise a force" from a settlement. If not set -> the value is read from female_character_culture_details |  |  |
| public_office | False | OptionalStringU8 | values: ("y" / "n" / not set ) - access to the "Secure Promotion" action, as well as the ability to be faction and party leader. If not set -> the value is read from female_character_culture_details |  |  |
| missions | False | OptionalStringU8 | values: ("y" / "n" / not set ) - access to any and all actions listed as missions (Diplomat, Administrator, Organize Feast + the new Political Marriage, Diplomatic Marriage, Dynastic Marriage). If not set -> the value is read from female_character_culture_details |  |  |
| subculture | True | StringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| trait | False | OptionalStringU8 | special trait gives females bonus to missions. If not set the value is read from female_character_culture_details | [trait_info_tables](#trait_info_tables) | trait |
  
## first_person_engines_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| chance_to_spawn | False | I32 | values: (>= 0) - chance to spawn female character (in percent). If not set (value < 0) -> the value is read from female_character_culture_details |  |  |
| general | False | OptionalStringU8 | values: ("y" / "n" / not set ) - the ability to "raise a force" from a settlement. If not set -> the value is read from female_character_culture_details |  |  |
| public_office | False | OptionalStringU8 | values: ("y" / "n" / not set ) - access to the "Secure Promotion" action, as well as the ability to be faction and party leader. If not set -> the value is read from female_character_culture_details |  |  |
| missions | False | OptionalStringU8 | values: ("y" / "n" / not set ) - access to any and all actions listed as missions (Diplomat, Administrator, Organize Feast + the new Political Marriage, Diplomatic Marriage, Dynastic Marriage). If not set -> the value is read from female_character_culture_details |  |  |
| subculture | True | StringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| trait | False | OptionalStringU8 | special trait gives females bonus to missions. If not set the value is read from female_character_culture_details | [trait_info_tables](#trait_info_tables) | trait |
  
## font_names_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| font_name | True | StringU8 |  |  |  |
  
## fonts_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| bold | True | Boolean | Whether font is a bold font |  |  |
| key | True | StringU8 |  | [font_names_tables](#font_names_tables) | font_name |
| size | True | I32 | Size of font |  |  |
  
## formations_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| formation | True | StringU8 |  |  |  |
| icon_name | False | StringU8 | Name of icon to use for formation button |  |  |
| is_army | False | Boolean | Is formation for applying to whole army |  |  |
| is_naval | False | Boolean | Is the formation for naval purposes |  |  |
| order | False | I32 | Determines order formation buttons shown in ui |  |  |
  
## formations_to_subcultures_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| formation | True | StringU8 |  | [formations_tables](#formations_tables) | formation |
| sub_culture | True | StringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## fort_underlay_climate_jcts_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| fort_name | True | StringU16 |  | [battlefield_buildings_tables](#battlefield_buildings_tables) | key |
| climate | True | StringU16 |  | [climates_tables](#climates_tables) | climate_type |
| snow_underlay | True | Boolean |  |  |  |
| underlay | False | StringU16 |  | [battle_terrain_farms_tables](#battle_terrain_farms_tables) | farm |
  
## frontend_faction_leaders_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| fort_name | True | StringU16 |  | [battlefield_buildings_tables](#battlefield_buildings_tables) | key |
| climate | True | StringU16 |  | [climates_tables](#climates_tables) | climate_type |
| snow_underlay | True | Boolean |  |  |  |
| underlay | False | StringU16 |  | [battle_terrain_farms_tables](#battle_terrain_farms_tables) | farm |
  
## game_area_enums_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## general_command_star_level_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| alive_morale_bonus | False | I32 |  |  |  |
| command_star_level | True | I32 |  |  |  |
| melee_attack_bonus | False | I32 |  |  |  |
| melee_defence_bonus | False | I32 |  |  |  |
| nearby_morale_bonus | False | I32 |  |  |  |
  
## government_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| alive_morale_bonus | False | I32 |  |  |  |
| command_star_level | True | I32 |  |  |  |
| melee_attack_bonus | False | I32 |  |  |  |
| melee_defence_bonus | False | I32 |  |  |  |
| nearby_morale_bonus | False | I32 |  |  |  |
  
## governorships_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| governorship | True | StringU8 |  |  |  |
  
## ground_type_to_stat_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| governorship | True | StringU8 |  |  |  |
  
## ground_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| governorship | True | StringU8 |  |  |  |
  
## groupings_military_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| military_group | True | StringU8 |  |  |  |
  
## historical_battles_ui_locations_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  | [battles_tables](#battles_tables) | key |
| x | False | I32 |  |  |  |
| y | False | I32 |  |  |  |
| height_percent | False | I32 |  |  |  |
  
## historical_character_traits_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| character | True | StringU8 |  | [historical_characters_tables](#historical_characters_tables) | key |
| trait | True | StringU8 |  | [character_trait_levels_tables](#character_trait_levels_tables) | key |
  
## historical_characters_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| character | True | StringU8 |  | [historical_characters_tables](#historical_characters_tables) | key |
| trait | True | StringU8 |  | [character_trait_levels_tables](#character_trait_levels_tables) | key |
  
## honour_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| applies_to_ai | False | Boolean |  |  |  |
| factor | False | StringU8 |  | [honour_factors_tables](#honour_factors_tables) | key |
| key | True | StringU8 |  |  |  |
| value | False | I32 |  |  |  |
  
## honour_factors_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| maximum_value | False | I32 |  |  |  |
| minimum_value | False | I32 |  |  |  |
  
## incident_heading_texts_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU16 |  |  |  |
| text | False | StringU16 |  |  |  |
  
## incidents_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU16 |  |  |  |
| text | False | StringU16 |  |  |  |
  
## land_units_officers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU16 |  |  |  |
| text | False | StringU16 |  |  |  |
  
## land_units_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU16 |  |  |  |
| text | False | StringU16 |  |  |  |
  
## land_units_to_unit_abilites_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| ability | True | StringU8 |  | [unit_abilities_tables](#unit_abilities_tables) | key |
| land_unit | True | StringU8 |  | [land_units_tables](#land_units_tables) | key |
  
## loyalty_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| applies_to_ai | False | Boolean |  |  |  |
| factor | False | StringU8 |  | [loyalty_factors_tables](#loyalty_factors_tables) | key |
| key | True | StringU8 |  |  |  |
| value | False | I32 |  |  |  |
  
## loyalty_factors_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| maximum_value | False | I32 |  |  |  |
| minimum_value | False | I32 |  |  |  |
  
## main_units_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| maximum_value | False | I32 |  |  |  |
| minimum_value | False | I32 |  |  |  |
  
## marriage_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## melee_weapons_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## mercenary_pool_modifiers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| cost_modifier | False | F32 |  |  |  |
| culture_origin_match | False | Boolean |  |  |  |
| key | True | StringU8 |  |  |  |
| min_pool_culture_percentage | False | I32 |  |  |  |
| pool_type | False | StringU8 |  | [mercenary_pool_type_enums_tables](#mercenary_pool_type_enums_tables) | pool_type |
| replenishment_modifier | False | F32 |  |  |  |
  
## mercenary_pool_to_groups_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| group | False | StringU8 |  | [mercenary_unit_groups_tables](#mercenary_unit_groups_tables) | key |
| initial_unit_count | False | I32 |  |  |  |
| key | True | I32 |  |  |  |
| pool | False | StringU8 |  | [mercenary_pools_tables](#mercenary_pools_tables) | key |
| faction_requirement | False | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| subculture_requirement | False | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| tech_requirement | False | OptionalStringU8 |  | [technologies_tables](#technologies_tables) | key |
  
## mercenary_pool_type_enums_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| pool_type | True | StringU8 |  |  |  |
  
## mercenary_pools_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## mercenary_unit_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## message_event_strings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| event | True | StringU8 |  | [message_events_tables](#message_events_tables) | event |
| optional_campaign_key | True | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| culture | True | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| text | False | StringU8 |  | [message_event_text_tables](#message_event_text_tables) | key |
| image | False | StringU8 |  |  |  |
| icon | False | StringU8 |  |  |  |
| sound_event | False | StringU8 |  |  |  |
| optional_subculture | True | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## message_events_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| event | True | StringU8 |  |  |  |
| instant_open | False | Boolean |  |  |  |
| layout | False | StringU8 |  | [message_event_layout_types_tables](#message_event_layout_types_tables) | Type |
| requires_response | False | Boolean |  |  |  |
| priority | False | I32 | Messages with a higher priority will be opened over those with a lower priority. 100 is standard for all messages. |  |  |
  
## military_force_legacy_emblems_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| event | True | StringU8 |  |  |  |
| instant_open | False | Boolean |  |  |  |
| layout | False | StringU8 |  | [message_event_layout_types_tables](#message_event_layout_types_tables) | Type |
| requires_response | False | Boolean |  |  |  |
| priority | False | I32 | Messages with a higher priority will be opened over those with a lower priority. 100 is standard for all messages. |  |  |
  
## military_force_legacy_names_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| event | True | StringU8 |  |  |  |
| instant_open | False | Boolean |  |  |  |
| layout | False | StringU8 |  | [message_event_layout_types_tables](#message_event_layout_types_tables) | Type |
| requires_response | False | Boolean |  |  |  |
| priority | False | I32 | Messages with a higher priority will be opened over those with a lower priority. 100 is standard for all messages. |  |  |
  
## ministerial_effectiveness_modifiers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| leader_minister_level | True | I32 |  |  |  |
| government_type | True | StringU8 |  | [government_types_tables](#government_types_tables) | government_type |
| effectiveness_bonus | False | I32 |  |  |  |
  
## ministerial_positions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| leader_minister_level | True | I32 |  |  |  |
| government_type | True | StringU8 |  | [government_types_tables](#government_types_tables) | government_type |
| effectiveness_bonus | False | I32 |  |  |  |
  
## ministerial_positions_to_character_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| minister_level | True | I32 |  |  |  |
| position | True | StringU8 |  | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| ui_id | False | I32 |  |  |  |
| value | False | I32 |  |  |  |
  
## ministerial_positions_to_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| position | True | StringU8 |  | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| value | False | I32 |  |  |  |
| minister_level | True | I32 |  |  |  |
| ui_id | False | I32 |  |  |  |
  
## missile_weapons_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| position | True | StringU8 |  | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| value | False | I32 |  |  |  |
| minister_level | True | I32 |  |  |  |
| ui_id | False | I32 |  |  |  |
  
## missile_weapons_to_projectiles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| missile_weapon | True | StringU8 |  | [missile_weapons_tables](#missile_weapons_tables) | key |
| projectile | True | StringU8 |  | [projectiles_tables](#projectiles_tables) | key |
  
## mission_issuers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| missile_weapon | True | StringU8 |  | [missile_weapons_tables](#missile_weapons_tables) | key |
| projectile | True | StringU8 |  | [projectiles_tables](#projectiles_tables) | key |
  
## missions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| missile_weapon | True | StringU8 |  | [missile_weapons_tables](#missile_weapons_tables) | key |
| projectile | True | StringU8 |  | [projectiles_tables](#projectiles_tables) | key |
  
## models_deployables_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| display_path | False | OptionalStringU8 |  |  |  |
| key | True | StringU8 |  |  |  |
| logic_file | False | StringU8 |  |  |  |
| model_file | False | StringU8 |  |  |  |
  
## models_entity_weapons_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| logic_file | False | StringU8 |  |  |  |
| model_file | False | StringU8 |  |  |  |
  
## models_oars_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| left_row | False | OptionalStringU8 |  |  |  |
| key | True | StringU8 |  |  |  |
| rigid_model | False | OptionalStringU8 |  |  |  |
| left_end | False | OptionalStringU8 |  |  |  |
| right_row | False | OptionalStringU8 |  |  |  |
| right_end | False | OptionalStringU8 |  |  |  |
  
## mount_variants_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| mount_key | False | StringU8 |  | [mounts_tables](#mounts_tables) | key |
| display_key | False | StringU8 |  |  |  |
| weight | False | F32 |  |  |  |
  
## mountable_artillery_units_custom_battles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| cap | False | I32 |  |  |  |
| mountable_artillery | True | StringU8 |  | [mountable_artillery_units_tables](#mountable_artillery_units_tables) | unit_key |
| probability | False | I32 |  |  |  |
| faction | True | StringU8 |  | [factions_tables](#factions_tables) | key |
  
## mountable_artillery_units_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| unit_key | True | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
  
## mounts_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| unit_key | True | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
  
## movie_event_strings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| event | True | StringU8 |  |  |  |
| culture | True | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| movie | False | StringU8 |  |  |  |
| id | False | StringU8 |  |  |  |
  
## mp_budgets_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| budget | False | I32 |  |  |  |
| budget_size_key | False | StringU8 |  | [mp_budget_sizes_tables](#mp_budget_sizes_tables) | key |
| key | True | StringU8 |  |  |  |
| land | False | Boolean |  |  |  |
| siege_defender | False | Boolean |  |  |  |
  
## mp_force_gen_army_sizes_by_budgets_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| budget | True | StringU8 |  | [mp_budgets_tables](#mp_budgets_tables) | key |
| maximum_unit_count | False | I32 |  |  |  |
| minimum_unit_count | True | I32 |  |  |  |
  
## mp_force_gen_template_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| budget | True | StringU8 |  | [mp_budgets_tables](#mp_budgets_tables) | key |
| maximum_unit_count | False | I32 |  |  |  |
| minimum_unit_count | True | I32 |  |  |  |
  
## multiplayer_mininum_length_funds_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| value | False | F32 |  |  |  |
  
## name_orders_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| name_group | True | I32 |  | [names_groups_tables](#names_groups_tables) | key |
| order | True | I32 |  |  |  |
| type | True | StringU8 |  | [name_types_tables](#name_types_tables) | key |
  
## names_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | I32 |  |  |  |
  
## names_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| names_group | False | I32 |  | [names_groups_tables](#names_groups_tables) | key |
| type | False | I32 |  | [name_types_tables](#name_types_tables) | key |
| gender | False | I32 |  | [genders_tables](#genders_tables) | gender |
| frequency | False | I32 |  |  |  |
| id | True | StringU8 |  |  |  |
  
## naval_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect_name | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| key | True | StringU8 |  |  |  |
  
## naval_fire_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| chance_of_fire | False | F32 | percentage chance of catching fire when hit by projectile |  |  |
| incendiary_level | True | StringU8 |  | [projectile_incendiary_enum_tables](#projectile_incendiary_enum_tables) | key |
| unit_category | True | StringU8 |  | [unit_category_tables](#unit_category_tables) | key |
  
## naval_ramming_events_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| base_damage | False | I32 |  |  |  |
| key | True | StringU8 |  |  |  |
| rammed_ship | False | StringU8 |  | [unit_category_tables](#unit_category_tables) | key |
| ramming_ship | False | StringU8 |  | [unit_category_tables](#unit_category_tables) | key |
  
## naval_units_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| base_damage | False | I32 |  |  |  |
| key | True | StringU8 |  |  |  |
| rammed_ship | False | StringU8 |  | [unit_category_tables](#unit_category_tables) | key |
| ramming_ship | False | StringU8 |  | [unit_category_tables](#unit_category_tables) | key |
  
## naval_units_to_unit_abilites_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| ability | True | StringU8 |  | [unit_abilities_tables](#unit_abilities_tables) | key |
| naval_unit | True | StringU8 |  | [naval_units_tables](#naval_units_tables) | key |
  
## naval_weapons_enums_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| types | True | StringU8 |  |  |  |
  
## naval_weapons_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| types | True | StringU8 |  |  |  |
  
## particle_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## pdlc_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| ID | True | StringU8 |  |  |  |
| SteamID | False | I32 |  |  |  |
| description | False | OptionalStringU8 |  |  |  |
| release_order | False | I32 |  |  |  |
  
## plagues_permitted_campaigns_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign | True | StringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| plague | True | StringU8 |  | [plagues_tables](#plagues_tables) | name |
  
## plagues_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| grade | False | I32 |  |  |  |
| infectivity | False | I32 |  |  |  |
| lifetime | False | I32 |  |  |  |
| region_effect_bundle | False | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| minimum_squalor | False | I32 |  |  |  |
| name | True | StringU8 |  |  |  |
| military_force_effect_bundle | False | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
  
## political_actions_effect_bundles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| action | True | StringU8 |  |  |  |
| effect_bundle | False | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| duration | False | I32 |  |  |  |
  
## political_actions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| action | True | StringU8 |  |  |  |
| effect_bundle | False | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| duration | False | I32 |  |  |  |
  
## political_parties_loyalty_effect_bundles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| bundle_key | True | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| loyalty | True | I32 |  |  |  |
  
## political_parties_power_effect_bundles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect_bundle | True | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| political_party_key | True | StringU8 |  | [political_parties_tables](#political_parties_tables) | key |
| power_level | False | I32 |  |  |  |
  
## political_parties_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect_bundle | True | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| political_party_key | True | StringU8 |  | [political_parties_tables](#political_parties_tables) | key |
| power_level | False | I32 |  |  |  |
  
## political_traits_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 | The id of the political party trait |  |  |
| onscreen_name | False | StringU8 | The name of the trait, shown in the politics UI |  |  |
| description | False | OptionalStringU8 | Localized description of the trait. |  |  |
  
## politics_government_actions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## politics_government_type_political_action_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| government_type | True | StringU8 |  | [politics_government_types_tables](#politics_government_types_tables) | government_type |
| is_available_for_faction_leader | False | Boolean |  |  |  |
| is_available_for_non_ruling_party_leaders | False | Boolean |  |  |  |
| is_available_for_non_ruling_party_members | False | Boolean |  |  |  |
| is_available_for_ruling_party_members | False | Boolean |  |  |  |
| political_action | True | StringU8 |  | [political_actions_tables](#political_actions_tables) | political_action_key |
  
## politics_government_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| government_type | True | StringU8 |  |  |  |
  
## population_classes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| government_type | True | StringU8 |  |  |  |
  
## portrait_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## pre_battle_speeches_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| text | False | StringU8 |  |  |  |
| type | False | I32 |  | [pre_battle_speech_types_enum_tables](#pre_battle_speech_types_enum_tables) | index |
| parameter | False | OptionalStringU8 |  | [pre_battle_speech_parameters_enum_tables](#pre_battle_speech_parameters_enum_tables) | key |
  
## projectile_displays_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| text | False | StringU8 |  |  |  |
| type | False | I32 |  | [pre_battle_speech_types_enum_tables](#pre_battle_speech_types_enum_tables) | index |
| parameter | False | OptionalStringU8 |  | [pre_battle_speech_parameters_enum_tables](#pre_battle_speech_parameters_enum_tables) | key |
  
## projectile_impacts_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| text | False | StringU8 |  |  |  |
| type | False | I32 |  | [pre_battle_speech_types_enum_tables](#pre_battle_speech_types_enum_tables) | index |
| parameter | False | OptionalStringU8 |  | [pre_battle_speech_parameters_enum_tables](#pre_battle_speech_parameters_enum_tables) | key |
  
## projectile_shot_type_enum_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| text | False | StringU8 |  |  |  |
| type | False | I32 |  | [pre_battle_speech_types_enum_tables](#pre_battle_speech_types_enum_tables) | index |
| parameter | False | OptionalStringU8 |  | [pre_battle_speech_parameters_enum_tables](#pre_battle_speech_parameters_enum_tables) | key |
  
## projectile_trails_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | False | StringU8 | delete this field if you see it |  |  |
| type | False | StringU8 |  | [projectiles_trail_types_enum_tables](#projectiles_trail_types_enum_tables) | key |
| width | False | F32 |  |  |  |
| duration | False | F32 |  |  |  |
| min_aparent_width_distance | False | F32 |  |  |  |
| colour_r | False | F32 |  |  |  |
| colour_g | False | F32 |  |  |  |
| colour_b | False | F32 |  |  |  |
| opacity | False | F32 |  |  |  |
| fadeout_distance | False | F32 |  |  |  |
| distortion_cross_fade_start_distance | False | F32 |  |  |  |
| distortion_cross_fade_range | False | F32 |  |  |  |
  
## projectiles_explosions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | False | StringU8 | delete this field if you see it |  |  |
| type | False | StringU8 |  | [projectiles_trail_types_enum_tables](#projectiles_trail_types_enum_tables) | key |
| width | False | F32 |  |  |  |
| duration | False | F32 |  |  |  |
| min_aparent_width_distance | False | F32 |  |  |  |
| colour_r | False | F32 |  |  |  |
| colour_g | False | F32 |  |  |  |
| colour_b | False | F32 |  |  |  |
| opacity | False | F32 |  |  |  |
| fadeout_distance | False | F32 |  |  |  |
| distortion_cross_fade_start_distance | False | F32 |  |  |  |
| distortion_cross_fade_range | False | F32 |  |  |  |
  
## projectiles_missile_type_enum_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | False | StringU8 |  |  |  |
  
## projectiles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | False | StringU8 |  |  |  |
  
## prologue_chapters_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | False | StringU8 |  |  |  |
  
## prologue_loading_screens_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| background_image | False | StringU8 | Path to background graphic |  |  |
| index | True | I64 |  |  |  |
| inset_image | False | StringU8 | Path to inset graphic |  |  |
| pane_on_left | False | Boolean | Is the text pane on the left or the right of the loading screen? |  |  |
| campaign | False | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## province_to_mercenary_set_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| background_image | False | StringU8 | Path to background graphic |  |  |
| index | True | I64 |  |  |  |
| inset_image | False | StringU8 | Path to inset graphic |  |  |
| pane_on_left | False | Boolean | Is the text pane on the left or the right of the loading screen? |  |  |
| campaign | False | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## provinces_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## provincial_initiative_records_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## provincial_initiatives_to_subculture_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| provincial_initiative_key | True | StringU8 |  | [provincial_initiative_records_tables](#provincial_initiative_records_tables) | key |
| subculture | True | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## public_order_factors_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| factor | True | StringU8 |  |  |  |
| positive_pip_path | False | StringU8 |  |  |  |
| negative_pip_path | False | OptionalStringU8 |  |  |  |
| optional_campaign_key | False | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## quotes_people_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| quote_person_key | True | StringU8 |  |  |  |
| quote_person_onscreen | False | StringU8 |  |  |  |
  
## quotes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| quote_onscreen | False | StringU8 |  |  |  |
| quote_person | False | StringU8 |  | [quotes_people_tables](#quotes_people_tables) | quote_person_key |
| key | True | StringU8 |  |  |  |
  
## random_localisation_strings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## region_campaign_overrides_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign | True | StringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| region | True | StringU8 |  | [regions_tables](#regions_tables) | key |
| religion | False | OptionalStringU8 |  | [religions_tables](#religions_tables) | religion_key |
| religion_zeal | False | I32 |  |  |  |
  
## region_economics_factors_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| factor | True | StringU8 |  |  |  |
| positive_pip_path | False | StringU8 |  |  |  |
  
## region_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| factor | True | StringU8 |  |  |  |
| positive_pip_path | False | StringU8 |  |  |  |
  
## region_religions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| region | True | StringU8 |  | [regions_tables](#regions_tables) | key |
| religion | False | StringU8 |  | [religions_tables](#religions_tables) | religion_key |
| religion_zeal | False | I32 |  |  |  |
  
## region_to_province_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| region | True | StringU8 |  | [regions_tables](#regions_tables) | key |
| religion | False | StringU8 |  | [religions_tables](#religions_tables) | religion_key |
| religion_zeal | False | I32 |  |  |  |
  
## region_unit_resources_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| string | False | StringU8 |  |  |  |
  
## regions_continents_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| continent | True | StringU8 |  |  |  |
  
## regions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| continent | True | StringU8 |  |  |  |
  
## regions_to_region_groups_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| continent | True | StringU8 |  |  |  |
  
## religion_conversion_mods_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| rel_from | True | StringU8 |  | [religions_tables](#religions_tables) | religion_key |
| rel_to | True | StringU8 |  | [religions_tables](#religions_tables) | religion_key |
| modifier | False | F32 |  |  |  |
  
## religions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| rel_from | True | StringU8 |  | [religions_tables](#religions_tables) | religion_key |
| rel_to | True | StringU8 |  | [religions_tables](#religions_tables) | religion_key |
| modifier | False | F32 |  |  |  |
  
## resource_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect_key | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| resource_key | True | StringU8 |  | [resources_tables](#resources_tables) | key |
| value | False | F32 |  |  |  |
  
## resources_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect_key | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| resource_key | True | StringU8 |  | [resources_tables](#resources_tables) | key |
| value | False | F32 |  |  |  |
  
## scripted_objectives_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 | Key used by scriptors to trigger |  |  |
  
## scripted_subtitles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 | Key for scriptors to trigger |  |  |
| character_for_vo | False | OptionalStringU8 | In-game character who will provide VO for this line, if any |  |  |
  
## sea_surfaces_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| sea_wind_speed | False | F32 |  |  |  |
| sea_phillips_constant | False | F32 |  |  |  |
| sea_choppiness | False | F32 |  |  |  |
| swell_wind_speed | False | F32 |  |  |  |
| swell_phillips_constant | False | F32 |  |  |  |
| foam_enabled | False | Boolean |  |  |  |
| foam_decay_rate | False | F32 |  |  |  |
| foam_fade_in_time | False | F32 |  |  |  |
| foam_cut_off_value | False | F32 |  |  |  |
| froth_value | False | F32 |  |  |  |
| froth_distortion_speed | False | F32 |  |  |  |
| froth_distortion_amount | False | F32 |  |  |  |
| spray_cut_off_value | False | F32 |  |  |  |
| spray_speed | False | F32 |  |  |  |
| spray_duration | False | F32 |  |  |  |
| sea_shininess | False | F32 |  |  |  |
| sea_decay | False | F32 |  |  |  |
| reflection_flattening_factor | False | F32 |  |  |  |
| wave_trough_y_value | False | F32 |  |  |  |
| detail_normal_uv_scale1 | False | F32 |  |  |  |
| detail_normal_uv_speed1 | False | F32 |  |  |  |
| detail_normal_uv_scale2 | False | F32 |  |  |  |
| detail_normal_uv_speed2 | False | F32 |  |  |  |
  
## season_attritions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| sea_wind_speed | False | F32 |  |  |  |
| sea_phillips_constant | False | F32 |  |  |  |
| sea_choppiness | False | F32 |  |  |  |
| swell_wind_speed | False | F32 |  |  |  |
| swell_phillips_constant | False | F32 |  |  |  |
| foam_enabled | False | Boolean |  |  |  |
| foam_decay_rate | False | F32 |  |  |  |
| foam_fade_in_time | False | F32 |  |  |  |
| foam_cut_off_value | False | F32 |  |  |  |
| froth_value | False | F32 |  |  |  |
| froth_distortion_speed | False | F32 |  |  |  |
| froth_distortion_amount | False | F32 |  |  |  |
| spray_cut_off_value | False | F32 |  |  |  |
| spray_speed | False | F32 |  |  |  |
| spray_duration | False | F32 |  |  |  |
| sea_shininess | False | F32 |  |  |  |
| sea_decay | False | F32 |  |  |  |
| reflection_flattening_factor | False | F32 |  |  |  |
| wave_trough_y_value | False | F32 |  |  |  |
| detail_normal_uv_scale1 | False | F32 |  |  |  |
| detail_normal_uv_speed1 | False | F32 |  |  |  |
| detail_normal_uv_scale2 | False | F32 |  |  |  |
| detail_normal_uv_speed2 | False | F32 |  |  |  |
  
## season_province_effect_bundles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| sea_wind_speed | False | F32 |  |  |  |
| sea_phillips_constant | False | F32 |  |  |  |
| sea_choppiness | False | F32 |  |  |  |
| swell_wind_speed | False | F32 |  |  |  |
| swell_phillips_constant | False | F32 |  |  |  |
| foam_enabled | False | Boolean |  |  |  |
| foam_decay_rate | False | F32 |  |  |  |
| foam_fade_in_time | False | F32 |  |  |  |
| foam_cut_off_value | False | F32 |  |  |  |
| froth_value | False | F32 |  |  |  |
| froth_distortion_speed | False | F32 |  |  |  |
| froth_distortion_amount | False | F32 |  |  |  |
| spray_cut_off_value | False | F32 |  |  |  |
| spray_speed | False | F32 |  |  |  |
| spray_duration | False | F32 |  |  |  |
| sea_shininess | False | F32 |  |  |  |
| sea_decay | False | F32 |  |  |  |
| reflection_flattening_factor | False | F32 |  |  |  |
| wave_trough_y_value | False | F32 |  |  |  |
| detail_normal_uv_scale1 | False | F32 |  |  |  |
| detail_normal_uv_speed1 | False | F32 |  |  |  |
| detail_normal_uv_scale2 | False | F32 |  |  |  |
| detail_normal_uv_speed2 | False | F32 |  |  |  |
  
## seasons_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| sea_wind_speed | False | F32 |  |  |  |
| sea_phillips_constant | False | F32 |  |  |  |
| sea_choppiness | False | F32 |  |  |  |
| swell_wind_speed | False | F32 |  |  |  |
| swell_phillips_constant | False | F32 |  |  |  |
| foam_enabled | False | Boolean |  |  |  |
| foam_decay_rate | False | F32 |  |  |  |
| foam_fade_in_time | False | F32 |  |  |  |
| foam_cut_off_value | False | F32 |  |  |  |
| froth_value | False | F32 |  |  |  |
| froth_distortion_speed | False | F32 |  |  |  |
| froth_distortion_amount | False | F32 |  |  |  |
| spray_cut_off_value | False | F32 |  |  |  |
| spray_speed | False | F32 |  |  |  |
| spray_duration | False | F32 |  |  |  |
| sea_shininess | False | F32 |  |  |  |
| sea_decay | False | F32 |  |  |  |
| reflection_flattening_factor | False | F32 |  |  |  |
| wave_trough_y_value | False | F32 |  |  |  |
| detail_normal_uv_scale1 | False | F32 |  |  |  |
| detail_normal_uv_speed1 | False | F32 |  |  |  |
| detail_normal_uv_scale2 | False | F32 |  |  |  |
| detail_normal_uv_speed2 | False | F32 |  |  |  |
  
## send_diplomat_incidents_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| incident | True | StringU8 |  | [incidents_tables](#incidents_tables) | key |
| outcome | True | StringU8 |  | [send_diplomat_outcomes_tables](#send_diplomat_outcomes_tables) | key |
| culture | True | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| weight | False | I32 | Used to select randomly between all applicable events |  |  |
  
## ship_dbs_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| incident | True | StringU8 |  | [incidents_tables](#incidents_tables) | key |
| outcome | True | StringU8 |  | [send_diplomat_outcomes_tables](#send_diplomat_outcomes_tables) | key |
| culture | True | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| weight | False | I32 | Used to select randomly between all applicable events |  |  |
  
## shortcut_localisation_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | OptionalStringU8 | Key that matches up to default_keys.xml |  |  |
  
## slot_template_to_building_superchain_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building_superchain | False | StringU8 |  | [building_superchains_tables](#building_superchains_tables) | key |
| id | True | StringU8 |  |  |  |
| slot_template | False | StringU8 |  | [slot_templates_tables](#slot_templates_tables) | key |
  
## slot_templates_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building_superchain | False | StringU8 |  | [building_superchains_tables](#building_superchains_tables) | key |
| id | True | StringU8 |  |  |  |
| slot_template | False | StringU8 |  | [slot_templates_tables](#slot_templates_tables) | key |
  
## slot_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| can_convert | False | Boolean |  |  |  |
| can_destroy | False | Boolean |  |  |  |
| key | True | StringU8 |  |  |  |
  
## slots_gdp_values_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| slot | True | StringU8 |  | [slots_tables](#slots_tables) | slot |
| level | True | I32 |  |  |  |
| gdp_value | False | F32 |  |  |  |
| building_gdp_modifier | False | F32 |  |  |  |
  
## slots_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| slot | True | StringU8 |  |  |  |
| is_farm | False | Boolean |  |  |  |
| is_town | False | Boolean |  |  |  |
| is_port | False | Boolean |  |  |  |
| is_resource | False | Boolean |  |  |  |
| supports_building_level_conversion | False | Boolean |  |  |  |
  
## slots_templates_models_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| template_name | True | StringU8 |  |  |  |
| model_filename | False | StringU8 |  |  |  |
| model_filepath | False | StringU8 |  |  |  |
  
## sound_events_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | False | OptionalStringU16 |  |  |  |
  
## special_ability_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | False | OptionalStringU16 |  |  |  |
  
## special_ability_groups_to_factions_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| ability_group | True | StringU8 |  | [special_ability_groups_tables](#special_ability_groups_tables) | ability_group |
| faction | False | StringU8 |  | [factions_tables](#factions_tables) | key |
  
## special_ability_groups_to_unit_abilities_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| special_ability_groups | True | StringU8 |  | [special_ability_groups_tables](#special_ability_groups_tables) | ability_group |
| unit_special_abilities | True | StringU8 |  | [unit_special_abilities_tables](#unit_special_abilities_tables) | key |
  
## special_ability_invalid_usage_flags_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| special_ability_groups | True | StringU8 |  | [special_ability_groups_tables](#special_ability_groups_tables) | ability_group |
| unit_special_abilities | True | StringU8 |  | [unit_special_abilities_tables](#unit_special_abilities_tables) | key |
  
## special_ability_phase_attribute_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| special_ability_groups | True | StringU8 |  | [special_ability_groups_tables](#special_ability_groups_tables) | ability_group |
| unit_special_abilities | True | StringU8 |  | [unit_special_abilities_tables](#unit_special_abilities_tables) | key |
  
## special_ability_phase_stat_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| special_ability_groups | True | StringU8 |  | [special_ability_groups_tables](#special_ability_groups_tables) | ability_group |
| unit_special_abilities | True | StringU8 |  | [unit_special_abilities_tables](#unit_special_abilities_tables) | key |
  
## special_ability_phases_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| special_ability_groups | True | StringU8 |  | [special_ability_groups_tables](#special_ability_groups_tables) | ability_group |
| unit_special_abilities | True | StringU8 |  | [unit_special_abilities_tables](#unit_special_abilities_tables) | key |
  
## special_ability_to_auto_deactivate_flags_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| invalid_usage_flag | True | StringU8 |  | [special_ability_invalid_usage_flags_tables](#special_ability_invalid_usage_flags_tables) | flag_key |
| special_ability_key | True | StringU8 |  | [unit_special_abilities_tables](#unit_special_abilities_tables) | key |
  
## special_ability_to_invalid_usage_flags_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| invalid_usage_flag | True | StringU8 |  | [special_ability_invalid_usage_flags_tables](#special_ability_invalid_usage_flags_tables) | flag_key |
| special_ability | True | StringU8 |  | [unit_special_abilities_tables](#unit_special_abilities_tables) | key |
  
## special_ability_to_special_ability_phase_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| order | True | I32 |  |  |  |
| phase | False | StringU8 |  | [special_ability_phases_tables](#special_ability_phases_tables) | id |
| special_ability | True | StringU8 |  | [unit_special_abilities_tables](#unit_special_abilities_tables) | key |
  
## spotting_and_hiding_values_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| spot_dist_scrub | False | I32 | At what range do we see units hidden in scrub |  |  |
| spot_dist_tree | False | I32 | At what range do we see units hidden in trees |  |  |
| visibility_max_spot_range | False | I32 | We cannot see units after this range |  |  |
| visibility_min_spot_range | False | I32 | We always see units within this range |  |  |
  
## stances_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| onscreen | False | StringU8 |  |  |  |
  
## start_pos_calendars_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign | True | StringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| start_year | False | I32 |  |  |  |
| turns_per_year | False | I32 |  |  |  |
| start_season | False | StringU8 |  | [seasons_tables](#seasons_tables) | season |
| start_week_of_year | False | I32 |  |  |  |
  
## start_pos_character_ancillaries_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | StringU8 |  |  |  |
| character_id | False | StringU8 |  | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
| ancillary | False | StringU8 |  | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
  
## start_pos_character_to_settlements_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| character | True | StringU8 |  | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
| settlement | False | StringU8 |  | [start_pos_settlements_tables](#start_pos_settlements_tables) | id |
  
## start_pos_character_traits_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | StringU8 |  |  |  |
| character_id | False | StringU8 |  | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
| trait_level | False | StringU8 |  | [character_trait_levels_tables](#character_trait_levels_tables) | key |
  
## start_pos_characters_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| ID | True | StringU8 |  |  |  |
| faction | False | StringU8 |  | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| Name | False | StringU8 |  | [names_tables](#names_tables) | id |
| Surname | False | OptionalStringU8 |  | [names_tables](#names_tables) | id |
| Age | False | I32 |  |  |  |
| Type | False | StringU8 |  | [agents_tables](#agents_tables) | key |
| startx | False | F32 |  |  |  |
| starty | False | F32 |  |  |  |
| ministerial_position | False | OptionalStringU8 |  | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| portrait_id | False | OptionalStringU8 |  | [campaign_character_art_sets_tables](#campaign_character_art_sets_tables) | art_set_id |
| model | False | OptionalStringU8 |  |  |  |
| immortal | False | Boolean |  |  |  |
| override_general_unit | False | OptionalStringU8 |  | [main_units_tables](#main_units_tables) | unit |
| is_in_generals_pool | False | Boolean |  |  |  |
| is_male | False | Boolean |  |  |  |
| loyalty | False | I32 |  |  |  |
| clan_name | False | OptionalStringU8 |  | [names_tables](#names_tables) | id |
| other_name | False | OptionalStringU8 |  | [names_tables](#names_tables) | id |
| ambition | False | I32 |  |  |  |
| political_party | False | OptionalStringU8 |  | [political_parties_tables](#political_parties_tables) | key |
| death_type | False | OptionalStringU8 |  | [death_types_tables](#death_types_tables) | key |
| turns_died_before_start | False | OptionalStringU8 |  |  |  |
| progenitor | False | Boolean |  |  |  |
| xp | False | I32 |  |  |  |
  
## start_pos_diplomacy_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | False | StringU8 |  |  |  |
| faction1 | True | StringU8 |  | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| faction2 | True | StringU8 |  | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| stance | False | StringU8 |  | [stances_tables](#stances_tables) | key |
| grants_military_access | False | Boolean |  |  |  |
| grants_trade_agreement | False | Boolean |  |  |  |
| non_aggression_pact | False | Boolean |  |  |  |
  
## start_pos_factions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| ID | True | StringU8 |  |  |  |
| faction | False | StringU8 |  | [factions_tables](#factions_tables) | key |
| campaign | False | StringU8 |  | [start_pos_calendars_tables](#start_pos_calendars_tables) | campaign |
| playable | False | Boolean |  |  |  |
| treasury | False | I32 |  |  |  |
| starting_order | False | I32 |  |  |  |
| government_type | False | StringU8 |  | [government_types_tables](#government_types_tables) | government_type |
| state_religion | False | StringU8 |  | [religions_tables](#religions_tables) | religion_key |
| is_major | False | Boolean |  |  |  |
| difficulty | False | StringU16 |  |  |  |
| ai_manager | False | StringU8 |  | [campaign_ai_managers_tables](#campaign_ai_managers_tables) | manager |
| ai_personality | False | StringU8 |  | [campaign_ai_personalities_tables](#campaign_ai_personalities_tables) | personality |
| long_victory_region_count | False | I32 |  |  |  |
| short_victory_region_count | False | I32 |  |  |  |
| prestige_victory_region_count | False | I32 |  |  |  |
| world_domination_victory_region_count | False | I32 |  |  |  |
| short_victory_year_end | False | I32 |  |  |  |
| long_victory_year_end | False | I32 |  |  |  |
| prestige_victory_year_end | False | I32 |  |  |  |
| world_domination_victory_year_end | False | I32 |  |  |  |
| prestige_army | False | I32 |  |  |  |
| prestige_navy | False | I32 |  |  |  |
| prestige_economy | False | I32 |  |  |  |
| prestige_enlightenment | False | I32 |  |  |  |
| short_victory_week_in_year_end | False | I32 |  |  |  |
| long_victory_week_in_year_end | False | I32 |  |  |  |
| prestige_victory_week_in_year_end | False | I32 |  |  |  |
| world_domination_victory_week_in_year_end | False | I32 |  |  |  |
| honour | False | I32 |  |  |  |
| ai_technology_manager | False | OptionalStringU8 |  | [campaign_ai_technology_managers_tables](#campaign_ai_technology_managers_tables) | key |
| ai_character_skill_tree_manager | False | OptionalStringU8 |  | [campaign_ai_character_skill_tree_managers_tables](#campaign_ai_character_skill_tree_managers_tables) | key |
| cai_agent_distribution_profile | False | StringU8 |  | [cai_agent_distribution_profiles_tables](#cai_agent_distribution_profiles_tables) | key |
| cai_agent_recruitment_profile | False | StringU8 |  | [cai_agent_recruitment_profiles_tables](#cai_agent_recruitment_profiles_tables) | key |
| cai_starting_personality | False | OptionalStringU8 |  | [cai_personalities_tables](#cai_personalities_tables) | key |
| mp_one_vs_one_region_count | False | I32 |  |  |  |
| mp_2p_co_op_region_count | False | I32 |  |  |  |
| mp_2p_co_op_region_count_long | False | I32 |  |  |  |
| long_description | False | OptionalStringU8 |  |  |  |
| can_ever_convert_religion | False | Boolean |  |  |  |
| cdir_military_generator_config | False | StringU8 |  | [cdir_military_generator_configs_tables](#cdir_military_generator_configs_tables) | key |
  
## start_pos_family_relationships_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| character | True | I32 |  | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
| related_to | True | I32 |  | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
| relationship | False | StringU8 |  | [family_relationship_types_tables](#family_relationship_types_tables) | relationship_type |
| bastard | False | Boolean |  |  |  |
| adopted | False | Boolean |  |  |  |
  
## start_pos_land_units_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | StringU8 |  |  |  |
| unit_type | False | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
| general | False | StringU8 |  | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
| soldiers | False | I32 |  |  |  |
  
## start_pos_naval_units_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| ID | True | StringU8 |  |  |  |
| unit_type | False | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
| admiral | False | StringU8 |  | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
  
## start_pos_past_events_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| event | True | StringU8 |  | [cai_personality_diplomatic_events_tables](#cai_personality_diplomatic_events_tables) | id |
| source | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| target | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| turns_ago | True | I32 |  |  |  |
  
## start_pos_region_religions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| region | True | I32 |  | [start_pos_regions_tables](#start_pos_regions_tables) | id |
| religion | True | StringU8 |  | [religions_tables](#religions_tables) | religion_key |
| percentage | False | F32 |  |  |  |
  
## start_pos_region_slot_templates_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign | True | StringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| id | True | StringU8 |  |  |  |
| region | True | StringU8 |  | [regions_tables](#regions_tables) | key |
| slot_template | True | StringU8 |  | [slot_templates_tables](#slot_templates_tables) | key |
| slot_type | True | StringU8 |  | [slot_types_tables](#slot_types_tables) | key |
  
## start_pos_regions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | False | I64 |  |  |  |
| region | True | StringU8 |  | [regions_tables](#regions_tables) | key |
| campaign | True | StringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| owning_faction | False | StringU8 |  | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| faction_capital | False | Boolean |  |  |  |
| base_population | False | I32 |  |  |  |
| base_max_population | False | I32 |  |  |  |
| population | False | I32 |  |  |  |
| base_gdp | False | I32 |  |  |  |
| road_upgrades | False | I32 |  |  |  |
| canals | False | Boolean |  |  |  |
| railways | False | Boolean |  |  |  |
| town_wealth | False | I32 |  |  |  |
| governorship | False | StringU8 |  | [governorships_tables](#governorships_tables) | governorship |
| rebel_faction | False | StringU8 |  | [factions_tables](#factions_tables) | key |
| cultural_originator | False | StringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| settler_rebellions_enabled | False | Boolean |  |  |  |
| capture_prestige | False | I32 |  |  |  |
| alternative_rebel_faction | False | StringU8 |  | [factions_tables](#factions_tables) | key |
| long_description | False | OptionalStringU8 |  |  |  |
| development_points | False | I32 |  |  |  |
  
## start_pos_regions_to_unit_resources_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  | [start_pos_regions_tables](#start_pos_regions_tables) | id |
| resource | True | StringU8 |  | [region_unit_resources_tables](#region_unit_resources_tables) | key |
  
## start_pos_settlements_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| settlement_id | True | StringU8 |  | [campaign_map_settlements_tables](#campaign_map_settlements_tables) | settlement_id |
| region | True | I32 |  | [start_pos_regions_tables](#start_pos_regions_tables) | id |
| building1 | False | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| building2 | False | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| building3 | False | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| building4 | False | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| building5 | False | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| wealth | False | I32 |  |  |  |
| fortification | False | I32 |  |  |  |
| id | False | I64 |  |  |  |
| roads | False | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| fortifications | False | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| primary_building | False | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| port_building | False | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| startpos_slave_points | False | I32 |  |  |  |
  
## start_pos_technologies_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| faction | True | StringU8 |  | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| technology | True | StringU8 |  | [technologies_tables](#technologies_tables) | key |
  
## start_pos_victory_conditions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| start_pos_faction | True | StringU8 |  | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| region | True | StringU8 |  | [regions_tables](#regions_tables) | key |
| victory_type | True | StringU8 |  | [victory_types_tables](#victory_types_tables) | victory_type |
  
## state_gift_values_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| value | False | I32 |  |  |  |
  
## stats_clans_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| label | False | OptionalStringU8 |  | [random_localisation_strings_tables](#random_localisation_strings_tables) | key |
| public | False | Boolean |  |  |  |
| ladder | False | Boolean |  |  |  |
  
## stats_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| label | False | OptionalStringU8 |  | [random_localisation_strings_tables](#random_localisation_strings_tables) | key |
| public | False | Boolean |  |  |  |
| ladder | False | Boolean |  |  |  |
  
## subtitle_timings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| label | False | OptionalStringU8 |  | [random_localisation_strings_tables](#random_localisation_strings_tables) | key |
| public | False | Boolean |  |  |  |
| ladder | False | Boolean |  |  |  |
  
## taxes_classes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| tax | True | StringU8 |  |  |  |
  
## taxes_effects_jct_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| tax | True | StringU8 |  |  |  |
  
## taxes_keys_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| tax_class | True | StringU8 |  | [taxes_classes_tables](#taxes_classes_tables) | tax |
| tax_level | True | StringU8 |  | [taxes_levels_tables](#taxes_levels_tables) | tax_level |
| tax_lookup | False | StringU8 |  |  |  |
  
## taxes_levels_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| tax_level | True | StringU8 |  |  |  |
| percentage | False | I32 |  |  |  |
  
## team_colours_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| alliance | False | I32 |  |  |  |
| b | True | I32 |  |  |  |
| g | True | I32 |  |  |  |
| r | True | I32 |  |  |  |
| army_index | False | I32 |  |  |  |
  
## technologies_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| alliance | False | I32 |  |  |  |
| b | True | I32 |  |  |  |
| g | True | I32 |  |  |  |
| r | True | I32 |  |  |  |
| army_index | False | I32 |  |  |  |
  
## technology_categories_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| position | False | I32 |  |  |  |
  
## technology_category_modules_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect_bundle | False | OptionalStringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| max_tier | True | I32 |  |  |  |
| min_tier | False | I32 |  |  |  |
| technology_node_set | True | StringU8 |  | [technology_node_sets_tables](#technology_node_sets_tables) | key |
  
## technology_category_parents_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| child_category | True | StringU8 |  | [technology_categories_tables](#technology_categories_tables) | key |
| parent_category | True | StringU8 |  | [technology_categories_tables](#technology_categories_tables) | key |
  
## technology_effects_junction_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| technology | True | StringU8 |  | [technologies_tables](#technologies_tables) | key |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| value | False | F32 |  |  |  |
  
## technology_node_links_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| technology | True | StringU8 |  | [technologies_tables](#technologies_tables) | key |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| value | False | F32 |  |  |  |
  
## technology_node_sets_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| technology | True | StringU8 |  | [technologies_tables](#technologies_tables) | key |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| value | False | F32 |  |  |  |
  
## technology_nodes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| technology | True | StringU8 |  | [technologies_tables](#technologies_tables) | key |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| value | False | F32 |  |  |  |
  
## technology_required_building_levels_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| technology | True | StringU8 |  | [technologies_tables](#technologies_tables) | key |
| required_building_level | True | StringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
  
## technology_required_technology_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| technology | True | StringU8 |  | [technologies_tables](#technologies_tables) | key |
| required_technology | True | StringU8 |  | [technologies_tables](#technologies_tables) | key |
  
## technology_unit_upgrades_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| cost | False | I32 |  |  |  |
| target_unit | False | OptionalStringU8 |  | [main_units_tables](#main_units_tables) | unit |
| technology | True | StringU8 |  | [technologies_tables](#technologies_tables) | key |
| unit | True | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
  
## terrain_tilesets_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| tileset_name | True | StringU8 |  |  |  |
  
## town_wealth_growth_factors_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| factor | True | StringU8 |  |  |  |
| positive_pip_path | False | StringU8 |  |  |  |
| negative_pip_path | False | StringU8 |  |  |  |
  
## trade_details_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| icon_filepath | False | StringU8 |  |  |  |
  
## trade_display_campaign_originating_culture_trade_model_options_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign | False | StringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| key | True | I64 |  |  |  |
| model | False | StringU8 |  | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| originating_culture | False | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| priority | False | F32 |  |  |  |
| relative_frequency | False | F32 |  |  |  |
  
## trade_display_campaign_owning_culture_produced_resource_trade_model_options_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign | False | StringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| key | True | I64 |  |  |  |
| model | False | StringU8 |  | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| owning_culture | False | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| priority | False | F32 |  |  |  |
| produced_resource | False | StringU8 |  | [resources_tables](#resources_tables) | key |
| relative_frequency | False | F32 |  |  |  |
  
## trade_display_campaign_owning_culture_trade_model_options_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign | False | StringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| key | True | I64 |  |  |  |
| model | False | StringU8 |  | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| owning_culture | False | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| priority | False | F32 |  |  |  |
| relative_frequency | False | F32 |  |  |  |
  
## trade_display_campaign_trade_model_options_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign | False | StringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| key | True | I64 |  |  |  |
| model | False | StringU8 |  | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | F32 |  |  |  |
| relative_frequency | False | StringU8 |  |  |  |
  
## trade_display_generic_trade_model_options_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | I64 |  |  |  |
| model | False | StringU8 |  | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | F32 |  |  |  |
| relative_frequency | False | F32 |  |  |  |
  
## trade_display_originating_culture_trade_model_options_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | I64 |  |  |  |
| model | False | StringU8 |  | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| originating_culture | False | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| priority | False | F32 |  |  |  |
| relative_frequency | False | F32 |  |  |  |
  
## trade_display_originating_subculture_trade_model_options_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | I64 |  |  |  |
| model | False | StringU8 |  | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| originating_subculture | False | StringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| priority | False | F32 |  |  |  |
| relative_frequency | False | F32 |  |  |  |
  
## trade_display_owning_culture_trade_model_options_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | I64 |  |  |  |
| model | False | StringU8 |  | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| owning_culture | False | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| priority | False | F32 |  |  |  |
| relative_frequency | False | F32 |  |  |  |
  
## trade_display_owning_faction_trade_model_options_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | I64 |  |  |  |
| model | False | StringU8 |  | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| owning_faction | False | StringU8 |  | [factions_tables](#factions_tables) | key |
| priority | False | F32 |  |  |  |
| relative_frequency | False | F32 |  |  |  |
  
## trade_display_produced_resource_trade_model_options_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | I64 |  |  |  |
| model | False | StringU8 |  | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | F32 |  |  |  |
| produced_resource | False | StringU8 |  | [resources_tables](#resources_tables) | key |
| relative_frequency | False | F32 |  |  |  |
  
## trade_display_trade_models_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| is_naval | False | Boolean |  |  |  |
| key | True | StringU8 |  |  |  |
| model | False | StringU8 |  | [warscape_animated_tables](#warscape_animated_tables) | key |
| optional_following_model | False | OptionalStringU8 |  | [warscape_animated_tables](#warscape_animated_tables) | key |
| optional_following_model_distance | False | F32 |  |  |  |
  
## trade_node_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## trait_categories_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| category | True | StringU8 |  |  |  |
| icon_path | False | OptionalStringU8 |  |  |  |
  
## trait_info_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| category | True | StringU8 |  |  |  |
| icon_path | False | OptionalStringU8 |  |  |  |
  
## trait_level_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| trait_level | True | StringU8 |  | [character_trait_levels_tables](#character_trait_levels_tables) | key |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| value | False | F32 |  |  |  |
  
## trait_to_antitraits_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| antitrait | True | StringU8 |  | [trait_info_tables](#trait_info_tables) | trait |
| trait | True | StringU8 |  | [trait_info_tables](#trait_info_tables) | trait |
  
## trait_to_included_agents_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| trait | True | StringU8 |  | [trait_info_tables](#trait_info_tables) | trait |
| agent | True | StringU8 |  | [agents_tables](#agents_tables) | key |
  
## trees_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| tree_id | False | StringU16 |  |  |  |
| distance_to_coast | False | I32 |  |  |  |
| shrub | False | Boolean |  |  |  |
| high_altitude | False | Boolean |  |  |  |
| conifer | False | Boolean |  |  |  |
  
## trigger_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | StringU8 |  |  |  |
| trigger | False | StringU8 |  | [trait_triggers_tables](#trait_triggers_tables) | trigger |
| trait | False | StringU8 |  | [trait_info_tables](#trait_info_tables) | trait |
| value | False | I32 |  |  |  |
| chance | False | I32 |  |  |  |
  
## trigger_events_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| event | True | StringU8 |  |  |  |
  
## ui_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 | Key for ui_effect |  |  |
| banner_fx | False | OptionalStringU8 | Effect that plays around base of unit banner | [particle_effects_tables](#particle_effects_tables) | key |
| ping_fx | False | OptionalStringU8 | Effect that plays around effect icon that appears on top of banner | [particle_effects_tables](#particle_effects_tables) | key |
  
## ui_unit_stat_to_classes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 | Key for ui_effect |  |  |
| banner_fx | False | OptionalStringU8 | Effect that plays around base of unit banner | [particle_effects_tables](#particle_effects_tables) | key |
| ping_fx | False | OptionalStringU8 | Effect that plays around effect icon that appears on top of banner | [particle_effects_tables](#particle_effects_tables) | key |
  
## ui_unit_stats_filters_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## ui_unit_stats_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## unit_abilities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## unit_armour_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## unit_attributes_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| group_name | True | StringU8 |  |  |  |
  
## unit_attributes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| group_name | True | StringU8 |  |  |  |
  
## unit_attributes_to_groups_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| attribute | True | StringU8 |  | [unit_attributes_tables](#unit_attributes_tables) | key |
| attribute_group | True | OptionalStringU8 |  | [unit_attributes_groups_tables](#unit_attributes_groups_tables) | group_name |
  
## unit_castes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| caste | True | StringU8 |  |  |  |
| localised_name | False | OptionalStringU8 |  |  |  |
| sort_priority | False | I32 |  |  |  |
  
## unit_category_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| caste | True | StringU8 |  |  |  |
| localised_name | False | OptionalStringU8 |  |  |  |
| sort_priority | False | I32 |  |  |  |
  
## unit_class_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| caste | True | StringU8 |  |  |  |
| localised_name | False | OptionalStringU8 |  |  |  |
| sort_priority | False | I32 |  |  |  |
  
## unit_description_gameplay_texts_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | False | StringU8 |  |  |  |
  
## unit_description_historical_texts_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## unit_description_short_texts_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## unit_description_strengths_weaknesses_texts_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## unit_experience_bonuses_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| stat | True | StringU8 |  | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| value | False | I32 |  |  |  |
| growth_rate | False | F32 |  |  |  |
| growth_scalar | False | F32 |  |  |  |
  
## unit_experience_threshold_modifiers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
| modifier | False | F32 |  |  |  |
  
## unit_experience_thresholds_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| value | False | I32 |  |  |  |
  
## unit_fatigue_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| value | False | I32 |  |  |  |
  
## unit_ground_type_movement_modifiers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| category | True | StringU8 |  | [unit_category_tables](#unit_category_tables) | key |
| ground_type | True | StringU8 |  | [ground_types_tables](#ground_types_tables) | type |
| speed_modifier | False | F32 |  |  |  |
  
## unit_required_technology_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| unit_key | True | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
| technology_key | True | StringU8 |  | [technologies_tables](#technologies_tables) | key |
  
## unit_set_to_unit_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| exclude | False | Boolean |  |  |  |
| unit_caste | True | OptionalStringU8 |  | [unit_castes_tables](#unit_castes_tables) | caste |
| unit_category | True | OptionalStringU8 |  | [unit_category_tables](#unit_category_tables) | key |
| unit_class | True | OptionalStringU8 |  | [unit_class_tables](#unit_class_tables) | key |
| unit_record | True | OptionalStringU8 |  | [main_units_tables](#main_units_tables) | unit |
| unit_set | True | StringU8 |  | [unit_sets_tables](#unit_sets_tables) | key |
  
## unit_sets_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| exclude | False | Boolean |  |  |  |
| unit_caste | True | OptionalStringU8 |  | [unit_castes_tables](#unit_castes_tables) | caste |
| unit_category | True | OptionalStringU8 |  | [unit_category_tables](#unit_category_tables) | key |
| unit_class | True | OptionalStringU8 |  | [unit_class_tables](#unit_class_tables) | key |
| unit_record | True | OptionalStringU8 |  | [main_units_tables](#main_units_tables) | unit |
| unit_set | True | StringU8 |  | [unit_sets_tables](#unit_sets_tables) | key |
  
## unit_shield_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| exclude | False | Boolean |  |  |  |
| unit_caste | True | OptionalStringU8 |  | [unit_castes_tables](#unit_castes_tables) | caste |
| unit_category | True | OptionalStringU8 |  | [unit_category_tables](#unit_category_tables) | key |
| unit_class | True | OptionalStringU8 |  | [unit_class_tables](#unit_class_tables) | key |
| unit_record | True | OptionalStringU8 |  | [main_units_tables](#main_units_tables) | unit |
| unit_set | True | StringU8 |  | [unit_sets_tables](#unit_sets_tables) | key |
  
## unit_spacings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| exclude | False | Boolean |  |  |  |
| unit_caste | True | OptionalStringU8 |  | [unit_castes_tables](#unit_castes_tables) | caste |
| unit_category | True | OptionalStringU8 |  | [unit_category_tables](#unit_category_tables) | key |
| unit_class | True | OptionalStringU8 |  | [unit_class_tables](#unit_class_tables) | key |
| unit_record | True | OptionalStringU8 |  | [main_units_tables](#main_units_tables) | unit |
| unit_set | True | StringU8 |  | [unit_sets_tables](#unit_sets_tables) | key |
  
## unit_special_abilities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| exclude | False | Boolean |  |  |  |
| unit_caste | True | OptionalStringU8 |  | [unit_castes_tables](#unit_castes_tables) | caste |
| unit_category | True | OptionalStringU8 |  | [unit_category_tables](#unit_category_tables) | key |
| unit_class | True | OptionalStringU8 |  | [unit_class_tables](#unit_class_tables) | key |
| unit_record | True | OptionalStringU8 |  | [main_units_tables](#main_units_tables) | unit |
| unit_set | True | StringU8 |  | [unit_sets_tables](#unit_sets_tables) | key |
  
## unit_stat_modifiers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| exclude | False | Boolean |  |  |  |
| unit_caste | True | OptionalStringU8 |  | [unit_castes_tables](#unit_castes_tables) | caste |
| unit_category | True | OptionalStringU8 |  | [unit_category_tables](#unit_category_tables) | key |
| unit_class | True | OptionalStringU8 |  | [unit_class_tables](#unit_class_tables) | key |
| unit_record | True | OptionalStringU8 |  | [main_units_tables](#main_units_tables) | unit |
| unit_set | True | StringU8 |  | [unit_sets_tables](#unit_sets_tables) | key |
  
## unit_stats_land_experience_bonuses_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| exclude | False | Boolean |  |  |  |
| unit_caste | True | OptionalStringU8 |  | [unit_castes_tables](#unit_castes_tables) | caste |
| unit_category | True | OptionalStringU8 |  | [unit_category_tables](#unit_category_tables) | key |
| unit_class | True | OptionalStringU8 |  | [unit_class_tables](#unit_class_tables) | key |
| unit_record | True | OptionalStringU8 |  | [main_units_tables](#main_units_tables) | unit |
| unit_set | True | StringU8 |  | [unit_sets_tables](#unit_sets_tables) | key |
  
## unit_stats_naval_crew_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| unit_type | True | StringU8 |  |  |  |
| core_loading_skill | False | I32 |  |  |  |
| core_marksmanship | False | I32 |  |  |  |
| melee_attack | False | I32 |  |  |  |
| melee_defence | False | I32 |  |  |  |
| melee_weapon_type | False | StringU8 |  |  |  |
| pistols | False | Boolean |  |  |  |
| ammo | False | I32 |  |  |  |
| battle_entity | False | StringU8 |  | [battle_entities_tables](#battle_entities_tables) | key |
| soldier_model | False | StringU8 |  | [warscape_animated_tables](#warscape_animated_tables) | key |
| man_animations_table | False | StringU8 |  | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| equipment_theme | False | StringU8 |  |  |  |
| armour_audio | False | StringU8 |  |  |  |
| armour | False | I32 |  |  |  |
| spacing | False | F32 |  |  |  |
| discipline | False | I32 |  |  |  |
| missile_type | False | OptionalStringU8 |  | [projectiles_tables](#projectiles_tables) | key |
  
## unit_stats_naval_crew_to_factions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| faction | False | StringU16 |  |  |  |
| marines | False | StringU16 |  |  |  |
| seaman | False | StringU16 |  |  |  |
| guncrew | False | StringU16 |  |  |  |
| admiral | False | StringU16 |  |  |  |
| commodore | False | StringU16 |  |  |  |
| naval_officer | False | StringU16 |  |  |  |
| musician | False | StringU16 |  |  |  |
  
## unit_stats_naval_experience_bonuses_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| xp_level | True | StringU8 |  |  |  |
| melee_defence | False | I32 |  |  |  |
| melee_attack | False | I32 |  |  |  |
| core_gunner_loading_skill | False | I32 |  |  |  |
| core_gunner_marksmanship | False | I32 |  |  |  |
| morale | False | I32 |  |  |  |
| mp_fixed_cost | False | I32 |  |  |  |
| mp_experience_cost_multiplier | False | F32 |  |  |  |
  
## unit_type_enums_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## unit_variants_colours_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## unit_variants_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## unit_voice_categories_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU16 |  |  |  |
  
## unit_weights_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## units_custom_battle_permissions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## units_to_exclusive_faction_permissions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
| faction | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| allowed | False | Boolean |  |  |  |
  
## units_to_groupings_military_permissions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| unit | True | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
| military_group | True | StringU8 |  | [groupings_military_tables](#groupings_military_tables) | military_group |
  
## variants_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| unit | True | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
| military_group | True | StringU8 |  | [groupings_military_tables](#groupings_military_tables) | military_group |
  
## victory_conditions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| condition | True | StringU8 |  |  |  |
  
## victory_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| condition | True | StringU8 |  |  |  |
  
## videos_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| condition | True | StringU8 |  |  |  |
  
## voice_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU16 |  |  |  |
  
## warscape_animated_lod_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| filename | False | StringU8 |  |  |  |
| range | False | F32 |  |  |  |
| animated | False | StringU8 |  | [warscape_animated_tables](#warscape_animated_tables) | key |
  
## warscape_animated_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| texture_filename_base | False | StringU8 |  |  |  |
| category | False | StringU8 |  | [warscape_categories_tables](#warscape_categories_tables) | key |
  
## warscape_equipment_items_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| equipment_item | False | StringU8 |  |  |  |
| equipment_key | True | StringU8 |  |  |  |
  
## warscape_equipment_themes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| theme | True | StringU16 |  |  |  |
| primary_weapon | False | OptionalStringU16 |  | [warscape_equipment_collections_tables](#warscape_equipment_collections_tables) | collection_key |
| secondary_weapon | False | OptionalStringU16 |  | [warscape_equipment_collections_tables](#warscape_equipment_collections_tables) | collection_key |
| defensive | False | OptionalStringU16 |  | [warscape_equipment_collections_tables](#warscape_equipment_collections_tables) | collection_key |
| ambient | False | OptionalStringU16 |  | [warscape_equipment_collections_tables](#warscape_equipment_collections_tables) | collection_key |
| personal | False | OptionalStringU16 |  | [warscape_equipment_collections_tables](#warscape_equipment_collections_tables) | collection_key |
| banners | False | OptionalStringU16 |  | [warscape_equipment_collections_tables](#warscape_equipment_collections_tables) | collection_key |
  
## warscape_rigid_lod_range_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| LOD_id | True | StringU8 |  |  |  |
| range | False | F32 |  |  |  |
  
## warscape_rigid_lod_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| filename | False | StringU8 |  |  |  |
| range | False | StringU8 |  |  |  |
| rigid | False | StringU8 |  | [warscape_rigid_tables](#warscape_rigid_tables) | key |
  
## warscape_rigid_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| texture_directory | False | StringU8 |  |  |  |
| category | False | StringU8 |  | [warscape_categories_tables](#warscape_categories_tables) | key |
  
## warscape_trees_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| tree | False | StringU16 |  |  |  |
| season | False | StringU16 |  |  |  |
| model_path | False | StringU16 |  |  |  |
  
## warscape_underlay_textures_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| underlay_key | True | StringU8 |  |  |  |
| filename | False | StringU8 |  |  |  |
| filepath | False | StringU8 |  |  |  |
| levels | False | I32 |  |  |  |
  
## wind_levels_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| sea_surface | False | StringU8 |  | [sea_surfaces_tables](#sea_surfaces_tables) | key |
| magnitudeX | False | F32 |  |  |  |
| magnitudeY | False | F32 |  |  |  |
| sort_order | False | I32 |  |  |  |