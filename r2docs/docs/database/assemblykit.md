---
title: assemblykit
summary: A brief description of my document.
---

# Assembly Kit Database
---
Database schemas extracted from the assembly kit `TWaD_` files.  


  
## abilities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ability | True | text | True | 50 | None | None |
| cannot_fail | False | yesno | True | None | None | None |
  
## achievements_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 80 | None | None |
| title | False | text | True | 50 | None | None |
| description | False | text | True | 536870910 | None | None |
  
## action_results_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| actor_effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| target_effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
  
## action_results_additional_outcomes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| action_result_key | False | text | True | 255 | [action_results_tables](#action_results_tables) | key |
| outcome | False | text | True | 255 | [action_results_additional_outcomes_enums_tables](#action_results_additional_outcomes_enums_tables) | key |
| value | False | double | True | None | None | None |
| effect_record | False | text | False | 255 | [effects_tables](#effects_tables) | effect |
| effect_scope_record | False | text | False | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| key | True | text | True | 255 | None | None |
| opportune_failure_weighting | False | integer | False | None | None | None |
| authority_value_coefficient | False | double | True | None | None | None |
| subterfuge_value_coefficient | False | double | True | None | None | None |
| zeal_value_coefficient | False | double | True | None | None | None |
  
## action_results_additional_outcomes_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## advice_info_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| advice_level_lookup | False | integer | True | None | [advice_levels_tables](#advice_levels_tables) | key |
| localised_text | False | text | True | 255 | None | None |
| persistant | False | yesno | True | None | None | None |
| show_on_navigate | False | yesno | True | None | None | None |
| show_instant | False | yesno | True | None | None | None |
| is_header | False | yesno | True | None | None | None |
| navigation_order | False | integer | True | None | None | None |
  
## advice_levels_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| advice_thread | False | text | True | 255 | [advice_threads_tables](#advice_threads_tables) | thread |
| advice_thread_level | False | integer | True | None | None | None |
| points_needed | False | integer | True | None | None | None |
| game_area | False | text | True | 255 | None | None |
| category | False | text | True | 255 | None | None |
| sub_category | False | text | True | 255 | None | None |
| max_repeat_count | False | integer | True | None | None | None |
| repeat_interval | False | integer | True | None | None | None |
| pause_battle | False | yesno | True | None | None | None |
| advice_item_title | False | text | False | 255 | None | None |
| priority_level | False | integer | True | None | None | None |
| high_verbosity_only | False | yesno | False | None | None | None |
| locatable | False | yesno | False | None | None | None |
| parameter | False | text | True | 50 | None | None |
| on_display_script | False | text | False | 536870910 | None | None |
| on_click_script | False | text | False | 536870910 | None | None |
| suppressible | False | yesno | True | None | None | None |
| uninhibitable | False | yesno | True | None | None | None |
| audio_clip | False | text | True | 255 | None | None |
| onscreen_text | False | text | True | 536870910 | None | None |
| advisor_name | False | text | True | 255 | [advisors_tables](#advisors_tables) | advisor_name |
| for_loading_screen | False | yesno | False | None | None | None |
| movie_link | False | text | False | 255 | None | None |
  
## advice_threads_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| thread | True | text | True | 50 | None | None |
  
## advice_triggers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| test_when | False | text | True | 255 | [trigger_events_tables](#trigger_events_tables) | event |
| condition_script | False | text | False | 536870910 | None | None |
  
## advice_trigger_to_advice_thread_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| trigger | True | text | True | 255 | [advice_triggers_tables](#advice_triggers_tables) | key |
| thread | True | text | True | 50 | [advice_threads_tables](#advice_threads_tables) | thread |
| amount | False | text | True | 50 | None | None |
  
## advisors_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| advisor_name | True | text | True | 255 | None | None |
| advisor_icon_path | False | text | True | 255 | None | None |
  
## agents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| move_points | False | integer | True | None | None | None |
| line_of_sight | False | integer | True | None | None | None |
| playable | False | yesno | True | None | None | None |
| portrait_override | False | text | False | 50 | None | None |
| primary_attribute | False | text | False | 50 | [agent_attributes_tables](#agent_attributes_tables) | key |
| religion | False | text | False | 50 | [religions_tables](#religions_tables) | religion_key |
| faction_total_cap | False | integer | True | None | None | None |
| cost | False | integer | True | None | None | None |
| in_encyclopedia | False | yesno | True | None | None | None |
  
## agent_actions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent | True | text | True | 255 | [agents_tables](#agents_tables) | key |
| ability | True | text | True | 50 | [abilities_tables](#abilities_tables) | ability |
| attribute | True | text | True | 50 | [agent_attributes_tables](#agent_attributes_tables) | key |
| critical_failure | False | text | True | 255 | [action_results_tables](#action_results_tables) | key |
| failure | False | text | True | 255 | [action_results_tables](#action_results_tables) | key |
| opportune_failure | False | text | True | 255 | [action_results_tables](#action_results_tables) | key |
| success | False | text | True | 255 | [action_results_tables](#action_results_tables) | key |
| critical_success | False | text | True | 255 | [action_results_tables](#action_results_tables) | key |
| cannot_fail | False | text | True | 255 | [action_results_tables](#action_results_tables) | key |
| localised_action_name | False | text | True | 255 | None | None |
| localised_action_description | False | text | True | 255 | None | None |
| your_message_events_male | False | text | False | 255 | [agent_action_message_events_tables](#agent_action_message_events_tables) | key |
| your_message_events_female | False | text | False | 255 | [agent_action_message_events_tables](#agent_action_message_events_tables) | key |
| their_message_events_male | False | text | False | 255 | [agent_action_message_events_tables](#agent_action_message_events_tables) | key |
| their_message_events_female | False | text | False | 255 | [agent_action_message_events_tables](#agent_action_message_events_tables) | key |
| enabled_by_effect | False | text | False | 255 | [effects_tables](#effects_tables) | effect |
  
## agent_action_message_events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| critical_failure | False | text | False | 255 | [message_events_tables](#message_events_tables) | event |
| failure | False | text | False | 255 | [message_events_tables](#message_events_tables) | event |
| opportune_failure | False | text | False | 255 | [message_events_tables](#message_events_tables) | event |
| success | False | text | False | 255 | [message_events_tables](#message_events_tables) | event |
| critical_success | False | text | False | 255 | [message_events_tables](#message_events_tables) | event |
  
## agent_attributes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## agent_culture_details_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| agent | False | text | True | 50 | [agents_tables](#agents_tables) | key |
| culture | False | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| onscreen_name | False | text | True | 50 | None | None |
| associated_unit | False | text | False | 255 | [main_units_tables](#main_units_tables) | unit |
| description_text | False | text | True | 20000 | None | None |
| season | False | text | False | 255 | None | None |
| level | False | integer | True | None | None | None |
| equipment_theme | False | text | False | 255 | None | None |
| agent_recruited_movie | False | text | False | 50 | [movie_event_strings_tables](#movie_event_strings_tables) | event |
| gender | False | text | False | 255 | [genders_tables](#genders_tables) | gender |
  
## agent_localisations_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| text | False | text | True | 255 | None | None |
  
## agent_string_faction_overrides_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent | True | text | True | 255 | [agents_tables](#agents_tables) | key |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| gender | True | text | True | 255 | [genders_tables](#genders_tables) | gender |
| name_override | False | text | False | 255 | None | None |
| description_override | False | text | False | 255 | None | None |
| icon_path | False | text | False | 255 | None | None |
  
## agent_string_subculture_overrides_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent | True | text | True | 255 | [agents_tables](#agents_tables) | key |
| subculture | True | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| gender | True | text | True | 255 | [genders_tables](#genders_tables) | gender |
| name_override | False | text | False | 255 | None | None |
| description_override | False | text | False | 255 | None | None |
| icon_path | False | text | False | 255 | None | None |
  
## agent_subculture_gender_overrides_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent | True | text | True | 255 | [agents_tables](#agents_tables) | key |
| subculture | True | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| gender | True | text | True | 255 | [genders_tables](#genders_tables) | gender |
  
## agent_to_agent_abilities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent | True | text | True | 50 | [agents_tables](#agents_tables) | key |
| ability | True | text | True | 50 | [abilities_tables](#abilities_tables) | ability |
| localised_ability_name | False | text | True | 255 | None | None |
| localised_ability_description | False | text | True | 255 | None | None |
  
## agent_to_agent_attributes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| attribute | True | text | True | 50 | [agent_attributes_tables](#agent_attributes_tables) | key |
| agent | True | text | True | 50 | [agents_tables](#agents_tables) | key |
| default_value | False | integer | True | None | None | None |
  
## agent_uniforms_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| uniform_name | True | text | True | 255 | None | None |
| filename | False | text | True | 255 | [variants_tables](#variants_tables) | variant_name |
| battle_filename | False | text | False | 255 | [variants_tables](#variants_tables) | variant_name |
| campaign_porthole_filename | False | text | False | 255 | [variants_tables](#variants_tables) | variant_name |
| audio_armour_type | False | text | True | 255 | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
| audio_weapon_type | False | text | True | 255 | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
| audio_shield_type | False | text | True | 255 | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
| campaign_politician_filename | False | text | False | 255 | None | None |
  
## aide_de_camp_speeches_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| text | False | text | True | 255 | None | None |
| picture_in_picture | False | yesno | True | None | None | None |
| offset_angle | False | double | True | None | None | None |
| offset_range | False | double | True | None | None | None |
| circumvent_cooldown | False | yesno | True | None | None | None |
| cinematic_event | False | text | False | 255 | [battle_cinematic_events_tables](#battle_cinematic_events_tables) | key |
  
## ambient_battlefield_objects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ambient_battlefield_object | True | text | True | 50 | None | None |
  
## ambient_battlefield_objects_junc_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| climate | True | text | True | 50 | [climates_tables](#climates_tables) | climate_type |
| season | True | text | True | 50 | [seasons_tables](#seasons_tables) | season |
| ambient_battlefield_object | True | text | True | 50 | [ambient_battlefield_objects_tables](#ambient_battlefield_objects_tables) | ambient_battlefield_object |
  
## ancillaries_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
| onscreen_name | False | text | True | 255 | None | None |
| type | False | text | True | 255 | [ancillary_types_tables](#ancillary_types_tables) | type |
| applies_to | False | text | True | 50 | None | None |
| transferrable | False | yesno | True | None | None | None |
| unique_to_world | False | yesno | True | None | None | None |
| unique_to_faction | False | yesno | False | None | None | None |
| precedence | False | integer | False | None | None | None |
| start_date | False | integer | True | None | None | None |
| end_date | False | integer | True | None | None | None |
| effect_text | False | text | True | 536870910 | None | None |
| colour_text | False | text | True | 536870910 | None | None |
| explanation_text | False | text | False | 536870910 | None | None |
| exclusion_text | False | text | False | 536870910 | None | None |
| avatar_skill | False | text | False | 255 | None | None |
| avatar_special_ability | False | text | False | 255 | None | None |
| legendary_item | False | yesno | True | None | None | None |
| mp_exclusive | False | yesno | True | None | None | None |
| is_wife_ancillary | False | yesno | True | None | None | None |
| is_husband_ancillary | False | yesno | True | None | None | None |
| is_diplomatic_ancillary | False | yesno | True | None | None | None |
| is_dynastic_ancillary | False | yesno | True | None | None | None |
| spouse_subculture | False | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| category | False | text | True | 255 | [ancillaries_categories_tables](#ancillaries_categories_tables) | category |
| min_starting_age | False | integer | True | None | None | None |
| max_starting_age | False | integer | True | None | None | None |
| min_expiry_age | False | integer | True | None | None | None |
| max_expiry_age | False | integer | True | None | None | None |
| spouse_type | False | text | False | 255 | [marriage_types_tables](#marriage_types_tables) | key |
  
## ancillaries_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| category | True | text | True | 255 | None | None |
  
## ancillary_included_subcultures_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ancillary | True | text | True | 50 | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
| subculture | True | text | True | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## ancillary_info_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ancillary | True | text | True | 50 | None | None |
| historical_example | False | text | False | 50 | None | None |
| author | False | text | True | 50 | None | None |
| comment | False | text | False | 536870910 | None | None |
  
## ancillary_to_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ancillary | True | text | True | 50 | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | double | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## ancillary_to_excluded_ancillaries_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ancillary | True | text | True | 50 | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
| excluded_ancillary | True | text | True | 50 | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
  
## ancillary_to_included_agents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ancillary | True | text | True | 50 | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
| agent | True | text | True | 50 | [agents_tables](#agents_tables) | key |
  
## ancillary_triggers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| trigger | True | text | True | 50 | None | None |
| event | False | text | True | 50 | [trigger_events_tables](#trigger_events_tables) | event |
| conditions | False | text | False | 536870910 | None | None |
  
## ancillary_triggers_to_ancillary_removals_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| trigger | False | text | False | 50 | [ancillary_triggers_tables](#ancillary_triggers_tables) | trigger |
| ancillary | False | text | True | 50 | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
  
## ancillary_trigger_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| trigger | False | text | True | 50 | [ancillary_triggers_tables](#ancillary_triggers_tables) | trigger |
| ancillary | False | text | True | 50 | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
| chance | False | integer | True | None | None | None |
  
## ancillary_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 50 | None | None |
| ui_icon | False | text | True | 50 | None | None |
  
## animals_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| animation | False | text | True | 255 | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| entity | False | text | True | 255 | [battle_entities_tables](#battle_entities_tables) | key |
| melee_attack | False | integer | True | None | None | None |
| melee_defence | False | integer | True | None | None | None |
| charge_bonus | False | integer | True | None | None | None |
| armour | False | text | False | 255 | [unit_armour_types_tables](#unit_armour_types_tables) | key |
  
## animation_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name | True | text | True | 200000 | None | None |
| order | False | integer | True | None | None | None |
  
## animation_slot_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| slot | True | text | True | 200000 | None | None |
| category | True | text | True | 200000 | [animation_categories_tables](#animation_categories_tables) | name |
  
## anim_reference_poses_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| path | False | text | True | 536870910 | None | None |
| root_node | False | text | True | 50 | None | None |
  
## armed_citizenry_units_to_unit_groups_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| unit_group | False | text | True | 255 | [armed_citizenry_unit_groups_tables](#armed_citizenry_unit_groups_tables) | unit_group |
| unit | False | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| priority | False | integer | True | None | None | None |
  
## armed_citizenry_unit_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_group | True | text | True | 255 | None | None |
  
## audio_campaign_building_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## audio_explosions_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## audio_materials_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## audio_projectiles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| audio_projectile_type | False | text | True | 255 | [audio_projectiles_enums_tables](#audio_projectiles_enums_tables) | key |
| play_incoming_sound | False | yesno | True | None | None | None |
| max_attenuation_fire | False | double | True | None | None | None |
| max_attenuation_inflight | False | double | True | None | None | None |
| max_attenuation_impact | False | double | True | None | None | None |
| requires_speed | False | yesno | True | None | None | None |
| requires_distance | False | yesno | True | None | None | None |
| inflight_min_speed | False | double | True | None | None | None |
  
## audio_projectiles_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## audio_vo_actors_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## audio_vo_actor_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| actor_1 | False | text | True | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_2 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_3 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_4 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_5 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_6 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_7 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_8 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_9 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_10 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_11 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_12 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_13 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_14 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_15 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
  
## audio_vo_selected_switches_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## banditry_events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name | True | text | True | 255 | None | None |
| message_event | False | text | True | 255 | [message_events_tables](#message_events_tables) | event |
| province_effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| minimum_banditry | False | integer | True | None | None | None |
| maximum_banditry | False | integer | True | None | None | None |
| weight | False | integer | True | None | None | None |
| duration | False | integer | True | None | None | None |
  
## battlefield_buildings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| category | False | text | True | 50 | [battlefield_building_categories_tables](#battlefield_building_categories_tables) | category |
| model | False | text | True | 50 | [models_building_tables](#models_building_tables) | key |
| audio_material | False | text | True | 255 | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
| hit_points | False | text | True | 50 | None | None |
| gun_type | False | text | False | 255 | [missile_weapons_tables](#missile_weapons_tables) | key |
| onscreen_name | False | text | False | 50 | [battlefield_buildings_names_tables](#battlefield_buildings_names_tables) | key |
| ignition_threshold | False | integer | True | None | None | None |
| radar_icon | False | text | False | 2000 | None | None |
| visible_in_public_ted | False | yesno | True | None | None | None |
| fortwall_penetration_chance | False | integer | True | None | None | None |
| collision_3d | False | yesno | True | None | None | None |
| destruct_thresholds | False | text | False | 255 | None | None |
| joiner | False | yesno | True | None | None | None |
| auxiliary | False | yesno | True | None | None | None |
| burn_rate | False | single | True | None | None | None |
  
## battlefield_buildings_names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| onscreen_name | False | text | True | 50 | None | None |
| key | True | text | True | 50 | None | None |
| global_effects_description | False | text | False | 255 | None | None |
| local_effects_description | False | text | False | 255 | None | None |
  
## battlefield_buildings_with_projectiles_names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building_category | True | text | True | 255 | [battlefield_building_categories_tables](#battlefield_building_categories_tables) | category |
| projectile | True | text | True | 255 | [projectiles_tables](#projectiles_tables) | key |
| name | False | text | True | 255 | [battlefield_buildings_names_tables](#battlefield_buildings_names_tables) | key |
  
## battlefield_building_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| category | True | text | True | 50 | None | None |
| default_destruction_effect | False | text | True | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| icon_path | False | text | True | 255 | None | None |
  
## battlefield_building_transformations_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| transformation | True | text | True | 50 | None | None |
| description | False | text | False | 255 | None | None |
  
## battlefield_chariots_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| chariot_type | False | text | True | 255 | [chariot_types_enums_tables](#chariot_types_enums_tables) | key |
| model | False | text | True | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
| chariot_animation_table | False | text | True | 255 | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| destruction_animation | False | text | True | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
| destroyed_model | False | text | True | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| battle_entity | False | text | True | 255 | [battle_entities_tables](#battle_entities_tables) | key |
  
## battlefield_deployable_siege_items_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| battlefield_siege_vehicle | False | text | True | 50 | [battlefield_siege_vehicles_tables](#battlefield_siege_vehicles_tables) | key |
| level | False | integer | True | None | None | None |
| type | False | text | False | 255 | None | None |
  
## battlefield_engines_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| engine_type | False | text | True | 255 | [gun_types_enum_tables](#gun_types_enum_tables) | key |
| model | False | text | True | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
| gun_animation_table | False | text | True | 255 | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| missile_weapon | False | text | False | 255 | [missile_weapons_tables](#missile_weapons_tables) | key |
| destruction_animation | False | text | False | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
| destroyed_model | False | text | False | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| battle_entity | False | text | True | 50 | [battle_entities_tables](#battle_entities_tables) | key |
| can_move | False | yesno | True | None | None | None |
  
## battlefield_engines_autonomous_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| autonomous_engine_type | False | text | True | 255 | [battlefield_engines_tables](#battlefield_engines_tables) | key |
| engine_crew_entity | False | text | True | 255 | [battle_entities_tables](#battle_entities_tables) | key |
| engine_crew_anims | False | text | True | 255 | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| num_ammo | False | integer | True | None | None | None |
  
## battlefield_siege_vehicles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| model | False | text | True | 50 | [models_sieges_tables](#models_sieges_tables) | key |
| hit_points | False | integer | True | None | None | None |
| battle_entity | False | text | True | 50 | [battle_entities_tables](#battle_entities_tables) | key |
| gun_type | False | text | False | 255 | None | None |
| docking_clearance | False | double | True | None | None | None |
| engine | False | text | False | 255 | [battlefield_engines_autonomous_tables](#battlefield_engines_autonomous_tables) | key |
| onscreen_name | False | text | False | 255 | None | None |
| description | False | text | False | 255 | None | None |
| image_path | False | text | True | 255 | None | None |
| recruitment_cap | False | integer | True | None | None | None |
| uses_8m_wall | False | yesno | True | None | None | None |
| uses_15m_wall | False | yesno | True | None | None | None |
| cost | False | integer | True | None | None | None |
| category_image_path | False | text | True | 255 | None | None |
| special_edition_mask | False | integer | True | None | None | None |
| ignition_threshold | False | integer | True | None | None | None |
| attack_damage | False | double | True | None | None | None |
| selection_priority | False | double | True | None | None | None |
  
## battlefield_siege_vehicles_custom_battles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| vehicle | True | text | True | 255 | [battlefield_siege_vehicles_tables](#battlefield_siege_vehicles_tables) | key |
| cap | False | integer | True | None | None | None |
| probability | False | decimal | True | None | None | None |
  
## battlefield_siege_vehicles_to_autonomous_engines_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| vehicle | True | text | True | 255 | [battlefield_siege_vehicles_tables](#battlefield_siege_vehicles_tables) | key |
| engine | True | text | True | 255 | [battlefield_engines_autonomous_tables](#battlefield_engines_autonomous_tables) | key |
  
## battlefield_snow_props_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| prop | True | text | True | 50 | [battlefield_buildings_tables](#battlefield_buildings_tables) | key |
| enable_for_snow | True | yesno | True | None | [seasons_tables](#seasons_tables) | season |
  
## battlefield_temperatures_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| climate | True | text | True | 50 | [climates_tables](#climates_tables) | climate_type |
| season | True | text | True | 50 | [seasons_tables](#seasons_tables) | season |
| temperature | False | text | True | 50 | None | None |
  
## battles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| type | False | text | True | 255 | [battle_types_tables](#battle_types_tables) | type |
| is_naval | False | yesno | True | None | None | None |
| specification | False | text | True | 255 | None | None |
| localised_name | False | text | True | 255 | None | None |
| description | False | text | True | 536870910 | None | None |
| objectives_team_1 | False | text | True | 536870910 | None | None |
| objectives_team_2 | False | text | False | 536870910 | None | None |
| screenshot_path | False | text | False | 255 | None | None |
| map_path | False | text | False | 255 | None | None |
| team_size_1 | False | integer | True | None | None | None |
| team_size_2 | False | integer | True | None | None | None |
| release | False | yesno | False | None | None | None |
| multiplayer | False | yesno | False | None | None | None |
| singleplayer | False | yesno | False | None | None | None |
| intro_movie | False | text | False | 255 | None | None |
| year | False | integer | True | None | None | None |
| defender_funds_ratio | False | double | True | None | None | None |
| has_key_buildings | False | yesno | False | None | None | None |
| matchmaking | False | yesno | True | None | None | None |
| playable_area_width | False | double | True | None | None | None |
| playable_area_height | False | double | True | None | None | None |
| is_large_settlement | False | yesno | True | None | None | None |
| has_15m_walls | False | yesno | True | None | None | None |
  
## battles_to_battle_sky_types_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle_key | True | text | True | 255 | [battles_tables](#battles_tables) | key |
| battle_sky_type_key | True | text | True | 255 | [battle_sky_types_tables](#battle_sky_types_tables) | key |
  
## battle_animations_table_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## battle_autoresolver_balances_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| source_unit_class | True | text | True | 50 | [unit_class_tables](#unit_class_tables) | key |
| target_unit_class | True | text | True | 50 | [unit_class_tables](#unit_class_tables) | key |
| melee_potential_multiplier | False | single | True | None | None | None |
| missile_potential_multiplier | False | single | True | None | None | None |
  
## battle_bridge_subculture_jcts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| subculture | True | text | True | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| simple_bridge | False | text | True | 50 | [battlefield_buildings_tables](#battlefield_buildings_tables) | key |
| refined_bridge | False | text | True | 50 | [battlefield_buildings_tables](#battlefield_buildings_tables) | key |
  
## battle_cameras_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| min_height | False | single | True | None | None | None |
| max_height_small | False | single | True | None | None | None |
| max_height_large | False | single | True | None | None | None |
| min_fort_max_height | False | single | True | None | None | None |
| move_speed_min_multiplier | False | single | True | None | None | None |
| move_speed_max_multiplier | False | single | True | None | None | None |
| turn_speed_multiplier | False | single | True | None | None | None |
| move_fast_multiplier | False | single | True | None | None | None |
  
## battle_cinematic_events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| filename | False | text | True | 255 | None | None |
| priority | False | integer | True | None | None | None |
| level | False | text | True | 255 | None | None |
| window_in | False | integer | True | None | None | None |
| window_out | False | integer | True | None | None | None |
| repeat_wait_ms | False | integer | True | None | None | None |
| event_category | False | text | True | 255 | [battle_cinematic_event_categories_tables](#battle_cinematic_event_categories_tables) | key |
| time_after_event | False | integer | True | None | None | None |
  
## battle_cinematic_event_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## battle_cities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| city | True | text | True | 50 | None | None |
| minimum_building_scale | False | decimal | True | None | None | None |
| maximum_building_scale | False | decimal | True | None | None | None |
| town_min_distance | False | integer | True | None | None | None |
| city_min_distance | False | integer | True | None | None | None |
| town_radius | False | integer | True | None | None | None |
| city_radius | False | integer | True | None | None | None |
| number_of_town_buildings | False | integer | True | None | None | None |
| number_of_city_buildings | False | integer | True | None | None | None |
  
## battle_city_buildings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building | True | text | True | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| city | False | text | True | 50 | [battle_cities_tables](#battle_cities_tables) | city |
| amount_in_town | False | integer | True | None | None | None |
| amount_in_city | False | integer | True | None | None | None |
  
## battle_city_subculture_jct_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| subculture | True | text | True | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| city | False | text | True | 50 | [battle_cities_tables](#battle_cities_tables) | city |
  
## battle_climate_weather_descriptions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | False | text | True | 50 | None | None |
| climate_type | True | text | True | 50 | [climates_tables](#climates_tables) | climate_type |
| season | True | text | False | 50 | [seasons_tables](#seasons_tables) | season |
| weather_type | True | text | True | 50 | [battle_weather_types_tables](#battle_weather_types_tables) | key |
| probability | False | integer | True | None | None | None |
| heat_fatigue | False | integer | True | None | None | None |
| cold_fatigue | False | integer | True | None | None | None |
| spotting_scalar | False | double | True | None | None | None |
  
## battle_difficulty_modifiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| difficulty_level | True | text | True | 255 | None | None |
| human | True | yesno | True | None | None | None |
| stat | True | text | True | 255 | None | None |
| value | False | text | False | 255 | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
  
## battle_entities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| type | False | text | False | 50 | [battle_entities_types_enum_tables](#battle_entities_types_enum_tables) | key |
| walk_speed | False | single | True | None | None | None |
| run_speed | False | single | True | None | None | None |
| acceleration | False | single | True | None | None | None |
| deceleration | False | single | True | None | None | None |
| charge_speed | False | single | True | None | None | None |
| crawl_speed | False | single | True | None | None | None |
| charge_distance_commence_run | False | single | True | None | None | None |
| charge_distance_adopt_charge_pose | False | single | True | None | None | None |
| charge_distance_pick_target | False | single | True | None | None | None |
| radius | False | single | True | None | None | None |
| shape | False | text | True | 50 | [battle_entities_shape_enum_tables](#battle_entities_shape_enum_tables) | key |
| radii_ratio | False | single | True | None | None | None |
| mass | False | single | True | None | None | None |
| height | False | single | True | None | None | None |
| fire_arc_close | False | integer | False | None | None | None |
| fire_arc_loose | False | integer | False | None | None | None |
| turn_speed | False | integer | False | None | None | None |
| hit_points | False | integer | True | None | None | None |
| allow_turn_to_move_anim | False | yesno | True | None | None | None |
| allow_static_turn_anim | False | yesno | True | None | None | None |
| tracking_threshold | False | single | True | None | None | None |
| min_turning_speed | False | single | True | None | None | None |
| display_model_offset_z | False | single | True | None | None | None |
  
## battle_entities_class_validation_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## battle_entities_shape_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## battle_entities_types_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## battle_entity_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name | True | text | True | 255 | None | None |
| forest | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| grass | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| mud | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| sand | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| scrub | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| rock | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| deep_water | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| shallow_water | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| road | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| wooden_floor | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| snow | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
  
## battle_misc_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name | True | text | True | 255 | None | None |
| effect | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
  
## battle_personalities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| soldier_model | False | text | True | 50 | [warscape_animated_tables](#warscape_animated_tables) | key |
| man_animations_table | False | text | True | 50 | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| type | False | text | False | 50 | [battle_personality_types_enum_tables](#battle_personality_types_enum_tables) | key |
| missile_type | False | text | False | 255 | [projectiles_tables](#projectiles_tables) | key |
| variant | False | text | True | 255 | [variants_tables](#variants_tables) | variant_name |
  
## battle_personality_types_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## battle_sequences_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle | True | text | False | 255 | [battles_tables](#battles_tables) | key |
| unlock_order | False | integer | False | None | None | None |
  
## battle_siege_vehicle_permissions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| vehicle | True | text | True | 255 | [battlefield_siege_vehicles_tables](#battlefield_siege_vehicles_tables) | key |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## battle_skeletons_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name | True | text | True | 255 | None | None |
| category | False | text | True | 255 | [battle_skeleton_category_enums_tables](#battle_skeleton_category_enums_tables) | type |
| root | False | text | True | 255 | None | None |
| scale | False | single | True | None | None | None |
| scale_deviation | False | single | True | None | None | None |
| hips_node | False | text | False | 255 | None | None |
| spine_node | False | text | False | 255 | None | None |
| weapon1_node | False | text | False | 255 | None | None |
| weapon2_node | False | text | False | 255 | None | None |
| weapon3_node | False | text | False | 255 | None | None |
| weapon4_node | False | text | False | 255 | None | None |
| weapon5_node | False | text | False | 255 | None | None |
| head_node | False | text | False | 255 | None | None |
| neck_node | False | text | False | 255 | None | None |
| leftshoulder_node | False | text | False | 255 | None | None |
| rightshoulder_node | False | text | False | 255 | None | None |
| leftarm_node | False | text | False | 255 | None | None |
| rightarm_node | False | text | False | 255 | None | None |
| lefthand_node | False | text | False | 255 | None | None |
| righthand_node | False | text | False | 255 | None | None |
| leftupleg_node | False | text | False | 255 | None | None |
| rightupleg_node | False | text | False | 255 | None | None |
| leftleg_node | False | text | False | 255 | None | None |
| rightleg_node | False | text | False | 255 | None | None |
| leftfoot_node | False | text | False | 255 | None | None |
| rightfoot_node | False | text | False | 255 | None | None |
| leftfinger_node | False | text | False | 255 | None | None |
| rightfinger_node | False | text | False | 255 | None | None |
| lefttoe_node | False | text | False | 255 | None | None |
| righttoe_node | False | text | False | 255 | None | None |
| leftwheel_node | False | text | False | 255 | None | None |
| rightwheel_node | False | text | False | 255 | None | None |
  
## battle_skeleton_category_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 255 | None | None |
  
## battle_sky_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 100 | None | None |
| season | False | text | True | 50 | [seasons_tables](#seasons_tables) | season |
| weather_type | False | text | True | 50 | [battle_weather_types_tables](#battle_weather_types_tables) | key |
| time_of_day | False | text | True | 50 | None | None |
| climate | False | text | False | 50 | [climates_tables](#climates_tables) | climate_type |
| sky_file | False | text | True | 50 | None | None |
| supports_ambient_fog | False | yesno | True | None | None | None |
| supports_volumetric_fog | False | yesno | True | None | None | None |
  
## battle_terrain_farms_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| farm | True | text | True | 50 | None | None |
| tile_model | False | text | True | 150 | None | None |
| colour_map_model | False | text | True | 150 | None | None |
| blend_map_model | False | text | True | 150 | None | None |
| grass_map_model | False | text | True | 150 | None | None |
| alternate_colour_map_model | False | text | True | 150 | None | None |
| alternate_blend_map_model | False | text | True | 150 | None | None |
| alternate_grass_map_model | False | text | True | 150 | None | None |
| road_colour_map_model | False | text | True | 150 | None | None |
| road_blend_map_model | False | text | True | 150 | None | None |
| road_grass_map_model | False | text | True | 150 | None | None |
| tile_map | False | text | False | 100 | None | None |
| wall_texture | False | text | True | 50 | None | None |
| wall_end | False | text | True | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| wall_cross_section | False | text | True | 50 | None | None |
  
## battle_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 255 | None | None |
| onscreen | False | text | False | 255 | None | None |
| sort_order | False | integer | True | None | None | None |
| defender_funds_ratio | False | double | True | None | None | None |
| max_teamsize | False | integer | True | None | None | None |
  
## battle_types_to_victory_conditions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle_type | True | text | True | 255 | [battle_types_tables](#battle_types_tables) | type |
| attacker_victory_condition | True | text | False | 20000 | [victory_conditions_tables](#victory_conditions_tables) | condition |
| defender_victory_condition | True | text | False | 20000 | [victory_conditions_tables](#victory_conditions_tables) | condition |
  
## battle_type_faction_presets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| weighting_type | True | integer | True | None | [battle_type_setup_limits_tables](#battle_type_setup_limits_tables) | id |
| id | False | autonumber | False | None | None | None |
  
## battle_type_setup_limits_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle_type | True | text | True | 255 | [battle_types_tables](#battle_types_tables) | type |
| weighting_type | True | text | True | 255 | None | None |
| army_size | True | text | False | 255 | None | None |
| era | True | text | False | 255 | None | None |
| max_infantry | False | integer | True | None | None | None |
| max_cavalry | False | integer | True | None | None | None |
| max_artillery | False | integer | True | None | None | None |
| max_small_ship | False | integer | True | None | None | None |
| max_frigate | False | integer | True | None | None | None |
| max_line_of_battle | False | integer | True | None | None | None |
| id | False | autonumber | True | None | None | None |
  
## battle_unit_permission_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| battle_type | True | text | True | 255 | [battle_types_tables](#battle_types_tables) | type |
  
## battle_weather_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| weather_type | True | text | True | 50 | [battle_weather_types_tables](#battle_weather_types_tables) | key |
| stat | True | text | True | 255 | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| value | False | integer | True | None | None | None |
  
## battle_weather_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| level | False | integer | True | None | None | None |
| precipitation_type | False | text | True | 50 | None | None |
| num_particles | False | integer | True | None | None | None |
| particle_size | False | single | True | None | None | None |
| particle_speed | False | single | True | None | None | None |
| onscreen | False | text | False | 255 | None | None |
| list_order | False | integer | False | None | None | None |
| naval_appropriate | False | yesno | False | None | None | None |
  
## building_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 255 | None | None |
  
## building_chains_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| tech_category_tab | False | text | False | 255 | None | None |
| tech_category_position | False | integer | False | None | None | None |
| chain_category | False | text | False | 50 | None | None |
| chain_tooltip | False | text | True | 536870910 | None | None |
| in_encyclopedia | False | yesno | True | None | None | None |
| building_superchain | False | text | False | 255 | [building_superchains_tables](#building_superchains_tables) | key |
| encyclopedia_description | False | text | True | 65535 | None | None |
| encyclopedia_group | False | text | False | 255 | [encyclopedia_building_chain_groups_tables](#encyclopedia_building_chain_groups_tables) | group_name |
| encyclopedia_include_in_index | False | yesno | True | None | None | None |
| encyclopedia_name | False | text | True | 255 | None | None |
  
## building_chain_availabilities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| set_id | False | text | True | 255 | [building_chain_availability_set_ids_tables](#building_chain_availability_set_ids_tables) | id |
| culture | False | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| sub_culture | False | text | False | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| faction | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| campaign | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## building_chain_availability_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | [building_chain_availability_set_ids_tables](#building_chain_availability_set_ids_tables) | id |
| building_chain | True | text | True | 255 | [building_chains_tables](#building_chains_tables) | key |
  
## building_chain_availability_set_ids_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
  
## building_chain_to_slots_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| chain | True | text | True | 50 | [building_chains_tables](#building_chains_tables) | key |
| slot | True | text | True | 50 | [slots_tables](#slots_tables) | slot |
  
## building_culture_gov_type_variants_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| government_type | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| name | False | text | True | 50 | None | None |
| artpiece | False | text | False | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| artpiece_animated | False | text | False | 50 | [warscape_animated_tables](#warscape_animated_tables) | key |
| description | False | text | True | 50 | [building_description_texts_tables](#building_description_texts_tables) | key |
| icon | False | text | True | 50 | None | None |
| short_description | False | text | True | 255 | [building_short_description_texts_tables](#building_short_description_texts_tables) | key |
  
## building_culture_variants_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| name | False | text | True | 50 | None | None |
| battlefield_building | False | text | False | 50 | [battlefield_buildings_tables](#battlefield_buildings_tables) | key |
| artpiece | False | text | False | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| artpiece_animated | False | text | False | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
| description | False | text | False | 50 | [building_description_texts_tables](#building_description_texts_tables) | key |
| icon | False | text | True | 50 | None | None |
| subculture | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| disables | False | yesno | True | None | None | None |
| short_description | False | text | False | 255 | [building_short_description_texts_tables](#building_short_description_texts_tables) | key |
| flavour | False | text | False | 255 | [building_flavour_texts_tables](#building_flavour_texts_tables) | key |
| display_tooltip | False | yesno | True | None | None | None |
  
## building_description_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| long_description | False | text | False | 536870910 | None | None |
  
## building_effects_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | double | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| value_damaged | False | double | True | None | None | None |
| value_ruined | False | double | True | None | None | None |
  
## building_factionwide_effects_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| effect_value | False | integer | True | None | None | None |
  
## building_faction_variants_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| onscreen_name | False | text | True | 255 | None | None |
| artpiece | False | text | True | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| description | False | text | True | 50 | [building_description_texts_tables](#building_description_texts_tables) | key |
| icon | False | text | True | 50 | None | None |
| short_description | False | text | True | 255 | [building_short_description_texts_tables](#building_short_description_texts_tables) | key |
  
## building_flavour_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| flavour | False | text | True | 255 | None | None |
  
## building_instances_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| num_instances | False | integer | True | None | None | None |
  
## building_levels_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| level_name | True | text | True | 50 | None | None |
| chain | False | text | True | 50 | [building_chains_tables](#building_chains_tables) | key |
| level | False | integer | True | None | None | None |
| condition | False | text | False | 536870910 | None | None |
| only_in_capital | False | yesno | False | None | None | None |
| create_time | False | integer | True | None | None | None |
| create_cost | False | integer | True | None | None | None |
| upkeep_cost | False | integer | True | None | None | None |
| demolition_cost | False | integer | True | None | None | None |
| zoc | False | double | True | None | None | None |
| lower_happiness | False | integer | True | None | None | None |
| upper_happiness | False | integer | True | None | None | None |
| repression | False | integer | True | None | None | None |
| gdp | False | integer | True | None | None | None |
| town_wealth_growth | False | integer | True | None | None | None |
| pop_change | False | double | True | None | None | None |
| maxpop_change | False | double | True | None | None | None |
| commodity | False | text | False | 50 | [commodities_tables](#commodities_tables) | key |
| commodity_vol | False | integer | True | None | None | None |
| building_category | False | text | False | 255 | [building_categories_tables](#building_categories_tables) | key |
| gov_type_key | False | text | False | 50 | [government_types_tables](#government_types_tables) | government_type |
| military_prestige | False | integer | False | None | None | None |
| naval_prestige | False | integer | False | None | None | None |
| economic_prestige | False | integer | False | None | None | None |
| enlightenment_prestige | False | integer | False | None | None | None |
| destruction_terminator | False | yesno | True | None | None | None |
| faction_unique | False | yesno | True | None | None | None |
| religion_requirement | False | text | False | 1024 | [religions_tables](#religions_tables) | religion_key |
| first_in_world_bundle | False | text | False | 1024 | [effect_bundles_tables](#effect_bundles_tables) | key |
| resource_requirement | False | text | False | 1024 | [resources_tables](#resources_tables) | key |
| working_model | False | text | True | 1024 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| unique_index | False | autonumber | True | None | None | None |
| can_convert | False | yesno | True | None | None | None |
| building_instance_key | False | text | False | 255 | [building_instances_tables](#building_instances_tables) | key |
| audio_building_type | False | text | True | 255 | [audio_campaign_building_enums_tables](#audio_campaign_building_enums_tables) | key |
| should_show_building_level_in_ui_for_technology | False | yesno | True | None | None | None |
| is_new | False | yesno | True | None | None | None |
  
## building_level_armed_citizenry_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| building_level | False | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| unit_group | False | text | True | 255 | [armed_citizenry_unit_groups_tables](#armed_citizenry_unit_groups_tables) | unit_group |
  
## building_level_required_technology_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building_level_key | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| technology_key | True | text | True | 255 | [technologies_tables](#technologies_tables) | key |
  
## building_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## building_set_to_building_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building_set | True | text | True | 255 | [building_sets_tables](#building_sets_tables) | key |
| building_level | True | text | False | 255 | [building_levels_tables](#building_levels_tables) | level_name |
| building_chain | True | text | False | 255 | [building_chains_tables](#building_chains_tables) | key |
| exclude | False | yesno | True | None | None | None |
  
## building_short_description_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| short_description | False | text | True | 255 | None | None |
  
## building_states_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## building_superchains_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| max_instances_per_region | False | integer | True | None | None | None |
  
## building_to_unit_abilities_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building_name | True | text | True | 50 | [battlefield_buildings_tables](#battlefield_buildings_tables) | key |
| ability | True | text | True | 50 | [unit_abilities_tables](#unit_abilities_tables) | key |
  
## building_units_allowed_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building | False | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| unit | False | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| XP | False | integer | True | None | None | None |
| conditions | False | text | False | 536870910 | None | None |
| key | True | autonumber | True | None | None | None |
| faction | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| enabled | False | yesno | False | None | None | None |
  
## building_upgrades_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| from | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| to | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
  
## cai_agent_distribution_profiles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_agent_distribution_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_agent_record_to_cai_agent_type_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent_type_key | True | text | True | 255 | [cai_agent_types_tables](#cai_agent_types_tables) | key |
| agent_record_key | True | text | True | 255 | [agents_tables](#agents_tables) | key |
  
## cai_agent_recruitment_profiles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_agent_recruitment_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_agent_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_agent_type_distribution_profile_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| distribution_profile_key | True | text | True | 255 | [cai_agent_distribution_profiles_tables](#cai_agent_distribution_profiles_tables) | key |
| agent_type_key | True | text | True | 255 | [cai_agent_types_tables](#cai_agent_types_tables) | key |
| distribution_type_key | True | text | True | 255 | [cai_agent_distribution_types_tables](#cai_agent_distribution_types_tables) | key |
  
## cai_agent_type_recruitment_profile_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| recruitment_profile_key | True | text | True | 255 | [cai_agent_recruitment_profiles_tables](#cai_agent_recruitment_profiles_tables) | key |
| agent_type_key | True | text | True | 255 | [cai_agent_types_tables](#cai_agent_types_tables) | key |
| recruitment_type_key | True | text | True | 255 | [cai_agent_recruitment_types_tables](#cai_agent_recruitment_types_tables) | key |
  
## cai_base_building_context_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building_key | True | text | True | 1024 | [building_levels_tables](#building_levels_tables) | level_name |
| economic_value | False | double | True | None | None | None |
| military_value | False | double | True | None | None | None |
| happiness_value | False | double | True | None | None | None |
| prestige_value | False | double | True | None | None | None |
| education_value | False | double | True | None | None | None |
| existing_buildings_apply_discount_over_limit | False | double | True | None | None | None |
| existing_buildings_discount_per_building | False | double | True | None | None | None |
| existing_buildings_maximum_discount | False | double | True | None | None | None |
  
## cai_construction_system_building_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign | True | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| sub_culture | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| culture | True | text | False | 255 | [cultures_tables](#cultures_tables) | key |
| building_or_building_range_start_inclusive | True | text | False | 255 | [building_levels_tables](#building_levels_tables) | level_name |
| building_range_end_inclusive | True | text | False | 255 | [building_levels_tables](#building_levels_tables) | level_name |
| building_instance | True | text | False | 255 | [building_instances_tables](#building_instances_tables) | key |
| building_chain | True | text | False | 255 | [building_chains_tables](#building_chains_tables) | key |
| building_super_chain | True | text | False | 255 | [building_superchains_tables](#building_superchains_tables) | key |
| cai_construction_system_category | True | text | False | 255 | [cai_construction_system_categories_tables](#cai_construction_system_categories_tables) | key |
| cai_construction_system_category_group | True | text | False | 255 | [cai_construction_system_category_groups_tables](#cai_construction_system_category_groups_tables) | key |
| score_or_score_start_inclusive | False | integer | True | None | None | None |
| score_end_inclusive | False | integer | True | None | None | None |
| per_province_building_limit_start | False | integer | True | None | None | None |
| per_province_building_minimum_discount_when_exceeding_limit_start | False | integer | True | None | None | None |
| per_province_building_maximum_discount_when_exceeding_limit_start | False | integer | True | None | None | None |
| per_province_per_building_discount_increment_when_exceeding_limit_start | False | integer | True | None | None | None |
| per_province_building_limit_end | False | integer | True | None | None | None |
| per_province_building_minimum_discount_when_exceeding_limit_end | False | integer | True | None | None | None |
| per_province_building_maximum_discount_when_exceeding_limit_end | False | integer | True | None | None | None |
| per_province_per_building_discount_increment_when_exceeding_limit_end | False | integer | True | None | None | None |
| per_faction_building_limit_start | False | integer | True | None | None | None |
| per_faction_building_minimum_discount_when_exceeding_limit_start | False | integer | True | None | None | None |
| per_faction_building_maximum_discount_when_exceeding_limit_start | False | integer | True | None | None | None |
| per_faction_per_building_discount_increment_when_exceeding_limit_start | False | integer | True | None | None | None |
| per_faction_building_limit_end | False | integer | True | None | None | None |
| per_faction_building_minimum_discount_when_exceeding_limit_end | False | integer | True | None | None | None |
| per_faction_building_maximum_discount_when_exceeding_limit_end | False | integer | True | None | None | None |
| per_faction_per_building_discount_increment_when_exceeding_limit_end | False | integer | True | None | None | None |
  
## cai_construction_system_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| cai_construction_system_category_group | False | text | True | 255 | [cai_construction_system_category_groups_tables](#cai_construction_system_category_groups_tables) | key |
| cdir_military_generator_unit_group | False | text | False | 255 | [cdir_military_generator_unit_groups_tables](#cdir_military_generator_unit_groups_tables) | key |
  
## cai_construction_system_category_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_construction_system_province_template_assignment_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| capital_province_template | False | text | True | 255 | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| military_province_template | False | text | True | 255 | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| economic_province_template | False | text | True | 255 | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| military_port_province_template | False | text | True | 255 | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| economic_port_province_template | False | text | True | 255 | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| non_port_province_military_ideal_percentage | False | integer | True | None | None | None |
| port_province_military_ideal_percentage | False | integer | True | None | None | None |
  
## cai_construction_system_strategic_context_template_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| default_cai_construction_system_template | False | text | True | 255 | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
  
## cai_construction_system_strategic_context_template_policy_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| cai_construction_system_strategic_context_policy | True | text | True | 255 | [cai_construction_system_strategic_context_template_policies_tables](#cai_construction_system_strategic_context_template_policies_tables) | key |
| cai_strategic_context | True | text | True | 255 | [cai_strategic_context_types_tables](#cai_strategic_context_types_tables) | key |
| cai_construction_system_template | True | text | True | 255 | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
  
## cai_construction_system_superchain_hints_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| super_chain_key | True | text | True | 255 | [building_superchains_tables](#building_superchains_tables) | key |
| military_specialisation_recommended | False | yesno | True | None | None | None |
| economic_specialisation_recommended | False | yesno | True | None | None | None |
  
## cai_construction_system_synergies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| synergy_policy_key | True | text | True | 2000 | [cai_construction_system_synergy_policies_tables](#cai_construction_system_synergy_policies_tables) | key |
| existing_building_chain_key | True | text | False | 50 | [building_chains_tables](#building_chains_tables) | key |
| existing_building_level_inclusive_start | True | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| existing_building_level_inclusive_end | True | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| potential_buiding_chain_key | True | text | False | 50 | [building_chains_tables](#building_chains_tables) | key |
| potential_building_level_inclusive_start | True | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| potential_building_level_inclusive_end | True | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| synergy_level_key | False | text | True | 2000 | [cai_construction_system_synergy_levels_tables](#cai_construction_system_synergy_levels_tables) | key |
| existing_building_instance | True | text | False | 255 | [building_instances_tables](#building_instances_tables) | key |
| existing_building_super_chain | True | text | True | 255 | [building_superchains_tables](#building_superchains_tables) | key |
| potential_building_instance | True | text | False | 255 | [building_instances_tables](#building_instances_tables) | key |
| potential_building_super_chain | True | text | True | 255 | [building_superchains_tables](#building_superchains_tables) | key |
  
## cai_construction_system_synergy_levels_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 2000 | None | None |
| relative_effect | False | single | True | None | None | None |
| absolute_effect | False | single | True | None | None | None |
| priority | False | integer | True | None | None | None |
  
## cai_construction_system_synergy_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 2000 | None | None |
  
## cai_construction_system_templates_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| default_category_and_group_value | False | double | True | None | None | None |
  
## cai_construction_system_templates_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| cai_construction_system_template | True | text | True | 255 | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| cai_construction_system_category | True | text | False | 255 | [cai_construction_system_categories_tables](#cai_construction_system_categories_tables) | key |
| cai_construction_system_category_group | True | text | False | 255 | [cai_construction_system_category_groups_tables](#cai_construction_system_category_groups_tables) | key |
| value | False | double | True | None | None | None |
  
## cai_diplomacy_complex_treacheries_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| first_event | True | text | True | 255 | [cai_personality_diplomatic_events_tables](#cai_personality_diplomatic_events_tables) | id |
| second_event | True | text | True | 255 | [cai_personality_diplomatic_events_tables](#cai_personality_diplomatic_events_tables) | id |
| max_turn_difference | False | integer | True | None | None | None |
| value | False | single | True | None | None | None |
  
## cai_diplomacy_simple_treacheries_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| event | True | text | True | 255 | [cai_personality_diplomatic_events_tables](#cai_personality_diplomatic_events_tables) | id |
| value | False | single | True | None | None | None |
  
## cai_military_aggressiveness_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_military_behaviour_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_personalities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| budget_policy_key | False | text | True | 255 | [cai_personalities_budget_policies_tables](#cai_personalities_budget_policies_tables) | key |
| technology_manager_key | False | text | True | 255 | [campaign_ai_technology_managers_tables](#campaign_ai_technology_managers_tables) | key |
| character_skill_tree_manager_key | False | text | True | 255 | [campaign_ai_character_skill_tree_managers_tables](#campaign_ai_character_skill_tree_managers_tables) | key |
| agent_distribution_profile_key | False | text | True | 255 | [cai_agent_distribution_profiles_tables](#cai_agent_distribution_profiles_tables) | key |
| agent_recruitment_profile_key | False | text | True | 255 | [cai_agent_recruitment_profiles_tables](#cai_agent_recruitment_profiles_tables) | key |
| reliability_policy_key | False | text | True | 255 | [cai_personalities_reliability_policies_tables](#cai_personalities_reliability_policies_tables) | key |
| religious_conversion_policy | False | text | True | 255 | [cai_personalities_religious_conversion_policies_tables](#cai_personalities_religious_conversion_policies_tables) | key |
| military_aggressiveness_policy | False | text | True | 255 | [cai_military_aggressiveness_policies_tables](#cai_military_aggressiveness_policies_tables) | key |
| military_behaviour_policy | False | text | True | 255 | [cai_military_behaviour_policies_tables](#cai_military_behaviour_policies_tables) | key |
| allowed_for_random_selection | False | yesno | True | None | None | None |
| diplomatic_component | False | text | True | 255 | [cai_personality_diplomatic_components_tables](#cai_personality_diplomatic_components_tables) | id |
| strategic_component | False | text | True | 255 | [cai_personality_strategic_components_tables](#cai_personality_strategic_components_tables) | id |
| cultural_component | False | text | True | 255 | [cai_personality_cultural_components_tables](#cai_personality_cultural_components_tables) | id |
| deal_evaluation_component | False | text | True | 255 | [cai_personality_deal_evaluation_components_tables](#cai_personality_deal_evaluation_components_tables) | id |
| deal_generation_component | False | text | True | 255 | [cai_personality_deal_generation_components_tables](#cai_personality_deal_generation_components_tables) | id |
| construction_system_policy | False | text | True | 255 | [cai_personalities_construction_system_policies_tables](#cai_personalities_construction_system_policies_tables) | key |
| task_management_system_task_generation_profile | False | text | True | 255 | [cai_personalities_task_management_system_task_generator_profiles_tables](#cai_personalities_task_management_system_task_generator_profiles_tables) | key |
| negotiation_component | False | text | True | 255 | [cai_personality_negotiation_components_tables](#cai_personality_negotiation_components_tables) | id |
| income_allocation_policy | False | text | True | 255 | [cai_personalities_income_allocation_policies_tables](#cai_personalities_income_allocation_policies_tables) | key |
| occupation_decision_component | False | text | True | 255 | [cai_personality_occupation_decision_components_tables](#cai_personality_occupation_decision_components_tables) | id |
  
## cai_personalities_budget_allocations_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| army_funds_allocation_percentage | False | integer | True | None | None | None |
| army_turns_of_inactivity_until_cap | False | integer | True | None | None | None |
| army_funding_cap | False | integer | True | None | None | None |
| army_percentage_of_pool_to_save_on_fail | False | integer | True | None | None | None |
| navy_funds_allocation_percentage | False | integer | True | None | None | None |
| navy_turns_of_inactivity_until_cap | False | integer | True | None | None | None |
| navy_funding_cap | False | integer | True | None | None | None |
| navy_percentage_of_pool_to_save_on_fail | False | integer | True | None | None | None |
| agents_funds_allocation_percentage | False | integer | True | None | None | None |
| agents_turns_of_inactivity_until_cap | False | integer | True | None | None | None |
| agents_funding_cap | False | integer | True | None | None | None |
| agents_percentage_of_pool_to_save_on_fail | False | integer | True | None | None | None |
| construction_funds_allocation_percentage | False | integer | True | None | None | None |
| construction_turns_of_inactivity_until_cap | False | integer | True | None | None | None |
| construction_funding_cap | False | integer | True | None | None | None |
| construction_percentage_of_pool_to_save_on_fail | False | integer | True | None | None | None |
| diplomacy_funds_allocation_percentage | False | integer | True | None | None | None |
| diplomacy_turns_of_inactivity_until_cap | False | integer | True | None | None | None |
| diplomacy_funding_cap | False | integer | True | None | None | None |
| diplomacy_percentage_of_pool_to_save_on_fail | False | integer | True | None | None | None |
| minimum_settable_tax_level | False | text | True | 50 | [taxes_levels_tables](#taxes_levels_tables) | tax_level |
| maximum_settable_tax_level | False | text | True | 50 | [taxes_levels_tables](#taxes_levels_tables) | tax_level |
| technology_funds_allocation_percentage | False | integer | True | None | None | None |
| technology_turns_of_inactivity_until_cap | False | integer | True | None | None | None |
| technology_funding_cap | False | integer | True | None | None | None |
| technology_percentage_of_pool_to_save_on_fail | False | integer | True | None | None | None |
  
## cai_personalities_budget_allocation_policy_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| budget_policy_key | True | text | True | 255 | [cai_personalities_budget_policies_tables](#cai_personalities_budget_policies_tables) | key |
| budget_context_key | True | text | True | 255 | [cai_strategic_context_types_tables](#cai_strategic_context_types_tables) | key |
| budget_allocation_key | True | text | True | 255 | [cai_personalities_budget_allocations_tables](#cai_personalities_budget_allocations_tables) | key |
| priority | False | integer | True | None | None | None |
  
## cai_personalities_budget_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| default_budget_allocation_key | False | text | True | 255 | [cai_personalities_budget_allocations_tables](#cai_personalities_budget_allocations_tables) | key |
  
## cai_personalities_construction_preference_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_personalities_construction_preference_policy_building_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| policy_key | True | text | True | 255 | [cai_personalities_construction_preference_policies_tables](#cai_personalities_construction_preference_policies_tables) | key |
| building_key | True | text | True | 255 | [building_levels_tables](#building_levels_tables) | level_name |
| bias_level | False | single | True | None | None | None |
| absolute_adjustment | False | single | True | None | None | None |
| building_discount_limit_adjustment | False | integer | True | None | None | None |
  
## cai_personalities_construction_system_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| strategic_context_template_assignment_policy | False | text | True | 255 | [cai_construction_system_strategic_context_template_policies_tables](#cai_construction_system_strategic_context_template_policies_tables) | key |
| province_specialisation_template_assignment_policy | False | text | True | 255 | [cai_construction_system_province_template_assignment_policies_tables](#cai_construction_system_province_template_assignment_policies_tables) | key |
| building_synergies_policy | False | text | True | 2000 | [cai_construction_system_synergy_policies_tables](#cai_construction_system_synergy_policies_tables) | key |
  
## cai_personalities_faction_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction_key | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| campaign_key | True | text | True | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| default_personality | False | text | True | 255 | [cai_personalities_tables](#cai_personalities_tables) | key |
| personality_group | False | text | True | 2000 | [cai_personalities_random_groups_tables](#cai_personalities_random_groups_tables) | random_personality_group_key |
| randomisation_policy_key | False | text | True | 2000 | [cai_personalities_randomisation_policies_tables](#cai_personalities_randomisation_policies_tables) | randomisation_policy_key |
  
## cai_personalities_income_allocation_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| default_proportion_of_net_income_to_spend | False | double | True | None | None | None |
| default_zero_or_negative_net_income_survival_rounds | False | integer | True | None | None | None |
| default_positive_net_income_survival_rounds | False | integer | True | None | None | None |
  
## cai_personalities_income_allocation_policy_strategic_context_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| income_allocation_policy_key | True | text | True | 255 | [cai_personalities_income_allocation_policies_tables](#cai_personalities_income_allocation_policies_tables) | key |
| strategic_context_key | True | text | True | 255 | [cai_strategic_context_types_tables](#cai_strategic_context_types_tables) | key |
| proportion_of_net_income_to_spend | False | double | True | None | None | None |
| zero_or_negative_net_income_survival_rounds | False | integer | True | None | None | None |
| positive_net_income_survival_rounds | False | integer | True | None | None | None |
  
## cai_personalities_randomisation_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| randomisation_policy_key | True | text | True | 2000 | None | None |
  
## cai_personalities_random_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| random_personality_group_key | True | text | True | 2000 | None | None |
  
## cai_personalities_random_group_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| random_personality_group_key | True | text | True | 2000 | [cai_personalities_random_groups_tables](#cai_personalities_random_groups_tables) | random_personality_group_key |
| personality_key | True | text | True | 255 | [cai_personalities_tables](#cai_personalities_tables) | key |
  
## cai_personalities_reliability_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| join_ally_bias | False | single | True | None | None | None |
  
## cai_personalities_religious_conversion_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_personalities_task_management_system_task_generator_profiles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| default_generator_group_when_owning_regions | False | text | True | 255 | [cai_task_management_system_task_generator_groups_tables](#cai_task_management_system_task_generator_groups_tables) | key |
| default_generator_group_when_no_owned_regions | False | text | True | 255 | [cai_task_management_system_task_generator_groups_tables](#cai_task_management_system_task_generator_groups_tables) | key |
  
## cai_personalities_tms_task_generator_profiles_strategic_contexts_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| task_generator_profile_key | True | text | True | 255 | [cai_personalities_task_management_system_task_generator_profiles_tables](#cai_personalities_task_management_system_task_generator_profiles_tables) | key |
| strategic_context_key | True | text | True | 255 | [cai_strategic_context_types_tables](#cai_strategic_context_types_tables) | key |
| for_use_when_the_faction_has_regions | True | yesno | True | None | None | None |
| generator_group_key | False | text | True | 255 | [cai_task_management_system_task_generator_groups_tables](#cai_task_management_system_task_generator_groups_tables) | key |
  
## cai_personality_cultural_components_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
  
## cai_personality_cultural_multipliers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_id | True | text | True | 255 | [cai_personality_cultural_components_tables](#cai_personality_cultural_components_tables) | id |
| source | True | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
| target | True | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
| positive_attitude_multiplier | False | single | True | None | None | None |
| negative_attitude_multiplier | False | single | True | None | None | None |
| attitude_base | False | single | True | None | None | None |
  
## cai_personality_deal_evaluation_components_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| max_payment_value | False | single | True | None | None | None |
| payment_treachery_value | False | single | True | None | None | None |
| payment_offered_multiplier | False | single | True | None | None | None |
| payment_requested_multiplier | False | single | True | None | None | None |
  
## cai_personality_deal_evaluation_component_overrides_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component | True | text | True | 255 | [cai_personality_deal_evaluation_components_tables](#cai_personality_deal_evaluation_components_tables) | id |
| parent | False | text | True | 255 | [cai_personality_deal_evaluation_components_tables](#cai_personality_deal_evaluation_components_tables) | id |
  
## cai_personality_deal_evaluation_deal_component_names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
  
## cai_personality_deal_evaluation_deal_component_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| personality_component | True | text | True | 255 | [cai_personality_deal_evaluation_components_tables](#cai_personality_deal_evaluation_components_tables) | id |
| deal_component | True | text | True | 255 | [cai_personality_deal_evaluation_deal_component_names_tables](#cai_personality_deal_evaluation_deal_component_names_tables) | id |
| best_friends_value | False | single | True | None | None | None |
| very_friendly_value | False | single | True | None | None | None |
| friendly_value | False | single | True | None | None | None |
| neutral_value | False | single | True | None | None | None |
| unfriendly_value | False | single | True | None | None | None |
| very_unfriendly_value | False | single | True | None | None | None |
| bitter_enemies_value | False | single | True | None | None | None |
| last_stand_balance_factor | False | single | True | None | None | None |
| total_war_balance_factor | False | single | True | None | None | None |
| war_balance_factor | False | single | True | None | None | None |
| tension_balance_factor | False | single | True | None | None | None |
| peace_balance_factor | False | single | True | None | None | None |
| treachery_value | False | single | True | None | None | None |
  
## cai_personality_deal_generation_components_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
  
## cai_personality_deal_generation_generators_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
  
## cai_personality_deal_generation_generator_priorities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_key | True | text | True | 255 | [cai_personality_deal_generation_components_tables](#cai_personality_deal_generation_components_tables) | id |
| generator_key | True | text | True | 255 | [cai_personality_deal_generation_generators_tables](#cai_personality_deal_generation_generators_tables) | id |
| last_stand_priority | False | single | True | None | None | None |
| total_war_priority | False | single | True | None | None | None |
| war_priority | False | single | True | None | None | None |
| tension_priority | False | single | True | None | None | None |
| peace_priority | False | single | True | None | None | None |
| param1 | False | single | True | None | None | None |
| param2 | False | single | True | None | None | None |
| param3 | False | single | True | None | None | None |
| param4 | False | single | True | None | None | None |
| failure_timeout | False | integer | True | None | None | None |
| min_payment_cap | False | integer | True | None | None | None |
| max_payment_cap | False | integer | True | None | None | None |
| max_payment_pct | False | single | True | None | None | None |
  
## cai_personality_diplomatic_components_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
  
## cai_personality_diplomatic_component_overrides_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component | True | text | True | 255 | [cai_personality_diplomatic_components_tables](#cai_personality_diplomatic_components_tables) | id |
| parent | False | text | True | 255 | [cai_personality_diplomatic_components_tables](#cai_personality_diplomatic_components_tables) | id |
  
## cai_personality_diplomatic_events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| diplomatic_factor_group_active | False | text | False | 255 | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| diplomatic_factor_group_inactive | False | text | False | 255 | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
  
## cai_personality_diplomatic_event_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_id | True | text | True | 255 | [cai_personality_diplomatic_components_tables](#cai_personality_diplomatic_components_tables) | id |
| event_id | True | text | True | 255 | [cai_personality_diplomatic_events_tables](#cai_personality_diplomatic_events_tables) | id |
| value | False | single | True | None | None | None |
| falloff | False | integer | True | None | None | None |
  
## cai_personality_diplomatic_treaty_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_id | True | text | True | 255 | [cai_personality_diplomatic_components_tables](#cai_personality_diplomatic_components_tables) | id |
| defensive_alliance | False | single | False | None | None | None |
| trade_agreement | False | single | False | None | None | None |
| military_alliance | False | single | True | None | None | None |
| non_aggression_pact | False | single | True | None | None | None |
| vassalage_master | False | single | True | None | None | None |
| vassalage_vassal | False | single | True | None | None | None |
| client_state_protector | False | single | True | None | None | None |
| client_state_client | False | single | True | None | None | None |
| war | False | single | True | None | None | None |
| military_access | False | single | True | None | None | None |
  
## cai_personality_negotiation_components_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| initial_decline | False | integer | True | None | None | None |
| initial_counter | False | integer | True | None | None | None |
| irrelevant_decline | False | integer | True | None | None | None |
| irrelevant_accept | False | integer | True | None | None | None |
| irrelevant_counter_new | False | integer | True | None | None | None |
| irrelevant_counter_last | False | integer | True | None | None | None |
| angry_reject_min | False | integer | True | None | None | None |
| angry_reject_max | False | integer | True | None | None | None |
| no_payment_chance | False | integer | True | None | None | None |
| max_steps_above_acceptable | False | integer | True | None | None | None |
| no_offer_chance | False | integer | True | None | None | None |
| num_goals_generated | False | integer | True | None | None | None |
| max_interactions | False | integer | True | None | None | None |
  
## cai_personality_occupation_decision_components_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| food_shortage_cap | False | integer | True | None | None | None |
| food_excess_cap | False | integer | True | None | None | None |
| squalor_cap | False | integer | True | None | None | None |
| min_attitude | False | integer | True | None | None | None |
  
## cai_personality_occupation_decision_priorities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_id | True | text | True | 255 | [cai_personality_occupation_decision_components_tables](#cai_personality_occupation_decision_components_tables) | id |
| option | True | text | True | 255 | None | None |
| last_stand_priority | False | single | True | None | None | None |
| total_war_priority | False | single | True | None | None | None |
| war_priority | False | single | True | None | None | None |
| tension_priority | False | single | True | None | None | None |
| peace_priority | False | single | True | None | None | None |
  
## cai_personality_strategic_components_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| max_friendly_attitude | False | single | True | None | None | None |
| friendly_towards_friend_multiplier | False | single | True | None | None | None |
| hostile_towards_friend_multiplier | False | single | True | None | None | None |
| max_hostile_attitude | False | single | True | None | None | None |
| friendly_towards_enemy_multiplier | False | single | True | None | None | None |
| hostile_towards_enemy_multiplier | False | single | True | None | None | None |
| unknown_faction_multiplier | False | single | True | None | None | None |
| max_merc_proportion | False | single | True | None | None | None |
| min_merc_cap | False | integer | True | None | None | None |
| enemy_strength_modifier | False | single | True | None | None | None |
| enemy_threat_strength_modifier | False | single | True | None | None | None |
| min_retreat_ratio | False | single | True | None | None | None |
| min_retreat_to_settlement_ratio | False | single | True | None | None | None |
| strategic_balance_opportunism_factor | False | single | True | None | None | None |
| fortified_settlement_assault_strength_modifier | False | single | True | None | None | None |
| fortified_settlement_defend_strength_modifier | False | single | True | None | None | None |
  
## cai_personality_strategic_desired_attitudes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| strategic_component | True | text | True | 255 | [cai_personality_strategic_components_tables](#cai_personality_strategic_components_tables) | id |
| best_friends_attitude | False | single | True | None | None | None |
| very_friendly_attitude | False | single | True | None | None | None |
| friendly_attitude | False | single | True | None | None | None |
| neutral_attitude | False | single | True | None | None | None |
| unfriendly_attitude | False | single | True | None | None | None |
| very_unfriendly_attitude | False | single | True | None | None | None |
| bitter_enemies_attitude | False | single | True | None | None | None |
| best_friends_positive_factor | False | single | True | None | None | None |
| very_friendly_positive_factor | False | single | True | None | None | None |
| friendly_positive_factor | False | single | True | None | None | None |
| neutral_positive_factor | False | single | True | None | None | None |
| unfriendly_positive_factor | False | single | True | None | None | None |
| very_unfriendly_positive_factor | False | single | True | None | None | None |
| bitter_enemies_positive_factor | False | single | True | None | None | None |
| best_friends_negative_factor | False | single | True | None | None | None |
| very_friendly_negative_factor | False | single | True | None | None | None |
| friendly_negative_factor | False | single | True | None | None | None |
| neutral_negative_factor | False | single | True | None | None | None |
| unfriendly_negative_factor | False | single | True | None | None | None |
| very_unfriendly_negative_factor | False | single | True | None | None | None |
| bitter_enemies_negative_factor | False | single | True | None | None | None |
  
## cai_personality_strategic_resource_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| strategic_component | True | text | True | 255 | [cai_personality_strategic_components_tables](#cai_personality_strategic_components_tables) | id |
| resource | True | text | True | 255 | [resources_tables](#resources_tables) | key |
| trade_value | False | single | True | None | None | None |
| trade_falloff | False | single | True | None | None | None |
| ownership_value | False | single | True | None | None | None |
| ownership_falloff | False | single | True | None | None | None |
  
## cai_siege_strength_modifiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| subculture | True | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| defence_strength_modifier | False | single | True | None | None | None |
| assault_strength_modifier | False | single | True | None | None | None |
  
## cai_strategic_context_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_task_management_system_task_generators_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_task_management_system_task_generator_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_task_management_system_task_generator_groups_generators_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| task_generator_group_key | True | text | True | 255 | [cai_task_management_system_task_generator_groups_tables](#cai_task_management_system_task_generator_groups_tables) | key |
| task_generator_key | True | text | True | 255 | [cai_task_management_system_task_generators_tables](#cai_task_management_system_task_generators_tables) | key |
| priority | False | double | True | None | None | None |
  
## cai_variables_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| value | False | double | True | None | None | None |
| description | False | text | True | 536870910 | None | None |
  
## cai_variables_overides_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| cai_variable_key | True | text | True | 255 | [cai_variables_tables](#cai_variables_tables) | key |
| campaign_key | True | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| value | False | double | True | None | None | None |
| optional_difficulty_level | True | text | False | 20000 | None | None |
| optional_campaign_type | True | text | False | 20000 | None | None |
  
## campaigns_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_name | True | text | True | 50 | None | None |
| onscreen_name | False | text | True | 50 | None | None |
| description | False | text | True | 536870910 | None | None |
| map_name | False | text | True | 50 | [campaign_maps_tables](#campaign_maps_tables) | mapname |
| data_directory | False | text | True | 50 | None | None |
| is_grand | False | yesno | False | None | None | None |
| exportable | False | yesno | False | None | None | None |
| campaign_order | False | integer | False | None | None | None |
| bullet_list | False | text | False | 536870910 | None | None |
| display_location | False | text | False | 255 | None | None |
| is_tutorial | False | yesno | True | None | None | None |
| banner_image | False | text | False | 255 | None | None |
| banner_icon | False | text | False | 255 | None | None |
| available_for_mp | False | yesno | True | None | None | None |
| mp_sort_order | False | integer | True | None | None | None |
  
## campaigns_campaign_variables_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| variable_key | True | text | True | 50 | [campaign_variables_tables](#campaign_variables_tables) | variable_key |
| campaign_name | True | text | True | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| value | False | double | True | None | None | None |
| optional_difficulty_level | True | text | False | 20000 | None | None |
| optional_campaign_type | True | text | False | 20000 | None | None |
  
## campaign_ai_behaviours_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| behaviour | True | text | True | 255 | None | None |
| description | False | text | False | 255 | None | None |
  
## campaign_ai_character_skill_tree_agent_managers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_ai_character_skill_tree_distributions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_ai_character_skill_tree_distribution_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent_manager_key | True | text | True | 255 | [campaign_ai_character_skill_tree_agent_managers_tables](#campaign_ai_character_skill_tree_agent_managers_tables) | key |
| distribution_key | True | text | True | 255 | [campaign_ai_character_skill_tree_distributions_tables](#campaign_ai_character_skill_tree_distributions_tables) | key |
| priority | False | integer | True | None | None | None |
  
## campaign_ai_character_skill_tree_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent_manager_key | True | text | True | 255 | [campaign_ai_character_skill_tree_agent_managers_tables](#campaign_ai_character_skill_tree_agent_managers_tables) | key |
| skill_key | True | text | True | 255 | [character_skills_tables](#character_skills_tables) | key |
| priority | False | integer | True | None | None | None |
  
## campaign_ai_character_skill_tree_managers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_ai_character_skill_tree_manager_agent_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| manager_key | True | text | True | 255 | [campaign_ai_character_skill_tree_managers_tables](#campaign_ai_character_skill_tree_managers_tables) | key |
| agent_key | True | text | True | 255 | [character_skill_node_sets_tables](#character_skill_node_sets_tables) | key |
| agent_manager_key | False | text | True | 255 | [campaign_ai_character_skill_tree_agent_managers_tables](#campaign_ai_character_skill_tree_agent_managers_tables) | key |
  
## campaign_ai_managers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| manager | True | text | True | 255 | None | None |
| description | False | text | False | 255 | None | None |
  
## campaign_ai_manager_behaviour_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| manager | True | text | True | 255 | [campaign_ai_managers_tables](#campaign_ai_managers_tables) | manager |
| behaviour | True | text | True | 255 | [campaign_ai_behaviours_tables](#campaign_ai_behaviours_tables) | behaviour |
| priority | False | single | True | None | None | None |
  
## campaign_ai_personalities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| personality | True | text | True | 255 | None | None |
| is_default | False | yesno | True | None | None | None |
| description | False | text | False | 255 | None | None |
  
## campaign_ai_personality_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| personality | True | text | True | 255 | [campaign_ai_personalities_tables](#campaign_ai_personalities_tables) | personality |
| property | True | text | True | 255 | [campaign_ai_personality_properties_tables](#campaign_ai_personality_properties_tables) | property |
| property_value | False | single | True | None | None | None |
  
## campaign_ai_personality_properties_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| property | True | text | True | 255 | None | None |
| description | False | text | False | 255 | None | None |
  
## campaign_ai_technology_managers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_ai_technology_manager_path_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| manager_key | True | text | True | 255 | [campaign_ai_technology_managers_tables](#campaign_ai_technology_managers_tables) | key |
| path_key | True | text | True | 255 | [campaign_ai_technology_paths_tables](#campaign_ai_technology_paths_tables) | key |
| priority | False | integer | True | None | None | None |
  
## campaign_ai_technology_paths_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_ai_technology_path_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| path_key | True | text | True | 255 | [campaign_ai_technology_paths_tables](#campaign_ai_technology_paths_tables) | key |
| technology_key | True | text | True | 255 | [technologies_tables](#technologies_tables) | key |
| priority | False | integer | True | None | None | None |
  
## campaign_ambush_ground_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | [campaign_ground_types_tables](#campaign_ground_types_tables) | type |
| ambush_chance_of_success | False | double | True | None | None | None |
  
## campaign_anim_set_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name | True | text | True | 255 | None | None |
| skeleton | False | text | False | 255 | None | None |
  
## campaign_autoresolver_battle_situations_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| battle_type | False | text | False | 255 | [campaign_battle_type_enums_tables](#campaign_battle_type_enums_tables) | key |
| night_battle | False | text | False | 255 | None | None |
| stance | False | text | False | 255 | None | None |
  
## campaign_autoresolver_modifiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| class | False | text | False | 255 | [unit_class_tables](#unit_class_tables) | key |
| vs_class | False | text | False | 255 | [unit_class_tables](#unit_class_tables) | key |
| stat_variable_id | False | text | True | 255 | [campaign_autoresolver_stat_variables_tables](#campaign_autoresolver_stat_variables_tables) | id |
  
## campaign_autoresolver_mod_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
  
## campaign_autoresolver_mod_group_modifier_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| group_id | False | text | True | 255 | [campaign_autoresolver_mod_groups_tables](#campaign_autoresolver_mod_groups_tables) | id |
| modification_id | False | text | True | 255 | [campaign_autoresolver_modifiers_tables](#campaign_autoresolver_modifiers_tables) | id |
| value | False | double | True | None | None | None |
  
## campaign_autoresolver_mod_group_targets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| mechanic_target | False | text | False | 255 | None | None |
| alliance_target | False | text | False | 255 | None | None |
| player_target | False | text | False | 255 | None | None |
  
## campaign_autoresolver_situation_mod_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| situation_id | False | text | True | 255 | [campaign_autoresolver_battle_situations_tables](#campaign_autoresolver_battle_situations_tables) | id |
| group_target_id | False | text | True | 255 | [campaign_autoresolver_mod_group_targets_tables](#campaign_autoresolver_mod_group_targets_tables) | id |
| group_id | False | text | True | 255 | [campaign_autoresolver_mod_groups_tables](#campaign_autoresolver_mod_groups_tables) | id |
  
## campaign_autoresolver_stat_variables_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| description | False | text | False | 255 | None | None |
  
## campaign_battle_presets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| onscreen_name | False | text | False | 255 | None | None |
| description | False | text | False | 255 | None | None |
| coord_x | False | decimal | True | None | None | None |
| coord_y | False | decimal | True | None | None | None |
| tile_upgrade | False | text | False | 255 | None | None |
| battle_type | False | text | True | 255 | [campaign_battle_type_enums_tables](#campaign_battle_type_enums_tables) | key |
| is_unique_settlement | False | yesno | True | None | None | None |
| campaign_map | False | integer | True | None | [campaign_map_playable_areas_tables](#campaign_map_playable_areas_tables) | index |
  
## campaign_battle_type_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_bonus_value_battle_context_battle_type_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle_context_key | True | text | True | 255 | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| battle_type_key | True | text | True | 255 | [campaign_battle_type_enums_tables](#campaign_battle_type_enums_tables) | key |
  
## campaign_bonus_value_battle_context_culture_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle_context_key | True | text | True | 255 | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| culture_key | True | text | True | 255 | [cultures_tables](#cultures_tables) | key |
  
## campaign_bonus_value_battle_context_faction_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle_context_key | True | text | True | 255 | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| faction_key | True | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## campaign_bonus_value_battle_context_force_status_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_bonus_value_battle_context_force_status_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle_context_key | True | text | True | 255 | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| force_status_key | True | text | True | 255 | [campaign_bonus_value_battle_context_force_status_tables](#campaign_bonus_value_battle_context_force_status_tables) | key |
| is_yours | False | yesno | True | None | None | None |
  
## campaign_bonus_value_battle_context_ground_type_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle_context_key | True | text | True | 255 | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| ground_type_key | True | text | True | 255 | [campaign_ground_types_tables](#campaign_ground_types_tables) | type |
  
## campaign_bonus_value_battle_context_specifiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| night_battles_only | False | yesno | True | None | None | None |
  
## campaign_bonus_value_battle_context_territory_status_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_bonus_value_battle_context_territory_status_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle_context_key | True | text | True | 255 | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| territory_status_key | True | text | True | 255 | [campaign_bonus_value_battle_context_territory_status_tables](#campaign_bonus_value_battle_context_territory_status_tables) | key |
  
## campaign_bonus_value_ids_action_results_additional_outcomes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 255 | None | None |
  
## campaign_bonus_value_ids_agent_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_basic_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_battlefield_deployables_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 255 | None | None |
  
## campaign_bonus_value_ids_battle_contexts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_bonus_value_ids_building_chain_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_building_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 512 | None | None |
  
## campaign_bonus_value_ids_commodity_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_melee_weapon_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_missile_weapon_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_population_class_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_population_class_and_religion_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_projectile_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_projectile_shot_type_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_projectile_type_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_provincial_initiative_effect_records_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 255 | None | None |
  
## campaign_bonus_value_ids_religion_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_resource_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_siege_items_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 255 | None | None |
  
## campaign_bonus_value_ids_technology_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 64 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_unit_ability_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_unit_caste_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_unit_category_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_unit_class_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_unit_records_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_unit_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 512 | None | None |
  
## campaign_character_anim_status_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| status | True | text | True | 255 | None | None |
  
## campaign_character_arts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| art_set_id | True | text | True | 255 | [campaign_character_art_sets_tables](#campaign_character_art_sets_tables) | art_set_id |
| level | True | integer | True | None | None | None |
| season | True | text | True | 255 | None | None |
| age | True | integer | True | None | None | None |
| portrait | False | text | False | 255 | None | None |
| uniform | False | text | False | 255 | [agent_uniforms_tables](#agent_uniforms_tables) | uniform_name |
| card | False | text | False | 255 | None | None |
| info | False | text | False | 255 | None | None |
| sea_uniform | False | text | False | 255 | [agent_uniforms_tables](#agent_uniforms_tables) | uniform_name |
| navy_uniform | False | text | False | 255 | [agent_uniforms_tables](#agent_uniforms_tables) | uniform_name |
| land_animation | False | text | False | 255 | [campaign_anim_set_enums_tables](#campaign_anim_set_enums_tables) | name |
| sea_animation | False | text | False | 255 | [campaign_anim_set_enums_tables](#campaign_anim_set_enums_tables) | name |
| navy_animation | False | text | False | 255 | [campaign_anim_set_enums_tables](#campaign_anim_set_enums_tables) | name |
  
## campaign_character_art_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| art_set_id | True | text | True | 255 | None | None |
| is_custom | False | yesno | True | None | None | None |
| agent_type | False | text | False | 255 | [agents_tables](#agents_tables) | key |
| faction | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| culture | False | text | False | 255 | [cultures_tables](#cultures_tables) | key |
| subculture | False | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| is_male | False | yesno | True | None | None | None |
| group | False | text | False | 255 | [campaign_character_art_sets_campaign_groups_tables](#campaign_character_art_sets_campaign_groups_tables) | key |
  
## campaign_character_art_sets_campaign_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_character_art_sets_group_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| group | True | text | True | 255 | [campaign_character_art_sets_campaign_groups_tables](#campaign_character_art_sets_campaign_groups_tables) | key |
| campaign | True | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## campaign_character_art_set_campaign_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| art_set_id | False | text | True | 255 | [campaign_character_art_sets_tables](#campaign_character_art_sets_tables) | art_set_id |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## campaign_character_attribute_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent_record | True | text | True | 255 | [agents_tables](#agents_tables) | key |
| attribute_record | True | text | True | 255 | [agent_attributes_tables](#agent_attributes_tables) | key |
| attribute_level | True | integer | True | None | None | None |
| effect_record | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| effect_scope | True | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| effect_value | False | single | True | None | None | None |
| culture_record | True | text | False | 255 | [cultures_tables](#cultures_tables) | key |
| subculture_record | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| faction_record | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| campaign_record | True | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## campaign_clan_level_infos_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| clan_level | True | integer | True | None | None | None |
| optional_faction_key | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| optional_difficulty_level | True | text | False | 255 | None | None |
| modernisation_threshold | False | integer | True | None | None | None |
| technology_unlock_level | False | integer | True | None | None | None |
| effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
  
## campaign_difficulty_handicap_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_difficulty_handicap | True | integer | True | None | None | None |
| human | True | yesno | True | None | None | None |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| effect_value | False | single | True | None | None | None |
| optional_campaign_key | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## campaign_effect_scopes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| localised_text | False | text | False | 255 | None | None |
| order | False | integer | True | None | None | None |
| source | False | text | True | 255 | [campaign_effect_scope_objects_tables](#campaign_effect_scope_objects_tables) | key |
| target | False | text | True | 255 | [campaign_effect_scope_objects_tables](#campaign_effect_scope_objects_tables) | key |
| ownership | False | text | False | 255 | [campaign_effect_scope_ownerships_tables](#campaign_effect_scope_ownerships_tables) | key |
| location | False | text | False | 255 | [campaign_effect_scope_locations_tables](#campaign_effect_scope_locations_tables) | key |
  
## campaign_effect_scope_agent_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_effect_scope_key | True | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| agent_key | True | text | True | 255 | [agents_tables](#agents_tables) | key |
  
## campaign_effect_scope_character_force_relationships_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_effect_scope_character_force_relationship_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_effect_scope_key | True | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| force_relationship_key | True | text | True | 255 | [campaign_effect_scope_character_force_relationships_tables](#campaign_effect_scope_character_force_relationships_tables) | key |
  
## campaign_effect_scope_character_unit_relationships_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_effect_scope_character_unit_relationship_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_effect_scope_key | True | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| unit_relationship_key | True | text | True | 255 | [campaign_effect_scope_character_unit_relationships_tables](#campaign_effect_scope_character_unit_relationships_tables) | key |
  
## campaign_effect_scope_locations_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_effect_scope_objects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_effect_scope_ownerships_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_ground_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 50 | None | None |
| movement_cost | False | integer | True | None | None | None |
| can_ambush | False | yesno | True | None | None | None |
| onscreen_name | False | text | False | 50 | None | None |
| is_sea | False | yesno | True | None | None | None |
| icon | False | text | True | 255 | None | None |
  
## campaign_localised_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| string | False | text | True | 255 | None | None |
  
## campaign_maps_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| mapname | True | text | True | 50 | None | None |
| minx | False | integer | True | None | None | None |
| miny | False | integer | True | None | None | None |
| maxx | False | integer | True | None | None | None |
| maxy | False | integer | True | None | None | None |
  
## campaign_map_attritions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| type | False | text | True | 255 | [campaign_map_attrition_types_tables](#campaign_map_attrition_types_tables) | key |
| damage | False | text | True | 255 | [campaign_map_attrition_damages_tables](#campaign_map_attrition_damages_tables) | key |
| campaign_map_tooltip | False | text | False | 20000 | None | None |
| unit_card_tooltip | False | text | False | 20000 | None | None |
| unit_immunity_text | False | text | False | 20000 | None | None |
| message_event_association | False | text | False | 255 | [message_events_tables](#message_events_tables) | event |
  
## campaign_map_attrition_damages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| percent_unit_damage | False | integer | True | None | None | None |
  
## campaign_map_attrition_faction_immunities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| attrition | True | text | True | 255 | [campaign_map_attritions_tables](#campaign_map_attritions_tables) | key |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## campaign_map_attrition_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_map_attrition_unit_immunities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| attrition | True | text | True | 255 | [campaign_map_attritions_tables](#campaign_map_attritions_tables) | key |
| unit | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
  
## campaign_map_pieces_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ID | True | autonumber | False | None | None | None |
  
## campaign_map_playable_areas_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| mapname | False | text | True | 50 | [campaign_maps_tables](#campaign_maps_tables) | mapname |
| index | True | autonumber | True | None | None | None |
| minx | False | double | True | None | None | None |
| maxx | False | double | True | None | None | None |
| miny | False | double | True | None | None | None |
| maxy | False | double | True | None | None | None |
| sea_trade | False | yesno | True | None | None | None |
| onscreen_name | False | text | True | 536870910 | None | None |
| map_file | False | text | False | 50 | None | None |
| overlay_file | False | text | False | 50 | None | None |
| radar_file | False | text | False | 50 | None | None |
| meaningful_id | False | text | True | 50 | None | None |
| preview_width | False | integer | False | None | None | None |
| preview_height | False | integer | False | None | None | None |
| preview_border | False | integer | False | None | None | None |
| minimap_lookup_file | False | text | False | 50 | None | None |
| is_available_in_custom_battle | False | yesno | True | None | None | None |
  
## campaign_map_regions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_map | True | text | True | 50 | [campaign_maps_tables](#campaign_maps_tables) | mapname |
| region | True | text | True | 50 | [regions_tables](#regions_tables) | key |
  
## campaign_map_roads_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| threshold | False | double | True | None | None | None |
| turns_required_to_upgrade_to | False | integer | True | None | None | None |
| turns_required_to_downgrade_from | False | integer | True | None | None | None |
| movement_cost | False | integer | True | None | None | None |
  
## campaign_map_settlements_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| settlement_id | True | text | True | 50 | None | None |
| region | False | text | True | 50 | [regions_tables](#regions_tables) | key |
| default_onscreen_name | False | text | True | 50 | None | None |
| template_name | False | text | True | 50 | [campaign_map_settlement_templates_tables](#campaign_map_settlement_templates_tables) | template_name |
| slot_count | False | integer | True | None | None | None |
| slot_type | False | text | True | 50 | [slots_tables](#slots_tables) | slot |
  
## campaign_map_settlement_templates_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| template_name | True | text | True | 50 | None | None |
| slot_total | False | integer | True | None | None | None |
  
## campaign_map_settlement_templates_cult_art_jct_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| settlement_template | True | text | True | 50 | [campaign_map_settlement_templates_tables](#campaign_map_settlement_templates_tables) | template_name |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| artpiece | False | text | True | 50 | None | None |
  
## campaign_map_slots_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| slot_id | True | text | True | 50 | None | None |
| region | False | text | True | 50 | [regions_tables](#regions_tables) | key |
| slot_type | False | text | True | 50 | [slots_tables](#slots_tables) | slot |
| template | False | text | False | 50 | [campaign_map_slots_templates_tables](#campaign_map_slots_templates_tables) | template_name |
| rotation | False | integer | True | None | None | None |
| underlay | False | text | False | 50 | [warscape_underlay_textures_tables](#warscape_underlay_textures_tables) | underlay_key |
| onscreen | False | text | False | 50 | None | None |
  
## campaign_map_slots_templates_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| template_name | True | text | True | 50 | None | None |
| slot | False | text | True | 50 | [slots_tables](#slots_tables) | slot |
| levels | False | integer | True | None | None | None |
| art_file | False | text | True | 50 | None | None |
  
## campaign_map_tooltips_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| select_context | True | text | True | 50 | [campaign_map_tooltip_select_contexts_tables](#campaign_map_tooltip_select_contexts_tables) | select_context |
| over_context | True | text | True | 50 | [campaign_map_tooltip_over_contexts_tables](#campaign_map_tooltip_over_contexts_tables) | over_contexts |
| tooltip_line | False | text | False | 255 | [campaign_map_tooltip_texts_tables](#campaign_map_tooltip_texts_tables) | key |
| advice_line | False | text | False | 255 | [campaign_map_tooltip_texts_tables](#campaign_map_tooltip_texts_tables) | key |
| main_line | False | text | False | 255 | [campaign_map_tooltip_texts_tables](#campaign_map_tooltip_texts_tables) | key |
  
## campaign_map_tooltip_over_contexts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| over_contexts | True | text | True | 50 | None | None |
  
## campaign_map_tooltip_select_contexts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| select_context | True | text | True | 50 | None | None |
  
## campaign_map_tooltip_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| tooltip_text | False | text | True | 536870910 | None | None |
  
## campaign_map_towns_and_ports_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| town_id | True | text | True | 50 | None | None |
| region | False | text | True | 50 | [regions_tables](#regions_tables) | key |
| slot_type | False | text | True | 50 | [slots_tables](#slots_tables) | slot |
| onscreen_name | False | text | True | 50 | None | None |
| template | False | text | False | 50 | [campaign_map_slots_templates_tables](#campaign_map_slots_templates_tables) | template_name |
  
## campaign_map_town_templates_cult_art_jct_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| artpiece | False | text | True | 50 | None | None |
  
## campaign_map_transition_areas_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| mapname | False | text | True | 255 | [campaign_maps_tables](#campaign_maps_tables) | mapname |
| index | True | autonumber | False | None | None | None |
| minx | False | double | True | None | None | None |
| miny | False | double | True | None | None | None |
| maxx | False | double | True | None | None | None |
| maxy | False | double | True | None | None | None |
| storm_chance_percentage | False | integer | True | None | None | None |
| onscreen_name | False | text | False | 255 | None | None |
  
## campaign_map_transition_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| index | False | autonumber | False | None | None | None |
| start_area | True | integer | True | None | [campaign_map_transition_areas_tables](#campaign_map_transition_areas_tables) | index |
| end_area | True | integer | True | None | [campaign_map_transition_areas_tables](#campaign_map_transition_areas_tables) | index |
| delay_chance_percentage | False | integer | True | None | None | None |
| turns_start_to_end | False | integer | True | None | None | None |
| turns_end_to_start | False | integer | True | None | None | None |
  
## campaign_mp_coop_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_mp_coop_groups_to_factions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction_key | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| mp_coop_group | True | text | True | 255 | [campaign_mp_coop_groups_tables](#campaign_mp_coop_groups_tables) | key |
  
## campaign_politics_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| string | False | text | True | 255 | None | None |
  
## campaign_public_order_populace_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| populace_happiness | True | text | True | 255 | None | None |
| culture | True | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
  
## campaign_settlement_display_aqueducts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| region_key | True | text | True | 255 | [regions_tables](#regions_tables) | key |
| building_path | False | text | False | 255 | None | None |
| position_x_map | False | double | True | None | None | None |
| position_y_map | False | double | True | None | None | None |
| position_z_height | False | double | True | None | None | None |
| rotation_cw_radians | False | double | True | None | None | None |
  
## campaign_settlement_display_buildings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| display_building_key | False | text | True | 255 | [campaign_settlement_display_building_ids_tables](#campaign_settlement_display_building_ids_tables) | key |
| state | False | text | False | 255 | [campaign_settlement_display_buildings_enums_tables](#campaign_settlement_display_buildings_enums_tables) | type |
| is_slum | False | yesno | True | None | None | None |
| is_sieged | False | yesno | True | None | None | None |
| is_blockaded | False | yesno | True | None | None | None |
| building_path | False | text | False | 255 | None | None |
| destruction_additional_model | False | text | False | 255 | None | None |
| destruction_override_model | False | text | False | 255 | None | None |
| construction_additional_model | False | text | False | 255 | None | None |
| construction_override_model | False | text | False | 255 | None | None |
  
## campaign_settlement_display_buildings_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | False | 255 | None | None |
  
## campaign_settlement_display_building_constructions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| display_building_key | False | text | True | 255 | [campaign_settlement_display_building_ids_tables](#campaign_settlement_display_building_ids_tables) | key |
| construction_type | False | text | True | 255 | [campaign_settlement_display_building_construction_enums_tables](#campaign_settlement_display_building_construction_enums_tables) | type |
| phase | False | integer | True | None | None | None |
| building_path | False | text | False | 255 | None | None |
  
## campaign_settlement_display_building_construction_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 255 | None | None |
  
## campaign_settlement_display_building_ids_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| building_level_key | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| sprawl_piece_type | False | text | False | 255 | [campaign_settlement_display_sprawl_pieces_tables](#campaign_settlement_display_sprawl_pieces_tables) | key |
| sprawl_piece_level | False | integer | True | None | None | None |
| culture | False | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| sub_culture | False | text | False | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| faction | False | text | False | 255 | [factions_tables](#factions_tables) | key |
  
## campaign_settlement_display_building_trees_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| rigid_lookup_key | False | text | False | 255 | None | None |
| climate_type | False | text | True | 50 | [climates_tables](#climates_tables) | climate_type |
| building_path | False | text | False | 255 | None | None |
  
## campaign_settlement_display_siege_item_ids_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battlefield_deployable_siege_item | True | text | True | 255 | [battlefield_deployable_siege_items_tables](#battlefield_deployable_siege_items_tables) | key |
| sprawl_piece | False | text | True | 255 | [campaign_settlement_display_sprawl_pieces_tables](#campaign_settlement_display_sprawl_pieces_tables) | key |
  
## campaign_settlement_display_sprawl_pieces_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_stances_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_stance_effects_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| stance | True | text | True | 255 | [campaign_stances_tables](#campaign_stances_tables) | key |
| effect_bundle | True | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| culture | True | text | False | 255 | [cultures_tables](#cultures_tables) | key |
| subculture | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
  
## campaign_statistics_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| localised_description | False | text | True | 255 | None | None |
| category_order | False | integer | True | None | None | None |
  
## campaign_statistics_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_statistics_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_statistic | True | text | True | 255 | [campaign_statistics_enums_tables](#campaign_statistics_enums_tables) | key |
| localised_description | False | text | True | 255 | None | None |
| campaign_statistic_category | False | text | True | 255 | [campaign_statistics_categories_tables](#campaign_statistics_categories_tables) | key |
| statistic_order | False | integer | True | None | None | None |
  
## campaign_subjects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| optional_name | False | text | False | 255 | [campaign_subject_strings_tables](#campaign_subject_strings_tables) | key |
| optional_name_source_faction | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| ui_image | False | text | True | 255 | None | None |
| flavour_text | False | text | True | 255 | [campaign_subject_strings_tables](#campaign_subject_strings_tables) | key |
| male | False | yesno | True | None | None | None |
  
## campaign_subject_evolutions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| campaign_subject_key | False | text | True | 255 | [campaign_subjects_tables](#campaign_subjects_tables) | key |
| effect_bundle_key | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| min_turns | False | integer | True | None | None | None |
| max_turns | False | integer | True | None | None | None |
| weighting | False | single | True | None | None | None |
| arrival_message | False | text | False | 255 | [campaign_subject_messages_tables](#campaign_subject_messages_tables) | key |
| departure_message | False | text | False | 255 | [campaign_subject_messages_tables](#campaign_subject_messages_tables) | key |
| flavour_text | False | text | False | 255 | [campaign_subject_strings_tables](#campaign_subject_strings_tables) | key |
  
## campaign_subject_evolution_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| parent | True | text | True | 255 | [campaign_subject_evolutions_tables](#campaign_subject_evolutions_tables) | key |
| child | True | text | True | 255 | [campaign_subject_evolutions_tables](#campaign_subject_evolutions_tables) | key |
  
## campaign_subject_faction_restriction_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_subject_key | True | text | True | 255 | [campaign_subjects_tables](#campaign_subjects_tables) | key |
| faction_key | True | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## campaign_subject_messages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| message_type | False | text | True | 255 | [message_events_tables](#message_events_tables) | event |
| optional_text | False | text | False | 255 | None | None |
  
## campaign_subject_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| string | False | text | True | 255 | None | None |
  
## campaign_unit_stat_bonuses_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| bonus | True | text | True | 255 | None | None |
| level | True | integer | True | None | None | None |
| threshold | False | integer | True | None | None | None |
| description | False | text | True | 20000 | None | None |
| icon_path | False | text | True | 20000 | None | None |
| upgrade_cost_new | False | integer | True | None | None | None |
| upgrade_cost_from_previous_level | False | integer | True | None | None | None |
  
## campaign_variables_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| variable_key | True | text | True | 50 | None | None |
| value | False | double | True | None | None | None |
| description | False | text | True | 536870910 | None | None |
  
## campaign_vfx_campaign_vfx_event_ids_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_vfx_event | True | text | True | 255 | None | None |
  
## campaign_vfx_descriptions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| vfx | False | text | True | 255 | [particle_effects_tables](#particle_effects_tables) | key |
| x_offset | False | decimal | True | None | None | None |
| y_offset | False | decimal | True | None | None | None |
| z_offset | False | decimal | True | None | None | None |
  
## campaign_vfx_lookups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| vfx_event | False | text | True | 255 | [campaign_vfx_campaign_vfx_event_ids_tables](#campaign_vfx_campaign_vfx_event_ids_tables) | campaign_vfx_event |
| vfx_description | False | text | True | 255 | [campaign_vfx_descriptions_tables](#campaign_vfx_descriptions_tables) | key |
| faction_filter | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| culture_filter | False | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| agent_filter | False | text | False | 255 | [agents_tables](#agents_tables) | key |
  
## campaign_walk_anim_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| reference_pose | False | text | True | 50 | [anim_reference_poses_tables](#anim_reference_poses_tables) | key |
| pre_step_to | False | text | False | 255 | None | None |
| step_to | False | text | True | 255 | None | None |
| post_step_to | False | text | False | 255 | None | None |
| pre_stand_to_walk | False | text | True | 255 | None | None |
| stand_to_walk | False | text | True | 255 | None | None |
| stand_to_walk_distance | False | single | True | None | None | None |
| walk | False | text | True | 255 | None | None |
| walk_distance | False | single | True | None | None | None |
| walk_to_stand | False | text | True | 255 | None | None |
| mid_walk_to_stand | False | text | True | 255 | None | None |
| walk_to_stand_distance | False | single | True | None | None | None |
| post_walk_to_stand | False | text | True | 255 | None | None |
| post_mid_walk_to_stand | False | text | True | 255 | None | None |
  
## capture_point_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| onscreen_name | False | text | True | 255 | None | None |
| icon_name | False | text | True | 255 | None | None |
  
## cdir_campaign_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| campaign | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## cdir_configs_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_key | True | text | True | 255 | [cdir_campaign_junctions_tables](#cdir_campaign_junctions_tables) | key |
| faction_key | True | text | True | 255 | [cdir_faction_junctions_tables](#cdir_faction_junctions_tables) | key |
| cdir_config_key | True | text | True | 255 | [cdir_config_values_tables](#cdir_config_values_tables) | key |
| value | False | text | False | 255 | None | None |
  
## cdir_config_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cdir_desires_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cdir_desire_priorities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_key | True | text | True | 255 | [cdir_campaign_junctions_tables](#cdir_campaign_junctions_tables) | key |
| desire_key | True | text | True | 255 | [cdir_desires_tables](#cdir_desires_tables) | key |
| priority | False | integer | True | None | None | None |
  
## cdir_events_dilemma_choices_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| choice_key | True | text | True | 255 | None | None |
  
## cdir_events_dilemma_choice_details_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| dilemma_key | True | text | True | 255 | [dilemmas_tables](#dilemmas_tables) | key |
| choice_key | True | text | True | 255 | [cdir_events_dilemma_choices_tables](#cdir_events_dilemma_choices_tables) | choice_key |
| localised_choice_label | False | text | True | 20000 | None | None |
| localised_choice_title | False | text | True | 20000 | None | None |
  
## cdir_events_dilemma_followup_dilemmas_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| dilemma_key | True | text | True | 255 | [dilemmas_tables](#dilemmas_tables) | key |
| choice_key | True | text | True | 255 | [cdir_events_dilemma_choices_tables](#cdir_events_dilemma_choices_tables) | choice_key |
| followup_dilemma_key | True | text | True | 255 | [dilemmas_tables](#dilemmas_tables) | key |
  
## cdir_events_dilemma_followup_missions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| dilemma_key | True | text | True | 255 | [dilemmas_tables](#dilemmas_tables) | key |
| choice_key | True | text | True | 255 | [cdir_events_dilemma_choices_tables](#cdir_events_dilemma_choices_tables) | choice_key |
| followup_mission_key | True | text | True | 255 | [missions_tables](#missions_tables) | key |
  
## cdir_events_dilemma_incidents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| dilemma_key | True | text | True | 255 | None | None |
| choice_key | True | text | True | 255 | None | None |
| incident_key | True | text | True | 255 | None | None |
  
## cdir_events_dilemma_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| option_key | True | text | True | 255 | None | None |
  
## cdir_events_dilemma_option_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| dilemma_key | False | text | True | 255 | [dilemmas_tables](#dilemmas_tables) | key |
| option_key | False | text | True | 255 | [cdir_events_dilemma_options_tables](#cdir_events_dilemma_options_tables) | option_key |
| value | False | text | False | 255 | None | None |
  
## cdir_events_dilemma_payloads_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| dilemma_key | False | text | True | 255 | None | None |
| choice_key | False | text | True | 255 | None | None |
| payload_key | False | text | True | 255 | [cdir_events_payloads_tables](#cdir_events_payloads_tables) | payload_key |
| value | False | text | False | 255 | None | None |
  
## cdir_events_incident_followup_dilemmas_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| incident_key | True | text | True | 255 | [incidents_tables](#incidents_tables) | key |
| followup_dliemma_key | True | text | True | 255 | [dilemmas_tables](#dilemmas_tables) | key |
  
## cdir_events_incident_followup_incidents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| incident_key | True | text | True | 255 | [incidents_tables](#incidents_tables) | key |
| followup_incident_key | True | text | True | 255 | [incidents_tables](#incidents_tables) | key |
  
## cdir_events_incident_followup_missions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| incident_key | True | text | True | 255 | [incidents_tables](#incidents_tables) | key |
| followup_mission_key | True | text | True | 255 | [missions_tables](#missions_tables) | key |
  
## cdir_events_incident_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| option_key | True | text | True | 255 | None | None |
  
## cdir_events_incident_option_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| incident_key | False | text | True | 255 | [incidents_tables](#incidents_tables) | key |
| option_key | False | text | True | 255 | [cdir_events_incident_options_tables](#cdir_events_incident_options_tables) | option_key |
| value | False | text | False | 255 | None | None |
  
## cdir_events_incident_payloads_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| incident_key | False | text | True | 255 | None | None |
| payload_key | False | text | True | 255 | [cdir_events_payloads_tables](#cdir_events_payloads_tables) | payload_key |
| value | False | text | False | 255 | None | None |
  
## cdir_events_mission_followup_dilemmas_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| mission_key | True | text | True | 255 | [missions_tables](#missions_tables) | key |
| status_key | True | text | True | 255 | [cdir_events_mission_statuses_tables](#cdir_events_mission_statuses_tables) | status_key |
| followup_dilemma_key | True | text | True | 255 | [dilemmas_tables](#dilemmas_tables) | key |
  
## cdir_events_mission_followup_missions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| mission_key | True | text | True | 255 | [missions_tables](#missions_tables) | key |
| status_key | True | text | True | 255 | [cdir_events_mission_statuses_tables](#cdir_events_mission_statuses_tables) | status_key |
| followup_mission_key | True | text | True | 255 | [missions_tables](#missions_tables) | key |
  
## cdir_events_mission_incidents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| mission_key | True | text | True | 255 | None | None |
| status_key | True | text | True | 255 | None | None |
| incident_key | True | text | True | 255 | None | None |
  
## cdir_events_mission_issuer_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| mission_key | True | text | True | 255 | None | None |
| issuer_key | True | text | True | 255 | [mission_issuers_tables](#mission_issuers_tables) | issuer_key |
  
## cdir_events_mission_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| option_key | True | text | True | 255 | None | None |
  
## cdir_events_mission_option_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| mission_key | False | text | True | 255 | [missions_tables](#missions_tables) | key |
| option_key | False | text | True | 255 | [cdir_events_mission_options_tables](#cdir_events_mission_options_tables) | option_key |
| value | False | text | False | 255 | None | None |
  
## cdir_events_mission_payloads_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| mission_key | False | text | True | 255 | None | None |
| status_key | False | text | True | 255 | None | None |
| payload_key | False | text | True | 255 | [cdir_events_payloads_tables](#cdir_events_payloads_tables) | payload_key |
| value | False | text | False | 255 | None | None |
  
## cdir_events_mission_statuses_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| status_key | True | text | True | 255 | None | None |
  
## cdir_events_payloads_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| payload_key | True | text | True | 255 | None | None |
| effect_bundle_key | False | text | False | 255 | None | None |
  
## cdir_faction_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| faction | False | text | False | 255 | [factions_tables](#factions_tables) | key |
  
## cdir_military_generator_configs_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cdir_military_generator_templates_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cdir_military_generator_template_priorities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| config_key | True | text | True | 255 | [cdir_military_generator_configs_tables](#cdir_military_generator_configs_tables) | key |
| template_key | True | text | True | 255 | [cdir_military_generator_templates_tables](#cdir_military_generator_templates_tables) | key |
| priority | False | integer | True | None | None | None |
  
## cdir_military_generator_template_ratios_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| template_key | True | text | True | 255 | [cdir_military_generator_templates_tables](#cdir_military_generator_templates_tables) | key |
| unit_group_key | True | text | True | 255 | [cdir_military_generator_unit_groups_tables](#cdir_military_generator_unit_groups_tables) | key |
| ratio | False | integer | True | None | None | None |
  
## cdir_military_generator_unit_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cdir_military_generator_unit_qualities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| group_key | True | text | True | 255 | [cdir_military_generator_unit_groups_tables](#cdir_military_generator_unit_groups_tables) | key |
| unit_key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| quality | False | integer | True | None | None | None |
  
## centralised_upgrade_building_level_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| upgraded_building_level | True | text | True | 255 | [building_levels_tables](#building_levels_tables) | level_name |
| central_building_level | False | text | True | 255 | [building_levels_tables](#building_levels_tables) | level_name |
| priority | True | integer | True | None | None | None |
  
## character_experience_skill_tiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent_key | True | text | False | 255 | [agents_tables](#agents_tables) | key |
| skill_rank | True | integer | True | None | None | None |
| experience_threshold | False | integer | True | None | None | None |
| skill_points | False | integer | True | None | None | None |
| optional_campaign_key | True | text | False | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| for_army | True | yesno | True | None | None | None |
| for_navy | True | yesno | True | None | None | None |
  
## character_skills_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| image_path | False | text | True | 255 | None | None |
| localised_name | False | text | True | 255 | None | None |
| localised_description | False | text | True | 255 | None | None |
| pre_battle_speech_parameter | False | text | False | 255 | [pre_battle_speech_parameters_enum_tables](#pre_battle_speech_parameters_enum_tables) | key |
| unlocked_at_rank | False | integer | True | None | None | None |
| is_background_skill | False | yesno | True | None | None | None |
| is_female_only_background_skill | False | yesno | True | None | None | None |
| is_male_only_background_skill | False | yesno | True | None | None | None |
| background_weighting | False | single | True | None | None | None |
  
## character_skill_level_details_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| level | True | integer | True | None | None | None |
| skill_key | True | text | True | 255 | [character_skills_tables](#character_skills_tables) | key |
| faction_key | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| campaign_key | True | text | False | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| subculture_key | True | text | False | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| localised_name | False | text | False | 20000 | None | None |
| localised_description | False | text | False | 20000 | None | None |
| image_path | False | text | True | 255 | None | None |
| unlocked_at_rank | False | integer | True | None | None | None |
  
## character_skill_level_to_effects_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| character_skill_key | True | text | True | 255 | [character_skills_tables](#character_skills_tables) | key |
| level | True | integer | True | None | None | None |
| effect_key | True | text | True | 256 | [effects_tables](#effects_tables) | effect |
| value | False | single | True | None | None | None |
| is_factionwide | False | yesno | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## character_skill_nodes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| character_skill_node_set_key | False | text | True | 255 | [character_skill_node_sets_tables](#character_skill_node_sets_tables) | key |
| character_skill_key | False | text | True | 255 | [character_skills_tables](#character_skills_tables) | key |
| faction_key | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| campaign_key | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| tier | False | integer | True | None | None | None |
| indent | False | integer | True | None | None | None |
| subculture | False | text | False | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## character_skill_node_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| parent_key | True | text | True | 255 | [character_skill_nodes_tables](#character_skill_nodes_tables) | key |
| child_key | True | text | True | 255 | [character_skill_nodes_tables](#character_skill_nodes_tables) | key |
| initial_descent_tiers | False | integer | True | None | None | None |
| parent_link_position | False | integer | True | None | None | None |
| child_link_position | False | integer | True | None | None | None |
  
## character_skill_node_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| faction_key | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| campaign_key | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| agent_key | False | text | False | 255 | [agents_tables](#agents_tables) | key |
| enc_title | False | text | True | 1024 | None | None |
| subculture | False | text | False | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| for_army | False | yesno | True | None | None | None |
| for_navy | False | yesno | True | None | None | None |
  
## character_traits_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | [trait_info_tables](#trait_info_tables) | trait |
| no_going_back_level | False | integer | True | None | None | None |
| hidden | False | yesno | True | None | None | None |
| precedence | False | integer | False | None | None | None |
| icon | False | text | True | 50 | [trait_categories_tables](#trait_categories_tables) | category |
| author | False | text | True | 50 | None | None |
| comment | False | text | False | 536870910 | None | None |
| pre_battle_speech_parameter | False | text | False | 255 | [pre_battle_speech_parameters_enum_tables](#pre_battle_speech_parameters_enum_tables) | key |
  
## character_trait_levels_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| onscreen_name | False | text | True | 50 | None | None |
| trait | False | text | True | 50 | [trait_info_tables](#trait_info_tables) | trait |
| level | False | integer | True | None | None | None |
| threshold_points | False | integer | True | None | None | None |
| epithet_text | False | text | False | 536870910 | None | None |
| gain_text | False | text | False | 536870910 | None | None |
| effect_text | False | text | False | 536870910 | None | None |
| colour_text | False | text | True | 536870910 | None | None |
| explanation_text | False | text | False | 536870910 | None | None |
| removal_text | False | text | False | 536870910 | None | None |
| enabled_by_tech | False | text | False | 255 | [technologies_tables](#technologies_tables) | key |
  
## chariot_types_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## chat_shortcuts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| description | False | text | True | 20000 | None | None |
| game_area | False | text | True | 255 | [game_area_enums_tables](#game_area_enums_tables) | key |
  
## climates_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| climate_type | True | text | True | 50 | None | None |
| colour_index | False | integer | True | None | None | None |
| conifer_line | False | integer | True | None | None | None |
| tree_line | False | integer | True | None | None | None |
| is_land | False | yesno | False | None | None | None |
  
## climate_to_weather_land_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| Climate_type | True | text | True | 50 | [climates_tables](#climates_tables) | climate_type |
| season | True | text | True | 50 | [seasons_tables](#seasons_tables) | season |
| Dry | False | integer | True | None | None | None |
| Dusty | False | integer | True | None | None | None |
| Sandstorm | False | integer | True | None | None | None |
| Drizzle | False | integer | True | None | None | None |
| Light_rain | False | integer | True | None | None | None |
| Moderate_rain | False | integer | True | None | None | None |
| Heavy_rain | False | integer | True | None | None | None |
| Storm | False | integer | True | None | None | None |
| Light_snow | False | integer | True | None | None | None |
| Moderate_snow | False | integer | True | None | None | None |
| Heavy_snow | False | integer | True | None | None | None |
| Blizzard | False | integer | True | None | None | None |
| Heat_fatigue | False | integer | True | None | None | None |
| Cold_fatigue | False | integer | True | None | None | None |
| Haze_index | False | integer | True | None | None | None |
| Fog_index | False | integer | True | None | None | None |
  
## commander_unit_permissions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| faction_key | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| culture_key | True | text | False | 255 | [cultures_tables](#cultures_tables) | key |
| subculture_key | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## commodities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [resources_tables](#resources_tables) | key |
| baseline_price_per_unit | False | double | True | None | None | None |
| price_elasticity_of_demand | False | double | True | None | None | None |
  
## commodity_unit_names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit | True | text | True | 50 | None | None |
| plural | False | text | True | 50 | None | None |
| singular | False | text | True | 50 | None | None |
  
## cultures_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| index | False | autonumber | True | None | None | None |
| fallback_ui_culture | False | text | False | 50 | None | None |
| name | False | text | True | 255 | None | None |
  
## cultures_subcultures_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| subculture | True | text | True | 50 | None | None |
| culture | False | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| index | False | autonumber | True | None | None | None |
| farm | False | text | True | 50 | [battle_terrain_farms_tables](#battle_terrain_farms_tables) | farm |
| name | False | text | True | 255 | None | None |
| confederation_screen_name | False | text | False | 255 | None | None |
| confederation_summary_name | False | text | False | 255 | None | None |
  
## culture_settlement_occupation_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| option | True | text | True | 255 | None | None |
  
## culture_subculture_character_portraits_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| portrait_type | True | text | True | 255 | [portrait_types_tables](#portrait_types_tables) | key |
| culture | True | text | False | 255 | [cultures_tables](#cultures_tables) | key |
| subculture | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| path | False | text | True | 255 | None | None |
  
## culture_subculture_politics_government_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| culture | True | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| government_type | True | text | True | 255 | [politics_government_types_tables](#politics_government_types_tables) | government_type |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| on_screen_name_government_type | False | text | True | 255 | None | None |
| on_screen_name_faction_leader | False | text | False | 255 | None | None |
| effect_bundle | False | text | False | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| is_default | False | yesno | True | None | None | None |
| faction_leader_trait | False | text | True | 255 | [trait_info_tables](#trait_info_tables) | trait |
| on_screen_name_faction_leader_female | False | text | False | 255 | None | None |
| faction_leader_trait_female | False | text | True | 255 | [trait_info_tables](#trait_info_tables) | trait |
| on_screen_name_government_actions | False | text | False | 255 | None | None |
| on_screen_descr_government_actions | False | text | False | 255 | None | None |
  
## cursors_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| image | False | text | True | 50 | None | None |
| frames | False | integer | True | None | None | None |
| framerate | False | integer | True | None | None | None |
| hotspotX | False | integer | True | None | None | None |
| hotspotY | False | integer | True | None | None | None |
| loop | False | yesno | True | None | None | None |
| width | False | integer | False | None | None | None |
| height | False | integer | False | None | None | None |
  
## cursor_mouse_events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 20000 | None | None |
  
## cursor_transitions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| initiating_cursor | True | text | True | 50 | [cursors_tables](#cursors_tables) | key |
| resulting_cursor | False | text | True | 50 | [cursors_tables](#cursors_tables) | key |
| mouse_event | True | text | True | 20000 | [cursor_mouse_events_tables](#cursor_mouse_events_tables) | key |
  
## cursus_honorum_level_requirements_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| subculture_key | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| level | True | integer | True | None | None | None |
| rank | False | integer | True | None | None | None |
| age | False | integer | True | None | None | None |
| faction_key | True | text | False | 255 | [factions_tables](#factions_tables) | key |
  
## cursus_honorum_trait_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| subculture_key | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| trait_info_key | True | text | True | 255 | [trait_info_tables](#trait_info_tables) | trait |
| faction_key | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| trait_info_key_female | True | text | False | 255 | [trait_info_tables](#trait_info_tables) | trait |
  
## dave_permissions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| permission | True | text | True | 255 | None | None |
  
## dave_restricted_tables_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| table_name | True | text | True | 255 | [TExc_ImplementedTables_tables](#TExc_ImplementedTables_tables) | table_name |
  
## dave_user_table_permissions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| user_name | True | text | True | 255 | None | None |
| table_name | True | text | True | 255 | [TExc_ImplementedTables_tables](#TExc_ImplementedTables_tables) | table_name |
| permission | True | text | True | 255 | [dave_permissions_tables](#dave_permissions_tables) | permission |
  
## death_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## deployables_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| name | False | text | True | 255 | None | None |
| model | False | text | True | 255 | [models_deployables_tables](#models_deployables_tables) | key |
| model_2 | False | text | False | 255 | [models_deployables_tables](#models_deployables_tables) | key |
| number | False | integer | True | None | None | None |
| spacing_x | False | decimal | True | None | None | None |
| spacing_y | False | decimal | True | None | None | None |
| min_rows | False | integer | True | None | None | None |
| min_columns | False | integer | True | None | None | None |
| random_offset | False | decimal | True | None | None | None |
| hitpoints | False | integer | True | None | None | None |
| kill_chance | False | decimal | True | None | None | None |
| stat_mod | False | text | False | 255 | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| value | False | decimal | True | None | None | None |
| how | False | text | False | 255 | [unit_stat_modifiers_how_enums_tables](#unit_stat_modifiers_how_enums_tables) | key |
| icon_name | False | text | True | 255 | None | None |
| info_pic | False | text | True | 255 | None | None |
| description | False | text | True | 255 | None | None |
| tooltip | False | text | True | 255 | None | None |
| in_encyclopaedia | False | yesno | True | None | None | None |
| recruitment_cap | False | integer | True | None | None | None |
| max_rows | False | integer | True | None | None | None |
| ignition_threshold | False | integer | True | None | None | None |
  
## deployables_custom_battles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| deployable | True | text | True | 255 | [deployables_tables](#deployables_tables) | key |
| cap | False | integer | True | None | None | None |
| probability | False | integer | True | None | None | None |
  
## dilemmas_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| localised_title | False | text | True | 255 | None | None |
| localised_description | False | text | True | 900000 | None | None |
| ui_image | False | text | True | 255 | None | None |
| ui_icon | False | text | True | 255 | None | None |
| generate | False | yesno | True | None | None | None |
| prioritized | False | yesno | True | None | None | None |
  
## dilemma_to_campaign_subject_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| dilemma_key | True | text | True | 255 | [dilemmas_tables](#dilemmas_tables) | key |
| campaign_subject_key | True | text | True | 255 | [campaign_subjects_tables](#campaign_subjects_tables) | key |
| weighting | False | single | True | None | None | None |
  
## diplomacy_current_treaties_to_diplomatic_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| current_treaty_key | True | text | True | 255 | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| diplomatic_option_key | False | text | True | 255 | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| can_be_cancelled | False | yesno | True | None | None | None |
  
## diplomacy_keys_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## diplomacy_negotiation_attitudes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| minimum_attitude | False | integer | True | None | None | None |
| maximum_attitude | False | integer | True | None | None | None |
  
## diplomacy_negotiation_attitude_override_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [diplomacy_keys_tables](#diplomacy_keys_tables) | key |
| culture | True | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| government_type | True | text | True | 255 | [government_types_tables](#government_types_tables) | government_type |
| attitude | True | text | True | 255 | [diplomacy_negotiation_attitudes_tables](#diplomacy_negotiation_attitudes_tables) | key |
| string | False | text | True | 255 | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| option | True | integer | True | None | None | None |
  
## diplomacy_negotiation_faction_attitude_override_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [diplomacy_keys_tables](#diplomacy_keys_tables) | key |
| culture | True | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| government_type | True | text | True | 255 | [government_types_tables](#government_types_tables) | government_type |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| attitude | True | text | True | 255 | [diplomacy_negotiation_attitudes_tables](#diplomacy_negotiation_attitudes_tables) | key |
| string | False | text | True | 255 | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| option | True | integer | True | None | None | None |
  
## diplomacy_negotiation_faction_override_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | [diplomacy_keys_tables](#diplomacy_keys_tables) | key |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| government_type | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| faction | True | text | True | 50 | [factions_tables](#factions_tables) | key |
| string | False | text | True | 255 | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| option | True | integer | True | None | None | None |
  
## diplomacy_negotiation_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [diplomacy_keys_tables](#diplomacy_keys_tables) | key |
| culture | True | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| government_type | True | text | True | 255 | [government_types_tables](#government_types_tables) | government_type |
  
## diplomacy_negotiation_string_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | [diplomacy_keys_tables](#diplomacy_keys_tables) | key |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| government_type | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| string | False | text | True | 255 | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| option | True | integer | True | None | None | None |
  
## diplomacy_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| string | False | text | True | 536870910 | None | None |
  
## diplomatic_action_faction_restrictions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| can_make_vassals | False | yesno | True | None | None | None |
| can_make_client_states | False | yesno | True | None | None | None |
| can_make_confederations | False | yesno | True | None | None | None |
  
## diplomatic_action_subculture_restrictions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| subculture | True | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| can_make_vassals | False | yesno | True | None | None | None |
| can_make_client_states | False | yesno | True | None | None | None |
| can_make_confederations | False | yesno | True | None | None | None |
  
## diplomatic_relations_attitudes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| attitude | True | text | True | 50 | None | None |
| value | False | text | True | 50 | None | None |
  
## diplomatic_relations_religion_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| religion_A | True | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
| religion_B | True | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
| relations_modifier | False | integer | True | None | None | None |
| religious_unhappiness_modifier | False | single | True | None | None | None |
  
## effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | False | 50 | None | None |
| icon | False | text | False | 256 | None | None |
| description | False | text | False | 536870910 | None | None |
| priority | False | integer | True | None | None | None |
| icon_negative | False | text | False | 256 | None | None |
  
## effect_bonus_value_agent_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_agent_tables](#campaign_bonus_value_ids_agent_tables) | key |
| agent | True | text | True | 255 | [agents_tables](#agents_tables) | key |
  
## effect_bonus_value_basic_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_basic_tables](#campaign_bonus_value_ids_basic_tables) | key |
  
## effect_bonus_value_battlefield_deployables_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_battlefield_deployables_tables](#campaign_bonus_value_ids_battlefield_deployables_tables) | key |
| battlefield_deployable | True | text | True | 255 | [deployables_tables](#deployables_tables) | key |
  
## effect_bonus_value_battle_context_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect_key | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_battle_contexts_tables](#campaign_bonus_value_ids_battle_contexts_tables) | key |
| battle_context_key | False | text | True | 255 | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
  
## effect_bonus_value_building_chain_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | False | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | False | 255 | [campaign_bonus_value_ids_building_chain_tables](#campaign_bonus_value_ids_building_chain_tables) | key |
| building_chain | True | text | False | 50 | [building_chains_tables](#building_chains_tables) | key |
  
## effect_bonus_value_building_set_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_building_sets_tables](#campaign_bonus_value_ids_building_sets_tables) | key |
| building_set | True | text | True | 255 | [building_sets_tables](#building_sets_tables) | key |
  
## effect_bonus_value_commodity_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_commodity_tables](#campaign_bonus_value_ids_commodity_tables) | key |
| commodity | True | text | True | 255 | [commodities_tables](#commodities_tables) | key |
  
## effect_bonus_value_ids_unit_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_unit_sets_tables](#campaign_bonus_value_ids_unit_sets_tables) | key |
| unit_set | True | text | True | 255 | [unit_sets_tables](#unit_sets_tables) | key |
  
## effect_bonus_value_id_action_results_additional_outcomes_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_action_results_additional_outcomes_tables](#campaign_bonus_value_ids_action_results_additional_outcomes_tables) | key |
| action_results_additional_outcome_record | True | text | True | 255 | [action_results_additional_outcomes_tables](#action_results_additional_outcomes_tables) | key |
  
## effect_bonus_value_melee_weapon_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| melee_weapon | True | text | True | 50 | [unit_melee_weapons_enum_tables](#unit_melee_weapons_enum_tables) | key |
| stat_modifier | False | text | True | 255 | [unit_stat_modifiers_tables](#unit_stat_modifiers_tables) | key |
  
## effect_bonus_value_population_class_and_religion_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_population_class_and_religion_tables](#campaign_bonus_value_ids_population_class_and_religion_tables) | key |
| population_class | True | text | True | 50 | [population_classes_tables](#population_classes_tables) | population_class |
| religion | True | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
  
## effect_bonus_value_population_class_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_population_class_tables](#campaign_bonus_value_ids_population_class_tables) | key |
| population_class | True | text | True | 50 | [population_classes_tables](#population_classes_tables) | population_class |
  
## effect_bonus_value_projectile_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| projectile | True | text | True | 255 | [projectiles_tables](#projectiles_tables) | key |
| bonus_value | True | text | True | 255 | [campaign_bonus_value_ids_projectile_tables](#campaign_bonus_value_ids_projectile_tables) | key |
  
## effect_bonus_value_provincial_initiative_effect_record_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_provincial_initiative_effect_records_tables](#campaign_bonus_value_ids_provincial_initiative_effect_records_tables) | key |
| effect_bonus_will_modify | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
  
## effect_bonus_value_religion_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_religion_tables](#campaign_bonus_value_ids_religion_tables) | key |
| religion | True | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
  
## effect_bonus_value_resource_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_resource_tables](#campaign_bonus_value_ids_resource_tables) | key |
| resource | True | text | True | 50 | [resources_tables](#resources_tables) | key |
  
## effect_bonus_value_shot_type_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_projectile_shot_type_enum_tables](#campaign_bonus_value_ids_projectile_shot_type_enum_tables) | key |
| shot_type | True | text | True | 50 | [projectile_shot_type_enum_tables](#projectile_shot_type_enum_tables) | key |
  
## effect_bonus_value_siege_item_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_siege_items_tables](#campaign_bonus_value_ids_siege_items_tables) | key |
| siege_item | True | text | True | 50 | [battlefield_deployable_siege_items_tables](#battlefield_deployable_siege_items_tables) | key |
  
## effect_bonus_value_technology_category_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 64 | [campaign_bonus_value_ids_technology_categories_tables](#campaign_bonus_value_ids_technology_categories_tables) | key |
| technology_category | True | text | True | 255 | [technology_categories_tables](#technology_categories_tables) | key |
  
## effect_bonus_value_unit_ability_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_unit_ability_tables](#campaign_bonus_value_ids_unit_ability_tables) | key |
| unit_ability | True | text | True | 50 | [unit_abilities_tables](#unit_abilities_tables) | key |
  
## effect_bonus_value_unit_caste_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_unit_caste_tables](#campaign_bonus_value_ids_unit_caste_tables) | key |
| caste | True | text | True | 50 | [unit_castes_tables](#unit_castes_tables) | caste |
  
## effect_bonus_value_unit_caste_stat_modifiers_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| caste | True | text | True | 255 | [unit_castes_tables](#unit_castes_tables) | caste |
| stat_modifier | True | text | True | 255 | [unit_stat_modifiers_tables](#unit_stat_modifiers_tables) | key |
  
## effect_bonus_value_unit_category_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_unit_category_tables](#campaign_bonus_value_ids_unit_category_tables) | key |
| unit_category | True | text | True | 50 | [unit_category_tables](#unit_category_tables) | key |
  
## effect_bonus_value_unit_category_stat_modifiers_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| category | True | text | True | 50 | [unit_category_tables](#unit_category_tables) | key |
| stat_modifier | True | text | True | 255 | [unit_stat_modifiers_tables](#unit_stat_modifiers_tables) | key |
  
## effect_bonus_value_unit_class_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_unit_class_tables](#campaign_bonus_value_ids_unit_class_tables) | key |
| unit_class | True | text | True | 50 | [unit_class_tables](#unit_class_tables) | key |
  
## effect_bonus_value_unit_class_stat_modifiers_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| class | True | text | True | 255 | [unit_class_tables](#unit_class_tables) | key |
| stat_modifier | True | text | True | 255 | [unit_stat_modifiers_tables](#unit_stat_modifiers_tables) | key |
  
## effect_bonus_value_unit_record_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_unit_records_tables](#campaign_bonus_value_ids_unit_records_tables) | key |
| unit_record_key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
  
## effect_bonus_value_unit_record_stat_modifiers_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| unit | True | text | True | 255 | [units_tables](#units_tables) | key |
| stat_modifier | True | text | True | 255 | [unit_stat_modifiers_tables](#unit_stat_modifiers_tables) | key |
  
## effect_bonus_value_unit_stat_modifiers_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| stat_modifier | True | text | True | 255 | [unit_stat_modifiers_tables](#unit_stat_modifiers_tables) | key |
  
## effect_bundles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| localised_title | False | text | True | 255 | None | None |
| localised_description | False | text | True | 255 | None | None |
| ui_icon | False | text | True | 255 | None | None |
| bundle_target | False | text | True | 255 | [effect_bundle_targets_tables](#effect_bundle_targets_tables) | key |
  
## effect_bundles_to_effects_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect_bundle_key | True | text | True | 255 | None | None |
| effect_key | True | text | True | 255 | None | None |
| value | False | single | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| advancement_stage | False | text | True | 255 | [effect_bundle_advancement_stages_tables](#effect_bundle_advancement_stages_tables) | key |
  
## effect_bundle_advancement_stages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## effect_bundle_targets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## encyclopedia_agent_manual_block_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent_key | True | text | True | 255 | [agents_tables](#agents_tables) | key |
| block_key | True | text | True | 255 | [encyclopedia_blocks_tables](#encyclopedia_blocks_tables) | block_key |
  
## encyclopedia_agent_manual_page_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent_key | True | text | True | 255 | [agents_tables](#agents_tables) | key |
| page_key | True | text | True | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
  
## encyclopedia_blocks_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| block_key | True | text | True | 255 | None | None |
| page_key | False | text | True | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
| order | False | integer | True | None | None | None |
| heading | False | text | True | 65535 | None | None |
| class | False | text | True | 255 | None | None |
| content | False | text | True | 65535 | None | None |
| image | False | text | False | 65535 | None | None |
| image_class | False | text | True | 65535 | None | None |
| video | False | text | False | 65535 | None | None |
  
## encyclopedia_building_chain_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| group_name | True | text | True | 255 | None | None |
| localised_name | False | text | True | 255 | None | None |
| order | False | integer | True | None | None | None |
  
## encyclopedia_building_redirects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| redirect_building | False | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
  
## encyclopedia_faction_groupings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| group | False | text | True | 255 | [encyclopedia_faction_groups_tables](#encyclopedia_faction_groups_tables) | group_id |
| order | False | integer | True | None | None | None |
  
## encyclopedia_faction_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| group_id | True | text | True | 255 | None | None |
  
## encyclopedia_faction_iconic_units_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| main_unit_key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| faction_key | True | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## encyclopedia_glossary_blocks_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| block_key | True | text | True | 255 | None | None |
| page_key | False | text | True | 255 | [encyclopedia_glossary_pages_tables](#encyclopedia_glossary_pages_tables) | page_key |
| order | False | integer | True | None | None | None |
| heading | False | text | True | 65535 | None | None |
| class | False | text | True | 255 | None | None |
| content | False | text | True | 65535 | None | None |
| image | False | text | False | 65535 | None | None |
| image_class | False | text | True | 65535 | None | None |
| video | False | text | False | 65535 | None | None |
  
## encyclopedia_glossary_pages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | None | None |
| title | False | text | True | 65535 | None | None |
| template | False | text | True | 65535 | None | None |
  
## encyclopedia_glossary_page_linkages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | [encyclopedia_glossary_pages_tables](#encyclopedia_glossary_pages_tables) | page_key |
| parent_key | False | text | False | 255 | [encyclopedia_glossary_pages_tables](#encyclopedia_glossary_pages_tables) | page_key |
| next_key | False | text | False | 255 | [encyclopedia_glossary_pages_tables](#encyclopedia_glossary_pages_tables) | page_key |
  
## encyclopedia_historical_info_blocks_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| block_key | True | text | True | 255 | None | None |
| page_key | False | text | True | 255 | [encyclopedia_historical_info_pages_tables](#encyclopedia_historical_info_pages_tables) | page_key |
| order | False | integer | True | None | None | None |
| heading | False | text | True | 65535 | None | None |
| class | False | text | True | 255 | None | None |
| content | False | text | True | 65535 | None | None |
| image | False | text | False | 65535 | None | None |
| image_class | False | text | True | 65535 | None | None |
| video | False | text | False | 65535 | None | None |
  
## encyclopedia_historical_info_pages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | None | None |
| title | False | text | True | 65535 | None | None |
| template | False | text | True | 65535 | None | None |
  
## encyclopedia_historical_info_page_linkages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | [encyclopedia_historical_info_pages_tables](#encyclopedia_historical_info_pages_tables) | page_key |
| parent_key | False | text | False | 255 | [encyclopedia_historical_info_pages_tables](#encyclopedia_historical_info_pages_tables) | page_key |
| next_key | False | text | False | 255 | [encyclopedia_historical_info_pages_tables](#encyclopedia_historical_info_pages_tables) | page_key |
  
## encyclopedia_index_pages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | None | None |
| annotation | False | text | True | 255 | [encyclopedia_blocks_tables](#encyclopedia_blocks_tables) | block_key |
  
## encyclopedia_multiplayer_blocks_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| block_key | True | text | True | 255 | None | None |
| page_key | False | text | True | 255 | [encyclopedia_multiplayer_pages_tables](#encyclopedia_multiplayer_pages_tables) | page_key |
| order | False | integer | True | None | None | None |
| heading | False | text | True | 65535 | None | None |
| class | False | text | True | 255 | None | None |
| content | False | text | True | 65535 | None | None |
| image | False | text | False | 65535 | None | None |
| image_class | False | text | True | 65535 | None | None |
| video | False | text | False | 65535 | None | None |
  
## encyclopedia_multiplayer_pages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | None | None |
| title | False | text | True | 65535 | None | None |
| template | False | text | True | 65535 | None | None |
  
## encyclopedia_multiplayer_page_linkages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | [encyclopedia_multiplayer_pages_tables](#encyclopedia_multiplayer_pages_tables) | page_key |
| parent_key | False | text | False | 255 | [encyclopedia_multiplayer_pages_tables](#encyclopedia_multiplayer_pages_tables) | page_key |
| next_key | False | text | False | 255 | [encyclopedia_multiplayer_pages_tables](#encyclopedia_multiplayer_pages_tables) | page_key |
  
## encyclopedia_pages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | None | None |
| title | False | text | True | 65535 | None | None |
| template | False | text | True | 65535 | None | None |
  
## encyclopedia_page_linkages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
| parent_key | False | text | False | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
| next_key | False | text | False | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
  
## encyclopedia_page_related_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
| target | True | text | True | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
  
## encyclopedia_patch_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| text | False | text | True | 255 | None | None |
  
## encyclopedia_projectile_shot_type_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| shot_type | True | text | True | 50 | [projectile_shot_type_enum_tables](#projectile_shot_type_enum_tables) | key |
| manual_page | False | text | True | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
| manual_block | False | text | False | 255 | [encyclopedia_blocks_tables](#encyclopedia_blocks_tables) | block_key |
  
## encyclopedia_settings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| value | False | text | True | 1024 | None | None |
  
## encyclopedia_template_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| string_key | True | text | True | 255 | None | None |
| text | False | text | True | 65535 | None | None |
  
## encyclopedia_triggers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_key | True | text | True | 65535 | None | None |
| url | False | text | True | 65535 | None | None |
  
## encyclopedia_tutorial_sections_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| section | True | text | True | 255 | None | None |
| name | False | text | True | 20000 | None | None |
  
## encyclopedia_tutorial_videos_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| title | False | text | True | 20000 | None | None |
| section | False | text | True | 255 | [encyclopedia_tutorial_sections_tables](#encyclopedia_tutorial_sections_tables) | section |
| file | False | text | True | 255 | None | None |
| description | False | text | True | 200000 | None | None |
  
## encyclopedia_tutorial_videos_default_subtitles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| video | True | text | True | 255 | [encyclopedia_tutorial_videos_tables](#encyclopedia_tutorial_videos_tables) | key |
| language | True | text | True | 255 | [languages_tables](#languages_tables) | key |
  
## encyclopedia_tutorial_video_subtitles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [encyclopedia_tutorial_videos_tables](#encyclopedia_tutorial_videos_tables) | key |
| subtitle_number | True | integer | True | None | None | None |
| timecode_in | False | text | True | 255 | None | None |
| timecode_out | False | text | True | 255 | None | None |
| text | False | text | True | 20000 | None | None |
| line | False | integer | True | None | None | None |
  
## encyclopedia_unit_abilities_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_ability | True | text | True | 50 | [unit_abilities_tables](#unit_abilities_tables) | key |
| manual_page | False | text | True | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
| manual_block | False | text | False | 255 | [encyclopedia_blocks_tables](#encyclopedia_blocks_tables) | block_key |
  
## encyclopedia_unit_attributes_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_attribute | True | text | True | 255 | [unit_attributes_tables](#unit_attributes_tables) | key |
| manual_page | False | text | True | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
| manual_block | False | text | False | 255 | [encyclopedia_blocks_tables](#encyclopedia_blocks_tables) | block_key |
  
## encyclopedia_unit_patch_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| patch_text | False | text | True | 255 | [encyclopedia_patch_texts_tables](#encyclopedia_patch_texts_tables) | key |
  
## encyclopedia_unit_redirects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| redirect_unit | False | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
  
## encyclopedia_urls_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 255 | None | None |
| url | False | text | False | 255 | None | None |
  
## entity_training_levels_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| training_level | True | text | True | 50 | None | None |
| max_offset_distance | False | double | True | None | None | None |
  
## events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| picture_category | False | text | True | 255 | None | None |
| dynamic | False | yesno | True | None | None | None |
| onscreen_name | False | text | True | 255 | None | None |
| event_text | False | text | True | 536870910 | None | None |
| historical_date | False | double | True | None | None | None |
| season | False | text | True | 50 | [seasons_tables](#seasons_tables) | season |
| conditions | False | text | True | 536870910 | None | None |
| picture | False | text | True | 255 | None | None |
| turn_in_year | False | integer | True | None | None | None |
  
## events_effects_junct_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| event | True | text | True | 50 | [events_tables](#events_tables) | key |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | text | True | 50 | None | None |
  
## event_log_descriptions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| event_key | True | text | True | 255 | None | None |
| event_title | False | text | True | 255 | None | None |
| event_content | False | text | True | 255 | None | None |
| icon | False | text | True | 255 | None | None |
| has_position | False | yesno | True | None | None | None |
| is_region_position | False | yesno | True | None | None | None |
| notes | False | text | False | 65535 | None | None |
| optional_campaign_key | False | text | False | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| movie_id | False | integer | True | None | None | None |
  
## experience_triggers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| trigger_key | True | text | True | 255 | None | None |
| event | False | text | True | 255 | [trigger_events_tables](#trigger_events_tables) | event |
| experience_points | False | integer | True | None | None | None |
| condition | False | text | True | 255 | None | None |
| localised_description | False | text | False | 255 | None | None |
| target | False | text | True | 2000 | [experience_triggers_targets_tables](#experience_triggers_targets_tables) | key |
  
## experience_triggers_targets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 2000 | None | None |
  
## factions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| index | False | autonumber | True | None | None | None |
| subculture | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| category | False | text | True | 255 | None | None |
| screen_name | False | text | True | 255 | None | None |
| screen_name_when_rebels | False | text | True | 255 | None | None |
| screen_adjective | False | text | True | 255 | None | None |
| name_group | False | integer | True | None | [names_groups_tables](#names_groups_tables) | key |
| skin | False | text | True | 50 | None | None |
| is_rebel | False | yesno | True | None | None | None |
| icons_path_units | False | text | True | 50 | None | None |
| flags_path | False | text | True | 50 | None | None |
| republican_flag_path | False | text | False | 255 | None | None |
| same_gov_type_revolution_flag_path | False | text | False | 255 | None | None |
| primary_colour_r | False | double | True | None | None | None |
| primary_colour_g | False | double | True | None | None | None |
| primary_colour_b | False | double | True | None | None | None |
| alt_primary_colour_r | False | double | True | None | None | None |
| alt_primary_colour_g | False | double | True | None | None | None |
| alt_primary_colour_b | False | double | True | None | None | None |
| secondary_colour_r | False | double | True | None | None | None |
| secondary_colour_g | False | double | True | None | None | None |
| secondary_colour_b | False | double | True | None | None | None |
| alt_secondary_colour_r | False | double | True | None | None | None |
| alt_secondary_colour_g | False | double | True | None | None | None |
| alt_secondary_colour_b | False | double | True | None | None | None |
| rebel_colour_r | False | double | True | None | None | None |
| rebel_colour_g | False | double | True | None | None | None |
| rebel_colour_b | False | double | True | None | None | None |
| uniform_colour_r | False | double | True | None | None | None |
| uniform_colour_g | False | double | True | None | None | None |
| uniform_colour_b | False | double | True | None | None | None |
| alt_uniform_colour_r | False | double | True | None | None | None |
| alt_uniform_colour_g | False | double | True | None | None | None |
| alt_uniform_colour_b | False | double | True | None | None | None |
| military_group | False | text | False | 50 | [groupings_military_tables](#groupings_military_tables) | military_group |
| settler_rebellion_faction | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| mp_available | False | yesno | False | None | None | None |
| mp_available_naval | False | yesno | False | None | None | None |
| movie_death_event | False | integer | False | None | [movie_event_strings_tables](#movie_event_strings_tables) | id |
| mp_use_republic_early | False | yesno | False | None | None | None |
| mp_use_republic_late | False | yesno | False | None | None | None |
| unit_regiment_name_group | False | integer | True | None | [names_groups_tables](#names_groups_tables) | key |
| ship_name_group | False | integer | True | None | [names_groups_tables](#names_groups_tables) | key |
| ui_skin | False | text | False | 255 | None | None |
| attack_desc | False | text | True | 255 | None | None |
| defend_desc | False | text | True | 255 | None | None |
| mp_stats_name | False | text | False | 255 | None | None |
| pre_battle_speech_parameter | False | text | True | 255 | [pre_battle_speech_parameters_enum_tables](#pre_battle_speech_parameters_enum_tables) | key |
| screen_name_when_shogun | False | text | True | 2048 | None | None |
| clan_summary_name | False | text | False | 2048 | None | None |
| clan_summary_name_when_shogun | False | text | False | 2048 | None | None |
| can_be_regionless | False | yesno | True | None | None | None |
| card_colour_r | False | double | True | None | None | None |
| card_colour_g | False | double | True | None | None | None |
| card_colour_b | False | double | True | None | None | None |
| diplomacy_culture | False | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| senator_total | False | integer | True | None | None | None |
| senator_text_n_out_of_n | False | text | False | 255 | None | None |
| senator_text_lose_n | False | text | False | 255 | None | None |
| senator_text_lose_1 | False | text | False | 255 | None | None |
| senator_text_gain_n | False | text | False | 255 | None | None |
| senator_text_gain_1 | False | text | False | 255 | None | None |
| uses_legion_names | False | yesno | True | None | None | None |
  
## factions_parents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction | True | text | True | 50 | [factions_tables](#factions_tables) | key |
| parent_faction | False | text | True | 50 | [factions_tables](#factions_tables) | key |
  
## faction_banners_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| symbol | False | text | False | 255 | None | None |
| primary_red | False | integer | True | None | None | None |
| primary_green | False | integer | True | None | None | None |
| primary_blue | False | integer | True | None | None | None |
| secondary_red | False | integer | True | None | None | None |
| secondary_green | False | integer | True | None | None | None |
| secondary_blue | False | integer | True | None | None | None |
| tertiary_red | False | integer | True | None | None | None |
| tertiary_green | False | integer | True | None | None | None |
| tertiary_blue | False | integer | True | None | None | None |
  
## faction_civil_war_setups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| primary_faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| secondary_faction | False | text | True | 255 | [factions_tables](#factions_tables) | key |
| faction_name_override_primary_high | False | text | False | 255 | None | None |
| faction_name_override_primary_low | False | text | False | 255 | None | None |
| faction_name_override_secondary_high | False | text | False | 255 | None | None |
| faction_name_override_secondary_low | False | text | False | 255 | None | None |
| faction_name_override_victory | False | text | False | 255 | None | None |
| faction_leader_title_override_victory | False | text | False | 255 | None | None |
| secessionist_faction | False | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## faction_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| name_localised | False | text | True | 255 | None | None |
| ui_icon | False | text | True | 255 | None | None |
| effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| description_localised | False | text | True | 255 | None | None |
  
## faction_political_parties_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction_key | False | text | True | 255 | [factions_tables](#factions_tables) | key |
| political_party_key | True | text | True | 255 | [political_parties_tables](#political_parties_tables) | key |
  
## faction_politics_government_actions_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| type | True | text | True | 255 | [politics_government_actions_tables](#politics_government_actions_tables) | key |
| image_path | False | text | True | 255 | None | None |
| title | False | text | True | 255 | None | None |
| description | False | text | True | 255 | None | None |
| cost | False | integer | True | None | None | None |
| cost_per_region | False | integer | True | None | None | None |
| cooldown | False | integer | True | None | None | None |
  
## faction_rebellion_units_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction_key | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| unit_key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
  
## faction_resource_consumptions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| number_of_regions | True | integer | True | None | None | None |
| resource_consumption | False | integer | True | None | None | None |
  
## faction_to_campaign_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## faction_to_faction_groups_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction_key | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| faction_group_key | False | text | True | 255 | [faction_groups_tables](#faction_groups_tables) | key |
  
## faction_to_mercenary_set_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| mercenary_set | True | text | True | 255 | [mercenary_pools_tables](#mercenary_pools_tables) | key |
  
## faction_uniform_colours_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction_name | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| primary_colour_r | False | double | True | None | None | None |
| primary_colour_g | False | double | True | None | None | None |
| primary_colour_b | False | single | True | None | None | None |
| secondary_colour_r | False | single | True | None | None | None |
| secondary_colour_g | False | double | True | None | None | None |
| secondary_colour_b | False | double | True | None | None | None |
| tertiary_colour_r | False | double | True | None | None | None |
| tertiary_colour_g | False | double | True | None | None | None |
| tertiary_colour_b | False | double | True | None | None | None |
  
## faction_variables_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction_variable_key | True | text | True | 20000 | None | None |
| value | False | text | True | 20000 | None | None |
| description | False | text | False | 20000 | None | None |
  
## faction_variables_optional_overrides_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction_variable_key | True | text | True | 20000 | [faction_variables_tables](#faction_variables_tables) | faction_variable_key |
| faction_key | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| campaign_key | True | text | False | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| difficulty_level | True | text | False | 255 | None | None |
| campaign_type | True | text | False | 20000 | None | None |
| value | False | text | True | 20000 | None | None |
  
## fame_levels_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| level | True | integer | True | None | None | None |
| player_prestige | False | integer | True | None | None | None |
| ai_prestige | False | integer | True | None | None | None |
| army_cap | False | integer | True | None | None | None |
| navy_cap | False | integer | True | None | None | None |
| champion_cap | False | integer | True | None | None | None |
| dignitary_cap | False | integer | True | None | None | None |
| spy_cap | False | integer | True | None | None | None |
| province_initiative_cap | False | integer | True | None | None | None |
| campaign | True | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| description_lookup | False | text | False | 255 | [campaign_localised_strings_tables](#campaign_localised_strings_tables) | key |
| effect_bundle | False | text | False | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
  
## family_relationship_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| relationship_type | True | text | True | 255 | None | None |
  
## famous_battle_pools_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| pool_id | True | integer | True | None | None | None |
| pool_posX | False | integer | True | None | None | None |
| pool_posY | False | integer | True | None | None | None |
| pool_radius | False | integer | True | None | None | None |
| battle_name | False | text | True | 50 | None | None |
  
## female_character_culture_details_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| culture | True | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| general | False | text | True | 255 | None | None |
| public_office | False | text | True | 255 | None | None |
| missions | False | text | True | 255 | None | None |
| chance_to_spawn | False | integer | True | None | None | None |
| trait | False | text | False | 255 | [trait_info_tables](#trait_info_tables) | trait |
  
## female_character_faction_details_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| general | False | text | False | 1 | None | None |
| public_office | False | text | False | 1 | None | None |
| missions | False | text | False | 1 | None | None |
| chance_to_spawn | False | integer | True | None | None | None |
| trait | False | text | False | 255 | [trait_info_tables](#trait_info_tables) | trait |
  
## female_character_subculture_details_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| subculture | True | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| general | False | text | False | 255 | None | None |
| public_office | False | text | False | 255 | None | None |
| missions | False | text | False | 255 | None | None |
| chance_to_spawn | False | integer | True | None | None | None |
| trait | False | text | False | 255 | [trait_info_tables](#trait_info_tables) | trait |
  
## first_person_engines_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [gun_types_enum_tables](#gun_types_enum_tables) | key |
| reload_time | False | single | True | None | None | None |
| auto_target | False | yesno | True | None | None | None |
| camera_offset_x | False | single | True | None | None | None |
| camera_offset_y | False | single | True | None | None | None |
| camera_offset_z | False | single | True | None | None | None |
| near_clipping_plane | False | single | True | None | None | None |
| track_projectile_distance | False | single | True | None | None | None |
| half_accuracy_arc | False | single | True | None | None | None |
| half_horizontal_fire_arc | False | single | True | None | None | None |
| half_vertical_fire_arc_elevation | False | single | True | None | None | None |
| turn_delay | False | single | True | None | None | None |
| half_vertical_fire_arc_declination | False | single | True | None | None | None |
  
## fonts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [font_names_tables](#font_names_tables) | font_name |
| size | True | integer | True | None | None | None |
| bold | True | yesno | True | None | None | None |
  
## font_names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| font_name | True | text | True | 255 | None | None |
  
## formations_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| formation | True | text | True | 255 | None | None |
| is_naval | False | yesno | True | None | None | None |
| is_army | False | yesno | True | None | None | None |
| name | False | text | False | 255 | None | None |
| tooltip | False | text | False | 255 | None | None |
| description | False | text | False | 255 | None | None |
| icon_name | False | text | True | 255 | None | None |
| order | False | integer | True | None | None | None |
  
## formations_to_subcultures_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| formation | True | text | True | 255 | [formations_tables](#formations_tables) | formation |
| sub_culture | True | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## forts_to_gun_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| gun_type | True | text | True | 50 | [gun_types_tables](#gun_types_tables) | gun_type |
  
## fort_underlay_climate_jcts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| fort_name | True | text | True | 50 | [battlefield_buildings_tables](#battlefield_buildings_tables) | key |
| climate | True | text | True | 50 | [climates_tables](#climates_tables) | climate_type |
| snow_underlay | True | yesno | True | None | None | None |
| underlay | False | text | True | 50 | [battle_terrain_farms_tables](#battle_terrain_farms_tables) | farm |
  
## frontend_faction_leaders_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| uniform | False | text | True | 2048 | None | None |
| animation | False | text | False | 2048 | None | None |
| x_offset | False | double | False | None | None | None |
| y_offset | False | double | False | None | None | None |
| party | True | text | True | 255 | [political_parties_tables](#political_parties_tables) | key |
  
## game_area_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## genders_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| gender | True | text | True | 50 | None | None |
| onscreen | False | text | True | 50 | None | None |
  
## general_command_star_level_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| command_star_level | True | integer | True | None | None | None |
| alive_morale_bonus | False | integer | True | None | None | None |
| nearby_morale_bonus | False | integer | True | None | None | None |
| melee_attack_bonus | False | integer | True | None | None | None |
| melee_defence_bonus | False | integer | True | None | None | None |
  
## government_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| government_type | True | text | True | 50 | None | None |
| onscreen | False | text | True | 50 | None | None |
| elected_ministers | False | yesno | True | None | None | None |
| hereditary_ministers | False | yesno | True | None | None | None |
| rank | False | integer | True | None | None | None |
| active_upper_class | False | text | True | 50 | [population_classes_tables](#population_classes_tables) | population_class |
| active_lower_class | False | text | True | 50 | [population_classes_tables](#population_classes_tables) | population_class |
  
## government_types_to_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| gov_type | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | integer | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## governorships_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| governorship | True | text | True | 50 | None | None |
| onscreen | False | text | True | 50 | None | None |
  
## ground_condition_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 50 | None | None |
  
## ground_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 50 | None | None |
| enum_value | False | integer | True | None | None | None |
| tooltip | False | text | False | 255 | None | None |
| standard_cursor | False | text | False | 255 | [cursors_tables](#cursors_tables) | key |
| selection_cursor | False | text | False | 255 | [cursors_tables](#cursors_tables) | key |
| penalty_immune_attribute | False | text | True | 255 | [unit_attributes_tables](#unit_attributes_tables) | key |
  
## ground_type_to_stat_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ground_type | True | text | True | 255 | [ground_types_tables](#ground_types_tables) | type |
| affected_stat | True | text | True | 255 | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| multiplier | False | double | True | None | None | None |
  
## groupings_military_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| military_group | True | text | True | 50 | None | None |
  
## gun_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| gun_type | True | text | True | 50 | None | None |
| battle_entity | False | text | True | 50 | [battle_entities_tables](#battle_entities_tables) | key |
| model | False | text | False | 50 | [warscape_animated_tables](#warscape_animated_tables) | key |
| gun_animations_table | False | text | True | 50 | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| equipment_table | False | text | False | 50 | None | None |
| destroyed_model | False | text | False | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| destruction_animation | False | text | False | 50 | [warscape_animated_tables](#warscape_animated_tables) | key |
| engine_type | False | text | False | 255 | [gun_types_enum_tables](#gun_types_enum_tables) | key |
| gun_mount_entity | False | text | False | 50 | [battle_entities_tables](#battle_entities_tables) | key |
  
## gun_types_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## gun_type_muzzle_flash_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## gun_type_to_projectiles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| gun_type | True | text | True | 50 | [gun_types_tables](#gun_types_tables) | gun_type |
| shot_type | True | text | True | 50 | [projectiles_tables](#projectiles_tables) | key |
| muzzle_flash | False | text | True | 50 | [gun_type_muzzle_flash_enum_tables](#gun_type_muzzle_flash_enum_tables) | key |
  
## historical_battles_ui_locations_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [battles_tables](#battles_tables) | key |
| x | False | integer | True | None | None | None |
| y | False | integer | True | None | None | None |
| height_percent | False | integer | True | None | None | None |
  
## historical_characters_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| on_screen_name | False | text | True | 255 | None | None |
| nobility | False | yesno | True | None | None | None |
| gender | False | text | True | 50 | [genders_tables](#genders_tables) | gender |
| agent_type | False | text | True | 255 | [agents_tables](#agents_tables) | key |
| faction | False | text | True | 255 | [factions_tables](#factions_tables) | key |
| spawning_window_start | False | integer | True | None | None | None |
| spawning_window_end | False | integer | True | None | None | None |
| spawn_conditions | False | text | True | 536870910 | None | None |
| name_key | False | integer | True | None | [names_tables](#names_tables) | id |
| surname_key | False | integer | False | None | [names_tables](#names_tables) | id |
| art_set_id | False | text | False | 255 | [campaign_character_art_sets_tables](#campaign_character_art_sets_tables) | art_set_id |
| clan_name_key | False | integer | False | None | [names_tables](#names_tables) | id |
| other_name_key | False | integer | False | None | [names_tables](#names_tables) | id |
| political_party | False | text | False | 255 | [political_parties_tables](#political_parties_tables) | key |
| age_start | False | integer | True | None | None | None |
  
## historical_character_traits_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| character | True | text | True | 50 | [historical_characters_tables](#historical_characters_tables) | key |
| trait | True | text | True | 50 | [character_trait_levels_tables](#character_trait_levels_tables) | key |
  
## honour_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 1024 | None | None |
| factor | False | text | True | 1024 | [honour_factors_tables](#honour_factors_tables) | key |
| value | False | integer | True | None | None | None |
| applies_to_ai | False | yesno | True | None | None | None |
  
## honour_factors_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 1024 | None | None |
| minimum_value | False | integer | True | None | None | None |
| maximum_value | False | integer | True | None | None | None |
| localised_negative_name | False | text | True | 1024 | None | None |
| localised_positive_name | False | text | True | 1024 | None | None |
  
## imposter_sharing_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 2048 | None | None |
  
## incidents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| ui_image | False | text | True | 255 | None | None |
| ui_icon | False | text | True | 255 | None | None |
| generate | False | yesno | True | None | None | None |
| prioritised | False | yesno | True | None | None | None |
| localised_title | False | text | True | 20000 | None | None |
| localised_description | False | text | True | 200000 | None | None |
  
## land_units_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| onscreen_name | False | text | True | 20000 | None | None |
| category | False | text | True | 50 | [unit_category_tables](#unit_category_tables) | key |
| class | False | text | True | 50 | [unit_class_tables](#unit_class_tables) | key |
| short_description_text | False | text | True | 255 | [unit_description_short_texts_tables](#unit_description_short_texts_tables) | key |
| historical_description_text | False | text | True | 255 | [unit_description_historical_texts_tables](#unit_description_historical_texts_tables) | key |
| strengths_weaknesses_text | False | text | True | 255 | [unit_description_strengths_weaknesses_texts_tables](#unit_description_strengths_weaknesses_texts_tables) | key |
| campaign_action_points | False | integer | True | None | None | None |
| supports_first_person | False | yesno | True | None | None | None |
| man_entity | False | text | True | 50 | [battle_entities_tables](#battle_entities_tables) | key |
| man_animation | False | text | False | 50 | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| num_mounts | False | integer | True | None | None | None |
| mount | False | text | False | 50 | [mounts_tables](#mounts_tables) | key |
| num_animals | False | integer | True | None | None | None |
| animal | False | text | False | 255 | [animals_tables](#animals_tables) | key |
| spacing | False | text | True | 255 | [unit_spacings_tables](#unit_spacings_tables) | key |
| rank_depth | False | integer | True | None | None | None |
| morale | False | integer | True | None | None | None |
| bonus_hit_points | False | integer | True | None | None | None |
| training_level | False | text | True | 50 | [unit_training_level_enum_tables](#unit_training_level_enum_tables) | key |
| armour | False | text | True | 255 | [unit_armour_types_tables](#unit_armour_types_tables) | key |
| shield | False | text | True | 255 | [unit_shield_types_tables](#unit_shield_types_tables) | key |
| primary_missile_weapon | False | text | False | 255 | [missile_weapons_tables](#missile_weapons_tables) | key |
| accuracy | False | integer | True | None | None | None |
| ammo | False | integer | True | None | None | None |
| primary_melee_weapon | False | text | True | 255 | [melee_weapons_tables](#melee_weapons_tables) | key |
| melee_attack | False | integer | True | None | None | None |
| charge_bonus | False | integer | True | None | None | None |
| melee_defence | False | integer | True | None | None | None |
| dismounted_melee_attack | False | integer | True | None | None | None |
| dismounted_charge_bonus | False | integer | True | None | None | None |
| dismounted_melee_defence | False | integer | True | None | None | None |
| num_guns | False | integer | True | None | None | None |
| officers | False | text | True | 255 | [land_units_officers_tables](#land_units_officers_tables) | key |
| engine | False | text | False | 255 | [battlefield_engines_tables](#battlefield_engines_tables) | key |
| articulated_record | False | text | False | 255 | [land_unit_articulated_vehicles_tables](#land_unit_articulated_vehicles_tables) | key |
| is_male | False | yesno | True | None | None | None |
| visibility_spotting_range_min | False | single | True | None | None | None |
| visibility_spotting_range_max | False | single | True | None | None | None |
| ability_global_recharge | False | double | True | None | None | None |
| attribute_group | False | text | False | 255 | [unit_attributes_groups_tables](#unit_attributes_groups_tables) | group_name |
| spot_dist_tree | False | double | True | None | None | None |
| spot_dist_scrub | False | double | True | None | None | None |
| chariot | False | text | False | 255 | [battlefield_chariots_tables](#battlefield_chariots_tables) | key |
| num_chariots | False | integer | True | None | None | None |
| reload | False | integer | True | None | None | None |
| loose_spacing | False | yesno | True | None | None | None |
| spotting_and_hiding | False | text | False | 255 | [spotting_and_hiding_values_tables](#spotting_and_hiding_values_tables) | key |
| selection_vo | False | text | True | 255 | [audio_vo_selected_switches_tables](#audio_vo_selected_switches_tables) | key |
| selected_vo_secondary | False | text | True | 255 | [audio_vo_selected_switches_tables](#audio_vo_selected_switches_tables) | key |
| selected_vo_tertiary | False | text | True | 255 | [audio_vo_selected_switches_tables](#audio_vo_selected_switches_tables) | key |
| hiding_scalar | False | double | True | None | None | None |
  
## land_units_officers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| officer_1 | False | text | False | 50 | [battle_personalities_tables](#battle_personalities_tables) | key |
| officer_2 | False | text | False | 50 | [battle_personalities_tables](#battle_personalities_tables) | key |
| standard_bearer_1 | False | text | False | 50 | [battle_personalities_tables](#battle_personalities_tables) | key |
| standard_bearer_2 | False | text | False | 50 | [battle_personalities_tables](#battle_personalities_tables) | key |
| musician_1 | False | text | False | 50 | [battle_personalities_tables](#battle_personalities_tables) | key |
| musician_2 | False | text | False | 50 | [battle_personalities_tables](#battle_personalities_tables) | key |
| personality_location | False | text | False | 255 | [personality_location_enums_tables](#personality_location_enums_tables) | key |
  
## land_units_to_unit_abilites_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| land_unit | True | text | True | 255 | [land_units_tables](#land_units_tables) | key |
| ability | True | text | True | 50 | [unit_abilities_tables](#unit_abilities_tables) | key |
  
## land_unit_articulated_vehicles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| articulated_entity | False | text | False | 50 | [battle_entities_tables](#battle_entities_tables) | key |
| ammo_caisson_entity | False | text | False | 50 | [battle_entities_tables](#battle_entities_tables) | key |
| ammo_caisson_model | False | text | False | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
| ammo_caisson_destroyed_model | False | text | False | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| ammo_caisson_destruction | False | text | True | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
  
## languages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| full_name | False | text | True | 255 | None | None |
  
## lighting_setups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name | True | text | True | 50 | None | None |
| depth_bias | False | double | True | None | None | None |
| dirx | False | double | True | None | None | None |
| diry | False | double | True | None | None | None |
| dirz | False | double | True | None | None | None |
| colour_scale | False | double | True | None | None | None |
| colour_r | False | double | True | None | None | None |
| colour_g | False | double | True | None | None | None |
| colour_b | False | double | True | None | None | None |
| colour_top_r | False | double | True | None | None | None |
| colour_top_g | False | double | True | None | None | None |
| colour_top_b | False | double | True | None | None | None |
| colour_bottom_r | False | double | True | None | None | None |
| colour_bottom_g | False | double | True | None | None | None |
| colour_bottom_b | False | double | True | None | None | None |
| gamma | False | double | True | None | None | None |
| bloom_multiplier | False | double | True | None | None | None |
| bloom_angle_1 | False | double | True | None | None | None |
| bloom_angle_2 | False | double | True | None | None | None |
| bloom_scale_1 | False | double | True | None | None | None |
| bloom_scale_2 | False | double | True | None | None | None |
| main_bloom_scalex | False | double | True | None | None | None |
| main_bloom_scaley | False | double | True | None | None | None |
| main_bloom_distribution | False | double | True | None | None | None |
| high_pass | False | double | False | None | None | None |
| colour_fog_r | False | double | True | None | None | None |
| colour_fog_g | False | double | True | None | None | None |
| colour_fog_b | False | double | True | None | None | None |
| fog_near | False | double | True | None | None | None |
| fog_far | False | double | True | None | None | None |
| fog_density | False | double | True | None | None | None |
  
## loyalty_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 1024 | None | None |
| factor | False | text | True | 1024 | [loyalty_factors_tables](#loyalty_factors_tables) | key |
| value | False | integer | True | None | None | None |
| applies_to_ai | False | yesno | True | None | None | None |
  
## loyalty_factors_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 1024 | None | None |
| minimum_value | False | integer | True | None | None | None |
| maximum_value | False | integer | True | None | None | None |
| localised_negative_name | False | text | True | 1024 | None | None |
| localised_positive_name | False | text | True | 1024 | None | None |
  
## main_units_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit | True | text | True | 255 | None | None |
| land_unit | False | text | True | 255 | [land_units_tables](#land_units_tables) | key |
| num_men | False | integer | True | None | None | None |
| naval_unit | False | text | False | 255 | [naval_units_tables](#naval_units_tables) | key |
| num_ships | False | integer | True | None | None | None |
| min_men_per_ship | False | integer | True | None | None | None |
| max_men_per_ship | False | integer | True | None | None | None |
| is_naval | False | yesno | True | None | None | None |
| weight | False | text | False | 255 | [unit_weights_tables](#unit_weights_tables) | key |
| recruitment_cost | False | integer | True | None | None | None |
| upkeep_cost | False | integer | True | None | None | None |
| create_time | False | integer | True | None | None | None |
| campaign_cap | False | integer | True | None | None | None |
| multiplayer_cost | False | integer | True | None | None | None |
| multiplayer_cap | False | integer | True | None | None | None |
| caste | False | text | True | 255 | [unit_castes_tables](#unit_castes_tables) | caste |
| prestige | False | integer | True | None | None | None |
| additional_building_requirement | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| religion_requirement | False | text | False | 50 | [religions_tables](#religions_tables) | religion_key |
| recruitment_movie | False | text | False | 255 | None | None |
| campaign_total_cap | False | integer | True | None | None | None |
| resource_requirement | False | text | False | 50 | [resources_tables](#resources_tables) | key |
| world_leader_only | False | yesno | True | None | None | None |
| can_trade | False | yesno | True | None | None | None |
| special_edition_mask | False | integer | True | None | None | None |
| unique_index | False | autonumber | True | None | None | None |
| in_encyclopedia | False | yesno | True | None | None | None |
| region_unit_resource_requirement | False | text | False | 255 | [region_unit_resources_tables](#region_unit_resources_tables) | key |
| audio_language | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| audio_vo_actor_group | False | text | False | 255 | [audio_vo_actor_groups_tables](#audio_vo_actor_groups_tables) | key |
  
## marriage_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## melee_weapons_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| damage | False | integer | True | None | None | None |
| ap_damage | False | integer | True | None | None | None |
| first_strike | False | integer | True | None | None | None |
| bonus_v_infantry | False | integer | True | None | None | None |
| bonus_v_cavalry | False | integer | True | None | None | None |
| bonus_v_elephants | False | integer | True | None | None | None |
| armour_piercing | False | yesno | True | None | None | None |
| shield_piercing | False | yesno | True | None | None | None |
| armour_penetrating | False | yesno | True | None | None | None |
| weapon_length | False | decimal | True | None | None | None |
| melee_weapon_type | False | text | True | 50 | [unit_melee_weapons_enum_tables](#unit_melee_weapons_enum_tables) | key |
| audio_material | False | text | True | 255 | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
  
## mercenary_pools_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## mercenary_pool_modifiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| pool_type | False | text | True | 20000 | [mercenary_pool_type_enums_tables](#mercenary_pool_type_enums_tables) | pool_type |
| culture_origin_match | False | yesno | True | None | None | None |
| min_pool_culture_percentage | False | integer | True | None | None | None |
| replenishment_modifier | False | single | True | None | None | None |
| cost_modifier | False | single | True | None | None | None |
| key | True | autonumber | True | None | None | None |
  
## mercenary_pool_to_groups_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| pool | False | text | True | 255 | [mercenary_pools_tables](#mercenary_pools_tables) | key |
| group | False | text | True | 20000 | [mercenary_unit_groups_tables](#mercenary_unit_groups_tables) | key |
| initial_unit_count | False | integer | True | None | None | None |
| faction_requirement | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| subculture_requirement | False | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| tech_requirement | False | text | False | 255 | [technologies_tables](#technologies_tables) | key |
  
## mercenary_pool_type_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| pool_type | True | text | True | 20000 | None | None |
  
## mercenary_unit_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 20000 | None | None |
| unit_record | False | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| max_count | False | integer | True | None | None | None |
| max_replenish_per_turn | False | integer | True | None | None | None |
| chance_to_replenish | False | single | True | None | None | None |
  
## message_events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| event | True | text | True | 255 | None | None |
| layout | False | text | True | 255 | [message_event_layout_types_tables](#message_event_layout_types_tables) | Type |
| requires_response | False | yesno | True | None | None | None |
| instant_open | False | yesno | True | None | None | None |
| priority | False | integer | True | None | None | None |
  
## message_event_layout_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| Type | True | text | False | 255 | None | None |
  
## message_event_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| event | True | text | True | 255 | [message_events_tables](#message_events_tables) | event |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| title | False | text | True | 50 | None | None |
| text | False | text | True | 50 | [message_event_text_tables](#message_event_text_tables) | key |
| image | False | text | False | 200 | None | None |
| icon | False | text | False | 255 | None | None |
| sound_event | False | text | False | 255 | None | None |
| optional_campaign_key | True | text | False | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| optional_subculture | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## message_event_text_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| text | False | text | True | 536870910 | None | None |
  
## military_force_legacy_emblems_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| is_army | False | yesno | True | None | None | None |
| faction_key | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| culure_key | False | text | False | 255 | [cultures_tables](#cultures_tables) | key |
| subculture_key | False | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| icon | False | text | True | 255 | None | None |
| banner_decorator | False | text | True | 255 | None | None |
  
## military_force_legacy_names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| subculture | True | text | False | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| localised_name | False | text | True | 255 | None | None |
| for_army | False | yesno | True | None | None | None |
| campaign | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## ministerial_effectiveness_modifiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| leader_minister_level | True | integer | True | None | None | None |
| government_type | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| effectiveness_bonus | False | integer | True | None | None | None |
  
## ministerial_positions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| minister_key | True | text | True | 50 | None | None |
| rank | False | integer | True | None | None | None |
  
## ministerial_positions_by_gov_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction | True | text | True | 50 | [factions_tables](#factions_tables) | key |
| minister_key | True | text | True | 50 | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| government_type | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| gender | True | text | True | 50 | [genders_tables](#genders_tables) | gender |
| string | False | text | False | 50 | [ministerial_positions_strings_tables](#ministerial_positions_strings_tables) | key |
| loyalty_gained | False | integer | True | None | None | None |
| loyalty_on_loss | False | integer | True | None | None | None |
  
## ministerial_positions_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 255 | None | None |
| on_screen | False | text | False | 255 | None | None |
  
## ministerial_positions_switching_loyalty_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| position_from | True | text | True | 50 | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| position_to | True | text | True | 50 | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| loyalty_gained | False | integer | True | None | None | None |
  
## ministerial_positions_to_character_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| position | True | text | True | 50 | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| minister_level | True | integer | True | None | None | None |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | integer | True | None | None | None |
| ui_id | False | integer | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## ministerial_positions_to_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| position | True | text | True | 50 | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| minister_level | True | integer | True | None | None | None |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | integer | True | None | None | None |
| ui_id | False | integer | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## ministerial_positions_to_governorships_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ministerial_position | True | text | True | 50 | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| governorship | True | text | True | 50 | [governorships_tables](#governorships_tables) | governorship |
  
## ministerial_position_default_names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ministerial_position | True | text | True | 50 | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| gov_type | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| default_name | False | text | True | 50 | None | None |
  
## missile_weapons_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| precursor | False | yesno | True | None | None | None |
| default_projectile | False | text | True | 255 | [projectiles_tables](#projectiles_tables) | key |
| can_fire_at_buildings | False | yesno | True | None | None | None |
  
## missile_weapons_to_projectiles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| missile_weapon | True | text | True | 255 | [missile_weapons_tables](#missile_weapons_tables) | key |
| projectile | True | text | True | 255 | [projectiles_tables](#projectiles_tables) | key |
  
## missions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| mission_type | False | text | True | 255 | None | None |
| localised_title | False | text | True | 255 | None | None |
| localised_description | False | text | True | 65535 | None | None |
| ui_image | False | text | True | 255 | None | None |
| ui_icon | False | text | True | 255 | None | None |
| generate | False | yesno | True | None | None | None |
| prioritised | False | yesno | True | None | None | None |
  
## mission_issuers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| issuer_key | True | text | True | 255 | None | None |
  
## mission_text_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 50 | None | None |
| text | False | text | False | 536870910 | None | None |
  
## mission_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## models_artillery_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| model_file | False | text | True | 255 | None | None |
| logic_file | False | text | True | 255 | None | None |
  
## models_building_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| model_file | False | text | True | 255 | None | None |
| logic_file | False | text | True | 255 | None | None |
| display_path | False | text | False | 20000 | None | None |
  
## models_deployables_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| model_file | False | text | True | 255 | None | None |
| logic_file | False | text | True | 255 | None | None |
| display_path | False | text | False | 20000 | None | None |
  
## models_entity_weapons_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| model_file | False | text | True | 255 | None | None |
| logic_file | False | text | True | 255 | None | None |
  
## models_foot_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## models_mount_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## models_naval_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| logic_folder | False | text | False | 255 | None | None |
| rigging_file | False | text | False | 255 | None | None |
| destruction_file | False | text | False | 255 | None | None |
| display_folder | False | text | True | 255 | None | None |
| oar_upper | False | text | True | 255 | [models_oars_tables](#models_oars_tables) | key |
| oar_middle | False | text | True | 255 | [models_oars_tables](#models_oars_tables) | key |
| oar_lower | False | text | True | 255 | [models_oars_tables](#models_oars_tables) | key |
| selection_indicator_shape | False | text | True | 255 | None | None |
  
## models_oars_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| rigid_model | False | text | False | 255 | None | None |
| left_row | False | text | False | 255 | None | None |
| left_end | False | text | False | 255 | None | None |
| right_row | False | text | False | 255 | None | None |
| right_end | False | text | False | 255 | None | None |
  
## models_sieges_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| model_file | False | text | True | 255 | None | None |
| logic_file | False | text | True | 255 | None | None |
| display_path | False | text | False | 20000 | None | None |
  
## mountable_artillery_units_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
  
## mountable_artillery_units_custom_battles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| mountable_artillery | True | text | True | 255 | [mountable_artillery_units_tables](#mountable_artillery_units_tables) | unit_key |
| cap | False | integer | True | None | None | None |
| probability | False | integer | True | None | None | None |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## mounts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| animation | False | text | True | 50 | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| entity | False | text | True | 50 | [battle_entities_tables](#battle_entities_tables) | key |
| mount_armour | False | integer | True | None | None | None |
| variant | False | text | True | 255 | [variants_tables](#variants_tables) | variant_name |
| audio_armour_type | False | text | True | 255 | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
  
## mount_variants_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| mount_key | False | text | True | 50 | [mounts_tables](#mounts_tables) | key |
| display_key | False | text | True | 255 | None | None |
| weight | False | double | True | None | None | None |
  
## movement_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 50 | None | None |
  
## movie_event_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| event | True | text | True | 50 | None | None |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| title | False | text | False | 255 | None | None |
| movie | False | text | True | 50 | None | None |
| id | False | autonumber | False | None | None | None |
  
## mp_budgets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| budget_size_key | False | text | True | 255 | [mp_budget_sizes_tables](#mp_budget_sizes_tables) | key |
| land | False | yesno | True | None | None | None |
| siege_defender | False | yesno | True | None | None | None |
| budget | False | integer | True | None | None | None |
  
## mp_budget_sizes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## mp_force_gen_templates_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## mp_force_gen_template_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| template_key | True | text | True | 255 | [mp_force_gen_templates_tables](#mp_force_gen_templates_tables) | key |
| budget_key | True | text | True | 255 | [mp_budgets_tables](#mp_budgets_tables) | key |
| priority | False | integer | True | None | None | None |
| general_pct | False | single | True | None | None | None |
| units_pct | False | single | True | None | None | None |
| upgrade_pct | False | single | True | None | None | None |
| config_key | False | text | True | 255 | [cdir_military_generator_configs_tables](#cdir_military_generator_configs_tables) | key |
| is_defender | True | yesno | True | None | None | None |
  
## multiplayer_mininum_length_funds_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| value | False | double | True | None | None | None |
| description | False | text | True | 255 | None | None |
  
## names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| names_group | False | integer | True | None | [names_groups_tables](#names_groups_tables) | key |
| name | False | text | True | 50 | None | None |
| type | False | text | True | 50 | [name_types_tables](#name_types_tables) | key |
| gender | False | text | True | 255 | [genders_tables](#genders_tables) | gender |
| frequency | False | integer | True | None | None | None |
| nobility | False | yesno | True | None | None | None |
| id | True | autonumber | True | None | None | None |
  
## names_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ID | False | text | True | 50 | None | None |
| Description | False | text | True | 50 | None | None |
| key | True | autonumber | True | None | None | None |
  
## names_titles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name_group | True | integer | True | None | [names_groups_tables](#names_groups_tables) | key |
| title | True | text | True | 50 | None | None |
| gender | False | text | True | 50 | [genders_tables](#genders_tables) | gender |
| rank | False | integer | True | None | None | None |
  
## names_titles_by_agent_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent_type | True | text | True | 50 | [agents_tables](#agents_tables) | key |
| highest_title | False | integer | True | None | None | None |
  
## name_orders_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 50 | [name_types_tables](#name_types_tables) | key |
| order | True | integer | True | None | None | None |
| name_group | True | integer | True | None | [names_groups_tables](#names_groups_tables) | key |
  
## name_order_overrides_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 50 | [name_types_tables](#name_types_tables) | key |
| order | True | integer | True | None | None | None |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## name_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## naval_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| effect_name | False | text | False | 255 | [particle_effects_tables](#particle_effects_tables) | key |
  
## naval_fire_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| incendiary_level | True | text | True | 255 | [projectile_incendiary_enum_tables](#projectile_incendiary_enum_tables) | key |
| unit_category | True | text | True | 255 | [unit_category_tables](#unit_category_tables) | key |
| chance_of_fire | False | decimal | True | None | None | None |
  
## naval_oar_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## naval_ramming_events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| ramming_ship | False | text | True | 255 | [unit_category_tables](#unit_category_tables) | key |
| rammed_ship | False | text | True | 255 | [unit_category_tables](#unit_category_tables) | key |
| base_damage | False | integer | True | None | None | None |
  
## naval_units_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| onscreen_name | False | text | True | 20000 | None | None |
| category | False | text | True | 50 | [unit_category_tables](#unit_category_tables) | key |
| class | False | text | True | 50 | [unit_class_tables](#unit_class_tables) | key |
| short_description_text | False | text | True | 255 | [unit_description_short_texts_tables](#unit_description_short_texts_tables) | key |
| historical_description_text | False | text | True | 255 | [unit_description_historical_texts_tables](#unit_description_historical_texts_tables) | key |
| strengths_weaknesses_text | False | text | True | 255 | [unit_description_strengths_weaknesses_texts_tables](#unit_description_strengths_weaknesses_texts_tables) | key |
| campaign_action_points | False | integer | True | None | None | None |
| unit_type_icon | False | text | False | 255 | None | None |
| supports_first_person | False | yesno | True | None | None | None |
| ship | False | text | True | 255 | [ship_dbs_tables](#ship_dbs_tables) | key |
| primary_naval_weapon | False | text | False | 255 | [naval_weapons_tables](#naval_weapons_tables) | key |
| secondary_naval_weapon | False | text | False | 255 | [naval_weapons_tables](#naval_weapons_tables) | key |
| rank_depth | False | integer | True | None | None | None |
| attribute_groups | False | text | False | 255 | [unit_attributes_groups_tables](#unit_attributes_groups_tables) | group_name |
| can_board | False | yesno | True | None | None | None |
| can_ram | False | yesno | True | None | None | None |
| unit_card | False | text | True | 255 | None | None |
| is_composite | False | yesno | True | None | None | None |
| ignition_threshold | False | integer | True | None | None | None |
  
## naval_units_to_unit_abilites_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| naval_unit | True | text | True | 255 | [naval_units_tables](#naval_units_tables) | key |
| ability | True | text | True | 50 | [unit_abilities_tables](#unit_abilities_tables) | key |
  
## naval_weapons_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| type | False | text | True | 255 | [naval_weapons_enums_tables](#naval_weapons_enums_tables) | types |
| autonomous_engine | False | text | False | 255 | [battlefield_engines_autonomous_tables](#battlefield_engines_autonomous_tables) | key |
| models_entity_weaponry | False | text | False | 255 | [models_entity_weapons_tables](#models_entity_weapons_tables) | key |
  
## naval_weapons_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| types | True | text | True | 255 | None | None |
  
## particle_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## pdlc_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ID | True | text | True | 255 | None | None |
| SteamID | False | integer | True | None | None | None |
| description | False | text | False | 536870910 | None | None |
| release_order | False | integer | True | None | None | None |
  
## personality_location_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## plagues_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name | True | text | True | 255 | None | None |
| grade | False | integer | True | None | None | None |
| minimum_squalor | False | integer | True | None | None | None |
| infectivity | False | integer | True | None | None | None |
| lifetime | False | integer | True | None | None | None |
| region_effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| military_force_effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
  
## plagues_permitted_campaigns_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| plague | True | text | True | 255 | [plagues_tables](#plagues_tables) | name |
| campaign | True | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## political_actions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| political_action_key | True | text | True | 255 | None | None |
| onscreen_name | False | text | True | 255 | None | None |
| icon_file_path | False | text | False | 255 | None | None |
| usage_cost_multiplier | False | double | True | None | None | None |
  
## political_actions_dilemma_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| politiical_action | True | text | True | 255 | [political_actions_tables](#political_actions_tables) | political_action_key |
| dilemma | True | text | True | 255 | [dilemmas_tables](#dilemmas_tables) | key |
| weighting | True | integer | True | None | None | None |
  
## political_actions_effect_bundles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| action | True | text | True | 255 | None | None |
| effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| duration | False | integer | True | None | None | None |
  
## political_actions_incidents_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| political_action | True | text | True | 255 | [political_actions_tables](#political_actions_tables) | political_action_key |
| incident | True | text | True | 255 | [incidents_tables](#incidents_tables) | key |
| weighting | True | integer | True | None | None | None |
  
## political_actions_mission_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| political_action | True | text | True | 255 | [political_actions_tables](#political_actions_tables) | political_action_key |
| mission | True | text | True | 255 | [missions_tables](#missions_tables) | key |
| weighting | True | integer | True | None | None | None |
  
## political_parties_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| name_localised | False | text | True | 255 | None | None |
| playable | False | yesno | True | None | None | None |
| associated_surname | False | text | False | 255 | None | None |
| ui_icon | False | text | True | 255 | None | None |
| effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| description_localised | False | text | True | 255 | None | None |
| initial_power | False | integer | True | None | None | None |
| r | False | double | True | None | None | None |
| g | False | double | True | None | None | None |
| b | False | double | True | None | None | None |
| trait1 | False | text | False | 255 | [political_traits_tables](#political_traits_tables) | key |
| trait2 | False | text | False | 255 | [political_traits_tables](#political_traits_tables) | key |
  
## political_parties_loyalty_effect_bundles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| loyalty | True | integer | True | None | None | None |
| bundle_key | True | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
  
## political_parties_power_effect_bundles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| political_party_key | True | text | True | 255 | [political_parties_tables](#political_parties_tables) | key |
| effect_bundle | True | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| power_level | False | integer | True | None | None | None |
  
## political_traits_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| onscreen_name | False | text | True | 255 | None | None |
| description | False | text | False | 255 | None | None |
  
## political_triggers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| trigger | True | text | True | 50 | None | None |
| event | False | text | True | 50 | [trigger_events_tables](#trigger_events_tables) | event |
| conditions | False | text | True | 536870910 | None | None |
  
## politics_government_actions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## politics_government_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| government_type | True | text | True | 255 | None | None |
  
## politics_government_type_political_action_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| government_type | True | text | True | 255 | [politics_government_types_tables](#politics_government_types_tables) | government_type |
| political_action | True | text | True | 255 | [political_actions_tables](#political_actions_tables) | political_action_key |
| is_available_for_faction_leader | False | yesno | True | None | None | None |
| is_available_for_non_ruling_party_leaders | False | yesno | True | None | None | None |
| is_available_for_ruling_party_members | False | yesno | True | None | None | None |
| is_available_for_non_ruling_party_members | False | yesno | True | None | None | None |
  
## population_classes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| population_class | True | text | True | 50 | None | None |
| riots | False | yesno | True | None | None | None |
| demands | False | yesno | True | None | None | None |
| spawn_rebel_general | False | yesno | True | None | None | None |
| onscreen_name | False | text | False | 50 | None | None |
  
## portrait_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## preset_colours_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| Key | True | text | True | 255 | None | None |
| red | False | double | True | None | None | None |
| green | False | double | True | None | None | None |
| blue | False | double | True | None | None | None |
  
## pre_battle_speeches_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| text | False | text | True | 536870910 | None | None |
| type | False | integer | True | None | [pre_battle_speech_types_enum_tables](#pre_battle_speech_types_enum_tables) | index |
| parameter | False | text | True | 255 | [pre_battle_speech_parameters_enum_tables](#pre_battle_speech_parameters_enum_tables) | key |
  
## pre_battle_speech_parameters_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## pre_battle_speech_types_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| index | True | integer | True | None | None | None |
| description | False | text | True | 255 | None | None |
  
## projectiles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| category | False | text | True | 50 | [projectile_category_enum_tables](#projectile_category_enum_tables) | key |
| shot_type | False | text | True | 50 | [projectile_shot_type_enum_tables](#projectile_shot_type_enum_tables) | key |
| explosion_type | False | text | False | 50 | [projectiles_explosions_tables](#projectiles_explosions_tables) | key |
| high_air_resistance | False | yesno | False | None | None | None |
| spin_type | False | text | True | 50 | None | None |
| projectile_number | False | integer | False | None | None | None |
| trajectory_sight | False | text | True | 50 | [projectile_trajectory_sight_enum_tables](#projectile_trajectory_sight_enum_tables) | key |
| effective_range | False | integer | True | None | None | None |
| minimum_range | False | integer | True | None | None | None |
| max_elevation | False | integer | True | None | None | None |
| muzzle_velocity | False | single | True | None | None | None |
| marksmanship_bonus | False | integer | True | None | None | None |
| spread | False | double | True | None | None | None |
| damage | False | integer | True | None | None | None |
| ap_damage | False | integer | True | None | None | None |
| penetration | False | text | False | 255 | [projectile_penetration_enum_tables](#projectile_penetration_enum_tables) | key |
| incendiary | False | text | False | 255 | [projectile_incendiary_enum_tables](#projectile_incendiary_enum_tables) | key |
| can_bounce | False | yesno | True | None | None | None |
| collision_radius | False | double | True | None | None | None |
| base_reload_time | False | integer | True | None | None | None |
| below_waterline_damage_modifer | False | single | True | None | None | None |
| calibration_distance | False | single | True | None | None | None |
| calibration_area | False | single | True | None | None | None |
| bonus_v_infantry | False | integer | True | None | None | None |
| bonus_v_cavalry | False | integer | True | None | None | None |
| bonus_v_elephant | False | integer | True | None | None | None |
| projectile_display | False | text | False | 255 | [projectile_displays_tables](#projectile_displays_tables) | key |
| overhead_stat_effect | False | text | False | 255 | [special_ability_phases_tables](#special_ability_phases_tables) | id |
| contact_stat_effect | False | text | False | 255 | [special_ability_phases_tables](#special_ability_phases_tables) | id |
| projectile_audio | False | text | True | 255 | [audio_projectiles_tables](#audio_projectiles_tables) | key |
| shockwave_radius | False | single | True | None | None | None |
| can_damage_buildings | False | yesno | True | None | None | None |
| is_grapple | False | yesno | True | None | None | None |
  
## projectiles_detonation_types_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## projectiles_detonator_types_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| detonator_type | True | text | True | 50 | None | None |
  
## projectiles_explosions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| detonator_type | False | text | True | 50 | [projectiles_detonator_types_enum_tables](#projectiles_detonator_types_enum_tables) | detonator_type |
| detonation_type | False | text | True | 50 | [projectiles_detonation_types_enum_tables](#projectiles_detonation_types_enum_tables) | key |
| detonation_radius | False | integer | True | None | None | None |
| detonation_duration | False | single | True | None | None | None |
| detonation_speed | False | integer | True | None | None | None |
| detonation_damage | False | single | True | None | None | None |
| projectile_name | False | text | False | 50 | [projectiles_tables](#projectiles_tables) | key |
| projectile_amount | False | integer | True | None | None | None |
| explosion_particle_effect | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| distance_from_target | False | integer | True | None | None | None |
| error_margin | False | double | True | None | None | None |
| non_lethal_detonation | False | yesno | False | None | None | None |
| explosion_particle_effect_on_ground | False | text | False | 50 | None | None |
| audio_explosion_type | False | text | True | 255 | [audio_explosions_enums_tables](#audio_explosions_enums_tables) | key |
  
## projectiles_spin_type_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## projectile_category_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## projectile_displays_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| display_model | False | text | False | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| damaged_display_model | False | text | False | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| launch_fx | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| trail_fx | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| stationary_fx | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| impact | False | text | False | 50 | [projectile_impacts_tables](#projectile_impacts_tables) | key |
| skeleton | False | text | False | 255 | None | None |
| airborne_anim | False | text | False | 255 | None | None |
| landing_anim | False | text | False | 255 | None | None |
  
## projectile_gun_types_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| gun_type | True | text | True | 50 | None | None |
  
## projectile_impacts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| water | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| sails | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| mud | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| grass | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| road | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| rock | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| sand | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| cloth | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| snow | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| leather | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| wood | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| foliage | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| glass | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| size | False | text | True | 50 | None | None |
| blood | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| metal | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
  
## projectile_incendiary_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## projectile_penetration_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## projectile_shot_type_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| requires_effect_enabling | False | yesno | False | None | None | None |
| supersedes_shot_type | False | text | False | 255 | None | None |
| button_tooltip_text | False | text | True | 20000 | None | None |
  
## projectile_trajectory_sight_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## prologue_chapters_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| number | True | integer | True | None | None | None |
| title | False | text | True | 255 | None | None |
| description | False | text | False | 1000 | None | None |
| is_battle | False | yesno | True | None | None | None |
| battle_key | False | text | False | 255 | [battles_tables](#battles_tables) | key |
| campaign_key | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| subtitle | False | text | False | 255 | None | None |
| banner | False | text | False | 255 | None | None |
  
## prologue_loading_screens_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| index | True | autonumber | True | None | None | None |
| title | False | text | True | 255 | None | None |
| main_text | False | text | True | 1000 | None | None |
| inset_image | False | text | True | 255 | None | None |
| background_image | False | text | True | 255 | None | None |
| pane_on_left | False | yesno | True | None | None | None |
| campaign | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## provinces_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| onscreen | False | text | True | 20000 | None | None |
  
## province_to_mercenary_set_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| province | True | text | True | 255 | [provinces_tables](#provinces_tables) | key |
| mercenary_set | True | text | True | 255 | [mercenary_pools_tables](#mercenary_pools_tables) | key |
| optional_campaign_key | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## provincial_initiatives_to_subculture_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| provincial_initiative_key | True | text | True | 255 | [provincial_initiative_records_tables](#provincial_initiative_records_tables) | key |
| subculture | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## provincial_initiative_records_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| localised_name | False | text | True | 255 | None | None |
| effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| order | False | integer | True | None | None | None |
| icon_path | False | text | True | 255 | None | None |
| campaign_vfx_id | False | text | False | 255 | [campaign_vfx_campaign_vfx_event_ids_tables](#campaign_vfx_campaign_vfx_event_ids_tables) | campaign_vfx_event |
  
## public_order_factors_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| factor | True | text | True | 50 | None | None |
| positive_pip_path | False | text | True | 100 | None | None |
| positive_tooltip | False | text | True | 536870910 | None | None |
| negative_pip_path | False | text | False | 200 | None | None |
| negative_tooltip | False | text | False | 536870910 | None | None |
| optional_campaign_key | False | text | False | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## quotes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| quote_onscreen | False | text | True | 536870910 | None | None |
| quote_person | False | text | False | 50 | [quotes_people_tables](#quotes_people_tables) | quote_person_key |
| key | True | autonumber | False | None | None | None |
  
## quotes_people_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| quote_person_key | True | text | False | 50 | None | None |
| quote_person_onscreen | False | text | True | 536870910 | None | None |
  
## random_localisation_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| string | False | text | True | 536870910 | None | None |
  
## regions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| onscreen | False | text | True | 255 | None | None |
| palette_entry | False | integer | True | None | None | None |
| r | False | integer | True | None | None | None |
| g | False | integer | True | None | None | None |
| b | False | integer | True | None | None | None |
| battle_name | False | text | True | 255 | None | None |
| in_encyclopedia | False | yesno | True | None | None | None |
| is_sea | False | yesno | True | None | None | None |
| owner_bundle | False | text | False | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
  
## regions_continents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| continent | True | text | True | 50 | None | None |
  
## regions_titles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| region | True | text | True | 50 | [regions_tables](#regions_tables) | key |
| government | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| gender | True | text | True | 50 | [genders_tables](#genders_tables) | gender |
| title | False | text | True | 50 | None | None |
  
## regions_to_region_groups_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| region_group | True | text | True | 1024 | [region_groups_tables](#region_groups_tables) | group_key |
| region | True | text | True | 50 | [regions_tables](#regions_tables) | key |
  
## region_campaign_overrides_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| region | True | text | True | 255 | [regions_tables](#regions_tables) | key |
| campaign | True | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| religion | False | text | False | 255 | [religions_tables](#religions_tables) | religion_key |
| religion_zeal | False | integer | True | None | None | None |
  
## region_economics_factors_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| factor | True | text | True | 50 | None | None |
| positive_pip_path | False | text | True | 100 | None | None |
| positive_tooltip | False | text | True | 536870910 | None | None |
  
## region_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| group_key | True | text | True | 1024 | None | None |
| localised_name | False | text | True | 20000 | None | None |
| camera_position_x | False | double | True | None | None | None |
| camera_position_y | False | double | True | None | None | None |
| camera_zoom | False | double | True | None | None | None |
| camera_heading | False | double | True | None | None | None |
| round | False | integer | True | None | None | None |
  
## region_religions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| region | True | text | True | 255 | [regions_tables](#regions_tables) | key |
| religion | False | text | True | 255 | [religions_tables](#religions_tables) | religion_key |
| religion_zeal | False | integer | True | None | None | None |
  
## region_to_province_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| region | True | text | True | 50 | [regions_tables](#regions_tables) | key |
| province | True | text | True | 255 | [provinces_tables](#provinces_tables) | key |
  
## region_unit_resources_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| string | False | text | True | 50 | None | None |
  
## religions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| religion_key | True | text | True | 50 | None | None |
| onscreen | False | text | True | 50 | None | None |
| convertibility | False | integer | True | None | None | None |
| ui_icon_path | False | text | True | 100 | None | None |
  
## religion_conversion_mods_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| rel_from | True | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
| rel_to | True | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
| modifier | False | double | True | None | None | None |
  
## resources_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| icon_filepath | False | text | True | 50 | None | None |
| key | True | text | True | 50 | None | None |
| onscreen_text | False | text | True | 50 | None | None |
| unit | False | text | False | 50 | [commodity_unit_names_tables](#commodity_unit_names_tables) | unit |
| slot_bed | False | text | True | 50 | [slots_tables](#slots_tables) | slot |
| trade_value | False | integer | True | None | None | None |
| strategic_value | False | integer | True | None | None | None |
| description | False | text | True | 2048 | None | None |
| long_description | False | text | False | 2048 | None | None |
| in_encyclopedia | False | yesno | True | None | None | None |
  
## resource_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| resource_key | True | text | True | 50 | [resources_tables](#resources_tables) | key |
| effect_key | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | single | True | None | None | None |
  
## scripted_objectives_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| localised_text | False | text | True | 255 | None | None |
  
## scripted_subtitles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| localised_text | False | text | True | 255 | None | None |
| character_for_vo | False | text | False | 255 | None | None |
  
## seasons_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| season | True | text | True | 50 | None | None |
| onscreen | False | text | True | 50 | None | None |
| order | False | integer | True | None | None | None |
  
## season_attritions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| season | True | text | True | 255 | [seasons_tables](#seasons_tables) | season |
| attrition_type | True | text | True | 255 | [campaign_map_attritions_tables](#campaign_map_attritions_tables) | key |
| enable | True | yesno | True | None | None | None |
| campaign | True | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## season_province_effect_bundles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| season | True | text | True | 255 | [seasons_tables](#seasons_tables) | season |
| province | True | text | True | 255 | [provinces_tables](#provinces_tables) | key |
| effect_bundle | True | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| weighting | False | integer | True | None | None | None |
| default | False | yesno | True | None | None | None |
  
## sea_climate_details_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | [climates_tables](#climates_tables) | climate_type |
| sea_deep_colour | False | text | True | 50 | None | None |
| sea_shallow_colour | False | text | True | 50 | None | None |
| sun_colour | False | text | True | 50 | None | None |
| sky_colour | False | text | True | 50 | None | None |
  
## sea_surfaces_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| sea_wind_speed | False | single | True | None | None | None |
| sea_phillips_constant | False | single | True | None | None | None |
| sea_choppiness | False | single | True | None | None | None |
| swell_wind_speed | False | single | True | None | None | None |
| swell_phillips_constant | False | single | True | None | None | None |
| foam_enabled | False | yesno | True | None | None | None |
| foam_decay_rate | False | single | True | None | None | None |
| foam_fade_in_time | False | single | True | None | None | None |
| foam_cut_off_value | False | single | True | None | None | None |
| froth_value | False | single | True | None | None | None |
| froth_distortion_speed | False | single | True | None | None | None |
| froth_distortion_amount | False | single | True | None | None | None |
| spray_cut_off_value | False | single | True | None | None | None |
| spray_speed | False | single | True | None | None | None |
| spray_duration | False | single | True | None | None | None |
| sea_shininess | False | single | True | None | None | None |
| sea_decay | False | single | True | None | None | None |
| reflection_flattening_factor | False | single | True | None | None | None |
| wave_trough_y_value | False | single | True | None | None | None |
| detail_normal_uv_scale1 | False | single | True | None | None | None |
| detail_normal_uv_speed1 | False | single | True | None | None | None |
| detail_normal_uv_scale2 | False | single | True | None | None | None |
| detail_normal_uv_speed2 | False | single | True | None | None | None |
  
## send_diplomat_incidents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| outcome | True | text | True | 20 | [send_diplomat_outcomes_tables](#send_diplomat_outcomes_tables) | key |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| incident | True | text | True | 255 | [incidents_tables](#incidents_tables) | key |
| weight | False | integer | True | None | None | None |
  
## send_diplomat_outcomes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 20 | None | None |
  
## ship_dbs_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| spacing | False | text | True | 255 | [unit_spacings_tables](#unit_spacings_tables) | key |
| entity | False | text | True | 50 | [battle_entities_tables](#battle_entities_tables) | key |
| model | False | text | True | 50 | [models_naval_tables](#models_naval_tables) | key |
  
## ship_names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | integer | True | None | [names_groups_tables](#names_groups_tables) | key |
| name_group | False | integer | True | None | [names_groups_tables](#names_groups_tables) | key |
| Ship_Name | False | text | True | 50 | None | None |
| exclusive_to_faction | False | text | False | 50 | [factions_tables](#factions_tables) | key |
  
## shortcut_localisation_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 50 | None | None |
| onscreen | False | text | False | 536870910 | None | None |
| toolitp | False | text | False | 255 | None | None |
  
## skeletons_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## slots_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| slot | True | text | True | 50 | None | None |
| is_farm | False | yesno | True | None | None | None |
| is_resource | False | yesno | False | None | None | None |
| is_town | False | yesno | False | None | None | None |
| is_port | False | yesno | False | None | None | None |
| supports_building_level_conversion | False | yesno | False | None | None | None |
  
## slots_art_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| slot | True | text | True | 50 | [slots_tables](#slots_tables) | slot |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| underlay_terrain_texture | False | text | False | 50 | [warscape_underlay_textures_tables](#warscape_underlay_textures_tables) | underlay_key |
| underlay_rotation | False | integer | False | None | None | None |
| underlay_scale | False | integer | False | None | None | None |
| underlay_differs_with_building | False | yesno | False | None | None | None |
| template_model | False | text | False | 50 | [slots_templates_models_tables](#slots_templates_models_tables) | template_name |
| template_differs_at_quality_zero | False | yesno | False | None | None | None |
| template_model_art_quality_zero | False | text | False | 50 | [slots_templates_models_tables](#slots_templates_models_tables) | template_name |
| use_minibuildings | False | yesno | False | None | None | None |
| minibuildings_differ_at_quality | False | yesno | False | None | None | None |
| use_minibuildings_from_quality | False | integer | True | None | None | None |
| empty_building_model | False | text | False | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| empty_building_model_animated | False | text | False | 50 | [warscape_animated_tables](#warscape_animated_tables) | key |
| display_empty_bldg_from_quality | False | integer | True | None | None | None |
  
## slots_gdp_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| slot | True | text | True | 50 | [slots_tables](#slots_tables) | slot |
| level | True | integer | True | None | None | None |
| gdp_value | False | integer | True | None | None | None |
| building_gdp_modifier | False | double | True | None | None | None |
| onscreen_name | False | text | True | 50 | None | None |
  
## slots_templates_models_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| template_name | True | text | True | 50 | None | None |
| model_filename | False | text | True | 255 | None | None |
| model_filepath | False | text | True | 255 | None | None |
  
## slot_templates_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## slot_template_to_building_superchain_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| slot_template | False | text | True | 255 | [slot_templates_tables](#slot_templates_tables) | key |
| building_superchain | False | text | True | 255 | [building_superchains_tables](#building_superchains_tables) | key |
  
## slot_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| can_destroy | False | yesno | True | None | None | None |
| can_convert | False | yesno | True | None | None | None |
  
## small_vegetation_climates_jct_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| climate | True | text | True | 50 | [climates_tables](#climates_tables) | climate_type |
| rigid_name | True | text | True | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
  
## special_abilities_specific_behaviour_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 20000 | None | None |
  
## special_ability_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ability_group | True | text | True | 255 | None | None |
| tooltip | False | text | True | 255 | None | None |
| icon_path | False | text | True | 255 | None | None |
| name | False | text | True | 255 | None | None |
| special_edition_mask | False | integer | True | None | None | None |
  
## special_ability_groups_to_factions_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ability_group | True | text | True | 255 | [special_ability_groups_tables](#special_ability_groups_tables) | ability_group |
| faction | False | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## special_ability_groups_to_unit_abilities_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| special_ability_groups | True | text | True | 255 | [special_ability_groups_tables](#special_ability_groups_tables) | ability_group |
| unit_special_abilities | True | text | True | 255 | [unit_special_abilities_tables](#unit_special_abilities_tables) | key |
  
## special_ability_invalid_usage_flags_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| flag_key | True | text | True | 255 | None | None |
  
## special_ability_phases_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| duration | False | single | True | None | None | None |
| effect_type | False | text | True | 255 | [special_ability_phase_effect_types_tables](#special_ability_phase_effect_types_tables) | effect_type |
| requested_stance | False | text | False | 255 | [special_ability_stance_enums_tables](#special_ability_stance_enums_tables) | key |
| unbreakable | False | yesno | True | None | None | None |
| cant_move | False | yesno | True | None | None | None |
| kill_own_unit | False | yesno | True | None | None | None |
| minor_casualties | False | yesno | True | None | None | None |
| major_casualties | False | yesno | True | None | None | None |
| freeze_fatigue | False | yesno | True | None | None | None |
| fatigue_change_ratio | False | double | True | None | None | None |
| inspiration_aura_range_mod | False | double | True | None | None | None |
| ability_recharge_change | False | double | True | None | None | None |
| ui_vfx | False | text | False | 255 | [ui_effects_tables](#ui_effects_tables) | key |
| rally_amount | False | integer | True | None | None | None |
  
## special_ability_phase_attribute_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| phase | True | text | True | 255 | [special_ability_phases_tables](#special_ability_phases_tables) | id |
| attribute | True | text | True | 255 | [unit_attributes_tables](#unit_attributes_tables) | key |
  
## special_ability_phase_effect_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect_type | True | text | True | 255 | None | None |
  
## special_ability_phase_stat_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| phase | True | text | True | 255 | [special_ability_phases_tables](#special_ability_phases_tables) | id |
| value | False | text | True | 255 | None | None |
| stat | True | text | True | 255 | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| how | False | text | True | 255 | [unit_stat_modifiers_how_enums_tables](#unit_stat_modifiers_how_enums_tables) | key |
  
## special_ability_stance_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## special_ability_to_auto_deactivate_flags_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| invalid_usage_flag | True | text | True | 255 | [special_ability_invalid_usage_flags_tables](#special_ability_invalid_usage_flags_tables) | flag_key |
| special_ability_key | True | text | True | 255 | [unit_special_abilities_tables](#unit_special_abilities_tables) | key |
  
## special_ability_to_invalid_usage_flags_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| special_ability | True | text | True | 255 | [unit_special_abilities_tables](#unit_special_abilities_tables) | key |
| invalid_usage_flag | True | text | True | 255 | [special_ability_invalid_usage_flags_tables](#special_ability_invalid_usage_flags_tables) | flag_key |
  
## special_ability_to_special_ability_phase_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| special_ability | True | text | True | 50 | [unit_special_abilities_tables](#unit_special_abilities_tables) | key |
| phase | False | text | True | 255 | [special_ability_phases_tables](#special_ability_phases_tables) | id |
| order | True | integer | True | None | None | None |
  
## spotting_and_hiding_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| visibility_min_spot_range | False | integer | True | None | None | None |
| visibility_max_spot_range | False | integer | True | None | None | None |
| spot_dist_tree | False | integer | True | None | None | None |
| spot_dist_scrub | False | integer | True | None | None | None |
  
## stances_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| onscreen | False | text | True | 50 | None | None |
  
## start_pos_calendars_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign | True | text | True | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| start_year | False | integer | True | None | None | None |
| start_season | False | text | True | 50 | [seasons_tables](#seasons_tables) | season |
| turns_per_year | False | integer | True | None | None | None |
| start_week_of_year | False | integer | True | None | None | None |
  
## start_pos_characters_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ID | True | autonumber | True | None | None | None |
| faction | False | integer | True | None | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| Name | False | integer | True | None | [names_tables](#names_tables) | id |
| Surname | False | integer | False | None | [names_tables](#names_tables) | id |
| Age | False | integer | True | None | None | None |
| Type | False | text | True | 50 | [agents_tables](#agents_tables) | key |
| startx | False | double | True | None | None | None |
| starty | False | double | True | None | None | None |
| ministerial_position | False | text | False | 50 | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| portrait_id | False | text | False | 255 | [campaign_character_art_sets_tables](#campaign_character_art_sets_tables) | art_set_id |
| model | False | text | False | 255 | None | None |
| immortal | False | yesno | False | None | None | None |
| override_general_unit | False | text | False | 255 | [main_units_tables](#main_units_tables) | unit |
| is_in_generals_pool | False | yesno | True | None | None | None |
| is_male | False | yesno | True | None | None | None |
| loyalty | False | integer | True | None | None | None |
| clan_name | False | integer | False | None | [names_tables](#names_tables) | id |
| other_name | False | integer | False | None | [names_tables](#names_tables) | id |
| ambition | False | integer | True | None | None | None |
| political_party | False | text | False | 255 | [political_parties_tables](#political_parties_tables) | key |
| death_type | False | text | False | 255 | [death_types_tables](#death_types_tables) | key |
| turns_died_before_start | False | text | False | 255 | None | None |
| legacy_override | False | text | False | 255 | None | None |
| progenitor | False | yesno | True | None | None | None |
| xp | False | integer | True | None | None | None |
  
## start_pos_character_ancillaries_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| character_id | False | integer | True | None | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
| ancillary | False | text | True | 50 | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
  
## start_pos_character_to_settlements_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| character | True | integer | True | None | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
| settlement | False | integer | True | None | [start_pos_settlements_tables](#start_pos_settlements_tables) | id |
  
## start_pos_character_traits_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| character_id | False | integer | True | None | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
| trait_level | False | text | True | 50 | [character_trait_levels_tables](#character_trait_levels_tables) | key |
  
## start_pos_diplomacy_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | False | autonumber | True | None | None | None |
| faction1 | True | integer | True | None | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| faction2 | True | integer | True | None | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| stance | False | text | True | 50 | [stances_tables](#stances_tables) | key |
| grants_military_access | False | yesno | True | None | None | None |
| grants_trade_agreement | False | yesno | True | None | None | None |
| relations_modifier | False | integer | True | None | None | None |
| non_aggression_pact | False | yesno | True | None | None | None |
  
## start_pos_factions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ID | True | autonumber | True | None | None | None |
| faction | False | text | True | 50 | [factions_tables](#factions_tables) | key |
| campaign | False | text | True | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| playable | False | yesno | True | None | None | None |
| treasury | False | integer | True | None | None | None |
| starting_order | False | integer | True | None | None | None |
| government_type | False | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| state_religion | False | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
| is_major | False | yesno | False | None | None | None |
| description | False | text | False | 536870910 | None | None |
| difficulty | False | text | False | 255 | None | None |
| ai_manager | False | text | True | 255 | [campaign_ai_managers_tables](#campaign_ai_managers_tables) | manager |
| ai_personality | False | text | True | 255 | [campaign_ai_personalities_tables](#campaign_ai_personalities_tables) | personality |
| long_victory_region_count | False | integer | True | None | None | None |
| short_victory_region_count | False | integer | True | None | None | None |
| prestige_victory_region_count | False | integer | True | None | None | None |
| world_domination_victory_region_count | False | integer | True | None | None | None |
| short_victory_year_end | False | integer | True | None | None | None |
| long_victory_year_end | False | integer | True | None | None | None |
| prestige_victory_year_end | False | integer | True | None | None | None |
| world_domination_victory_year_end | False | integer | True | None | None | None |
| prestige_army | False | integer | True | None | None | None |
| prestige_navy | False | integer | True | None | None | None |
| prestige_economy | False | integer | True | None | None | None |
| prestige_enlightenment | False | integer | True | None | None | None |
| short_victory_week_in_year_end | False | integer | True | None | None | None |
| long_victory_week_in_year_end | False | integer | True | None | None | None |
| prestige_victory_week_in_year_end | False | integer | True | None | None | None |
| world_domination_victory_week_in_year_end | False | integer | True | None | None | None |
| honour | False | integer | True | None | None | None |
| ai_technology_manager | False | text | False | 255 | [campaign_ai_technology_managers_tables](#campaign_ai_technology_managers_tables) | key |
| ai_character_skill_tree_manager | False | text | False | 255 | [campaign_ai_character_skill_tree_managers_tables](#campaign_ai_character_skill_tree_managers_tables) | key |
| cai_agent_distribution_profile | False | text | True | 255 | [cai_agent_distribution_profiles_tables](#cai_agent_distribution_profiles_tables) | key |
| cai_agent_recruitment_profile | False | text | True | 255 | [cai_agent_recruitment_profiles_tables](#cai_agent_recruitment_profiles_tables) | key |
| cai_starting_personality | False | text | False | 255 | [cai_personalities_tables](#cai_personalities_tables) | key |
| mp_one_vs_one_region_count | False | integer | True | None | None | None |
| mp_2p_co_op_region_count | False | integer | True | None | None | None |
| mp_2p_co_op_region_count_long | False | integer | True | None | None | None |
| long_description | False | text | False | 536870910 | None | None |
| can_ever_convert_religion | False | yesno | True | None | None | None |
| cdir_military_generator_config | False | text | True | 255 | [cdir_military_generator_configs_tables](#cdir_military_generator_configs_tables) | key |
  
## start_pos_faction_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| start_pos_faction | True | integer | True | None | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| effect_value | False | single | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## start_pos_faction_effect_bundles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| start_pos_faction | True | integer | True | None | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| effect_bundle | True | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| duration | False | integer | True | None | None | None |
  
## start_pos_family_relationships_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| character | True | integer | True | None | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
| related_to | True | integer | True | None | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
| relationship | False | text | True | 255 | [family_relationship_types_tables](#family_relationship_types_tables) | relationship_type |
| bastard | False | yesno | True | None | None | None |
| adopted | False | yesno | True | None | None | None |
  
## start_pos_governorships_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| governorship | False | text | True | 50 | [governorships_tables](#governorships_tables) | governorship |
| campaign | False | text | True | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| lower_class_tax_rate | False | integer | True | None | None | None |
| upper_class_tax_rate | False | double | True | None | None | None |
  
## start_pos_land_units_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| unit_type | False | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| general | False | integer | True | None | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
| soldiers | False | integer | True | None | None | None |
  
## start_pos_naval_units_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ID | True | autonumber | True | None | None | None |
| unit_type | False | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| admiral | False | integer | True | None | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
  
## start_pos_past_events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| source | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| target | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| event | True | text | True | 255 | [cai_personality_diplomatic_events_tables](#cai_personality_diplomatic_events_tables) | id |
| turns_ago | True | integer | True | None | None | None |
  
## start_pos_regions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | False | autonumber | True | None | None | None |
| region | True | text | True | 50 | [regions_tables](#regions_tables) | key |
| campaign | True | text | True | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| owning_faction | False | integer | True | None | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| faction_capital | False | yesno | True | None | None | None |
| base_population | False | integer | True | None | None | None |
| base_max_population | False | integer | True | None | None | None |
| population | False | integer | True | None | None | None |
| base_gdp | False | integer | True | None | None | None |
| road_upgrades | False | integer | True | None | None | None |
| canals | False | yesno | True | None | None | None |
| railways | False | yesno | True | None | None | None |
| town_wealth | False | integer | True | None | None | None |
| governorship | False | text | True | 50 | [governorships_tables](#governorships_tables) | governorship |
| cultural_originator | False | text | False | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| rebel_faction | False | text | True | 50 | [factions_tables](#factions_tables) | key |
| rebel_faction_name | False | text | True | 536870910 | None | None |
| alternative_rebel_faction | False | text | True | 255 | [factions_tables](#factions_tables) | key |
| settler_rebellions_enabled | False | yesno | False | None | None | None |
| capture_prestige | False | integer | True | None | None | None |
| long_description | False | text | False | 536870910 | None | None |
| development_points | False | integer | True | None | None | None |
  
## start_pos_regions_to_unit_resources_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | integer | False | None | [start_pos_regions_tables](#start_pos_regions_tables) | id |
| resource | True | text | False | 50 | [region_unit_resources_tables](#region_unit_resources_tables) | key |
  
## start_pos_region_religions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| region | True | integer | True | None | [start_pos_regions_tables](#start_pos_regions_tables) | id |
| religion | True | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
| percentage | False | double | True | None | None | None |
  
## start_pos_region_slot_templates_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| campaign | True | text | True | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| region | True | text | True | 50 | [regions_tables](#regions_tables) | key |
| slot_type | True | text | True | 255 | [slot_types_tables](#slot_types_tables) | key |
| slot_template | True | text | True | 255 | [slot_templates_tables](#slot_templates_tables) | key |
  
## start_pos_settlements_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| settlement_id | True | text | True | 50 | [campaign_map_settlements_tables](#campaign_map_settlements_tables) | settlement_id |
| region | True | integer | True | None | [start_pos_regions_tables](#start_pos_regions_tables) | id |
| building1 | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| building2 | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| building3 | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| building4 | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| building5 | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| wealth | False | integer | False | None | None | None |
| fortification | False | integer | False | None | None | None |
| onscreen_name | False | text | True | 536870910 | None | None |
| id | False | autonumber | False | None | None | None |
| roads | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| fortifications | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| primary_building | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| port_building | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| startpos_slave_points | False | integer | True | None | None | None |
  
## start_pos_settlement_garrisons_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| settlement | False | integer | True | None | [start_pos_settlements_tables](#start_pos_settlements_tables) | id |
| unit | False | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| soldiers | False | integer | True | None | None | None |
  
## start_pos_technologies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction | True | integer | True | None | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| technology | True | text | True | 50 | [technologies_tables](#technologies_tables) | key |
  
## start_pos_victory_conditions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| start_pos_faction | True | integer | True | None | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| region | True | text | True | 50 | [regions_tables](#regions_tables) | key |
| victory_type | True | text | True | 50 | [victory_types_tables](#victory_types_tables) | victory_type |
  
## state_gift_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| value | False | integer | True | None | None | None |
  
## stats_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| public | False | yesno | True | None | None | None |
| label | False | text | False | 255 | [random_localisation_strings_tables](#random_localisation_strings_tables) | key |
| ladder | False | yesno | True | None | None | None |
  
## stats_clans_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| public | False | yesno | True | None | None | None |
| label | False | text | False | 255 | [random_localisation_strings_tables](#random_localisation_strings_tables) | key |
| ladder | False | yesno | True | None | None | None |
  
## subtitle_timings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| subtitle_field | True | integer | True | None | [TExc_LocalisableFields_tables](#TExc_LocalisableFields_tables) | key |
| language | True | text | True | 255 | [languages_tables](#languages_tables) | key |
| start | False | integer | True | None | None | None |
| end | False | integer | True | None | None | None |
| script_id | False | integer | True | None | [vo_scripts_tables](#vo_scripts_tables) | id |
| text_section | True | integer | True | None | None | None |
| foreign_key | True | text | True | 255 | None | None |
| text_id | False | text | True | 20000 | None | None |
  
## taxes_classes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| tax | True | text | True | 50 | None | None |
  
## taxes_effects_jct_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| tax_name | True | text | False | 50 | [taxes_keys_tables](#taxes_keys_tables) | tax_lookup |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | double | True | None | None | None |
| optional_campaign_key | True | text | False | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| optional_difficulty_level | True | text | False | 50 | None | None |
| ai_only | True | yesno | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## taxes_keys_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| tax_class | True | text | True | 50 | [taxes_classes_tables](#taxes_classes_tables) | tax |
| tax_level | True | text | False | 50 | [taxes_levels_tables](#taxes_levels_tables) | tax_level |
| tax_lookup | False | text | True | 50 | None | None |
  
## taxes_levels_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| tax_level | True | text | True | 50 | None | None |
| percentage | False | integer | True | None | None | None |
  
## team_colours_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| alliance | False | integer | True | None | None | None |
| r | True | integer | True | None | None | None |
| g | True | integer | True | None | None | None |
| b | True | integer | True | None | None | None |
| army_index | False | integer | True | None | None | None |
  
## technologies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| building_level | False | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| position_index | False | integer | True | None | None | None |
| onscreen_name | False | text | True | 255 | None | None |
| short_description | False | text | True | 536870910 | None | None |
| long_description | False | text | True | 536870910 | None | None |
| icon_name | False | text | True | 255 | None | None |
| research_points_required | False | integer | True | None | None | None |
| military_prestige | False | integer | True | None | None | None |
| naval_prestige | False | integer | True | None | None | None |
| economic_prestige | False | integer | True | None | None | None |
| enlightenment_prestige | False | integer | True | None | None | None |
| mp_available_early | False | yesno | False | None | None | None |
| mp_available_late | False | yesno | False | None | None | None |
| info_pic | False | text | True | 255 | None | None |
| ai_bias | False | integer | True | None | None | None |
| unique_index | False | autonumber | True | None | None | None |
| in_encyclopedia | False | yesno | True | None | None | None |
| cost_per_round | False | integer | True | None | None | None |
| is_civil | False | yesno | True | None | None | None |
| is_engineering | False | yesno | True | None | None | None |
| is_military | False | yesno | True | None | None | None |
  
## technology_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| position | False | integer | True | None | None | None |
  
## technology_category_modules_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| technology_node_set | True | text | True | 255 | [technology_node_sets_tables](#technology_node_sets_tables) | key |
| max_tier | True | integer | True | None | None | None |
| effect_bundle | False | text | False | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| min_tier | False | integer | True | None | None | None |
  
## technology_category_parents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| parent_category | True | text | True | 255 | [technology_categories_tables](#technology_categories_tables) | key |
| child_category | True | text | True | 255 | [technology_categories_tables](#technology_categories_tables) | key |
  
## technology_effects_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| technology | True | text | True | 255 | [technologies_tables](#technologies_tables) | key |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | text | True | 50 | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## technology_faction_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| technology_key | True | text | True | 255 | [technologies_tables](#technologies_tables) | key |
| faction_key | True | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## technology_nodes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| technology_node_set | False | text | True | 255 | [technology_node_sets_tables](#technology_node_sets_tables) | key |
| technology_key | False | text | True | 255 | [technologies_tables](#technologies_tables) | key |
| faction_key | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| campaign_key | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| tier | False | integer | True | None | None | None |
| indent | False | integer | True | None | None | None |
  
## technology_node_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| parent_key | True | text | True | 255 | [technology_nodes_tables](#technology_nodes_tables) | key |
| child_key | True | text | True | 255 | [technology_nodes_tables](#technology_nodes_tables) | key |
| initial_descent_tiers | False | integer | True | None | None | None |
| parent_link_position | False | integer | True | None | None | None |
| child_link_position | False | integer | True | None | None | None |
| encyclopedia_parent_link_position | False | integer | False | None | None | None |
| encyclopedia_child_link_position | False | integer | False | None | None | None |
  
## technology_node_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| faction_key | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| campaign_key | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| technology_category | False | text | True | 255 | [technology_categories_tables](#technology_categories_tables) | key |
| culture | False | text | False | 255 | [cultures_tables](#cultures_tables) | key |
| subculture | False | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| localised_name | False | text | True | 255 | None | None |
| tooltip_string | False | text | True | 255 | None | None |
| encyclopaedia_string | False | text | True | 255 | None | None |
  
## technology_required_building_levels_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| technology | True | text | True | 255 | [technologies_tables](#technologies_tables) | key |
| required_building_level | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
  
## technology_required_technology_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| technology | True | text | True | 255 | [technologies_tables](#technologies_tables) | key |
| required_technology | True | text | True | 255 | [technologies_tables](#technologies_tables) | key |
  
## technology_unit_upgrades_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| technology | True | text | True | 255 | [technologies_tables](#technologies_tables) | key |
| unit | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| target_unit | False | text | False | 255 | [main_units_tables](#main_units_tables) | unit |
| cost | False | integer | True | None | None | None |
  
## terrain_tilesets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| tileset_name | True | text | True | 255 | None | None |
  
## TExc_campaign_map_processing_exports_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| table_name | True | text | False | 50 | None | None |
  
## TExc_data_folders_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| directory | True | text | False | 255 | None | None |
| code_owner | False | text | False | 50 | None | None |
| author | False | text | False | 50 | None | None |
| exclude | False | yesno | False | None | None | None |
| packing_notes | False | text | False | 536870910 | None | None |
| pack_file | False | text | False | 255 | [TExc_pack_files_tables](#TExc_pack_files_tables) | pack_file |
  
## texc_expansions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| expansion | True | text | True | 255 | None | None |
| description | False | text | True | 255 | None | None |
| pack_filename_extension | False | text | False | 255 | None | None |
| released | False | yesno | True | None | None | None |
  
## TExc_ImplementedTables_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| table_name | True | text | False | 100 | None | None |
| Designer | False | text | False | 50 | None | None |
| Implemented | False | yesno | False | None | None | None |
| Implementer | False | text | False | 50 | None | None |
| Modified | False | yesno | False | None | None | None |
| destination_pack | False | text | False | 50 | [TExc_PackCategories_tables](#TExc_PackCategories_tables) | pack_category |
  
## TExc_LocalisableFields_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | False | None | None | None |
| table_name | False | text | False | 50 | [TExc_ImplementedTables_tables](#TExc_ImplementedTables_tables) | table_name |
| field | False | text | False | 50 | None | None |
| destination_file | False | text | False | 50 | None | None |
| ready_for_export | False | yesno | False | None | None | None |
| spreadsheet | False | text | False | 255 | None | None |
| field_as_key | False | text | False | 255 | None | None |
| for_vo | False | yesno | True | None | None | None |
  
## TExc_missing_conditions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ID | True | autonumber | False | None | None | None |
| exported_script | False | text | False | 255 | None | None |
| condition | False | text | False | 255 | None | None |
  
## TExc_PackCategories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| pack_category | True | text | False | 50 | None | None |
| script_name | False | text | False | 50 | None | None |
| pack_file | False | text | False | 50 | None | None |
| localisation_file | False | text | False | 50 | None | None |
| locked | False | yesno | False | None | None | None |
| locked_by | False | text | False | 50 | None | None |
  
## TExc_pack_files_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| pack_file | True | text | False | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## TExc_script_conditions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| Condition | True | text | False | 100 | None | None |
  
## TExc_TableExportCategories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| category | True | text | False | 50 | None | None |
  
## TExc_TableExportGroups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ID | True | autonumber | False | None | None | None |
| category | False | text | False | 50 | [TExc_TableExportCategories_tables](#TExc_TableExportCategories_tables) | category |
| table | False | text | False | 50 | [TExc_ImplementedTables_tables](#TExc_ImplementedTables_tables) | table_name |
  
## TExc_unrest_causes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| cause | True | text | False | 50 | None | None |
  
## TExc_unrest_demands_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| demand | True | text | False | 50 | None | None |
  
## town_wealth_growth_factors_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| factor | True | text | True | 50 | None | None |
| positive_pip_path | False | text | True | 100 | None | None |
| positive_tooltip | False | text | True | 536870910 | None | None |
| negative_pip_path | False | text | False | 200 | None | None |
| negative_tooltip | False | text | False | 536870910 | None | None |
  
## trade_details_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| onscreen_text | False | text | True | 536870910 | None | None |
| icon_filepath | False | text | True | 50 | None | None |
  
## trade_display_campaign_originating_culture_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| originating_culture | False | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_originating_culture_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| originating_culture | False | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_originating_subculture_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| originating_subculture | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_originating_subculture_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| originating_subculture | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_owning_culture_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| owning_culture | False | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_owning_culture_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| owning_culture | False | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_owning_faction_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| owning_faction | False | text | True | 255 | [factions_tables](#factions_tables) | key |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_owning_faction_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| owning_faction | False | text | True | 255 | [factions_tables](#factions_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_owning_subculture_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| owning_subculture | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_owning_subculture_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| owning_subculture | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_generic_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_originating_culture_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| originating_culture | False | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_originating_culture_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| originating_culture | False | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_originating_subculture_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| originating_subculture | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_originating_subculture_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| originating_subculture | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_owning_culture_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| owning_culture | False | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_owning_culture_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| owning_culture | False | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_owning_faction_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| owning_faction | False | text | True | 255 | [factions_tables](#factions_tables) | key |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_owning_faction_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| owning_faction | False | text | True | 255 | [factions_tables](#factions_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_owning_subculture_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| owning_subculture | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_owning_subculture_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| owning_subculture | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_trade_models_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| model | False | text | True | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
| optional_following_model | False | text | False | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
| is_naval | False | yesno | True | None | None | None |
| optional_following_model_distance | False | single | True | None | None | None |
  
## trade_nodes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ID | True | text | True | 50 | None | None |
| commodity | False | text | True | 50 | [commodities_tables](#commodities_tables) | key |
| base_quantity | False | integer | True | None | None | None |
| percentage_increase_per_agent | False | double | True | None | None | None |
| maximum_percentage_increase | False | double | True | None | None | None |
| display_name | False | text | True | 255 | None | None |
| group | False | text | True | 255 | [trade_node_groups_tables](#trade_node_groups_tables) | key |
  
## trade_node_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| display_name | False | text | True | 255 | None | None |
  
## trait_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| category | True | text | False | 50 | None | None |
| icon_path | False | text | False | 100 | None | None |
  
## trait_info_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| trait | True | text | True | 255 | None | None |
| applicable_to | False | text | True | 50 | None | None |
  
## trait_level_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| trait_level | True | text | True | 50 | [character_trait_levels_tables](#character_trait_levels_tables) | key |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | double | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## trait_to_antitraits_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| trait | True | text | True | 50 | [trait_info_tables](#trait_info_tables) | trait |
| antitrait | True | text | True | 50 | [trait_info_tables](#trait_info_tables) | trait |
  
## trait_to_included_agents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| trait | True | text | True | 50 | [trait_info_tables](#trait_info_tables) | trait |
| agent | True | text | True | 50 | [agents_tables](#agents_tables) | key |
  
## trait_triggers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| trigger | True | text | True | 50 | None | None |
| event | False | text | True | 50 | [trigger_events_tables](#trigger_events_tables) | event |
| conditions | False | text | True | 536870910 | None | None |
  
## translated_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| language | True | text | True | 255 | [languages_tables](#languages_tables) | key |
| last_english_text | False | text | False | 255 | None | None |
| translated_text | False | text | False | 255 | None | None |
| requires_translation | False | yesno | True | None | None | None |
| requires_recording | False | yesno | True | None | None | None |
  
## trigger_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | False | None | None | None |
| trigger | False | text | False | 50 | [trait_triggers_tables](#trait_triggers_tables) | trigger |
| trait | False | text | True | 50 | [trait_info_tables](#trait_info_tables) | trait |
| value | False | integer | True | None | None | None |
| chance | False | integer | True | None | None | None |
  
## trigger_events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| event | True | text | True | 50 | None | None |
| from_ui | False | yesno | False | None | None | None |
  
## trigger_event_to_excluded_agent_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| event | True | text | False | 50 | [trigger_events_tables](#trigger_events_tables) | event |
| agent | True | text | True | 50 | [agents_tables](#agents_tables) | key |
  
## uied_component_addresses_to_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_label | True | text | True | 255 | [uied_component_texts_tables](#uied_component_texts_tables) | component_label |
| component_address | True | text | True | 255 | None | None |
| component_layout | False | text | True | 255 | [uied_text_layouts_tables](#uied_text_layouts_tables) | layout_id |
  
## uied_component_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_label | True | text | True | 255 | None | None |
| localised_string | False | text | True | 536870910 | None | None |
  
## uied_text_layouts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| layout_id | True | text | True | 255 | None | None |
| layout_location | False | text | True | 20000 | None | None |
  
## ui_component_addresses_with_localisation_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_label | True | text | True | 255 | [ui_component_localisation_tables](#ui_component_localisation_tables) | component_label |
| component_address | True | text | False | 255 | None | None |
  
## ui_component_localisation_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_label | True | text | False | 255 | None | None |
| localised_string | False | text | False | 536870910 | None | None |
  
## ui_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| banner_fx | False | text | False | 255 | [particle_effects_tables](#particle_effects_tables) | key |
| ping_fx | False | text | False | 255 | [particle_effects_tables](#particle_effects_tables) | key |
  
## ui_unit_stats_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| onscreen_name | False | text | True | 255 | None | None |
| max_value | False | integer | True | None | None | None |
| campaign_only | False | yesno | True | None | None | None |
| sort_order | False | integer | True | None | None | None |
| tooltip_text | False | text | True | 1024 | None | None |
  
## ui_unit_stats_filters_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## ui_unit_stat_to_classes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| stat_key | True | text | True | 255 | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| unit_class | True | text | True | 255 | [unit_class_tables](#unit_class_tables) | key |
| list_order | False | integer | True | None | None | None |
| filter | True | text | True | 255 | [ui_unit_stats_filters_tables](#ui_unit_stats_filters_tables) | key |
  
## uniform_type_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## units_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| on_screen_name | False | text | True | 50 | None | None |
| category | False | text | True | 50 | [unit_category_tables](#unit_category_tables) | key |
| class | False | text | True | 50 | [unit_class_tables](#unit_class_tables) | key |
| multiplayer_cost | False | integer | True | None | None | None |
| multiplayer_late_cost | False | integer | True | None | None | None |
| create_time | False | integer | True | None | None | None |
| create_cost | False | integer | True | None | None | None |
| upkeep_cost | False | integer | True | None | None | None |
| campaign_action_points | False | integer | True | None | None | None |
| voice | False | text | False | 255 | None | None |
| fitness | False | integer | True | None | None | None |
| icon_name | False | text | True | 100 | None | None |
| unit_description_text | False | text | True | 50 | [unit_description_texts_tables](#unit_description_texts_tables) | key |
| info_pic | False | text | True | 100 | None | None |
| region_unit_resource | False | text | False | 50 | [region_unit_resources_tables](#region_unit_resources_tables) | key |
| total_cap | False | integer | True | None | None | None |
| era | False | text | True | 255 | None | None |
| mp_available_early | False | yesno | True | None | None | None |
| mp_available_middle | False | yesno | True | None | None | None |
| mp_available_late | False | yesno | True | None | None | None |
| prestige | False | integer | True | None | None | None |
| armed_citizenry | False | yesno | True | None | None | None |
| total_cap_mp | False | integer | True | None | None | None |
| unit_type_icon | False | text | False | 255 | None | None |
| use_onscreen_name | False | yesno | True | None | None | None |
| unit_caste | False | text | True | 255 | [unit_castes_tables](#unit_castes_tables) | caste |
| additional_building_level_requirement | False | text | False | 1024 | [building_levels_tables](#building_levels_tables) | level_name |
| religion_requirement | False | text | False | 1024 | [religions_tables](#religions_tables) | religion_key |
| resource_requirement | False | text | False | 1024 | [resources_tables](#resources_tables) | key |
| in_encyclopedia | False | yesno | True | None | None | None |
| unit_recruited_movie | False | text | False | 50 | [movie_event_strings_tables](#movie_event_strings_tables) | event |
| unique_index | False | autonumber | True | None | None | None |
| pdlc | False | text | False | 255 | [pdlc_tables](#pdlc_tables) | ID |
| is_male | False | yesno | True | None | None | None |
| supports_first_person | False | yesno | True | None | None | None |
  
## units_custom_battle_permissions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| general_unit | True | yesno | True | None | None | None |
| siege_unit_attacker | False | yesno | True | None | None | None |
| siege_unit_defender | False | yesno | True | None | None | None |
  
## units_special_edition_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 50 | [units_tables](#units_tables) | key |
  
## units_to_exclusive_faction_permissions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| faction | True | text | True | 50 | [factions_tables](#factions_tables) | key |
| allowed | False | yesno | True | None | None | None |
  
## units_to_gov_types_conversion_jcts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | integer | True | None | [units_to_gov_type_permissions_tables](#units_to_gov_type_permissions_tables) | unique_number |
| unit | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
  
## units_to_gov_type_outcomes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | [units_tables](#units_tables) | key |
| gov_type | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| outcome | False | text | True | 50 | [units_to_gov_type_outcomes_enum_tables](#units_to_gov_type_outcomes_enum_tables) | key |
  
## units_to_gov_type_outcomes_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## units_to_gov_type_permissions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unique_number | False | autonumber | False | None | None | None |
| key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| gov_type | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| outcome | False | text | True | 50 | [units_to_gov_type_outcomes_enum_tables](#units_to_gov_type_outcomes_enum_tables) | key |
  
## units_to_groupings_military_permissions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| military_group | True | text | True | 50 | [groupings_military_tables](#groupings_military_tables) | military_group |
  
## unit_abilities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| stationary_for_turn | False | yesno | True | None | None | None |
| supersedes_ability | False | text | False | 50 | None | None |
| requires_effect_enabling | False | yesno | False | None | None | None |
| tooltip_text | False | text | False | 20000 | None | None |
  
## unit_armour_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| armour_value | False | integer | True | None | None | None |
| bonus_v_missiles | False | yesno | False | None | None | None |
| weak_v_missiles | False | yesno | False | None | None | None |
| audio_material | False | text | True | 255 | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
  
## unit_attributes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| bullet_text | False | text | True | 255 | None | None |
  
## unit_attributes_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| group_name | True | text | True | 255 | None | None |
  
## unit_attributes_to_groups_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| attribute | True | text | True | 255 | [unit_attributes_tables](#unit_attributes_tables) | key |
| attribute_group | True | text | False | 255 | [unit_attributes_groups_tables](#unit_attributes_groups_tables) | group_name |
  
## unit_castes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| caste | True | text | True | 255 | None | None |
| localised_name | False | text | False | 20000 | None | None |
| sort_priority | False | integer | True | None | None | None |
  
## unit_category_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| localised_name | False | text | False | 20000 | None | None |
| r_colour | False | double | True | None | None | None |
| g_colour | False | double | True | None | None | None |
| b_colour | False | double | True | None | None | None |
| min_battle_rows | False | integer | True | None | None | None |
  
## unit_class_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| onscreen | False | text | True | 50 | None | None |
| tooltip | False | text | False | 536870910 | None | None |
| sort_priority | False | integer | True | None | None | None |
| icon | False | text | True | 255 | None | None |
| can_assault_settlment | False | yesno | True | None | None | None |
  
## unit_class_to_population_class_priorities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_class | True | text | False | 50 | [unit_class_tables](#unit_class_tables) | key |
| upper_class_priority | False | integer | False | None | None | None |
| middle_class_priority | False | integer | False | None | None | None |
| lower_class_priority | False | integer | False | None | None | None |
  
## unit_description_historical_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| text | False | text | True | 20000 | None | None |
  
## unit_description_short_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| text | False | text | True | 20000 | None | None |
  
## unit_description_strengths_weaknesses_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| text | False | text | True | 20000 | None | None |
  
## unit_description_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| description_text | False | text | True | 536870910 | None | None |
| long_description_text | False | text | True | 536870910 | None | None |
| strengths_and_weaknesses | False | text | True | 536870910 | None | None |
  
## unit_drills_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_drill_set_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_drill_set | True | text | True | 50 | None | None |
  
## unit_experience_bonuses_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| stat | True | text | True | 255 | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| value | False | integer | True | None | None | None |
| growth_rate | False | double | True | None | None | None |
| growth_scalar | False | double | True | None | None | None |
  
## unit_experience_thresholds_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| value | False | integer | True | None | None | None |
  
## unit_experience_threshold_modifiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| modifier | False | double | True | None | None | None |
  
## unit_fatigue_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| fatigue_level | True | text | True | 255 | [_kv_fatigue_tables](#_kv_fatigue_tables) | key |
| stat | True | text | True | 255 | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| value | False | double | True | None | None | None |
  
## unit_formations_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_formation_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 20000 | None | None |
  
## unit_ground_type_movement_modifiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ground_type | True | text | True | 50 | [ground_types_tables](#ground_types_tables) | type |
| category | True | text | True | 50 | [unit_category_tables](#unit_category_tables) | key |
| speed_modifier | False | double | True | None | None | None |
  
## unit_melee_weapons_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_naval_artillery_positions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_naval_damage_sites_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_population_caps_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit | True | text | True | 50 | [units_tables](#units_tables) | key |
| faction | True | text | False | 50 | [factions_tables](#factions_tables) | key |
| unit_cap | False | integer | True | None | None | None |
  
## unit_regiment_names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name_group | True | integer | True | None | [names_groups_tables](#names_groups_tables) | key |
| unit_caste | True | text | False | 255 | [unit_castes_tables](#unit_castes_tables) | caste |
| unit_name | True | text | False | 50 | [unit_regiment_names_localisation_lookup_tables](#unit_regiment_names_localisation_lookup_tables) | key |
| name_order | False | integer | False | None | None | None |
  
## unit_regiment_names_localisation_lookup_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 50 | None | None |
| unit_name | False | text | False | 50 | None | None |
  
## unit_required_technology_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| technology_key | True | text | True | 255 | [technologies_tables](#technologies_tables) | key |
  
## unit_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## unit_set_to_unit_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_set | True | text | True | 255 | [unit_sets_tables](#unit_sets_tables) | key |
| unit_record | True | text | False | 255 | [main_units_tables](#main_units_tables) | unit |
| unit_caste | True | text | False | 255 | [unit_castes_tables](#unit_castes_tables) | caste |
| unit_category | True | text | False | 255 | [unit_category_tables](#unit_category_tables) | key |
| unit_class | True | text | False | 255 | [unit_class_tables](#unit_class_tables) | key |
| exclude | False | yesno | True | None | None | None |
  
## unit_shield_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| shield_defence_value | False | integer | True | None | None | None |
| shield_armour_value | False | integer | True | None | None | None |
| audio_material | False | text | True | 255 | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
| missile_block_chance | False | integer | True | None | None | None |
  
## unit_spacings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| close_formation_spacing_horizontal | False | double | True | None | None | None |
| close_formation_spacing_vertical | False | double | True | None | None | None |
| close_formation_spacing_variation | False | double | True | None | None | None |
| loose_formation_spacing_horizontal | False | double | True | None | None | None |
| loose_formation_spacing_vertical | False | double | True | None | None | None |
| loose_formation_spacing_variation | False | double | True | None | None | None |
| dismounted_close_formation_spacing_horizontal | False | double | True | None | None | None |
| dismounted_close_formation_spacing_vertical | False | double | True | None | None | None |
| dismounted_close_formation_spacing_variation | False | double | True | None | None | None |
| dismounted_loose_formation_spacing_horizontal | False | double | True | None | None | None |
| dismounted_loose_formation_spacing_vertical | False | double | True | None | None | None |
| dismounted_loose_formation_spacing_variation | False | double | True | None | None | None |
| horde | False | yesno | True | None | None | None |
  
## unit_special_abilities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | [unit_abilities_tables](#unit_abilities_tables) | key |
| num_uses | False | integer | True | None | None | None |
| active_time | False | double | True | None | None | None |
| recharge_time | False | double | True | None | None | None |
| initial_recharge | False | single | True | None | None | None |
| wind_up_time | False | double | True | None | None | None |
| passive | False | yesno | True | None | None | None |
| effect_range | False | double | True | None | None | None |
| affect_self | False | yesno | True | None | None | None |
| num_effected_friendly_units | False | integer | True | None | None | None |
| num_effected_enemy_units | False | integer | True | None | None | None |
| update_targets_every_frame | False | yesno | True | None | None | None |
| activated_projectile | False | text | False | 255 | [projectiles_tables](#projectiles_tables) | key |
| can_autotrigger | False | yesno | True | None | None | None |
| target_friends | False | yesno | True | None | None | None |
| target_enemies | False | yesno | True | None | None | None |
| target_ground | False | yesno | True | None | None | None |
| target_intercept_range | False | single | True | None | None | None |
| assume_specific_behaviour | False | text | False | 20000 | [special_abilities_specific_behaviour_types_tables](#special_abilities_specific_behaviour_types_tables) | key |
| clear_current_order | False | yesno | True | None | None | None |
| unique_id | False | autonumber | True | None | None | None |
  
## unit_stats_firing_mechanism_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_stats_land_experience_bonuses_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| xp_level | True | integer | True | None | None | None |
| melee_attack | False | integer | False | None | None | None |
| melee_defence | False | integer | True | None | None | None |
| core_reloading_skill | False | integer | True | None | None | None |
| morale | False | integer | True | None | None | None |
| core_marksmanship | False | integer | True | None | None | None |
| fatigue | False | integer | True | None | None | None |
| mp_fixed_cost | False | double | True | None | None | None |
| mp_experience_cost_multiplier | False | double | True | None | None | None |
  
## unit_stats_naval_crew_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_type | True | text | True | 50 | None | None |
| core_loading_skill | False | integer | True | None | None | None |
| core_marksmanship | False | integer | True | None | None | None |
| melee_attack | False | integer | True | None | None | None |
| melee_defence | False | integer | True | None | None | None |
| melee_weapon_type | False | text | True | 50 | None | None |
| pistols | False | yesno | True | None | None | None |
| ammo | False | integer | True | None | None | None |
| battle_entity | False | text | True | 50 | [battle_entities_tables](#battle_entities_tables) | key |
| soldier_model | False | text | True | 50 | [warscape_animated_tables](#warscape_animated_tables) | key |
| man_animations_table | False | text | False | 50 | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| equipment_theme | False | text | True | 50 | None | None |
| armour_audio | False | text | True | 50 | None | None |
| armour | False | integer | True | None | None | None |
| spacing | False | single | True | None | None | None |
| discipline | False | integer | True | None | None | None |
| missile_type | False | text | False | 255 | [projectiles_tables](#projectiles_tables) | key |
  
## unit_stats_naval_experience_bonuses_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| xp_level | True | integer | True | None | None | None |
| melee_defence | False | integer | True | None | None | None |
| melee_attack | False | integer | True | None | None | None |
| core_gunner_loading_skill | False | integer | False | None | None | None |
| core_gunner_marksmanship | False | integer | True | None | None | None |
| morale | False | integer | True | None | None | None |
| mp_fixed_cost | False | double | True | None | None | None |
| mp_experience_cost_multiplier | False | double | True | None | None | None |
  
## unit_stats_primary_missile_weapon_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_stats_ship_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 100 | None | None |
  
## unit_stats_skeleton_melee_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_stats_skeleton_missile_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_stat_modifiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| stat | False | text | True | 255 | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| how | False | text | True | 255 | [unit_stat_modifiers_how_enums_tables](#unit_stat_modifiers_how_enums_tables) | key |
  
## unit_stat_modifiers_how_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## unit_to_unit_abilities_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_name | True | text | True | 50 | [units_tables](#units_tables) | key |
| ability | True | text | True | 50 | [unit_abilities_tables](#unit_abilities_tables) | key |
  
## unit_training_level_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 50 | None | None |
  
## unit_variants_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name | False | text | True | 255 | None | None |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| unit | True | text | True | 255 | [land_units_tables](#land_units_tables) | key |
| variant | False | text | True | 255 | [variants_tables](#variants_tables) | variant_name |
| height_variation | False | decimal | True | None | None | None |
| height_scale | False | decimal | True | None | None | None |
| unit_card | False | text | True | 255 | None | None |
  
## unit_variants_colours_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_variant | True | text | True | 255 | [unit_variants_tables](#unit_variants_tables) | name |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| primary_colour_r | False | integer | True | None | None | None |
| primary_colour_g | False | integer | True | None | None | None |
| primary_colour_b | False | integer | True | None | None | None |
| secondary_colour_r | False | integer | True | None | None | None |
| secondary_colour_g | False | integer | True | None | None | None |
| secondary_colour_b | False | integer | True | None | None | None |
| tertiary_colour_r | False | integer | True | None | None | None |
| tertiary_colour_g | False | integer | True | None | None | None |
| tertiary_colour_b | False | integer | True | None | None | None |
| soldier_type | False | text | False | 255 | [uniform_type_enums_tables](#uniform_type_enums_tables) | key |
  
## unit_weights_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| onscreen_text | False | text | True | 20000 | None | None |
  
## unrest_cause_to_demands_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| cause | True | text | True | 50 | [TExc_unrest_causes_tables](#TExc_unrest_causes_tables) | cause |
| level_of_unrest | True | text | True | 50 | None | None |
| demand | False | text | True | 50 | [TExc_unrest_demands_tables](#TExc_unrest_demands_tables) | demand |
  
## variants_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| variant_name | True | text | True | 255 | None | None |
  
## victory_conditions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| condition | True | text | True | 20000 | None | None |
  
## victory_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| victory_type | True | text | False | 50 | None | None |
  
## videos_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| video_name | True | text | True | 255 | None | None |
| video_type | False | text | True | 255 | [video_types_tables](#video_types_tables) | video_type |
| audio_tracks | False | integer | True | None | None | None |
| script_ref | False | integer | True | None | [vo_scripts_tables](#vo_scripts_tables) | id |
  
## video_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| video_type | True | text | True | 255 | None | None |
  
## vo_campaign_agent_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| character | False | text | False | 255 | None | None |
| key | True | text | True | 255 | None | None |
| text | False | text | True | 20000 | None | None |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| subculture | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## vo_characters_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| name | False | text | True | 20000 | None | None |
  
## vo_context_sensitive_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| text | False | text | True | 255 | None | None |
  
## vo_diplomacy_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| text | False | text | True | 20000 | None | None |
  
## vo_faction_intro_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| text | False | text | True | 20000 | None | None |
  
## vo_fmv_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| text | False | text | True | 20000 | None | None |
  
## vo_historical_battle_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| text | False | text | True | 20000 | None | None |
  
## vo_scripts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | integer | True | None | None | None |
| name | False | text | True | 255 | None | None |
  
## vo_speech_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| text | False | text | True | 20000 | None | None |
  
## vo_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| recorded_filename | False | text | True | 255 | None | None |
| script_id | False | integer | True | None | [vo_scripts_tables](#vo_scripts_tables) | id |
| order | False | integer | True | None | None | None |
| comment | False | text | False | 255 | None | None |
| table_field | False | integer | True | None | [TExc_LocalisableFields_tables](#TExc_LocalisableFields_tables) | key |
| foreign_key | False | text | True | 20000 | None | None |
  
## vo_text_characters_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| vo_text | True | integer | True | None | [vo_texts_tables](#vo_texts_tables) | key |
| vo_character | True | integer | True | None | [vo_characters_tables](#vo_characters_tables) | key |
  
## vo_tutorial_fmv_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| text | False | text | True | 20000 | None | None |
  
## vo_unit_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| text | False | text | True | 20000 | None | None |
  
## warscape_animated_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| texture_filename_base | False | text | True | 255 | None | None |
| category | False | text | True | 50 | [warscape_categories_tables](#warscape_categories_tables) | key |
  
## warscape_animated_lod_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| filename | False | text | True | 255 | None | None |
| range | False | single | True | None | None | None |
| animated | False | text | True | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
  
## warscape_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 50 | None | None |
  
## warscape_equipment_items_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| equipment_item | False | text | True | 50 | None | None |
| equipment_key | True | text | True | 50 | None | None |
  
## warscape_rigid_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| texture_directory | False | text | True | 255 | None | None |
| category | False | text | True | 50 | [warscape_categories_tables](#warscape_categories_tables) | key |
  
## warscape_rigid_lod_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| filename | False | text | True | 255 | None | None |
| range | False | text | True | 50 | None | None |
| rigid | False | text | True | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
  
## warscape_rigid_lod_range_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| LOD_id | True | text | False | 50 | None | None |
| range | False | integer | False | None | None | None |
  
## warscape_underlay_textures_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| underlay_key | True | text | True | 50 | None | None |
| filename | False | text | True | 50 | None | None |
| filepath | False | text | True | 50 | None | None |
| levels | False | integer | True | None | None | None |
| orientation-angle | False | integer | False | None | None | None |
| width | False | integer | False | None | None | None |
| height | False | integer | False | None | None | None |
  
## wind_levels_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| sea_surface | False | text | True | 50 | [sea_surfaces_tables](#sea_surfaces_tables) | key |
| onscreen | False | text | True | 255 | None | None |
| magnitudeX | False | double | True | None | None | None |
| magnitudeY | False | double | True | None | None | None |
| sort_order | False | integer | False | None | None | None |
  
## _kv_experience_bonuses_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| value | False | integer | True | None | None | None |
| description | False | text | True | 536870910 | None | None |
  
## _kv_fatigue_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| value | False | integer | True | None | None | None |
| description | False | text | True | 536870910 | None | None |
  
## _kv_key_buildings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| value | False | single | True | None | None | None |
| description | False | text | True | 536870910 | None | None |
  
## _kv_morale_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| value | False | single | True | None | None | None |
| description | False | text | True | 50 | None | None |
  
## _kv_naval_morale_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| value | False | integer | False | None | None | None |
| description | False | text | False | 50 | None | None |
  
## _kv_rules_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| value | False | decimal | True | None | None | None |
| description | False | text | False | 536870910 | None | None |
---
title: assemblykit db
summary: A brief description of my document.
---

# Assembly Kit Database
---
Database schemas extracted from the assembly kit `TWaD_` files.  


  
## abilities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ability | True | text | True | 50 | None | None |
| cannot_fail | False | yesno | True | None | None | None |
  
## achievements_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 80 | None | None |
| title | False | text | True | 50 | None | None |
| description | False | text | True | 536870910 | None | None |
  
## action_results_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| actor_effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| target_effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
  
## action_results_additional_outcomes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| action_result_key | False | text | True | 255 | [action_results_tables](#action_results_tables) | key |
| outcome | False | text | True | 255 | [action_results_additional_outcomes_enums_tables](#action_results_additional_outcomes_enums_tables) | key |
| value | False | double | True | None | None | None |
| effect_record | False | text | False | 255 | [effects_tables](#effects_tables) | effect |
| effect_scope_record | False | text | False | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| key | True | text | True | 255 | None | None |
| opportune_failure_weighting | False | integer | False | None | None | None |
| authority_value_coefficient | False | double | True | None | None | None |
| subterfuge_value_coefficient | False | double | True | None | None | None |
| zeal_value_coefficient | False | double | True | None | None | None |
  
## action_results_additional_outcomes_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## advice_info_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| advice_level_lookup | False | integer | True | None | [advice_levels_tables](#advice_levels_tables) | key |
| localised_text | False | text | True | 255 | None | None |
| persistant | False | yesno | True | None | None | None |
| show_on_navigate | False | yesno | True | None | None | None |
| show_instant | False | yesno | True | None | None | None |
| is_header | False | yesno | True | None | None | None |
| navigation_order | False | integer | True | None | None | None |
  
## advice_levels_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| advice_thread | False | text | True | 255 | [advice_threads_tables](#advice_threads_tables) | thread |
| advice_thread_level | False | integer | True | None | None | None |
| points_needed | False | integer | True | None | None | None |
| game_area | False | text | True | 255 | None | None |
| category | False | text | True | 255 | None | None |
| sub_category | False | text | True | 255 | None | None |
| max_repeat_count | False | integer | True | None | None | None |
| repeat_interval | False | integer | True | None | None | None |
| pause_battle | False | yesno | True | None | None | None |
| advice_item_title | False | text | False | 255 | None | None |
| priority_level | False | integer | True | None | None | None |
| high_verbosity_only | False | yesno | False | None | None | None |
| locatable | False | yesno | False | None | None | None |
| parameter | False | text | True | 50 | None | None |
| on_display_script | False | text | False | 536870910 | None | None |
| on_click_script | False | text | False | 536870910 | None | None |
| suppressible | False | yesno | True | None | None | None |
| uninhibitable | False | yesno | True | None | None | None |
| audio_clip | False | text | True | 255 | None | None |
| onscreen_text | False | text | True | 536870910 | None | None |
| advisor_name | False | text | True | 255 | [advisors_tables](#advisors_tables) | advisor_name |
| for_loading_screen | False | yesno | False | None | None | None |
| movie_link | False | text | False | 255 | None | None |
  
## advice_threads_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| thread | True | text | True | 50 | None | None |
  
## advice_triggers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| test_when | False | text | True | 255 | [trigger_events_tables](#trigger_events_tables) | event |
| condition_script | False | text | False | 536870910 | None | None |
  
## advice_trigger_to_advice_thread_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| trigger | True | text | True | 255 | [advice_triggers_tables](#advice_triggers_tables) | key |
| thread | True | text | True | 50 | [advice_threads_tables](#advice_threads_tables) | thread |
| amount | False | text | True | 50 | None | None |
  
## advisors_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| advisor_name | True | text | True | 255 | None | None |
| advisor_icon_path | False | text | True | 255 | None | None |
  
## agents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| move_points | False | integer | True | None | None | None |
| line_of_sight | False | integer | True | None | None | None |
| playable | False | yesno | True | None | None | None |
| portrait_override | False | text | False | 50 | None | None |
| primary_attribute | False | text | False | 50 | [agent_attributes_tables](#agent_attributes_tables) | key |
| religion | False | text | False | 50 | [religions_tables](#religions_tables) | religion_key |
| faction_total_cap | False | integer | True | None | None | None |
| cost | False | integer | True | None | None | None |
| in_encyclopedia | False | yesno | True | None | None | None |
  
## agent_actions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent | True | text | True | 255 | [agents_tables](#agents_tables) | key |
| ability | True | text | True | 50 | [abilities_tables](#abilities_tables) | ability |
| attribute | True | text | True | 50 | [agent_attributes_tables](#agent_attributes_tables) | key |
| critical_failure | False | text | True | 255 | [action_results_tables](#action_results_tables) | key |
| failure | False | text | True | 255 | [action_results_tables](#action_results_tables) | key |
| opportune_failure | False | text | True | 255 | [action_results_tables](#action_results_tables) | key |
| success | False | text | True | 255 | [action_results_tables](#action_results_tables) | key |
| critical_success | False | text | True | 255 | [action_results_tables](#action_results_tables) | key |
| cannot_fail | False | text | True | 255 | [action_results_tables](#action_results_tables) | key |
| localised_action_name | False | text | True | 255 | None | None |
| localised_action_description | False | text | True | 255 | None | None |
| your_message_events_male | False | text | False | 255 | [agent_action_message_events_tables](#agent_action_message_events_tables) | key |
| your_message_events_female | False | text | False | 255 | [agent_action_message_events_tables](#agent_action_message_events_tables) | key |
| their_message_events_male | False | text | False | 255 | [agent_action_message_events_tables](#agent_action_message_events_tables) | key |
| their_message_events_female | False | text | False | 255 | [agent_action_message_events_tables](#agent_action_message_events_tables) | key |
| enabled_by_effect | False | text | False | 255 | [effects_tables](#effects_tables) | effect |
  
## agent_action_message_events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| critical_failure | False | text | False | 255 | [message_events_tables](#message_events_tables) | event |
| failure | False | text | False | 255 | [message_events_tables](#message_events_tables) | event |
| opportune_failure | False | text | False | 255 | [message_events_tables](#message_events_tables) | event |
| success | False | text | False | 255 | [message_events_tables](#message_events_tables) | event |
| critical_success | False | text | False | 255 | [message_events_tables](#message_events_tables) | event |
  
## agent_attributes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## agent_culture_details_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| agent | False | text | True | 50 | [agents_tables](#agents_tables) | key |
| culture | False | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| onscreen_name | False | text | True | 50 | None | None |
| associated_unit | False | text | False | 255 | [main_units_tables](#main_units_tables) | unit |
| description_text | False | text | True | 20000 | None | None |
| season | False | text | False | 255 | None | None |
| level | False | integer | True | None | None | None |
| equipment_theme | False | text | False | 255 | None | None |
| agent_recruited_movie | False | text | False | 50 | [movie_event_strings_tables](#movie_event_strings_tables) | event |
| gender | False | text | False | 255 | [genders_tables](#genders_tables) | gender |
  
## agent_localisations_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| text | False | text | True | 255 | None | None |
  
## agent_string_faction_overrides_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent | True | text | True | 255 | [agents_tables](#agents_tables) | key |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| gender | True | text | True | 255 | [genders_tables](#genders_tables) | gender |
| name_override | False | text | False | 255 | None | None |
| description_override | False | text | False | 255 | None | None |
| icon_path | False | text | False | 255 | None | None |
  
## agent_string_subculture_overrides_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent | True | text | True | 255 | [agents_tables](#agents_tables) | key |
| subculture | True | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| gender | True | text | True | 255 | [genders_tables](#genders_tables) | gender |
| name_override | False | text | False | 255 | None | None |
| description_override | False | text | False | 255 | None | None |
| icon_path | False | text | False | 255 | None | None |
  
## agent_subculture_gender_overrides_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent | True | text | True | 255 | [agents_tables](#agents_tables) | key |
| subculture | True | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| gender | True | text | True | 255 | [genders_tables](#genders_tables) | gender |
  
## agent_to_agent_abilities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent | True | text | True | 50 | [agents_tables](#agents_tables) | key |
| ability | True | text | True | 50 | [abilities_tables](#abilities_tables) | ability |
| localised_ability_name | False | text | True | 255 | None | None |
| localised_ability_description | False | text | True | 255 | None | None |
  
## agent_to_agent_attributes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| attribute | True | text | True | 50 | [agent_attributes_tables](#agent_attributes_tables) | key |
| agent | True | text | True | 50 | [agents_tables](#agents_tables) | key |
| default_value | False | integer | True | None | None | None |
  
## agent_uniforms_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| uniform_name | True | text | True | 255 | None | None |
| filename | False | text | True | 255 | [variants_tables](#variants_tables) | variant_name |
| battle_filename | False | text | False | 255 | [variants_tables](#variants_tables) | variant_name |
| campaign_porthole_filename | False | text | False | 255 | [variants_tables](#variants_tables) | variant_name |
| audio_armour_type | False | text | True | 255 | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
| audio_weapon_type | False | text | True | 255 | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
| audio_shield_type | False | text | True | 255 | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
| campaign_politician_filename | False | text | False | 255 | None | None |
  
## aide_de_camp_speeches_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| text | False | text | True | 255 | None | None |
| picture_in_picture | False | yesno | True | None | None | None |
| offset_angle | False | double | True | None | None | None |
| offset_range | False | double | True | None | None | None |
| circumvent_cooldown | False | yesno | True | None | None | None |
| cinematic_event | False | text | False | 255 | [battle_cinematic_events_tables](#battle_cinematic_events_tables) | key |
  
## ambient_battlefield_objects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ambient_battlefield_object | True | text | True | 50 | None | None |
  
## ambient_battlefield_objects_junc_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| climate | True | text | True | 50 | [climates_tables](#climates_tables) | climate_type |
| season | True | text | True | 50 | [seasons_tables](#seasons_tables) | season |
| ambient_battlefield_object | True | text | True | 50 | [ambient_battlefield_objects_tables](#ambient_battlefield_objects_tables) | ambient_battlefield_object |
  
## ancillaries_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
| onscreen_name | False | text | True | 255 | None | None |
| type | False | text | True | 255 | [ancillary_types_tables](#ancillary_types_tables) | type |
| applies_to | False | text | True | 50 | None | None |
| transferrable | False | yesno | True | None | None | None |
| unique_to_world | False | yesno | True | None | None | None |
| unique_to_faction | False | yesno | False | None | None | None |
| precedence | False | integer | False | None | None | None |
| start_date | False | integer | True | None | None | None |
| end_date | False | integer | True | None | None | None |
| effect_text | False | text | True | 536870910 | None | None |
| colour_text | False | text | True | 536870910 | None | None |
| explanation_text | False | text | False | 536870910 | None | None |
| exclusion_text | False | text | False | 536870910 | None | None |
| avatar_skill | False | text | False | 255 | None | None |
| avatar_special_ability | False | text | False | 255 | None | None |
| legendary_item | False | yesno | True | None | None | None |
| mp_exclusive | False | yesno | True | None | None | None |
| is_wife_ancillary | False | yesno | True | None | None | None |
| is_husband_ancillary | False | yesno | True | None | None | None |
| is_diplomatic_ancillary | False | yesno | True | None | None | None |
| is_dynastic_ancillary | False | yesno | True | None | None | None |
| spouse_subculture | False | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| category | False | text | True | 255 | [ancillaries_categories_tables](#ancillaries_categories_tables) | category |
| min_starting_age | False | integer | True | None | None | None |
| max_starting_age | False | integer | True | None | None | None |
| min_expiry_age | False | integer | True | None | None | None |
| max_expiry_age | False | integer | True | None | None | None |
| spouse_type | False | text | False | 255 | [marriage_types_tables](#marriage_types_tables) | key |
  
## ancillaries_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| category | True | text | True | 255 | None | None |
  
## ancillary_included_subcultures_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ancillary | True | text | True | 50 | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
| subculture | True | text | True | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## ancillary_info_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ancillary | True | text | True | 50 | None | None |
| historical_example | False | text | False | 50 | None | None |
| author | False | text | True | 50 | None | None |
| comment | False | text | False | 536870910 | None | None |
  
## ancillary_to_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ancillary | True | text | True | 50 | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | double | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## ancillary_to_excluded_ancillaries_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ancillary | True | text | True | 50 | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
| excluded_ancillary | True | text | True | 50 | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
  
## ancillary_to_included_agents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ancillary | True | text | True | 50 | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
| agent | True | text | True | 50 | [agents_tables](#agents_tables) | key |
  
## ancillary_triggers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| trigger | True | text | True | 50 | None | None |
| event | False | text | True | 50 | [trigger_events_tables](#trigger_events_tables) | event |
| conditions | False | text | False | 536870910 | None | None |
  
## ancillary_triggers_to_ancillary_removals_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| trigger | False | text | False | 50 | [ancillary_triggers_tables](#ancillary_triggers_tables) | trigger |
| ancillary | False | text | True | 50 | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
  
## ancillary_trigger_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| trigger | False | text | True | 50 | [ancillary_triggers_tables](#ancillary_triggers_tables) | trigger |
| ancillary | False | text | True | 50 | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
| chance | False | integer | True | None | None | None |
  
## ancillary_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 50 | None | None |
| ui_icon | False | text | True | 50 | None | None |
  
## animals_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| animation | False | text | True | 255 | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| entity | False | text | True | 255 | [battle_entities_tables](#battle_entities_tables) | key |
| melee_attack | False | integer | True | None | None | None |
| melee_defence | False | integer | True | None | None | None |
| charge_bonus | False | integer | True | None | None | None |
| armour | False | text | False | 255 | [unit_armour_types_tables](#unit_armour_types_tables) | key |
  
## animation_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name | True | text | True | 200000 | None | None |
| order | False | integer | True | None | None | None |
  
## animation_slot_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| slot | True | text | True | 200000 | None | None |
| category | True | text | True | 200000 | [animation_categories_tables](#animation_categories_tables) | name |
  
## anim_reference_poses_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| path | False | text | True | 536870910 | None | None |
| root_node | False | text | True | 50 | None | None |
  
## armed_citizenry_units_to_unit_groups_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| unit_group | False | text | True | 255 | [armed_citizenry_unit_groups_tables](#armed_citizenry_unit_groups_tables) | unit_group |
| unit | False | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| priority | False | integer | True | None | None | None |
  
## armed_citizenry_unit_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_group | True | text | True | 255 | None | None |
  
## audio_campaign_building_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## audio_explosions_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## audio_materials_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## audio_projectiles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| audio_projectile_type | False | text | True | 255 | [audio_projectiles_enums_tables](#audio_projectiles_enums_tables) | key |
| play_incoming_sound | False | yesno | True | None | None | None |
| max_attenuation_fire | False | double | True | None | None | None |
| max_attenuation_inflight | False | double | True | None | None | None |
| max_attenuation_impact | False | double | True | None | None | None |
| requires_speed | False | yesno | True | None | None | None |
| requires_distance | False | yesno | True | None | None | None |
| inflight_min_speed | False | double | True | None | None | None |
  
## audio_projectiles_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## audio_vo_actors_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## audio_vo_actor_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| actor_1 | False | text | True | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_2 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_3 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_4 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_5 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_6 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_7 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_8 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_9 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_10 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_11 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_12 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_13 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_14 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
| actor_15 | False | text | False | 255 | [audio_vo_actors_tables](#audio_vo_actors_tables) | key |
  
## audio_vo_selected_switches_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## banditry_events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name | True | text | True | 255 | None | None |
| message_event | False | text | True | 255 | [message_events_tables](#message_events_tables) | event |
| province_effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| minimum_banditry | False | integer | True | None | None | None |
| maximum_banditry | False | integer | True | None | None | None |
| weight | False | integer | True | None | None | None |
| duration | False | integer | True | None | None | None |
  
## battlefield_buildings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| category | False | text | True | 50 | [battlefield_building_categories_tables](#battlefield_building_categories_tables) | category |
| model | False | text | True | 50 | [models_building_tables](#models_building_tables) | key |
| audio_material | False | text | True | 255 | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
| hit_points | False | text | True | 50 | None | None |
| gun_type | False | text | False | 255 | [missile_weapons_tables](#missile_weapons_tables) | key |
| onscreen_name | False | text | False | 50 | [battlefield_buildings_names_tables](#battlefield_buildings_names_tables) | key |
| ignition_threshold | False | integer | True | None | None | None |
| radar_icon | False | text | False | 2000 | None | None |
| visible_in_public_ted | False | yesno | True | None | None | None |
| fortwall_penetration_chance | False | integer | True | None | None | None |
| collision_3d | False | yesno | True | None | None | None |
| destruct_thresholds | False | text | False | 255 | None | None |
| joiner | False | yesno | True | None | None | None |
| auxiliary | False | yesno | True | None | None | None |
| burn_rate | False | single | True | None | None | None |
  
## battlefield_buildings_names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| onscreen_name | False | text | True | 50 | None | None |
| key | True | text | True | 50 | None | None |
| global_effects_description | False | text | False | 255 | None | None |
| local_effects_description | False | text | False | 255 | None | None |
  
## battlefield_buildings_with_projectiles_names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building_category | True | text | True | 255 | [battlefield_building_categories_tables](#battlefield_building_categories_tables) | category |
| projectile | True | text | True | 255 | [projectiles_tables](#projectiles_tables) | key |
| name | False | text | True | 255 | [battlefield_buildings_names_tables](#battlefield_buildings_names_tables) | key |
  
## battlefield_building_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| category | True | text | True | 50 | None | None |
| default_destruction_effect | False | text | True | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| icon_path | False | text | True | 255 | None | None |
  
## battlefield_building_transformations_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| transformation | True | text | True | 50 | None | None |
| description | False | text | False | 255 | None | None |
  
## battlefield_chariots_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| chariot_type | False | text | True | 255 | [chariot_types_enums_tables](#chariot_types_enums_tables) | key |
| model | False | text | True | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
| chariot_animation_table | False | text | True | 255 | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| destruction_animation | False | text | True | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
| destroyed_model | False | text | True | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| battle_entity | False | text | True | 255 | [battle_entities_tables](#battle_entities_tables) | key |
  
## battlefield_deployable_siege_items_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| battlefield_siege_vehicle | False | text | True | 50 | [battlefield_siege_vehicles_tables](#battlefield_siege_vehicles_tables) | key |
| level | False | integer | True | None | None | None |
| type | False | text | False | 255 | None | None |
  
## battlefield_engines_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| engine_type | False | text | True | 255 | [gun_types_enum_tables](#gun_types_enum_tables) | key |
| model | False | text | True | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
| gun_animation_table | False | text | True | 255 | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| missile_weapon | False | text | False | 255 | [missile_weapons_tables](#missile_weapons_tables) | key |
| destruction_animation | False | text | False | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
| destroyed_model | False | text | False | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| battle_entity | False | text | True | 50 | [battle_entities_tables](#battle_entities_tables) | key |
| can_move | False | yesno | True | None | None | None |
  
## battlefield_engines_autonomous_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| autonomous_engine_type | False | text | True | 255 | [battlefield_engines_tables](#battlefield_engines_tables) | key |
| engine_crew_entity | False | text | True | 255 | [battle_entities_tables](#battle_entities_tables) | key |
| engine_crew_anims | False | text | True | 255 | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| num_ammo | False | integer | True | None | None | None |
  
## battlefield_siege_vehicles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| model | False | text | True | 50 | [models_sieges_tables](#models_sieges_tables) | key |
| hit_points | False | integer | True | None | None | None |
| battle_entity | False | text | True | 50 | [battle_entities_tables](#battle_entities_tables) | key |
| gun_type | False | text | False | 255 | None | None |
| docking_clearance | False | double | True | None | None | None |
| engine | False | text | False | 255 | [battlefield_engines_autonomous_tables](#battlefield_engines_autonomous_tables) | key |
| onscreen_name | False | text | False | 255 | None | None |
| description | False | text | False | 255 | None | None |
| image_path | False | text | True | 255 | None | None |
| recruitment_cap | False | integer | True | None | None | None |
| uses_8m_wall | False | yesno | True | None | None | None |
| uses_15m_wall | False | yesno | True | None | None | None |
| cost | False | integer | True | None | None | None |
| category_image_path | False | text | True | 255 | None | None |
| special_edition_mask | False | integer | True | None | None | None |
| ignition_threshold | False | integer | True | None | None | None |
| attack_damage | False | double | True | None | None | None |
| selection_priority | False | double | True | None | None | None |
  
## battlefield_siege_vehicles_custom_battles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| vehicle | True | text | True | 255 | [battlefield_siege_vehicles_tables](#battlefield_siege_vehicles_tables) | key |
| cap | False | integer | True | None | None | None |
| probability | False | decimal | True | None | None | None |
  
## battlefield_siege_vehicles_to_autonomous_engines_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| vehicle | True | text | True | 255 | [battlefield_siege_vehicles_tables](#battlefield_siege_vehicles_tables) | key |
| engine | True | text | True | 255 | [battlefield_engines_autonomous_tables](#battlefield_engines_autonomous_tables) | key |
  
## battlefield_snow_props_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| prop | True | text | True | 50 | [battlefield_buildings_tables](#battlefield_buildings_tables) | key |
| enable_for_snow | True | yesno | True | None | [seasons_tables](#seasons_tables) | season |
  
## battlefield_temperatures_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| climate | True | text | True | 50 | [climates_tables](#climates_tables) | climate_type |
| season | True | text | True | 50 | [seasons_tables](#seasons_tables) | season |
| temperature | False | text | True | 50 | None | None |
  
## battles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| type | False | text | True | 255 | [battle_types_tables](#battle_types_tables) | type |
| is_naval | False | yesno | True | None | None | None |
| specification | False | text | True | 255 | None | None |
| localised_name | False | text | True | 255 | None | None |
| description | False | text | True | 536870910 | None | None |
| objectives_team_1 | False | text | True | 536870910 | None | None |
| objectives_team_2 | False | text | False | 536870910 | None | None |
| screenshot_path | False | text | False | 255 | None | None |
| map_path | False | text | False | 255 | None | None |
| team_size_1 | False | integer | True | None | None | None |
| team_size_2 | False | integer | True | None | None | None |
| release | False | yesno | False | None | None | None |
| multiplayer | False | yesno | False | None | None | None |
| singleplayer | False | yesno | False | None | None | None |
| intro_movie | False | text | False | 255 | None | None |
| year | False | integer | True | None | None | None |
| defender_funds_ratio | False | double | True | None | None | None |
| has_key_buildings | False | yesno | False | None | None | None |
| matchmaking | False | yesno | True | None | None | None |
| playable_area_width | False | double | True | None | None | None |
| playable_area_height | False | double | True | None | None | None |
| is_large_settlement | False | yesno | True | None | None | None |
| has_15m_walls | False | yesno | True | None | None | None |
  
## battles_to_battle_sky_types_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle_key | True | text | True | 255 | [battles_tables](#battles_tables) | key |
| battle_sky_type_key | True | text | True | 255 | [battle_sky_types_tables](#battle_sky_types_tables) | key |
  
## battle_animations_table_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## battle_autoresolver_balances_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| source_unit_class | True | text | True | 50 | [unit_class_tables](#unit_class_tables) | key |
| target_unit_class | True | text | True | 50 | [unit_class_tables](#unit_class_tables) | key |
| melee_potential_multiplier | False | single | True | None | None | None |
| missile_potential_multiplier | False | single | True | None | None | None |
  
## battle_bridge_subculture_jcts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| subculture | True | text | True | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| simple_bridge | False | text | True | 50 | [battlefield_buildings_tables](#battlefield_buildings_tables) | key |
| refined_bridge | False | text | True | 50 | [battlefield_buildings_tables](#battlefield_buildings_tables) | key |
  
## battle_cameras_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| min_height | False | single | True | None | None | None |
| max_height_small | False | single | True | None | None | None |
| max_height_large | False | single | True | None | None | None |
| min_fort_max_height | False | single | True | None | None | None |
| move_speed_min_multiplier | False | single | True | None | None | None |
| move_speed_max_multiplier | False | single | True | None | None | None |
| turn_speed_multiplier | False | single | True | None | None | None |
| move_fast_multiplier | False | single | True | None | None | None |
  
## battle_cinematic_events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| filename | False | text | True | 255 | None | None |
| priority | False | integer | True | None | None | None |
| level | False | text | True | 255 | None | None |
| window_in | False | integer | True | None | None | None |
| window_out | False | integer | True | None | None | None |
| repeat_wait_ms | False | integer | True | None | None | None |
| event_category | False | text | True | 255 | [battle_cinematic_event_categories_tables](#battle_cinematic_event_categories_tables) | key |
| time_after_event | False | integer | True | None | None | None |
  
## battle_cinematic_event_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## battle_cities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| city | True | text | True | 50 | None | None |
| minimum_building_scale | False | decimal | True | None | None | None |
| maximum_building_scale | False | decimal | True | None | None | None |
| town_min_distance | False | integer | True | None | None | None |
| city_min_distance | False | integer | True | None | None | None |
| town_radius | False | integer | True | None | None | None |
| city_radius | False | integer | True | None | None | None |
| number_of_town_buildings | False | integer | True | None | None | None |
| number_of_city_buildings | False | integer | True | None | None | None |
  
## battle_city_buildings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building | True | text | True | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| city | False | text | True | 50 | [battle_cities_tables](#battle_cities_tables) | city |
| amount_in_town | False | integer | True | None | None | None |
| amount_in_city | False | integer | True | None | None | None |
  
## battle_city_subculture_jct_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| subculture | True | text | True | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| city | False | text | True | 50 | [battle_cities_tables](#battle_cities_tables) | city |
  
## battle_climate_weather_descriptions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | False | text | True | 50 | None | None |
| climate_type | True | text | True | 50 | [climates_tables](#climates_tables) | climate_type |
| season | True | text | False | 50 | [seasons_tables](#seasons_tables) | season |
| weather_type | True | text | True | 50 | [battle_weather_types_tables](#battle_weather_types_tables) | key |
| probability | False | integer | True | None | None | None |
| heat_fatigue | False | integer | True | None | None | None |
| cold_fatigue | False | integer | True | None | None | None |
| spotting_scalar | False | double | True | None | None | None |
  
## battle_difficulty_modifiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| difficulty_level | True | text | True | 255 | None | None |
| human | True | yesno | True | None | None | None |
| stat | True | text | True | 255 | None | None |
| value | False | text | False | 255 | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
  
## battle_entities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| type | False | text | False | 50 | [battle_entities_types_enum_tables](#battle_entities_types_enum_tables) | key |
| walk_speed | False | single | True | None | None | None |
| run_speed | False | single | True | None | None | None |
| acceleration | False | single | True | None | None | None |
| deceleration | False | single | True | None | None | None |
| charge_speed | False | single | True | None | None | None |
| crawl_speed | False | single | True | None | None | None |
| charge_distance_commence_run | False | single | True | None | None | None |
| charge_distance_adopt_charge_pose | False | single | True | None | None | None |
| charge_distance_pick_target | False | single | True | None | None | None |
| radius | False | single | True | None | None | None |
| shape | False | text | True | 50 | [battle_entities_shape_enum_tables](#battle_entities_shape_enum_tables) | key |
| radii_ratio | False | single | True | None | None | None |
| mass | False | single | True | None | None | None |
| height | False | single | True | None | None | None |
| fire_arc_close | False | integer | False | None | None | None |
| fire_arc_loose | False | integer | False | None | None | None |
| turn_speed | False | integer | False | None | None | None |
| hit_points | False | integer | True | None | None | None |
| allow_turn_to_move_anim | False | yesno | True | None | None | None |
| allow_static_turn_anim | False | yesno | True | None | None | None |
| tracking_threshold | False | single | True | None | None | None |
| min_turning_speed | False | single | True | None | None | None |
| display_model_offset_z | False | single | True | None | None | None |
  
## battle_entities_class_validation_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## battle_entities_shape_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## battle_entities_types_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## battle_entity_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name | True | text | True | 255 | None | None |
| forest | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| grass | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| mud | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| sand | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| scrub | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| rock | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| deep_water | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| shallow_water | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| road | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| wooden_floor | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| snow | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
  
## battle_misc_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name | True | text | True | 255 | None | None |
| effect | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
  
## battle_personalities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| soldier_model | False | text | True | 50 | [warscape_animated_tables](#warscape_animated_tables) | key |
| man_animations_table | False | text | True | 50 | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| type | False | text | False | 50 | [battle_personality_types_enum_tables](#battle_personality_types_enum_tables) | key |
| missile_type | False | text | False | 255 | [projectiles_tables](#projectiles_tables) | key |
| variant | False | text | True | 255 | [variants_tables](#variants_tables) | variant_name |
  
## battle_personality_types_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## battle_sequences_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle | True | text | False | 255 | [battles_tables](#battles_tables) | key |
| unlock_order | False | integer | False | None | None | None |
  
## battle_siege_vehicle_permissions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| vehicle | True | text | True | 255 | [battlefield_siege_vehicles_tables](#battlefield_siege_vehicles_tables) | key |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## battle_skeletons_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name | True | text | True | 255 | None | None |
| category | False | text | True | 255 | [battle_skeleton_category_enums_tables](#battle_skeleton_category_enums_tables) | type |
| root | False | text | True | 255 | None | None |
| scale | False | single | True | None | None | None |
| scale_deviation | False | single | True | None | None | None |
| hips_node | False | text | False | 255 | None | None |
| spine_node | False | text | False | 255 | None | None |
| weapon1_node | False | text | False | 255 | None | None |
| weapon2_node | False | text | False | 255 | None | None |
| weapon3_node | False | text | False | 255 | None | None |
| weapon4_node | False | text | False | 255 | None | None |
| weapon5_node | False | text | False | 255 | None | None |
| head_node | False | text | False | 255 | None | None |
| neck_node | False | text | False | 255 | None | None |
| leftshoulder_node | False | text | False | 255 | None | None |
| rightshoulder_node | False | text | False | 255 | None | None |
| leftarm_node | False | text | False | 255 | None | None |
| rightarm_node | False | text | False | 255 | None | None |
| lefthand_node | False | text | False | 255 | None | None |
| righthand_node | False | text | False | 255 | None | None |
| leftupleg_node | False | text | False | 255 | None | None |
| rightupleg_node | False | text | False | 255 | None | None |
| leftleg_node | False | text | False | 255 | None | None |
| rightleg_node | False | text | False | 255 | None | None |
| leftfoot_node | False | text | False | 255 | None | None |
| rightfoot_node | False | text | False | 255 | None | None |
| leftfinger_node | False | text | False | 255 | None | None |
| rightfinger_node | False | text | False | 255 | None | None |
| lefttoe_node | False | text | False | 255 | None | None |
| righttoe_node | False | text | False | 255 | None | None |
| leftwheel_node | False | text | False | 255 | None | None |
| rightwheel_node | False | text | False | 255 | None | None |
  
## battle_skeleton_category_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 255 | None | None |
  
## battle_sky_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 100 | None | None |
| season | False | text | True | 50 | [seasons_tables](#seasons_tables) | season |
| weather_type | False | text | True | 50 | [battle_weather_types_tables](#battle_weather_types_tables) | key |
| time_of_day | False | text | True | 50 | None | None |
| climate | False | text | False | 50 | [climates_tables](#climates_tables) | climate_type |
| sky_file | False | text | True | 50 | None | None |
| supports_ambient_fog | False | yesno | True | None | None | None |
| supports_volumetric_fog | False | yesno | True | None | None | None |
  
## battle_terrain_farms_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| farm | True | text | True | 50 | None | None |
| tile_model | False | text | True | 150 | None | None |
| colour_map_model | False | text | True | 150 | None | None |
| blend_map_model | False | text | True | 150 | None | None |
| grass_map_model | False | text | True | 150 | None | None |
| alternate_colour_map_model | False | text | True | 150 | None | None |
| alternate_blend_map_model | False | text | True | 150 | None | None |
| alternate_grass_map_model | False | text | True | 150 | None | None |
| road_colour_map_model | False | text | True | 150 | None | None |
| road_blend_map_model | False | text | True | 150 | None | None |
| road_grass_map_model | False | text | True | 150 | None | None |
| tile_map | False | text | False | 100 | None | None |
| wall_texture | False | text | True | 50 | None | None |
| wall_end | False | text | True | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| wall_cross_section | False | text | True | 50 | None | None |
  
## battle_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 255 | None | None |
| onscreen | False | text | False | 255 | None | None |
| sort_order | False | integer | True | None | None | None |
| defender_funds_ratio | False | double | True | None | None | None |
| max_teamsize | False | integer | True | None | None | None |
  
## battle_types_to_victory_conditions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle_type | True | text | True | 255 | [battle_types_tables](#battle_types_tables) | type |
| attacker_victory_condition | True | text | False | 20000 | [victory_conditions_tables](#victory_conditions_tables) | condition |
| defender_victory_condition | True | text | False | 20000 | [victory_conditions_tables](#victory_conditions_tables) | condition |
  
## battle_type_faction_presets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| weighting_type | True | integer | True | None | [battle_type_setup_limits_tables](#battle_type_setup_limits_tables) | id |
| id | False | autonumber | False | None | None | None |
  
## battle_type_setup_limits_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle_type | True | text | True | 255 | [battle_types_tables](#battle_types_tables) | type |
| weighting_type | True | text | True | 255 | None | None |
| army_size | True | text | False | 255 | None | None |
| era | True | text | False | 255 | None | None |
| max_infantry | False | integer | True | None | None | None |
| max_cavalry | False | integer | True | None | None | None |
| max_artillery | False | integer | True | None | None | None |
| max_small_ship | False | integer | True | None | None | None |
| max_frigate | False | integer | True | None | None | None |
| max_line_of_battle | False | integer | True | None | None | None |
| id | False | autonumber | True | None | None | None |
  
## battle_unit_permission_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| battle_type | True | text | True | 255 | [battle_types_tables](#battle_types_tables) | type |
  
## battle_weather_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| weather_type | True | text | True | 50 | [battle_weather_types_tables](#battle_weather_types_tables) | key |
| stat | True | text | True | 255 | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| value | False | integer | True | None | None | None |
  
## battle_weather_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| level | False | integer | True | None | None | None |
| precipitation_type | False | text | True | 50 | None | None |
| num_particles | False | integer | True | None | None | None |
| particle_size | False | single | True | None | None | None |
| particle_speed | False | single | True | None | None | None |
| onscreen | False | text | False | 255 | None | None |
| list_order | False | integer | False | None | None | None |
| naval_appropriate | False | yesno | False | None | None | None |
  
## building_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 255 | None | None |
  
## building_chains_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| tech_category_tab | False | text | False | 255 | None | None |
| tech_category_position | False | integer | False | None | None | None |
| chain_category | False | text | False | 50 | None | None |
| chain_tooltip | False | text | True | 536870910 | None | None |
| in_encyclopedia | False | yesno | True | None | None | None |
| building_superchain | False | text | False | 255 | [building_superchains_tables](#building_superchains_tables) | key |
| encyclopedia_description | False | text | True | 65535 | None | None |
| encyclopedia_group | False | text | False | 255 | [encyclopedia_building_chain_groups_tables](#encyclopedia_building_chain_groups_tables) | group_name |
| encyclopedia_include_in_index | False | yesno | True | None | None | None |
| encyclopedia_name | False | text | True | 255 | None | None |
  
## building_chain_availabilities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| set_id | False | text | True | 255 | [building_chain_availability_set_ids_tables](#building_chain_availability_set_ids_tables) | id |
| culture | False | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| sub_culture | False | text | False | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| faction | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| campaign | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## building_chain_availability_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | [building_chain_availability_set_ids_tables](#building_chain_availability_set_ids_tables) | id |
| building_chain | True | text | True | 255 | [building_chains_tables](#building_chains_tables) | key |
  
## building_chain_availability_set_ids_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
  
## building_chain_to_slots_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| chain | True | text | True | 50 | [building_chains_tables](#building_chains_tables) | key |
| slot | True | text | True | 50 | [slots_tables](#slots_tables) | slot |
  
## building_culture_gov_type_variants_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| government_type | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| name | False | text | True | 50 | None | None |
| artpiece | False | text | False | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| artpiece_animated | False | text | False | 50 | [warscape_animated_tables](#warscape_animated_tables) | key |
| description | False | text | True | 50 | [building_description_texts_tables](#building_description_texts_tables) | key |
| icon | False | text | True | 50 | None | None |
| short_description | False | text | True | 255 | [building_short_description_texts_tables](#building_short_description_texts_tables) | key |
  
## building_culture_variants_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| name | False | text | True | 50 | None | None |
| battlefield_building | False | text | False | 50 | [battlefield_buildings_tables](#battlefield_buildings_tables) | key |
| artpiece | False | text | False | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| artpiece_animated | False | text | False | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
| description | False | text | False | 50 | [building_description_texts_tables](#building_description_texts_tables) | key |
| icon | False | text | True | 50 | None | None |
| subculture | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| disables | False | yesno | True | None | None | None |
| short_description | False | text | False | 255 | [building_short_description_texts_tables](#building_short_description_texts_tables) | key |
| flavour | False | text | False | 255 | [building_flavour_texts_tables](#building_flavour_texts_tables) | key |
| display_tooltip | False | yesno | True | None | None | None |
  
## building_description_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| long_description | False | text | False | 536870910 | None | None |
  
## building_effects_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | double | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| value_damaged | False | double | True | None | None | None |
| value_ruined | False | double | True | None | None | None |
  
## building_factionwide_effects_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| effect_value | False | integer | True | None | None | None |
  
## building_faction_variants_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| onscreen_name | False | text | True | 255 | None | None |
| artpiece | False | text | True | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| description | False | text | True | 50 | [building_description_texts_tables](#building_description_texts_tables) | key |
| icon | False | text | True | 50 | None | None |
| short_description | False | text | True | 255 | [building_short_description_texts_tables](#building_short_description_texts_tables) | key |
  
## building_flavour_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| flavour | False | text | True | 255 | None | None |
  
## building_instances_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| num_instances | False | integer | True | None | None | None |
  
## building_levels_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| level_name | True | text | True | 50 | None | None |
| chain | False | text | True | 50 | [building_chains_tables](#building_chains_tables) | key |
| level | False | integer | True | None | None | None |
| condition | False | text | False | 536870910 | None | None |
| only_in_capital | False | yesno | False | None | None | None |
| create_time | False | integer | True | None | None | None |
| create_cost | False | integer | True | None | None | None |
| upkeep_cost | False | integer | True | None | None | None |
| demolition_cost | False | integer | True | None | None | None |
| zoc | False | double | True | None | None | None |
| lower_happiness | False | integer | True | None | None | None |
| upper_happiness | False | integer | True | None | None | None |
| repression | False | integer | True | None | None | None |
| gdp | False | integer | True | None | None | None |
| town_wealth_growth | False | integer | True | None | None | None |
| pop_change | False | double | True | None | None | None |
| maxpop_change | False | double | True | None | None | None |
| commodity | False | text | False | 50 | [commodities_tables](#commodities_tables) | key |
| commodity_vol | False | integer | True | None | None | None |
| building_category | False | text | False | 255 | [building_categories_tables](#building_categories_tables) | key |
| gov_type_key | False | text | False | 50 | [government_types_tables](#government_types_tables) | government_type |
| military_prestige | False | integer | False | None | None | None |
| naval_prestige | False | integer | False | None | None | None |
| economic_prestige | False | integer | False | None | None | None |
| enlightenment_prestige | False | integer | False | None | None | None |
| destruction_terminator | False | yesno | True | None | None | None |
| faction_unique | False | yesno | True | None | None | None |
| religion_requirement | False | text | False | 1024 | [religions_tables](#religions_tables) | religion_key |
| first_in_world_bundle | False | text | False | 1024 | [effect_bundles_tables](#effect_bundles_tables) | key |
| resource_requirement | False | text | False | 1024 | [resources_tables](#resources_tables) | key |
| working_model | False | text | True | 1024 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| unique_index | False | autonumber | True | None | None | None |
| can_convert | False | yesno | True | None | None | None |
| building_instance_key | False | text | False | 255 | [building_instances_tables](#building_instances_tables) | key |
| audio_building_type | False | text | True | 255 | [audio_campaign_building_enums_tables](#audio_campaign_building_enums_tables) | key |
| should_show_building_level_in_ui_for_technology | False | yesno | True | None | None | None |
| is_new | False | yesno | True | None | None | None |
  
## building_level_armed_citizenry_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| building_level | False | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| unit_group | False | text | True | 255 | [armed_citizenry_unit_groups_tables](#armed_citizenry_unit_groups_tables) | unit_group |
  
## building_level_required_technology_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building_level_key | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| technology_key | True | text | True | 255 | [technologies_tables](#technologies_tables) | key |
  
## building_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## building_set_to_building_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building_set | True | text | True | 255 | [building_sets_tables](#building_sets_tables) | key |
| building_level | True | text | False | 255 | [building_levels_tables](#building_levels_tables) | level_name |
| building_chain | True | text | False | 255 | [building_chains_tables](#building_chains_tables) | key |
| exclude | False | yesno | True | None | None | None |
  
## building_short_description_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| short_description | False | text | True | 255 | None | None |
  
## building_states_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## building_superchains_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| max_instances_per_region | False | integer | True | None | None | None |
  
## building_to_unit_abilities_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building_name | True | text | True | 50 | [battlefield_buildings_tables](#battlefield_buildings_tables) | key |
| ability | True | text | True | 50 | [unit_abilities_tables](#unit_abilities_tables) | key |
  
## building_units_allowed_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building | False | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| unit | False | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| XP | False | integer | True | None | None | None |
| conditions | False | text | False | 536870910 | None | None |
| key | True | autonumber | True | None | None | None |
| faction | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| enabled | False | yesno | False | None | None | None |
  
## building_upgrades_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| from | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| to | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
  
## cai_agent_distribution_profiles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_agent_distribution_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_agent_record_to_cai_agent_type_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent_type_key | True | text | True | 255 | [cai_agent_types_tables](#cai_agent_types_tables) | key |
| agent_record_key | True | text | True | 255 | [agents_tables](#agents_tables) | key |
  
## cai_agent_recruitment_profiles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_agent_recruitment_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_agent_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_agent_type_distribution_profile_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| distribution_profile_key | True | text | True | 255 | [cai_agent_distribution_profiles_tables](#cai_agent_distribution_profiles_tables) | key |
| agent_type_key | True | text | True | 255 | [cai_agent_types_tables](#cai_agent_types_tables) | key |
| distribution_type_key | True | text | True | 255 | [cai_agent_distribution_types_tables](#cai_agent_distribution_types_tables) | key |
  
## cai_agent_type_recruitment_profile_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| recruitment_profile_key | True | text | True | 255 | [cai_agent_recruitment_profiles_tables](#cai_agent_recruitment_profiles_tables) | key |
| agent_type_key | True | text | True | 255 | [cai_agent_types_tables](#cai_agent_types_tables) | key |
| recruitment_type_key | True | text | True | 255 | [cai_agent_recruitment_types_tables](#cai_agent_recruitment_types_tables) | key |
  
## cai_base_building_context_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building_key | True | text | True | 1024 | [building_levels_tables](#building_levels_tables) | level_name |
| economic_value | False | double | True | None | None | None |
| military_value | False | double | True | None | None | None |
| happiness_value | False | double | True | None | None | None |
| prestige_value | False | double | True | None | None | None |
| education_value | False | double | True | None | None | None |
| existing_buildings_apply_discount_over_limit | False | double | True | None | None | None |
| existing_buildings_discount_per_building | False | double | True | None | None | None |
| existing_buildings_maximum_discount | False | double | True | None | None | None |
  
## cai_construction_system_building_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign | True | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| sub_culture | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| culture | True | text | False | 255 | [cultures_tables](#cultures_tables) | key |
| building_or_building_range_start_inclusive | True | text | False | 255 | [building_levels_tables](#building_levels_tables) | level_name |
| building_range_end_inclusive | True | text | False | 255 | [building_levels_tables](#building_levels_tables) | level_name |
| building_instance | True | text | False | 255 | [building_instances_tables](#building_instances_tables) | key |
| building_chain | True | text | False | 255 | [building_chains_tables](#building_chains_tables) | key |
| building_super_chain | True | text | False | 255 | [building_superchains_tables](#building_superchains_tables) | key |
| cai_construction_system_category | True | text | False | 255 | [cai_construction_system_categories_tables](#cai_construction_system_categories_tables) | key |
| cai_construction_system_category_group | True | text | False | 255 | [cai_construction_system_category_groups_tables](#cai_construction_system_category_groups_tables) | key |
| score_or_score_start_inclusive | False | integer | True | None | None | None |
| score_end_inclusive | False | integer | True | None | None | None |
| per_province_building_limit_start | False | integer | True | None | None | None |
| per_province_building_minimum_discount_when_exceeding_limit_start | False | integer | True | None | None | None |
| per_province_building_maximum_discount_when_exceeding_limit_start | False | integer | True | None | None | None |
| per_province_per_building_discount_increment_when_exceeding_limit_start | False | integer | True | None | None | None |
| per_province_building_limit_end | False | integer | True | None | None | None |
| per_province_building_minimum_discount_when_exceeding_limit_end | False | integer | True | None | None | None |
| per_province_building_maximum_discount_when_exceeding_limit_end | False | integer | True | None | None | None |
| per_province_per_building_discount_increment_when_exceeding_limit_end | False | integer | True | None | None | None |
| per_faction_building_limit_start | False | integer | True | None | None | None |
| per_faction_building_minimum_discount_when_exceeding_limit_start | False | integer | True | None | None | None |
| per_faction_building_maximum_discount_when_exceeding_limit_start | False | integer | True | None | None | None |
| per_faction_per_building_discount_increment_when_exceeding_limit_start | False | integer | True | None | None | None |
| per_faction_building_limit_end | False | integer | True | None | None | None |
| per_faction_building_minimum_discount_when_exceeding_limit_end | False | integer | True | None | None | None |
| per_faction_building_maximum_discount_when_exceeding_limit_end | False | integer | True | None | None | None |
| per_faction_per_building_discount_increment_when_exceeding_limit_end | False | integer | True | None | None | None |
  
## cai_construction_system_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| cai_construction_system_category_group | False | text | True | 255 | [cai_construction_system_category_groups_tables](#cai_construction_system_category_groups_tables) | key |
| cdir_military_generator_unit_group | False | text | False | 255 | [cdir_military_generator_unit_groups_tables](#cdir_military_generator_unit_groups_tables) | key |
  
## cai_construction_system_category_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_construction_system_province_template_assignment_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| capital_province_template | False | text | True | 255 | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| military_province_template | False | text | True | 255 | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| economic_province_template | False | text | True | 255 | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| military_port_province_template | False | text | True | 255 | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| economic_port_province_template | False | text | True | 255 | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| non_port_province_military_ideal_percentage | False | integer | True | None | None | None |
| port_province_military_ideal_percentage | False | integer | True | None | None | None |
  
## cai_construction_system_strategic_context_template_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| default_cai_construction_system_template | False | text | True | 255 | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
  
## cai_construction_system_strategic_context_template_policy_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| cai_construction_system_strategic_context_policy | True | text | True | 255 | [cai_construction_system_strategic_context_template_policies_tables](#cai_construction_system_strategic_context_template_policies_tables) | key |
| cai_strategic_context | True | text | True | 255 | [cai_strategic_context_types_tables](#cai_strategic_context_types_tables) | key |
| cai_construction_system_template | True | text | True | 255 | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
  
## cai_construction_system_superchain_hints_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| super_chain_key | True | text | True | 255 | [building_superchains_tables](#building_superchains_tables) | key |
| military_specialisation_recommended | False | yesno | True | None | None | None |
| economic_specialisation_recommended | False | yesno | True | None | None | None |
  
## cai_construction_system_synergies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| synergy_policy_key | True | text | True | 2000 | [cai_construction_system_synergy_policies_tables](#cai_construction_system_synergy_policies_tables) | key |
| existing_building_chain_key | True | text | False | 50 | [building_chains_tables](#building_chains_tables) | key |
| existing_building_level_inclusive_start | True | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| existing_building_level_inclusive_end | True | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| potential_buiding_chain_key | True | text | False | 50 | [building_chains_tables](#building_chains_tables) | key |
| potential_building_level_inclusive_start | True | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| potential_building_level_inclusive_end | True | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| synergy_level_key | False | text | True | 2000 | [cai_construction_system_synergy_levels_tables](#cai_construction_system_synergy_levels_tables) | key |
| existing_building_instance | True | text | False | 255 | [building_instances_tables](#building_instances_tables) | key |
| existing_building_super_chain | True | text | True | 255 | [building_superchains_tables](#building_superchains_tables) | key |
| potential_building_instance | True | text | False | 255 | [building_instances_tables](#building_instances_tables) | key |
| potential_building_super_chain | True | text | True | 255 | [building_superchains_tables](#building_superchains_tables) | key |
  
## cai_construction_system_synergy_levels_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 2000 | None | None |
| relative_effect | False | single | True | None | None | None |
| absolute_effect | False | single | True | None | None | None |
| priority | False | integer | True | None | None | None |
  
## cai_construction_system_synergy_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 2000 | None | None |
  
## cai_construction_system_templates_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| default_category_and_group_value | False | double | True | None | None | None |
  
## cai_construction_system_templates_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| cai_construction_system_template | True | text | True | 255 | [cai_construction_system_templates_tables](#cai_construction_system_templates_tables) | key |
| cai_construction_system_category | True | text | False | 255 | [cai_construction_system_categories_tables](#cai_construction_system_categories_tables) | key |
| cai_construction_system_category_group | True | text | False | 255 | [cai_construction_system_category_groups_tables](#cai_construction_system_category_groups_tables) | key |
| value | False | double | True | None | None | None |
  
## cai_diplomacy_complex_treacheries_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| first_event | True | text | True | 255 | [cai_personality_diplomatic_events_tables](#cai_personality_diplomatic_events_tables) | id |
| second_event | True | text | True | 255 | [cai_personality_diplomatic_events_tables](#cai_personality_diplomatic_events_tables) | id |
| max_turn_difference | False | integer | True | None | None | None |
| value | False | single | True | None | None | None |
  
## cai_diplomacy_simple_treacheries_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| event | True | text | True | 255 | [cai_personality_diplomatic_events_tables](#cai_personality_diplomatic_events_tables) | id |
| value | False | single | True | None | None | None |
  
## cai_military_aggressiveness_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_military_behaviour_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_personalities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| budget_policy_key | False | text | True | 255 | [cai_personalities_budget_policies_tables](#cai_personalities_budget_policies_tables) | key |
| technology_manager_key | False | text | True | 255 | [campaign_ai_technology_managers_tables](#campaign_ai_technology_managers_tables) | key |
| character_skill_tree_manager_key | False | text | True | 255 | [campaign_ai_character_skill_tree_managers_tables](#campaign_ai_character_skill_tree_managers_tables) | key |
| agent_distribution_profile_key | False | text | True | 255 | [cai_agent_distribution_profiles_tables](#cai_agent_distribution_profiles_tables) | key |
| agent_recruitment_profile_key | False | text | True | 255 | [cai_agent_recruitment_profiles_tables](#cai_agent_recruitment_profiles_tables) | key |
| reliability_policy_key | False | text | True | 255 | [cai_personalities_reliability_policies_tables](#cai_personalities_reliability_policies_tables) | key |
| religious_conversion_policy | False | text | True | 255 | [cai_personalities_religious_conversion_policies_tables](#cai_personalities_religious_conversion_policies_tables) | key |
| military_aggressiveness_policy | False | text | True | 255 | [cai_military_aggressiveness_policies_tables](#cai_military_aggressiveness_policies_tables) | key |
| military_behaviour_policy | False | text | True | 255 | [cai_military_behaviour_policies_tables](#cai_military_behaviour_policies_tables) | key |
| allowed_for_random_selection | False | yesno | True | None | None | None |
| diplomatic_component | False | text | True | 255 | [cai_personality_diplomatic_components_tables](#cai_personality_diplomatic_components_tables) | id |
| strategic_component | False | text | True | 255 | [cai_personality_strategic_components_tables](#cai_personality_strategic_components_tables) | id |
| cultural_component | False | text | True | 255 | [cai_personality_cultural_components_tables](#cai_personality_cultural_components_tables) | id |
| deal_evaluation_component | False | text | True | 255 | [cai_personality_deal_evaluation_components_tables](#cai_personality_deal_evaluation_components_tables) | id |
| deal_generation_component | False | text | True | 255 | [cai_personality_deal_generation_components_tables](#cai_personality_deal_generation_components_tables) | id |
| construction_system_policy | False | text | True | 255 | [cai_personalities_construction_system_policies_tables](#cai_personalities_construction_system_policies_tables) | key |
| task_management_system_task_generation_profile | False | text | True | 255 | [cai_personalities_task_management_system_task_generator_profiles_tables](#cai_personalities_task_management_system_task_generator_profiles_tables) | key |
| negotiation_component | False | text | True | 255 | [cai_personality_negotiation_components_tables](#cai_personality_negotiation_components_tables) | id |
| income_allocation_policy | False | text | True | 255 | [cai_personalities_income_allocation_policies_tables](#cai_personalities_income_allocation_policies_tables) | key |
| occupation_decision_component | False | text | True | 255 | [cai_personality_occupation_decision_components_tables](#cai_personality_occupation_decision_components_tables) | id |
  
## cai_personalities_budget_allocations_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| army_funds_allocation_percentage | False | integer | True | None | None | None |
| army_turns_of_inactivity_until_cap | False | integer | True | None | None | None |
| army_funding_cap | False | integer | True | None | None | None |
| army_percentage_of_pool_to_save_on_fail | False | integer | True | None | None | None |
| navy_funds_allocation_percentage | False | integer | True | None | None | None |
| navy_turns_of_inactivity_until_cap | False | integer | True | None | None | None |
| navy_funding_cap | False | integer | True | None | None | None |
| navy_percentage_of_pool_to_save_on_fail | False | integer | True | None | None | None |
| agents_funds_allocation_percentage | False | integer | True | None | None | None |
| agents_turns_of_inactivity_until_cap | False | integer | True | None | None | None |
| agents_funding_cap | False | integer | True | None | None | None |
| agents_percentage_of_pool_to_save_on_fail | False | integer | True | None | None | None |
| construction_funds_allocation_percentage | False | integer | True | None | None | None |
| construction_turns_of_inactivity_until_cap | False | integer | True | None | None | None |
| construction_funding_cap | False | integer | True | None | None | None |
| construction_percentage_of_pool_to_save_on_fail | False | integer | True | None | None | None |
| diplomacy_funds_allocation_percentage | False | integer | True | None | None | None |
| diplomacy_turns_of_inactivity_until_cap | False | integer | True | None | None | None |
| diplomacy_funding_cap | False | integer | True | None | None | None |
| diplomacy_percentage_of_pool_to_save_on_fail | False | integer | True | None | None | None |
| minimum_settable_tax_level | False | text | True | 50 | [taxes_levels_tables](#taxes_levels_tables) | tax_level |
| maximum_settable_tax_level | False | text | True | 50 | [taxes_levels_tables](#taxes_levels_tables) | tax_level |
| technology_funds_allocation_percentage | False | integer | True | None | None | None |
| technology_turns_of_inactivity_until_cap | False | integer | True | None | None | None |
| technology_funding_cap | False | integer | True | None | None | None |
| technology_percentage_of_pool_to_save_on_fail | False | integer | True | None | None | None |
  
## cai_personalities_budget_allocation_policy_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| budget_policy_key | True | text | True | 255 | [cai_personalities_budget_policies_tables](#cai_personalities_budget_policies_tables) | key |
| budget_context_key | True | text | True | 255 | [cai_strategic_context_types_tables](#cai_strategic_context_types_tables) | key |
| budget_allocation_key | True | text | True | 255 | [cai_personalities_budget_allocations_tables](#cai_personalities_budget_allocations_tables) | key |
| priority | False | integer | True | None | None | None |
  
## cai_personalities_budget_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| default_budget_allocation_key | False | text | True | 255 | [cai_personalities_budget_allocations_tables](#cai_personalities_budget_allocations_tables) | key |
  
## cai_personalities_construction_preference_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_personalities_construction_preference_policy_building_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| policy_key | True | text | True | 255 | [cai_personalities_construction_preference_policies_tables](#cai_personalities_construction_preference_policies_tables) | key |
| building_key | True | text | True | 255 | [building_levels_tables](#building_levels_tables) | level_name |
| bias_level | False | single | True | None | None | None |
| absolute_adjustment | False | single | True | None | None | None |
| building_discount_limit_adjustment | False | integer | True | None | None | None |
  
## cai_personalities_construction_system_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| strategic_context_template_assignment_policy | False | text | True | 255 | [cai_construction_system_strategic_context_template_policies_tables](#cai_construction_system_strategic_context_template_policies_tables) | key |
| province_specialisation_template_assignment_policy | False | text | True | 255 | [cai_construction_system_province_template_assignment_policies_tables](#cai_construction_system_province_template_assignment_policies_tables) | key |
| building_synergies_policy | False | text | True | 2000 | [cai_construction_system_synergy_policies_tables](#cai_construction_system_synergy_policies_tables) | key |
  
## cai_personalities_faction_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction_key | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| campaign_key | True | text | True | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| default_personality | False | text | True | 255 | [cai_personalities_tables](#cai_personalities_tables) | key |
| personality_group | False | text | True | 2000 | [cai_personalities_random_groups_tables](#cai_personalities_random_groups_tables) | random_personality_group_key |
| randomisation_policy_key | False | text | True | 2000 | [cai_personalities_randomisation_policies_tables](#cai_personalities_randomisation_policies_tables) | randomisation_policy_key |
  
## cai_personalities_income_allocation_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| default_proportion_of_net_income_to_spend | False | double | True | None | None | None |
| default_zero_or_negative_net_income_survival_rounds | False | integer | True | None | None | None |
| default_positive_net_income_survival_rounds | False | integer | True | None | None | None |
  
## cai_personalities_income_allocation_policy_strategic_context_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| income_allocation_policy_key | True | text | True | 255 | [cai_personalities_income_allocation_policies_tables](#cai_personalities_income_allocation_policies_tables) | key |
| strategic_context_key | True | text | True | 255 | [cai_strategic_context_types_tables](#cai_strategic_context_types_tables) | key |
| proportion_of_net_income_to_spend | False | double | True | None | None | None |
| zero_or_negative_net_income_survival_rounds | False | integer | True | None | None | None |
| positive_net_income_survival_rounds | False | integer | True | None | None | None |
  
## cai_personalities_randomisation_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| randomisation_policy_key | True | text | True | 2000 | None | None |
  
## cai_personalities_random_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| random_personality_group_key | True | text | True | 2000 | None | None |
  
## cai_personalities_random_group_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| random_personality_group_key | True | text | True | 2000 | [cai_personalities_random_groups_tables](#cai_personalities_random_groups_tables) | random_personality_group_key |
| personality_key | True | text | True | 255 | [cai_personalities_tables](#cai_personalities_tables) | key |
  
## cai_personalities_reliability_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| join_ally_bias | False | single | True | None | None | None |
  
## cai_personalities_religious_conversion_policies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_personalities_task_management_system_task_generator_profiles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| default_generator_group_when_owning_regions | False | text | True | 255 | [cai_task_management_system_task_generator_groups_tables](#cai_task_management_system_task_generator_groups_tables) | key |
| default_generator_group_when_no_owned_regions | False | text | True | 255 | [cai_task_management_system_task_generator_groups_tables](#cai_task_management_system_task_generator_groups_tables) | key |
  
## cai_personalities_tms_task_generator_profiles_strategic_contexts_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| task_generator_profile_key | True | text | True | 255 | [cai_personalities_task_management_system_task_generator_profiles_tables](#cai_personalities_task_management_system_task_generator_profiles_tables) | key |
| strategic_context_key | True | text | True | 255 | [cai_strategic_context_types_tables](#cai_strategic_context_types_tables) | key |
| for_use_when_the_faction_has_regions | True | yesno | True | None | None | None |
| generator_group_key | False | text | True | 255 | [cai_task_management_system_task_generator_groups_tables](#cai_task_management_system_task_generator_groups_tables) | key |
  
## cai_personality_cultural_components_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
  
## cai_personality_cultural_multipliers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_id | True | text | True | 255 | [cai_personality_cultural_components_tables](#cai_personality_cultural_components_tables) | id |
| source | True | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
| target | True | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
| positive_attitude_multiplier | False | single | True | None | None | None |
| negative_attitude_multiplier | False | single | True | None | None | None |
| attitude_base | False | single | True | None | None | None |
  
## cai_personality_deal_evaluation_components_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| max_payment_value | False | single | True | None | None | None |
| payment_treachery_value | False | single | True | None | None | None |
| payment_offered_multiplier | False | single | True | None | None | None |
| payment_requested_multiplier | False | single | True | None | None | None |
  
## cai_personality_deal_evaluation_component_overrides_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component | True | text | True | 255 | [cai_personality_deal_evaluation_components_tables](#cai_personality_deal_evaluation_components_tables) | id |
| parent | False | text | True | 255 | [cai_personality_deal_evaluation_components_tables](#cai_personality_deal_evaluation_components_tables) | id |
  
## cai_personality_deal_evaluation_deal_component_names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
  
## cai_personality_deal_evaluation_deal_component_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| personality_component | True | text | True | 255 | [cai_personality_deal_evaluation_components_tables](#cai_personality_deal_evaluation_components_tables) | id |
| deal_component | True | text | True | 255 | [cai_personality_deal_evaluation_deal_component_names_tables](#cai_personality_deal_evaluation_deal_component_names_tables) | id |
| best_friends_value | False | single | True | None | None | None |
| very_friendly_value | False | single | True | None | None | None |
| friendly_value | False | single | True | None | None | None |
| neutral_value | False | single | True | None | None | None |
| unfriendly_value | False | single | True | None | None | None |
| very_unfriendly_value | False | single | True | None | None | None |
| bitter_enemies_value | False | single | True | None | None | None |
| last_stand_balance_factor | False | single | True | None | None | None |
| total_war_balance_factor | False | single | True | None | None | None |
| war_balance_factor | False | single | True | None | None | None |
| tension_balance_factor | False | single | True | None | None | None |
| peace_balance_factor | False | single | True | None | None | None |
| treachery_value | False | single | True | None | None | None |
  
## cai_personality_deal_generation_components_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
  
## cai_personality_deal_generation_generators_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
  
## cai_personality_deal_generation_generator_priorities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_key | True | text | True | 255 | [cai_personality_deal_generation_components_tables](#cai_personality_deal_generation_components_tables) | id |
| generator_key | True | text | True | 255 | [cai_personality_deal_generation_generators_tables](#cai_personality_deal_generation_generators_tables) | id |
| last_stand_priority | False | single | True | None | None | None |
| total_war_priority | False | single | True | None | None | None |
| war_priority | False | single | True | None | None | None |
| tension_priority | False | single | True | None | None | None |
| peace_priority | False | single | True | None | None | None |
| param1 | False | single | True | None | None | None |
| param2 | False | single | True | None | None | None |
| param3 | False | single | True | None | None | None |
| param4 | False | single | True | None | None | None |
| failure_timeout | False | integer | True | None | None | None |
| min_payment_cap | False | integer | True | None | None | None |
| max_payment_cap | False | integer | True | None | None | None |
| max_payment_pct | False | single | True | None | None | None |
  
## cai_personality_diplomatic_components_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
  
## cai_personality_diplomatic_component_overrides_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component | True | text | True | 255 | [cai_personality_diplomatic_components_tables](#cai_personality_diplomatic_components_tables) | id |
| parent | False | text | True | 255 | [cai_personality_diplomatic_components_tables](#cai_personality_diplomatic_components_tables) | id |
  
## cai_personality_diplomatic_events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| diplomatic_factor_group_active | False | text | False | 255 | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| diplomatic_factor_group_inactive | False | text | False | 255 | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
  
## cai_personality_diplomatic_event_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_id | True | text | True | 255 | [cai_personality_diplomatic_components_tables](#cai_personality_diplomatic_components_tables) | id |
| event_id | True | text | True | 255 | [cai_personality_diplomatic_events_tables](#cai_personality_diplomatic_events_tables) | id |
| value | False | single | True | None | None | None |
| falloff | False | integer | True | None | None | None |
  
## cai_personality_diplomatic_treaty_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_id | True | text | True | 255 | [cai_personality_diplomatic_components_tables](#cai_personality_diplomatic_components_tables) | id |
| defensive_alliance | False | single | False | None | None | None |
| trade_agreement | False | single | False | None | None | None |
| military_alliance | False | single | True | None | None | None |
| non_aggression_pact | False | single | True | None | None | None |
| vassalage_master | False | single | True | None | None | None |
| vassalage_vassal | False | single | True | None | None | None |
| client_state_protector | False | single | True | None | None | None |
| client_state_client | False | single | True | None | None | None |
| war | False | single | True | None | None | None |
| military_access | False | single | True | None | None | None |
  
## cai_personality_negotiation_components_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| initial_decline | False | integer | True | None | None | None |
| initial_counter | False | integer | True | None | None | None |
| irrelevant_decline | False | integer | True | None | None | None |
| irrelevant_accept | False | integer | True | None | None | None |
| irrelevant_counter_new | False | integer | True | None | None | None |
| irrelevant_counter_last | False | integer | True | None | None | None |
| angry_reject_min | False | integer | True | None | None | None |
| angry_reject_max | False | integer | True | None | None | None |
| no_payment_chance | False | integer | True | None | None | None |
| max_steps_above_acceptable | False | integer | True | None | None | None |
| no_offer_chance | False | integer | True | None | None | None |
| num_goals_generated | False | integer | True | None | None | None |
| max_interactions | False | integer | True | None | None | None |
  
## cai_personality_occupation_decision_components_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| food_shortage_cap | False | integer | True | None | None | None |
| food_excess_cap | False | integer | True | None | None | None |
| squalor_cap | False | integer | True | None | None | None |
| min_attitude | False | integer | True | None | None | None |
  
## cai_personality_occupation_decision_priorities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_id | True | text | True | 255 | [cai_personality_occupation_decision_components_tables](#cai_personality_occupation_decision_components_tables) | id |
| option | True | text | True | 255 | None | None |
| last_stand_priority | False | single | True | None | None | None |
| total_war_priority | False | single | True | None | None | None |
| war_priority | False | single | True | None | None | None |
| tension_priority | False | single | True | None | None | None |
| peace_priority | False | single | True | None | None | None |
  
## cai_personality_strategic_components_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| max_friendly_attitude | False | single | True | None | None | None |
| friendly_towards_friend_multiplier | False | single | True | None | None | None |
| hostile_towards_friend_multiplier | False | single | True | None | None | None |
| max_hostile_attitude | False | single | True | None | None | None |
| friendly_towards_enemy_multiplier | False | single | True | None | None | None |
| hostile_towards_enemy_multiplier | False | single | True | None | None | None |
| unknown_faction_multiplier | False | single | True | None | None | None |
| max_merc_proportion | False | single | True | None | None | None |
| min_merc_cap | False | integer | True | None | None | None |
| enemy_strength_modifier | False | single | True | None | None | None |
| enemy_threat_strength_modifier | False | single | True | None | None | None |
| min_retreat_ratio | False | single | True | None | None | None |
| min_retreat_to_settlement_ratio | False | single | True | None | None | None |
| strategic_balance_opportunism_factor | False | single | True | None | None | None |
| fortified_settlement_assault_strength_modifier | False | single | True | None | None | None |
| fortified_settlement_defend_strength_modifier | False | single | True | None | None | None |
  
## cai_personality_strategic_desired_attitudes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| strategic_component | True | text | True | 255 | [cai_personality_strategic_components_tables](#cai_personality_strategic_components_tables) | id |
| best_friends_attitude | False | single | True | None | None | None |
| very_friendly_attitude | False | single | True | None | None | None |
| friendly_attitude | False | single | True | None | None | None |
| neutral_attitude | False | single | True | None | None | None |
| unfriendly_attitude | False | single | True | None | None | None |
| very_unfriendly_attitude | False | single | True | None | None | None |
| bitter_enemies_attitude | False | single | True | None | None | None |
| best_friends_positive_factor | False | single | True | None | None | None |
| very_friendly_positive_factor | False | single | True | None | None | None |
| friendly_positive_factor | False | single | True | None | None | None |
| neutral_positive_factor | False | single | True | None | None | None |
| unfriendly_positive_factor | False | single | True | None | None | None |
| very_unfriendly_positive_factor | False | single | True | None | None | None |
| bitter_enemies_positive_factor | False | single | True | None | None | None |
| best_friends_negative_factor | False | single | True | None | None | None |
| very_friendly_negative_factor | False | single | True | None | None | None |
| friendly_negative_factor | False | single | True | None | None | None |
| neutral_negative_factor | False | single | True | None | None | None |
| unfriendly_negative_factor | False | single | True | None | None | None |
| very_unfriendly_negative_factor | False | single | True | None | None | None |
| bitter_enemies_negative_factor | False | single | True | None | None | None |
  
## cai_personality_strategic_resource_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| strategic_component | True | text | True | 255 | [cai_personality_strategic_components_tables](#cai_personality_strategic_components_tables) | id |
| resource | True | text | True | 255 | [resources_tables](#resources_tables) | key |
| trade_value | False | single | True | None | None | None |
| trade_falloff | False | single | True | None | None | None |
| ownership_value | False | single | True | None | None | None |
| ownership_falloff | False | single | True | None | None | None |
  
## cai_siege_strength_modifiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| subculture | True | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| defence_strength_modifier | False | single | True | None | None | None |
| assault_strength_modifier | False | single | True | None | None | None |
  
## cai_strategic_context_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_task_management_system_task_generators_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_task_management_system_task_generator_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cai_task_management_system_task_generator_groups_generators_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| task_generator_group_key | True | text | True | 255 | [cai_task_management_system_task_generator_groups_tables](#cai_task_management_system_task_generator_groups_tables) | key |
| task_generator_key | True | text | True | 255 | [cai_task_management_system_task_generators_tables](#cai_task_management_system_task_generators_tables) | key |
| priority | False | double | True | None | None | None |
  
## cai_variables_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| value | False | double | True | None | None | None |
| description | False | text | True | 536870910 | None | None |
  
## cai_variables_overides_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| cai_variable_key | True | text | True | 255 | [cai_variables_tables](#cai_variables_tables) | key |
| campaign_key | True | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| value | False | double | True | None | None | None |
| optional_difficulty_level | True | text | False | 20000 | None | None |
| optional_campaign_type | True | text | False | 20000 | None | None |
  
## campaigns_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_name | True | text | True | 50 | None | None |
| onscreen_name | False | text | True | 50 | None | None |
| description | False | text | True | 536870910 | None | None |
| map_name | False | text | True | 50 | [campaign_maps_tables](#campaign_maps_tables) | mapname |
| data_directory | False | text | True | 50 | None | None |
| is_grand | False | yesno | False | None | None | None |
| exportable | False | yesno | False | None | None | None |
| campaign_order | False | integer | False | None | None | None |
| bullet_list | False | text | False | 536870910 | None | None |
| display_location | False | text | False | 255 | None | None |
| is_tutorial | False | yesno | True | None | None | None |
| banner_image | False | text | False | 255 | None | None |
| banner_icon | False | text | False | 255 | None | None |
| available_for_mp | False | yesno | True | None | None | None |
| mp_sort_order | False | integer | True | None | None | None |
  
## campaigns_campaign_variables_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| variable_key | True | text | True | 50 | [campaign_variables_tables](#campaign_variables_tables) | variable_key |
| campaign_name | True | text | True | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| value | False | double | True | None | None | None |
| optional_difficulty_level | True | text | False | 20000 | None | None |
| optional_campaign_type | True | text | False | 20000 | None | None |
  
## campaign_ai_behaviours_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| behaviour | True | text | True | 255 | None | None |
| description | False | text | False | 255 | None | None |
  
## campaign_ai_character_skill_tree_agent_managers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_ai_character_skill_tree_distributions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_ai_character_skill_tree_distribution_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent_manager_key | True | text | True | 255 | [campaign_ai_character_skill_tree_agent_managers_tables](#campaign_ai_character_skill_tree_agent_managers_tables) | key |
| distribution_key | True | text | True | 255 | [campaign_ai_character_skill_tree_distributions_tables](#campaign_ai_character_skill_tree_distributions_tables) | key |
| priority | False | integer | True | None | None | None |
  
## campaign_ai_character_skill_tree_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent_manager_key | True | text | True | 255 | [campaign_ai_character_skill_tree_agent_managers_tables](#campaign_ai_character_skill_tree_agent_managers_tables) | key |
| skill_key | True | text | True | 255 | [character_skills_tables](#character_skills_tables) | key |
| priority | False | integer | True | None | None | None |
  
## campaign_ai_character_skill_tree_managers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_ai_character_skill_tree_manager_agent_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| manager_key | True | text | True | 255 | [campaign_ai_character_skill_tree_managers_tables](#campaign_ai_character_skill_tree_managers_tables) | key |
| agent_key | True | text | True | 255 | [character_skill_node_sets_tables](#character_skill_node_sets_tables) | key |
| agent_manager_key | False | text | True | 255 | [campaign_ai_character_skill_tree_agent_managers_tables](#campaign_ai_character_skill_tree_agent_managers_tables) | key |
  
## campaign_ai_managers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| manager | True | text | True | 255 | None | None |
| description | False | text | False | 255 | None | None |
  
## campaign_ai_manager_behaviour_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| manager | True | text | True | 255 | [campaign_ai_managers_tables](#campaign_ai_managers_tables) | manager |
| behaviour | True | text | True | 255 | [campaign_ai_behaviours_tables](#campaign_ai_behaviours_tables) | behaviour |
| priority | False | single | True | None | None | None |
  
## campaign_ai_personalities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| personality | True | text | True | 255 | None | None |
| is_default | False | yesno | True | None | None | None |
| description | False | text | False | 255 | None | None |
  
## campaign_ai_personality_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| personality | True | text | True | 255 | [campaign_ai_personalities_tables](#campaign_ai_personalities_tables) | personality |
| property | True | text | True | 255 | [campaign_ai_personality_properties_tables](#campaign_ai_personality_properties_tables) | property |
| property_value | False | single | True | None | None | None |
  
## campaign_ai_personality_properties_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| property | True | text | True | 255 | None | None |
| description | False | text | False | 255 | None | None |
  
## campaign_ai_technology_managers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_ai_technology_manager_path_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| manager_key | True | text | True | 255 | [campaign_ai_technology_managers_tables](#campaign_ai_technology_managers_tables) | key |
| path_key | True | text | True | 255 | [campaign_ai_technology_paths_tables](#campaign_ai_technology_paths_tables) | key |
| priority | False | integer | True | None | None | None |
  
## campaign_ai_technology_paths_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_ai_technology_path_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| path_key | True | text | True | 255 | [campaign_ai_technology_paths_tables](#campaign_ai_technology_paths_tables) | key |
| technology_key | True | text | True | 255 | [technologies_tables](#technologies_tables) | key |
| priority | False | integer | True | None | None | None |
  
## campaign_ambush_ground_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | [campaign_ground_types_tables](#campaign_ground_types_tables) | type |
| ambush_chance_of_success | False | double | True | None | None | None |
  
## campaign_anim_set_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name | True | text | True | 255 | None | None |
| skeleton | False | text | False | 255 | None | None |
  
## campaign_autoresolver_battle_situations_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| battle_type | False | text | False | 255 | [campaign_battle_type_enums_tables](#campaign_battle_type_enums_tables) | key |
| night_battle | False | text | False | 255 | None | None |
| stance | False | text | False | 255 | None | None |
  
## campaign_autoresolver_modifiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| class | False | text | False | 255 | [unit_class_tables](#unit_class_tables) | key |
| vs_class | False | text | False | 255 | [unit_class_tables](#unit_class_tables) | key |
| stat_variable_id | False | text | True | 255 | [campaign_autoresolver_stat_variables_tables](#campaign_autoresolver_stat_variables_tables) | id |
  
## campaign_autoresolver_mod_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
  
## campaign_autoresolver_mod_group_modifier_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| group_id | False | text | True | 255 | [campaign_autoresolver_mod_groups_tables](#campaign_autoresolver_mod_groups_tables) | id |
| modification_id | False | text | True | 255 | [campaign_autoresolver_modifiers_tables](#campaign_autoresolver_modifiers_tables) | id |
| value | False | double | True | None | None | None |
  
## campaign_autoresolver_mod_group_targets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| mechanic_target | False | text | False | 255 | None | None |
| alliance_target | False | text | False | 255 | None | None |
| player_target | False | text | False | 255 | None | None |
  
## campaign_autoresolver_situation_mod_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| situation_id | False | text | True | 255 | [campaign_autoresolver_battle_situations_tables](#campaign_autoresolver_battle_situations_tables) | id |
| group_target_id | False | text | True | 255 | [campaign_autoresolver_mod_group_targets_tables](#campaign_autoresolver_mod_group_targets_tables) | id |
| group_id | False | text | True | 255 | [campaign_autoresolver_mod_groups_tables](#campaign_autoresolver_mod_groups_tables) | id |
  
## campaign_autoresolver_stat_variables_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| description | False | text | False | 255 | None | None |
  
## campaign_battle_presets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| onscreen_name | False | text | False | 255 | None | None |
| description | False | text | False | 255 | None | None |
| coord_x | False | decimal | True | None | None | None |
| coord_y | False | decimal | True | None | None | None |
| tile_upgrade | False | text | False | 255 | None | None |
| battle_type | False | text | True | 255 | [campaign_battle_type_enums_tables](#campaign_battle_type_enums_tables) | key |
| is_unique_settlement | False | yesno | True | None | None | None |
| campaign_map | False | integer | True | None | [campaign_map_playable_areas_tables](#campaign_map_playable_areas_tables) | index |
  
## campaign_battle_type_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_bonus_value_battle_context_battle_type_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle_context_key | True | text | True | 255 | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| battle_type_key | True | text | True | 255 | [campaign_battle_type_enums_tables](#campaign_battle_type_enums_tables) | key |
  
## campaign_bonus_value_battle_context_culture_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle_context_key | True | text | True | 255 | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| culture_key | True | text | True | 255 | [cultures_tables](#cultures_tables) | key |
  
## campaign_bonus_value_battle_context_faction_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle_context_key | True | text | True | 255 | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| faction_key | True | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## campaign_bonus_value_battle_context_force_status_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_bonus_value_battle_context_force_status_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle_context_key | True | text | True | 255 | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| force_status_key | True | text | True | 255 | [campaign_bonus_value_battle_context_force_status_tables](#campaign_bonus_value_battle_context_force_status_tables) | key |
| is_yours | False | yesno | True | None | None | None |
  
## campaign_bonus_value_battle_context_ground_type_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle_context_key | True | text | True | 255 | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| ground_type_key | True | text | True | 255 | [campaign_ground_types_tables](#campaign_ground_types_tables) | type |
  
## campaign_bonus_value_battle_context_specifiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| night_battles_only | False | yesno | True | None | None | None |
  
## campaign_bonus_value_battle_context_territory_status_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_bonus_value_battle_context_territory_status_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battle_context_key | True | text | True | 255 | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
| territory_status_key | True | text | True | 255 | [campaign_bonus_value_battle_context_territory_status_tables](#campaign_bonus_value_battle_context_territory_status_tables) | key |
  
## campaign_bonus_value_ids_action_results_additional_outcomes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 255 | None | None |
  
## campaign_bonus_value_ids_agent_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_basic_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_battlefield_deployables_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 255 | None | None |
  
## campaign_bonus_value_ids_battle_contexts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_bonus_value_ids_building_chain_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_building_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 512 | None | None |
  
## campaign_bonus_value_ids_commodity_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_melee_weapon_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_missile_weapon_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_population_class_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_population_class_and_religion_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_projectile_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_projectile_shot_type_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_projectile_type_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_provincial_initiative_effect_records_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 255 | None | None |
  
## campaign_bonus_value_ids_religion_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_resource_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_siege_items_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 255 | None | None |
  
## campaign_bonus_value_ids_technology_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 64 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_unit_ability_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_unit_caste_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_unit_category_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_unit_class_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_unit_records_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## campaign_bonus_value_ids_unit_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| notes | False | text | False | 512 | None | None |
  
## campaign_character_anim_status_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| status | True | text | True | 255 | None | None |
  
## campaign_character_arts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| art_set_id | True | text | True | 255 | [campaign_character_art_sets_tables](#campaign_character_art_sets_tables) | art_set_id |
| level | True | integer | True | None | None | None |
| season | True | text | True | 255 | None | None |
| age | True | integer | True | None | None | None |
| portrait | False | text | False | 255 | None | None |
| uniform | False | text | False | 255 | [agent_uniforms_tables](#agent_uniforms_tables) | uniform_name |
| card | False | text | False | 255 | None | None |
| info | False | text | False | 255 | None | None |
| sea_uniform | False | text | False | 255 | [agent_uniforms_tables](#agent_uniforms_tables) | uniform_name |
| navy_uniform | False | text | False | 255 | [agent_uniforms_tables](#agent_uniforms_tables) | uniform_name |
| land_animation | False | text | False | 255 | [campaign_anim_set_enums_tables](#campaign_anim_set_enums_tables) | name |
| sea_animation | False | text | False | 255 | [campaign_anim_set_enums_tables](#campaign_anim_set_enums_tables) | name |
| navy_animation | False | text | False | 255 | [campaign_anim_set_enums_tables](#campaign_anim_set_enums_tables) | name |
  
## campaign_character_art_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| art_set_id | True | text | True | 255 | None | None |
| is_custom | False | yesno | True | None | None | None |
| agent_type | False | text | False | 255 | [agents_tables](#agents_tables) | key |
| faction | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| culture | False | text | False | 255 | [cultures_tables](#cultures_tables) | key |
| subculture | False | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| is_male | False | yesno | True | None | None | None |
| group | False | text | False | 255 | [campaign_character_art_sets_campaign_groups_tables](#campaign_character_art_sets_campaign_groups_tables) | key |
  
## campaign_character_art_sets_campaign_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_character_art_sets_group_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| group | True | text | True | 255 | [campaign_character_art_sets_campaign_groups_tables](#campaign_character_art_sets_campaign_groups_tables) | key |
| campaign | True | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## campaign_character_art_set_campaign_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| art_set_id | False | text | True | 255 | [campaign_character_art_sets_tables](#campaign_character_art_sets_tables) | art_set_id |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## campaign_character_attribute_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent_record | True | text | True | 255 | [agents_tables](#agents_tables) | key |
| attribute_record | True | text | True | 255 | [agent_attributes_tables](#agent_attributes_tables) | key |
| attribute_level | True | integer | True | None | None | None |
| effect_record | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| effect_scope | True | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| effect_value | False | single | True | None | None | None |
| culture_record | True | text | False | 255 | [cultures_tables](#cultures_tables) | key |
| subculture_record | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| faction_record | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| campaign_record | True | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## campaign_clan_level_infos_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| clan_level | True | integer | True | None | None | None |
| optional_faction_key | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| optional_difficulty_level | True | text | False | 255 | None | None |
| modernisation_threshold | False | integer | True | None | None | None |
| technology_unlock_level | False | integer | True | None | None | None |
| effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
  
## campaign_difficulty_handicap_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_difficulty_handicap | True | integer | True | None | None | None |
| human | True | yesno | True | None | None | None |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| effect_value | False | single | True | None | None | None |
| optional_campaign_key | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## campaign_effect_scopes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| localised_text | False | text | False | 255 | None | None |
| order | False | integer | True | None | None | None |
| source | False | text | True | 255 | [campaign_effect_scope_objects_tables](#campaign_effect_scope_objects_tables) | key |
| target | False | text | True | 255 | [campaign_effect_scope_objects_tables](#campaign_effect_scope_objects_tables) | key |
| ownership | False | text | False | 255 | [campaign_effect_scope_ownerships_tables](#campaign_effect_scope_ownerships_tables) | key |
| location | False | text | False | 255 | [campaign_effect_scope_locations_tables](#campaign_effect_scope_locations_tables) | key |
  
## campaign_effect_scope_agent_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_effect_scope_key | True | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| agent_key | True | text | True | 255 | [agents_tables](#agents_tables) | key |
  
## campaign_effect_scope_character_force_relationships_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_effect_scope_character_force_relationship_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_effect_scope_key | True | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| force_relationship_key | True | text | True | 255 | [campaign_effect_scope_character_force_relationships_tables](#campaign_effect_scope_character_force_relationships_tables) | key |
  
## campaign_effect_scope_character_unit_relationships_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_effect_scope_character_unit_relationship_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_effect_scope_key | True | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| unit_relationship_key | True | text | True | 255 | [campaign_effect_scope_character_unit_relationships_tables](#campaign_effect_scope_character_unit_relationships_tables) | key |
  
## campaign_effect_scope_locations_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_effect_scope_objects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_effect_scope_ownerships_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_ground_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 50 | None | None |
| movement_cost | False | integer | True | None | None | None |
| can_ambush | False | yesno | True | None | None | None |
| onscreen_name | False | text | False | 50 | None | None |
| is_sea | False | yesno | True | None | None | None |
| icon | False | text | True | 255 | None | None |
  
## campaign_localised_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| string | False | text | True | 255 | None | None |
  
## campaign_maps_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| mapname | True | text | True | 50 | None | None |
| minx | False | integer | True | None | None | None |
| miny | False | integer | True | None | None | None |
| maxx | False | integer | True | None | None | None |
| maxy | False | integer | True | None | None | None |
  
## campaign_map_attritions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| type | False | text | True | 255 | [campaign_map_attrition_types_tables](#campaign_map_attrition_types_tables) | key |
| damage | False | text | True | 255 | [campaign_map_attrition_damages_tables](#campaign_map_attrition_damages_tables) | key |
| campaign_map_tooltip | False | text | False | 20000 | None | None |
| unit_card_tooltip | False | text | False | 20000 | None | None |
| unit_immunity_text | False | text | False | 20000 | None | None |
| message_event_association | False | text | False | 255 | [message_events_tables](#message_events_tables) | event |
  
## campaign_map_attrition_damages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| percent_unit_damage | False | integer | True | None | None | None |
  
## campaign_map_attrition_faction_immunities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| attrition | True | text | True | 255 | [campaign_map_attritions_tables](#campaign_map_attritions_tables) | key |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## campaign_map_attrition_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_map_attrition_unit_immunities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| attrition | True | text | True | 255 | [campaign_map_attritions_tables](#campaign_map_attritions_tables) | key |
| unit | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
  
## campaign_map_pieces_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ID | True | autonumber | False | None | None | None |
  
## campaign_map_playable_areas_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| mapname | False | text | True | 50 | [campaign_maps_tables](#campaign_maps_tables) | mapname |
| index | True | autonumber | True | None | None | None |
| minx | False | double | True | None | None | None |
| maxx | False | double | True | None | None | None |
| miny | False | double | True | None | None | None |
| maxy | False | double | True | None | None | None |
| sea_trade | False | yesno | True | None | None | None |
| onscreen_name | False | text | True | 536870910 | None | None |
| map_file | False | text | False | 50 | None | None |
| overlay_file | False | text | False | 50 | None | None |
| radar_file | False | text | False | 50 | None | None |
| meaningful_id | False | text | True | 50 | None | None |
| preview_width | False | integer | False | None | None | None |
| preview_height | False | integer | False | None | None | None |
| preview_border | False | integer | False | None | None | None |
| minimap_lookup_file | False | text | False | 50 | None | None |
| is_available_in_custom_battle | False | yesno | True | None | None | None |
  
## campaign_map_regions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_map | True | text | True | 50 | [campaign_maps_tables](#campaign_maps_tables) | mapname |
| region | True | text | True | 50 | [regions_tables](#regions_tables) | key |
  
## campaign_map_roads_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| threshold | False | double | True | None | None | None |
| turns_required_to_upgrade_to | False | integer | True | None | None | None |
| turns_required_to_downgrade_from | False | integer | True | None | None | None |
| movement_cost | False | integer | True | None | None | None |
  
## campaign_map_settlements_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| settlement_id | True | text | True | 50 | None | None |
| region | False | text | True | 50 | [regions_tables](#regions_tables) | key |
| default_onscreen_name | False | text | True | 50 | None | None |
| template_name | False | text | True | 50 | [campaign_map_settlement_templates_tables](#campaign_map_settlement_templates_tables) | template_name |
| slot_count | False | integer | True | None | None | None |
| slot_type | False | text | True | 50 | [slots_tables](#slots_tables) | slot |
  
## campaign_map_settlement_templates_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| template_name | True | text | True | 50 | None | None |
| slot_total | False | integer | True | None | None | None |
  
## campaign_map_settlement_templates_cult_art_jct_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| settlement_template | True | text | True | 50 | [campaign_map_settlement_templates_tables](#campaign_map_settlement_templates_tables) | template_name |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| artpiece | False | text | True | 50 | None | None |
  
## campaign_map_slots_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| slot_id | True | text | True | 50 | None | None |
| region | False | text | True | 50 | [regions_tables](#regions_tables) | key |
| slot_type | False | text | True | 50 | [slots_tables](#slots_tables) | slot |
| template | False | text | False | 50 | [campaign_map_slots_templates_tables](#campaign_map_slots_templates_tables) | template_name |
| rotation | False | integer | True | None | None | None |
| underlay | False | text | False | 50 | [warscape_underlay_textures_tables](#warscape_underlay_textures_tables) | underlay_key |
| onscreen | False | text | False | 50 | None | None |
  
## campaign_map_slots_templates_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| template_name | True | text | True | 50 | None | None |
| slot | False | text | True | 50 | [slots_tables](#slots_tables) | slot |
| levels | False | integer | True | None | None | None |
| art_file | False | text | True | 50 | None | None |
  
## campaign_map_tooltips_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| select_context | True | text | True | 50 | [campaign_map_tooltip_select_contexts_tables](#campaign_map_tooltip_select_contexts_tables) | select_context |
| over_context | True | text | True | 50 | [campaign_map_tooltip_over_contexts_tables](#campaign_map_tooltip_over_contexts_tables) | over_contexts |
| tooltip_line | False | text | False | 255 | [campaign_map_tooltip_texts_tables](#campaign_map_tooltip_texts_tables) | key |
| advice_line | False | text | False | 255 | [campaign_map_tooltip_texts_tables](#campaign_map_tooltip_texts_tables) | key |
| main_line | False | text | False | 255 | [campaign_map_tooltip_texts_tables](#campaign_map_tooltip_texts_tables) | key |
  
## campaign_map_tooltip_over_contexts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| over_contexts | True | text | True | 50 | None | None |
  
## campaign_map_tooltip_select_contexts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| select_context | True | text | True | 50 | None | None |
  
## campaign_map_tooltip_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| tooltip_text | False | text | True | 536870910 | None | None |
  
## campaign_map_towns_and_ports_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| town_id | True | text | True | 50 | None | None |
| region | False | text | True | 50 | [regions_tables](#regions_tables) | key |
| slot_type | False | text | True | 50 | [slots_tables](#slots_tables) | slot |
| onscreen_name | False | text | True | 50 | None | None |
| template | False | text | False | 50 | [campaign_map_slots_templates_tables](#campaign_map_slots_templates_tables) | template_name |
  
## campaign_map_town_templates_cult_art_jct_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| artpiece | False | text | True | 50 | None | None |
  
## campaign_map_transition_areas_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| mapname | False | text | True | 255 | [campaign_maps_tables](#campaign_maps_tables) | mapname |
| index | True | autonumber | False | None | None | None |
| minx | False | double | True | None | None | None |
| miny | False | double | True | None | None | None |
| maxx | False | double | True | None | None | None |
| maxy | False | double | True | None | None | None |
| storm_chance_percentage | False | integer | True | None | None | None |
| onscreen_name | False | text | False | 255 | None | None |
  
## campaign_map_transition_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| index | False | autonumber | False | None | None | None |
| start_area | True | integer | True | None | [campaign_map_transition_areas_tables](#campaign_map_transition_areas_tables) | index |
| end_area | True | integer | True | None | [campaign_map_transition_areas_tables](#campaign_map_transition_areas_tables) | index |
| delay_chance_percentage | False | integer | True | None | None | None |
| turns_start_to_end | False | integer | True | None | None | None |
| turns_end_to_start | False | integer | True | None | None | None |
  
## campaign_mp_coop_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_mp_coop_groups_to_factions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction_key | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| mp_coop_group | True | text | True | 255 | [campaign_mp_coop_groups_tables](#campaign_mp_coop_groups_tables) | key |
  
## campaign_politics_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| string | False | text | True | 255 | None | None |
  
## campaign_public_order_populace_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| populace_happiness | True | text | True | 255 | None | None |
| culture | True | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
  
## campaign_settlement_display_aqueducts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| region_key | True | text | True | 255 | [regions_tables](#regions_tables) | key |
| building_path | False | text | False | 255 | None | None |
| position_x_map | False | double | True | None | None | None |
| position_y_map | False | double | True | None | None | None |
| position_z_height | False | double | True | None | None | None |
| rotation_cw_radians | False | double | True | None | None | None |
  
## campaign_settlement_display_buildings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| display_building_key | False | text | True | 255 | [campaign_settlement_display_building_ids_tables](#campaign_settlement_display_building_ids_tables) | key |
| state | False | text | False | 255 | [campaign_settlement_display_buildings_enums_tables](#campaign_settlement_display_buildings_enums_tables) | type |
| is_slum | False | yesno | True | None | None | None |
| is_sieged | False | yesno | True | None | None | None |
| is_blockaded | False | yesno | True | None | None | None |
| building_path | False | text | False | 255 | None | None |
| destruction_additional_model | False | text | False | 255 | None | None |
| destruction_override_model | False | text | False | 255 | None | None |
| construction_additional_model | False | text | False | 255 | None | None |
| construction_override_model | False | text | False | 255 | None | None |
  
## campaign_settlement_display_buildings_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | False | 255 | None | None |
  
## campaign_settlement_display_building_constructions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| display_building_key | False | text | True | 255 | [campaign_settlement_display_building_ids_tables](#campaign_settlement_display_building_ids_tables) | key |
| construction_type | False | text | True | 255 | [campaign_settlement_display_building_construction_enums_tables](#campaign_settlement_display_building_construction_enums_tables) | type |
| phase | False | integer | True | None | None | None |
| building_path | False | text | False | 255 | None | None |
  
## campaign_settlement_display_building_construction_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 255 | None | None |
  
## campaign_settlement_display_building_ids_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| building_level_key | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| sprawl_piece_type | False | text | False | 255 | [campaign_settlement_display_sprawl_pieces_tables](#campaign_settlement_display_sprawl_pieces_tables) | key |
| sprawl_piece_level | False | integer | True | None | None | None |
| culture | False | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| sub_culture | False | text | False | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| faction | False | text | False | 255 | [factions_tables](#factions_tables) | key |
  
## campaign_settlement_display_building_trees_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| rigid_lookup_key | False | text | False | 255 | None | None |
| climate_type | False | text | True | 50 | [climates_tables](#climates_tables) | climate_type |
| building_path | False | text | False | 255 | None | None |
  
## campaign_settlement_display_siege_item_ids_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| battlefield_deployable_siege_item | True | text | True | 255 | [battlefield_deployable_siege_items_tables](#battlefield_deployable_siege_items_tables) | key |
| sprawl_piece | False | text | True | 255 | [campaign_settlement_display_sprawl_pieces_tables](#campaign_settlement_display_sprawl_pieces_tables) | key |
  
## campaign_settlement_display_sprawl_pieces_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_stances_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_stance_effects_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| stance | True | text | True | 255 | [campaign_stances_tables](#campaign_stances_tables) | key |
| effect_bundle | True | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| culture | True | text | False | 255 | [cultures_tables](#cultures_tables) | key |
| subculture | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
  
## campaign_statistics_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| localised_description | False | text | True | 255 | None | None |
| category_order | False | integer | True | None | None | None |
  
## campaign_statistics_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## campaign_statistics_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_statistic | True | text | True | 255 | [campaign_statistics_enums_tables](#campaign_statistics_enums_tables) | key |
| localised_description | False | text | True | 255 | None | None |
| campaign_statistic_category | False | text | True | 255 | [campaign_statistics_categories_tables](#campaign_statistics_categories_tables) | key |
| statistic_order | False | integer | True | None | None | None |
  
## campaign_subjects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| optional_name | False | text | False | 255 | [campaign_subject_strings_tables](#campaign_subject_strings_tables) | key |
| optional_name_source_faction | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| ui_image | False | text | True | 255 | None | None |
| flavour_text | False | text | True | 255 | [campaign_subject_strings_tables](#campaign_subject_strings_tables) | key |
| male | False | yesno | True | None | None | None |
  
## campaign_subject_evolutions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| campaign_subject_key | False | text | True | 255 | [campaign_subjects_tables](#campaign_subjects_tables) | key |
| effect_bundle_key | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| min_turns | False | integer | True | None | None | None |
| max_turns | False | integer | True | None | None | None |
| weighting | False | single | True | None | None | None |
| arrival_message | False | text | False | 255 | [campaign_subject_messages_tables](#campaign_subject_messages_tables) | key |
| departure_message | False | text | False | 255 | [campaign_subject_messages_tables](#campaign_subject_messages_tables) | key |
| flavour_text | False | text | False | 255 | [campaign_subject_strings_tables](#campaign_subject_strings_tables) | key |
  
## campaign_subject_evolution_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| parent | True | text | True | 255 | [campaign_subject_evolutions_tables](#campaign_subject_evolutions_tables) | key |
| child | True | text | True | 255 | [campaign_subject_evolutions_tables](#campaign_subject_evolutions_tables) | key |
  
## campaign_subject_faction_restriction_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_subject_key | True | text | True | 255 | [campaign_subjects_tables](#campaign_subjects_tables) | key |
| faction_key | True | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## campaign_subject_messages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| message_type | False | text | True | 255 | [message_events_tables](#message_events_tables) | event |
| optional_text | False | text | False | 255 | None | None |
  
## campaign_subject_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| string | False | text | True | 255 | None | None |
  
## campaign_unit_stat_bonuses_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| bonus | True | text | True | 255 | None | None |
| level | True | integer | True | None | None | None |
| threshold | False | integer | True | None | None | None |
| description | False | text | True | 20000 | None | None |
| icon_path | False | text | True | 20000 | None | None |
| upgrade_cost_new | False | integer | True | None | None | None |
| upgrade_cost_from_previous_level | False | integer | True | None | None | None |
  
## campaign_variables_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| variable_key | True | text | True | 50 | None | None |
| value | False | double | True | None | None | None |
| description | False | text | True | 536870910 | None | None |
  
## campaign_vfx_campaign_vfx_event_ids_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_vfx_event | True | text | True | 255 | None | None |
  
## campaign_vfx_descriptions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| vfx | False | text | True | 255 | [particle_effects_tables](#particle_effects_tables) | key |
| x_offset | False | decimal | True | None | None | None |
| y_offset | False | decimal | True | None | None | None |
| z_offset | False | decimal | True | None | None | None |
  
## campaign_vfx_lookups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| vfx_event | False | text | True | 255 | [campaign_vfx_campaign_vfx_event_ids_tables](#campaign_vfx_campaign_vfx_event_ids_tables) | campaign_vfx_event |
| vfx_description | False | text | True | 255 | [campaign_vfx_descriptions_tables](#campaign_vfx_descriptions_tables) | key |
| faction_filter | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| culture_filter | False | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| agent_filter | False | text | False | 255 | [agents_tables](#agents_tables) | key |
  
## campaign_walk_anim_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| reference_pose | False | text | True | 50 | [anim_reference_poses_tables](#anim_reference_poses_tables) | key |
| pre_step_to | False | text | False | 255 | None | None |
| step_to | False | text | True | 255 | None | None |
| post_step_to | False | text | False | 255 | None | None |
| pre_stand_to_walk | False | text | True | 255 | None | None |
| stand_to_walk | False | text | True | 255 | None | None |
| stand_to_walk_distance | False | single | True | None | None | None |
| walk | False | text | True | 255 | None | None |
| walk_distance | False | single | True | None | None | None |
| walk_to_stand | False | text | True | 255 | None | None |
| mid_walk_to_stand | False | text | True | 255 | None | None |
| walk_to_stand_distance | False | single | True | None | None | None |
| post_walk_to_stand | False | text | True | 255 | None | None |
| post_mid_walk_to_stand | False | text | True | 255 | None | None |
  
## capture_point_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| onscreen_name | False | text | True | 255 | None | None |
| icon_name | False | text | True | 255 | None | None |
  
## cdir_campaign_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| campaign | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## cdir_configs_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_key | True | text | True | 255 | [cdir_campaign_junctions_tables](#cdir_campaign_junctions_tables) | key |
| faction_key | True | text | True | 255 | [cdir_faction_junctions_tables](#cdir_faction_junctions_tables) | key |
| cdir_config_key | True | text | True | 255 | [cdir_config_values_tables](#cdir_config_values_tables) | key |
| value | False | text | False | 255 | None | None |
  
## cdir_config_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cdir_desires_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cdir_desire_priorities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign_key | True | text | True | 255 | [cdir_campaign_junctions_tables](#cdir_campaign_junctions_tables) | key |
| desire_key | True | text | True | 255 | [cdir_desires_tables](#cdir_desires_tables) | key |
| priority | False | integer | True | None | None | None |
  
## cdir_events_dilemma_choices_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| choice_key | True | text | True | 255 | None | None |
  
## cdir_events_dilemma_choice_details_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| dilemma_key | True | text | True | 255 | [dilemmas_tables](#dilemmas_tables) | key |
| choice_key | True | text | True | 255 | [cdir_events_dilemma_choices_tables](#cdir_events_dilemma_choices_tables) | choice_key |
| localised_choice_label | False | text | True | 20000 | None | None |
| localised_choice_title | False | text | True | 20000 | None | None |
  
## cdir_events_dilemma_followup_dilemmas_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| dilemma_key | True | text | True | 255 | [dilemmas_tables](#dilemmas_tables) | key |
| choice_key | True | text | True | 255 | [cdir_events_dilemma_choices_tables](#cdir_events_dilemma_choices_tables) | choice_key |
| followup_dilemma_key | True | text | True | 255 | [dilemmas_tables](#dilemmas_tables) | key |
  
## cdir_events_dilemma_followup_missions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| dilemma_key | True | text | True | 255 | [dilemmas_tables](#dilemmas_tables) | key |
| choice_key | True | text | True | 255 | [cdir_events_dilemma_choices_tables](#cdir_events_dilemma_choices_tables) | choice_key |
| followup_mission_key | True | text | True | 255 | [missions_tables](#missions_tables) | key |
  
## cdir_events_dilemma_incidents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| dilemma_key | True | text | True | 255 | None | None |
| choice_key | True | text | True | 255 | None | None |
| incident_key | True | text | True | 255 | None | None |
  
## cdir_events_dilemma_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| option_key | True | text | True | 255 | None | None |
  
## cdir_events_dilemma_option_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| dilemma_key | False | text | True | 255 | [dilemmas_tables](#dilemmas_tables) | key |
| option_key | False | text | True | 255 | [cdir_events_dilemma_options_tables](#cdir_events_dilemma_options_tables) | option_key |
| value | False | text | False | 255 | None | None |
  
## cdir_events_dilemma_payloads_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| dilemma_key | False | text | True | 255 | None | None |
| choice_key | False | text | True | 255 | None | None |
| payload_key | False | text | True | 255 | [cdir_events_payloads_tables](#cdir_events_payloads_tables) | payload_key |
| value | False | text | False | 255 | None | None |
  
## cdir_events_incident_followup_dilemmas_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| incident_key | True | text | True | 255 | [incidents_tables](#incidents_tables) | key |
| followup_dliemma_key | True | text | True | 255 | [dilemmas_tables](#dilemmas_tables) | key |
  
## cdir_events_incident_followup_incidents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| incident_key | True | text | True | 255 | [incidents_tables](#incidents_tables) | key |
| followup_incident_key | True | text | True | 255 | [incidents_tables](#incidents_tables) | key |
  
## cdir_events_incident_followup_missions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| incident_key | True | text | True | 255 | [incidents_tables](#incidents_tables) | key |
| followup_mission_key | True | text | True | 255 | [missions_tables](#missions_tables) | key |
  
## cdir_events_incident_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| option_key | True | text | True | 255 | None | None |
  
## cdir_events_incident_option_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| incident_key | False | text | True | 255 | [incidents_tables](#incidents_tables) | key |
| option_key | False | text | True | 255 | [cdir_events_incident_options_tables](#cdir_events_incident_options_tables) | option_key |
| value | False | text | False | 255 | None | None |
  
## cdir_events_incident_payloads_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| incident_key | False | text | True | 255 | None | None |
| payload_key | False | text | True | 255 | [cdir_events_payloads_tables](#cdir_events_payloads_tables) | payload_key |
| value | False | text | False | 255 | None | None |
  
## cdir_events_mission_followup_dilemmas_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| mission_key | True | text | True | 255 | [missions_tables](#missions_tables) | key |
| status_key | True | text | True | 255 | [cdir_events_mission_statuses_tables](#cdir_events_mission_statuses_tables) | status_key |
| followup_dilemma_key | True | text | True | 255 | [dilemmas_tables](#dilemmas_tables) | key |
  
## cdir_events_mission_followup_missions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| mission_key | True | text | True | 255 | [missions_tables](#missions_tables) | key |
| status_key | True | text | True | 255 | [cdir_events_mission_statuses_tables](#cdir_events_mission_statuses_tables) | status_key |
| followup_mission_key | True | text | True | 255 | [missions_tables](#missions_tables) | key |
  
## cdir_events_mission_incidents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| mission_key | True | text | True | 255 | None | None |
| status_key | True | text | True | 255 | None | None |
| incident_key | True | text | True | 255 | None | None |
  
## cdir_events_mission_issuer_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| mission_key | True | text | True | 255 | None | None |
| issuer_key | True | text | True | 255 | [mission_issuers_tables](#mission_issuers_tables) | issuer_key |
  
## cdir_events_mission_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| option_key | True | text | True | 255 | None | None |
  
## cdir_events_mission_option_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| mission_key | False | text | True | 255 | [missions_tables](#missions_tables) | key |
| option_key | False | text | True | 255 | [cdir_events_mission_options_tables](#cdir_events_mission_options_tables) | option_key |
| value | False | text | False | 255 | None | None |
  
## cdir_events_mission_payloads_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| mission_key | False | text | True | 255 | None | None |
| status_key | False | text | True | 255 | None | None |
| payload_key | False | text | True | 255 | [cdir_events_payloads_tables](#cdir_events_payloads_tables) | payload_key |
| value | False | text | False | 255 | None | None |
  
## cdir_events_mission_statuses_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| status_key | True | text | True | 255 | None | None |
  
## cdir_events_payloads_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| payload_key | True | text | True | 255 | None | None |
| effect_bundle_key | False | text | False | 255 | None | None |
  
## cdir_faction_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| faction | False | text | False | 255 | [factions_tables](#factions_tables) | key |
  
## cdir_military_generator_configs_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cdir_military_generator_templates_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cdir_military_generator_template_priorities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| config_key | True | text | True | 255 | [cdir_military_generator_configs_tables](#cdir_military_generator_configs_tables) | key |
| template_key | True | text | True | 255 | [cdir_military_generator_templates_tables](#cdir_military_generator_templates_tables) | key |
| priority | False | integer | True | None | None | None |
  
## cdir_military_generator_template_ratios_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| template_key | True | text | True | 255 | [cdir_military_generator_templates_tables](#cdir_military_generator_templates_tables) | key |
| unit_group_key | True | text | True | 255 | [cdir_military_generator_unit_groups_tables](#cdir_military_generator_unit_groups_tables) | key |
| ratio | False | integer | True | None | None | None |
  
## cdir_military_generator_unit_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## cdir_military_generator_unit_qualities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| group_key | True | text | True | 255 | [cdir_military_generator_unit_groups_tables](#cdir_military_generator_unit_groups_tables) | key |
| unit_key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| quality | False | integer | True | None | None | None |
  
## centralised_upgrade_building_level_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| upgraded_building_level | True | text | True | 255 | [building_levels_tables](#building_levels_tables) | level_name |
| central_building_level | False | text | True | 255 | [building_levels_tables](#building_levels_tables) | level_name |
| priority | True | integer | True | None | None | None |
  
## character_experience_skill_tiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent_key | True | text | False | 255 | [agents_tables](#agents_tables) | key |
| skill_rank | True | integer | True | None | None | None |
| experience_threshold | False | integer | True | None | None | None |
| skill_points | False | integer | True | None | None | None |
| optional_campaign_key | True | text | False | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| for_army | True | yesno | True | None | None | None |
| for_navy | True | yesno | True | None | None | None |
  
## character_skills_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| image_path | False | text | True | 255 | None | None |
| localised_name | False | text | True | 255 | None | None |
| localised_description | False | text | True | 255 | None | None |
| pre_battle_speech_parameter | False | text | False | 255 | [pre_battle_speech_parameters_enum_tables](#pre_battle_speech_parameters_enum_tables) | key |
| unlocked_at_rank | False | integer | True | None | None | None |
| is_background_skill | False | yesno | True | None | None | None |
| is_female_only_background_skill | False | yesno | True | None | None | None |
| is_male_only_background_skill | False | yesno | True | None | None | None |
| background_weighting | False | single | True | None | None | None |
  
## character_skill_level_details_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| level | True | integer | True | None | None | None |
| skill_key | True | text | True | 255 | [character_skills_tables](#character_skills_tables) | key |
| faction_key | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| campaign_key | True | text | False | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| subculture_key | True | text | False | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| localised_name | False | text | False | 20000 | None | None |
| localised_description | False | text | False | 20000 | None | None |
| image_path | False | text | True | 255 | None | None |
| unlocked_at_rank | False | integer | True | None | None | None |
  
## character_skill_level_to_effects_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| character_skill_key | True | text | True | 255 | [character_skills_tables](#character_skills_tables) | key |
| level | True | integer | True | None | None | None |
| effect_key | True | text | True | 256 | [effects_tables](#effects_tables) | effect |
| value | False | single | True | None | None | None |
| is_factionwide | False | yesno | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## character_skill_nodes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| character_skill_node_set_key | False | text | True | 255 | [character_skill_node_sets_tables](#character_skill_node_sets_tables) | key |
| character_skill_key | False | text | True | 255 | [character_skills_tables](#character_skills_tables) | key |
| faction_key | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| campaign_key | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| tier | False | integer | True | None | None | None |
| indent | False | integer | True | None | None | None |
| subculture | False | text | False | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## character_skill_node_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| parent_key | True | text | True | 255 | [character_skill_nodes_tables](#character_skill_nodes_tables) | key |
| child_key | True | text | True | 255 | [character_skill_nodes_tables](#character_skill_nodes_tables) | key |
| initial_descent_tiers | False | integer | True | None | None | None |
| parent_link_position | False | integer | True | None | None | None |
| child_link_position | False | integer | True | None | None | None |
  
## character_skill_node_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| faction_key | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| campaign_key | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| agent_key | False | text | False | 255 | [agents_tables](#agents_tables) | key |
| enc_title | False | text | True | 1024 | None | None |
| subculture | False | text | False | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| for_army | False | yesno | True | None | None | None |
| for_navy | False | yesno | True | None | None | None |
  
## character_traits_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | [trait_info_tables](#trait_info_tables) | trait |
| no_going_back_level | False | integer | True | None | None | None |
| hidden | False | yesno | True | None | None | None |
| precedence | False | integer | False | None | None | None |
| icon | False | text | True | 50 | [trait_categories_tables](#trait_categories_tables) | category |
| author | False | text | True | 50 | None | None |
| comment | False | text | False | 536870910 | None | None |
| pre_battle_speech_parameter | False | text | False | 255 | [pre_battle_speech_parameters_enum_tables](#pre_battle_speech_parameters_enum_tables) | key |
  
## character_trait_levels_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| onscreen_name | False | text | True | 50 | None | None |
| trait | False | text | True | 50 | [trait_info_tables](#trait_info_tables) | trait |
| level | False | integer | True | None | None | None |
| threshold_points | False | integer | True | None | None | None |
| epithet_text | False | text | False | 536870910 | None | None |
| gain_text | False | text | False | 536870910 | None | None |
| effect_text | False | text | False | 536870910 | None | None |
| colour_text | False | text | True | 536870910 | None | None |
| explanation_text | False | text | False | 536870910 | None | None |
| removal_text | False | text | False | 536870910 | None | None |
| enabled_by_tech | False | text | False | 255 | [technologies_tables](#technologies_tables) | key |
  
## chariot_types_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## chat_shortcuts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| description | False | text | True | 20000 | None | None |
| game_area | False | text | True | 255 | [game_area_enums_tables](#game_area_enums_tables) | key |
  
## climates_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| climate_type | True | text | True | 50 | None | None |
| colour_index | False | integer | True | None | None | None |
| conifer_line | False | integer | True | None | None | None |
| tree_line | False | integer | True | None | None | None |
| is_land | False | yesno | False | None | None | None |
  
## climate_to_weather_land_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| Climate_type | True | text | True | 50 | [climates_tables](#climates_tables) | climate_type |
| season | True | text | True | 50 | [seasons_tables](#seasons_tables) | season |
| Dry | False | integer | True | None | None | None |
| Dusty | False | integer | True | None | None | None |
| Sandstorm | False | integer | True | None | None | None |
| Drizzle | False | integer | True | None | None | None |
| Light_rain | False | integer | True | None | None | None |
| Moderate_rain | False | integer | True | None | None | None |
| Heavy_rain | False | integer | True | None | None | None |
| Storm | False | integer | True | None | None | None |
| Light_snow | False | integer | True | None | None | None |
| Moderate_snow | False | integer | True | None | None | None |
| Heavy_snow | False | integer | True | None | None | None |
| Blizzard | False | integer | True | None | None | None |
| Heat_fatigue | False | integer | True | None | None | None |
| Cold_fatigue | False | integer | True | None | None | None |
| Haze_index | False | integer | True | None | None | None |
| Fog_index | False | integer | True | None | None | None |
  
## commander_unit_permissions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| faction_key | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| culture_key | True | text | False | 255 | [cultures_tables](#cultures_tables) | key |
| subculture_key | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## commodities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [resources_tables](#resources_tables) | key |
| baseline_price_per_unit | False | double | True | None | None | None |
| price_elasticity_of_demand | False | double | True | None | None | None |
  
## commodity_unit_names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit | True | text | True | 50 | None | None |
| plural | False | text | True | 50 | None | None |
| singular | False | text | True | 50 | None | None |
  
## cultures_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| index | False | autonumber | True | None | None | None |
| fallback_ui_culture | False | text | False | 50 | None | None |
| name | False | text | True | 255 | None | None |
  
## cultures_subcultures_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| subculture | True | text | True | 50 | None | None |
| culture | False | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| index | False | autonumber | True | None | None | None |
| farm | False | text | True | 50 | [battle_terrain_farms_tables](#battle_terrain_farms_tables) | farm |
| name | False | text | True | 255 | None | None |
| confederation_screen_name | False | text | False | 255 | None | None |
| confederation_summary_name | False | text | False | 255 | None | None |
  
## culture_settlement_occupation_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| option | True | text | True | 255 | None | None |
  
## culture_subculture_character_portraits_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| portrait_type | True | text | True | 255 | [portrait_types_tables](#portrait_types_tables) | key |
| culture | True | text | False | 255 | [cultures_tables](#cultures_tables) | key |
| subculture | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| path | False | text | True | 255 | None | None |
  
## culture_subculture_politics_government_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| culture | True | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| government_type | True | text | True | 255 | [politics_government_types_tables](#politics_government_types_tables) | government_type |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| on_screen_name_government_type | False | text | True | 255 | None | None |
| on_screen_name_faction_leader | False | text | False | 255 | None | None |
| effect_bundle | False | text | False | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| is_default | False | yesno | True | None | None | None |
| faction_leader_trait | False | text | True | 255 | [trait_info_tables](#trait_info_tables) | trait |
| on_screen_name_faction_leader_female | False | text | False | 255 | None | None |
| faction_leader_trait_female | False | text | True | 255 | [trait_info_tables](#trait_info_tables) | trait |
| on_screen_name_government_actions | False | text | False | 255 | None | None |
| on_screen_descr_government_actions | False | text | False | 255 | None | None |
  
## cursors_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| image | False | text | True | 50 | None | None |
| frames | False | integer | True | None | None | None |
| framerate | False | integer | True | None | None | None |
| hotspotX | False | integer | True | None | None | None |
| hotspotY | False | integer | True | None | None | None |
| loop | False | yesno | True | None | None | None |
| width | False | integer | False | None | None | None |
| height | False | integer | False | None | None | None |
  
## cursor_mouse_events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 20000 | None | None |
  
## cursor_transitions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| initiating_cursor | True | text | True | 50 | [cursors_tables](#cursors_tables) | key |
| resulting_cursor | False | text | True | 50 | [cursors_tables](#cursors_tables) | key |
| mouse_event | True | text | True | 20000 | [cursor_mouse_events_tables](#cursor_mouse_events_tables) | key |
  
## cursus_honorum_level_requirements_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| subculture_key | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| level | True | integer | True | None | None | None |
| rank | False | integer | True | None | None | None |
| age | False | integer | True | None | None | None |
| faction_key | True | text | False | 255 | [factions_tables](#factions_tables) | key |
  
## cursus_honorum_trait_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| subculture_key | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| trait_info_key | True | text | True | 255 | [trait_info_tables](#trait_info_tables) | trait |
| faction_key | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| trait_info_key_female | True | text | False | 255 | [trait_info_tables](#trait_info_tables) | trait |
  
## dave_permissions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| permission | True | text | True | 255 | None | None |
  
## dave_restricted_tables_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| table_name | True | text | True | 255 | [TExc_ImplementedTables_tables](#TExc_ImplementedTables_tables) | table_name |
  
## dave_user_table_permissions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| user_name | True | text | True | 255 | None | None |
| table_name | True | text | True | 255 | [TExc_ImplementedTables_tables](#TExc_ImplementedTables_tables) | table_name |
| permission | True | text | True | 255 | [dave_permissions_tables](#dave_permissions_tables) | permission |
  
## death_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## deployables_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| name | False | text | True | 255 | None | None |
| model | False | text | True | 255 | [models_deployables_tables](#models_deployables_tables) | key |
| model_2 | False | text | False | 255 | [models_deployables_tables](#models_deployables_tables) | key |
| number | False | integer | True | None | None | None |
| spacing_x | False | decimal | True | None | None | None |
| spacing_y | False | decimal | True | None | None | None |
| min_rows | False | integer | True | None | None | None |
| min_columns | False | integer | True | None | None | None |
| random_offset | False | decimal | True | None | None | None |
| hitpoints | False | integer | True | None | None | None |
| kill_chance | False | decimal | True | None | None | None |
| stat_mod | False | text | False | 255 | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| value | False | decimal | True | None | None | None |
| how | False | text | False | 255 | [unit_stat_modifiers_how_enums_tables](#unit_stat_modifiers_how_enums_tables) | key |
| icon_name | False | text | True | 255 | None | None |
| info_pic | False | text | True | 255 | None | None |
| description | False | text | True | 255 | None | None |
| tooltip | False | text | True | 255 | None | None |
| in_encyclopaedia | False | yesno | True | None | None | None |
| recruitment_cap | False | integer | True | None | None | None |
| max_rows | False | integer | True | None | None | None |
| ignition_threshold | False | integer | True | None | None | None |
  
## deployables_custom_battles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| deployable | True | text | True | 255 | [deployables_tables](#deployables_tables) | key |
| cap | False | integer | True | None | None | None |
| probability | False | integer | True | None | None | None |
  
## dilemmas_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| localised_title | False | text | True | 255 | None | None |
| localised_description | False | text | True | 900000 | None | None |
| ui_image | False | text | True | 255 | None | None |
| ui_icon | False | text | True | 255 | None | None |
| generate | False | yesno | True | None | None | None |
| prioritized | False | yesno | True | None | None | None |
  
## dilemma_to_campaign_subject_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| dilemma_key | True | text | True | 255 | [dilemmas_tables](#dilemmas_tables) | key |
| campaign_subject_key | True | text | True | 255 | [campaign_subjects_tables](#campaign_subjects_tables) | key |
| weighting | False | single | True | None | None | None |
  
## diplomacy_current_treaties_to_diplomatic_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| current_treaty_key | True | text | True | 255 | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| diplomatic_option_key | False | text | True | 255 | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| can_be_cancelled | False | yesno | True | None | None | None |
  
## diplomacy_keys_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## diplomacy_negotiation_attitudes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| minimum_attitude | False | integer | True | None | None | None |
| maximum_attitude | False | integer | True | None | None | None |
  
## diplomacy_negotiation_attitude_override_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [diplomacy_keys_tables](#diplomacy_keys_tables) | key |
| culture | True | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| government_type | True | text | True | 255 | [government_types_tables](#government_types_tables) | government_type |
| attitude | True | text | True | 255 | [diplomacy_negotiation_attitudes_tables](#diplomacy_negotiation_attitudes_tables) | key |
| string | False | text | True | 255 | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| option | True | integer | True | None | None | None |
  
## diplomacy_negotiation_faction_attitude_override_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [diplomacy_keys_tables](#diplomacy_keys_tables) | key |
| culture | True | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| government_type | True | text | True | 255 | [government_types_tables](#government_types_tables) | government_type |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| attitude | True | text | True | 255 | [diplomacy_negotiation_attitudes_tables](#diplomacy_negotiation_attitudes_tables) | key |
| string | False | text | True | 255 | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| option | True | integer | True | None | None | None |
  
## diplomacy_negotiation_faction_override_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | [diplomacy_keys_tables](#diplomacy_keys_tables) | key |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| government_type | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| faction | True | text | True | 50 | [factions_tables](#factions_tables) | key |
| string | False | text | True | 255 | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| option | True | integer | True | None | None | None |
  
## diplomacy_negotiation_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [diplomacy_keys_tables](#diplomacy_keys_tables) | key |
| culture | True | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| government_type | True | text | True | 255 | [government_types_tables](#government_types_tables) | government_type |
  
## diplomacy_negotiation_string_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | [diplomacy_keys_tables](#diplomacy_keys_tables) | key |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| government_type | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| string | False | text | True | 255 | [diplomacy_strings_tables](#diplomacy_strings_tables) | key |
| option | True | integer | True | None | None | None |
  
## diplomacy_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| string | False | text | True | 536870910 | None | None |
  
## diplomatic_action_faction_restrictions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| can_make_vassals | False | yesno | True | None | None | None |
| can_make_client_states | False | yesno | True | None | None | None |
| can_make_confederations | False | yesno | True | None | None | None |
  
## diplomatic_action_subculture_restrictions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| subculture | True | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| can_make_vassals | False | yesno | True | None | None | None |
| can_make_client_states | False | yesno | True | None | None | None |
| can_make_confederations | False | yesno | True | None | None | None |
  
## diplomatic_relations_attitudes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| attitude | True | text | True | 50 | None | None |
| value | False | text | True | 50 | None | None |
  
## diplomatic_relations_religion_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| religion_A | True | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
| religion_B | True | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
| relations_modifier | False | integer | True | None | None | None |
| religious_unhappiness_modifier | False | single | True | None | None | None |
  
## effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | False | 50 | None | None |
| icon | False | text | False | 256 | None | None |
| description | False | text | False | 536870910 | None | None |
| priority | False | integer | True | None | None | None |
| icon_negative | False | text | False | 256 | None | None |
  
## effect_bonus_value_agent_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_agent_tables](#campaign_bonus_value_ids_agent_tables) | key |
| agent | True | text | True | 255 | [agents_tables](#agents_tables) | key |
  
## effect_bonus_value_basic_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_basic_tables](#campaign_bonus_value_ids_basic_tables) | key |
  
## effect_bonus_value_battlefield_deployables_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_battlefield_deployables_tables](#campaign_bonus_value_ids_battlefield_deployables_tables) | key |
| battlefield_deployable | True | text | True | 255 | [deployables_tables](#deployables_tables) | key |
  
## effect_bonus_value_battle_context_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect_key | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_battle_contexts_tables](#campaign_bonus_value_ids_battle_contexts_tables) | key |
| battle_context_key | False | text | True | 255 | [campaign_bonus_value_battle_context_specifiers_tables](#campaign_bonus_value_battle_context_specifiers_tables) | key |
  
## effect_bonus_value_building_chain_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | False | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | False | 255 | [campaign_bonus_value_ids_building_chain_tables](#campaign_bonus_value_ids_building_chain_tables) | key |
| building_chain | True | text | False | 50 | [building_chains_tables](#building_chains_tables) | key |
  
## effect_bonus_value_building_set_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_building_sets_tables](#campaign_bonus_value_ids_building_sets_tables) | key |
| building_set | True | text | True | 255 | [building_sets_tables](#building_sets_tables) | key |
  
## effect_bonus_value_commodity_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_commodity_tables](#campaign_bonus_value_ids_commodity_tables) | key |
| commodity | True | text | True | 255 | [commodities_tables](#commodities_tables) | key |
  
## effect_bonus_value_ids_unit_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_unit_sets_tables](#campaign_bonus_value_ids_unit_sets_tables) | key |
| unit_set | True | text | True | 255 | [unit_sets_tables](#unit_sets_tables) | key |
  
## effect_bonus_value_id_action_results_additional_outcomes_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_action_results_additional_outcomes_tables](#campaign_bonus_value_ids_action_results_additional_outcomes_tables) | key |
| action_results_additional_outcome_record | True | text | True | 255 | [action_results_additional_outcomes_tables](#action_results_additional_outcomes_tables) | key |
  
## effect_bonus_value_melee_weapon_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| melee_weapon | True | text | True | 50 | [unit_melee_weapons_enum_tables](#unit_melee_weapons_enum_tables) | key |
| stat_modifier | False | text | True | 255 | [unit_stat_modifiers_tables](#unit_stat_modifiers_tables) | key |
  
## effect_bonus_value_population_class_and_religion_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_population_class_and_religion_tables](#campaign_bonus_value_ids_population_class_and_religion_tables) | key |
| population_class | True | text | True | 50 | [population_classes_tables](#population_classes_tables) | population_class |
| religion | True | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
  
## effect_bonus_value_population_class_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_population_class_tables](#campaign_bonus_value_ids_population_class_tables) | key |
| population_class | True | text | True | 50 | [population_classes_tables](#population_classes_tables) | population_class |
  
## effect_bonus_value_projectile_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| projectile | True | text | True | 255 | [projectiles_tables](#projectiles_tables) | key |
| bonus_value | True | text | True | 255 | [campaign_bonus_value_ids_projectile_tables](#campaign_bonus_value_ids_projectile_tables) | key |
  
## effect_bonus_value_provincial_initiative_effect_record_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_provincial_initiative_effect_records_tables](#campaign_bonus_value_ids_provincial_initiative_effect_records_tables) | key |
| effect_bonus_will_modify | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
  
## effect_bonus_value_religion_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_religion_tables](#campaign_bonus_value_ids_religion_tables) | key |
| religion | True | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
  
## effect_bonus_value_resource_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_resource_tables](#campaign_bonus_value_ids_resource_tables) | key |
| resource | True | text | True | 50 | [resources_tables](#resources_tables) | key |
  
## effect_bonus_value_shot_type_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_projectile_shot_type_enum_tables](#campaign_bonus_value_ids_projectile_shot_type_enum_tables) | key |
| shot_type | True | text | True | 50 | [projectile_shot_type_enum_tables](#projectile_shot_type_enum_tables) | key |
  
## effect_bonus_value_siege_item_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_siege_items_tables](#campaign_bonus_value_ids_siege_items_tables) | key |
| siege_item | True | text | True | 50 | [battlefield_deployable_siege_items_tables](#battlefield_deployable_siege_items_tables) | key |
  
## effect_bonus_value_technology_category_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 64 | [campaign_bonus_value_ids_technology_categories_tables](#campaign_bonus_value_ids_technology_categories_tables) | key |
| technology_category | True | text | True | 255 | [technology_categories_tables](#technology_categories_tables) | key |
  
## effect_bonus_value_unit_ability_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_unit_ability_tables](#campaign_bonus_value_ids_unit_ability_tables) | key |
| unit_ability | True | text | True | 50 | [unit_abilities_tables](#unit_abilities_tables) | key |
  
## effect_bonus_value_unit_caste_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_unit_caste_tables](#campaign_bonus_value_ids_unit_caste_tables) | key |
| caste | True | text | True | 50 | [unit_castes_tables](#unit_castes_tables) | caste |
  
## effect_bonus_value_unit_caste_stat_modifiers_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| caste | True | text | True | 255 | [unit_castes_tables](#unit_castes_tables) | caste |
| stat_modifier | True | text | True | 255 | [unit_stat_modifiers_tables](#unit_stat_modifiers_tables) | key |
  
## effect_bonus_value_unit_category_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_unit_category_tables](#campaign_bonus_value_ids_unit_category_tables) | key |
| unit_category | True | text | True | 50 | [unit_category_tables](#unit_category_tables) | key |
  
## effect_bonus_value_unit_category_stat_modifiers_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| category | True | text | True | 50 | [unit_category_tables](#unit_category_tables) | key |
| stat_modifier | True | text | True | 255 | [unit_stat_modifiers_tables](#unit_stat_modifiers_tables) | key |
  
## effect_bonus_value_unit_class_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_unit_class_tables](#campaign_bonus_value_ids_unit_class_tables) | key |
| unit_class | True | text | True | 50 | [unit_class_tables](#unit_class_tables) | key |
  
## effect_bonus_value_unit_class_stat_modifiers_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| class | True | text | True | 255 | [unit_class_tables](#unit_class_tables) | key |
| stat_modifier | True | text | True | 255 | [unit_stat_modifiers_tables](#unit_stat_modifiers_tables) | key |
  
## effect_bonus_value_unit_record_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| bonus_value_id | True | text | True | 255 | [campaign_bonus_value_ids_unit_records_tables](#campaign_bonus_value_ids_unit_records_tables) | key |
| unit_record_key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
  
## effect_bonus_value_unit_record_stat_modifiers_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| unit | True | text | True | 255 | [units_tables](#units_tables) | key |
| stat_modifier | True | text | True | 255 | [unit_stat_modifiers_tables](#unit_stat_modifiers_tables) | key |
  
## effect_bonus_value_unit_stat_modifiers_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect | True | text | True | 255 | [effects_tables](#effects_tables) | effect |
| stat_modifier | True | text | True | 255 | [unit_stat_modifiers_tables](#unit_stat_modifiers_tables) | key |
  
## effect_bundles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| localised_title | False | text | True | 255 | None | None |
| localised_description | False | text | True | 255 | None | None |
| ui_icon | False | text | True | 255 | None | None |
| bundle_target | False | text | True | 255 | [effect_bundle_targets_tables](#effect_bundle_targets_tables) | key |
  
## effect_bundles_to_effects_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect_bundle_key | True | text | True | 255 | None | None |
| effect_key | True | text | True | 255 | None | None |
| value | False | single | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
| advancement_stage | False | text | True | 255 | [effect_bundle_advancement_stages_tables](#effect_bundle_advancement_stages_tables) | key |
  
## effect_bundle_advancement_stages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## effect_bundle_targets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## encyclopedia_agent_manual_block_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent_key | True | text | True | 255 | [agents_tables](#agents_tables) | key |
| block_key | True | text | True | 255 | [encyclopedia_blocks_tables](#encyclopedia_blocks_tables) | block_key |
  
## encyclopedia_agent_manual_page_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent_key | True | text | True | 255 | [agents_tables](#agents_tables) | key |
| page_key | True | text | True | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
  
## encyclopedia_blocks_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| block_key | True | text | True | 255 | None | None |
| page_key | False | text | True | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
| order | False | integer | True | None | None | None |
| heading | False | text | True | 65535 | None | None |
| class | False | text | True | 255 | None | None |
| content | False | text | True | 65535 | None | None |
| image | False | text | False | 65535 | None | None |
| image_class | False | text | True | 65535 | None | None |
| video | False | text | False | 65535 | None | None |
  
## encyclopedia_building_chain_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| group_name | True | text | True | 255 | None | None |
| localised_name | False | text | True | 255 | None | None |
| order | False | integer | True | None | None | None |
  
## encyclopedia_building_redirects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| building | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| redirect_building | False | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
  
## encyclopedia_faction_groupings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| group | False | text | True | 255 | [encyclopedia_faction_groups_tables](#encyclopedia_faction_groups_tables) | group_id |
| order | False | integer | True | None | None | None |
  
## encyclopedia_faction_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| group_id | True | text | True | 255 | None | None |
  
## encyclopedia_faction_iconic_units_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| main_unit_key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| faction_key | True | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## encyclopedia_glossary_blocks_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| block_key | True | text | True | 255 | None | None |
| page_key | False | text | True | 255 | [encyclopedia_glossary_pages_tables](#encyclopedia_glossary_pages_tables) | page_key |
| order | False | integer | True | None | None | None |
| heading | False | text | True | 65535 | None | None |
| class | False | text | True | 255 | None | None |
| content | False | text | True | 65535 | None | None |
| image | False | text | False | 65535 | None | None |
| image_class | False | text | True | 65535 | None | None |
| video | False | text | False | 65535 | None | None |
  
## encyclopedia_glossary_pages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | None | None |
| title | False | text | True | 65535 | None | None |
| template | False | text | True | 65535 | None | None |
  
## encyclopedia_glossary_page_linkages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | [encyclopedia_glossary_pages_tables](#encyclopedia_glossary_pages_tables) | page_key |
| parent_key | False | text | False | 255 | [encyclopedia_glossary_pages_tables](#encyclopedia_glossary_pages_tables) | page_key |
| next_key | False | text | False | 255 | [encyclopedia_glossary_pages_tables](#encyclopedia_glossary_pages_tables) | page_key |
  
## encyclopedia_historical_info_blocks_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| block_key | True | text | True | 255 | None | None |
| page_key | False | text | True | 255 | [encyclopedia_historical_info_pages_tables](#encyclopedia_historical_info_pages_tables) | page_key |
| order | False | integer | True | None | None | None |
| heading | False | text | True | 65535 | None | None |
| class | False | text | True | 255 | None | None |
| content | False | text | True | 65535 | None | None |
| image | False | text | False | 65535 | None | None |
| image_class | False | text | True | 65535 | None | None |
| video | False | text | False | 65535 | None | None |
  
## encyclopedia_historical_info_pages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | None | None |
| title | False | text | True | 65535 | None | None |
| template | False | text | True | 65535 | None | None |
  
## encyclopedia_historical_info_page_linkages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | [encyclopedia_historical_info_pages_tables](#encyclopedia_historical_info_pages_tables) | page_key |
| parent_key | False | text | False | 255 | [encyclopedia_historical_info_pages_tables](#encyclopedia_historical_info_pages_tables) | page_key |
| next_key | False | text | False | 255 | [encyclopedia_historical_info_pages_tables](#encyclopedia_historical_info_pages_tables) | page_key |
  
## encyclopedia_index_pages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | None | None |
| annotation | False | text | True | 255 | [encyclopedia_blocks_tables](#encyclopedia_blocks_tables) | block_key |
  
## encyclopedia_multiplayer_blocks_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| block_key | True | text | True | 255 | None | None |
| page_key | False | text | True | 255 | [encyclopedia_multiplayer_pages_tables](#encyclopedia_multiplayer_pages_tables) | page_key |
| order | False | integer | True | None | None | None |
| heading | False | text | True | 65535 | None | None |
| class | False | text | True | 255 | None | None |
| content | False | text | True | 65535 | None | None |
| image | False | text | False | 65535 | None | None |
| image_class | False | text | True | 65535 | None | None |
| video | False | text | False | 65535 | None | None |
  
## encyclopedia_multiplayer_pages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | None | None |
| title | False | text | True | 65535 | None | None |
| template | False | text | True | 65535 | None | None |
  
## encyclopedia_multiplayer_page_linkages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | [encyclopedia_multiplayer_pages_tables](#encyclopedia_multiplayer_pages_tables) | page_key |
| parent_key | False | text | False | 255 | [encyclopedia_multiplayer_pages_tables](#encyclopedia_multiplayer_pages_tables) | page_key |
| next_key | False | text | False | 255 | [encyclopedia_multiplayer_pages_tables](#encyclopedia_multiplayer_pages_tables) | page_key |
  
## encyclopedia_pages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | None | None |
| title | False | text | True | 65535 | None | None |
| template | False | text | True | 65535 | None | None |
  
## encyclopedia_page_linkages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
| parent_key | False | text | False | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
| next_key | False | text | False | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
  
## encyclopedia_page_related_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| page_key | True | text | True | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
| target | True | text | True | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
  
## encyclopedia_patch_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| text | False | text | True | 255 | None | None |
  
## encyclopedia_projectile_shot_type_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| shot_type | True | text | True | 50 | [projectile_shot_type_enum_tables](#projectile_shot_type_enum_tables) | key |
| manual_page | False | text | True | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
| manual_block | False | text | False | 255 | [encyclopedia_blocks_tables](#encyclopedia_blocks_tables) | block_key |
  
## encyclopedia_settings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| value | False | text | True | 1024 | None | None |
  
## encyclopedia_template_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| string_key | True | text | True | 255 | None | None |
| text | False | text | True | 65535 | None | None |
  
## encyclopedia_triggers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_key | True | text | True | 65535 | None | None |
| url | False | text | True | 65535 | None | None |
  
## encyclopedia_tutorial_sections_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| section | True | text | True | 255 | None | None |
| name | False | text | True | 20000 | None | None |
  
## encyclopedia_tutorial_videos_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| title | False | text | True | 20000 | None | None |
| section | False | text | True | 255 | [encyclopedia_tutorial_sections_tables](#encyclopedia_tutorial_sections_tables) | section |
| file | False | text | True | 255 | None | None |
| description | False | text | True | 200000 | None | None |
  
## encyclopedia_tutorial_videos_default_subtitles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| video | True | text | True | 255 | [encyclopedia_tutorial_videos_tables](#encyclopedia_tutorial_videos_tables) | key |
| language | True | text | True | 255 | [languages_tables](#languages_tables) | key |
  
## encyclopedia_tutorial_video_subtitles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [encyclopedia_tutorial_videos_tables](#encyclopedia_tutorial_videos_tables) | key |
| subtitle_number | True | integer | True | None | None | None |
| timecode_in | False | text | True | 255 | None | None |
| timecode_out | False | text | True | 255 | None | None |
| text | False | text | True | 20000 | None | None |
| line | False | integer | True | None | None | None |
  
## encyclopedia_unit_abilities_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_ability | True | text | True | 50 | [unit_abilities_tables](#unit_abilities_tables) | key |
| manual_page | False | text | True | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
| manual_block | False | text | False | 255 | [encyclopedia_blocks_tables](#encyclopedia_blocks_tables) | block_key |
  
## encyclopedia_unit_attributes_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_attribute | True | text | True | 255 | [unit_attributes_tables](#unit_attributes_tables) | key |
| manual_page | False | text | True | 255 | [encyclopedia_pages_tables](#encyclopedia_pages_tables) | page_key |
| manual_block | False | text | False | 255 | [encyclopedia_blocks_tables](#encyclopedia_blocks_tables) | block_key |
  
## encyclopedia_unit_patch_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| patch_text | False | text | True | 255 | [encyclopedia_patch_texts_tables](#encyclopedia_patch_texts_tables) | key |
  
## encyclopedia_unit_redirects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| redirect_unit | False | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
  
## encyclopedia_urls_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 255 | None | None |
| url | False | text | False | 255 | None | None |
  
## entity_training_levels_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| training_level | True | text | True | 50 | None | None |
| max_offset_distance | False | double | True | None | None | None |
  
## events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| picture_category | False | text | True | 255 | None | None |
| dynamic | False | yesno | True | None | None | None |
| onscreen_name | False | text | True | 255 | None | None |
| event_text | False | text | True | 536870910 | None | None |
| historical_date | False | double | True | None | None | None |
| season | False | text | True | 50 | [seasons_tables](#seasons_tables) | season |
| conditions | False | text | True | 536870910 | None | None |
| picture | False | text | True | 255 | None | None |
| turn_in_year | False | integer | True | None | None | None |
  
## events_effects_junct_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| event | True | text | True | 50 | [events_tables](#events_tables) | key |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | text | True | 50 | None | None |
  
## event_log_descriptions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| event_key | True | text | True | 255 | None | None |
| event_title | False | text | True | 255 | None | None |
| event_content | False | text | True | 255 | None | None |
| icon | False | text | True | 255 | None | None |
| has_position | False | yesno | True | None | None | None |
| is_region_position | False | yesno | True | None | None | None |
| notes | False | text | False | 65535 | None | None |
| optional_campaign_key | False | text | False | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| movie_id | False | integer | True | None | None | None |
  
## experience_triggers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| trigger_key | True | text | True | 255 | None | None |
| event | False | text | True | 255 | [trigger_events_tables](#trigger_events_tables) | event |
| experience_points | False | integer | True | None | None | None |
| condition | False | text | True | 255 | None | None |
| localised_description | False | text | False | 255 | None | None |
| target | False | text | True | 2000 | [experience_triggers_targets_tables](#experience_triggers_targets_tables) | key |
  
## experience_triggers_targets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 2000 | None | None |
  
## factions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| index | False | autonumber | True | None | None | None |
| subculture | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| category | False | text | True | 255 | None | None |
| screen_name | False | text | True | 255 | None | None |
| screen_name_when_rebels | False | text | True | 255 | None | None |
| screen_adjective | False | text | True | 255 | None | None |
| name_group | False | integer | True | None | [names_groups_tables](#names_groups_tables) | key |
| skin | False | text | True | 50 | None | None |
| is_rebel | False | yesno | True | None | None | None |
| icons_path_units | False | text | True | 50 | None | None |
| flags_path | False | text | True | 50 | None | None |
| republican_flag_path | False | text | False | 255 | None | None |
| same_gov_type_revolution_flag_path | False | text | False | 255 | None | None |
| primary_colour_r | False | double | True | None | None | None |
| primary_colour_g | False | double | True | None | None | None |
| primary_colour_b | False | double | True | None | None | None |
| alt_primary_colour_r | False | double | True | None | None | None |
| alt_primary_colour_g | False | double | True | None | None | None |
| alt_primary_colour_b | False | double | True | None | None | None |
| secondary_colour_r | False | double | True | None | None | None |
| secondary_colour_g | False | double | True | None | None | None |
| secondary_colour_b | False | double | True | None | None | None |
| alt_secondary_colour_r | False | double | True | None | None | None |
| alt_secondary_colour_g | False | double | True | None | None | None |
| alt_secondary_colour_b | False | double | True | None | None | None |
| rebel_colour_r | False | double | True | None | None | None |
| rebel_colour_g | False | double | True | None | None | None |
| rebel_colour_b | False | double | True | None | None | None |
| uniform_colour_r | False | double | True | None | None | None |
| uniform_colour_g | False | double | True | None | None | None |
| uniform_colour_b | False | double | True | None | None | None |
| alt_uniform_colour_r | False | double | True | None | None | None |
| alt_uniform_colour_g | False | double | True | None | None | None |
| alt_uniform_colour_b | False | double | True | None | None | None |
| military_group | False | text | False | 50 | [groupings_military_tables](#groupings_military_tables) | military_group |
| settler_rebellion_faction | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| mp_available | False | yesno | False | None | None | None |
| mp_available_naval | False | yesno | False | None | None | None |
| movie_death_event | False | integer | False | None | [movie_event_strings_tables](#movie_event_strings_tables) | id |
| mp_use_republic_early | False | yesno | False | None | None | None |
| mp_use_republic_late | False | yesno | False | None | None | None |
| unit_regiment_name_group | False | integer | True | None | [names_groups_tables](#names_groups_tables) | key |
| ship_name_group | False | integer | True | None | [names_groups_tables](#names_groups_tables) | key |
| ui_skin | False | text | False | 255 | None | None |
| attack_desc | False | text | True | 255 | None | None |
| defend_desc | False | text | True | 255 | None | None |
| mp_stats_name | False | text | False | 255 | None | None |
| pre_battle_speech_parameter | False | text | True | 255 | [pre_battle_speech_parameters_enum_tables](#pre_battle_speech_parameters_enum_tables) | key |
| screen_name_when_shogun | False | text | True | 2048 | None | None |
| clan_summary_name | False | text | False | 2048 | None | None |
| clan_summary_name_when_shogun | False | text | False | 2048 | None | None |
| can_be_regionless | False | yesno | True | None | None | None |
| card_colour_r | False | double | True | None | None | None |
| card_colour_g | False | double | True | None | None | None |
| card_colour_b | False | double | True | None | None | None |
| diplomacy_culture | False | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| senator_total | False | integer | True | None | None | None |
| senator_text_n_out_of_n | False | text | False | 255 | None | None |
| senator_text_lose_n | False | text | False | 255 | None | None |
| senator_text_lose_1 | False | text | False | 255 | None | None |
| senator_text_gain_n | False | text | False | 255 | None | None |
| senator_text_gain_1 | False | text | False | 255 | None | None |
| uses_legion_names | False | yesno | True | None | None | None |
  
## factions_parents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction | True | text | True | 50 | [factions_tables](#factions_tables) | key |
| parent_faction | False | text | True | 50 | [factions_tables](#factions_tables) | key |
  
## faction_banners_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| symbol | False | text | False | 255 | None | None |
| primary_red | False | integer | True | None | None | None |
| primary_green | False | integer | True | None | None | None |
| primary_blue | False | integer | True | None | None | None |
| secondary_red | False | integer | True | None | None | None |
| secondary_green | False | integer | True | None | None | None |
| secondary_blue | False | integer | True | None | None | None |
| tertiary_red | False | integer | True | None | None | None |
| tertiary_green | False | integer | True | None | None | None |
| tertiary_blue | False | integer | True | None | None | None |
  
## faction_civil_war_setups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| primary_faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| secondary_faction | False | text | True | 255 | [factions_tables](#factions_tables) | key |
| faction_name_override_primary_high | False | text | False | 255 | None | None |
| faction_name_override_primary_low | False | text | False | 255 | None | None |
| faction_name_override_secondary_high | False | text | False | 255 | None | None |
| faction_name_override_secondary_low | False | text | False | 255 | None | None |
| faction_name_override_victory | False | text | False | 255 | None | None |
| faction_leader_title_override_victory | False | text | False | 255 | None | None |
| secessionist_faction | False | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## faction_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| name_localised | False | text | True | 255 | None | None |
| ui_icon | False | text | True | 255 | None | None |
| effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| description_localised | False | text | True | 255 | None | None |
  
## faction_political_parties_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction_key | False | text | True | 255 | [factions_tables](#factions_tables) | key |
| political_party_key | True | text | True | 255 | [political_parties_tables](#political_parties_tables) | key |
  
## faction_politics_government_actions_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| type | True | text | True | 255 | [politics_government_actions_tables](#politics_government_actions_tables) | key |
| image_path | False | text | True | 255 | None | None |
| title | False | text | True | 255 | None | None |
| description | False | text | True | 255 | None | None |
| cost | False | integer | True | None | None | None |
| cost_per_region | False | integer | True | None | None | None |
| cooldown | False | integer | True | None | None | None |
  
## faction_rebellion_units_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction_key | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| unit_key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
  
## faction_resource_consumptions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| number_of_regions | True | integer | True | None | None | None |
| resource_consumption | False | integer | True | None | None | None |
  
## faction_to_campaign_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## faction_to_faction_groups_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction_key | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| faction_group_key | False | text | True | 255 | [faction_groups_tables](#faction_groups_tables) | key |
  
## faction_to_mercenary_set_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| mercenary_set | True | text | True | 255 | [mercenary_pools_tables](#mercenary_pools_tables) | key |
  
## faction_uniform_colours_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction_name | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| primary_colour_r | False | double | True | None | None | None |
| primary_colour_g | False | double | True | None | None | None |
| primary_colour_b | False | single | True | None | None | None |
| secondary_colour_r | False | single | True | None | None | None |
| secondary_colour_g | False | double | True | None | None | None |
| secondary_colour_b | False | double | True | None | None | None |
| tertiary_colour_r | False | double | True | None | None | None |
| tertiary_colour_g | False | double | True | None | None | None |
| tertiary_colour_b | False | double | True | None | None | None |
  
## faction_variables_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction_variable_key | True | text | True | 20000 | None | None |
| value | False | text | True | 20000 | None | None |
| description | False | text | False | 20000 | None | None |
  
## faction_variables_optional_overrides_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction_variable_key | True | text | True | 20000 | [faction_variables_tables](#faction_variables_tables) | faction_variable_key |
| faction_key | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| campaign_key | True | text | False | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| difficulty_level | True | text | False | 255 | None | None |
| campaign_type | True | text | False | 20000 | None | None |
| value | False | text | True | 20000 | None | None |
  
## fame_levels_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| level | True | integer | True | None | None | None |
| player_prestige | False | integer | True | None | None | None |
| ai_prestige | False | integer | True | None | None | None |
| army_cap | False | integer | True | None | None | None |
| navy_cap | False | integer | True | None | None | None |
| champion_cap | False | integer | True | None | None | None |
| dignitary_cap | False | integer | True | None | None | None |
| spy_cap | False | integer | True | None | None | None |
| province_initiative_cap | False | integer | True | None | None | None |
| campaign | True | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| description_lookup | False | text | False | 255 | [campaign_localised_strings_tables](#campaign_localised_strings_tables) | key |
| effect_bundle | False | text | False | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
  
## family_relationship_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| relationship_type | True | text | True | 255 | None | None |
  
## famous_battle_pools_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| pool_id | True | integer | True | None | None | None |
| pool_posX | False | integer | True | None | None | None |
| pool_posY | False | integer | True | None | None | None |
| pool_radius | False | integer | True | None | None | None |
| battle_name | False | text | True | 50 | None | None |
  
## female_character_culture_details_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| culture | True | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| general | False | text | True | 255 | None | None |
| public_office | False | text | True | 255 | None | None |
| missions | False | text | True | 255 | None | None |
| chance_to_spawn | False | integer | True | None | None | None |
| trait | False | text | False | 255 | [trait_info_tables](#trait_info_tables) | trait |
  
## female_character_faction_details_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| general | False | text | False | 1 | None | None |
| public_office | False | text | False | 1 | None | None |
| missions | False | text | False | 1 | None | None |
| chance_to_spawn | False | integer | True | None | None | None |
| trait | False | text | False | 255 | [trait_info_tables](#trait_info_tables) | trait |
  
## female_character_subculture_details_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| subculture | True | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| general | False | text | False | 255 | None | None |
| public_office | False | text | False | 255 | None | None |
| missions | False | text | False | 255 | None | None |
| chance_to_spawn | False | integer | True | None | None | None |
| trait | False | text | False | 255 | [trait_info_tables](#trait_info_tables) | trait |
  
## first_person_engines_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [gun_types_enum_tables](#gun_types_enum_tables) | key |
| reload_time | False | single | True | None | None | None |
| auto_target | False | yesno | True | None | None | None |
| camera_offset_x | False | single | True | None | None | None |
| camera_offset_y | False | single | True | None | None | None |
| camera_offset_z | False | single | True | None | None | None |
| near_clipping_plane | False | single | True | None | None | None |
| track_projectile_distance | False | single | True | None | None | None |
| half_accuracy_arc | False | single | True | None | None | None |
| half_horizontal_fire_arc | False | single | True | None | None | None |
| half_vertical_fire_arc_elevation | False | single | True | None | None | None |
| turn_delay | False | single | True | None | None | None |
| half_vertical_fire_arc_declination | False | single | True | None | None | None |
  
## fonts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [font_names_tables](#font_names_tables) | font_name |
| size | True | integer | True | None | None | None |
| bold | True | yesno | True | None | None | None |
  
## font_names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| font_name | True | text | True | 255 | None | None |
  
## formations_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| formation | True | text | True | 255 | None | None |
| is_naval | False | yesno | True | None | None | None |
| is_army | False | yesno | True | None | None | None |
| name | False | text | False | 255 | None | None |
| tooltip | False | text | False | 255 | None | None |
| description | False | text | False | 255 | None | None |
| icon_name | False | text | True | 255 | None | None |
| order | False | integer | True | None | None | None |
  
## formations_to_subcultures_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| formation | True | text | True | 255 | [formations_tables](#formations_tables) | formation |
| sub_culture | True | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## forts_to_gun_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| gun_type | True | text | True | 50 | [gun_types_tables](#gun_types_tables) | gun_type |
  
## fort_underlay_climate_jcts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| fort_name | True | text | True | 50 | [battlefield_buildings_tables](#battlefield_buildings_tables) | key |
| climate | True | text | True | 50 | [climates_tables](#climates_tables) | climate_type |
| snow_underlay | True | yesno | True | None | None | None |
| underlay | False | text | True | 50 | [battle_terrain_farms_tables](#battle_terrain_farms_tables) | farm |
  
## frontend_faction_leaders_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| uniform | False | text | True | 2048 | None | None |
| animation | False | text | False | 2048 | None | None |
| x_offset | False | double | False | None | None | None |
| y_offset | False | double | False | None | None | None |
| party | True | text | True | 255 | [political_parties_tables](#political_parties_tables) | key |
  
## game_area_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## genders_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| gender | True | text | True | 50 | None | None |
| onscreen | False | text | True | 50 | None | None |
  
## general_command_star_level_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| command_star_level | True | integer | True | None | None | None |
| alive_morale_bonus | False | integer | True | None | None | None |
| nearby_morale_bonus | False | integer | True | None | None | None |
| melee_attack_bonus | False | integer | True | None | None | None |
| melee_defence_bonus | False | integer | True | None | None | None |
  
## government_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| government_type | True | text | True | 50 | None | None |
| onscreen | False | text | True | 50 | None | None |
| elected_ministers | False | yesno | True | None | None | None |
| hereditary_ministers | False | yesno | True | None | None | None |
| rank | False | integer | True | None | None | None |
| active_upper_class | False | text | True | 50 | [population_classes_tables](#population_classes_tables) | population_class |
| active_lower_class | False | text | True | 50 | [population_classes_tables](#population_classes_tables) | population_class |
  
## government_types_to_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| gov_type | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | integer | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## governorships_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| governorship | True | text | True | 50 | None | None |
| onscreen | False | text | True | 50 | None | None |
  
## ground_condition_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 50 | None | None |
  
## ground_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 50 | None | None |
| enum_value | False | integer | True | None | None | None |
| tooltip | False | text | False | 255 | None | None |
| standard_cursor | False | text | False | 255 | [cursors_tables](#cursors_tables) | key |
| selection_cursor | False | text | False | 255 | [cursors_tables](#cursors_tables) | key |
| penalty_immune_attribute | False | text | True | 255 | [unit_attributes_tables](#unit_attributes_tables) | key |
  
## ground_type_to_stat_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ground_type | True | text | True | 255 | [ground_types_tables](#ground_types_tables) | type |
| affected_stat | True | text | True | 255 | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| multiplier | False | double | True | None | None | None |
  
## groupings_military_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| military_group | True | text | True | 50 | None | None |
  
## gun_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| gun_type | True | text | True | 50 | None | None |
| battle_entity | False | text | True | 50 | [battle_entities_tables](#battle_entities_tables) | key |
| model | False | text | False | 50 | [warscape_animated_tables](#warscape_animated_tables) | key |
| gun_animations_table | False | text | True | 50 | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| equipment_table | False | text | False | 50 | None | None |
| destroyed_model | False | text | False | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| destruction_animation | False | text | False | 50 | [warscape_animated_tables](#warscape_animated_tables) | key |
| engine_type | False | text | False | 255 | [gun_types_enum_tables](#gun_types_enum_tables) | key |
| gun_mount_entity | False | text | False | 50 | [battle_entities_tables](#battle_entities_tables) | key |
  
## gun_types_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## gun_type_muzzle_flash_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## gun_type_to_projectiles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| gun_type | True | text | True | 50 | [gun_types_tables](#gun_types_tables) | gun_type |
| shot_type | True | text | True | 50 | [projectiles_tables](#projectiles_tables) | key |
| muzzle_flash | False | text | True | 50 | [gun_type_muzzle_flash_enum_tables](#gun_type_muzzle_flash_enum_tables) | key |
  
## historical_battles_ui_locations_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [battles_tables](#battles_tables) | key |
| x | False | integer | True | None | None | None |
| y | False | integer | True | None | None | None |
| height_percent | False | integer | True | None | None | None |
  
## historical_characters_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| on_screen_name | False | text | True | 255 | None | None |
| nobility | False | yesno | True | None | None | None |
| gender | False | text | True | 50 | [genders_tables](#genders_tables) | gender |
| agent_type | False | text | True | 255 | [agents_tables](#agents_tables) | key |
| faction | False | text | True | 255 | [factions_tables](#factions_tables) | key |
| spawning_window_start | False | integer | True | None | None | None |
| spawning_window_end | False | integer | True | None | None | None |
| spawn_conditions | False | text | True | 536870910 | None | None |
| name_key | False | integer | True | None | [names_tables](#names_tables) | id |
| surname_key | False | integer | False | None | [names_tables](#names_tables) | id |
| art_set_id | False | text | False | 255 | [campaign_character_art_sets_tables](#campaign_character_art_sets_tables) | art_set_id |
| clan_name_key | False | integer | False | None | [names_tables](#names_tables) | id |
| other_name_key | False | integer | False | None | [names_tables](#names_tables) | id |
| political_party | False | text | False | 255 | [political_parties_tables](#political_parties_tables) | key |
| age_start | False | integer | True | None | None | None |
  
## historical_character_traits_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| character | True | text | True | 50 | [historical_characters_tables](#historical_characters_tables) | key |
| trait | True | text | True | 50 | [character_trait_levels_tables](#character_trait_levels_tables) | key |
  
## honour_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 1024 | None | None |
| factor | False | text | True | 1024 | [honour_factors_tables](#honour_factors_tables) | key |
| value | False | integer | True | None | None | None |
| applies_to_ai | False | yesno | True | None | None | None |
  
## honour_factors_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 1024 | None | None |
| minimum_value | False | integer | True | None | None | None |
| maximum_value | False | integer | True | None | None | None |
| localised_negative_name | False | text | True | 1024 | None | None |
| localised_positive_name | False | text | True | 1024 | None | None |
  
## imposter_sharing_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 2048 | None | None |
  
## incidents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| ui_image | False | text | True | 255 | None | None |
| ui_icon | False | text | True | 255 | None | None |
| generate | False | yesno | True | None | None | None |
| prioritised | False | yesno | True | None | None | None |
| localised_title | False | text | True | 20000 | None | None |
| localised_description | False | text | True | 200000 | None | None |
  
## land_units_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| onscreen_name | False | text | True | 20000 | None | None |
| category | False | text | True | 50 | [unit_category_tables](#unit_category_tables) | key |
| class | False | text | True | 50 | [unit_class_tables](#unit_class_tables) | key |
| short_description_text | False | text | True | 255 | [unit_description_short_texts_tables](#unit_description_short_texts_tables) | key |
| historical_description_text | False | text | True | 255 | [unit_description_historical_texts_tables](#unit_description_historical_texts_tables) | key |
| strengths_weaknesses_text | False | text | True | 255 | [unit_description_strengths_weaknesses_texts_tables](#unit_description_strengths_weaknesses_texts_tables) | key |
| campaign_action_points | False | integer | True | None | None | None |
| supports_first_person | False | yesno | True | None | None | None |
| man_entity | False | text | True | 50 | [battle_entities_tables](#battle_entities_tables) | key |
| man_animation | False | text | False | 50 | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| num_mounts | False | integer | True | None | None | None |
| mount | False | text | False | 50 | [mounts_tables](#mounts_tables) | key |
| num_animals | False | integer | True | None | None | None |
| animal | False | text | False | 255 | [animals_tables](#animals_tables) | key |
| spacing | False | text | True | 255 | [unit_spacings_tables](#unit_spacings_tables) | key |
| rank_depth | False | integer | True | None | None | None |
| morale | False | integer | True | None | None | None |
| bonus_hit_points | False | integer | True | None | None | None |
| training_level | False | text | True | 50 | [unit_training_level_enum_tables](#unit_training_level_enum_tables) | key |
| armour | False | text | True | 255 | [unit_armour_types_tables](#unit_armour_types_tables) | key |
| shield | False | text | True | 255 | [unit_shield_types_tables](#unit_shield_types_tables) | key |
| primary_missile_weapon | False | text | False | 255 | [missile_weapons_tables](#missile_weapons_tables) | key |
| accuracy | False | integer | True | None | None | None |
| ammo | False | integer | True | None | None | None |
| primary_melee_weapon | False | text | True | 255 | [melee_weapons_tables](#melee_weapons_tables) | key |
| melee_attack | False | integer | True | None | None | None |
| charge_bonus | False | integer | True | None | None | None |
| melee_defence | False | integer | True | None | None | None |
| dismounted_melee_attack | False | integer | True | None | None | None |
| dismounted_charge_bonus | False | integer | True | None | None | None |
| dismounted_melee_defence | False | integer | True | None | None | None |
| num_guns | False | integer | True | None | None | None |
| officers | False | text | True | 255 | [land_units_officers_tables](#land_units_officers_tables) | key |
| engine | False | text | False | 255 | [battlefield_engines_tables](#battlefield_engines_tables) | key |
| articulated_record | False | text | False | 255 | [land_unit_articulated_vehicles_tables](#land_unit_articulated_vehicles_tables) | key |
| is_male | False | yesno | True | None | None | None |
| visibility_spotting_range_min | False | single | True | None | None | None |
| visibility_spotting_range_max | False | single | True | None | None | None |
| ability_global_recharge | False | double | True | None | None | None |
| attribute_group | False | text | False | 255 | [unit_attributes_groups_tables](#unit_attributes_groups_tables) | group_name |
| spot_dist_tree | False | double | True | None | None | None |
| spot_dist_scrub | False | double | True | None | None | None |
| chariot | False | text | False | 255 | [battlefield_chariots_tables](#battlefield_chariots_tables) | key |
| num_chariots | False | integer | True | None | None | None |
| reload | False | integer | True | None | None | None |
| loose_spacing | False | yesno | True | None | None | None |
| spotting_and_hiding | False | text | False | 255 | [spotting_and_hiding_values_tables](#spotting_and_hiding_values_tables) | key |
| selection_vo | False | text | True | 255 | [audio_vo_selected_switches_tables](#audio_vo_selected_switches_tables) | key |
| selected_vo_secondary | False | text | True | 255 | [audio_vo_selected_switches_tables](#audio_vo_selected_switches_tables) | key |
| selected_vo_tertiary | False | text | True | 255 | [audio_vo_selected_switches_tables](#audio_vo_selected_switches_tables) | key |
| hiding_scalar | False | double | True | None | None | None |
  
## land_units_officers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| officer_1 | False | text | False | 50 | [battle_personalities_tables](#battle_personalities_tables) | key |
| officer_2 | False | text | False | 50 | [battle_personalities_tables](#battle_personalities_tables) | key |
| standard_bearer_1 | False | text | False | 50 | [battle_personalities_tables](#battle_personalities_tables) | key |
| standard_bearer_2 | False | text | False | 50 | [battle_personalities_tables](#battle_personalities_tables) | key |
| musician_1 | False | text | False | 50 | [battle_personalities_tables](#battle_personalities_tables) | key |
| musician_2 | False | text | False | 50 | [battle_personalities_tables](#battle_personalities_tables) | key |
| personality_location | False | text | False | 255 | [personality_location_enums_tables](#personality_location_enums_tables) | key |
  
## land_units_to_unit_abilites_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| land_unit | True | text | True | 255 | [land_units_tables](#land_units_tables) | key |
| ability | True | text | True | 50 | [unit_abilities_tables](#unit_abilities_tables) | key |
  
## land_unit_articulated_vehicles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| articulated_entity | False | text | False | 50 | [battle_entities_tables](#battle_entities_tables) | key |
| ammo_caisson_entity | False | text | False | 50 | [battle_entities_tables](#battle_entities_tables) | key |
| ammo_caisson_model | False | text | False | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
| ammo_caisson_destroyed_model | False | text | False | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| ammo_caisson_destruction | False | text | True | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
  
## languages_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| full_name | False | text | True | 255 | None | None |
  
## lighting_setups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name | True | text | True | 50 | None | None |
| depth_bias | False | double | True | None | None | None |
| dirx | False | double | True | None | None | None |
| diry | False | double | True | None | None | None |
| dirz | False | double | True | None | None | None |
| colour_scale | False | double | True | None | None | None |
| colour_r | False | double | True | None | None | None |
| colour_g | False | double | True | None | None | None |
| colour_b | False | double | True | None | None | None |
| colour_top_r | False | double | True | None | None | None |
| colour_top_g | False | double | True | None | None | None |
| colour_top_b | False | double | True | None | None | None |
| colour_bottom_r | False | double | True | None | None | None |
| colour_bottom_g | False | double | True | None | None | None |
| colour_bottom_b | False | double | True | None | None | None |
| gamma | False | double | True | None | None | None |
| bloom_multiplier | False | double | True | None | None | None |
| bloom_angle_1 | False | double | True | None | None | None |
| bloom_angle_2 | False | double | True | None | None | None |
| bloom_scale_1 | False | double | True | None | None | None |
| bloom_scale_2 | False | double | True | None | None | None |
| main_bloom_scalex | False | double | True | None | None | None |
| main_bloom_scaley | False | double | True | None | None | None |
| main_bloom_distribution | False | double | True | None | None | None |
| high_pass | False | double | False | None | None | None |
| colour_fog_r | False | double | True | None | None | None |
| colour_fog_g | False | double | True | None | None | None |
| colour_fog_b | False | double | True | None | None | None |
| fog_near | False | double | True | None | None | None |
| fog_far | False | double | True | None | None | None |
| fog_density | False | double | True | None | None | None |
  
## loyalty_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 1024 | None | None |
| factor | False | text | True | 1024 | [loyalty_factors_tables](#loyalty_factors_tables) | key |
| value | False | integer | True | None | None | None |
| applies_to_ai | False | yesno | True | None | None | None |
  
## loyalty_factors_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 1024 | None | None |
| minimum_value | False | integer | True | None | None | None |
| maximum_value | False | integer | True | None | None | None |
| localised_negative_name | False | text | True | 1024 | None | None |
| localised_positive_name | False | text | True | 1024 | None | None |
  
## main_units_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit | True | text | True | 255 | None | None |
| land_unit | False | text | True | 255 | [land_units_tables](#land_units_tables) | key |
| num_men | False | integer | True | None | None | None |
| naval_unit | False | text | False | 255 | [naval_units_tables](#naval_units_tables) | key |
| num_ships | False | integer | True | None | None | None |
| min_men_per_ship | False | integer | True | None | None | None |
| max_men_per_ship | False | integer | True | None | None | None |
| is_naval | False | yesno | True | None | None | None |
| weight | False | text | False | 255 | [unit_weights_tables](#unit_weights_tables) | key |
| recruitment_cost | False | integer | True | None | None | None |
| upkeep_cost | False | integer | True | None | None | None |
| create_time | False | integer | True | None | None | None |
| campaign_cap | False | integer | True | None | None | None |
| multiplayer_cost | False | integer | True | None | None | None |
| multiplayer_cap | False | integer | True | None | None | None |
| caste | False | text | True | 255 | [unit_castes_tables](#unit_castes_tables) | caste |
| prestige | False | integer | True | None | None | None |
| additional_building_requirement | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| religion_requirement | False | text | False | 50 | [religions_tables](#religions_tables) | religion_key |
| recruitment_movie | False | text | False | 255 | None | None |
| campaign_total_cap | False | integer | True | None | None | None |
| resource_requirement | False | text | False | 50 | [resources_tables](#resources_tables) | key |
| world_leader_only | False | yesno | True | None | None | None |
| can_trade | False | yesno | True | None | None | None |
| special_edition_mask | False | integer | True | None | None | None |
| unique_index | False | autonumber | True | None | None | None |
| in_encyclopedia | False | yesno | True | None | None | None |
| region_unit_resource_requirement | False | text | False | 255 | [region_unit_resources_tables](#region_unit_resources_tables) | key |
| audio_language | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| audio_vo_actor_group | False | text | False | 255 | [audio_vo_actor_groups_tables](#audio_vo_actor_groups_tables) | key |
  
## marriage_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## melee_weapons_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| damage | False | integer | True | None | None | None |
| ap_damage | False | integer | True | None | None | None |
| first_strike | False | integer | True | None | None | None |
| bonus_v_infantry | False | integer | True | None | None | None |
| bonus_v_cavalry | False | integer | True | None | None | None |
| bonus_v_elephants | False | integer | True | None | None | None |
| armour_piercing | False | yesno | True | None | None | None |
| shield_piercing | False | yesno | True | None | None | None |
| armour_penetrating | False | yesno | True | None | None | None |
| weapon_length | False | decimal | True | None | None | None |
| melee_weapon_type | False | text | True | 50 | [unit_melee_weapons_enum_tables](#unit_melee_weapons_enum_tables) | key |
| audio_material | False | text | True | 255 | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
  
## mercenary_pools_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## mercenary_pool_modifiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| pool_type | False | text | True | 20000 | [mercenary_pool_type_enums_tables](#mercenary_pool_type_enums_tables) | pool_type |
| culture_origin_match | False | yesno | True | None | None | None |
| min_pool_culture_percentage | False | integer | True | None | None | None |
| replenishment_modifier | False | single | True | None | None | None |
| cost_modifier | False | single | True | None | None | None |
| key | True | autonumber | True | None | None | None |
  
## mercenary_pool_to_groups_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| pool | False | text | True | 255 | [mercenary_pools_tables](#mercenary_pools_tables) | key |
| group | False | text | True | 20000 | [mercenary_unit_groups_tables](#mercenary_unit_groups_tables) | key |
| initial_unit_count | False | integer | True | None | None | None |
| faction_requirement | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| subculture_requirement | False | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| tech_requirement | False | text | False | 255 | [technologies_tables](#technologies_tables) | key |
  
## mercenary_pool_type_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| pool_type | True | text | True | 20000 | None | None |
  
## mercenary_unit_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 20000 | None | None |
| unit_record | False | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| max_count | False | integer | True | None | None | None |
| max_replenish_per_turn | False | integer | True | None | None | None |
| chance_to_replenish | False | single | True | None | None | None |
  
## message_events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| event | True | text | True | 255 | None | None |
| layout | False | text | True | 255 | [message_event_layout_types_tables](#message_event_layout_types_tables) | Type |
| requires_response | False | yesno | True | None | None | None |
| instant_open | False | yesno | True | None | None | None |
| priority | False | integer | True | None | None | None |
  
## message_event_layout_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| Type | True | text | False | 255 | None | None |
  
## message_event_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| event | True | text | True | 255 | [message_events_tables](#message_events_tables) | event |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| title | False | text | True | 50 | None | None |
| text | False | text | True | 50 | [message_event_text_tables](#message_event_text_tables) | key |
| image | False | text | False | 200 | None | None |
| icon | False | text | False | 255 | None | None |
| sound_event | False | text | False | 255 | None | None |
| optional_campaign_key | True | text | False | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| optional_subculture | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## message_event_text_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| text | False | text | True | 536870910 | None | None |
  
## military_force_legacy_emblems_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| is_army | False | yesno | True | None | None | None |
| faction_key | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| culure_key | False | text | False | 255 | [cultures_tables](#cultures_tables) | key |
| subculture_key | False | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| icon | False | text | True | 255 | None | None |
| banner_decorator | False | text | True | 255 | None | None |
  
## military_force_legacy_names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| subculture | True | text | False | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| localised_name | False | text | True | 255 | None | None |
| for_army | False | yesno | True | None | None | None |
| campaign | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## ministerial_effectiveness_modifiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| leader_minister_level | True | integer | True | None | None | None |
| government_type | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| effectiveness_bonus | False | integer | True | None | None | None |
  
## ministerial_positions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| minister_key | True | text | True | 50 | None | None |
| rank | False | integer | True | None | None | None |
  
## ministerial_positions_by_gov_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction | True | text | True | 50 | [factions_tables](#factions_tables) | key |
| minister_key | True | text | True | 50 | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| government_type | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| gender | True | text | True | 50 | [genders_tables](#genders_tables) | gender |
| string | False | text | False | 50 | [ministerial_positions_strings_tables](#ministerial_positions_strings_tables) | key |
| loyalty_gained | False | integer | True | None | None | None |
| loyalty_on_loss | False | integer | True | None | None | None |
  
## ministerial_positions_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 255 | None | None |
| on_screen | False | text | False | 255 | None | None |
  
## ministerial_positions_switching_loyalty_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| position_from | True | text | True | 50 | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| position_to | True | text | True | 50 | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| loyalty_gained | False | integer | True | None | None | None |
  
## ministerial_positions_to_character_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| position | True | text | True | 50 | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| minister_level | True | integer | True | None | None | None |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | integer | True | None | None | None |
| ui_id | False | integer | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## ministerial_positions_to_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| position | True | text | True | 50 | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| minister_level | True | integer | True | None | None | None |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | integer | True | None | None | None |
| ui_id | False | integer | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## ministerial_positions_to_governorships_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ministerial_position | True | text | True | 50 | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| governorship | True | text | True | 50 | [governorships_tables](#governorships_tables) | governorship |
  
## ministerial_position_default_names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ministerial_position | True | text | True | 50 | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| gov_type | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| default_name | False | text | True | 50 | None | None |
  
## missile_weapons_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| precursor | False | yesno | True | None | None | None |
| default_projectile | False | text | True | 255 | [projectiles_tables](#projectiles_tables) | key |
| can_fire_at_buildings | False | yesno | True | None | None | None |
  
## missile_weapons_to_projectiles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| missile_weapon | True | text | True | 255 | [missile_weapons_tables](#missile_weapons_tables) | key |
| projectile | True | text | True | 255 | [projectiles_tables](#projectiles_tables) | key |
  
## missions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| mission_type | False | text | True | 255 | None | None |
| localised_title | False | text | True | 255 | None | None |
| localised_description | False | text | True | 65535 | None | None |
| ui_image | False | text | True | 255 | None | None |
| ui_icon | False | text | True | 255 | None | None |
| generate | False | yesno | True | None | None | None |
| prioritised | False | yesno | True | None | None | None |
  
## mission_issuers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| issuer_key | True | text | True | 255 | None | None |
  
## mission_text_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 50 | None | None |
| text | False | text | False | 536870910 | None | None |
  
## mission_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## models_artillery_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| model_file | False | text | True | 255 | None | None |
| logic_file | False | text | True | 255 | None | None |
  
## models_building_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| model_file | False | text | True | 255 | None | None |
| logic_file | False | text | True | 255 | None | None |
| display_path | False | text | False | 20000 | None | None |
  
## models_deployables_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| model_file | False | text | True | 255 | None | None |
| logic_file | False | text | True | 255 | None | None |
| display_path | False | text | False | 20000 | None | None |
  
## models_entity_weapons_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| model_file | False | text | True | 255 | None | None |
| logic_file | False | text | True | 255 | None | None |
  
## models_foot_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## models_mount_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## models_naval_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| logic_folder | False | text | False | 255 | None | None |
| rigging_file | False | text | False | 255 | None | None |
| destruction_file | False | text | False | 255 | None | None |
| display_folder | False | text | True | 255 | None | None |
| oar_upper | False | text | True | 255 | [models_oars_tables](#models_oars_tables) | key |
| oar_middle | False | text | True | 255 | [models_oars_tables](#models_oars_tables) | key |
| oar_lower | False | text | True | 255 | [models_oars_tables](#models_oars_tables) | key |
| selection_indicator_shape | False | text | True | 255 | None | None |
  
## models_oars_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| rigid_model | False | text | False | 255 | None | None |
| left_row | False | text | False | 255 | None | None |
| left_end | False | text | False | 255 | None | None |
| right_row | False | text | False | 255 | None | None |
| right_end | False | text | False | 255 | None | None |
  
## models_sieges_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| model_file | False | text | True | 255 | None | None |
| logic_file | False | text | True | 255 | None | None |
| display_path | False | text | False | 20000 | None | None |
  
## mountable_artillery_units_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
  
## mountable_artillery_units_custom_battles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| mountable_artillery | True | text | True | 255 | [mountable_artillery_units_tables](#mountable_artillery_units_tables) | unit_key |
| cap | False | integer | True | None | None | None |
| probability | False | integer | True | None | None | None |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## mounts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| animation | False | text | True | 50 | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| entity | False | text | True | 50 | [battle_entities_tables](#battle_entities_tables) | key |
| mount_armour | False | integer | True | None | None | None |
| variant | False | text | True | 255 | [variants_tables](#variants_tables) | variant_name |
| audio_armour_type | False | text | True | 255 | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
  
## mount_variants_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| mount_key | False | text | True | 50 | [mounts_tables](#mounts_tables) | key |
| display_key | False | text | True | 255 | None | None |
| weight | False | double | True | None | None | None |
  
## movement_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 50 | None | None |
  
## movie_event_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| event | True | text | True | 50 | None | None |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| title | False | text | False | 255 | None | None |
| movie | False | text | True | 50 | None | None |
| id | False | autonumber | False | None | None | None |
  
## mp_budgets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| budget_size_key | False | text | True | 255 | [mp_budget_sizes_tables](#mp_budget_sizes_tables) | key |
| land | False | yesno | True | None | None | None |
| siege_defender | False | yesno | True | None | None | None |
| budget | False | integer | True | None | None | None |
  
## mp_budget_sizes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## mp_force_gen_templates_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## mp_force_gen_template_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| template_key | True | text | True | 255 | [mp_force_gen_templates_tables](#mp_force_gen_templates_tables) | key |
| budget_key | True | text | True | 255 | [mp_budgets_tables](#mp_budgets_tables) | key |
| priority | False | integer | True | None | None | None |
| general_pct | False | single | True | None | None | None |
| units_pct | False | single | True | None | None | None |
| upgrade_pct | False | single | True | None | None | None |
| config_key | False | text | True | 255 | [cdir_military_generator_configs_tables](#cdir_military_generator_configs_tables) | key |
| is_defender | True | yesno | True | None | None | None |
  
## multiplayer_mininum_length_funds_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| value | False | double | True | None | None | None |
| description | False | text | True | 255 | None | None |
  
## names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| names_group | False | integer | True | None | [names_groups_tables](#names_groups_tables) | key |
| name | False | text | True | 50 | None | None |
| type | False | text | True | 50 | [name_types_tables](#name_types_tables) | key |
| gender | False | text | True | 255 | [genders_tables](#genders_tables) | gender |
| frequency | False | integer | True | None | None | None |
| nobility | False | yesno | True | None | None | None |
| id | True | autonumber | True | None | None | None |
  
## names_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ID | False | text | True | 50 | None | None |
| Description | False | text | True | 50 | None | None |
| key | True | autonumber | True | None | None | None |
  
## names_titles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name_group | True | integer | True | None | [names_groups_tables](#names_groups_tables) | key |
| title | True | text | True | 50 | None | None |
| gender | False | text | True | 50 | [genders_tables](#genders_tables) | gender |
| rank | False | integer | True | None | None | None |
  
## names_titles_by_agent_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| agent_type | True | text | True | 50 | [agents_tables](#agents_tables) | key |
| highest_title | False | integer | True | None | None | None |
  
## name_orders_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 50 | [name_types_tables](#name_types_tables) | key |
| order | True | integer | True | None | None | None |
| name_group | True | integer | True | None | [names_groups_tables](#names_groups_tables) | key |
  
## name_order_overrides_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 50 | [name_types_tables](#name_types_tables) | key |
| order | True | integer | True | None | None | None |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## name_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## naval_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| effect_name | False | text | False | 255 | [particle_effects_tables](#particle_effects_tables) | key |
  
## naval_fire_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| incendiary_level | True | text | True | 255 | [projectile_incendiary_enum_tables](#projectile_incendiary_enum_tables) | key |
| unit_category | True | text | True | 255 | [unit_category_tables](#unit_category_tables) | key |
| chance_of_fire | False | decimal | True | None | None | None |
  
## naval_oar_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## naval_ramming_events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| ramming_ship | False | text | True | 255 | [unit_category_tables](#unit_category_tables) | key |
| rammed_ship | False | text | True | 255 | [unit_category_tables](#unit_category_tables) | key |
| base_damage | False | integer | True | None | None | None |
  
## naval_units_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| onscreen_name | False | text | True | 20000 | None | None |
| category | False | text | True | 50 | [unit_category_tables](#unit_category_tables) | key |
| class | False | text | True | 50 | [unit_class_tables](#unit_class_tables) | key |
| short_description_text | False | text | True | 255 | [unit_description_short_texts_tables](#unit_description_short_texts_tables) | key |
| historical_description_text | False | text | True | 255 | [unit_description_historical_texts_tables](#unit_description_historical_texts_tables) | key |
| strengths_weaknesses_text | False | text | True | 255 | [unit_description_strengths_weaknesses_texts_tables](#unit_description_strengths_weaknesses_texts_tables) | key |
| campaign_action_points | False | integer | True | None | None | None |
| unit_type_icon | False | text | False | 255 | None | None |
| supports_first_person | False | yesno | True | None | None | None |
| ship | False | text | True | 255 | [ship_dbs_tables](#ship_dbs_tables) | key |
| primary_naval_weapon | False | text | False | 255 | [naval_weapons_tables](#naval_weapons_tables) | key |
| secondary_naval_weapon | False | text | False | 255 | [naval_weapons_tables](#naval_weapons_tables) | key |
| rank_depth | False | integer | True | None | None | None |
| attribute_groups | False | text | False | 255 | [unit_attributes_groups_tables](#unit_attributes_groups_tables) | group_name |
| can_board | False | yesno | True | None | None | None |
| can_ram | False | yesno | True | None | None | None |
| unit_card | False | text | True | 255 | None | None |
| is_composite | False | yesno | True | None | None | None |
| ignition_threshold | False | integer | True | None | None | None |
  
## naval_units_to_unit_abilites_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| naval_unit | True | text | True | 255 | [naval_units_tables](#naval_units_tables) | key |
| ability | True | text | True | 50 | [unit_abilities_tables](#unit_abilities_tables) | key |
  
## naval_weapons_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| type | False | text | True | 255 | [naval_weapons_enums_tables](#naval_weapons_enums_tables) | types |
| autonomous_engine | False | text | False | 255 | [battlefield_engines_autonomous_tables](#battlefield_engines_autonomous_tables) | key |
| models_entity_weaponry | False | text | False | 255 | [models_entity_weapons_tables](#models_entity_weapons_tables) | key |
  
## naval_weapons_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| types | True | text | True | 255 | None | None |
  
## particle_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## pdlc_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ID | True | text | True | 255 | None | None |
| SteamID | False | integer | True | None | None | None |
| description | False | text | False | 536870910 | None | None |
| release_order | False | integer | True | None | None | None |
  
## personality_location_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## plagues_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name | True | text | True | 255 | None | None |
| grade | False | integer | True | None | None | None |
| minimum_squalor | False | integer | True | None | None | None |
| infectivity | False | integer | True | None | None | None |
| lifetime | False | integer | True | None | None | None |
| region_effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| military_force_effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
  
## plagues_permitted_campaigns_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| plague | True | text | True | 255 | [plagues_tables](#plagues_tables) | name |
| campaign | True | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## political_actions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| political_action_key | True | text | True | 255 | None | None |
| onscreen_name | False | text | True | 255 | None | None |
| icon_file_path | False | text | False | 255 | None | None |
| usage_cost_multiplier | False | double | True | None | None | None |
  
## political_actions_dilemma_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| politiical_action | True | text | True | 255 | [political_actions_tables](#political_actions_tables) | political_action_key |
| dilemma | True | text | True | 255 | [dilemmas_tables](#dilemmas_tables) | key |
| weighting | True | integer | True | None | None | None |
  
## political_actions_effect_bundles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| action | True | text | True | 255 | None | None |
| effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| duration | False | integer | True | None | None | None |
  
## political_actions_incidents_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| political_action | True | text | True | 255 | [political_actions_tables](#political_actions_tables) | political_action_key |
| incident | True | text | True | 255 | [incidents_tables](#incidents_tables) | key |
| weighting | True | integer | True | None | None | None |
  
## political_actions_mission_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| political_action | True | text | True | 255 | [political_actions_tables](#political_actions_tables) | political_action_key |
| mission | True | text | True | 255 | [missions_tables](#missions_tables) | key |
| weighting | True | integer | True | None | None | None |
  
## political_parties_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| name_localised | False | text | True | 255 | None | None |
| playable | False | yesno | True | None | None | None |
| associated_surname | False | text | False | 255 | None | None |
| ui_icon | False | text | True | 255 | None | None |
| effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| description_localised | False | text | True | 255 | None | None |
| initial_power | False | integer | True | None | None | None |
| r | False | double | True | None | None | None |
| g | False | double | True | None | None | None |
| b | False | double | True | None | None | None |
| trait1 | False | text | False | 255 | [political_traits_tables](#political_traits_tables) | key |
| trait2 | False | text | False | 255 | [political_traits_tables](#political_traits_tables) | key |
  
## political_parties_loyalty_effect_bundles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| loyalty | True | integer | True | None | None | None |
| bundle_key | True | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
  
## political_parties_power_effect_bundles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| political_party_key | True | text | True | 255 | [political_parties_tables](#political_parties_tables) | key |
| effect_bundle | True | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| power_level | False | integer | True | None | None | None |
  
## political_traits_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| onscreen_name | False | text | True | 255 | None | None |
| description | False | text | False | 255 | None | None |
  
## political_triggers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| trigger | True | text | True | 50 | None | None |
| event | False | text | True | 50 | [trigger_events_tables](#trigger_events_tables) | event |
| conditions | False | text | True | 536870910 | None | None |
  
## politics_government_actions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## politics_government_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| government_type | True | text | True | 255 | None | None |
  
## politics_government_type_political_action_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| government_type | True | text | True | 255 | [politics_government_types_tables](#politics_government_types_tables) | government_type |
| political_action | True | text | True | 255 | [political_actions_tables](#political_actions_tables) | political_action_key |
| is_available_for_faction_leader | False | yesno | True | None | None | None |
| is_available_for_non_ruling_party_leaders | False | yesno | True | None | None | None |
| is_available_for_ruling_party_members | False | yesno | True | None | None | None |
| is_available_for_non_ruling_party_members | False | yesno | True | None | None | None |
  
## population_classes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| population_class | True | text | True | 50 | None | None |
| riots | False | yesno | True | None | None | None |
| demands | False | yesno | True | None | None | None |
| spawn_rebel_general | False | yesno | True | None | None | None |
| onscreen_name | False | text | False | 50 | None | None |
  
## portrait_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## preset_colours_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| Key | True | text | True | 255 | None | None |
| red | False | double | True | None | None | None |
| green | False | double | True | None | None | None |
| blue | False | double | True | None | None | None |
  
## pre_battle_speeches_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| text | False | text | True | 536870910 | None | None |
| type | False | integer | True | None | [pre_battle_speech_types_enum_tables](#pre_battle_speech_types_enum_tables) | index |
| parameter | False | text | True | 255 | [pre_battle_speech_parameters_enum_tables](#pre_battle_speech_parameters_enum_tables) | key |
  
## pre_battle_speech_parameters_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## pre_battle_speech_types_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| index | True | integer | True | None | None | None |
| description | False | text | True | 255 | None | None |
  
## projectiles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| category | False | text | True | 50 | [projectile_category_enum_tables](#projectile_category_enum_tables) | key |
| shot_type | False | text | True | 50 | [projectile_shot_type_enum_tables](#projectile_shot_type_enum_tables) | key |
| explosion_type | False | text | False | 50 | [projectiles_explosions_tables](#projectiles_explosions_tables) | key |
| high_air_resistance | False | yesno | False | None | None | None |
| spin_type | False | text | True | 50 | None | None |
| projectile_number | False | integer | False | None | None | None |
| trajectory_sight | False | text | True | 50 | [projectile_trajectory_sight_enum_tables](#projectile_trajectory_sight_enum_tables) | key |
| effective_range | False | integer | True | None | None | None |
| minimum_range | False | integer | True | None | None | None |
| max_elevation | False | integer | True | None | None | None |
| muzzle_velocity | False | single | True | None | None | None |
| marksmanship_bonus | False | integer | True | None | None | None |
| spread | False | double | True | None | None | None |
| damage | False | integer | True | None | None | None |
| ap_damage | False | integer | True | None | None | None |
| penetration | False | text | False | 255 | [projectile_penetration_enum_tables](#projectile_penetration_enum_tables) | key |
| incendiary | False | text | False | 255 | [projectile_incendiary_enum_tables](#projectile_incendiary_enum_tables) | key |
| can_bounce | False | yesno | True | None | None | None |
| collision_radius | False | double | True | None | None | None |
| base_reload_time | False | integer | True | None | None | None |
| below_waterline_damage_modifer | False | single | True | None | None | None |
| calibration_distance | False | single | True | None | None | None |
| calibration_area | False | single | True | None | None | None |
| bonus_v_infantry | False | integer | True | None | None | None |
| bonus_v_cavalry | False | integer | True | None | None | None |
| bonus_v_elephant | False | integer | True | None | None | None |
| projectile_display | False | text | False | 255 | [projectile_displays_tables](#projectile_displays_tables) | key |
| overhead_stat_effect | False | text | False | 255 | [special_ability_phases_tables](#special_ability_phases_tables) | id |
| contact_stat_effect | False | text | False | 255 | [special_ability_phases_tables](#special_ability_phases_tables) | id |
| projectile_audio | False | text | True | 255 | [audio_projectiles_tables](#audio_projectiles_tables) | key |
| shockwave_radius | False | single | True | None | None | None |
| can_damage_buildings | False | yesno | True | None | None | None |
| is_grapple | False | yesno | True | None | None | None |
  
## projectiles_detonation_types_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## projectiles_detonator_types_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| detonator_type | True | text | True | 50 | None | None |
  
## projectiles_explosions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| detonator_type | False | text | True | 50 | [projectiles_detonator_types_enum_tables](#projectiles_detonator_types_enum_tables) | detonator_type |
| detonation_type | False | text | True | 50 | [projectiles_detonation_types_enum_tables](#projectiles_detonation_types_enum_tables) | key |
| detonation_radius | False | integer | True | None | None | None |
| detonation_duration | False | single | True | None | None | None |
| detonation_speed | False | integer | True | None | None | None |
| detonation_damage | False | single | True | None | None | None |
| projectile_name | False | text | False | 50 | [projectiles_tables](#projectiles_tables) | key |
| projectile_amount | False | integer | True | None | None | None |
| explosion_particle_effect | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| distance_from_target | False | integer | True | None | None | None |
| error_margin | False | double | True | None | None | None |
| non_lethal_detonation | False | yesno | False | None | None | None |
| explosion_particle_effect_on_ground | False | text | False | 50 | None | None |
| audio_explosion_type | False | text | True | 255 | [audio_explosions_enums_tables](#audio_explosions_enums_tables) | key |
  
## projectiles_spin_type_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## projectile_category_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## projectile_displays_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| display_model | False | text | False | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| damaged_display_model | False | text | False | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| launch_fx | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| trail_fx | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| stationary_fx | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| impact | False | text | False | 50 | [projectile_impacts_tables](#projectile_impacts_tables) | key |
| skeleton | False | text | False | 255 | None | None |
| airborne_anim | False | text | False | 255 | None | None |
| landing_anim | False | text | False | 255 | None | None |
  
## projectile_gun_types_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| gun_type | True | text | True | 50 | None | None |
  
## projectile_impacts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| water | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| sails | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| mud | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| grass | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| road | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| rock | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| sand | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| cloth | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| snow | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| leather | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| wood | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| foliage | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| glass | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| size | False | text | True | 50 | None | None |
| blood | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
| metal | False | text | False | 50 | [particle_effects_tables](#particle_effects_tables) | key |
  
## projectile_incendiary_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## projectile_penetration_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## projectile_shot_type_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| requires_effect_enabling | False | yesno | False | None | None | None |
| supersedes_shot_type | False | text | False | 255 | None | None |
| button_tooltip_text | False | text | True | 20000 | None | None |
  
## projectile_trajectory_sight_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## prologue_chapters_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| number | True | integer | True | None | None | None |
| title | False | text | True | 255 | None | None |
| description | False | text | False | 1000 | None | None |
| is_battle | False | yesno | True | None | None | None |
| battle_key | False | text | False | 255 | [battles_tables](#battles_tables) | key |
| campaign_key | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| subtitle | False | text | False | 255 | None | None |
| banner | False | text | False | 255 | None | None |
  
## prologue_loading_screens_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| index | True | autonumber | True | None | None | None |
| title | False | text | True | 255 | None | None |
| main_text | False | text | True | 1000 | None | None |
| inset_image | False | text | True | 255 | None | None |
| background_image | False | text | True | 255 | None | None |
| pane_on_left | False | yesno | True | None | None | None |
| campaign | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## provinces_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| onscreen | False | text | True | 20000 | None | None |
  
## province_to_mercenary_set_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| province | True | text | True | 255 | [provinces_tables](#provinces_tables) | key |
| mercenary_set | True | text | True | 255 | [mercenary_pools_tables](#mercenary_pools_tables) | key |
| optional_campaign_key | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## provincial_initiatives_to_subculture_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| provincial_initiative_key | True | text | True | 255 | [provincial_initiative_records_tables](#provincial_initiative_records_tables) | key |
| subculture | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## provincial_initiative_records_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| localised_name | False | text | True | 255 | None | None |
| effect_bundle | False | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| order | False | integer | True | None | None | None |
| icon_path | False | text | True | 255 | None | None |
| campaign_vfx_id | False | text | False | 255 | [campaign_vfx_campaign_vfx_event_ids_tables](#campaign_vfx_campaign_vfx_event_ids_tables) | campaign_vfx_event |
  
## public_order_factors_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| factor | True | text | True | 50 | None | None |
| positive_pip_path | False | text | True | 100 | None | None |
| positive_tooltip | False | text | True | 536870910 | None | None |
| negative_pip_path | False | text | False | 200 | None | None |
| negative_tooltip | False | text | False | 536870910 | None | None |
| optional_campaign_key | False | text | False | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## quotes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| quote_onscreen | False | text | True | 536870910 | None | None |
| quote_person | False | text | False | 50 | [quotes_people_tables](#quotes_people_tables) | quote_person_key |
| key | True | autonumber | False | None | None | None |
  
## quotes_people_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| quote_person_key | True | text | False | 50 | None | None |
| quote_person_onscreen | False | text | True | 536870910 | None | None |
  
## random_localisation_strings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| string | False | text | True | 536870910 | None | None |
  
## regions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| onscreen | False | text | True | 255 | None | None |
| palette_entry | False | integer | True | None | None | None |
| r | False | integer | True | None | None | None |
| g | False | integer | True | None | None | None |
| b | False | integer | True | None | None | None |
| battle_name | False | text | True | 255 | None | None |
| in_encyclopedia | False | yesno | True | None | None | None |
| is_sea | False | yesno | True | None | None | None |
| owner_bundle | False | text | False | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
  
## regions_continents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| continent | True | text | True | 50 | None | None |
  
## regions_titles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| region | True | text | True | 50 | [regions_tables](#regions_tables) | key |
| government | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| gender | True | text | True | 50 | [genders_tables](#genders_tables) | gender |
| title | False | text | True | 50 | None | None |
  
## regions_to_region_groups_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| region_group | True | text | True | 1024 | [region_groups_tables](#region_groups_tables) | group_key |
| region | True | text | True | 50 | [regions_tables](#regions_tables) | key |
  
## region_campaign_overrides_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| region | True | text | True | 255 | [regions_tables](#regions_tables) | key |
| campaign | True | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| religion | False | text | False | 255 | [religions_tables](#religions_tables) | religion_key |
| religion_zeal | False | integer | True | None | None | None |
  
## region_economics_factors_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| factor | True | text | True | 50 | None | None |
| positive_pip_path | False | text | True | 100 | None | None |
| positive_tooltip | False | text | True | 536870910 | None | None |
  
## region_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| group_key | True | text | True | 1024 | None | None |
| localised_name | False | text | True | 20000 | None | None |
| camera_position_x | False | double | True | None | None | None |
| camera_position_y | False | double | True | None | None | None |
| camera_zoom | False | double | True | None | None | None |
| camera_heading | False | double | True | None | None | None |
| round | False | integer | True | None | None | None |
  
## region_religions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| region | True | text | True | 255 | [regions_tables](#regions_tables) | key |
| religion | False | text | True | 255 | [religions_tables](#religions_tables) | religion_key |
| religion_zeal | False | integer | True | None | None | None |
  
## region_to_province_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| region | True | text | True | 50 | [regions_tables](#regions_tables) | key |
| province | True | text | True | 255 | [provinces_tables](#provinces_tables) | key |
  
## region_unit_resources_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| string | False | text | True | 50 | None | None |
  
## religions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| religion_key | True | text | True | 50 | None | None |
| onscreen | False | text | True | 50 | None | None |
| convertibility | False | integer | True | None | None | None |
| ui_icon_path | False | text | True | 100 | None | None |
  
## religion_conversion_mods_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| rel_from | True | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
| rel_to | True | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
| modifier | False | double | True | None | None | None |
  
## resources_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| icon_filepath | False | text | True | 50 | None | None |
| key | True | text | True | 50 | None | None |
| onscreen_text | False | text | True | 50 | None | None |
| unit | False | text | False | 50 | [commodity_unit_names_tables](#commodity_unit_names_tables) | unit |
| slot_bed | False | text | True | 50 | [slots_tables](#slots_tables) | slot |
| trade_value | False | integer | True | None | None | None |
| strategic_value | False | integer | True | None | None | None |
| description | False | text | True | 2048 | None | None |
| long_description | False | text | False | 2048 | None | None |
| in_encyclopedia | False | yesno | True | None | None | None |
  
## resource_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| resource_key | True | text | True | 50 | [resources_tables](#resources_tables) | key |
| effect_key | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | single | True | None | None | None |
  
## scripted_objectives_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| localised_text | False | text | True | 255 | None | None |
  
## scripted_subtitles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| localised_text | False | text | True | 255 | None | None |
| character_for_vo | False | text | False | 255 | None | None |
  
## seasons_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| season | True | text | True | 50 | None | None |
| onscreen | False | text | True | 50 | None | None |
| order | False | integer | True | None | None | None |
  
## season_attritions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| season | True | text | True | 255 | [seasons_tables](#seasons_tables) | season |
| attrition_type | True | text | True | 255 | [campaign_map_attritions_tables](#campaign_map_attritions_tables) | key |
| enable | True | yesno | True | None | None | None |
| campaign | True | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
  
## season_province_effect_bundles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| season | True | text | True | 255 | [seasons_tables](#seasons_tables) | season |
| province | True | text | True | 255 | [provinces_tables](#provinces_tables) | key |
| effect_bundle | True | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| weighting | False | integer | True | None | None | None |
| default | False | yesno | True | None | None | None |
  
## sea_climate_details_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | [climates_tables](#climates_tables) | climate_type |
| sea_deep_colour | False | text | True | 50 | None | None |
| sea_shallow_colour | False | text | True | 50 | None | None |
| sun_colour | False | text | True | 50 | None | None |
| sky_colour | False | text | True | 50 | None | None |
  
## sea_surfaces_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| sea_wind_speed | False | single | True | None | None | None |
| sea_phillips_constant | False | single | True | None | None | None |
| sea_choppiness | False | single | True | None | None | None |
| swell_wind_speed | False | single | True | None | None | None |
| swell_phillips_constant | False | single | True | None | None | None |
| foam_enabled | False | yesno | True | None | None | None |
| foam_decay_rate | False | single | True | None | None | None |
| foam_fade_in_time | False | single | True | None | None | None |
| foam_cut_off_value | False | single | True | None | None | None |
| froth_value | False | single | True | None | None | None |
| froth_distortion_speed | False | single | True | None | None | None |
| froth_distortion_amount | False | single | True | None | None | None |
| spray_cut_off_value | False | single | True | None | None | None |
| spray_speed | False | single | True | None | None | None |
| spray_duration | False | single | True | None | None | None |
| sea_shininess | False | single | True | None | None | None |
| sea_decay | False | single | True | None | None | None |
| reflection_flattening_factor | False | single | True | None | None | None |
| wave_trough_y_value | False | single | True | None | None | None |
| detail_normal_uv_scale1 | False | single | True | None | None | None |
| detail_normal_uv_speed1 | False | single | True | None | None | None |
| detail_normal_uv_scale2 | False | single | True | None | None | None |
| detail_normal_uv_speed2 | False | single | True | None | None | None |
  
## send_diplomat_incidents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| outcome | True | text | True | 20 | [send_diplomat_outcomes_tables](#send_diplomat_outcomes_tables) | key |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| incident | True | text | True | 255 | [incidents_tables](#incidents_tables) | key |
| weight | False | integer | True | None | None | None |
  
## send_diplomat_outcomes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 20 | None | None |
  
## ship_dbs_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| spacing | False | text | True | 255 | [unit_spacings_tables](#unit_spacings_tables) | key |
| entity | False | text | True | 50 | [battle_entities_tables](#battle_entities_tables) | key |
| model | False | text | True | 50 | [models_naval_tables](#models_naval_tables) | key |
  
## ship_names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | integer | True | None | [names_groups_tables](#names_groups_tables) | key |
| name_group | False | integer | True | None | [names_groups_tables](#names_groups_tables) | key |
| Ship_Name | False | text | True | 50 | None | None |
| exclusive_to_faction | False | text | False | 50 | [factions_tables](#factions_tables) | key |
  
## shortcut_localisation_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 50 | None | None |
| onscreen | False | text | False | 536870910 | None | None |
| toolitp | False | text | False | 255 | None | None |
  
## skeletons_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## slots_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| slot | True | text | True | 50 | None | None |
| is_farm | False | yesno | True | None | None | None |
| is_resource | False | yesno | False | None | None | None |
| is_town | False | yesno | False | None | None | None |
| is_port | False | yesno | False | None | None | None |
| supports_building_level_conversion | False | yesno | False | None | None | None |
  
## slots_art_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| slot | True | text | True | 50 | [slots_tables](#slots_tables) | slot |
| culture | True | text | True | 50 | [cultures_tables](#cultures_tables) | key |
| underlay_terrain_texture | False | text | False | 50 | [warscape_underlay_textures_tables](#warscape_underlay_textures_tables) | underlay_key |
| underlay_rotation | False | integer | False | None | None | None |
| underlay_scale | False | integer | False | None | None | None |
| underlay_differs_with_building | False | yesno | False | None | None | None |
| template_model | False | text | False | 50 | [slots_templates_models_tables](#slots_templates_models_tables) | template_name |
| template_differs_at_quality_zero | False | yesno | False | None | None | None |
| template_model_art_quality_zero | False | text | False | 50 | [slots_templates_models_tables](#slots_templates_models_tables) | template_name |
| use_minibuildings | False | yesno | False | None | None | None |
| minibuildings_differ_at_quality | False | yesno | False | None | None | None |
| use_minibuildings_from_quality | False | integer | True | None | None | None |
| empty_building_model | False | text | False | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
| empty_building_model_animated | False | text | False | 50 | [warscape_animated_tables](#warscape_animated_tables) | key |
| display_empty_bldg_from_quality | False | integer | True | None | None | None |
  
## slots_gdp_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| slot | True | text | True | 50 | [slots_tables](#slots_tables) | slot |
| level | True | integer | True | None | None | None |
| gdp_value | False | integer | True | None | None | None |
| building_gdp_modifier | False | double | True | None | None | None |
| onscreen_name | False | text | True | 50 | None | None |
  
## slots_templates_models_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| template_name | True | text | True | 50 | None | None |
| model_filename | False | text | True | 255 | None | None |
| model_filepath | False | text | True | 255 | None | None |
  
## slot_templates_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## slot_template_to_building_superchain_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| slot_template | False | text | True | 255 | [slot_templates_tables](#slot_templates_tables) | key |
| building_superchain | False | text | True | 255 | [building_superchains_tables](#building_superchains_tables) | key |
  
## slot_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| can_destroy | False | yesno | True | None | None | None |
| can_convert | False | yesno | True | None | None | None |
  
## small_vegetation_climates_jct_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| climate | True | text | True | 50 | [climates_tables](#climates_tables) | climate_type |
| rigid_name | True | text | True | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
  
## special_abilities_specific_behaviour_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 20000 | None | None |
  
## special_ability_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ability_group | True | text | True | 255 | None | None |
| tooltip | False | text | True | 255 | None | None |
| icon_path | False | text | True | 255 | None | None |
| name | False | text | True | 255 | None | None |
| special_edition_mask | False | integer | True | None | None | None |
  
## special_ability_groups_to_factions_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ability_group | True | text | True | 255 | [special_ability_groups_tables](#special_ability_groups_tables) | ability_group |
| faction | False | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## special_ability_groups_to_unit_abilities_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| special_ability_groups | True | text | True | 255 | [special_ability_groups_tables](#special_ability_groups_tables) | ability_group |
| unit_special_abilities | True | text | True | 255 | [unit_special_abilities_tables](#unit_special_abilities_tables) | key |
  
## special_ability_invalid_usage_flags_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| flag_key | True | text | True | 255 | None | None |
  
## special_ability_phases_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | text | True | 255 | None | None |
| duration | False | single | True | None | None | None |
| effect_type | False | text | True | 255 | [special_ability_phase_effect_types_tables](#special_ability_phase_effect_types_tables) | effect_type |
| requested_stance | False | text | False | 255 | [special_ability_stance_enums_tables](#special_ability_stance_enums_tables) | key |
| unbreakable | False | yesno | True | None | None | None |
| cant_move | False | yesno | True | None | None | None |
| kill_own_unit | False | yesno | True | None | None | None |
| minor_casualties | False | yesno | True | None | None | None |
| major_casualties | False | yesno | True | None | None | None |
| freeze_fatigue | False | yesno | True | None | None | None |
| fatigue_change_ratio | False | double | True | None | None | None |
| inspiration_aura_range_mod | False | double | True | None | None | None |
| ability_recharge_change | False | double | True | None | None | None |
| ui_vfx | False | text | False | 255 | [ui_effects_tables](#ui_effects_tables) | key |
| rally_amount | False | integer | True | None | None | None |
  
## special_ability_phase_attribute_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| phase | True | text | True | 255 | [special_ability_phases_tables](#special_ability_phases_tables) | id |
| attribute | True | text | True | 255 | [unit_attributes_tables](#unit_attributes_tables) | key |
  
## special_ability_phase_effect_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| effect_type | True | text | True | 255 | None | None |
  
## special_ability_phase_stat_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| phase | True | text | True | 255 | [special_ability_phases_tables](#special_ability_phases_tables) | id |
| value | False | text | True | 255 | None | None |
| stat | True | text | True | 255 | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| how | False | text | True | 255 | [unit_stat_modifiers_how_enums_tables](#unit_stat_modifiers_how_enums_tables) | key |
  
## special_ability_stance_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## special_ability_to_auto_deactivate_flags_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| invalid_usage_flag | True | text | True | 255 | [special_ability_invalid_usage_flags_tables](#special_ability_invalid_usage_flags_tables) | flag_key |
| special_ability_key | True | text | True | 255 | [unit_special_abilities_tables](#unit_special_abilities_tables) | key |
  
## special_ability_to_invalid_usage_flags_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| special_ability | True | text | True | 255 | [unit_special_abilities_tables](#unit_special_abilities_tables) | key |
| invalid_usage_flag | True | text | True | 255 | [special_ability_invalid_usage_flags_tables](#special_ability_invalid_usage_flags_tables) | flag_key |
  
## special_ability_to_special_ability_phase_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| special_ability | True | text | True | 50 | [unit_special_abilities_tables](#unit_special_abilities_tables) | key |
| phase | False | text | True | 255 | [special_ability_phases_tables](#special_ability_phases_tables) | id |
| order | True | integer | True | None | None | None |
  
## spotting_and_hiding_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| visibility_min_spot_range | False | integer | True | None | None | None |
| visibility_max_spot_range | False | integer | True | None | None | None |
| spot_dist_tree | False | integer | True | None | None | None |
| spot_dist_scrub | False | integer | True | None | None | None |
  
## stances_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| onscreen | False | text | True | 50 | None | None |
  
## start_pos_calendars_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| campaign | True | text | True | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| start_year | False | integer | True | None | None | None |
| start_season | False | text | True | 50 | [seasons_tables](#seasons_tables) | season |
| turns_per_year | False | integer | True | None | None | None |
| start_week_of_year | False | integer | True | None | None | None |
  
## start_pos_characters_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ID | True | autonumber | True | None | None | None |
| faction | False | integer | True | None | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| Name | False | integer | True | None | [names_tables](#names_tables) | id |
| Surname | False | integer | False | None | [names_tables](#names_tables) | id |
| Age | False | integer | True | None | None | None |
| Type | False | text | True | 50 | [agents_tables](#agents_tables) | key |
| startx | False | double | True | None | None | None |
| starty | False | double | True | None | None | None |
| ministerial_position | False | text | False | 50 | [ministerial_positions_tables](#ministerial_positions_tables) | minister_key |
| portrait_id | False | text | False | 255 | [campaign_character_art_sets_tables](#campaign_character_art_sets_tables) | art_set_id |
| model | False | text | False | 255 | None | None |
| immortal | False | yesno | False | None | None | None |
| override_general_unit | False | text | False | 255 | [main_units_tables](#main_units_tables) | unit |
| is_in_generals_pool | False | yesno | True | None | None | None |
| is_male | False | yesno | True | None | None | None |
| loyalty | False | integer | True | None | None | None |
| clan_name | False | integer | False | None | [names_tables](#names_tables) | id |
| other_name | False | integer | False | None | [names_tables](#names_tables) | id |
| ambition | False | integer | True | None | None | None |
| political_party | False | text | False | 255 | [political_parties_tables](#political_parties_tables) | key |
| death_type | False | text | False | 255 | [death_types_tables](#death_types_tables) | key |
| turns_died_before_start | False | text | False | 255 | None | None |
| legacy_override | False | text | False | 255 | None | None |
| progenitor | False | yesno | True | None | None | None |
| xp | False | integer | True | None | None | None |
  
## start_pos_character_ancillaries_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| character_id | False | integer | True | None | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
| ancillary | False | text | True | 50 | [ancillary_info_tables](#ancillary_info_tables) | ancillary |
  
## start_pos_character_to_settlements_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| character | True | integer | True | None | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
| settlement | False | integer | True | None | [start_pos_settlements_tables](#start_pos_settlements_tables) | id |
  
## start_pos_character_traits_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| character_id | False | integer | True | None | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
| trait_level | False | text | True | 50 | [character_trait_levels_tables](#character_trait_levels_tables) | key |
  
## start_pos_diplomacy_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | False | autonumber | True | None | None | None |
| faction1 | True | integer | True | None | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| faction2 | True | integer | True | None | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| stance | False | text | True | 50 | [stances_tables](#stances_tables) | key |
| grants_military_access | False | yesno | True | None | None | None |
| grants_trade_agreement | False | yesno | True | None | None | None |
| relations_modifier | False | integer | True | None | None | None |
| non_aggression_pact | False | yesno | True | None | None | None |
  
## start_pos_factions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ID | True | autonumber | True | None | None | None |
| faction | False | text | True | 50 | [factions_tables](#factions_tables) | key |
| campaign | False | text | True | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| playable | False | yesno | True | None | None | None |
| treasury | False | integer | True | None | None | None |
| starting_order | False | integer | True | None | None | None |
| government_type | False | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| state_religion | False | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
| is_major | False | yesno | False | None | None | None |
| description | False | text | False | 536870910 | None | None |
| difficulty | False | text | False | 255 | None | None |
| ai_manager | False | text | True | 255 | [campaign_ai_managers_tables](#campaign_ai_managers_tables) | manager |
| ai_personality | False | text | True | 255 | [campaign_ai_personalities_tables](#campaign_ai_personalities_tables) | personality |
| long_victory_region_count | False | integer | True | None | None | None |
| short_victory_region_count | False | integer | True | None | None | None |
| prestige_victory_region_count | False | integer | True | None | None | None |
| world_domination_victory_region_count | False | integer | True | None | None | None |
| short_victory_year_end | False | integer | True | None | None | None |
| long_victory_year_end | False | integer | True | None | None | None |
| prestige_victory_year_end | False | integer | True | None | None | None |
| world_domination_victory_year_end | False | integer | True | None | None | None |
| prestige_army | False | integer | True | None | None | None |
| prestige_navy | False | integer | True | None | None | None |
| prestige_economy | False | integer | True | None | None | None |
| prestige_enlightenment | False | integer | True | None | None | None |
| short_victory_week_in_year_end | False | integer | True | None | None | None |
| long_victory_week_in_year_end | False | integer | True | None | None | None |
| prestige_victory_week_in_year_end | False | integer | True | None | None | None |
| world_domination_victory_week_in_year_end | False | integer | True | None | None | None |
| honour | False | integer | True | None | None | None |
| ai_technology_manager | False | text | False | 255 | [campaign_ai_technology_managers_tables](#campaign_ai_technology_managers_tables) | key |
| ai_character_skill_tree_manager | False | text | False | 255 | [campaign_ai_character_skill_tree_managers_tables](#campaign_ai_character_skill_tree_managers_tables) | key |
| cai_agent_distribution_profile | False | text | True | 255 | [cai_agent_distribution_profiles_tables](#cai_agent_distribution_profiles_tables) | key |
| cai_agent_recruitment_profile | False | text | True | 255 | [cai_agent_recruitment_profiles_tables](#cai_agent_recruitment_profiles_tables) | key |
| cai_starting_personality | False | text | False | 255 | [cai_personalities_tables](#cai_personalities_tables) | key |
| mp_one_vs_one_region_count | False | integer | True | None | None | None |
| mp_2p_co_op_region_count | False | integer | True | None | None | None |
| mp_2p_co_op_region_count_long | False | integer | True | None | None | None |
| long_description | False | text | False | 536870910 | None | None |
| can_ever_convert_religion | False | yesno | True | None | None | None |
| cdir_military_generator_config | False | text | True | 255 | [cdir_military_generator_configs_tables](#cdir_military_generator_configs_tables) | key |
  
## start_pos_faction_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| start_pos_faction | True | integer | True | None | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| effect_value | False | single | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## start_pos_faction_effect_bundles_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| start_pos_faction | True | integer | True | None | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| effect_bundle | True | text | True | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| duration | False | integer | True | None | None | None |
  
## start_pos_family_relationships_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| character | True | integer | True | None | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
| related_to | True | integer | True | None | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
| relationship | False | text | True | 255 | [family_relationship_types_tables](#family_relationship_types_tables) | relationship_type |
| bastard | False | yesno | True | None | None | None |
| adopted | False | yesno | True | None | None | None |
  
## start_pos_governorships_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| governorship | False | text | True | 50 | [governorships_tables](#governorships_tables) | governorship |
| campaign | False | text | True | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| lower_class_tax_rate | False | integer | True | None | None | None |
| upper_class_tax_rate | False | double | True | None | None | None |
  
## start_pos_land_units_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| unit_type | False | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| general | False | integer | True | None | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
| soldiers | False | integer | True | None | None | None |
  
## start_pos_naval_units_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ID | True | autonumber | True | None | None | None |
| unit_type | False | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| admiral | False | integer | True | None | [start_pos_characters_tables](#start_pos_characters_tables) | ID |
  
## start_pos_past_events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| source | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| target | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| event | True | text | True | 255 | [cai_personality_diplomatic_events_tables](#cai_personality_diplomatic_events_tables) | id |
| turns_ago | True | integer | True | None | None | None |
  
## start_pos_regions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | False | autonumber | True | None | None | None |
| region | True | text | True | 50 | [regions_tables](#regions_tables) | key |
| campaign | True | text | True | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| owning_faction | False | integer | True | None | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| faction_capital | False | yesno | True | None | None | None |
| base_population | False | integer | True | None | None | None |
| base_max_population | False | integer | True | None | None | None |
| population | False | integer | True | None | None | None |
| base_gdp | False | integer | True | None | None | None |
| road_upgrades | False | integer | True | None | None | None |
| canals | False | yesno | True | None | None | None |
| railways | False | yesno | True | None | None | None |
| town_wealth | False | integer | True | None | None | None |
| governorship | False | text | True | 50 | [governorships_tables](#governorships_tables) | governorship |
| cultural_originator | False | text | False | 50 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| rebel_faction | False | text | True | 50 | [factions_tables](#factions_tables) | key |
| rebel_faction_name | False | text | True | 536870910 | None | None |
| alternative_rebel_faction | False | text | True | 255 | [factions_tables](#factions_tables) | key |
| settler_rebellions_enabled | False | yesno | False | None | None | None |
| capture_prestige | False | integer | True | None | None | None |
| long_description | False | text | False | 536870910 | None | None |
| development_points | False | integer | True | None | None | None |
  
## start_pos_regions_to_unit_resources_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | integer | False | None | [start_pos_regions_tables](#start_pos_regions_tables) | id |
| resource | True | text | False | 50 | [region_unit_resources_tables](#region_unit_resources_tables) | key |
  
## start_pos_region_religions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| region | True | integer | True | None | [start_pos_regions_tables](#start_pos_regions_tables) | id |
| religion | True | text | True | 50 | [religions_tables](#religions_tables) | religion_key |
| percentage | False | double | True | None | None | None |
  
## start_pos_region_slot_templates_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| campaign | True | text | True | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| region | True | text | True | 50 | [regions_tables](#regions_tables) | key |
| slot_type | True | text | True | 255 | [slot_types_tables](#slot_types_tables) | key |
| slot_template | True | text | True | 255 | [slot_templates_tables](#slot_templates_tables) | key |
  
## start_pos_settlements_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| settlement_id | True | text | True | 50 | [campaign_map_settlements_tables](#campaign_map_settlements_tables) | settlement_id |
| region | True | integer | True | None | [start_pos_regions_tables](#start_pos_regions_tables) | id |
| building1 | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| building2 | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| building3 | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| building4 | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| building5 | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| wealth | False | integer | False | None | None | None |
| fortification | False | integer | False | None | None | None |
| onscreen_name | False | text | True | 536870910 | None | None |
| id | False | autonumber | False | None | None | None |
| roads | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| fortifications | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| primary_building | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| port_building | False | text | False | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| startpos_slave_points | False | integer | True | None | None | None |
  
## start_pos_settlement_garrisons_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | True | None | None | None |
| settlement | False | integer | True | None | [start_pos_settlements_tables](#start_pos_settlements_tables) | id |
| unit | False | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| soldiers | False | integer | True | None | None | None |
  
## start_pos_technologies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| faction | True | integer | True | None | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| technology | True | text | True | 50 | [technologies_tables](#technologies_tables) | key |
  
## start_pos_victory_conditions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| start_pos_faction | True | integer | True | None | [start_pos_factions_tables](#start_pos_factions_tables) | ID |
| region | True | text | True | 50 | [regions_tables](#regions_tables) | key |
| victory_type | True | text | True | 50 | [victory_types_tables](#victory_types_tables) | victory_type |
  
## state_gift_values_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| value | False | integer | True | None | None | None |
  
## stats_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| public | False | yesno | True | None | None | None |
| label | False | text | False | 255 | [random_localisation_strings_tables](#random_localisation_strings_tables) | key |
| ladder | False | yesno | True | None | None | None |
  
## stats_clans_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| public | False | yesno | True | None | None | None |
| label | False | text | False | 255 | [random_localisation_strings_tables](#random_localisation_strings_tables) | key |
| ladder | False | yesno | True | None | None | None |
  
## subtitle_timings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| subtitle_field | True | integer | True | None | [TExc_LocalisableFields_tables](#TExc_LocalisableFields_tables) | key |
| language | True | text | True | 255 | [languages_tables](#languages_tables) | key |
| start | False | integer | True | None | None | None |
| end | False | integer | True | None | None | None |
| script_id | False | integer | True | None | [vo_scripts_tables](#vo_scripts_tables) | id |
| text_section | True | integer | True | None | None | None |
| foreign_key | True | text | True | 255 | None | None |
| text_id | False | text | True | 20000 | None | None |
  
## taxes_classes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| tax | True | text | True | 50 | None | None |
  
## taxes_effects_jct_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| tax_name | True | text | False | 50 | [taxes_keys_tables](#taxes_keys_tables) | tax_lookup |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | double | True | None | None | None |
| optional_campaign_key | True | text | False | 50 | [campaigns_tables](#campaigns_tables) | campaign_name |
| optional_difficulty_level | True | text | False | 50 | None | None |
| ai_only | True | yesno | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## taxes_keys_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| tax_class | True | text | True | 50 | [taxes_classes_tables](#taxes_classes_tables) | tax |
| tax_level | True | text | False | 50 | [taxes_levels_tables](#taxes_levels_tables) | tax_level |
| tax_lookup | False | text | True | 50 | None | None |
  
## taxes_levels_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| tax_level | True | text | True | 50 | None | None |
| percentage | False | integer | True | None | None | None |
  
## team_colours_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| alliance | False | integer | True | None | None | None |
| r | True | integer | True | None | None | None |
| g | True | integer | True | None | None | None |
| b | True | integer | True | None | None | None |
| army_index | False | integer | True | None | None | None |
  
## technologies_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| building_level | False | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
| position_index | False | integer | True | None | None | None |
| onscreen_name | False | text | True | 255 | None | None |
| short_description | False | text | True | 536870910 | None | None |
| long_description | False | text | True | 536870910 | None | None |
| icon_name | False | text | True | 255 | None | None |
| research_points_required | False | integer | True | None | None | None |
| military_prestige | False | integer | True | None | None | None |
| naval_prestige | False | integer | True | None | None | None |
| economic_prestige | False | integer | True | None | None | None |
| enlightenment_prestige | False | integer | True | None | None | None |
| mp_available_early | False | yesno | False | None | None | None |
| mp_available_late | False | yesno | False | None | None | None |
| info_pic | False | text | True | 255 | None | None |
| ai_bias | False | integer | True | None | None | None |
| unique_index | False | autonumber | True | None | None | None |
| in_encyclopedia | False | yesno | True | None | None | None |
| cost_per_round | False | integer | True | None | None | None |
| is_civil | False | yesno | True | None | None | None |
| is_engineering | False | yesno | True | None | None | None |
| is_military | False | yesno | True | None | None | None |
  
## technology_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| position | False | integer | True | None | None | None |
  
## technology_category_modules_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| technology_node_set | True | text | True | 255 | [technology_node_sets_tables](#technology_node_sets_tables) | key |
| max_tier | True | integer | True | None | None | None |
| effect_bundle | False | text | False | 255 | [effect_bundles_tables](#effect_bundles_tables) | key |
| min_tier | False | integer | True | None | None | None |
  
## technology_category_parents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| parent_category | True | text | True | 255 | [technology_categories_tables](#technology_categories_tables) | key |
| child_category | True | text | True | 255 | [technology_categories_tables](#technology_categories_tables) | key |
  
## technology_effects_junction_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| technology | True | text | True | 255 | [technologies_tables](#technologies_tables) | key |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | text | True | 50 | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## technology_faction_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| technology_key | True | text | True | 255 | [technologies_tables](#technologies_tables) | key |
| faction_key | True | text | True | 255 | [factions_tables](#factions_tables) | key |
  
## technology_nodes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| technology_node_set | False | text | True | 255 | [technology_node_sets_tables](#technology_node_sets_tables) | key |
| technology_key | False | text | True | 255 | [technologies_tables](#technologies_tables) | key |
| faction_key | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| campaign_key | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| tier | False | integer | True | None | None | None |
| indent | False | integer | True | None | None | None |
  
## technology_node_links_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| parent_key | True | text | True | 255 | [technology_nodes_tables](#technology_nodes_tables) | key |
| child_key | True | text | True | 255 | [technology_nodes_tables](#technology_nodes_tables) | key |
| initial_descent_tiers | False | integer | True | None | None | None |
| parent_link_position | False | integer | True | None | None | None |
| child_link_position | False | integer | True | None | None | None |
| encyclopedia_parent_link_position | False | integer | False | None | None | None |
| encyclopedia_child_link_position | False | integer | False | None | None | None |
  
## technology_node_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| faction_key | False | text | False | 255 | [factions_tables](#factions_tables) | key |
| campaign_key | False | text | False | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| technology_category | False | text | True | 255 | [technology_categories_tables](#technology_categories_tables) | key |
| culture | False | text | False | 255 | [cultures_tables](#cultures_tables) | key |
| subculture | False | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| localised_name | False | text | True | 255 | None | None |
| tooltip_string | False | text | True | 255 | None | None |
| encyclopaedia_string | False | text | True | 255 | None | None |
  
## technology_required_building_levels_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| technology | True | text | True | 255 | [technologies_tables](#technologies_tables) | key |
| required_building_level | True | text | True | 50 | [building_levels_tables](#building_levels_tables) | level_name |
  
## technology_required_technology_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| technology | True | text | True | 255 | [technologies_tables](#technologies_tables) | key |
| required_technology | True | text | True | 255 | [technologies_tables](#technologies_tables) | key |
  
## technology_unit_upgrades_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| technology | True | text | True | 255 | [technologies_tables](#technologies_tables) | key |
| unit | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| target_unit | False | text | False | 255 | [main_units_tables](#main_units_tables) | unit |
| cost | False | integer | True | None | None | None |
  
## terrain_tilesets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| tileset_name | True | text | True | 255 | None | None |
  
## TExc_campaign_map_processing_exports_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| table_name | True | text | False | 50 | None | None |
  
## TExc_data_folders_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| directory | True | text | False | 255 | None | None |
| code_owner | False | text | False | 50 | None | None |
| author | False | text | False | 50 | None | None |
| exclude | False | yesno | False | None | None | None |
| packing_notes | False | text | False | 536870910 | None | None |
| pack_file | False | text | False | 255 | [TExc_pack_files_tables](#TExc_pack_files_tables) | pack_file |
  
## texc_expansions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| expansion | True | text | True | 255 | None | None |
| description | False | text | True | 255 | None | None |
| pack_filename_extension | False | text | False | 255 | None | None |
| released | False | yesno | True | None | None | None |
  
## TExc_ImplementedTables_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| table_name | True | text | False | 100 | None | None |
| Designer | False | text | False | 50 | None | None |
| Implemented | False | yesno | False | None | None | None |
| Implementer | False | text | False | 50 | None | None |
| Modified | False | yesno | False | None | None | None |
| destination_pack | False | text | False | 50 | [TExc_PackCategories_tables](#TExc_PackCategories_tables) | pack_category |
  
## TExc_LocalisableFields_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | False | None | None | None |
| table_name | False | text | False | 50 | [TExc_ImplementedTables_tables](#TExc_ImplementedTables_tables) | table_name |
| field | False | text | False | 50 | None | None |
| destination_file | False | text | False | 50 | None | None |
| ready_for_export | False | yesno | False | None | None | None |
| spreadsheet | False | text | False | 255 | None | None |
| field_as_key | False | text | False | 255 | None | None |
| for_vo | False | yesno | True | None | None | None |
  
## TExc_missing_conditions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ID | True | autonumber | False | None | None | None |
| exported_script | False | text | False | 255 | None | None |
| condition | False | text | False | 255 | None | None |
  
## TExc_PackCategories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| pack_category | True | text | False | 50 | None | None |
| script_name | False | text | False | 50 | None | None |
| pack_file | False | text | False | 50 | None | None |
| localisation_file | False | text | False | 50 | None | None |
| locked | False | yesno | False | None | None | None |
| locked_by | False | text | False | 50 | None | None |
  
## TExc_pack_files_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| pack_file | True | text | False | 255 | None | None |
| notes | False | text | False | 536870910 | None | None |
  
## TExc_script_conditions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| Condition | True | text | False | 100 | None | None |
  
## TExc_TableExportCategories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| category | True | text | False | 50 | None | None |
  
## TExc_TableExportGroups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ID | True | autonumber | False | None | None | None |
| category | False | text | False | 50 | [TExc_TableExportCategories_tables](#TExc_TableExportCategories_tables) | category |
| table | False | text | False | 50 | [TExc_ImplementedTables_tables](#TExc_ImplementedTables_tables) | table_name |
  
## TExc_unrest_causes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| cause | True | text | False | 50 | None | None |
  
## TExc_unrest_demands_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| demand | True | text | False | 50 | None | None |
  
## town_wealth_growth_factors_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| factor | True | text | True | 50 | None | None |
| positive_pip_path | False | text | True | 100 | None | None |
| positive_tooltip | False | text | True | 536870910 | None | None |
| negative_pip_path | False | text | False | 200 | None | None |
| negative_tooltip | False | text | False | 536870910 | None | None |
  
## trade_details_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| onscreen_text | False | text | True | 536870910 | None | None |
| icon_filepath | False | text | True | 50 | None | None |
  
## trade_display_campaign_originating_culture_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| originating_culture | False | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_originating_culture_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| originating_culture | False | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_originating_subculture_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| originating_subculture | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_originating_subculture_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| originating_subculture | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_owning_culture_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| owning_culture | False | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_owning_culture_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| owning_culture | False | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_owning_faction_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| owning_faction | False | text | True | 255 | [factions_tables](#factions_tables) | key |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_owning_faction_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| owning_faction | False | text | True | 255 | [factions_tables](#factions_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_owning_subculture_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| owning_subculture | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_owning_subculture_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| owning_subculture | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_campaign_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| campaign | False | text | True | 255 | [campaigns_tables](#campaigns_tables) | campaign_name |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_generic_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_originating_culture_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| originating_culture | False | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_originating_culture_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| originating_culture | False | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_originating_subculture_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| originating_subculture | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_originating_subculture_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| originating_subculture | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_owning_culture_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| owning_culture | False | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_owning_culture_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| owning_culture | False | text | True | 255 | [cultures_tables](#cultures_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_owning_faction_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| owning_faction | False | text | True | 255 | [factions_tables](#factions_tables) | key |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_owning_faction_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| owning_faction | False | text | True | 255 | [factions_tables](#factions_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_owning_subculture_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| owning_subculture | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_owning_subculture_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| owning_subculture | False | text | True | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_produced_resource_trade_model_options_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| produced_resource | False | text | True | 255 | [resources_tables](#resources_tables) | key |
| model | False | text | True | 255 | [trade_display_trade_models_tables](#trade_display_trade_models_tables) | key |
| priority | False | single | True | None | None | None |
| relative_frequency | False | single | True | None | None | None |
  
## trade_display_trade_models_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| model | False | text | True | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
| optional_following_model | False | text | False | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
| is_naval | False | yesno | True | None | None | None |
| optional_following_model_distance | False | single | True | None | None | None |
  
## trade_nodes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ID | True | text | True | 50 | None | None |
| commodity | False | text | True | 50 | [commodities_tables](#commodities_tables) | key |
| base_quantity | False | integer | True | None | None | None |
| percentage_increase_per_agent | False | double | True | None | None | None |
| maximum_percentage_increase | False | double | True | None | None | None |
| display_name | False | text | True | 255 | None | None |
| group | False | text | True | 255 | [trade_node_groups_tables](#trade_node_groups_tables) | key |
  
## trade_node_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| display_name | False | text | True | 255 | None | None |
  
## trait_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| category | True | text | False | 50 | None | None |
| icon_path | False | text | False | 100 | None | None |
  
## trait_info_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| trait | True | text | True | 255 | None | None |
| applicable_to | False | text | True | 50 | None | None |
  
## trait_level_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| trait_level | True | text | True | 50 | [character_trait_levels_tables](#character_trait_levels_tables) | key |
| effect | True | text | True | 50 | [effects_tables](#effects_tables) | effect |
| value | False | double | True | None | None | None |
| effect_scope | False | text | True | 255 | [campaign_effect_scopes_tables](#campaign_effect_scopes_tables) | key |
  
## trait_to_antitraits_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| trait | True | text | True | 50 | [trait_info_tables](#trait_info_tables) | trait |
| antitrait | True | text | True | 50 | [trait_info_tables](#trait_info_tables) | trait |
  
## trait_to_included_agents_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| trait | True | text | True | 50 | [trait_info_tables](#trait_info_tables) | trait |
| agent | True | text | True | 50 | [agents_tables](#agents_tables) | key |
  
## trait_triggers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| trigger | True | text | True | 50 | None | None |
| event | False | text | True | 50 | [trigger_events_tables](#trigger_events_tables) | event |
| conditions | False | text | True | 536870910 | None | None |
  
## translated_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| language | True | text | True | 255 | [languages_tables](#languages_tables) | key |
| last_english_text | False | text | False | 255 | None | None |
| translated_text | False | text | False | 255 | None | None |
| requires_translation | False | yesno | True | None | None | None |
| requires_recording | False | yesno | True | None | None | None |
  
## trigger_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | autonumber | False | None | None | None |
| trigger | False | text | False | 50 | [trait_triggers_tables](#trait_triggers_tables) | trigger |
| trait | False | text | True | 50 | [trait_info_tables](#trait_info_tables) | trait |
| value | False | integer | True | None | None | None |
| chance | False | integer | True | None | None | None |
  
## trigger_events_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| event | True | text | True | 50 | None | None |
| from_ui | False | yesno | False | None | None | None |
  
## trigger_event_to_excluded_agent_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| event | True | text | False | 50 | [trigger_events_tables](#trigger_events_tables) | event |
| agent | True | text | True | 50 | [agents_tables](#agents_tables) | key |
  
## uied_component_addresses_to_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_label | True | text | True | 255 | [uied_component_texts_tables](#uied_component_texts_tables) | component_label |
| component_address | True | text | True | 255 | None | None |
| component_layout | False | text | True | 255 | [uied_text_layouts_tables](#uied_text_layouts_tables) | layout_id |
  
## uied_component_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_label | True | text | True | 255 | None | None |
| localised_string | False | text | True | 536870910 | None | None |
  
## uied_text_layouts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| layout_id | True | text | True | 255 | None | None |
| layout_location | False | text | True | 20000 | None | None |
  
## ui_component_addresses_with_localisation_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_label | True | text | True | 255 | [ui_component_localisation_tables](#ui_component_localisation_tables) | component_label |
| component_address | True | text | False | 255 | None | None |
  
## ui_component_localisation_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| component_label | True | text | False | 255 | None | None |
| localised_string | False | text | False | 536870910 | None | None |
  
## ui_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| banner_fx | False | text | False | 255 | [particle_effects_tables](#particle_effects_tables) | key |
| ping_fx | False | text | False | 255 | [particle_effects_tables](#particle_effects_tables) | key |
  
## ui_unit_stats_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| onscreen_name | False | text | True | 255 | None | None |
| max_value | False | integer | True | None | None | None |
| campaign_only | False | yesno | True | None | None | None |
| sort_order | False | integer | True | None | None | None |
| tooltip_text | False | text | True | 1024 | None | None |
  
## ui_unit_stats_filters_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## ui_unit_stat_to_classes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| stat_key | True | text | True | 255 | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| unit_class | True | text | True | 255 | [unit_class_tables](#unit_class_tables) | key |
| list_order | False | integer | True | None | None | None |
| filter | True | text | True | 255 | [ui_unit_stats_filters_tables](#ui_unit_stats_filters_tables) | key |
  
## uniform_type_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## units_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| on_screen_name | False | text | True | 50 | None | None |
| category | False | text | True | 50 | [unit_category_tables](#unit_category_tables) | key |
| class | False | text | True | 50 | [unit_class_tables](#unit_class_tables) | key |
| multiplayer_cost | False | integer | True | None | None | None |
| multiplayer_late_cost | False | integer | True | None | None | None |
| create_time | False | integer | True | None | None | None |
| create_cost | False | integer | True | None | None | None |
| upkeep_cost | False | integer | True | None | None | None |
| campaign_action_points | False | integer | True | None | None | None |
| voice | False | text | False | 255 | None | None |
| fitness | False | integer | True | None | None | None |
| icon_name | False | text | True | 100 | None | None |
| unit_description_text | False | text | True | 50 | [unit_description_texts_tables](#unit_description_texts_tables) | key |
| info_pic | False | text | True | 100 | None | None |
| region_unit_resource | False | text | False | 50 | [region_unit_resources_tables](#region_unit_resources_tables) | key |
| total_cap | False | integer | True | None | None | None |
| era | False | text | True | 255 | None | None |
| mp_available_early | False | yesno | True | None | None | None |
| mp_available_middle | False | yesno | True | None | None | None |
| mp_available_late | False | yesno | True | None | None | None |
| prestige | False | integer | True | None | None | None |
| armed_citizenry | False | yesno | True | None | None | None |
| total_cap_mp | False | integer | True | None | None | None |
| unit_type_icon | False | text | False | 255 | None | None |
| use_onscreen_name | False | yesno | True | None | None | None |
| unit_caste | False | text | True | 255 | [unit_castes_tables](#unit_castes_tables) | caste |
| additional_building_level_requirement | False | text | False | 1024 | [building_levels_tables](#building_levels_tables) | level_name |
| religion_requirement | False | text | False | 1024 | [religions_tables](#religions_tables) | religion_key |
| resource_requirement | False | text | False | 1024 | [resources_tables](#resources_tables) | key |
| in_encyclopedia | False | yesno | True | None | None | None |
| unit_recruited_movie | False | text | False | 50 | [movie_event_strings_tables](#movie_event_strings_tables) | event |
| unique_index | False | autonumber | True | None | None | None |
| pdlc | False | text | False | 255 | [pdlc_tables](#pdlc_tables) | ID |
| is_male | False | yesno | True | None | None | None |
| supports_first_person | False | yesno | True | None | None | None |
  
## units_custom_battle_permissions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| faction | True | text | True | 255 | [factions_tables](#factions_tables) | key |
| general_unit | True | yesno | True | None | None | None |
| siege_unit_attacker | False | yesno | True | None | None | None |
| siege_unit_defender | False | yesno | True | None | None | None |
  
## units_special_edition_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 50 | [units_tables](#units_tables) | key |
  
## units_to_exclusive_faction_permissions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| faction | True | text | True | 50 | [factions_tables](#factions_tables) | key |
| allowed | False | yesno | True | None | None | None |
  
## units_to_gov_types_conversion_jcts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | integer | True | None | [units_to_gov_type_permissions_tables](#units_to_gov_type_permissions_tables) | unique_number |
| unit | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
  
## units_to_gov_type_outcomes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | [units_tables](#units_tables) | key |
| gov_type | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| outcome | False | text | True | 50 | [units_to_gov_type_outcomes_enum_tables](#units_to_gov_type_outcomes_enum_tables) | key |
  
## units_to_gov_type_outcomes_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## units_to_gov_type_permissions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unique_number | False | autonumber | False | None | None | None |
| key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| gov_type | True | text | True | 50 | [government_types_tables](#government_types_tables) | government_type |
| outcome | False | text | True | 50 | [units_to_gov_type_outcomes_enum_tables](#units_to_gov_type_outcomes_enum_tables) | key |
  
## units_to_groupings_military_permissions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| military_group | True | text | True | 50 | [groupings_military_tables](#groupings_military_tables) | military_group |
  
## unit_abilities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| stationary_for_turn | False | yesno | True | None | None | None |
| supersedes_ability | False | text | False | 50 | None | None |
| requires_effect_enabling | False | yesno | False | None | None | None |
| tooltip_text | False | text | False | 20000 | None | None |
  
## unit_armour_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| armour_value | False | integer | True | None | None | None |
| bonus_v_missiles | False | yesno | False | None | None | None |
| weak_v_missiles | False | yesno | False | None | None | None |
| audio_material | False | text | True | 255 | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
  
## unit_attributes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| bullet_text | False | text | True | 255 | None | None |
  
## unit_attributes_groups_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| group_name | True | text | True | 255 | None | None |
  
## unit_attributes_to_groups_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| attribute | True | text | True | 255 | [unit_attributes_tables](#unit_attributes_tables) | key |
| attribute_group | True | text | False | 255 | [unit_attributes_groups_tables](#unit_attributes_groups_tables) | group_name |
  
## unit_castes_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| caste | True | text | True | 255 | None | None |
| localised_name | False | text | False | 20000 | None | None |
| sort_priority | False | integer | True | None | None | None |
  
## unit_category_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| localised_name | False | text | False | 20000 | None | None |
| r_colour | False | double | True | None | None | None |
| g_colour | False | double | True | None | None | None |
| b_colour | False | double | True | None | None | None |
| min_battle_rows | False | integer | True | None | None | None |
  
## unit_class_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| onscreen | False | text | True | 50 | None | None |
| tooltip | False | text | False | 536870910 | None | None |
| sort_priority | False | integer | True | None | None | None |
| icon | False | text | True | 255 | None | None |
| can_assault_settlment | False | yesno | True | None | None | None |
  
## unit_class_to_population_class_priorities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_class | True | text | False | 50 | [unit_class_tables](#unit_class_tables) | key |
| upper_class_priority | False | integer | False | None | None | None |
| middle_class_priority | False | integer | False | None | None | None |
| lower_class_priority | False | integer | False | None | None | None |
  
## unit_description_historical_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| text | False | text | True | 20000 | None | None |
  
## unit_description_short_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| text | False | text | True | 20000 | None | None |
  
## unit_description_strengths_weaknesses_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| text | False | text | True | 20000 | None | None |
  
## unit_description_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| description_text | False | text | True | 536870910 | None | None |
| long_description_text | False | text | True | 536870910 | None | None |
| strengths_and_weaknesses | False | text | True | 536870910 | None | None |
  
## unit_drills_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_drill_set_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_drill_set | True | text | True | 50 | None | None |
  
## unit_experience_bonuses_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| stat | True | text | True | 255 | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| value | False | integer | True | None | None | None |
| growth_rate | False | double | True | None | None | None |
| growth_scalar | False | double | True | None | None | None |
  
## unit_experience_thresholds_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| value | False | integer | True | None | None | None |
  
## unit_experience_threshold_modifiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| modifier | False | double | True | None | None | None |
  
## unit_fatigue_effects_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| fatigue_level | True | text | True | 255 | [_kv_fatigue_tables](#_kv_fatigue_tables) | key |
| stat | True | text | True | 255 | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| value | False | double | True | None | None | None |
  
## unit_formations_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_formation_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 20000 | None | None |
  
## unit_ground_type_movement_modifiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| ground_type | True | text | True | 50 | [ground_types_tables](#ground_types_tables) | type |
| category | True | text | True | 50 | [unit_category_tables](#unit_category_tables) | key |
| speed_modifier | False | double | True | None | None | None |
  
## unit_melee_weapons_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_naval_artillery_positions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_naval_damage_sites_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_population_caps_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit | True | text | True | 50 | [units_tables](#units_tables) | key |
| faction | True | text | False | 50 | [factions_tables](#factions_tables) | key |
| unit_cap | False | integer | True | None | None | None |
  
## unit_regiment_names_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name_group | True | integer | True | None | [names_groups_tables](#names_groups_tables) | key |
| unit_caste | True | text | False | 255 | [unit_castes_tables](#unit_castes_tables) | caste |
| unit_name | True | text | False | 50 | [unit_regiment_names_localisation_lookup_tables](#unit_regiment_names_localisation_lookup_tables) | key |
| name_order | False | integer | False | None | None | None |
  
## unit_regiment_names_localisation_lookup_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 50 | None | None |
| unit_name | False | text | False | 50 | None | None |
  
## unit_required_technology_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_key | True | text | True | 255 | [main_units_tables](#main_units_tables) | unit |
| technology_key | True | text | True | 255 | [technologies_tables](#technologies_tables) | key |
  
## unit_sets_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## unit_set_to_unit_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_set | True | text | True | 255 | [unit_sets_tables](#unit_sets_tables) | key |
| unit_record | True | text | False | 255 | [main_units_tables](#main_units_tables) | unit |
| unit_caste | True | text | False | 255 | [unit_castes_tables](#unit_castes_tables) | caste |
| unit_category | True | text | False | 255 | [unit_category_tables](#unit_category_tables) | key |
| unit_class | True | text | False | 255 | [unit_class_tables](#unit_class_tables) | key |
| exclude | False | yesno | True | None | None | None |
  
## unit_shield_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| shield_defence_value | False | integer | True | None | None | None |
| shield_armour_value | False | integer | True | None | None | None |
| audio_material | False | text | True | 255 | [audio_materials_enums_tables](#audio_materials_enums_tables) | key |
| missile_block_chance | False | integer | True | None | None | None |
  
## unit_spacings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| close_formation_spacing_horizontal | False | double | True | None | None | None |
| close_formation_spacing_vertical | False | double | True | None | None | None |
| close_formation_spacing_variation | False | double | True | None | None | None |
| loose_formation_spacing_horizontal | False | double | True | None | None | None |
| loose_formation_spacing_vertical | False | double | True | None | None | None |
| loose_formation_spacing_variation | False | double | True | None | None | None |
| dismounted_close_formation_spacing_horizontal | False | double | True | None | None | None |
| dismounted_close_formation_spacing_vertical | False | double | True | None | None | None |
| dismounted_close_formation_spacing_variation | False | double | True | None | None | None |
| dismounted_loose_formation_spacing_horizontal | False | double | True | None | None | None |
| dismounted_loose_formation_spacing_vertical | False | double | True | None | None | None |
| dismounted_loose_formation_spacing_variation | False | double | True | None | None | None |
| horde | False | yesno | True | None | None | None |
  
## unit_special_abilities_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | [unit_abilities_tables](#unit_abilities_tables) | key |
| num_uses | False | integer | True | None | None | None |
| active_time | False | double | True | None | None | None |
| recharge_time | False | double | True | None | None | None |
| initial_recharge | False | single | True | None | None | None |
| wind_up_time | False | double | True | None | None | None |
| passive | False | yesno | True | None | None | None |
| effect_range | False | double | True | None | None | None |
| affect_self | False | yesno | True | None | None | None |
| num_effected_friendly_units | False | integer | True | None | None | None |
| num_effected_enemy_units | False | integer | True | None | None | None |
| update_targets_every_frame | False | yesno | True | None | None | None |
| activated_projectile | False | text | False | 255 | [projectiles_tables](#projectiles_tables) | key |
| can_autotrigger | False | yesno | True | None | None | None |
| target_friends | False | yesno | True | None | None | None |
| target_enemies | False | yesno | True | None | None | None |
| target_ground | False | yesno | True | None | None | None |
| target_intercept_range | False | single | True | None | None | None |
| assume_specific_behaviour | False | text | False | 20000 | [special_abilities_specific_behaviour_types_tables](#special_abilities_specific_behaviour_types_tables) | key |
| clear_current_order | False | yesno | True | None | None | None |
| unique_id | False | autonumber | True | None | None | None |
  
## unit_stats_firing_mechanism_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_stats_land_experience_bonuses_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| xp_level | True | integer | True | None | None | None |
| melee_attack | False | integer | False | None | None | None |
| melee_defence | False | integer | True | None | None | None |
| core_reloading_skill | False | integer | True | None | None | None |
| morale | False | integer | True | None | None | None |
| core_marksmanship | False | integer | True | None | None | None |
| fatigue | False | integer | True | None | None | None |
| mp_fixed_cost | False | double | True | None | None | None |
| mp_experience_cost_multiplier | False | double | True | None | None | None |
  
## unit_stats_naval_crew_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_type | True | text | True | 50 | None | None |
| core_loading_skill | False | integer | True | None | None | None |
| core_marksmanship | False | integer | True | None | None | None |
| melee_attack | False | integer | True | None | None | None |
| melee_defence | False | integer | True | None | None | None |
| melee_weapon_type | False | text | True | 50 | None | None |
| pistols | False | yesno | True | None | None | None |
| ammo | False | integer | True | None | None | None |
| battle_entity | False | text | True | 50 | [battle_entities_tables](#battle_entities_tables) | key |
| soldier_model | False | text | True | 50 | [warscape_animated_tables](#warscape_animated_tables) | key |
| man_animations_table | False | text | False | 50 | [battle_animations_table_tables](#battle_animations_table_tables) | key |
| equipment_theme | False | text | True | 50 | None | None |
| armour_audio | False | text | True | 50 | None | None |
| armour | False | integer | True | None | None | None |
| spacing | False | single | True | None | None | None |
| discipline | False | integer | True | None | None | None |
| missile_type | False | text | False | 255 | [projectiles_tables](#projectiles_tables) | key |
  
## unit_stats_naval_experience_bonuses_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| xp_level | True | integer | True | None | None | None |
| melee_defence | False | integer | True | None | None | None |
| melee_attack | False | integer | True | None | None | None |
| core_gunner_loading_skill | False | integer | False | None | None | None |
| core_gunner_marksmanship | False | integer | True | None | None | None |
| morale | False | integer | True | None | None | None |
| mp_fixed_cost | False | double | True | None | None | None |
| mp_experience_cost_multiplier | False | double | True | None | None | None |
  
## unit_stats_primary_missile_weapon_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_stats_ship_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 100 | None | None |
  
## unit_stats_skeleton_melee_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_stats_skeleton_missile_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_stat_modifiers_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| stat | False | text | True | 255 | [ui_unit_stats_tables](#ui_unit_stats_tables) | key |
| how | False | text | True | 255 | [unit_stat_modifiers_how_enums_tables](#unit_stat_modifiers_how_enums_tables) | key |
  
## unit_stat_modifiers_how_enums_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
  
## unit_to_unit_abilities_junctions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_name | True | text | True | 50 | [units_tables](#units_tables) | key |
| ability | True | text | True | 50 | [unit_abilities_tables](#unit_abilities_tables) | key |
  
## unit_training_level_enum_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
  
## unit_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| type | True | text | True | 50 | None | None |
  
## unit_variants_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| name | False | text | True | 255 | None | None |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| unit | True | text | True | 255 | [land_units_tables](#land_units_tables) | key |
| variant | False | text | True | 255 | [variants_tables](#variants_tables) | variant_name |
| height_variation | False | decimal | True | None | None | None |
| height_scale | False | decimal | True | None | None | None |
| unit_card | False | text | True | 255 | None | None |
  
## unit_variants_colours_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| unit_variant | True | text | True | 255 | [unit_variants_tables](#unit_variants_tables) | name |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| primary_colour_r | False | integer | True | None | None | None |
| primary_colour_g | False | integer | True | None | None | None |
| primary_colour_b | False | integer | True | None | None | None |
| secondary_colour_r | False | integer | True | None | None | None |
| secondary_colour_g | False | integer | True | None | None | None |
| secondary_colour_b | False | integer | True | None | None | None |
| tertiary_colour_r | False | integer | True | None | None | None |
| tertiary_colour_g | False | integer | True | None | None | None |
| tertiary_colour_b | False | integer | True | None | None | None |
| soldier_type | False | text | False | 255 | [uniform_type_enums_tables](#uniform_type_enums_tables) | key |
  
## unit_weights_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| onscreen_text | False | text | True | 20000 | None | None |
  
## unrest_cause_to_demands_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| cause | True | text | True | 50 | [TExc_unrest_causes_tables](#TExc_unrest_causes_tables) | cause |
| level_of_unrest | True | text | True | 50 | None | None |
| demand | False | text | True | 50 | [TExc_unrest_demands_tables](#TExc_unrest_demands_tables) | demand |
  
## variants_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| variant_name | True | text | True | 255 | None | None |
  
## victory_conditions_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| condition | True | text | True | 20000 | None | None |
  
## victory_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| victory_type | True | text | False | 50 | None | None |
  
## videos_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| video_name | True | text | True | 255 | None | None |
| video_type | False | text | True | 255 | [video_types_tables](#video_types_tables) | video_type |
| audio_tracks | False | integer | True | None | None | None |
| script_ref | False | integer | True | None | [vo_scripts_tables](#vo_scripts_tables) | id |
  
## video_types_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| video_type | True | text | True | 255 | None | None |
  
## vo_campaign_agent_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| character | False | text | False | 255 | None | None |
| key | True | text | True | 255 | None | None |
| text | False | text | True | 20000 | None | None |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| subculture | True | text | False | 255 | [cultures_subcultures_tables](#cultures_subcultures_tables) | subculture |
  
## vo_characters_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| name | False | text | True | 20000 | None | None |
  
## vo_context_sensitive_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| text | False | text | True | 255 | None | None |
  
## vo_diplomacy_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| text | False | text | True | 20000 | None | None |
  
## vo_faction_intro_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| text | False | text | True | 20000 | None | None |
  
## vo_fmv_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| text | False | text | True | 20000 | None | None |
  
## vo_historical_battle_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| text | False | text | True | 20000 | None | None |
  
## vo_scripts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| id | True | integer | True | None | None | None |
| name | False | text | True | 255 | None | None |
  
## vo_speech_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| text | False | text | True | 20000 | None | None |
  
## vo_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| recorded_filename | False | text | True | 255 | None | None |
| script_id | False | integer | True | None | [vo_scripts_tables](#vo_scripts_tables) | id |
| order | False | integer | True | None | None | None |
| comment | False | text | False | 255 | None | None |
| table_field | False | integer | True | None | [TExc_LocalisableFields_tables](#TExc_LocalisableFields_tables) | key |
| foreign_key | False | text | True | 20000 | None | None |
  
## vo_text_characters_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| vo_text | True | integer | True | None | [vo_texts_tables](#vo_texts_tables) | key |
| vo_character | True | integer | True | None | [vo_characters_tables](#vo_characters_tables) | key |
  
## vo_tutorial_fmv_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| text | False | text | True | 20000 | None | None |
  
## vo_unit_texts_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| culture | True | text | False | 50 | [cultures_tables](#cultures_tables) | key |
| faction | True | text | False | 255 | [factions_tables](#factions_tables) | key |
| text | False | text | True | 20000 | None | None |
  
## warscape_animated_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| texture_filename_base | False | text | True | 255 | None | None |
| category | False | text | True | 50 | [warscape_categories_tables](#warscape_categories_tables) | key |
  
## warscape_animated_lod_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| filename | False | text | True | 255 | None | None |
| range | False | single | True | None | None | None |
| animated | False | text | True | 255 | [warscape_animated_tables](#warscape_animated_tables) | key |
  
## warscape_categories_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | False | 50 | None | None |
  
## warscape_equipment_items_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| equipment_item | False | text | True | 50 | None | None |
| equipment_key | True | text | True | 50 | None | None |
  
## warscape_rigid_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| texture_directory | False | text | True | 255 | None | None |
| category | False | text | True | 50 | [warscape_categories_tables](#warscape_categories_tables) | key |
  
## warscape_rigid_lod_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | autonumber | True | None | None | None |
| filename | False | text | True | 255 | None | None |
| range | False | text | True | 50 | None | None |
| rigid | False | text | True | 255 | [warscape_rigid_tables](#warscape_rigid_tables) | key |
  
## warscape_rigid_lod_range_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| LOD_id | True | text | False | 50 | None | None |
| range | False | integer | False | None | None | None |
  
## warscape_underlay_textures_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| underlay_key | True | text | True | 50 | None | None |
| filename | False | text | True | 50 | None | None |
| filepath | False | text | True | 50 | None | None |
| levels | False | integer | True | None | None | None |
| orientation-angle | False | integer | False | None | None | None |
| width | False | integer | False | None | None | None |
| height | False | integer | False | None | None | None |
  
## wind_levels_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 255 | None | None |
| sea_surface | False | text | True | 50 | [sea_surfaces_tables](#sea_surfaces_tables) | key |
| onscreen | False | text | True | 255 | None | None |
| magnitudeX | False | double | True | None | None | None |
| magnitudeY | False | double | True | None | None | None |
| sort_order | False | integer | False | None | None | None |
  
## _kv_experience_bonuses_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| value | False | integer | True | None | None | None |
| description | False | text | True | 536870910 | None | None |
  
## _kv_fatigue_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| value | False | integer | True | None | None | None |
| description | False | text | True | 536870910 | None | None |
  
## _kv_key_buildings_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| value | False | single | True | None | None | None |
| description | False | text | True | 536870910 | None | None |
  
## _kv_morale_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| value | False | single | True | None | None | None |
| description | False | text | True | 50 | None | None |
  
## _kv_naval_morale_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| value | False | integer | False | None | None | None |
| description | False | text | False | 50 | None | None |
  
## _kv_rules_tables

| name | primary | type | required | max_length | ref_table | ref_column |
| --- | --- | --- | --- | --- | --- | --- |
| key | True | text | True | 50 | None | None |
| value | False | decimal | True | None | None | None |
| description | False | text | False | 536870910 | None | None |