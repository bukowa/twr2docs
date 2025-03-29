---
title: schema
summary: A brief description of my document.
---

# Tables
Database schema extracted from RPFM.
Required a few scripts to setup but seems pretty usable.


  
## _kv_experience_bonuses_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| value |  | False |
  
## _kv_fatigue_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| value |  | False |
  
## _kv_key_buildings_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| value |  | False |
  
## _kv_morale_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| value |  | False |
  
## _kv_naval_morale_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| value |  | False |
  
## _kv_rules_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| value |  | False |
  
## abilities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| value |  | False |
  
## achievements_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| value |  | False |
  
## action_results_additional_outcomes_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| outcome |  | False |
| action_result_key |  | False |
| value |  | False |
| effect_record |  | False |
| effect_scope_record |  | False |
| key |  | True |
| opportune_failure_weighting |  | False |
| authority_value_coefficient | final_value = value + (authority_value_coefficient * agent.attribute_level(ATTRIBUTE_AUTHORITY) | False |
| subterfuge_value_coefficient | final_value = value + (subterfuge_value_coefficient * agent.attribute_level(ATTRIBUTE_SUBTERFUGE) | False |
| zeal_value_coefficient | final_value = value + (zeal_value_coefficient * agent.attribute_level(ATTRIBUTE_ZEAL) | False |
  
## action_results_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| outcome |  | False |
| action_result_key |  | False |
| value |  | False |
| effect_record |  | False |
| effect_scope_record |  | False |
| key |  | True |
| opportune_failure_weighting |  | False |
| authority_value_coefficient | final_value = value + (authority_value_coefficient * agent.attribute_level(ATTRIBUTE_AUTHORITY) | False |
| subterfuge_value_coefficient | final_value = value + (subterfuge_value_coefficient * agent.attribute_level(ATTRIBUTE_SUBTERFUGE) | False |
| zeal_value_coefficient | final_value = value + (zeal_value_coefficient * agent.attribute_level(ATTRIBUTE_ZEAL) | False |
  
## advice_info_texts_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| outcome |  | False |
| action_result_key |  | False |
| value |  | False |
| effect_record |  | False |
| effect_scope_record |  | False |
| key |  | True |
| opportune_failure_weighting |  | False |
| authority_value_coefficient | final_value = value + (authority_value_coefficient * agent.attribute_level(ATTRIBUTE_AUTHORITY) | False |
| subterfuge_value_coefficient | final_value = value + (subterfuge_value_coefficient * agent.attribute_level(ATTRIBUTE_SUBTERFUGE) | False |
| zeal_value_coefficient | final_value = value + (zeal_value_coefficient * agent.attribute_level(ATTRIBUTE_ZEAL) | False |
  
## advice_levels_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| advice_thread |  | False |
| advice_thread_level |  | False |
| points_needed |  | False |
| game_area |  | False |
| category |  | False |
| sub_category |  | False |
| max_repeat_count |  | False |
| repeat_interval |  | False |
| pause_battle | Does this advice pause the battle | False |
| priority_level |  | False |
| high_verbosity_only |  | False |
| locatable |  | False |
| parameter |  | False |
| on_display_script |  | False |
| on_click_script |  | False |
| suppressible |  | False |
| uninhibitable |  | False |
| audio_clip | Audio to play for this advice | False |
| advisor_name | Name of advisor, determines advisor that presents advice | False |
| for_loading_screen | Specifies whether this bit of advice text should be shown in loading screen AS WELL. | False |
| movie_link | Link to a movie url in encyclopedia to play | False |
  
## advice_threads_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| advice_thread |  | False |
| advice_thread_level |  | False |
| points_needed |  | False |
| game_area |  | False |
| category |  | False |
| sub_category |  | False |
| max_repeat_count |  | False |
| repeat_interval |  | False |
| pause_battle | Does this advice pause the battle | False |
| priority_level |  | False |
| high_verbosity_only |  | False |
| locatable |  | False |
| parameter |  | False |
| on_display_script |  | False |
| on_click_script |  | False |
| suppressible |  | False |
| uninhibitable |  | False |
| audio_clip | Audio to play for this advice | False |
| advisor_name | Name of advisor, determines advisor that presents advice | False |
| for_loading_screen | Specifies whether this bit of advice text should be shown in loading screen AS WELL. | False |
| movie_link | Link to a movie url in encyclopedia to play | False |
  
## advisors_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| advisor_name |  | True |
| advisor_icon_path | This path specifies what model will get loaded to advisor | False |
  
## agent_action_message_events_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| critical_failure |  | False |
| critical_success |  | False |
| failure |  | False |
| key |  | True |
| opportune_failure |  | False |
| success |  | False |
  
## agent_actions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| critical_failure |  | False |
| critical_success |  | False |
| failure |  | False |
| key |  | True |
| opportune_failure |  | False |
| success |  | False |
  
## agent_attributes_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## agent_culture_details_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## agent_localisations_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## agent_string_faction_overrides_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## agent_string_subculture_overrides_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## agent_subculture_gender_overrides_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| agent |  | True |
| gender |  | True |
| subculture |  | True |
  
## agent_to_agent_abilities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| agent |  | True |
| gender |  | True |
| subculture |  | True |
  
## agent_to_agent_attributes_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| attribute |  | True |
| agent |  | True |
| default_value |  | False |
  
## agent_uniforms_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| attribute |  | True |
| agent |  | True |
| default_value |  | False |
  
## agents_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| attribute |  | True |
| agent |  | True |
| default_value |  | False |
  
## aide_de_camp_speeches_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| attribute |  | True |
| agent |  | True |
| default_value |  | False |
  
## ancillaries_categories_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| attribute |  | True |
| agent |  | True |
| default_value |  | False |
  
## ancillaries_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| attribute |  | True |
| agent |  | True |
| default_value |  | False |
  
## ancillary_included_subcultures_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| ancillary |  | True |
| subculture |  | True |
  
## ancillary_info_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| ancillary |  | True |
  
## ancillary_to_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| ancillary |  | True |
| effect |  | True |
| effect_scope |  | False |
| value |  | False |
  
## ancillary_to_included_agents_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| ancillary |  | True |
| agent |  | True |
  
## ancillary_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| type |  | True |
| ui_icon |  | False |
  
## anim_reference_poses_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| path |  | False |
| root_node |  | False |
  
## animals_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| animation |  | False |
| armour |  | False |
| charge_bonus |  | False |
| entity |  | False |
| key |  | True |
| melee_attack |  | False |
| melee_defence |  | False |
  
## armed_citizenry_unit_groups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| unit_group |  | True |
  
## armed_citizenry_units_to_unit_groups_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | True |
| priority |  | False |
| unit |  | False |
| unit_group |  | False |
  
## audio_campaign_building_enums_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## audio_projectiles_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## audio_vo_actor_groups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## banditry_events_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## battle_animations_table_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| skeleton | This creates an AGF dependency. | False |
  
## battle_autoresolver_balances_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| melee_potential_multiplier |  | False |
| missile_potential_multiplier |  | False |
| source_unit_class |  | True |
| target_unit_class |  | True |
  
## battle_cameras_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| melee_potential_multiplier |  | False |
| missile_potential_multiplier |  | False |
| source_unit_class |  | True |
| target_unit_class |  | True |
  
## battle_cinematic_event_categories_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## battle_cinematic_events_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| filename | Name of camera.txt file that specifies shots to be used | False |
| key |  | True |
| level |  | False |
| priority | Priority determines if shown as important event and which shots take precedence when selecting shot | False |
| window_in | Start of window to trigger, where imagine 0 is when event happens. So if want to start playing/notifying of shot 10 seconds before happens, this should be 10. | False |
| window_out | End of window to trigger, where imagine 0 is when event happens. So if closest time can play is 5 seconds before, this should be 5. | False |
| repeat_wait_ms | After a cinematic event is played, it waits this duration until can be played again | False |
| event_category | This is the event category, so the type of event the shot gets played for | False |
| time_after_event | in seconds after trigger event | False |
  
## battle_cities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| city |  | True |
| minimum_building_scale |  | False |
| maximum_building_scale |  | False |
| town_min_distance |  | False |
| city_min_distance |  | False |
| town_radius |  | False |
| city_radius |  | False |
| number_of_town_buildings |  | False |
| number_of_city_buildings |  | False |
  
## battle_city_buildings_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building |  | True |
| city |  | False |
| amount_in_town |  | False |
| amount_in_city |  | False |
  
## battle_climate_weather_descriptions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | False |
| climate_type |  | True |
| season |  | True |
| weather_type |  | True |
| probability |  | False |
| heat_fatigue |  | False |
| cold_fatigue |  | False |
| spotting_scalar |  | False |
  
## battle_difficulty_modifiers_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| difficulty_level |  | True |
| human |  | True |
| stat |  | True |
| value |  | False |
  
## battle_entities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| difficulty_level |  | True |
| human |  | True |
| stat |  | True |
| value |  | False |
  
## battle_entity_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| difficulty_level |  | True |
| human |  | True |
| stat |  | True |
| value |  | False |
  
## battle_misc_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect |  | False |
| name |  | True |
  
## battle_personalities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect |  | False |
| name |  | True |
  
## battle_siege_vehicle_permissions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| faction |  | True |
| vehicle |  | True |
  
## battle_skeletons_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| faction |  | True |
| vehicle |  | True |
  
## battle_sky_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| season |  | False |
| weather_type |  | False |
| time_of_day |  | False |
| climate |  | False |
| sky_file |  | False |
| supports_ambient_fog |  | False |
| supports_volumetric_fog |  | False |
  
## battle_terrain_farms_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| farm |  | True |
| tile_model |  | False |
| blend_map_model |  | False |
| alternate_blend_map_model |  | False |
| road_blend_map_model |  | False |
| colour_map_model |  | False |
| alternate_colour_map_model |  | False |
| road_colour_map_model |  | False |
| grass_map_model |  | False |
| alternate_grass_map_model |  | False |
| road_grass_map_model |  | False |
| tile_map |  | False |
| wall_texture |  | False |
| wall_end |  | False |
| wall_cross_section |  | False |
  
## battle_type_setup_limits_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| battle_type |  | True |
| weighting_type |  | True |
| army_size |  | True |
| era |  | True |
| max_infantry |  | False |
| max_cavalry |  | False |
| max_artillery |  | False |
| max_small_ship |  | False |
| max_frigate |  | False |
| max_line_of_battle |  | False |
| id |  | False |
  
## battle_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| type |  | True |
| sort_order | Order put in ui | False |
| defender_funds_ratio | Ratio of funds defender gets as opposed to attacker for this battle type | False |
| max_teamsize | Maximum number of armies per alliance for this battle type | False |
  
## battle_types_to_victory_conditions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| battle_type |  | True |
| attacker_victory_condition |  | True |
| defender_victory_condition |  | True |
  
## battle_weather_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| stat |  | True |
| value |  | False |
| weather_type |  | True |
  
## battle_weather_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| stat |  | True |
| value |  | False |
| weather_type |  | True |
  
## battlefield_building_categories_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| category |  | True |
| default_destruction_effect |  | False |
| icon_path | Icon path used for any related building icons for radar, etc | False |
  
## battlefield_building_transformations_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| transformation |  | True |
  
## battlefield_buildings_names_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| onscreen_name |  | False |
| global_effects_description |  | False |
| local_effects_description |  | False |
  
## battlefield_buildings_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| onscreen_name |  | False |
| global_effects_description |  | False |
| local_effects_description |  | False |
  
## battlefield_buildings_with_projectiles_names_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building_category |  | True |
| name |  | False |
| projectile |  | True |
  
## battlefield_chariots_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| battle_entity |  | False |
| chariot_animation_table |  | False |
| chariot_type |  | False |
| destroyed_model |  | False |
| destruction_animation |  | False |
| key |  | True |
| model |  | False |
  
## battlefield_deployable_siege_items_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| battle_entity |  | False |
| chariot_animation_table |  | False |
| chariot_type |  | False |
| destroyed_model |  | False |
| destruction_animation |  | False |
| key |  | True |
| model |  | False |
  
## battlefield_engines_autonomous_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| autonomous_engine_type |  | False |
| engine_crew_anims |  | False |
| engine_crew_entity |  | False |
| key |  | True |
| num_ammo |  | False |
  
## battlefield_engines_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| autonomous_engine_type |  | False |
| engine_crew_anims |  | False |
| engine_crew_entity |  | False |
| key |  | True |
| num_ammo |  | False |
  
## battlefield_siege_vehicles_custom_battles_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| cap |  | False |
| probability |  | False |
| vehicle |  | True |
  
## battlefield_siege_vehicles_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| cap |  | False |
| probability |  | False |
| vehicle |  | True |
  
## battlefield_siege_vehicles_to_autonomous_engines_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| engine |  | True |
| vehicle |  | True |
  
## battles_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| engine |  | True |
| vehicle |  | True |
  
## battles_to_battle_sky_types_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| battle_key |  | True |
| battle_sky_type_key |  | True |
  
## bribe_actions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | False |
| name |  | False |
  
## building_chain_availabilities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| set_id |  | False |
| culture |  | False |
| faction |  | False |
| id |  | True |
| sub_culture |  | False |
| campaign |  | False |
  
## building_chain_availability_set_ids_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | True |
  
## building_chain_availability_sets_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building_chain |  | True |
| id |  | True |
  
## building_chain_to_slots_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| chain |  | True |
| slot |  | True |
  
## building_chains_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| chain |  | True |
| slot |  | True |
  
## building_culture_variants_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| chain |  | True |
| slot |  | True |
  
## building_effects_junction_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building |  | True |
| effect |  | True |
| effect_scope |  | False |
| value |  | False |
| value_damaged |  | False |
| value_ruined |  | False |
  
## building_instances_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| num_instances |  | False |
  
## building_level_armed_citizenry_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building_level |  | False |
| id |  | True |
| unit_group |  | False |
  
## building_level_required_technology_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building_level_key |  | True |
| technology_key |  | True |
  
## building_levels_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building_level_key |  | True |
| technology_key |  | True |
  
## building_set_to_building_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building_chain |  | True |
| building_level |  | True |
| building_set |  | True |
| exclude |  | False |
  
## building_sets_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building_chain |  | True |
| building_level |  | True |
| building_set |  | True |
| exclude |  | False |
  
## building_states_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## building_superchains_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## building_units_allowed_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## building_upgrades_junction_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| from |  | True |
| to |  | True |
  
## cai_agent_distribution_profiles_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cai_agent_distribution_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cai_agent_record_to_cai_agent_type_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cai_agent_recruitment_profiles_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cai_agent_recruitment_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cai_agent_type_distribution_profile_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| agent_type_key |  | True |
| distribution_profile_key |  | True |
| distribution_type_key |  | True |
  
## cai_agent_type_recruitment_profile_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| agent_type_key |  | True |
| recruitment_profile_key |  | True |
| recruitment_type_key |  | True |
  
## cai_agent_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cai_base_building_context_values_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building_key |  | True |
| economic_value |  | False |
| prestige_value |  | False |
| happiness_value |  | False |
| military_value |  | False |
| education_value |  | False |
| existing_buildings_apply_discount_over_limit |  | False |
| existing_buildings_discount_per_building |  | False |
| existing_buildings_maximum_discount |  | False |
  
## cai_construction_system_building_values_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building_chain |  | True |
| building_instance |  | True |
| building_or_building_range_start_inclusive |  | True |
| building_range_end_inclusive |  | True |
| building_super_chain |  | True |
| cai_construction_system_category |  | True |
| cai_construction_system_category_group |  | True |
| campaign |  | True |
| culture |  | True |
| faction |  | True |
| per_faction_building_limit_start |  | False |
| per_faction_building_limit_end |  | False |
| per_faction_building_minimum_discount_when_exceeding_limit_start |  | False |
| per_faction_building_maximum_discount_when_exceeding_limit_start |  | False |
| per_faction_building_minimum_discount_when_exceeding_limit_end |  | False |
| per_faction_building_maximum_discount_when_exceeding_limit_end |  | False |
| per_faction_per_building_discount_increment_when_exceeding_limit_start |  | False |
| per_faction_per_building_discount_increment_when_exceeding_limit_end |  | False |
| per_province_building_limit_start |  | False |
| per_province_building_limit_end |  | False |
| per_province_building_minimum_discount_when_exceeding_limit_start |  | False |
| per_province_building_maximum_discount_when_exceeding_limit_start |  | False |
| per_province_building_minimum_discount_when_exceeding_limit_end |  | False |
| per_province_building_maximum_discount_when_exceeding_limit_end |  | False |
| per_province_per_building_discount_increment_when_exceeding_limit_start |  | False |
| per_province_per_building_discount_increment_when_exceeding_limit_end |  | False |
| score_end_inclusive |  | False |
| score_or_score_start_inclusive |  | False |
| sub_culture |  | True |
  
## cai_construction_system_categories_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| cai_construction_system_category_group |  | False |
| cdir_military_generator_unit_group |  | False |
| key |  | True |
  
## cai_construction_system_category_groups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cai_construction_system_province_template_assignment_policies_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cai_construction_system_strategic_context_template_policies_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| default_cai_construction_system_template |  | False |
| key |  | True |
  
## cai_construction_system_strategic_context_template_policy_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| cai_construction_system_strategic_context_policy |  | True |
| cai_construction_system_template |  | True |
| cai_strategic_context |  | True |
  
## cai_construction_system_superchain_hints_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| economic_specialisation_recommended |  | False |
| military_specialisation_recommended |  | False |
| super_chain_key |  | True |
  
## cai_construction_system_synergies_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| economic_specialisation_recommended |  | False |
| military_specialisation_recommended |  | False |
| super_chain_key |  | True |
  
## cai_construction_system_synergy_levels_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| absolute_effect |  | False |
| key |  | True |
| priority |  | False |
| relative_effect |  | False |
  
## cai_construction_system_synergy_policies_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cai_construction_system_templates_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| cai_construction_system_category |  | True |
| cai_construction_system_category_group |  | True |
| cai_construction_system_template |  | True |
| value |  | False |
  
## cai_construction_system_templates_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| default_category_and_group_value |  | False |
| key |  | True |
  
## cai_diplomacy_complex_treacheries_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| first_event |  | True |
| max_turn_difference |  | False |
| second_event |  | True |
| value |  | False |
  
## cai_diplomacy_simple_treacheries_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| event |  | True |
| value |  | False |
  
## cai_military_aggressiveness_policies_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| event |  | True |
| value |  | False |
  
## cai_military_behaviour_policies_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cai_personalities_budget_allocation_policy_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cai_personalities_budget_allocations_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| agents_funding_cap |  | False |
| agents_funds_allocation_percentage |  | False |
| agents_percentage_of_pool_to_save_on_fail |  | False |
| agents_turns_of_inactivity_until_cap |  | False |
| army_funding_cap |  | False |
| army_funds_allocation_percentage |  | False |
| army_percentage_of_pool_to_save_on_fail |  | False |
| army_turns_of_inactivity_until_cap |  | False |
| construction_funding_cap |  | False |
| construction_funds_allocation_percentage |  | False |
| construction_percentage_of_pool_to_save_on_fail |  | False |
| construction_turns_of_inactivity_until_cap |  | False |
| diplomacy_funding_cap |  | False |
| diplomacy_funds_allocation_percentage |  | False |
| diplomacy_percentage_of_pool_to_save_on_fail |  | False |
| diplomacy_turns_of_inactivity_until_cap |  | False |
| key |  | True |
| navy_funding_cap |  | False |
| navy_funds_allocation_percentage |  | False |
| navy_percentage_of_pool_to_save_on_fail |  | False |
| navy_turns_of_inactivity_until_cap |  | False |
| minimum_settable_tax_level |  | False |
| maximum_settable_tax_level |  | False |
| technology_funds_allocation_percentage |  | False |
| technology_turns_of_inactivity_until_cap |  | False |
| technology_funding_cap |  | False |
| technology_percentage_of_pool_to_save_on_fail |  | False |
  
## cai_personalities_budget_policies_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| agents_funding_cap |  | False |
| agents_funds_allocation_percentage |  | False |
| agents_percentage_of_pool_to_save_on_fail |  | False |
| agents_turns_of_inactivity_until_cap |  | False |
| army_funding_cap |  | False |
| army_funds_allocation_percentage |  | False |
| army_percentage_of_pool_to_save_on_fail |  | False |
| army_turns_of_inactivity_until_cap |  | False |
| construction_funding_cap |  | False |
| construction_funds_allocation_percentage |  | False |
| construction_percentage_of_pool_to_save_on_fail |  | False |
| construction_turns_of_inactivity_until_cap |  | False |
| diplomacy_funding_cap |  | False |
| diplomacy_funds_allocation_percentage |  | False |
| diplomacy_percentage_of_pool_to_save_on_fail |  | False |
| diplomacy_turns_of_inactivity_until_cap |  | False |
| key |  | True |
| navy_funding_cap |  | False |
| navy_funds_allocation_percentage |  | False |
| navy_percentage_of_pool_to_save_on_fail |  | False |
| navy_turns_of_inactivity_until_cap |  | False |
| minimum_settable_tax_level |  | False |
| maximum_settable_tax_level |  | False |
| technology_funds_allocation_percentage |  | False |
| technology_turns_of_inactivity_until_cap |  | False |
| technology_funding_cap |  | False |
| technology_percentage_of_pool_to_save_on_fail |  | False |
  
## cai_personalities_construction_preference_policies_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cai_personalities_construction_system_policies_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building_synergies_policy |  | False |
| key |  | True |
| province_specialisation_template_assignment_policy |  | False |
| strategic_context_template_assignment_policy |  | False |
  
## cai_personalities_income_allocation_policies_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building_synergies_policy |  | False |
| key |  | True |
| province_specialisation_template_assignment_policy |  | False |
| strategic_context_template_assignment_policy |  | False |
  
## cai_personalities_income_allocation_policy_strategic_context_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building_synergies_policy |  | False |
| key |  | True |
| province_specialisation_template_assignment_policy |  | False |
| strategic_context_template_assignment_policy |  | False |
  
## cai_personalities_random_group_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| personality_key |  | True |
| random_personality_group_key |  | True |
  
## cai_personalities_random_groups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| random_personality_group_key |  | True |
  
## cai_personalities_randomisation_policies_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| randomisation_policy_key |  | True |
  
## cai_personalities_reliability_policies_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| randomisation_policy_key |  | True |
  
## cai_personalities_religious_conversion_policies_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cai_personalities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cai_personalities_task_management_system_task_generator_profiles_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cai_personality_cultural_components_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cai_personality_cultural_multipliers_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| component_id |  | True |
| negative_attitude_multiplier |  | False |
| positive_attitude_multiplier |  | False |
| source |  | True |
| target |  | True |
| attitude_base |  | False |
  
## cai_personality_deal_evaluation_component_overrides_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| component |  | True |
| parent |  | False |
  
## cai_personality_deal_evaluation_components_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| component |  | True |
| parent |  | False |
  
## cai_personality_deal_evaluation_deal_component_names_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | True |
  
## cai_personality_deal_evaluation_deal_component_values_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | True |
  
## cai_personality_deal_generation_components_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | True |
  
## cai_personality_deal_generation_generator_priorities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| component_key |  | True |
| generator_key |  | True |
| last_stand_priority |  | False |
| param1 |  | False |
| param2 |  | False |
| param3 |  | False |
| param4 |  | False |
| peace_priority |  | False |
| tension_priority |  | False |
| war_priority |  | False |
| total_war_priority |  | False |
| failure_timeout |  | False |
| min_payment_cap |  | False |
| max_payment_cap |  | False |
| max_payment_pct |  | False |
  
## cai_personality_deal_generation_generators_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | True |
  
## cai_personality_diplomatic_component_overrides_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| component |  | True |
| parent |  | False |
  
## cai_personality_diplomatic_components_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| component |  | True |
| parent |  | False |
  
## cai_personality_diplomatic_event_values_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| component_id |  | True |
| event_id |  | True |
| falloff |  | False |
| value |  | False |
  
## cai_personality_diplomatic_events_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | True |
| diplomatic_factor_group_active |  | False |
| diplomatic_factor_group_inactive |  | False |
  
## cai_personality_diplomatic_treaty_values_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | True |
| diplomatic_factor_group_active |  | False |
| diplomatic_factor_group_inactive |  | False |
  
## cai_personality_negotiation_components_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | True |
| diplomatic_factor_group_active |  | False |
| diplomatic_factor_group_inactive |  | False |
  
## cai_personality_occupation_decision_components_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | True |
| diplomatic_factor_group_active |  | False |
| diplomatic_factor_group_inactive |  | False |
  
## cai_personality_occupation_decision_priorities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | True |
| diplomatic_factor_group_active |  | False |
| diplomatic_factor_group_inactive |  | False |
  
## cai_personality_strategic_components_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | True |
| diplomatic_factor_group_active |  | False |
| diplomatic_factor_group_inactive |  | False |
  
## cai_personality_strategic_desired_attitudes_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| best_friends_attitude |  | False |
| best_friends_positive_factor |  | False |
| bitter_enemies_attitude |  | False |
| bitter_enemies_positive_factor |  | False |
| friendly_attitude |  | False |
| friendly_positive_factor |  | False |
| neutral_attitude |  | False |
| neutral_positive_factor |  | False |
| strategic_component |  | True |
| unfriendly_attitude |  | False |
| unfriendly_positive_factor |  | False |
| very_friendly_attitude |  | False |
| very_friendly_positive_factor |  | False |
| very_unfriendly_attitude |  | False |
| very_unfriendly_positive_factor |  | False |
| best_friends_negative_factor |  | False |
| very_friendly_negative_factor |  | False |
| friendly_negative_factor |  | False |
| neutral_negative_factor |  | False |
| unfriendly_negative_factor |  | False |
| very_unfriendly_negative_factor |  | False |
| bitter_enemies_negative_factor |  | False |
  
## cai_personality_strategic_resource_values_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| trade_falloff |  | False |
| trade_value |  | False |
| resource |  | True |
| strategic_component |  | True |
| ownership_falloff |  | False |
| ownership_value |  | False |
  
## cai_siege_strength_modifiers_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| defence_strength_modifier |  | False |
| assault_strength_modifier |  | False |
| subculture |  | True |
  
## cai_strategic_context_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cai_task_management_system_task_generator_groups_generators_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| priority | Priority of the generator within the group. Generally scalled between 0.0 and 1.0 | False |
| task_generator_group_key |  | True |
| task_generator_key |  | True |
  
## cai_task_management_system_task_generator_groups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key | The name of the Task Generator Group | True |
  
## cai_task_management_system_task_generators_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key | The DB name of this CAI Task Management System Task Genertaor | True |
  
## cai_variables_overides_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| cai_variable_key | Campaign AI Variable to override | True |
| campaign_key | Campaign Key | True |
| optional_campaign_type | (Optional) Long/Short | True |
| optional_difficulty_level | (Optional) Integer value campaign difficulty | True |
| value | Override value | False |
  
## cai_variables_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key | Campaign AI Control Variable Key | True |
| value | Campaign AI Control Variable Base Value | False |
| description | Campaign AI Variable Description | False |
  
## campaign_ai_character_skill_tree_distribution_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| distribution_key |  | True |
| agent_manager_key |  | True |
| priority |  | False |
  
## campaign_ai_character_skill_tree_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| agent_manager_key |  | True |
| priority |  | False |
| skill_key |  | True |
  
## campaign_ai_character_skill_tree_manager_agent_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| agent_key |  | True |
| agent_manager_key |  | False |
| manager_key |  | True |
  
## campaign_ai_manager_behaviour_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| manager |  | True |
| behaviour |  | True |
| priority |  | False |
  
## campaign_ai_managers_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| manager |  | True |
  
## campaign_ai_personalities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| personality |  | True |
| is_default |  | False |
  
## campaign_ai_personality_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| personality |  | True |
| property |  | True |
| property_value |  | False |
  
## campaign_ai_technology_manager_path_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| manager_key |  | True |
| path_key |  | True |
| priority |  | False |
  
## campaign_ai_technology_managers_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## campaign_ai_technology_path_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| path_key |  | True |
| priority |  | False |
| technology_key |  | True |
  
## campaign_ambush_ground_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| ambush_chance_of_success |  | False |
| key |  | True |
  
## campaign_autoresolver_battle_situations_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| ambush_chance_of_success |  | False |
| key |  | True |
  
## campaign_autoresolver_mod_group_modifier_values_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| group_id |  | False |
| id |  | True |
| modification_id |  | False |
| value |  | False |
  
## campaign_autoresolver_mod_group_targets_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| alliance_target |  | False |
| id |  | True |
| mechanic_target |  | False |
| player_target |  | False |
  
## campaign_autoresolver_mod_groups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | True |
  
## campaign_autoresolver_modifiers_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| class |  | False |
| id |  | True |
| stat_variable_id |  | False |
| vs_class |  | False |
  
## campaign_autoresolver_situation_mod_groups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| group_id |  | False |
| group_target_id |  | False |
| id |  | True |
| situation_id |  | False |
  
## campaign_autoresolver_stat_variables_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| description |  | False |
| id |  | True |
  
## campaign_battle_presets_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| description |  | False |
| id |  | True |
  
## campaign_bonus_value_battle_context_battle_type_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| battle_context_key |  | True |
| battle_type_key |  | True |
  
## campaign_bonus_value_battle_context_culture_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| battle_context_key |  | True |
| culture_key |  | True |
  
## campaign_bonus_value_battle_context_faction_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| battle_context_key |  | True |
| faction_key |  | True |
  
## campaign_bonus_value_battle_context_force_status_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| battle_context_key |  | True |
| force_status_key |  | True |
| is_yours |  | False |
  
## campaign_bonus_value_battle_context_ground_type_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| battle_context_key |  | True |
| ground_type_key |  | True |
  
## campaign_bonus_value_battle_context_specifiers_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| night_battles_only |  | False |
  
## campaign_bonus_value_battle_context_territory_status_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| battle_context_key |  | True |
| territory_status_key |  | True |
  
## campaign_character_art_sets_campaign_groups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## campaign_character_art_sets_group_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign |  | True |
| group |  | True |
  
## campaign_character_art_sets_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign |  | True |
| group |  | True |
  
## campaign_character_arts_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign |  | True |
| group |  | True |
  
## campaign_character_attribute_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| agent_record |  | True |
| attribute_level |  | True |
| attribute_record |  | True |
| culture_record |  | True |
| effect_record |  | True |
| effect_scope |  | True |
| effect_value |  | False |
| faction_record |  | True |
| subculture_record |  | True |
| campaign_record |  | True |
  
## campaign_difficulty_handicap_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign_difficulty_handicap |  | True |
| human |  | True |
| effect |  | True |
| effect_scope |  | False |
| effect_value |  | False |
| optional_campaign_key |  | False |
  
## campaign_effect_scope_agent_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| agent_key |  | True |
| campaign_effect_scope_key |  | True |
  
## campaign_effect_scope_character_force_relationship_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign_effect_scope_key |  | True |
| force_relationship_key |  | True |
  
## campaign_effect_scopes_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign_effect_scope_key |  | True |
| force_relationship_key |  | True |
  
## campaign_ground_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign_effect_scope_key |  | True |
| force_relationship_key |  | True |
  
## campaign_map_attrition_damages_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign_effect_scope_key |  | True |
| force_relationship_key |  | True |
  
## campaign_map_attrition_faction_immunities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| attrition |  | True |
| faction |  | True |
  
## campaign_map_attrition_unit_immunities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| attrition |  | True |
| unit |  | True |
  
## campaign_map_attritions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| attrition |  | True |
| unit |  | True |
  
## campaign_map_playable_areas_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| attrition |  | True |
| unit |  | True |
  
## campaign_map_regions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign_map |  | True |
| region |  | True |
  
## campaign_map_roads_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign |  | False |
| key |  | True |
| movement_cost |  | False |
| threshold |  | False |
| turns_required_to_upgrade_to |  | False |
| turns_required_to_downgrade_from |  | False |
  
## campaign_map_settlements_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign |  | False |
| key |  | True |
| movement_cost |  | False |
| threshold |  | False |
| turns_required_to_upgrade_to |  | False |
| turns_required_to_downgrade_from |  | False |
  
## campaign_map_tooltips_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| select_context |  | True |
| over_context |  | True |
| tooltip_line |  | False |
| advice_line |  | False |
| main_line | first line in the tooltip | False |
  
## campaign_mp_coop_groups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## campaign_mp_coop_groups_to_factions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| faction_key | A faction to be added to a Multiplayer Coop Group | True |
| mp_coop_group | The Multiplayer Coop Group to which the specified faction belongs. | True |
  
## campaign_politics_strings_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## campaign_public_order_populace_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| culture |  | True |
| effect_bundle |  | False |
| populace_happiness |  | True |
  
## campaign_settlement_display_aqueducts_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building_path |  | False |
| position_x_map |  | False |
| position_y_map |  | False |
| position_z_height |  | False |
| region_key |  | True |
| rotation_cw_radians |  | False |
  
## campaign_settlement_display_building_constructions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building_path |  | False |
| position_x_map |  | False |
| position_y_map |  | False |
| position_z_height |  | False |
| region_key |  | True |
| rotation_cw_radians |  | False |
  
## campaign_settlement_display_building_ids_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building_path |  | False |
| position_x_map |  | False |
| position_y_map |  | False |
| position_z_height |  | False |
| region_key |  | True |
| rotation_cw_radians |  | False |
  
## campaign_settlement_display_building_trees_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| rigid_lookup_key |  | False |
| building_path |  | False |
| climate_type |  | False |
| id |  | True |
  
## campaign_settlement_display_buildings_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| rigid_lookup_key |  | False |
| building_path |  | False |
| climate_type |  | False |
| id |  | True |
  
## campaign_settlement_display_siege_item_ids_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| battlefield_deployable_siege_item |  | True |
| sprawl_piece |  | False |
  
## campaign_settlement_display_sprawl_pieces_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## campaign_stance_effects_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## campaign_stances_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## campaign_statistics_categories_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| category_order |  | False |
| key |  | True |
  
## campaign_statistics_strings_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign_statistic |  | True |
| campaign_statistic_category |  | False |
| statistic_order |  | False |
  
## campaign_subject_evolutions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| arrival_message |  | False |
| campaign_subject_key |  | False |
| departure_message |  | False |
| effect_bundle_key |  | False |
| flavour_text |  | False |
| key |  | True |
| max_turns |  | False |
| min_turns |  | False |
| weighting |  | False |
  
## campaign_subject_faction_restriction_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign_subject_key |  | True |
| faction_key |  | True |
  
## campaign_subject_messages_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| message_type |  | False |
  
## campaign_subject_strings_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## campaign_subjects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| flavour_text |  | False |
| key |  | True |
| male |  | False |
| optional_name |  | False |
| optional_name_source_faction |  | False |
| ui_image |  | False |
  
## campaign_unit_stat_bonuses_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| bonus |  | True |
| icon_path |  | False |
| level |  | True |
| threshold |  | False |
| upgrade_cost_new |  | False |
| upgrade_cost_from_previous_level |  | False |
  
## campaign_variables_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| variable_key |  | True |
| value |  | False |
  
## campaign_vfx_descriptions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| variable_key |  | True |
| value |  | False |
  
## campaign_vfx_lookups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| agent_filter |  | False |
| culture_filter |  | False |
| faction_filter |  | False |
| key |  | True |
| vfx_description |  | False |
| vfx_event |  | False |
  
## campaigns_campaign_variables_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| variable_key |  | True |
| campaign_name |  | True |
| value |  | False |
| optional_difficulty_level |  | True |
| optional_campaign_type |  | True |
  
## campaigns_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign_name |  | True |
| map_name |  | False |
| is_grand |  | False |
| campaign_order |  | False |
| exportable |  | False |
| display_location |  | False |
| is_tutorial |  | False |
| banner_icon |  | False |
| banner_image |  | False |
| available_for_mp |  | False |
| mp_sort_order | Sort order for MPC selection drop down | False |
  
## capture_point_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign_name |  | True |
| map_name |  | False |
| is_grand |  | False |
| campaign_order |  | False |
| exportable |  | False |
| display_location |  | False |
| is_tutorial |  | False |
| banner_icon |  | False |
| banner_image |  | False |
| available_for_mp |  | False |
| mp_sort_order | Sort order for MPC selection drop down | False |
  
## cdir_army_template_ratios_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| ratio |  | False |
| template |  | True |
| unit |  | True |
  
## cdir_campaign_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| campaign |  | False |
  
## cdir_configs_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign_key |  | True |
| faction_key |  | True |
| cdir_config_key |  | True |
| value |  | False |
  
## cdir_desire_priorities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign_key |  | True |
| desire_key |  | True |
| priority |  | False |
  
## cdir_events_dilemma_choice_details_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| choice_key |  | True |
| dilemma_key |  | True |
  
## cdir_events_dilemma_followup_dilemmas_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| choice_key |  | True |
| dilemma_key |  | True |
| followup_dilemma_key |  | True |
  
## cdir_events_dilemma_followup_missions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| dilemma_key |  | True |
| choice_key |  | True |
| followup_mission_key |  | True |
  
## cdir_events_dilemma_incidents_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| choice_key |  | True |
| dilemma_key |  | True |
| incident_key |  | True |
  
## cdir_events_dilemma_option_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| choice_key |  | True |
| dilemma_key |  | True |
| incident_key |  | True |
  
## cdir_events_dilemma_payloads_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| choice_key |  | False |
| dilemma_key |  | False |
| id |  | True |
| payload_key |  | False |
| value |  | False |
  
## cdir_events_incident_followup_dilemmas_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| incident_key |  | True |
| followup_dliemma_key |  | True |
  
## cdir_events_incident_followup_incidents_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| incident_key |  | True |
| followup_incident_key |  | True |
  
## cdir_events_incident_followup_missions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| incident_key |  | True |
| followup_mission_key |  | True |
  
## cdir_events_incident_option_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| incident_key |  | True |
| followup_mission_key |  | True |
  
## cdir_events_incident_payloads_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| incident_key |  | True |
| followup_mission_key |  | True |
  
## cdir_events_mission_followup_dilemmas_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| mission_key |  | True |
| status_key |  | True |
| followup_dilemma_key |  | True |
  
## cdir_events_mission_followup_missions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| mission_key |  | True |
| status_key |  | True |
| followup_mission_key |  | True |
  
## cdir_events_mission_incidents_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| incident_key |  | True |
| mission_key |  | True |
| status_key |  | True |
  
## cdir_events_mission_issuer_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| issuer_key |  | True |
| mission_key |  | True |
  
## cdir_events_mission_option_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| issuer_key |  | True |
| mission_key |  | True |
  
## cdir_events_mission_payloads_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | True |
| mission_key |  | False |
| payload_key |  | False |
| status_key |  | False |
| value |  | False |
  
## cdir_events_payloads_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect_bundle_key |  | False |
| payload_key |  | True |
  
## cdir_faction_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| faction |  | False |
  
## cdir_military_generator_configs_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cdir_military_generator_template_priorities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| config_key |  | True |
| priority |  | False |
| template_key |  | True |
  
## cdir_military_generator_template_ratios_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| ratio |  | False |
| template_key |  | True |
| unit_group_key |  | True |
  
## cdir_military_generator_templates_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cdir_military_generator_unit_groups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## cdir_military_generator_unit_qualities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| group_key |  | True |
| quality |  | False |
| unit_key |  | True |
  
## cdir_unit_balance_group_qualities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| config_key |  | False |
| group_key |  | False |
| quality_group_key |  | False |
| quality |  | False |
  
## cdir_unit_balance_groups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | False |
| army |  | False |
  
## cdir_unit_balance_template_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| config_key |  | False |
| template_key |  | False |
| priority |  | False |
  
## cdir_unit_balances_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| template_key |  | False |
| min_units |  | False |
| max_units |  | False |
| group_key |  | False |
| ideal_pct |  | False |
| variance |  | False |
| min_required |  | False |
  
## cdir_unit_qualities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| config_key |  | False |
| group_key |  | False |
| unit_key |  | False |
| quality |  | False |
  
## centralised_upgrade_building_level_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| upgraded_building_level | The level to which the dependent buildings will be upgraded. | True |
| central_building_level | The required level of the central building. | False |
| priority | Used when more than one central building is in effect. | True |
  
## character_experience_skill_tiers_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| agent_key |  | True |
| experience_threshold |  | False |
| skill_points |  | False |
| skill_rank |  | True |
| optional_campaign_key |  | True |
| for_army |  | True |
| for_navy |  | True |
  
## character_skill_level_details_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign_key |  | True |
| faction_key |  | True |
| image_path |  | False |
| level |  | True |
| skill_key |  | True |
| subculture_key |  | True |
| unlocked_at_rank |  | False |
  
## character_skill_level_to_effects_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| character_skill_key |  | True |
| effect_key |  | True |
| effect_scope |  | False |
| level |  | True |
| value |  | False |
  
## character_skill_node_links_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| character_skill_key |  | True |
| effect_key |  | True |
| effect_scope |  | False |
| level |  | True |
| value |  | False |
  
## character_skill_node_sets_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| character_skill_key |  | True |
| effect_key |  | True |
| effect_scope |  | False |
| level |  | True |
| value |  | False |
  
## character_skill_nodes_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| character_skill_key |  | True |
| effect_key |  | True |
| effect_scope |  | False |
| level |  | True |
| value |  | False |
  
## character_skills_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| character_skill_key |  | True |
| effect_key |  | True |
| effect_scope |  | False |
| level |  | True |
| value |  | False |
  
## character_trait_levels_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| character_skill_key |  | True |
| effect_key |  | True |
| effect_scope |  | False |
| level |  | True |
| value |  | False |
  
## character_traits_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| character_skill_key |  | True |
| effect_key |  | True |
| effect_scope |  | False |
| level |  | True |
| value |  | False |
  
## chariot_types_enums_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## chat_shortcuts_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| game_area |  | False |
| key |  | True |
  
## climates_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| game_area |  | False |
| key |  | True |
  
## commander_unit_permissions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| culture_key |  | True |
| faction_key |  | True |
| subculture_key |  | True |
| unit_key |  | True |
  
## commodities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| culture_key |  | True |
| faction_key |  | True |
| subculture_key |  | True |
| unit_key |  | True |
  
## commodity_unit_names_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| unit |  | True |
  
## culture_settlement_occupation_options_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| unit |  | True |
  
## culture_subculture_character_portraits_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| culture |  | True |
| faction |  | True |
| path |  | False |
| portrait_type |  | True |
| subculture |  | True |
  
## culture_subculture_politics_government_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| culture |  | True |
| government_type |  | True |
| on_screen_name_faction_leader |  | False |
| on_screen_name_government_type |  | False |
| faction |  | True |
| effect_bundle |  | False |
| is_default |  | False |
| faction_leader_trait |  | False |
| on_screen_name_faction_female_leader |  | False |
| faction_leader_trait_female |  | False |
| on_screen_name_government_actions |  | False |
| on_screen_descr_government_actions |  | False |
  
## cultures_subcultures_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| culture |  | True |
| government_type |  | True |
| on_screen_name_faction_leader |  | False |
| on_screen_name_government_type |  | False |
| faction |  | True |
| effect_bundle |  | False |
| is_default |  | False |
| faction_leader_trait |  | False |
| on_screen_name_faction_female_leader |  | False |
| faction_leader_trait_female |  | False |
| on_screen_name_government_actions |  | False |
| on_screen_descr_government_actions |  | False |
  
## cultures_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| culture |  | True |
| government_type |  | True |
| on_screen_name_faction_leader |  | False |
| on_screen_name_government_type |  | False |
| faction |  | True |
| effect_bundle |  | False |
| is_default |  | False |
| faction_leader_trait |  | False |
| on_screen_name_faction_female_leader |  | False |
| faction_leader_trait_female |  | False |
| on_screen_name_government_actions |  | False |
| on_screen_descr_government_actions |  | False |
  
## cursor_transitions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| initiating_cursor |  | True |
| mouse_event | Event that triggers transition | True |
| resulting_cursor |  | False |
  
## cursors_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| initiating_cursor |  | True |
| mouse_event | Event that triggers transition | True |
| resulting_cursor |  | False |
  
## cursus_honorum_level_requirements_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| age |  | False |
| level |  | True |
| rank |  | False |
| subculture_key |  | True |
| faction_key |  | True |
  
## cursus_honorum_trait_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| subculture_key |  | True |
| trait_info_key |  | True |
| faction_key |  | True |
| trait_info_key_female |  | True |
  
## death_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| subculture_key |  | True |
| trait_info_key |  | True |
| faction_key |  | True |
| trait_info_key_female |  | True |
  
## deployables_custom_battles_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| cap |  | False |
| deployable |  | True |
| probability |  | False |
  
## deployables_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| cap |  | False |
| deployable |  | True |
| probability |  | False |
  
## dilemma_to_campaign_subject_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign_subject_key |  | True |
| dilemma_key |  | True |
| weighting |  | False |
  
## dilemmas_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign_subject_key |  | True |
| dilemma_key |  | True |
| weighting |  | False |
  
## diplomacy_current_treaties_to_diplomatic_options_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| can_be_cancelled |  | False |
| current_treaty_key |  | True |
| diplomatic_option_key |  | False |
  
## diplomacy_keys_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## diplomacy_negotiation_attitude_override_strings_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| attitude |  | True |
| culture |  | True |
| government_type |  | True |
| key |  | True |
| option |  | True |
| string |  | False |
  
## diplomacy_negotiation_attitudes_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| maximum_attitude |  | False |
| minimum_attitude |  | False |
  
## diplomacy_negotiation_faction_attitude_override_strings_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| attitude |  | True |
| culture |  | True |
| faction |  | True |
| government_type |  | True |
| key |  | True |
| option |  | True |
| string |  | False |
  
## diplomacy_negotiation_faction_override_strings_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| culture |  | True |
| government_type |  | True |
| faction |  | True |
| string |  | False |
| option |  | True |
  
## diplomacy_negotiation_string_options_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| culture |  | True |
| government_type |  | True |
| faction |  | True |
| string |  | False |
| option |  | True |
  
## diplomacy_negotiation_strings_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| culture |  | True |
| government_type |  | True |
| key |  | True |
  
## diplomacy_strings_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## diplomatic_action_faction_restrictions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| can_make_client_states |  | False |
| can_make_confederations |  | False |
| can_make_vassals |  | False |
| faction |  | True |
  
## diplomatic_action_subculture_restrictions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| can_make_client_states |  | False |
| can_make_confederations |  | False |
| can_make_vassals |  | False |
| subculture |  | True |
  
## diplomatic_relations_attitudes_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| attitude |  | True |
| value |  | False |
  
## diplomatic_relations_religion_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| attitude |  | True |
| value |  | False |
  
## effect_bonus_value_agent_junction_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect |  | True |
| bonus_value_id |  | True |
| agent |  | True |
  
## effect_bonus_value_basic_junction_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect |  | True |
| bonus_value_id |  | True |
  
## effect_bonus_value_battle_context_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| battle_context_key |  | False |
| bonus_value_id |  | True |
| effect_key |  | True |
  
## effect_bonus_value_battlefield_deployables_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| battlefield_deployable |  | True |
| bonus_value_id |  | True |
| effect |  | True |
  
## effect_bonus_value_building_chain_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect |  | True |
| bonus_value_id |  | True |
| building_chain |  | True |
  
## effect_bonus_value_building_set_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| bonus_value_id |  | True |
| building_set |  | True |
| effect |  | True |
  
## effect_bonus_value_id_action_results_additional_outcomes_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| action_results_additional_outcome_record |  | True |
| bonus_value_id |  | True |
| effect |  | True |
  
## effect_bonus_value_ids_unit_sets_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| bonus_value_id |  | True |
| effect |  | True |
| unit_set |  | True |
  
## effect_bonus_value_projectile_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect |  | True |
| bonus_value |  | True |
| projectile |  | True |
  
## effect_bonus_value_provincial_initiative_effect_record_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| bonus_value_id |  | True |
| effect |  | True |
| effect_bonus_will_modify |  | True |
  
## effect_bonus_value_religion_junction_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect |  | True |
| bonus_value_id |  | True |
| religion |  | True |
  
## effect_bonus_value_resource_junction_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect |  | True |
| bonus_value_id |  | True |
| resource |  | True |
  
## effect_bonus_value_siege_item_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| bonus_value_id |  | True |
| effect |  | True |
| siege_item |  | True |
  
## effect_bonus_value_technology_category_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| bonus_value_id |  | True |
| effect |  | True |
| technology_category |  | True |
  
## effect_bonus_value_unit_ability_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect |  | True |
| bonus_value_id |  | True |
| unit_ability |  | True |
  
## effect_bonus_value_unit_caste_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| bonus_value_id |  | True |
| caste |  | True |
| effect |  | True |
  
## effect_bonus_value_unit_category_junction_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect |  | True |
| bonus_value_id |  | True |
| unit_category |  | True |
  
## effect_bonus_value_unit_class_junction_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect |  | True |
| bonus_value_id |  | True |
| unit_class |  | True |
  
## effect_bonus_value_unit_record_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| bonus_value_id |  | True |
| effect |  | True |
| unit_record_key |  | True |
  
## effect_bundle_advancement_stages_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## effect_bundles_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| localised_description |  | False |
| localised_title |  | False |
| ui_icon |  | False |
| bundle_target |  | False |
  
## effect_bundles_to_effects_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect_bundle_key |  | True |
| effect_key |  | True |
| effect_scope |  | False |
| value |  | False |
| advancement_stage |  | False |
  
## effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect_bundle_key |  | True |
| effect_key |  | True |
| effect_scope |  | False |
| value |  | False |
| advancement_stage |  | False |
  
## encyclopedia_blocks_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| block_key |  | True |
| class |  | False |
| image |  | False |
| image_class |  | False |
| order |  | False |
| page_key |  | False |
  
## encyclopedia_building_redirects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building |  | True |
| redirect_building | building to redirect the user to if 'building' was clicked on | False |
  
## encyclopedia_page_linkages_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| next_key |  | False |
| page_key |  | True |
| parent_key |  | False |
  
## encyclopedia_page_related_links_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| page_key |  | True |
| target |  | True |
  
## encyclopedia_pages_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| page_key |  | True |
| template |  | False |
  
## encyclopedia_template_strings_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| string_key |  | True |
  
## encyclopedia_unit_redirects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| redirect_unit |  | False |
| unit |  | True |
  
## entity_training_levels_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| training_level |  | True |
| max_offset_distance |  | False |
  
## event_log_descriptions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| event_key |  | True |
| optional_campaign_key |  | False |
| has_position |  | False |
| icon |  | False |
| is_region_position |  | False |
| movie_id |  | False |
  
## experience_triggers_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| event_key |  | True |
| optional_campaign_key |  | False |
| has_position |  | False |
| icon |  | False |
| is_region_position |  | False |
| movie_id |  | False |
  
## faction_banners_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| primary_blue |  | False |
| primary_green |  | False |
| primary_red |  | False |
| secondary_blue |  | False |
| secondary_green |  | False |
| secondary_red |  | False |
| symbol |  | False |
| tertiary_blue |  | False |
| tertiary_green |  | False |
| tertiary_red |  | False |
  
## faction_civil_war_setups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| primary_faction |  | True |
| secondary_faction |  | False |
| secessionist_faction |  | False |
  
## faction_groups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| primary_faction |  | True |
| secondary_faction |  | False |
| secessionist_faction |  | False |
  
## faction_political_parties_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| faction_key |  | False |
| political_party_key |  | True |
  
## faction_politics_government_actions_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| description |  | False |
| faction | The faction for which this action is defined. | True |
| id | An id for the action. Will be passed to lua for TRIGGER_EVENT-type actions. | True |
| image_path |  | False |
| title |  | False |
| type | One of the hardcoded action types. | True |
| cost | Fixed cost in gold for this action. | False |
| cost_per_region | Cost per owned region, used to make the action more expensive for large factions. | False |
| cooldown | Cooldown in turns. The cooldown counter is shared for all actions. | False |
  
## faction_rebellion_units_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| faction_key |  | True |
| unit_key |  | True |
  
## faction_resource_consumptions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| number_of_regions |  | True |
| resource_consumption |  | False |
  
## faction_to_campaign_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign |  | False |
| faction |  | True |
  
## faction_to_faction_groups_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| faction_group_key |  | False |
| faction_key |  | True |
  
## faction_to_mercenary_set_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| faction |  | True |
| mercenary_set |  | True |
  
## faction_uniform_colours_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| faction |  | True |
| mercenary_set |  | True |
  
## faction_variables_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| description |  | False |
| faction_variable_key |  | True |
| value |  | False |
  
## factions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| description |  | False |
| faction_variable_key |  | True |
| value |  | False |
  
## fame_levels_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| description |  | False |
| faction_variable_key |  | True |
| value |  | False |
  
## family_relationship_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| relationship_type |  | True |
  
## famous_battle_pools_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| relationship_type |  | True |
  
## female_character_culture_details_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| chance_to_spawn | values: (>= 0) - chance to spawn female character (in percent). If not set (value < 0) -> the value is read from female_character_faction_spawn_rates. | False |
| culture |  | True |
| general | values: ("y" / "n") - the ability to "raise a force" from a settlement. | False |
| public_office | values: ("y" / "n") - access to the "Secure Promotion" action, as well as the ability to be faction and party leader. | False |
| missions | values: ("y" / "n") - access to any and all actions listed as missions (Diplomat, Administrator, Organize Feast + the new Political Marriage, Diplomatic Marriage, Dynastic Marriage). | False |
| trait | special trait gives females bonus to missions. | False |
  
## female_character_faction_details_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| chance_to_spawn | values: (>= 0) - chance to spawn female character (in percent). If not set (value < 0) -> the value is read from female_character_subculture_details | False |
| faction |  | True |
| general | values: ("y" / "n" / not set ) - the ability to "raise a force" from a settlement. If not set -> the value is read from female_character_subculture_details | False |
| public_office | values: ("y" / "n" / not set ) - access to the "Secure Promotion" action, as well as the ability to be faction and party leader. If not set -> the value is read from female_character_subculture_details | False |
| missions | values: ("y" / "n" / not set ) - access to any and all actions listed as missions (Diplomat, Administrator, Organize Feast + the new Political Marriage, Diplomatic Marriage, Dynastic Marriage). If not set -> the value is read from female_character_subculture_details | False |
| trait | special trait gives females bonus to missions. If not set the value is read from female_character_subculture_details | False |
  
## female_character_subculture_details_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| chance_to_spawn | values: (>= 0) - chance to spawn female character (in percent). If not set (value < 0) -> the value is read from female_character_culture_details | False |
| general | values: ("y" / "n" / not set ) - the ability to "raise a force" from a settlement. If not set -> the value is read from female_character_culture_details | False |
| public_office | values: ("y" / "n" / not set ) - access to the "Secure Promotion" action, as well as the ability to be faction and party leader. If not set -> the value is read from female_character_culture_details | False |
| missions | values: ("y" / "n" / not set ) - access to any and all actions listed as missions (Diplomat, Administrator, Organize Feast + the new Political Marriage, Diplomatic Marriage, Dynastic Marriage). If not set -> the value is read from female_character_culture_details | False |
| subculture |  | True |
| trait | special trait gives females bonus to missions. If not set the value is read from female_character_culture_details | False |
  
## first_person_engines_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| chance_to_spawn | values: (>= 0) - chance to spawn female character (in percent). If not set (value < 0) -> the value is read from female_character_culture_details | False |
| general | values: ("y" / "n" / not set ) - the ability to "raise a force" from a settlement. If not set -> the value is read from female_character_culture_details | False |
| public_office | values: ("y" / "n" / not set ) - access to the "Secure Promotion" action, as well as the ability to be faction and party leader. If not set -> the value is read from female_character_culture_details | False |
| missions | values: ("y" / "n" / not set ) - access to any and all actions listed as missions (Diplomat, Administrator, Organize Feast + the new Political Marriage, Diplomatic Marriage, Dynastic Marriage). If not set -> the value is read from female_character_culture_details | False |
| subculture |  | True |
| trait | special trait gives females bonus to missions. If not set the value is read from female_character_culture_details | False |
  
## font_names_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| font_name |  | True |
  
## fonts_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| bold | Whether font is a bold font | True |
| key |  | True |
| size | Size of font | True |
  
## formations_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| formation |  | True |
| icon_name | Name of icon to use for formation button | False |
| is_army | Is formation for applying to whole army | False |
| is_naval | Is the formation for naval purposes | False |
| order | Determines order formation buttons shown in ui | False |
  
## formations_to_subcultures_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| formation |  | True |
| sub_culture |  | True |
  
## fort_underlay_climate_jcts_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| fort_name |  | True |
| climate |  | True |
| snow_underlay |  | True |
| underlay |  | False |
  
## frontend_faction_leaders_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| fort_name |  | True |
| climate |  | True |
| snow_underlay |  | True |
| underlay |  | False |
  
## game_area_enums_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## general_command_star_level_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| alive_morale_bonus |  | False |
| command_star_level |  | True |
| melee_attack_bonus |  | False |
| melee_defence_bonus |  | False |
| nearby_morale_bonus |  | False |
  
## government_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| alive_morale_bonus |  | False |
| command_star_level |  | True |
| melee_attack_bonus |  | False |
| melee_defence_bonus |  | False |
| nearby_morale_bonus |  | False |
  
## governorships_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| governorship |  | True |
  
## ground_type_to_stat_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| governorship |  | True |
  
## ground_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| governorship |  | True |
  
## groupings_military_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| military_group |  | True |
  
## historical_battles_ui_locations_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| x |  | False |
| y |  | False |
| height_percent |  | False |
  
## historical_character_traits_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| character |  | True |
| trait |  | True |
  
## historical_characters_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| character |  | True |
| trait |  | True |
  
## honour_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| applies_to_ai |  | False |
| factor |  | False |
| key |  | True |
| value |  | False |
  
## honour_factors_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| maximum_value |  | False |
| minimum_value |  | False |
  
## incident_heading_texts_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| text |  | False |
  
## incidents_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| text |  | False |
  
## land_units_officers_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| text |  | False |
  
## land_units_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| text |  | False |
  
## land_units_to_unit_abilites_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| ability |  | True |
| land_unit |  | True |
  
## loyalty_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| applies_to_ai |  | False |
| factor |  | False |
| key |  | True |
| value |  | False |
  
## loyalty_factors_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| maximum_value |  | False |
| minimum_value |  | False |
  
## main_units_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| maximum_value |  | False |
| minimum_value |  | False |
  
## marriage_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## melee_weapons_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## mercenary_pool_modifiers_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| cost_modifier |  | False |
| culture_origin_match |  | False |
| key |  | True |
| min_pool_culture_percentage |  | False |
| pool_type |  | False |
| replenishment_modifier |  | False |
  
## mercenary_pool_to_groups_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| group |  | False |
| initial_unit_count |  | False |
| key |  | True |
| pool |  | False |
| faction_requirement |  | False |
| subculture_requirement |  | False |
| tech_requirement |  | False |
  
## mercenary_pool_type_enums_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| pool_type |  | True |
  
## mercenary_pools_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## mercenary_unit_groups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## message_event_strings_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| event |  | True |
| optional_campaign_key |  | True |
| culture |  | True |
| text |  | False |
| image |  | False |
| icon |  | False |
| sound_event |  | False |
| optional_subculture |  | True |
  
## message_events_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| event |  | True |
| instant_open |  | False |
| layout |  | False |
| requires_response |  | False |
| priority | Messages with a higher priority will be opened over those with a lower priority. 100 is standard for all messages. | False |
  
## military_force_legacy_emblems_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| event |  | True |
| instant_open |  | False |
| layout |  | False |
| requires_response |  | False |
| priority | Messages with a higher priority will be opened over those with a lower priority. 100 is standard for all messages. | False |
  
## military_force_legacy_names_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| event |  | True |
| instant_open |  | False |
| layout |  | False |
| requires_response |  | False |
| priority | Messages with a higher priority will be opened over those with a lower priority. 100 is standard for all messages. | False |
  
## ministerial_effectiveness_modifiers_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| leader_minister_level |  | True |
| government_type |  | True |
| effectiveness_bonus |  | False |
  
## ministerial_positions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| leader_minister_level |  | True |
| government_type |  | True |
| effectiveness_bonus |  | False |
  
## ministerial_positions_to_character_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect |  | True |
| effect_scope |  | False |
| minister_level |  | True |
| position |  | True |
| ui_id |  | False |
| value |  | False |
  
## ministerial_positions_to_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| position |  | True |
| effect |  | True |
| effect_scope |  | False |
| value |  | False |
| minister_level |  | True |
| ui_id |  | False |
  
## missile_weapons_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| position |  | True |
| effect |  | True |
| effect_scope |  | False |
| value |  | False |
| minister_level |  | True |
| ui_id |  | False |
  
## missile_weapons_to_projectiles_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| missile_weapon |  | True |
| projectile |  | True |
  
## mission_issuers_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| missile_weapon |  | True |
| projectile |  | True |
  
## missions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| missile_weapon |  | True |
| projectile |  | True |
  
## models_deployables_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| display_path |  | False |
| key |  | True |
| logic_file |  | False |
| model_file |  | False |
  
## models_entity_weapons_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| logic_file |  | False |
| model_file |  | False |
  
## models_oars_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| left_row |  | False |
| key |  | True |
| rigid_model |  | False |
| left_end |  | False |
| right_row |  | False |
| right_end |  | False |
  
## mount_variants_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| mount_key |  | False |
| display_key |  | False |
| weight |  | False |
  
## mountable_artillery_units_custom_battles_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| cap |  | False |
| mountable_artillery |  | True |
| probability |  | False |
| faction |  | True |
  
## mountable_artillery_units_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| unit_key |  | True |
  
## mounts_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| unit_key |  | True |
  
## movie_event_strings_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| event |  | True |
| culture |  | True |
| movie |  | False |
| id |  | False |
  
## mp_budgets_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| budget |  | False |
| budget_size_key |  | False |
| key |  | True |
| land |  | False |
| siege_defender |  | False |
  
## mp_force_gen_army_sizes_by_budgets_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| budget |  | True |
| maximum_unit_count |  | False |
| minimum_unit_count |  | True |
  
## mp_force_gen_template_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| budget |  | True |
| maximum_unit_count |  | False |
| minimum_unit_count |  | True |
  
## multiplayer_mininum_length_funds_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| value |  | False |
  
## name_orders_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| name_group |  | True |
| order |  | True |
| type |  | True |
  
## names_groups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## names_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| names_group |  | False |
| type |  | False |
| gender |  | False |
| frequency |  | False |
| id |  | True |
  
## naval_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect_name |  | False |
| key |  | True |
  
## naval_fire_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| chance_of_fire | percentage chance of catching fire when hit by projectile | False |
| incendiary_level |  | True |
| unit_category |  | True |
  
## naval_ramming_events_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| base_damage |  | False |
| key |  | True |
| rammed_ship |  | False |
| ramming_ship |  | False |
  
## naval_units_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| base_damage |  | False |
| key |  | True |
| rammed_ship |  | False |
| ramming_ship |  | False |
  
## naval_units_to_unit_abilites_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| ability |  | True |
| naval_unit |  | True |
  
## naval_weapons_enums_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| types |  | True |
  
## naval_weapons_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| types |  | True |
  
## particle_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## pdlc_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| ID |  | True |
| SteamID |  | False |
| description |  | False |
| release_order |  | False |
  
## plagues_permitted_campaigns_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign |  | True |
| plague |  | True |
  
## plagues_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| grade |  | False |
| infectivity |  | False |
| lifetime |  | False |
| region_effect_bundle |  | False |
| minimum_squalor |  | False |
| name |  | True |
| military_force_effect_bundle |  | False |
  
## political_actions_effect_bundles_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| action |  | True |
| effect_bundle |  | False |
| duration |  | False |
  
## political_actions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| action |  | True |
| effect_bundle |  | False |
| duration |  | False |
  
## political_parties_loyalty_effect_bundles_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| bundle_key |  | True |
| loyalty |  | True |
  
## political_parties_power_effect_bundles_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect_bundle |  | True |
| political_party_key |  | True |
| power_level |  | False |
  
## political_parties_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect_bundle |  | True |
| political_party_key |  | True |
| power_level |  | False |
  
## political_traits_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key | The id of the political party trait | True |
| onscreen_name | The name of the trait, shown in the politics UI | False |
| description | Localized description of the trait. | False |
  
## politics_government_actions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## politics_government_type_political_action_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| government_type |  | True |
| is_available_for_faction_leader |  | False |
| is_available_for_non_ruling_party_leaders |  | False |
| is_available_for_non_ruling_party_members |  | False |
| is_available_for_ruling_party_members |  | False |
| political_action |  | True |
  
## politics_government_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| government_type |  | True |
  
## population_classes_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| government_type |  | True |
  
## portrait_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## pre_battle_speeches_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| text |  | False |
| type |  | False |
| parameter |  | False |
  
## projectile_displays_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| text |  | False |
| type |  | False |
| parameter |  | False |
  
## projectile_impacts_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| text |  | False |
| type |  | False |
| parameter |  | False |
  
## projectile_shot_type_enum_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| text |  | False |
| type |  | False |
| parameter |  | False |
  
## projectile_trails_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key | delete this field if you see it | False |
| type |  | False |
| width |  | False |
| duration |  | False |
| min_aparent_width_distance |  | False |
| colour_r |  | False |
| colour_g |  | False |
| colour_b |  | False |
| opacity |  | False |
| fadeout_distance |  | False |
| distortion_cross_fade_start_distance |  | False |
| distortion_cross_fade_range |  | False |
  
## projectiles_explosions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key | delete this field if you see it | False |
| type |  | False |
| width |  | False |
| duration |  | False |
| min_aparent_width_distance |  | False |
| colour_r |  | False |
| colour_g |  | False |
| colour_b |  | False |
| opacity |  | False |
| fadeout_distance |  | False |
| distortion_cross_fade_start_distance |  | False |
| distortion_cross_fade_range |  | False |
  
## projectiles_missile_type_enum_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | False |
  
## projectiles_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | False |
  
## prologue_chapters_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | False |
  
## prologue_loading_screens_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| background_image | Path to background graphic | False |
| index |  | True |
| inset_image | Path to inset graphic | False |
| pane_on_left | Is the text pane on the left or the right of the loading screen? | False |
| campaign |  | False |
  
## province_to_mercenary_set_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| background_image | Path to background graphic | False |
| index |  | True |
| inset_image | Path to inset graphic | False |
| pane_on_left | Is the text pane on the left or the right of the loading screen? | False |
| campaign |  | False |
  
## provinces_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## provincial_initiative_records_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## provincial_initiatives_to_subculture_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| provincial_initiative_key |  | True |
| subculture |  | True |
  
## public_order_factors_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| factor |  | True |
| positive_pip_path |  | False |
| negative_pip_path |  | False |
| optional_campaign_key |  | False |
  
## quotes_people_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| quote_person_key |  | True |
| quote_person_onscreen |  | False |
  
## quotes_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| quote_onscreen |  | False |
| quote_person |  | False |
| key |  | True |
  
## random_localisation_strings_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## region_campaign_overrides_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign |  | True |
| region |  | True |
| religion |  | False |
| religion_zeal |  | False |
  
## region_economics_factors_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| factor |  | True |
| positive_pip_path |  | False |
  
## region_groups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| factor |  | True |
| positive_pip_path |  | False |
  
## region_religions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| region |  | True |
| religion |  | False |
| religion_zeal |  | False |
  
## region_to_province_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| region |  | True |
| religion |  | False |
| religion_zeal |  | False |
  
## region_unit_resources_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| string |  | False |
  
## regions_continents_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| continent |  | True |
  
## regions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| continent |  | True |
  
## regions_to_region_groups_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| continent |  | True |
  
## religion_conversion_mods_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| rel_from |  | True |
| rel_to |  | True |
| modifier |  | False |
  
## religions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| rel_from |  | True |
| rel_to |  | True |
| modifier |  | False |
  
## resource_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect_key |  | True |
| resource_key |  | True |
| value |  | False |
  
## resources_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect_key |  | True |
| resource_key |  | True |
| value |  | False |
  
## scripted_objectives_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key | Key used by scriptors to trigger | True |
  
## scripted_subtitles_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key | Key for scriptors to trigger | True |
| character_for_vo | In-game character who will provide VO for this line, if any | False |
  
## sea_surfaces_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| sea_wind_speed |  | False |
| sea_phillips_constant |  | False |
| sea_choppiness |  | False |
| swell_wind_speed |  | False |
| swell_phillips_constant |  | False |
| foam_enabled |  | False |
| foam_decay_rate |  | False |
| foam_fade_in_time |  | False |
| foam_cut_off_value |  | False |
| froth_value |  | False |
| froth_distortion_speed |  | False |
| froth_distortion_amount |  | False |
| spray_cut_off_value |  | False |
| spray_speed |  | False |
| spray_duration |  | False |
| sea_shininess |  | False |
| sea_decay |  | False |
| reflection_flattening_factor |  | False |
| wave_trough_y_value |  | False |
| detail_normal_uv_scale1 |  | False |
| detail_normal_uv_speed1 |  | False |
| detail_normal_uv_scale2 |  | False |
| detail_normal_uv_speed2 |  | False |
  
## season_attritions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| sea_wind_speed |  | False |
| sea_phillips_constant |  | False |
| sea_choppiness |  | False |
| swell_wind_speed |  | False |
| swell_phillips_constant |  | False |
| foam_enabled |  | False |
| foam_decay_rate |  | False |
| foam_fade_in_time |  | False |
| foam_cut_off_value |  | False |
| froth_value |  | False |
| froth_distortion_speed |  | False |
| froth_distortion_amount |  | False |
| spray_cut_off_value |  | False |
| spray_speed |  | False |
| spray_duration |  | False |
| sea_shininess |  | False |
| sea_decay |  | False |
| reflection_flattening_factor |  | False |
| wave_trough_y_value |  | False |
| detail_normal_uv_scale1 |  | False |
| detail_normal_uv_speed1 |  | False |
| detail_normal_uv_scale2 |  | False |
| detail_normal_uv_speed2 |  | False |
  
## season_province_effect_bundles_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| sea_wind_speed |  | False |
| sea_phillips_constant |  | False |
| sea_choppiness |  | False |
| swell_wind_speed |  | False |
| swell_phillips_constant |  | False |
| foam_enabled |  | False |
| foam_decay_rate |  | False |
| foam_fade_in_time |  | False |
| foam_cut_off_value |  | False |
| froth_value |  | False |
| froth_distortion_speed |  | False |
| froth_distortion_amount |  | False |
| spray_cut_off_value |  | False |
| spray_speed |  | False |
| spray_duration |  | False |
| sea_shininess |  | False |
| sea_decay |  | False |
| reflection_flattening_factor |  | False |
| wave_trough_y_value |  | False |
| detail_normal_uv_scale1 |  | False |
| detail_normal_uv_speed1 |  | False |
| detail_normal_uv_scale2 |  | False |
| detail_normal_uv_speed2 |  | False |
  
## seasons_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| sea_wind_speed |  | False |
| sea_phillips_constant |  | False |
| sea_choppiness |  | False |
| swell_wind_speed |  | False |
| swell_phillips_constant |  | False |
| foam_enabled |  | False |
| foam_decay_rate |  | False |
| foam_fade_in_time |  | False |
| foam_cut_off_value |  | False |
| froth_value |  | False |
| froth_distortion_speed |  | False |
| froth_distortion_amount |  | False |
| spray_cut_off_value |  | False |
| spray_speed |  | False |
| spray_duration |  | False |
| sea_shininess |  | False |
| sea_decay |  | False |
| reflection_flattening_factor |  | False |
| wave_trough_y_value |  | False |
| detail_normal_uv_scale1 |  | False |
| detail_normal_uv_speed1 |  | False |
| detail_normal_uv_scale2 |  | False |
| detail_normal_uv_speed2 |  | False |
  
## send_diplomat_incidents_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| incident |  | True |
| outcome |  | True |
| culture |  | True |
| weight | Used to select randomly between all applicable events | False |
  
## ship_dbs_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| incident |  | True |
| outcome |  | True |
| culture |  | True |
| weight | Used to select randomly between all applicable events | False |
  
## shortcut_localisation_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key | Key that matches up to default_keys.xml | True |
  
## slot_template_to_building_superchain_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building_superchain |  | False |
| id |  | True |
| slot_template |  | False |
  
## slot_templates_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| building_superchain |  | False |
| id |  | True |
| slot_template |  | False |
  
## slot_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| can_convert |  | False |
| can_destroy |  | False |
| key |  | True |
  
## slots_gdp_values_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| slot |  | True |
| level |  | True |
| gdp_value |  | False |
| building_gdp_modifier |  | False |
  
## slots_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| slot |  | True |
| is_farm |  | False |
| is_town |  | False |
| is_port |  | False |
| is_resource |  | False |
| supports_building_level_conversion |  | False |
  
## slots_templates_models_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| template_name |  | True |
| model_filename |  | False |
| model_filepath |  | False |
  
## sound_events_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | False |
  
## special_ability_groups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | False |
  
## special_ability_groups_to_factions_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| ability_group |  | True |
| faction |  | False |
  
## special_ability_groups_to_unit_abilities_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| special_ability_groups |  | True |
| unit_special_abilities |  | True |
  
## special_ability_invalid_usage_flags_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| special_ability_groups |  | True |
| unit_special_abilities |  | True |
  
## special_ability_phase_attribute_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| special_ability_groups |  | True |
| unit_special_abilities |  | True |
  
## special_ability_phase_stat_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| special_ability_groups |  | True |
| unit_special_abilities |  | True |
  
## special_ability_phases_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| special_ability_groups |  | True |
| unit_special_abilities |  | True |
  
## special_ability_to_auto_deactivate_flags_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| invalid_usage_flag |  | True |
| special_ability_key |  | True |
  
## special_ability_to_invalid_usage_flags_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| invalid_usage_flag |  | True |
| special_ability |  | True |
  
## special_ability_to_special_ability_phase_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| order |  | True |
| phase |  | False |
| special_ability |  | True |
  
## spotting_and_hiding_values_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| spot_dist_scrub | At what range do we see units hidden in scrub | False |
| spot_dist_tree | At what range do we see units hidden in trees | False |
| visibility_max_spot_range | We cannot see units after this range | False |
| visibility_min_spot_range | We always see units within this range | False |
  
## stances_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| onscreen |  | False |
  
## start_pos_calendars_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign |  | True |
| start_year |  | False |
| turns_per_year |  | False |
| start_season |  | False |
| start_week_of_year |  | False |
  
## start_pos_character_ancillaries_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | True |
| character_id |  | False |
| ancillary |  | False |
  
## start_pos_character_to_settlements_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| character |  | True |
| settlement |  | False |
  
## start_pos_character_traits_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | True |
| character_id |  | False |
| trait_level |  | False |
  
## start_pos_characters_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| ID |  | True |
| faction |  | False |
| Name |  | False |
| Surname |  | False |
| Age |  | False |
| Type |  | False |
| startx |  | False |
| starty |  | False |
| ministerial_position |  | False |
| portrait_id |  | False |
| model |  | False |
| immortal |  | False |
| override_general_unit |  | False |
| is_in_generals_pool |  | False |
| is_male |  | False |
| loyalty |  | False |
| clan_name |  | False |
| other_name |  | False |
| ambition |  | False |
| political_party |  | False |
| death_type |  | False |
| turns_died_before_start |  | False |
| progenitor |  | False |
| xp |  | False |
  
## start_pos_diplomacy_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | False |
| faction1 |  | True |
| faction2 |  | True |
| stance |  | False |
| grants_military_access |  | False |
| grants_trade_agreement |  | False |
| non_aggression_pact |  | False |
  
## start_pos_factions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| ID |  | True |
| faction |  | False |
| campaign |  | False |
| playable |  | False |
| treasury |  | False |
| starting_order |  | False |
| government_type |  | False |
| state_religion |  | False |
| is_major |  | False |
| difficulty |  | False |
| ai_manager |  | False |
| ai_personality |  | False |
| long_victory_region_count |  | False |
| short_victory_region_count |  | False |
| prestige_victory_region_count |  | False |
| world_domination_victory_region_count |  | False |
| short_victory_year_end |  | False |
| long_victory_year_end |  | False |
| prestige_victory_year_end |  | False |
| world_domination_victory_year_end |  | False |
| prestige_army |  | False |
| prestige_navy |  | False |
| prestige_economy |  | False |
| prestige_enlightenment |  | False |
| short_victory_week_in_year_end |  | False |
| long_victory_week_in_year_end |  | False |
| prestige_victory_week_in_year_end |  | False |
| world_domination_victory_week_in_year_end |  | False |
| honour |  | False |
| ai_technology_manager |  | False |
| ai_character_skill_tree_manager |  | False |
| cai_agent_distribution_profile |  | False |
| cai_agent_recruitment_profile |  | False |
| cai_starting_personality |  | False |
| mp_one_vs_one_region_count |  | False |
| mp_2p_co_op_region_count |  | False |
| mp_2p_co_op_region_count_long |  | False |
| long_description |  | False |
| can_ever_convert_religion |  | False |
| cdir_military_generator_config |  | False |
  
## start_pos_family_relationships_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| character |  | True |
| related_to |  | True |
| relationship |  | False |
| bastard |  | False |
| adopted |  | False |
  
## start_pos_land_units_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | True |
| unit_type |  | False |
| general |  | False |
| soldiers |  | False |
  
## start_pos_naval_units_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| ID |  | True |
| unit_type |  | False |
| admiral |  | False |
  
## start_pos_past_events_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| event |  | True |
| source |  | True |
| target |  | True |
| turns_ago |  | True |
  
## start_pos_region_religions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| region |  | True |
| religion |  | True |
| percentage |  | False |
  
## start_pos_region_slot_templates_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign |  | True |
| id |  | True |
| region |  | True |
| slot_template |  | True |
| slot_type |  | True |
  
## start_pos_regions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | False |
| region |  | True |
| campaign |  | True |
| owning_faction |  | False |
| faction_capital |  | False |
| base_population |  | False |
| base_max_population |  | False |
| population |  | False |
| base_gdp |  | False |
| road_upgrades |  | False |
| canals |  | False |
| railways |  | False |
| town_wealth |  | False |
| governorship |  | False |
| rebel_faction |  | False |
| cultural_originator |  | False |
| settler_rebellions_enabled |  | False |
| capture_prestige |  | False |
| alternative_rebel_faction |  | False |
| long_description |  | False |
| development_points |  | False |
  
## start_pos_regions_to_unit_resources_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| resource |  | True |
  
## start_pos_settlements_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| settlement_id |  | True |
| region |  | True |
| building1 |  | False |
| building2 |  | False |
| building3 |  | False |
| building4 |  | False |
| building5 |  | False |
| wealth |  | False |
| fortification |  | False |
| id |  | False |
| roads |  | False |
| fortifications |  | False |
| primary_building |  | False |
| port_building |  | False |
| startpos_slave_points |  | False |
  
## start_pos_technologies_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| faction |  | True |
| technology |  | True |
  
## start_pos_victory_conditions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| start_pos_faction |  | True |
| region |  | True |
| victory_type |  | True |
  
## state_gift_values_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| value |  | False |
  
## stats_clans_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| label |  | False |
| public |  | False |
| ladder |  | False |
  
## stats_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| label |  | False |
| public |  | False |
| ladder |  | False |
  
## subtitle_timings_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| label |  | False |
| public |  | False |
| ladder |  | False |
  
## taxes_classes_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| tax |  | True |
  
## taxes_effects_jct_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| tax |  | True |
  
## taxes_keys_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| tax_class |  | True |
| tax_level |  | True |
| tax_lookup |  | False |
  
## taxes_levels_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| tax_level |  | True |
| percentage |  | False |
  
## team_colours_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| alliance |  | False |
| b |  | True |
| g |  | True |
| r |  | True |
| army_index |  | False |
  
## technologies_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| alliance |  | False |
| b |  | True |
| g |  | True |
| r |  | True |
| army_index |  | False |
  
## technology_categories_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| position |  | False |
  
## technology_category_modules_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| effect_bundle |  | False |
| max_tier |  | True |
| min_tier |  | False |
| technology_node_set |  | True |
  
## technology_category_parents_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| child_category |  | True |
| parent_category |  | True |
  
## technology_effects_junction_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| technology |  | True |
| effect |  | True |
| effect_scope |  | False |
| value |  | False |
  
## technology_node_links_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| technology |  | True |
| effect |  | True |
| effect_scope |  | False |
| value |  | False |
  
## technology_node_sets_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| technology |  | True |
| effect |  | True |
| effect_scope |  | False |
| value |  | False |
  
## technology_nodes_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| technology |  | True |
| effect |  | True |
| effect_scope |  | False |
| value |  | False |
  
## technology_required_building_levels_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| technology |  | True |
| required_building_level |  | True |
  
## technology_required_technology_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| technology |  | True |
| required_technology |  | True |
  
## technology_unit_upgrades_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| cost |  | False |
| target_unit |  | False |
| technology |  | True |
| unit |  | True |
  
## terrain_tilesets_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| tileset_name |  | True |
  
## town_wealth_growth_factors_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| factor |  | True |
| positive_pip_path |  | False |
| negative_pip_path |  | False |
  
## trade_details_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| icon_filepath |  | False |
  
## trade_display_campaign_originating_culture_trade_model_options_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign |  | False |
| key |  | True |
| model |  | False |
| originating_culture |  | False |
| priority |  | False |
| relative_frequency |  | False |
  
## trade_display_campaign_owning_culture_produced_resource_trade_model_options_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign |  | False |
| key |  | True |
| model |  | False |
| owning_culture |  | False |
| priority |  | False |
| produced_resource |  | False |
| relative_frequency |  | False |
  
## trade_display_campaign_owning_culture_trade_model_options_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign |  | False |
| key |  | True |
| model |  | False |
| owning_culture |  | False |
| priority |  | False |
| relative_frequency |  | False |
  
## trade_display_campaign_trade_model_options_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| campaign |  | False |
| key |  | True |
| model |  | False |
| priority |  | False |
| relative_frequency |  | False |
  
## trade_display_generic_trade_model_options_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| model |  | False |
| priority |  | False |
| relative_frequency |  | False |
  
## trade_display_originating_culture_trade_model_options_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| model |  | False |
| originating_culture |  | False |
| priority |  | False |
| relative_frequency |  | False |
  
## trade_display_originating_subculture_trade_model_options_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| model |  | False |
| originating_subculture |  | False |
| priority |  | False |
| relative_frequency |  | False |
  
## trade_display_owning_culture_trade_model_options_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| model |  | False |
| owning_culture |  | False |
| priority |  | False |
| relative_frequency |  | False |
  
## trade_display_owning_faction_trade_model_options_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| model |  | False |
| owning_faction |  | False |
| priority |  | False |
| relative_frequency |  | False |
  
## trade_display_produced_resource_trade_model_options_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| model |  | False |
| priority |  | False |
| produced_resource |  | False |
| relative_frequency |  | False |
  
## trade_display_trade_models_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| is_naval |  | False |
| key |  | True |
| model |  | False |
| optional_following_model |  | False |
| optional_following_model_distance |  | False |
  
## trade_node_groups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## trait_categories_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| category |  | True |
| icon_path |  | False |
  
## trait_info_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| category |  | True |
| icon_path |  | False |
  
## trait_level_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| trait_level |  | True |
| effect |  | True |
| effect_scope |  | False |
| value |  | False |
  
## trait_to_antitraits_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| antitrait |  | True |
| trait |  | True |
  
## trait_to_included_agents_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| trait |  | True |
| agent |  | True |
  
## trees_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| tree_id |  | False |
| distance_to_coast |  | False |
| shrub |  | False |
| high_altitude |  | False |
| conifer |  | False |
  
## trigger_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| id |  | True |
| trigger |  | False |
| trait |  | False |
| value |  | False |
| chance |  | False |
  
## trigger_events_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| event |  | True |
  
## ui_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key | Key for ui_effect | True |
| banner_fx | Effect that plays around base of unit banner | False |
| ping_fx | Effect that plays around effect icon that appears on top of banner | False |
  
## ui_unit_stat_to_classes_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key | Key for ui_effect | True |
| banner_fx | Effect that plays around base of unit banner | False |
| ping_fx | Effect that plays around effect icon that appears on top of banner | False |
  
## ui_unit_stats_filters_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## ui_unit_stats_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## unit_abilities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## unit_armour_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## unit_attributes_groups_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| group_name |  | True |
  
## unit_attributes_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| group_name |  | True |
  
## unit_attributes_to_groups_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| attribute |  | True |
| attribute_group |  | True |
  
## unit_castes_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| caste |  | True |
| localised_name |  | False |
| sort_priority |  | False |
  
## unit_category_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| caste |  | True |
| localised_name |  | False |
| sort_priority |  | False |
  
## unit_class_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| caste |  | True |
| localised_name |  | False |
| sort_priority |  | False |
  
## unit_description_gameplay_texts_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | False |
  
## unit_description_historical_texts_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## unit_description_short_texts_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## unit_description_strengths_weaknesses_texts_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## unit_experience_bonuses_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| stat |  | True |
| value |  | False |
| growth_rate |  | False |
| growth_scalar |  | False |
  
## unit_experience_threshold_modifiers_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| modifier |  | False |
  
## unit_experience_thresholds_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| value |  | False |
  
## unit_fatigue_effects_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| value |  | False |
  
## unit_ground_type_movement_modifiers_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| category |  | True |
| ground_type |  | True |
| speed_modifier |  | False |
  
## unit_required_technology_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| unit_key |  | True |
| technology_key |  | True |
  
## unit_set_to_unit_junctions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| exclude |  | False |
| unit_caste |  | True |
| unit_category |  | True |
| unit_class |  | True |
| unit_record |  | True |
| unit_set |  | True |
  
## unit_sets_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| exclude |  | False |
| unit_caste |  | True |
| unit_category |  | True |
| unit_class |  | True |
| unit_record |  | True |
| unit_set |  | True |
  
## unit_shield_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| exclude |  | False |
| unit_caste |  | True |
| unit_category |  | True |
| unit_class |  | True |
| unit_record |  | True |
| unit_set |  | True |
  
## unit_spacings_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| exclude |  | False |
| unit_caste |  | True |
| unit_category |  | True |
| unit_class |  | True |
| unit_record |  | True |
| unit_set |  | True |
  
## unit_special_abilities_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| exclude |  | False |
| unit_caste |  | True |
| unit_category |  | True |
| unit_class |  | True |
| unit_record |  | True |
| unit_set |  | True |
  
## unit_stat_modifiers_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| exclude |  | False |
| unit_caste |  | True |
| unit_category |  | True |
| unit_class |  | True |
| unit_record |  | True |
| unit_set |  | True |
  
## unit_stats_land_experience_bonuses_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| exclude |  | False |
| unit_caste |  | True |
| unit_category |  | True |
| unit_class |  | True |
| unit_record |  | True |
| unit_set |  | True |
  
## unit_stats_naval_crew_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| unit_type |  | True |
| core_loading_skill |  | False |
| core_marksmanship |  | False |
| melee_attack |  | False |
| melee_defence |  | False |
| melee_weapon_type |  | False |
| pistols |  | False |
| ammo |  | False |
| battle_entity |  | False |
| soldier_model |  | False |
| man_animations_table |  | False |
| equipment_theme |  | False |
| armour_audio |  | False |
| armour |  | False |
| spacing |  | False |
| discipline |  | False |
| missile_type |  | False |
  
## unit_stats_naval_crew_to_factions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| faction |  | False |
| marines |  | False |
| seaman |  | False |
| guncrew |  | False |
| admiral |  | False |
| commodore |  | False |
| naval_officer |  | False |
| musician |  | False |
  
## unit_stats_naval_experience_bonuses_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| xp_level |  | True |
| melee_defence |  | False |
| melee_attack |  | False |
| core_gunner_loading_skill |  | False |
| core_gunner_marksmanship |  | False |
| morale |  | False |
| mp_fixed_cost |  | False |
| mp_experience_cost_multiplier |  | False |
  
## unit_type_enums_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## unit_variants_colours_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## unit_variants_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## unit_voice_categories_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## unit_weights_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## units_custom_battle_permissions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## units_to_exclusive_faction_permissions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| faction |  | True |
| allowed |  | False |
  
## units_to_groupings_military_permissions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| unit |  | True |
| military_group |  | True |
  
## variants_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| unit |  | True |
| military_group |  | True |
  
## victory_conditions_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| condition |  | True |
  
## victory_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| condition |  | True |
  
## videos_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| condition |  | True |
  
## voice_types_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
  
## warscape_animated_lod_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| filename |  | False |
| range |  | False |
| animated |  | False |
  
## warscape_animated_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| texture_filename_base |  | False |
| category |  | False |
  
## warscape_equipment_items_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| equipment_item |  | False |
| equipment_key |  | True |
  
## warscape_equipment_themes_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| theme |  | True |
| primary_weapon |  | False |
| secondary_weapon |  | False |
| defensive |  | False |
| ambient |  | False |
| personal |  | False |
| banners |  | False |
  
## warscape_rigid_lod_range_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| LOD_id |  | True |
| range |  | False |
  
## warscape_rigid_lod_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| filename |  | False |
| range |  | False |
| rigid |  | False |
  
## warscape_rigid_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| texture_directory |  | False |
| category |  | False |
  
## warscape_trees_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| tree |  | False |
| season |  | False |
| model_path |  | False |
  
## warscape_underlay_textures_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| underlay_key |  | True |
| filename |  | False |
| filepath |  | False |
| levels |  | False |
  
## wind_levels_tables

| Field Name | Description | Is Key |
|------------|-------------|--------|
| key |  | True |
| sea_surface |  | False |
| magnitudeX |  | False |
| magnitudeY |  | False |
| sort_order |  | False |