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
| ability | True | StringU8 |  |  |  |
| cannot_fail | False | Boolean |  |  |  |
  
## achievements_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
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
| actor_effect_bundle | False | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| key | True | StringU8 |  |  |  |
| target_effect_bundle | False | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
  
## advice_info_texts_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| advice_level_lookup | False | I32 | Advice level linked to, when this advice level is trigged this info text will  be shown | [advice_levels_tables](#advice_levels_tables) | key |
| key | True | StringU8 |  |  |  |
| persistant | False | Boolean | Persistant entry will stick around until scriptor calls for entry to be removed |  |  |
| show_instant | False | Boolean | If true the info text will appear automatically when advice triggered. If false then it is up to the scriptor to trigger when it appears. |  |  |
| show_on_navigate | False | Boolean | If true when navigating back to a piece of advisor it will show again |  |  |
| is_header | False | Boolean | Specifies whether appears as header or bulleted entry |  |  |
| navigation_order | False | I32 | Sets the display order of infotext when browsing back and forth between advice items |  |  |
  
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
| thread | True | StringU8 |  |  |  |
  
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
| ability | True | StringU8 |  | [abilities_tables](#abilities_tables) | ability |
| agent | True | StringU8 |  | [agents_tables](#agents_tables) | key |
| attribute | True | StringU8 |  | [agent_attributes_tables](#agent_attributes_tables) | key |
| cannot_fail | False | StringU8 |  | [action_results_tables](#action_results_tables) | key |
| critical_failure | False | StringU8 |  | [action_results_tables](#action_results_tables) | key |
| critical_success | False | StringU8 |  | [action_results_tables](#action_results_tables) | key |
| failure | False | StringU8 |  | [action_results_tables](#action_results_tables) | key |
| opportune_failure | False | StringU8 |  | [action_results_tables](#action_results_tables) | key |
| success | False | StringU8 |  | [action_results_tables](#action_results_tables) | key |
| localised_action_name | False | StringU8 |  |  |  |
| localised_action_description | False | StringU8 |  |  |  |
| your_message_events_male | False | OptionalStringU8 |  | [agent_action_message_events_tables](#agent_action_message_events_tables) | key |
| your_message_events_female | False | OptionalStringU8 |  | [agent_action_message_events_tables](#agent_action_message_events_tables) | key |
| their_message_events_male | False | OptionalStringU8 |  | [agent_action_message_events_tables](#agent_action_message_events_tables) | key |
| their_message_events_female | False | OptionalStringU8 |  | [agent_action_message_events_tables](#agent_action_message_events_tables) | key |
| enabled_by_effect | False | OptionalStringU8 |  | [effects_tables](#effects_tables) | effect |
  
## agent_attributes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## agent_culture_details_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| agent | False | StringU8 |  | [agents_tables](#agents_tables) | key |
| culture | False | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| associated_unit | False | OptionalStringU8 |  | [main_units_tables](#main_units_tables) | unit |
| key | True | I32 |  |  |  |
| season | False | OptionalStringU8 |  |  |  |
| level | False | I32 |  |  |  |
| equipment_theme | False | OptionalStringU8 |  |  |  |
| agent_recruited_movie | False | OptionalStringU8 |  | [movie_event_strings_tables](#movie_event_strings_tables) | event |
| gender | False | OptionalStringU8 |  | [genders_tables](#genders_tables) | gender |
  
## agent_localisations_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## agent_string_faction_overrides_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| agent | True | StringU8 |  | [agents_tables](#agents_tables) | key |
| faction | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| gender | True | StringU8 |  | [genders_tables](#genders_tables) | gender |
| icon_path | False | OptionalStringU8 |  |  |  |
  
## agent_string_subculture_overrides_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| agent | True | StringU8 |  | [agents_tables](#agents_tables) | key |
| gender | True | StringU8 |  | [genders_tables](#genders_tables) | gender |
| subculture | True | StringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| icon_path | False | OptionalStringU8 |  |  |  |
  
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
| ability | True | StringU8 |  | [abilities_tables](#abilities_tables) | ability |
| localised_name | False | StringU8 |  |  |  |
| localised_ability_name | False | StringU8 |  |  |  |
  
## agent_to_agent_attributes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| attribute | True | StringU8 |  | [agent_attributes_tables](#agent_attributes_tables) | key |
| agent | True | StringU8 |  | [agents_tables](#agents_tables) | key |
| default_value | False | I32 |  |  |  |
  
## agent_uniforms_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| filename | False | StringU8 |  | [variants_tables](#variants_tables) | variant_name |
| uniform_name | True | StringU8 |  |  |  |
| battle_filename | False | OptionalStringU8 |  | [variants_tables](#variants_tables) | variant_name |
| campaign_porthole_filename | False | OptionalStringU8 |  | [variants_tables](#variants_tables) | variant_name |
| audio_armour_type | False | StringU8 |  | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
| audio_weapon_type | False | StringU8 |  | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
| audio_shield_type | False | StringU8 |  | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
| campaign_politician_filename | False | OptionalStringU8 |  |  |  |
  
## agents_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| move_points | False | I32 |  |  |  |
| line_of_sight | False | I32 |  |  |  |
| playable | False | Boolean |  |  |  |
| portrait_override | False | OptionalStringU8 |  |  |  |
| primary_attribute | False | StringU8 |  | [agent_attributes_tables](#agent_attributes_tables) | key |
| religion | False | OptionalStringU8 |  | [religions_tables](#religions_tables) | religion_key |
| faction_total_cap | False | I32 |  |  |  |
| cost | False | I32 |  |  |  |
| in_encyclopedia | False | Boolean |  |  |  |
  
## aide_de_camp_speeches_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| picture_in_picture | False | Boolean |  |  |  |
| offset_angle | False | F32 |  |  |  |
| offset_range | False | F32 |  |  |  |
| circumvent_cooldown | False | Boolean |  |  |  |
| cinematic_event | False | OptionalStringU8 | Cinematic event to trigger when receives aide de camp message | [battle_cinematic_events_tables](#battle_cinematic_events_tables) | key |
  
## ancillaries_categories_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| category | True | StringU8 |  |  |  |
  
## ancillaries_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
| type | False | StringU8 |  | [ancillary_types_tables](#ancillary_types_tables) | type |
| applies_to | False | StringU8 |  |  |  |
| transferrable | False | Boolean |  |  |  |
| unique_to_world | False | Boolean |  |  |  |
| unique_to_faction | False | Boolean |  |  |  |
| precedence | False | I32 |  |  |  |
| start_date | False | I32 |  |  |  |
| end_date | False | I32 |  |  |  |
| avatar_skill | False | OptionalStringU8 |  |  |  |
| avatar_special_ability | False | OptionalStringU8 |  |  |  |
| legendary_item | False | Boolean |  |  |  |
| mp_exclusive | False | Boolean |  |  |  |
| is_wife_ancillary | False | Boolean |  |  |  |
| is_husband_ancillary | False | Boolean |  |  |  |
| is_diplomatic_ancillary | False | Boolean |  |  |  |
| is_dynastic_ancillary | False | Boolean |  |  |  |
| spouse_subculture | False | OptionalStringU8 | used for diplomatic / dynastic marriages -> this record is applied for spouse subculture | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| category | False | StringU8 |  | [ancillaries_categories_tables](#ancillaries_categories_tables) | category |
| min_starting_age | False | I32 |  |  |  |
| max_starting_age | False | I32 |  |  |  |
| min_expiry_age | False | I32 |  |  |  |
| max_expiry_age | False | I32 |  |  |  |
| spouse_type | False | OptionalStringU8 | For spouse ancillaries | [marriage_types_tables](#marriage_types_tables) | key |
  
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
| audio_projectile_type | False | StringU8 |  | [audio_projectiles_enums_tables](#audio_projectiles_enums_tables) | key |
| max_attenuation_fire | False | F32 |  |  |  |
| max_attenuation_impact | False | F32 |  |  |  |
| max_attenuation_inflight | False | F32 |  |  |  |
| play_incoming_sound | False | Boolean |  |  |  |
| requires_distance | False | Boolean |  |  |  |
| requires_speed | False | Boolean |  |  |  |
| inflight_min_speed | False | F32 |  |  |  |
  
## audio_vo_actor_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| actor_1 | False | StringU8 |  | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_2 | False | OptionalStringU8 |  | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_3 | False | OptionalStringU8 |  | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_4 | False | OptionalStringU8 |  | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_5 | False | OptionalStringU8 |  | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_6 | False | OptionalStringU8 |  | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_7 | False | OptionalStringU8 |  | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_8 | False | OptionalStringU8 |  | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_9 | False | OptionalStringU8 |  | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_10 | False | OptionalStringU8 |  | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_11 | False | OptionalStringU8 |  | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_12 | False | OptionalStringU8 |  | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_13 | False | OptionalStringU8 |  | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_14 | False | OptionalStringU8 |  | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_15 | False | OptionalStringU8 |  | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
  
## banditry_events_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| maximum_banditry | False | I32 |  |  |  |
| message_event | False | StringU8 |  | [message_events_tables](#message_events_tables) | event |
| minimum_banditry | False | I32 |  |  |  |
| name | True | StringU8 |  |  |  |
| province_effect_bundle | False | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| weight | False | I32 |  |  |  |
  
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
| key | True | StringU8 |  |  |  |
| max_height_large | False | F32 |  |  |  |
| max_height_small | False | F32 |  |  |  |
| min_fort_max_height | False | F32 |  |  |  |
| min_height | False | F32 |  |  |  |
| move_speed_max_multiplier | False | F32 |  |  |  |
| move_speed_min_multiplier | False | F32 |  |  |  |
| turn_speed_multiplier | False | F32 |  |  |  |
| move_fast_multiplier | False | F32 |  |  |  |
  
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
| key | True | StringU8 |  |  |  |
| type | False | StringU8 |  | [battle_entities_types_enum_tables](#battle_entities_types_enum_tables) | key |
| walk_speed | False | F32 |  |  |  |
| run_speed | False | F32 |  |  |  |
| acceleration | False | F32 |  |  |  |
| deceleration | False | F32 |  |  |  |
| charge_speed | False | F32 |  |  |  |
| crawl_speed | False | F32 |  |  |  |
| charge_distance_commence_run | False | F32 |  |  |  |
| charge_distance_adopt_charge_pose | False | F32 |  |  |  |
| charge_distance_pick_target | False | F32 |  |  |  |
| radius | False | F32 |  |  |  |
| shape | False | StringU8 |  | [battle_entities_shape_enum_tables](#battle_entities_shape_enum_tables) | key |
| radii_ratio | False | F32 |  |  |  |
| mass | False | F32 |  |  |  |
| height | False | F32 |  |  |  |
| fire_arc_close | False | F32 |  |  |  |
| fire_arc_loose | False | F32 |  |  |  |
| turn_speed | False | F32 |  |  |  |
| hit_points | False | I32 |  |  |  |
| allow_turn_to_move_anim | False | Boolean |  |  |  |
| allow_static_turn_anim | False | Boolean |  |  |  |
| tracking_threshold | False | F32 |  |  |  |
| min_turning_speed | False | F32 |  |  |  |
| display_model_offset_z | False | F32 |  |  |  |
  
## battle_entity_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| deep_water | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| forest | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| grass | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| mud | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| name | True | StringU8 |  |  |  |
| rock | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| road | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| sand | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| scrub | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| shallow_water | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| snow | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| wooden_floor | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
  
## battle_misc_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| name | True | StringU8 |  |  |  |
  
## battle_personalities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| soldier_model | False | StringU8 |  | [warscape_animated_tables](#warscape_animated_tables) | key |
| man_animations_table | False | StringU8 |  | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| type | False | StringU8 |  | [battle_personality_types_enum_tables](#battle_personality_types_enum_tables) | key |
| missile_type | False | OptionalStringU8 |  | [projectiles_tables](#projectiles_tables) | key |
| variant | False | StringU8 |  | [variants_tables](#variants_tables) | variant_name |
  
## battle_siege_vehicle_permissions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| faction | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| vehicle | True | StringU8 |  | [battlefield_siege_vehicles_tables](#battlefield_siege_vehicles_tables) | key |
  
## battle_skeletons_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| category | False | StringU8 |  | [battle_skeleton_category_enums_tables](#battle_skeleton_category_enums_tables) | type |
| head_node | False | OptionalStringU8 |  |  |  |
| hips_node | False | OptionalStringU8 |  |  |  |
| leftarm_node | False | OptionalStringU8 |  |  |  |
| leftfoot_node | False | OptionalStringU8 |  |  |  |
| lefthand_node | False | OptionalStringU8 |  |  |  |
| leftleg_node | False | OptionalStringU8 |  |  |  |
| leftshoulder_node | False | OptionalStringU8 |  |  |  |
| leftupleg_node | False | OptionalStringU8 |  |  |  |
| leftwheel_node | False | OptionalStringU8 |  |  |  |
| name | True | StringU8 |  |  |  |
| neck_node | False | OptionalStringU8 |  |  |  |
| rightarm_node | False | OptionalStringU8 |  |  |  |
| rightfoot_node | False | OptionalStringU8 |  |  |  |
| righthand_node | False | OptionalStringU8 |  |  |  |
| rightleg_node | False | OptionalStringU8 |  |  |  |
| rightshoulder_node | False | OptionalStringU8 |  |  |  |
| rightupleg_node | False | OptionalStringU8 |  |  |  |
| rightwheel_node | False | OptionalStringU8 |  |  |  |
| root | False | StringU8 |  |  |  |
| scale | False | F32 |  |  |  |
| scale_deviation | False | F32 |  |  |  |
| spine_node | False | OptionalStringU8 |  |  |  |
| weapon1_node | False | OptionalStringU8 |  |  |  |
| weapon2_node | False | OptionalStringU8 |  |  |  |
| weapon3_node | False | OptionalStringU8 |  |  |  |
| weapon4_node | False | OptionalStringU8 |  |  |  |
| weapon5_node | False | OptionalStringU8 |  |  |  |
| leftfinger_node | False | OptionalStringU8 |  |  |  |
| rightfinger_node | False | OptionalStringU8 |  |  |  |
| lefttoe_node | False | OptionalStringU8 |  |  |  |
| righttoe_node | False | OptionalStringU8 |  |  |  |
  
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
| key | True | StringU8 |  |  |  |
| level | False | I32 |  |  |  |
| precipitation_type | False | I32 |  |  |  |
| num_particles | False | I32 |  |  |  |
| particle_size | False | F32 |  |  |  |
| particle_speed | False | F32 |  |  |  |
| list_order | False | I32 |  |  |  |
| naval_appropriate | False | Boolean |  |  |  |
  
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
| category | False | StringU8 |  | [battlefield_building_categories_tables](#battlefield_building_categories_tables) | category |
| model | False | StringU8 |  | [models_building_tables](#models_building_tables) | key |
| audio_material | False | StringU8 |  | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
| hit_points | False | I32 |  |  |  |
| gun_type | False | OptionalStringU8 |  | [missile_weapons_tables](#missile_weapons_tables) | key |
| onscreen_name | False | OptionalStringU8 |  | [battlefield_buildings_names_tables](#battlefield_buildings_names_tables) | key |
| ignition_threshold | False | I32 |  |  |  |
| radar_icon | False | OptionalStringU8 |  |  |  |
| visible_in_public_ted | False | Boolean |  |  |  |
| fortwall_penetration_chance | False | I32 |  |  |  |
| collision_3d | False | Boolean |  |  |  |
| destruct_thresholds | False | OptionalStringU8 |  |  |  |
| joiner | False | Boolean |  |  |  |
| auxiliary | False | Boolean |  |  |  |
| burn_rate | False | F32 | multiplier applied to the rate of damage caused by fire |  |  |
  
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
| key | True | StringU8 |  |  |  |
| battlefield_siege_vehicle | False | StringU8 |  | [battlefield_siege_vehicles_tables](#battlefield_siege_vehicles_tables) | key |
| level | False | I32 |  |  |  |
| type | False | OptionalStringU8 |  |  |  |
  
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
| destroyed_model | False | OptionalStringU8 |  | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| destruction_animation | False | OptionalStringU8 |  | [warscape_animated_tables](#warscape_animated_tables) | key |
| engine_type | False | StringU8 |  | [gun_types_enum_tables](#gun_types_enum_tables) | key |
| gun_animation_table | False | StringU8 |  | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| key | True | StringU8 |  |  |  |
| missile_weapon | False | OptionalStringU8 |  | [missile_weapons_tables](#missile_weapons_tables) | key |
| model | False | StringU8 |  | [warscape_animated_tables](#warscape_animated_tables) | key |
| battle_entity | False | StringU8 |  | [battle_entities_tables](#battle_entities_tables) | key |
| can_move | False | Boolean |  |  |  |
  
## battlefield_siege_vehicles_custom_battles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| cap | False | I32 |  |  |  |
| probability | False | F32 |  |  |  |
| vehicle | True | StringU8 |  | [battlefield_siege_vehicles_tables](#battlefield_siege_vehicles_tables) | key |
  
## battlefield_siege_vehicles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| hit_points | False | I32 |  |  |  |
| key | True | StringU8 |  |  |  |
| model | False | StringU8 |  | [models_sieges_tables](#models_sieges_tables) | key |
| battle_entity | False | StringU8 |  | [battle_entities_tables](#battle_entities_tables) | key |
| gun_type | False | OptionalStringU8 |  |  |  |
| docking_clearance | False | F32 |  |  |  |
| engine | False | OptionalStringU8 |  | [battlefield_engines_autonomous_tables](#battlefield_engines_autonomous_tables) | key |
| image_path | False | StringU8 | Image path used for recruitment icons in campaign and frontend |  |  |
| recruitment_cap | False | I32 | Maximum can recruit per army |  |  |
| uses_8m_wall | False | Boolean | Equipment valid to work with 8m walls |  |  |
| uses_15m_wall | False | Boolean | Equipment valid to work with 15m walls |  |  |
| cost | False | I32 | Cost to field vehicle in custom battle menu |  |  |
| category_image_path | False | StringU8 | Smaller icons used for battle radar and on unit cards |  |  |
| special_edition_mask | False | I32 | DLC - Special Edition Value |  |  |
| ignition_threshold | False | I32 |  |  |  |
| attack_damage | False | F32 | Used by battering rams |  |  |
| selection_priority | False | F32 | Used by campaign AI to select siege vehicle to build |  |  |
  
## battlefield_siege_vehicles_to_autonomous_engines_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| engine | True | StringU8 |  | [battlefield_engines_autonomous_tables](#battlefield_engines_autonomous_tables) | key |
| vehicle | True | StringU8 |  | [battlefield_siege_vehicles_tables](#battlefield_siege_vehicles_tables) | key |
  
## battles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| type | False | StringU8 |  | [battle_types_tables](#battle_types_tables) | type |
| is_naval | False | Boolean |  |  |  |
| specification | False | StringU8 |  |  |  |
| screenshot_path | False | OptionalStringU8 |  |  |  |
| map_path | False | OptionalStringU8 |  |  |  |
| team_size_1 | False | I32 |  |  |  |
| team_size_2 | False | I32 |  |  |  |
| release | False | Boolean |  |  |  |
| multiplayer | False | Boolean |  |  |  |
| singleplayer | False | Boolean |  |  |  |
| intro_movie | False | OptionalStringU8 |  |  |  |
| year | False | I32 |  |  |  |
| defender_funds_ratio | False | F32 |  |  |  |
| has_key_buildings | False | Boolean |  |  |  |
| matchmaking | False | Boolean |  |  |  |
| playable_area_width | False | F32 |  |  |  |
| playable_area_height | False | F32 |  |  |  |
| is_large_settlement | False | Boolean |  |  |  |
| has_15m_walls | False | Boolean |  |  |  |
  
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
| key | True | StringU8 |  |  |  |
| tech_category_tab | False | OptionalStringU8 |  |  |  |
| tech_category_position | False | OptionalStringU8 |  |  |  |
| chain_category | False | OptionalStringU8 |  |  |  |
| in_encyclopedia | False | Boolean |  |  |  |
| building_superchain | False | OptionalStringU8 |  | [building_superchains_tables](#building_superchains_tables) | key |
  
## building_culture_variants_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building | True | StringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| culture | True | OptionalStringU8 |  | [cultures_tables](#cultures_tables) | key |
| battlefield_building | False | OptionalStringU8 |  | [battlefield_buildings_tables](#battlefield_buildings_tables) | key |
| artpiece | False | OptionalStringU8 |  | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| artpiece_animated | False | OptionalStringU8 |  | [warscape_animated_tables](#warscape_animated_tables) | key |
| description | False | OptionalStringU8 |  | [building_description_texts_tables](#building_description_texts_tables) | key |
| icon | False | OptionalStringU8 |  |  |  |
| subculture | True | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| faction | True | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| disables | False | Boolean |  |  |  |
| short_description | False | OptionalStringU8 |  | [building_short_description_texts_tables](#building_short_description_texts_tables) | key |
| flavour | False | OptionalStringU8 |  | [building_flavour_texts_tables](#building_flavour_texts_tables) | key |
| display_tooltip | False | Boolean |  |  |  |
  
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
| level_name | True | StringU8 |  |  |  |
| chain | False | StringU8 |  | [building_chains_tables](#building_chains_tables) | key |
| level | False | I32 |  |  |  |
| condition | False | StringU8 |  |  |  |
| create_time | False | I32 |  |  |  |
| create_cost | False | I32 |  |  |  |
| upkeep_cost | False | I32 |  |  |  |
| demolition_cost | False | I32 |  |  |  |
| zoc | False | I32 |  |  |  |
| lower_happiness | False | I32 |  |  |  |
| upper_happiness | False | I32 |  |  |  |
| repression | False | I32 |  |  |  |
| gdp | False | I32 |  |  |  |
| town_wealth_growth | False | I32 |  |  |  |
| pop_change | False | F32 |  |  |  |
| maxpop_change | False | F32 |  |  |  |
| commodity | False | StringU8 |  | [commodities_tables](#commodities_tables) | key |
| gov_type_key | False | StringU8 |  | [government_types_tables](#government_types_tables) | government_type |
| commodity_vol | False | I32 |  |  |  |
| only_in_capital | False | Boolean |  |  |  |
| military_prestige | False | I32 |  |  |  |
| naval_prestige | False | I32 |  |  |  |
| economic_prestige | False | I32 |  |  |  |
| enlightenment_prestige | False | I32 |  |  |  |
| destruction_terminator | False | Boolean |  |  |  |
| faction_unique | False | Boolean |  |  |  |
| religion_requirement | False | OptionalStringU8 |  | [religions_tables](#religions_tables) | religion_key |
| first_in_world_bundle | False | OptionalStringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| resource_requirement | False | OptionalStringU8 |  | [resources_tables](#resources_tables) | key |
| working_model | False | StringU8 |  | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| unique_index | False | I32 |  |  |  |
| can_convert | False | Boolean |  |  |  |
| building_instance_key | False | OptionalStringU8 |  | [building_instances_tables](#building_instances_tables) | key |
| audio_building_type | False | StringU8 |  | [audio_campaign_building_enums_tables](#audio_campaign_building_enums_tables) | key |
| should_show_building_level_in_ui_for_technology | False | Boolean |  |  |  |
| is_new | False | Boolean |  |  |  |
  
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
| key | True | StringU8 |  |  |  |
  
## building_states_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## building_superchains_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| max_instances_per_region | False | I32 |  |  |  |
  
## building_units_allowed_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building | False | StringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| unit | False | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
| XP | False | I32 |  |  |  |
| conditions | False | OptionalStringU8 |  |  |  |
| key | True | I64 |  |  |  |
| faction | False | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| enabled | False | Boolean |  |  |  |
  
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
| agent_record_key | True | StringU8 |  | [agents_tables](#agents_tables) | key |
| agent_type_key | True | StringU8 |  | [cai_agent_types_tables](#cai_agent_types_tables) | key |
  
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
| capital_province_template | False | StringU8 |  | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| economic_province_template | False | StringU8 |  | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| economic_port_province_template | False | StringU8 |  | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| key | True | StringU8 |  |  |  |
| military_province_template | False | StringU8 |  | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| military_port_province_template | False | StringU8 |  | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| non_port_province_military_ideal_percentage | False | I32 |  |  |  |
| port_province_military_ideal_percentage | False | I32 |  |  |  |
  
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
| existing_building_chain_key | True | OptionalStringU8 |  | [building_chains_tables](#building_chains_tables) | key |
| existing_building_level_inclusive_end | True | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| existing_building_level_inclusive_start | True | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| potential_buiding_chain_key | True | OptionalStringU8 |  | [building_chains_tables](#building_chains_tables) | key |
| potential_building_level_inclusive_end | True | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| potential_building_level_inclusive_start | True | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| synergy_level_key | False | StringU8 |  | [cai_construction_system_synergy_levels_tables](#cai_construction_system_synergy_levels_tables) | key |
| synergy_policy_key | True | StringU8 |  | [cai_construction_system_synergy_policies_tables](#cai_construction_system_synergy_policies_tables) | key |
| existing_building_instance | True | OptionalStringU8 |  | [building_instances_tables](#building_instances_tables) | key |
| existing_building_super_chain | True | StringU8 |  | [building_superchains_tables](#building_superchains_tables) | key |
| potential_building_instance | True | OptionalStringU8 |  | [building_instances_tables](#building_instances_tables) | key |
| potential_building_super_chain | True | StringU8 |  | [building_superchains_tables](#building_superchains_tables) | key |
  
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
| key | True | StringU8 |  |  |  |
  
## cai_military_behaviour_policies_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_personalities_budget_allocation_policy_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| budget_allocation_key | True | StringU8 |  | [cai_personalities_budget_allocations_tables](#cai_personalities_budget_allocations_tables) | key |
| budget_context_key | True | StringU8 |  | [cai_strategic_context_types_tables](#cai_strategic_context_types_tables) | key |
| budget_policy_key | True | StringU8 |  | [cai_personalities_budget_policies_tables](#cai_personalities_budget_policies_tables) | key |
| priority | False | I32 |  |  |  |
  
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
| default_budget_allocation_key | False | StringU8 |  | [cai_personalities_budget_allocations_tables](#cai_personalities_budget_allocations_tables) | key |
| key | True | StringU8 |  |  |  |
  
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
| default_positive_net_income_survival_rounds | False | I32 | For positive income the number of rounds used to determine treasury based increases allow per-turn outgoings. |  |  |
| default_proportion_of_net_income_to_spend | False | F32 | Amount of net income to spend |  |  |
| default_zero_or_negative_net_income_survival_rounds | False | I32 | At or below zero net income the number of rounds the treasury should be divided up for |  |  |
| key | True | StringU8 | Policy key |  |  |
  
## cai_personalities_income_allocation_policy_strategic_context_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| income_allocation_policy_key | True | StringU8 |  | [cai_personalities_income_allocation_policies_tables](#cai_personalities_income_allocation_policies_tables) | key |
| positive_net_income_survival_rounds | False | I32 |  |  |  |
| proportion_of_net_income_to_spend | False | F32 |  |  |  |
| strategic_context_key | True | StringU8 |  | [cai_strategic_context_types_tables](#cai_strategic_context_types_tables) | key |
| zero_or_negative_net_income_survival_rounds | False | I32 |  |  |  |
  
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
| key | True | StringU8 |  |  |  |
| join_ally_bias | False | F32 |  |  |  |
  
## cai_personalities_religious_conversion_policies_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## cai_personalities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| agent_distribution_profile_key | False | StringU8 |  | [cai_agent_distribution_profiles_tables](#cai_agent_distribution_profiles_tables) | key |
| agent_recruitment_profile_key | False | StringU8 |  | [cai_agent_recruitment_profiles_tables](#cai_agent_recruitment_profiles_tables) | key |
| budget_policy_key | False | StringU8 |  | [cai_personalities_budget_policies_tables](#cai_personalities_budget_policies_tables) | key |
| character_skill_tree_manager_key | False | StringU8 |  | [campaign_ai_character_skill_tree_managers_tables](#campaign_ai_character_skill_tree_managers_tables) | key |
| key | True | StringU8 |  |  |  |
| military_aggressiveness_policy | False | StringU8 |  | [cai_military_aggressiveness_policies_tables](#cai_military_aggressiveness_policies_tables) | key |
| military_behaviour_policy | False | StringU8 |  | [cai_military_behaviour_policies_tables](#cai_military_behaviour_policies_tables) | key |
| reliability_policy_key | False | StringU8 |  | [cai_personalities_reliability_policies_tables](#cai_personalities_reliability_policies_tables) | key |
| religious_conversion_policy | False | StringU8 |  | [cai_personalities_religious_conversion_policies_tables](#cai_personalities_religious_conversion_policies_tables) | key |
| technology_manager_key | False | StringU8 |  | [campaign_ai_technology_managers_tables](#campaign_ai_technology_managers_tables) | key |
| allowed_for_random_selection | False | Boolean |  |  |  |
| diplomatic_component | False | StringU8 |  | [cai_personality_diplomatic_components_tables](#cai_personality_diplomatic_components_tables) | id |
| strategic_component | False | StringU8 |  | [cai_personality_strategic_components_tables](#cai_personality_strategic_components_tables) | id |
| cultural_component | False | StringU8 |  | [cai_personality_cultural_components_tables](#cai_personality_cultural_components_tables) | id |
| deal_evaluation_component | False | StringU8 |  | [cai_personality_deal_evaluation_components_tables](#cai_personality_deal_evaluation_components_tables) | id |
| deal_generation_component | False | StringU8 |  | [cai_personality_deal_generation_components_tables](#cai_personality_deal_generation_components_tables) | id |
| construction_system_policy | False | StringU8 |  | [cai_personalities_construction_system_policies_tables](#cai_personalities_construction_system_policies_tables) | key |
| task_management_system_task_generation_profile | False | StringU8 |  | [cai_personalities_task_management_system_task_generator_profiles_tables](#cai_personalities_task_management_system_task_generator_profiles_tables) | key |
| negotiation_component | False | StringU8 |  | [cai_personality_negotiation_components_tables](#cai_personality_negotiation_components_tables) | id |
| income_allocation_policy | False | StringU8 |  | [cai_personalities_income_allocation_policies_tables](#cai_personalities_income_allocation_policies_tables) | key |
| occupation_decision_component | False | StringU8 |  | [cai_personality_occupation_decision_components_tables](#cai_personality_occupation_decision_components_tables) | id |
  
## cai_personalities_task_management_system_task_generator_profiles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| default_generator_group_when_no_owned_regions | False | StringU8 |  | [cai_task_management_system_task_generator_groups_tables](#cai_task_management_system_task_generator_groups_tables) | key |
| default_generator_group_when_owning_regions | False | StringU8 |  | [cai_task_management_system_task_generator_groups_tables](#cai_task_management_system_task_generator_groups_tables) | key |
| key | True | StringU8 |  |  |  |
  
## cai_personality_cultural_components_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | StringU8 |  |  |  |
  
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
| id | True | StringU8 |  |  |  |
| max_payment_value | False | F32 |  |  |  |
| payment_treachery_value | False | F32 |  |  |  |
| payment_offered_multiplier | False | F32 |  |  |  |
| payment_requested_multiplier | False | F32 |  |  |  |
  
## cai_personality_deal_evaluation_deal_component_names_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | StringU8 |  |  |  |
  
## cai_personality_deal_evaluation_deal_component_values_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| best_friends_value | False | F32 |  |  |  |
| bitter_enemies_value | False | F32 |  |  |  |
| deal_component | True | StringU8 |  | [cai_personality_deal_evaluation_deal_component_names_tables](#cai_personality_deal_evaluation_deal_component_names_tables) | id |
| friendly_value | False | F32 |  |  |  |
| neutral_value | False | F32 |  |  |  |
| personality_component | True | StringU8 |  | [cai_personality_deal_evaluation_components_tables](#cai_personality_deal_evaluation_components_tables) | id |
| total_war_balance_factor | False | F32 |  |  |  |
| last_stand_balance_factor | False | F32 |  |  |  |
| unfriendly_value | False | F32 |  |  |  |
| very_friendly_value | False | F32 |  |  |  |
| very_unfriendly_value | False | F32 |  |  |  |
| war_balance_factor | False | F32 |  |  |  |
| tension_balance_factor | False | F32 |  |  |  |
| peace_balance_factor | False | F32 |  |  |  |
| treachery_value | False | F32 |  |  |  |
  
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
| id | True | StringU8 |  |  |  |
  
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
| defensive_alliance | False | F32 |  |  |  |
| component_id | True | StringU8 |  | [cai_personality_diplomatic_components_tables](#cai_personality_diplomatic_components_tables) | id |
| trade_agreement | False | F32 |  |  |  |
| military_alliance | False | F32 |  |  |  |
| non_aggression_pact | False | F32 |  |  |  |
| vassalage_master | False | F32 |  |  |  |
| vassalage_vassal | False | F32 |  |  |  |
| client_state_protector | False | F32 |  |  |  |
| client_state_client | False | F32 |  |  |  |
| war | False | F32 |  |  |  |
| military_access | False | F32 |  |  |  |
  
## cai_personality_negotiation_components_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| angry_reject_max | False | I32 | Maximum number of counter offers before AI breaks off the negotiation. |  |  |
| angry_reject_min | False | I32 | Minimum number of counter offers before AI breaks off the negotiation. |  |  |
| id | True | StringU8 |  |  |  |
| initial_decline | False | I32 | Probability of declining the initial offer. |  |  |
| initial_counter | False | I32 | Probability of countering the initial offer if able. |  |  |
| irrelevant_accept | False | I32 | Probability of declining a counter offer if irrelevant & acceptable. |  |  |
| irrelevant_decline | False | I32 | Probability of declining a counter offer if irrelevant. |  |  |
| irrelevant_counter_new | False | I32 | Probability of countering an irrevelant counter offer with another goal if one can be generated. |  |  |
| irrelevant_counter_last | False | I32 | Probability of countering an irrevelant counter offer with last goal. |  |  |
| max_interactions | False | I32 | Maximum number of times AI is going to start a negotiation in 1 turn |  |  |
| max_steps_above_acceptable | False | I32 | Maximum number of steps above the acceptable payment that can be proposed. |  |  |
| no_offer_chance | False | I32 | Probability of not offering anything even if a goal was generated. |  |  |
| no_payment_chance | False | I32 | Probability of not including payment in the initial offer of willing to offer it. |  |  |
| num_goals_generated | False | I32 | Number of goals generated & evaluated before one is selected. |  |  |
  
## cai_personality_occupation_decision_components_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| food_excess_cap | False | I32 |  |  |  |
| food_shortage_cap | False | I32 |  |  |  |
| id | True | StringU8 |  |  |  |
| min_attitude | False | I32 |  |  |  |
| squalor_cap | False | I32 |  |  |  |
  
## cai_personality_occupation_decision_priorities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| component_id | True | StringU8 |  | [cai_personality_occupation_decision_components_tables](#cai_personality_occupation_decision_components_tables) | id |
| last_stand_priority | False | F32 |  |  |  |
| option | True | StringU8 |  |  |  |
| total_war_priority | False | F32 |  |  |  |
| war_priority | False | F32 |  |  |  |
| tension_priority | False | F32 |  |  |  |
| peace_priority | False | F32 |  |  |  |
  
## cai_personality_strategic_components_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| friendly_towards_enemy_multiplier | False | F32 |  |  |  |
| friendly_towards_friend_multiplier | False | F32 |  |  |  |
| hostile_towards_enemy_multiplier | False | F32 |  |  |  |
| hostile_towards_friend_multiplier | False | F32 |  |  |  |
| id | True | StringU8 |  |  |  |
| max_friendly_attitude | False | F32 |  |  |  |
| max_hostile_attitude | False | F32 |  |  |  |
| unknown_faction_multiplier | False | F32 |  |  |  |
| max_merc_proportion | False | F32 |  |  |  |
| min_merc_cap | False | I32 |  |  |  |
| enemy_strength_modifier | False | F32 |  |  |  |
| enemy_threat_strength_modifier | False | F32 |  |  |  |
| min_retreat_ratio | False | F32 |  |  |  |
| min_retreat_to_settlement_ratio | False | F32 |  |  |  |
| strategic_balance_opportunism_factor | False | F32 |  |  |  |
| fortified_settlement_assault_strength_modifier | False | F32 |  |  |  |
| fortified_settlement_defend_strength_modifier | False | F32 |  |  |  |
  
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
| battle_type | False | OptionalStringU8 |  | [campaign_battle_type_enums_tables](#campaign_battle_type_enums_tables) | key |
| id | True | StringU8 |  |  |  |
| night_battle | False | OptionalStringU8 |  |  |  |
| stance | False | OptionalStringU8 |  |  |  |
  
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
| battle_type | False | StringU8 | Battle type this preset is for | [campaign_battle_type_enums_tables](#campaign_battle_type_enums_tables) | key |
| coord_x | False | F32 | X coordinate on map (0-1) |  |  |
| coord_y | False | F32 | Y coordinate on map (0-1) |  |  |
| key | True | StringU8 | Unique id |  |  |
| tile_upgrade | False | OptionalStringU8 | Optional tile upgrade (for specifying settlement levels, etc; see tile_upgrades.xml) |  |  |
| is_unique_settlement | False | Boolean | True only for unique settlements like carthage, currently used to determine if has all different settlement sizes |  |  |
| campaign_map | False | I32 | This is the campaign map this preset is for | [campaign_map_playable_areas_tables](#campaign_map_playable_areas_tables) | index |
  
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
| agent_type | False | OptionalStringU8 |  | [agents_tables](#agents_tables) | key |
| art_set_id | True | StringU8 |  |  |  |
| culture | False | OptionalStringU8 |  | [cultures_tables](#cultures_tables) | key |
| subculture | False | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| faction | False | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| is_custom | False | Boolean |  |  |  |
| is_male | False | Boolean |  |  |  |
| group | False | OptionalStringU8 |  | [campaign_character_art_sets_campaign_groups_tables](#campaign_character_art_sets_campaign_groups_tables) | key |
  
## campaign_character_arts_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| art_set_id | True | StringU8 |  | [campaign_character_art_sets_tables](#campaign_character_art_sets_tables) | art_set_id |
| level | True | I32 |  |  |  |
| age | True | I32 |  |  |  |
| portrait | False | OptionalStringU8 |  |  |  |
| season | True | StringU8 |  |  |  |
| uniform | False | OptionalStringU8 |  | [agent_uniforms_tables](#agent_uniforms_tables) | uniform_name |
| card | False | OptionalStringU8 |  |  |  |
| info | False | OptionalStringU8 |  |  |  |
| sea_uniform | False | OptionalStringU8 |  | [agent_uniforms_tables](#agent_uniforms_tables) | uniform_name |
| navy_uniform | False | OptionalStringU8 |  | [agent_uniforms_tables](#agent_uniforms_tables) | uniform_name |
| land_animation | False | OptionalStringU8 |  | [campaign_anim_set_enums_tables](#campaign_anim_set_enums_tables) | name |
| sea_animation | False | OptionalStringU8 |  | [campaign_anim_set_enums_tables](#campaign_anim_set_enums_tables) | name |
| navy_animation | False | OptionalStringU8 |  | [campaign_anim_set_enums_tables](#campaign_anim_set_enums_tables) | name |
  
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
| key | True | StringU8 |  |  |  |
| location | False | StringU8 |  | [campaign_effect_scope_locations_tables](#campaign_effect_scope_locations_tables) | key |
| order | False | I32 |  |  |  |
| ownership | False | OptionalStringU8 |  | [campaign_effect_scope_ownerships_tables](#campaign_effect_scope_ownerships_tables) | key |
| source | False | StringU8 |  | [campaign_effect_scope_objects_tables](#campaign_effect_scope_objects_tables) | key |
| target | False | StringU8 |  | [campaign_effect_scope_objects_tables](#campaign_effect_scope_objects_tables) | key |
  
## campaign_ground_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| type | True | StringU8 |  |  |  |
| movement_cost | False | I32 |  |  |  |
| can_ambush | False | Boolean |  |  |  |
| is_sea | False | Boolean |  |  |  |
| icon | False | StringU8 | icon for tooltips |  |  |
  
## campaign_map_attrition_damages_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| percent_unit_damage | False | I32 |  |  |  |
  
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
| damage | False | StringU8 |  | [campaign_map_attrition_damages_tables](#campaign_map_attrition_damages_tables) | key |
| key | True | StringU8 |  |  |  |
| type | False | StringU8 |  | [campaign_map_attrition_types_tables](#campaign_map_attrition_types_tables) | key |
| message_event_association | False | OptionalStringU8 |  | [message_events_tables](#message_events_tables) | event |
  
## campaign_map_playable_areas_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| index | True | StringU8 |  |  |  |
| sea_trade | False | Boolean |  |  |  |
| map_file | False | OptionalStringU8 |  |  |  |
| overlay_file | False | OptionalStringU8 |  |  |  |
| radar_file | False | OptionalStringU8 |  |  |  |
| meaningful_id | False | StringU8 |  |  |  |
| preview_width | False | I32 |  |  |  |
| preview_height | False | I32 |  |  |  |
| preview_border | False | I32 |  |  |  |
| minx | False | F32 |  |  |  |
| maxx | False | F32 |  |  |  |
| miny | False | F32 |  |  |  |
| maxy | False | F32 |  |  |  |
| mapname | False | StringU8 |  | [campaign_maps_tables](#campaign_maps_tables) | mapname |
| minimap_lookup_file | False | OptionalStringU8 |  |  |  |
| is_available_in_custom_battle | False | Boolean | Determines whether this maps tilemap is selectable in custom battle screen to pick battle maps |  |  |
  
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
| settlement_id | True | StringU8 |  |  |  |
| region | False | StringU8 |  | [regions_tables](#regions_tables) | key |
| default_onscreen_name | False | StringU8 |  |  |  |
| template_name | False | StringU8 |  | [campaign_map_settlement_templates_tables](#campaign_map_settlement_templates_tables) | template_name |
| slot_count | False | I32 |  |  |  |
| slot_type | False | StringU8 |  | [slots_tables](#slots_tables) | slot |
  
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
| construction_type | False | StringU8 |  | [campaign_settlement_display_building_construction_enums_tables](#campaign_settlement_display_building_construction_enums_tables) | type |
| display_building_key | False | StringU8 |  | [campaign_settlement_display_building_ids_tables](#campaign_settlement_display_building_ids_tables) | key |
| id | True | I64 |  |  |  |
| phase | False | I32 |  |  |  |
  
## campaign_settlement_display_building_ids_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| building_level_key | False | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| culture | False | OptionalStringU8 |  | [cultures_tables](#cultures_tables) | key |
| faction | False | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| key | True | StringU8 |  |  |  |
| sprawl_piece_level | False | I32 |  |  |  |
| sprawl_piece_type | False | OptionalStringU8 |  | [campaign_settlement_display_sprawl_pieces_tables](#campaign_settlement_display_sprawl_pieces_tables) | key |
| sub_culture | False | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
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
| building_path | False | OptionalStringU8 |  |  |  |
| display_building_key | False | StringU8 |  | [campaign_settlement_display_building_ids_tables](#campaign_settlement_display_building_ids_tables) | key |
| is_slum | False | Boolean |  |  |  |
| is_sieged | False | Boolean |  |  |  |
| is_blockaded | False | Boolean |  |  |  |
| key | True | I64 |  |  |  |
| state | False | OptionalStringU8 |  | [campaign_settlement_display_buildings_enums_tables](#campaign_settlement_display_buildings_enums_tables) | type |
| destruction_additional_model | False | OptionalStringU8 |  |  |  |
| destruction_override_model | False | OptionalStringU8 |  |  |  |
| construction_additional_model | False | OptionalStringU8 |  |  |  |
| construction_override_model | False | OptionalStringU8 |  |  |  |
  
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
| stance | True | StringU8 |  | [campaign_stances_tables](#campaign_stances_tables) | key |
| effect_bundle | True | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| culture | True | OptionalStringU8 |  | [cultures_tables](#cultures_tables) | key |
| subculture | True | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| faction | True | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
  
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
| key | True | StringU8 |  |  |  |
| vfx | False | StringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| x_offset | False | F32 |  |  |  |
| y_offset | False | F32 |  |  |  |
| z_offset | False | F32 |  |  |  |
  
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
| icon_name | False | StringU8 |  |  |  |
| key | True | StringU8 |  |  |  |
  
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
| dilemma_key | False | StringU8 |  | [dilemmas_tables](#dilemmas_tables) | key |
| id | True | I64 |  |  |  |
| option_key | False | StringU8 |  | [cdir_events_dilemma_options_tables](#cdir_events_dilemma_options_tables) | option_key |
| value | False | OptionalStringU8 |  |  |  |
  
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
| id | True | I64 |  |  |  |
| incident_key | False | StringU8 |  | [incidents_tables](#incidents_tables) | key |
| option_key | False | StringU8 |  | [cdir_events_incident_options_tables](#cdir_events_incident_options_tables) | option_key |
| value | False | OptionalStringU8 |  |  |  |
  
## cdir_events_incident_payloads_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| id | True | I64 |  |  |  |
| incident_key | False | StringU8 |  | [incidents_tables](#incidents_tables) | key |
| payload_key | False | StringU8 |  | [cdir_events_payloads_tables](#cdir_events_payloads_tables) | payload_key |
| value | False | StringU8 |  |  |  |
  
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
| id | True | I64 |  |  |  |
| mission_key | False | StringU8 |  | [missions_tables](#missions_tables) | key |
| option_key | False | StringU8 |  | [cdir_events_mission_options_tables](#cdir_events_mission_options_tables) | option_key |
| value | False | OptionalStringU8 |  |  |  |
  
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
| child_key | True | StringU8 |  | [character_skill_nodes_tables](#character_skill_nodes_tables) | key |
| initial_descent_tiers | False | I32 |  |  |  |
| parent_key | True | StringU8 |  | [character_skill_nodes_tables](#character_skill_nodes_tables) | key |
| parent_link_position | False | I32 |  |  |  |
| child_link_position | False | I32 |  |  |  |
  
## character_skill_node_sets_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| agent_key | False | OptionalStringU8 |  | [agents_tables](#agents_tables) | key |
| campaign_key | False | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| faction_key | False | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| key | True | StringU8 |  |  |  |
| subculture | False | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| for_army | False | Boolean |  |  |  |
| for_navy | False | Boolean |  |  |  |
  
## character_skill_nodes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_key | False | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| character_skill_key | False | StringU8 |  | [character_skills_tables](#character_skills_tables) | key |
| character_skill_node_set_key | False | StringU8 |  | [character_skill_node_sets_tables](#character_skill_node_sets_tables) | key |
| faction_key | False | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| indent | False | I32 |  |  |  |
| key | True | StringU8 |  |  |  |
| tier | False | I32 |  |  |  |
| subculture | False | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## character_skills_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| image_path | False | StringU8 |  |  |  |
| key | True | StringU8 |  |  |  |
| localised_description | False | StringU8 |  |  |  |
| localised_name | False | StringU8 |  |  |  |
| pre_battle_speech_parameter | False | OptionalStringU8 |  | [pre_battle_speech_parameters_enum_tables](#pre_battle_speech_parameters_enum_tables) | key |
| unlocked_at_rank | False | I32 |  |  |  |
| is_background_skill | False | Boolean |  |  |  |
| is_female_only_background_skill | False | Boolean |  |  |  |
| is_male_only_background_skill | False | Boolean |  |  |  |
| background_weighting | False | F32 |  |  |  |
  
## character_trait_levels_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| level | False | I32 |  |  |  |
| trait | False | StringU8 |  | [character_traits_tables](#character_traits_tables) | key |
| threshold_points | False | I32 |  |  |  |
| enabled_by_tech | False | OptionalStringU8 |  | [technologies_tables](#technologies_tables) | key |
  
## character_traits_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  | [trait_info_tables](#trait_info_tables) | trait |
| no_going_back_level | False | I32 |  |  |  |
| hidden | False | Boolean |  |  |  |
| precedence | False | I32 |  |  |  |
| icon | False | StringU8 |  | [trait_categories_tables](#trait_categories_tables) | category |
| pre_battle_speech_parameter | False | OptionalStringU8 |  | [pre_battle_speech_parameters_enum_tables](#pre_battle_speech_parameters_enum_tables) | key |
  
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
| climate_type | True | StringU8 |  |  |  |
| colour_index | False | I32 |  |  |  |
| conifer_line | False | I32 |  |  |  |
| tree_line | False | I32 |  |  |  |
| is_land | False | Boolean |  |  |  |
  
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
| key | True | StringU8 |  | [resources_tables](#resources_tables) | key |
| baseline_price_per_unit | False | F32 |  |  |  |
| price_elasticity_of_demand | False | F32 |  |  |  |
  
## commodity_unit_names_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| unit | True | StringU8 |  |  |  |
  
## culture_settlement_occupation_options_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| culture | True | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| option | True | StringU8 |  |  |  |
  
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
| subculture | True | StringU8 |  |  |  |
| culture | False | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| index | False | I32 |  |  |  |
| farm | False | StringU8 |  | [battle_terrain_farms_tables](#battle_terrain_farms_tables) | farm |
  
## cultures_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| index | False | I64 |  |  |  |
| fallback_ui_culture | False | OptionalStringU8 |  |  |  |
  
## cursor_transitions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| initiating_cursor | True | StringU8 |  | [cursors_tables](#cursors_tables) | key |
| mouse_event | True | StringU8 | Event that triggers transition | [cursor_mouse_events_tables](#cursor_mouse_events_tables) | key |
| resulting_cursor | False | StringU8 |  | [cursors_tables](#cursors_tables) | key |
  
## cursors_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU16 |  |  |  |
| image | False | StringU16 | .cur file to use for cursor |  |  |
| frames | False | I32 | Number of frames cursor has |  |  |
| framerate | False | I32 | Frame rate of cursor animation |  |  |
| hotspotX | False | I32 |  |  |  |
| hotspotY | False | I32 |  |  |  |
| loop | False | Boolean | Whether animation loops indefinately |  |  |
| width | False | I32 | Width of cursor image |  |  |
| height | False | I32 | Height of cursor image |  |  |
  
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
| key | True | StringU8 |  |  |  |
  
## deployables_custom_battles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| cap | False | I32 |  |  |  |
| deployable | True | StringU8 |  | [deployables_tables](#deployables_tables) | key |
| probability | False | I32 |  |  |  |
  
## deployables_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| hitpoints | False | I32 |  |  |  |
| how | False | OptionalStringU8 |  | [unit_stat_modifiers_how_enums_tables](#unit_stat_modifiers_how_enums_tables) | key |
| icon_name | False | StringU8 | Icon used for deployable card image |  |  |
| info_pic | False | OptionalStringU8 |  |  |  |
| key | True | StringU8 |  |  |  |
| kill_chance | False | F32 |  |  |  |
| min_columns | False | I32 |  |  |  |
| min_rows | False | I32 |  |  |  |
| model | False | StringU8 |  | [models_deployables_tables](#models_deployables_tables) | key |
| number | False | I32 |  |  |  |
| random_offset | False | F32 |  |  |  |
| spacing_x | False | F32 |  |  |  |
| spacing_y | False | F32 |  |  |  |
| stat_mod | False | OptionalStringU8 |  | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| value | False | F32 |  |  |  |
| recruitment_cap | False | I32 | Maximum number per army |  |  |
| max_rows | False | I32 |  |  |  |
| model_2 | False | OptionalStringU8 |  | [models_deployables_tables](#models_deployables_tables) | key |
| ignition_threshold | False | I32 |  |  |  |
  
## dilemma_to_campaign_subject_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_subject_key | True | StringU8 |  | [campaign_subjects_tables](#campaign_subjects_tables) | key |
| dilemma_key | True | StringU8 |  | [dilemmas_tables](#dilemmas_tables) | key |
| weighting | False | F32 |  |  |  |
  
## dilemmas_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| generate | False | Boolean |  |  |  |
| key | True | StringU8 |  |  |  |
| localised_description | False | StringU8 |  |  |  |
| localised_title | False | StringU8 |  |  |  |
| ui_icon | False | StringU8 |  |  |  |
| ui_image | False | StringU8 |  |  |  |
| prioritized | False | Boolean |  |  |  |
  
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
| religion_A | True | StringU8 |  | [religions_tables](#religions_tables) | religion_key |
| religion_B | True | StringU8 |  | [religions_tables](#religions_tables) | religion_key |
| relations_modifier | False | I32 |  |  |  |
| religious_unhappiness_modifier | False | F32 |  |  |  |
  
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
| effect | True | StringU8 |  |  |  |
| icon | False | OptionalStringU8 |  |  |  |
| priority | False | I32 |  |  |  |
| icon_negative | False | OptionalStringU8 |  |  |  |
  
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
| experience_points | False | I32 |  |  |  |
| trigger_key | True | StringU8 |  |  |  |
  
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
| effect_bundle | False | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| key | True | StringU8 |  |  |  |
| ui_icon | False | StringU8 |  |  |  |
  
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
| faction_name | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| primary_colour_r | False | I32 |  |  |  |
| primary_colour_g | False | I32 |  |  |  |
| primary_colour_b | False | I32 |  |  |  |
| secondary_colour_r | False | I32 |  |  |  |
| secondary_colour_g | False | I32 |  |  |  |
| secondary_colour_b | False | I32 |  |  |  |
| tertiary_colour_r | False | I32 |  |  |  |
| tertiary_colour_g | False | I32 |  |  |  |
| tertiary_colour_b | False | I32 |  |  |  |
  
## faction_variables_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| description | False | OptionalStringU8 |  |  |  |
| faction_variable_key | True | StringU8 |  |  |  |
| value | False | StringU8 |  |  |  |
  
## factions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| index | False | I64 |  |  |  |
| subculture | False | StringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| category | False | StringU8 |  |  |  |
| screen_name | False | StringU8 |  |  |  |
| screen_adjective | False | StringU8 |  |  |  |
| name_group | False | I32 |  | [names_groups_tables](#names_groups_tables) | key |
| skin | False | StringU8 |  |  |  |
| ui_skin | False | OptionalStringU8 |  |  |  |
| is_rebel | False | Boolean |  |  |  |
| mp_available | False | Boolean |  |  |  |
| mp_available_naval | False | Boolean |  |  |  |
| icons_path_units | False | StringU8 |  |  |  |
| flags_path | False | StringU8 |  |  |  |
| republican_flag_path | False | OptionalStringU8 |  |  |  |
| same_gov_type_revolution_flag_path | False | OptionalStringU8 |  |  |  |
| primary_colour_r | False | F32 |  |  |  |
| primary_colour_g | False | F32 |  |  |  |
| primary_colour_b | False | F32 |  |  |  |
| alt_primary_colour_r | False | F32 |  |  |  |
| alt_primary_colour_g | False | F32 |  |  |  |
| alt_primary_colour_b | False | F32 |  |  |  |
| secondary_colour_r | False | F32 |  |  |  |
| secondary_colour_g | False | F32 |  |  |  |
| secondary_colour_b | False | F32 |  |  |  |
| alt_secondary_colour_r | False | F32 |  |  |  |
| alt_secondary_colour_g | False | F32 |  |  |  |
| alt_secondary_colour_b | False | F32 |  |  |  |
| uniform_colour_r | False | F32 |  |  |  |
| uniform_colour_g | False | F32 |  |  |  |
| uniform_colour_b | False | F32 |  |  |  |
| alt_uniform_colour_r | False | F32 |  |  |  |
| alt_uniform_colour_g | False | F32 |  |  |  |
| alt_uniform_colour_b | False | F32 |  |  |  |
| military_group | False | StringU8 |  | [groupings_military_tables](#groupings_military_tables) | military_group |
| settler_rebellion_faction | False | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| rebel_colour_r | False | F32 |  |  |  |
| rebel_colour_g | False | F32 |  |  |  |
| rebel_colour_b | False | F32 |  |  |  |
| movie_death_event | False | OptionalStringU8 |  | [movie_event_strings_tables](#movie_event_strings_tables) | id |
| mp_use_republic_early | False | Boolean |  |  |  |
| mp_use_republic_late | False | Boolean |  |  |  |
| unit_regiment_name_group | False | I32 |  | [names_groups_tables](#names_groups_tables) | key |
| ship_name_group | False | I32 |  | [names_groups_tables](#names_groups_tables) | key |
| attack_desc | False | StringU8 |  |  |  |
| defend_desc | False | StringU8 |  |  |  |
| mp_stats_name | False | OptionalStringU8 |  |  |  |
| pre_battle_speech_parameter | False | StringU8 |  | [pre_battle_speech_parameters_enum_tables](#pre_battle_speech_parameters_enum_tables) | key |
| can_be_regionless | False | Boolean |  |  |  |
| card_colour_r | False | F32 |  |  |  |
| card_colour_g | False | F32 |  |  |  |
| card_colour_b | False | F32 |  |  |  |
| diplomacy_culture | False | StringU8 |  | [cultures_tables](#cultures_tables) | key |
| senator_total | False | I32 |  |  |  |
| uses_legion_names | False | Boolean |  |  |  |
  
## fame_levels_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| ai_prestige | False | I32 |  |  |  |
| army_cap | False | I32 |  |  |  |
| champion_cap | False | I32 |  |  |  |
| dignitary_cap | False | I32 |  |  |  |
| level | True | I32 |  |  |  |
| navy_cap | False | I32 |  |  |  |
| player_prestige | False | I32 |  |  |  |
| province_initiative_cap | False | I32 |  |  |  |
| spy_cap | False | I32 |  |  |  |
| campaign | True | StringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| description_lookup | False | OptionalStringU8 |  | [campaign_localised_strings_tables](#campaign_localised_strings_tables) | key |
| effect_bundle | False | OptionalStringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
  
## family_relationship_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| relationship_type | True | StringU8 |  |  |  |
  
## famous_battle_pools_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| pool_id | True | StringU8 |  |  |  |
| pool_posX | False | F32 |  |  |  |
| pool_posY | False | F32 |  |  |  |
| pool_radius | False | I32 |  |  |  |
| battle_name | False | StringU8 |  |  |  |
  
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
| auto_target | False | Boolean |  |  |  |
| camera_offset_x | False | F32 |  |  |  |
| camera_offset_y | False | F32 |  |  |  |
| camera_offset_z | False | F32 |  |  |  |
| half_accuracy_arc | False | F32 |  |  |  |
| half_horizontal_fire_arc | False | F32 |  |  |  |
| half_vertical_fire_arc_elevation | False | F32 |  |  |  |
| key | True | StringU8 |  | [gun_types_enum_tables](#gun_types_enum_tables) | key |
| near_clipping_plane | False | F32 |  |  |  |
| reload_time | False | F32 |  |  |  |
| track_projectile_distance | False | F32 |  |  |  |
| turn_delay | False | F32 |  |  |  |
| half_vertical_fire_arc_declination | False | F32 |  |  |  |
  
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
| animation | False | OptionalStringU8 |  |  |  |
| party | True | StringU8 |  | [political_parties_tables](#political_parties_tables) | key |
| uniform | False | StringU8 |  |  |  |
| x_offset | False | F32 |  |  |  |
| y_offset | False | F32 |  |  |  |
  
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
| government_type | True | StringU8 |  |  |  |
| elected_ministers | False | Boolean |  |  |  |
| hereditary_ministers | False | Boolean |  |  |  |
| rank | False | I32 |  |  |  |
| active_upper_class | False | StringU8 |  | [population_classes_tables](#population_classes_tables) | population_class |
| active_lower_class | False | StringU8 |  | [population_classes_tables](#population_classes_tables) | population_class |
  
## governorships_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| governorship | True | StringU8 |  |  |  |
  
## ground_type_to_stat_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| affected_stat | True | StringU8 |  | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| ground_type | True | StringU8 |  | [ground_types_tables](#ground_types_tables) | type |
| multiplier | False | F32 |  |  |  |
  
## ground_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| enum_value | False | I32 |  |  |  |
| selection_cursor | False | OptionalStringU8 | Cursor that appears while have unit selected and mouse over ground type | [cursors_tables](#cursors_tables) | key |
| standard_cursor | False | OptionalStringU8 | Cursor that appears when have nothing selected and mouse over ground type | [cursors_tables](#cursors_tables) | key |
| type | True | StringU8 |  |  |  |
| penalty_immune_attribute | False | OptionalStringU8 | Some ground types have penalties; this one will allow the unit to be immune to those penalties | [unit_attributes_tables](#unit_attributes_tables) | key |
  
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
| key | True | StringU8 |  |  |  |
| nobility | False | Boolean |  |  |  |
| gender | False | StringU8 |  | [genders_tables](#genders_tables) | gender |
| agent_type | False | StringU8 |  | [agents_tables](#agents_tables) | key |
| faction | False | StringU8 |  | [factions_tables](#factions_tables) | key |
| spawning_window_start | False | I32 |  |  |  |
| spawning_window_end | False | I32 |  |  |  |
| spawn_conditions | False | StringU8 |  |  |  |
| name_key | False | StringU8 |  | [names_tables](#names_tables) | id |
| surname_key | False | OptionalStringU8 |  | [names_tables](#names_tables) | id |
| art_set_id | False | OptionalStringU8 |  | [campaign_character_art_sets_tables](#campaign_character_art_sets_tables) | art_set_id |
| clan_name_key | False | OptionalStringU8 |  | [names_tables](#names_tables) | id |
| other_name_key | False | OptionalStringU8 |  | [names_tables](#names_tables) | id |
| political_party | False | OptionalStringU8 |  | [political_parties_tables](#political_parties_tables) | key |
| age_start | False | I32 |  |  |  |
  
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
| generate | False | Boolean |  |  |  |
| key | True | StringU8 |  |  |  |
| ui_icon | False | StringU8 |  |  |  |
| ui_image | False | StringU8 |  |  |  |
| prioritised | False | Boolean |  |  |  |
  
## land_units_officers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| officer_1 | False | OptionalStringU8 |  | [battle_personalities_tables](#battle_personalities_tables) | key |
| officer_2 | False | OptionalStringU8 |  | [battle_personalities_tables](#battle_personalities_tables) | key |
| standard_bearer_1 | False | OptionalStringU8 |  | [battle_personalities_tables](#battle_personalities_tables) | key |
| standard_bearer_2 | False | OptionalStringU8 |  | [battle_personalities_tables](#battle_personalities_tables) | key |
| musician_1 | False | OptionalStringU8 |  | [battle_personalities_tables](#battle_personalities_tables) | key |
| musician_2 | False | OptionalStringU8 |  | [battle_personalities_tables](#battle_personalities_tables) | key |
| personality_location | False | OptionalStringU8 |  | [personality_location_enums_tables](#personality_location_enums_tables) | key |
  
## land_units_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| accuracy | False | I32 |  |  |  |
| ammo | False | I32 |  |  |  |
| armour | False | StringU8 |  | [unit_armour_types_tables](#unit_armour_types_tables) | key |
| campaign_action_points | False | I32 |  |  |  |
| category | False | StringU8 |  | [unit_category_tables](#unit_category_tables) | key |
| charge_bonus | False | I32 |  |  |  |
| class | False | StringU8 |  | [unit_class_tables](#unit_class_tables) | key |
| dismounted_charge_bonus | False | I32 |  |  |  |
| dismounted_melee_attack | False | I32 |  |  |  |
| dismounted_melee_defence | False | I32 |  |  |  |
| historical_description_text | False | StringU8 |  | [unit_description_historical_texts_tables](#unit_description_historical_texts_tables) | key |
| key | True | StringU8 |  |  |  |
| man_animation | False | OptionalStringU8 |  | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| man_entity | False | StringU8 |  | [battle_entities_tables](#battle_entities_tables) | key |
| melee_attack | False | I32 |  |  |  |
| melee_defence | False | I32 |  |  |  |
| morale | False | I32 |  |  |  |
| bonus_hit_points | False | I32 |  |  |  |
| mount | False | OptionalStringU8 |  | [mounts_tables](#mounts_tables) | key |
| num_animals | False | I32 |  |  |  |
| animal | False | OptionalStringU8 |  | [animals_tables](#animals_tables) | key |
| num_mounts | False | I32 |  |  |  |
| primary_melee_weapon | False | StringU8 |  | [melee_weapons_tables](#melee_weapons_tables) | key |
| primary_missile_weapon | False | OptionalStringU8 |  | [missile_weapons_tables](#missile_weapons_tables) | key |
| rank_depth | False | I32 |  |  |  |
| shield | False | StringU8 |  | [unit_shield_types_tables](#unit_shield_types_tables) | key |
| short_description_text | False | StringU8 |  | [unit_description_short_texts_tables](#unit_description_short_texts_tables) | key |
| spacing | False | StringU8 |  | [unit_spacings_tables](#unit_spacings_tables) | key |
| strengths_weaknesses_text | False | StringU8 |  | [unit_description_strengths_weaknesses_texts_tables](#unit_description_strengths_weaknesses_texts_tables) | key |
| supports_first_person | False | Boolean |  |  |  |
| training_level | False | StringU8 |  | [unit_training_level_enum_tables](#unit_training_level_enum_tables) | key |
| num_guns | False | I32 |  |  |  |
| officers | False | StringU8 |  | [land_units_officers_tables](#land_units_officers_tables) | key |
| articulated_record | False | OptionalStringU8 |  | [land_unit_articulated_vehicles_tables](#land_unit_articulated_vehicles_tables) | key |
| engine | False | OptionalStringU8 |  | [battlefield_engines_tables](#battlefield_engines_tables) | key |
| is_male | False | Boolean |  |  |  |
| visibility_spotting_range_min | False | F32 |  |  |  |
| visibility_spotting_range_max | False | F32 |  |  |  |
| ability_global_recharge | False | F32 |  |  |  |
| attribute_group | False | OptionalStringU8 |  | [unit_attributes_groups_tables](#unit_attributes_groups_tables) | group_name |
| spot_dist_tree | False | F32 |  |  |  |
| spot_dist_scrub | False | F32 |  |  |  |
| chariot | False | OptionalStringU8 |  | [battlefield_chariots_tables](#battlefield_chariots_tables) | key |
| num_chariots | False | I32 |  |  |  |
| reload | False | I32 |  |  |  |
| loose_spacing | False | Boolean |  |  |  |
| spotting_and_hiding | False | OptionalStringU8 |  | [spotting_and_hiding_values_tables](#spotting_and_hiding_values_tables) | key |
| selection_vo | False | StringU8 |  | [audio_vo_selected_switches_tables](#audio_vo_selected_switches_tables) | key |
| selected_vo_secondary | False | StringU8 |  | [audio_vo_selected_switches_tables](#audio_vo_selected_switches_tables) | key |
| selected_vo_tertiary | False | StringU8 |  | [audio_vo_selected_switches_tables](#audio_vo_selected_switches_tables) | key |
| hiding_scalar | False | F32 | This affects the range that the unit can be spotted at, less than 1 makes it longer, greater than 1 shorter. So 1.5 would increase the spotters range by +50% |  |  |
  
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
| additional_building_requirement | False | OptionalStringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| campaign_cap | False | I32 |  |  |  |
| caste | False | StringU8 |  | [unit_castes_tables](#unit_castes_tables) | caste |
| create_time | False | I32 |  |  |  |
| is_naval | False | Boolean |  |  |  |
| land_unit | False | StringU8 |  | [land_units_tables](#land_units_tables) | key |
| num_men | False | I32 |  |  |  |
| multiplayer_cap | False | I32 |  |  |  |
| multiplayer_cost | False | I32 |  |  |  |
| naval_unit | False | OptionalStringU8 |  | [naval_units_tables](#naval_units_tables) | key |
| num_ships | False | I32 |  |  |  |
| min_men_per_ship | False | I32 |  |  |  |
| max_men_per_ship | False | I32 |  |  |  |
| prestige | False | I32 |  |  |  |
| recruitment_cost | False | I32 |  |  |  |
| recruitment_movie | False | OptionalStringU8 |  |  |  |
| religion_requirement | False | OptionalStringU8 |  | [religions_tables](#religions_tables) | religion_key |
| unit | True | StringU8 |  |  |  |
| upkeep_cost | False | I32 |  |  |  |
| weight | False | OptionalStringU8 |  | [unit_weights_tables](#unit_weights_tables) | key |
| campaign_total_cap | False | I32 |  |  |  |
| resource_requirement | False | OptionalStringU8 |  | [resources_tables](#resources_tables) | key |
| world_leader_only | False | Boolean |  |  |  |
| can_trade | False | Boolean |  |  |  |
| special_edition_mask | False | I32 |  |  |  |
| unique_index | False | I64 |  |  |  |
| in_encyclopedia | False | Boolean |  |  |  |
| region_unit_resource_requirement | False | OptionalStringU8 |  | [region_unit_resources_tables](#region_unit_resources_tables) | key |
| audio_language | False | StringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| audio_vo_actor_group | False | OptionalStringU8 |  | [audio_vo_actor_groups_tables](#audio_vo_actor_groups_tables) | key |
  
## marriage_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## melee_weapons_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| armour_penetrating | False | Boolean |  |  |  |
| armour_piercing | False | Boolean |  |  |  |
| bonus_v_cavalry | False | I32 |  |  |  |
| bonus_v_elephants | False | I32 |  |  |  |
| bonus_v_infantry | False | I32 |  |  |  |
| key | True | StringU8 |  |  |  |
| damage | False | I32 |  |  |  |
| ap_damage | False | I32 |  |  |  |
| first_strike | False | I32 |  |  |  |
| shield_piercing | False | Boolean |  |  |  |
| weapon_length | False | F32 |  |  |  |
| melee_weapon_type | False | StringU8 |  | [unit_melee_weapons_enum_tables](#unit_melee_weapons_enum_tables) | key |
| audio_material | False | StringU8 |  | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
  
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
| chance_to_replenish | False | F32 |  |  |  |
| key | True | StringU8 |  |  |  |
| max_count | False | I32 |  |  |  |
| max_replenish_per_turn | False | I32 |  |  |  |
| unit_record | False | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
  
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
| culure_key | False | OptionalStringU8 |  | [cultures_tables](#cultures_tables) | key |
| faction_key | False | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| is_army | False | Boolean |  |  |  |
| key | True | StringU8 |  |  |  |
| subculture_key | False | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| icon | False | StringU8 |  |  |  |
| banner_decorator | False | StringU8 |  |  |  |
  
## military_force_legacy_names_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| subculture | True | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| for_army | False | Boolean |  |  |  |
| campaign | False | OptionalStringU8 | If a campaign is set for a particular subculture, only explicitly marked records will be used for that subculture/campaign combination. | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## ministerial_effectiveness_modifiers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| leader_minister_level | True | I32 |  |  |  |
| government_type | True | StringU8 |  | [government_types_tables](#government_types_tables) | government_type |
| effectiveness_bonus | False | I32 |  |  |  |
  
## ministerial_positions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| minister_key | True | StringU8 |  |  |  |
| rank | False | I32 |  |  |  |
  
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
| key | True | StringU8 |  |  |  |
| precursor | False | Boolean |  |  |  |
| default_projectile | False | StringU8 |  | [projectiles_tables](#projectiles_tables) | key |
| can_fire_at_buildings | False | Boolean |  |  |  |
  
## missile_weapons_to_projectiles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| missile_weapon | True | StringU8 |  | [missile_weapons_tables](#missile_weapons_tables) | key |
| projectile | True | StringU8 |  | [projectiles_tables](#projectiles_tables) | key |
  
## mission_issuers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| issuer_key | True | StringU8 |  |  |  |
  
## missions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| generate | False | Boolean |  |  |  |
| key | True | StringU8 |  |  |  |
| localised_description | False | StringU8 |  |  |  |
| localised_title | False | StringU8 |  |  |  |
| mission_type | False | StringU8 |  | [mission_types_tables](#mission_types_tables) | key |
| ui_icon | False | StringU8 |  |  |  |
| ui_image | False | StringU8 |  |  |  |
| prioritised | False | Boolean |  |  |  |
  
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
| key | True | StringU8 |  |  |  |
| animation | False | StringU8 |  | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| entity | False | StringU8 |  | [battle_entities_tables](#battle_entities_tables) | key |
| mount_armour | False | I32 |  |  |  |
| variant | False | StringU8 |  | [variants_tables](#variants_tables) | variant_name |
| audio_armour_type | False | StringU8 |  | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
  
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
| budget_key | True | StringU8 |  | [mp_budgets_tables](#mp_budgets_tables) | key |
| general_pct | False | F32 |  |  |  |
| priority | False | I32 |  |  |  |
| template_key | True | StringU8 |  | [mp_force_gen_templates_tables](#mp_force_gen_templates_tables) | key |
| units_pct | False | F32 |  |  |  |
| upgrade_pct | False | F32 |  |  |  |
| config_key | False | StringU8 |  | [cdir_military_generator_configs_tables](#cdir_military_generator_configs_tables) | key |
| is_defender | True | Boolean |  |  |  |
  
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
| campaign_action_points | False | I32 |  |  |  |
| category | False | StringU8 |  | [unit_category_tables](#unit_category_tables) | key |
| class | False | StringU8 |  | [unit_class_tables](#unit_class_tables) | key |
| historical_description_text | False | StringU8 |  | [unit_description_historical_texts_tables](#unit_description_historical_texts_tables) | key |
| key | True | StringU8 |  |  |  |
| ship | False | StringU8 |  | [ship_dbs_tables](#ship_dbs_tables) | key |
| short_description_text | False | StringU8 |  | [unit_description_short_texts_tables](#unit_description_short_texts_tables) | key |
| strengths_weaknesses_text | False | StringU8 |  | [unit_description_strengths_weaknesses_texts_tables](#unit_description_strengths_weaknesses_texts_tables) | key |
| unit_type_icon | False | OptionalStringU8 |  |  |  |
| supports_first_person | False | Boolean |  |  |  |
| primary_naval_weapon | False | OptionalStringU8 |  | [naval_weapons_tables](#naval_weapons_tables) | key |
| secondary_naval_weapon | False | OptionalStringU8 |  | [naval_weapons_tables](#naval_weapons_tables) | key |
| rank_depth | False | I32 |  |  |  |
| attribute_groups | False | OptionalStringU8 |  | [unit_attributes_groups_tables](#unit_attributes_groups_tables) | group_name |
| can_board | False | Boolean |  |  |  |
| unit_card | False | StringU8 |  |  |  |
| is_composite | False | Boolean |  |  |  |
| ignition_threshold | False | I32 | This value indicates how many incendiary points are required before the ship will set on fire and start taking damage. |  |  |
| can_ram | False | Boolean |  |  |  |
  
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
| autonomous_engine | False | OptionalStringU8 |  | [battlefield_engines_autonomous_tables](#battlefield_engines_autonomous_tables) | key |
| key | True | StringU8 |  |  |  |
| models_entity_weaponry | False | OptionalStringU8 |  | [models_entity_weapons_tables](#models_entity_weapons_tables) | key |
| type | False | StringU8 |  | [naval_weapons_enums_tables](#naval_weapons_enums_tables) | types |
  
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
| political_action_key | True | StringU8 |  |  |  |
| onscreen_name | False | StringU8 |  |  |  |
| icon_file_path | False | OptionalStringU8 |  |  |  |
| usage_cost_multiplier | False | F32 |  |  |  |
  
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
| key | True | StringU8 |  |  |  |
| playable | False | Boolean |  |  |  |
| ui_icon | False | StringU8 |  |  |  |
| effect_bundle | False | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| initial_power | False | I32 |  |  |  |
| r | False | F32 |  |  |  |
| g | False | F32 |  |  |  |
| b | False | F32 |  |  |  |
| trait1 | False | OptionalStringU8 |  | [political_traits_tables](#political_traits_tables) | key |
| trait2 | False | OptionalStringU8 |  | [political_traits_tables](#political_traits_tables) | key |
  
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
| population_class | True | StringU8 |  |  |  |
| riots | False | Boolean |  |  |  |
| demands | False | Boolean |  |  |  |
| spawn_rebel_general | False | Boolean |  |  |  |
  
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
| damaged_display_model | False | OptionalStringU8 |  | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| display_model | False | OptionalStringU8 |  | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| impact | False | OptionalStringU8 |  | [projectile_impacts_tables](#projectile_impacts_tables) | key |
| key | True | StringU8 |  |  |  |
| launch_fx | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| trail_fx | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| stationary_fx | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| skeleton | False | OptionalStringU8 |  |  |  |
| airborne_anim | False | OptionalStringU8 |  |  |  |
| landing_anim | False | OptionalStringU8 |  |  |  |
  
## projectile_impacts_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| water | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| sails | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| mud | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| grass | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| road | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| rock | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| sand | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| cloth | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| snow | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| leather | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| wood | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| foliage | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| glass | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| blood | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| size | False | StringU8 |  |  |  |
| metal | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
  
## projectile_shot_type_enum_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| requires_effect_enabling | False | Boolean |  |  |  |
| supersedes_shot_type | False | OptionalStringU8 |  |  |  |
  
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
| key | True | StringU8 |  |  |  |
| detonator_type | False | StringU8 |  | [projectiles_detonator_types_enum_tables](#projectiles_detonator_types_enum_tables) | detonator_type |
| detonation_type | False | StringU8 |  | [projectiles_detonation_types_enum_tables](#projectiles_detonation_types_enum_tables) | key |
| detonation_radius | False | F32 |  |  |  |
| detonation_duration | False | F32 |  |  |  |
| detonation_speed | False | F32 |  |  |  |
| detonation_damage | False | F32 |  |  |  |
| projectile_name | False | OptionalStringU8 |  | [projectiles_tables](#projectiles_tables) | key |
| projectile_amount | False | I32 |  |  |  |
| explosion_particle_effect | False | OptionalStringU8 |  | [particle_effects_tables](#particle_effects_tables) | key |
| distance_from_target | False | F32 |  |  |  |
| error_margin | False | F32 |  |  |  |
| explosion_particle_effect_on_ground | False | OptionalStringU8 |  |  |  |
| audio_explosion_type | False | StringU8 |  | [audio_explosions_enums_tables](#audio_explosions_enums_tables) | key |
  
## projectiles_missile_type_enum_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | False | StringU8 |  |  |  |
  
## projectiles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| category | False | StringU8 |  | [projectile_category_enum_tables](#projectile_category_enum_tables) | key |
| shot_type | False | StringU8 |  | [projectile_shot_type_enum_tables](#projectile_shot_type_enum_tables) | key |
| explosion_type | False | OptionalStringU8 |  | [projectiles_explosions_tables](#projectiles_explosions_tables) | key |
| spin_type | False | StringU8 |  |  |  |
| projectile_number | False | I32 |  |  |  |
| trajectory_sight | False | StringU8 |  | [projectile_trajectory_sight_enum_tables](#projectile_trajectory_sight_enum_tables) | key |
| effective_range | False | I32 |  |  |  |
| minimum_range | False | I32 |  |  |  |
| max_elevation | False | I32 | This is the maximum angle that the projectile can be fired at. Generally you want it high (max 90 degrees), and above 45. Except for special cases (e.g. cannon) |  |  |
| muzzle_velocity | False | F32 | This describes the speed the projectile launches at (metres per second). If it is negative, the code will calculate this value based on firing at 45 degrees, hitting at the effective range |  |  |
| marksmanship_bonus | False | F32 |  |  |  |
| spread | False | F32 |  |  |  |
| damage | False | I32 |  |  |  |
| ap_damage | False | I32 |  |  |  |
| penetration | False | OptionalStringU8 |  | [projectile_penetration_enum_tables](#projectile_penetration_enum_tables) | key |
| incendiary | False | OptionalStringU8 | NONE = 0, VERY_LOW = 1, LOW = 5, MEDIUM = 10, HIGH = 20, VERY_HIGH = 50 | [projectile_incendiary_enum_tables](#projectile_incendiary_enum_tables) | key |
| can_bounce | False | Boolean |  |  |  |
| high_air_resistance | False | Boolean |  |  |  |
| collision_radius | False | F32 |  |  |  |
| base_reload_time | False | F32 |  |  |  |
| below_waterline_damage_modifer | False | F32 |  |  |  |
| calibration_distance | False | F32 |  |  |  |
| calibration_area | False | F32 |  |  |  |
| bonus_v_infantry | False | I32 |  |  |  |
| bonus_v_cavalry | False | I32 |  |  |  |
| bonus_v_elephant | False | I32 |  |  |  |
| projectile_display | False | OptionalStringU8 |  | [projectile_displays_tables](#projectile_displays_tables) | key |
| overhead_stat_effect | False | OptionalStringU8 |  | [special_ability_phases_tables](#special_ability_phases_tables) | id |
| projectile_audio | False | StringU8 |  | [audio_projectiles_tables](#audio_projectiles_tables) | key |
| shockwave_radius | False | F32 |  |  |  |
| can_damage_buildings | False | Boolean |  |  |  |
| contact_stat_effect | False | OptionalStringU8 |  | [special_ability_phases_tables](#special_ability_phases_tables) | id |
| is_grapple | False | Boolean |  |  |  |
  
## prologue_chapters_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| battle_key | False | OptionalStringU8 | Key in battles table (if this is a battle) | [battles_tables](#battles_tables) | key |
| campaign_key | False | OptionalStringU8 | Key in campaigns table (if this is a campaign) | [campaigns_tables](#campaigns_tables) | campaign_name |
| is_battle | False | Boolean | Is chapter a battle or campaign |  |  |
| number | True | I32 | Chapter number |  |  |
| banner | False | OptionalStringU8 | Path to the chapter banner from working_data |  |  |
  
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
| mercenary_set | True | StringU8 |  | [mercenary_pools_tables](#mercenary_pools_tables) | key |
| province | True | StringU8 |  | [provinces_tables](#provinces_tables) | key |
| optional_campaign_key | False | OptionalStringU8 | Empty means all campaigns using this province | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## provinces_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## provincial_initiative_records_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect_bundle | False | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| key | True | StringU8 |  |  |  |
| order | False | I32 |  |  |  |
| icon_path | False | StringU8 |  |  |  |
| campaign_vfx_id | False | OptionalStringU8 |  | [campaign_vfx_campaign_vfx_event_ids_tables](#campaign_vfx_campaign_vfx_event_ids_tables) | campaign_vfx_event |
  
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
| camera_heading | False | F32 |  |  |  |
| camera_position_x | False | F32 |  |  |  |
| camera_position_y | False | F32 |  |  |  |
| camera_zoom | False | F32 |  |  |  |
| group_key | True | StringU8 |  |  |  |
| round | False | I32 |  |  |  |
  
## region_religions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| region | True | StringU8 |  | [regions_tables](#regions_tables) | key |
| religion | False | StringU8 |  | [religions_tables](#religions_tables) | religion_key |
| religion_zeal | False | I32 |  |  |  |
  
## region_to_province_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| province | True | StringU8 |  | [provinces_tables](#provinces_tables) | key |
| region | True | StringU8 |  | [regions_tables](#regions_tables) | key |
  
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
| key | True | StringU8 |  |  |  |
| r | False | I32 |  |  |  |
| g | False | I32 |  |  |  |
| b | False | I32 |  |  |  |
| is_sea | False | Boolean |  |  |  |
| owner_bundle | False | OptionalStringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
  
## regions_to_region_groups_junctions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| region | True | StringU8 |  | [regions_tables](#regions_tables) | key |
| region_group | True | StringU8 |  | [region_groups_tables](#region_groups_tables) | group_key |
  
## religion_conversion_mods_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| rel_from | True | StringU8 |  | [religions_tables](#religions_tables) | religion_key |
| rel_to | True | StringU8 |  | [religions_tables](#religions_tables) | religion_key |
| modifier | False | F32 |  |  |  |
  
## religions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| religion_key | True | StringU8 |  |  |  |
| convertibility | False | I32 |  |  |  |
| ui_icon_path | False | StringU8 |  |  |  |
  
## resource_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| effect_key | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| resource_key | True | StringU8 |  | [resources_tables](#resources_tables) | key |
| value | False | F32 |  |  |  |
  
## resources_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| unit | False | OptionalStringU8 |  | [commodity_unit_names_tables](#commodity_unit_names_tables) | unit |
| slot_bed | False | StringU8 |  | [slots_tables](#slots_tables) | slot |
| trade_value | False | I32 |  |  |  |
| icon_filepath | False | StringU8 |  |  |  |
| strategic_value | False | I32 |  |  |  |
| in_encyclopedia | False | Boolean |  |  |  |
  
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
| attrition_type | True | StringU8 |  | [campaign_map_attritions_tables](#campaign_map_attritions_tables) | key |
| campaign | True | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| enable | True | Boolean |  |  |  |
| season | True | StringU8 |  | [seasons_tables](#seasons_tables) | season |
  
## season_province_effect_bundles_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| default | False | Boolean |  |  |  |
| effect_bundle | True | StringU8 |  | [effect_bundles_tables](#effect_bundles_tables) | key |
| province | True | StringU8 |  | [provinces_tables](#provinces_tables) | key |
| season | True | StringU8 |  | [seasons_tables](#seasons_tables) | season |
| weighting | False | I32 |  |  |  |
  
## seasons_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| season | True | StringU8 |  |  |  |
| onscreen | False | StringU8 |  |  |  |
| order | False | I32 |  |  |  |
  
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
| entity | False | StringU8 |  | [battle_entities_tables](#battle_entities_tables) | key |
| key | True | StringU8 |  |  |  |
| model | False | StringU8 |  | [models_naval_tables](#models_naval_tables) | key |
| spacing | False | StringU8 |  | [unit_spacings_tables](#unit_spacings_tables) | key |
  
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
| key | True | StringU8 |  |  |  |
  
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
| ability_group | True | StringU8 |  |  |  |
| icon_path | False | StringU8 |  |  |  |
| special_edition_mask | False | I32 |  |  |  |
  
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
| flag_key | True | StringU8 |  |  |  |
  
## special_ability_phase_attribute_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| attribute | True | StringU8 |  | [unit_attributes_tables](#unit_attributes_tables) | key |
| phase | True | StringU8 |  | [special_ability_phases_tables](#special_ability_phases_tables) | id |
  
## special_ability_phase_stat_effects_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| phase | True | StringU8 |  | [special_ability_phases_tables](#special_ability_phases_tables) | id |
| value | False | F32 |  |  |  |
| stat | True | StringU8 |  | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| how | False | StringU8 |  | [unit_stat_modifiers_how_enums_tables](#unit_stat_modifiers_how_enums_tables) | key |
  
## special_ability_phases_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| duration | False | F32 |  |  |  |
| effect_type | False | StringU8 |  | [special_ability_phase_effect_types_tables](#special_ability_phase_effect_types_tables) | effect_type |
| id | True | StringU8 |  |  |  |
| requested_stance | False | OptionalStringU8 |  | [special_ability_stance_enums_tables](#special_ability_stance_enums_tables) | key |
| unbreakable | False | Boolean |  |  |  |
| cant_move | False | Boolean |  |  |  |
| kill_own_unit | False | Boolean |  |  |  |
| freeze_fatigue | False | Boolean |  |  |  |
| fatigue_change_ratio | False | F32 | This is a scalar that changes the unit's fatigue (once off) relative to the maximum. For example, -0.25 will reduce it by 25% and 1.1 will increase it by 10% |  |  |
| inspiration_aura_range_mod | False | F32 |  |  |  |
| ability_recharge_change | False | F32 |  |  |  |
| minor_casualties | False | Boolean |  |  |  |
| major_casualties | False | Boolean |  |  |  |
| ui_vfx | False | OptionalStringU8 |  | [ui_effects_tables](#ui_effects_tables) | key |
| rally_amount | False | I32 | This will adda certain amount to the morale score, and also prevent routing while active |  |  |
  
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
| end | False | I32 |  |  |  |
| language | True | StringU8 |  | [languages_tables](#languages_tables) | key |
| script_id | False | I32 |  | [vo_scripts_tables](#vo_scripts_tables) | id |
| start | False | I32 |  |  |  |
| subtitle_field | True | StringU8 |  | [TExc_LocalisableFields_tables](#TExc_LocalisableFields_tables) | key |
| text_section | True | I32 |  |  |  |
| foreign_key | True | StringU8 |  |  |  |
| text_id | False | StringU8 |  |  |  |
  
## taxes_classes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| tax | True | StringU8 |  |  |  |
  
## taxes_effects_jct_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| tax_name | True | StringU8 |  | [taxes_keys_tables](#taxes_keys_tables) | tax_lookup |
| effect | True | StringU8 |  | [effects_tables](#effects_tables) | effect |
| effect_scope | False | StringU8 |  | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| ai_only | True | Boolean |  |  |  |
| optional_campaign_key | True | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| optional_difficulty_level | True | OptionalStringU8 |  |  |  |
| value | False | F32 |  |  |  |
  
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
| key | True | StringU8 |  |  |  |
| building_level | False | StringU8 |  | [building_levels_tables](#building_levels_tables) | level_name |
| position_index | False | I32 |  |  |  |
| research_points_required | False | I32 |  |  |  |
| icon_name | False | StringU8 |  |  |  |
| military_prestige | False | I32 |  |  |  |
| naval_prestige | False | I32 |  |  |  |
| economic_prestige | False | I32 |  |  |  |
| enlightenment_prestige | False | I32 |  |  |  |
| mp_available_early | False | Boolean |  |  |  |
| mp_available_late | False | Boolean |  |  |  |
| info_pic | False | StringU8 |  |  |  |
| ai_bias | False | I32 |  |  |  |
| unique_index | False | I32 |  |  |  |
| cost_per_round | False | I32 |  |  |  |
| is_civil | False | Boolean |  |  |  |
| is_engineering | False | Boolean |  |  |  |
| is_military | False | Boolean |  |  |  |
  
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
| child_key | True | StringU8 |  | [technology_nodes_tables](#technology_nodes_tables) | key |
| initial_descent_tiers | False | I32 |  |  |  |
| parent_key | True | StringU8 |  | [technology_nodes_tables](#technology_nodes_tables) | key |
| parent_link_position | False | I32 |  |  |  |
| child_link_position | False | I32 |  |  |  |
  
## technology_node_sets_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_key | False | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| faction_key | False | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| culture | False | OptionalStringU8 |  | [cultures_tables](#cultures_tables) | key |
| subculture | False | OptionalStringU8 |  | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| key | True | StringU8 |  |  |  |
| technology_category | False | StringU8 |  | [technology_categories_tables](#technology_categories_tables) | key |
  
## technology_nodes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| campaign_key | False | OptionalStringU8 |  | [campaigns_tables](#campaigns_tables) | campaign_name |
| faction_key | False | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| indent | False | I32 |  |  |  |
| key | True | StringU8 |  |  |  |
| technology_key | False | StringU8 |  | [technologies_tables](#technologies_tables) | key |
| technology_node_set | False | StringU8 |  | [technology_node_sets_tables](#technology_node_sets_tables) | key |
| tier | False | I32 |  |  |  |
  
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
| trait | True | StringU8 |  |  |  |
| applicable_to | False | StringU8 |  |  |  |
  
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
| stat_key | True | StringU8 |  | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| unit_class | True | StringU8 |  | [unit_class_tables](#unit_class_tables) | key |
| list_order | False | I32 |  |  |  |
| filter | True | StringU8 |  | [ui_unit_stats_filters_tables](#ui_unit_stats_filters_tables) | key |
  
## ui_unit_stats_filters_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
## ui_unit_stats_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| onscreen_name | False | StringU8 | On screen name for stat that is shown on info panel |  |  |
| max_value | False | I32 | Maximum value of stat, affects stat bars on info panel when calculating percentage full |  |  |
| campaign_only | False | Boolean | Is the stat only relevant to campaign? These are only shown in campaign. |  |  |
| sort_order | False | I32 | Determines order stats shown on info panel |  |  |
  
## unit_abilities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| stationary_for_turn | False | Boolean |  |  |  |
| supersedes_ability | False | OptionalStringU8 |  |  |  |
| requires_effect_enabling | False | Boolean |  |  |  |
| tooltip_text | False | OptionalStringU8 |  |  |  |
  
## unit_armour_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| armour_value | False | I32 |  |  |  |
| bonus_v_missiles | False | OptionalStringU8 |  |  |  |
| key | True | StringU8 |  |  |  |
| weak_v_missiles | False | OptionalStringU8 |  |  |  |
| audio_material | False | StringU8 |  | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
  
## unit_attributes_groups_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| group_name | True | StringU8 |  |  |  |
  
## unit_attributes_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
  
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
| key | True | StringU8 |  |  |  |
| localised_name | False | OptionalStringU8 |  |  |  |
| r_colour | False | F32 |  |  |  |
| g_colour | False | F32 |  |  |  |
| b_colour | False | F32 |  |  |  |
| min_battle_rows | False | I32 |  |  |  |
  
## unit_class_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| onscreen | False | StringU8 |  |  |  |
| sort_priority | False | I32 |  |  |  |
| icon | False | StringU8 |  |  |  |
| can_assault_settlment | False | Boolean |  |  |  |
  
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
| fatigue_level | True | StringU8 |  | [_kv_fatigue_tables](#_kv_fatigue_tables) | key |
| stat | True | StringU8 |  | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| value | False | F32 |  |  |  |
  
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
| key | True | StringU8 |  |  |  |
  
## unit_shield_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  |  |  |
| shield_defence_value | False | I32 |  |  |  |
| shield_armour_value | False | I32 |  |  |  |
| audio_material | False | StringU8 |  | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
| missile_block_chance | False | I32 |  |  |  |
  
## unit_spacings_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| close_formation_spacing_horizontal | False | F32 |  |  |  |
| close_formation_spacing_variation | False | F32 |  |  |  |
| close_formation_spacing_vertical | False | F32 |  |  |  |
| dismounted_close_formation_spacing_horizontal | False | F32 |  |  |  |
| dismounted_close_formation_spacing_variation | False | F32 |  |  |  |
| dismounted_close_formation_spacing_vertical | False | F32 |  |  |  |
| dismounted_loose_formation_spacing_horizontal | False | F32 |  |  |  |
| dismounted_loose_formation_spacing_variation | False | F32 |  |  |  |
| dismounted_loose_formation_spacing_vertical | False | F32 |  |  |  |
| horde | False | Boolean |  |  |  |
| key | True | StringU8 |  |  |  |
| loose_formation_spacing_horizontal | False | F32 |  |  |  |
| loose_formation_spacing_variation | False | F32 |  |  |  |
| loose_formation_spacing_vertical | False | F32 |  |  |  |
  
## unit_special_abilities_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| key | True | StringU8 |  | [unit_abilities_tables](#unit_abilities_tables) | key |
| active_time | False | F32 |  |  |  |
| recharge_time | False | F32 |  |  |  |
| num_uses | False | I32 |  |  |  |
| effect_range | False | F32 |  |  |  |
| affect_self | False | Boolean |  |  |  |
| num_effected_friendly_units | False | I32 |  |  |  |
| num_effected_enemy_units | False | I32 |  |  |  |
| update_targets_every_frame | False | Boolean |  |  |  |
| initial_recharge | False | F32 |  |  |  |
| activated_projectile | False | OptionalStringU8 |  | [projectiles_tables](#projectiles_tables) | key |
| can_autotrigger | False | Boolean |  |  |  |
| target_friends | False | Boolean |  |  |  |
| target_enemies | False | Boolean |  |  |  |
| target_ground | False | Boolean |  |  |  |
| target_intercept_range | False | F32 |  |  |  |
| assume_specific_behaviour | False | OptionalStringU8 |  | [special_abilities_specific_behaviour_types_tables](#special_abilities_specific_behaviour_types_tables) | key |
| clear_current_order | False | Boolean |  |  |  |
| wind_up_time | False | F32 |  |  |  |
| passive | False | Boolean |  |  |  |
| unique_id | False | I32 |  |  |  |
  
## unit_stat_modifiers_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| how | False | StringU8 |  | [unit_stat_modifiers_how_enums_tables](#unit_stat_modifiers_how_enums_tables) | key |
| key | True | StringU8 |  |  |  |
| stat | False | StringU8 |  | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
  
## unit_stats_land_experience_bonuses_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| xp_level | True | StringU8 |  |  |  |
| melee_attack | False | I32 |  |  |  |
| melee_defence | False | I32 |  |  |  |
| core_reloading_skill | False | I32 |  |  |  |
| morale | False | I32 |  |  |  |
| core_marksmanship | False | I32 |  |  |  |
| fatigue | False | I32 |  |  |  |
| mp_fixed_cost | False | I32 |  |  |  |
| mp_experience_cost_multiplier | False | F32 |  |  |  |
  
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
| faction | True | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| primary_colour_b | False | I32 |  |  |  |
| primary_colour_g | False | I32 |  |  |  |
| primary_colour_r | False | I32 |  |  |  |
| secondary_colour_b | False | I32 |  |  |  |
| secondary_colour_g | False | I32 |  |  |  |
| secondary_colour_r | False | I32 |  |  |  |
| soldier_type | False | OptionalStringU8 |  | [uniform_type_enums_tables](#uniform_type_enums_tables) | key |
| tertiary_colour_b | False | I32 |  |  |  |
| tertiary_colour_g | False | I32 |  |  |  |
| tertiary_colour_r | False | I32 |  |  |  |
| unit_variant | True | StringU8 |  | [unit_variants_tables](#unit_variants_tables) | name |
  
## unit_variants_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| faction | True | OptionalStringU8 |  | [factions_tables](#factions_tables) | key |
| name | False | StringU8 |  |  |  |
| unit | True | StringU8 |  | [land_units_tables](#land_units_tables) | key |
| variant | False | StringU8 |  | [variants_tables](#variants_tables) | variant_name |
| height_variation | False | F32 |  |  |  |
| height_scale | False | F32 |  |  |  |
| unit_card | False | StringU8 |  |  |  |
  
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
| faction | True | StringU8 |  | [factions_tables](#factions_tables) | key |
| general_unit | True | Boolean |  |  |  |
| unit | True | StringU8 |  | [main_units_tables](#main_units_tables) | unit |
| siege_unit_attacker | False | Boolean |  |  |  |
| siege_unit_defender | False | Boolean |  |  |  |
  
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
| variant_name | True | StringU8 |  |  |  |
  
## victory_conditions_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| condition | True | StringU8 |  |  |  |
  
## victory_types_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| victory_type | True | OptionalStringU8 |  |  |  |
| tree_y | False | I32 | Tree y position for ui display |  |  |
| tree_x | False | I32 | Tree x position for ui display |  |  |
| length_type | False | StringU8 |  |  |  |
| icon | False | StringU8 | Icon for tree in ui display |  |  |
  
## videos_tables

| Name | Key | Type | Description | RefTable | RefKey
|------|---------|--------|--------|--------|--------|
| video_name | True | StringU8 |  |  |  |
| video_type | False | StringU8 |  | [video_types_tables](#video_types_tables) | video_type |
| audio_tracks | False | I32 |  |  |  |
| script_ref | False | I32 |  | [vo_scripts_tables](#vo_scripts_tables) | id |
  
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