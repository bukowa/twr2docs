---
title: interfaces
summary: A brief description of my document.
---

## battle_manager
The `battle_manager` interface provides functions for managing various aspects of a battle, including setup, events, and unit control.

*   `new(battle_obj)`
*   `advice_cease()`
*   `advice_resume()`
*   `callback()`
*   `check_rout_manager()`
*   `check_watch_entry()`
*   `clear_watches_and_callbacks()`
*   `dont_close_queue_advice()`
*   `end_battle()`
*   `end_deployment()`
*   `get_next_watch_entry()`
*   `out()`
*   `play_next_advice()`
*   `print_callback_list()`
*   `print_watch_list()`
*   `process_results()`
*   `queue_advisor()`
*   `register_esc_key_callback()`
*   `register_phase_change_callback()`
*   `register_repeating_timer()`
*   `register_results_callbacks()`
*   `register_singleshot_timer()`
*   `register_victory_countdown_callback()`
*   `release_escape_key()`
*   `remove_process()`
*   `remove_process_from_callback_list()`
*   `remove_process_from_watch_list()`
*   `repeat_callback()`
*   `rout_threshold_reached()`
*   `set_load_balancing()`
*   `setup_battle()`
*   `setup_victory_callback()`
*   `start_rout_manager()`
*   `steal_escape_key()`
*   `stop_advice_on_battle_end()`
*   `stop_advisor_queue()`
*   `stop_rout_manager()`
*   `tick_watch_counter()`
*   `unlock_achievement()`
*   `unregister_esc_key_callback()`
*   `unregister_timer()`
*   `watch()`
*   `watch_advice_queue()`
*   `add_ping_icon()`
*   `advice_finished()`
*   `alliances()`
*   `assault_equipment()`
*   `buildings()`
*   `camera()`
*   `change_conflict_time_update_overridden()`
*   `change_victory_countdown_limit()`
*   `cindy_playback()`
*   `cindy_playback_no_camera()`
*   `close_advisor()`
*   `create_ui_attack_group()`
*   `create_ui_defend_group()`
*   `debug_drawing()`
*   `disable_shortcut()`
*   `enable_cinematic_camera()`
*   `enable_cinematic_ui()`
*   `enable_tooltips()`
*   `end_benchmark()`
*   `end_current_battle_phase()`
*   `error()`
*   `fade_volume()`
*   `get_volume()`
*   `highlight_component()`
*   `is_battle_over()`
*   `is_benchmarking_mode()`
*   `is_movie_playing()`
*   `is_music_playing()`
*   `local_alliance()`
*   `local_army()`
*   `modify_battle_speed()`
*   `place_naval_mine()`
*   `play_movie()`
*   `play_music()`
*   `play_music_custom_fade()`
*   `random_number()`
*   `register_battle_phase_handler()`
*   `register_command_handler()`
*   `register_input_handler()`
*   `register_unit_selection_handler()`
*   `release_input_focus()`
*   `remaining_conflict_time()`
*   `remove_ping_icon()`
*   `restore_battle_speed()`
*   `set_banners_enabled()`
*   `set_music_auto_playback()`
*   `set_music_loop()`
*   `set_volume()`
*   `show_objective()`
*   `start_lighting_environment_cross_fade()`
*   `start_terrain_effect()`
*   `steal_input_focus()`
*   `stop_cindy_playback()`
*   `stop_cindy_playback_no_camera()`
*   `stop_music()`
*   `stop_music_custom_fade()`
*   `stop_terrain_effect()`
*   `subtitles()`
*   `suppress_unit_musicians()`
*   `suppress_unit_voices()`
*   `suspend_contextual_advice()`
*   `trigger_projectile_launch()`
*   `ui_component()`
*   `unregister_battle_phase_handler()`
*   `unregister_command_handler()`
*   `unregister_input_handler()`
*   `unregister_unit_selection_handler()`
*   `vo_finished()`
*   `weather()`

## battle.ai_unit_controller
The `battle.ai_unit_controller` interface manages AI unit actions in battle.


*   `new()`
*   `add_units()`
*   `attack_unit()`
*   `clear_objective()`
*   `defend_position()`
*   `move_to_position()`
*   `remove_units()`

## battle.assault_equipment
The `battle.assault_equipment` interface provides information about assault equipment.


*   `new()`
*   `vehicle_count()`
*   `vehicle_item()`

## battle.building
The `battle.building` interface provides information and control over individual buildings in a battle.


*   `new()`
*   `alliance_owner_id()`
*   `capacity()`
*   `central_position()`
*   `change_immune_to_catching_fire()`
*   `change_immune_to_fire_damage()`
*   `change_is_destructible()`
*   `change_on_fire()`
*   `currently_garrisoned()`
*   `destroy()`
*   `health()`
*   `hide()`
*   `is_garrisoned()`
*   `name()`
*   `position()`
*   `show()`

## battle.buildings
The `battle.buildings` interface manages collections of buildings.


*   `new()`
*   `count()`
*   `garrisonable_count()`
*   `garrisonable_item()`
*   `item()`

## battle.camera
The `battle.camera` interface controls the in-battle camera.


*   `new()`
*   `change_depth_of_field()`
*   `change_height_range()`
*   `disable_anchor_to_army()`
*   `disable_functionality()`
*   `disable_shake()`
*   `enable_anchor_to_army()`
*   `enable_functionality()`
*   `enable_shake()`
*   `fade()`
*   `look_at()`
*   `move_to()`
*   `position()`
*   `target()`

## battle.commandevent
The `battle.commandevent` interface provides details about a command event.


*   `new()`
*   `get_bool1()`
*   `get_building()`
*   `get_name()`
*   `get_position()`
*   `get_ship()`
*   `get_string1()`
*   `get_unit()`

## battle.debug_drawing
The `battle.debug_drawing` interface provides functions for drawing debug elements on the terrain.


*   `new()`
*   `draw_circle_on_terrain()`
*   `draw_line_on_terrain()`
*   `draw_peg_on_terrain()`
*   `draw_white_circle_on_terrain()`
*   `draw_white_line_on_terrain()`
*   `draw_white_peg_on_terrain()`

## battle.ship
The `battle.ship` interface provides information and control over individual ships in a battle.


*   `new()`
*   `bearing()`
*   `deploy_reinforcement()`
*   `hull_damage()`
*   `is_routing()`
*   `is_surrendered()`
*   `name()`
*   `number_of_men_alive()`
*   `position()`
*   `sail_damage()`
*   `ship_in_range()`
*   `type()`

## battle.ships
The `battle.ships` interface manages collections of ships.


*   `new()`
*   `count()`
*   `item()`

## battle.subtitles
The `battle.subtitles` interface manages in-battle subtitles.


*   `new()`
*   `begin()`
*   `change_if_borders_drawn()`
*   `change_if_top_border_drawn()`
*   `clear()`
*   `end_subtitles()`
*   `push_back_subtitle()`
*   `push_back_subtitle_entry()`
*   `read_subtitles_file()`
*   `set_alignment()`
*   `set_text()`

## battle.vehicle
The `battle.vehicle` interface provides information about a vehicle.


*   `new()`
*   `position()`

## battle.weather
The `battle.weather` interface controls in-battle weather effects.


*   `new()`
*   `add_dust()`
*   `add_rain()`
*   `add_snow()`
*   `change_lighting()`
*   `clear_weather()`
*   `enable_random_lightning()`
*   `trigger_lightning_sheet()`
*   `trigger_lightning_strike()`

## battle_colour
The `battle_colour` interface represents a battle color.


*   `new()`

## battle_location
The `battle_location` interface represents a location in battle.


*   `new()`
*   `get_position()`
*   `set_position()`

## battle_sound_effect
The `battle_sound_effect` interface manages battle sound effects.


*   `new()`
*   `is_playing()`
*   `load()`
*   `play3D()`
*   `stop()`

## battle.alliances
The `battle.alliances` interface manages collections of alliances.


*   `new()`
*   `count()`
*   `item(index)`

## battle.alliance
The `battle.alliance` interface provides information and control over an alliance in battle.


*   `new()`
*   `armies()`
*   `create_ai_unit_planner()`
*   `force_ai_plan_type_attack()`
*   `force_ai_plan_type_defend()`
*   `force_snap_ai_to_hint_lines()`

## battle.armies
The `battle.armies` interface manages collections of armies.


*   `new()`
*   `count()`
*   `item(index)`

## battle.army
The `battle.army` interface provides information and control over an army in battle.


*   `new()`
*   `army_handicap()`
*   `change_faction()`
*   `create_unit_controller()`
*   `enable_army_destruction_morale_effect()`
*   `get_reinforcement_ships()`
*   `get_reinforcement_units()`
*   `is_commander_alive()`
*   `is_commander_invincible()`
*   `quit_battle()`
*   `ships()`
*   `units()`

## battle.units
The `battle.units` interface manages collections of units.


*   `new()`
*   `count()`
*   `kill_commander()`
*   `mountable_artillery_item()`
*   `item(index)`

## battle.unit
The `battle.unit` interface provides information and control over an individual unit in battle.


*   `new()`
*   `ammo_left()`
*   `bearing()`
*   `can_perform_special_ability()`
*   `current_special_ability()`
*   `deploy_reinforcement(can_deploy)`
*   `has_ships()`
*   `initial_number_of_men()`
*   `is_artillery()`
*   `is_behaviour_active()`
*   `is_cavalry()`
*   `is_currently_garrisoned()`
*   `is_dismounted_ships()`
*   `is_hidden()`
*   `is_idle()`
*   `is_infantry()`
*   `is_leaving_battle()`
*   `is_limbered_artillery()`
*   `is_moving()`
*   `is_moving_fast()`
*   `is_routing()`
*   `is_shattered()`
*   `is_under_missile_attack()`
*   `is_valid_target()`
*   `is_visible_to_alliance()`
*   `kill_number_of_men()`
*   `missile_range()`
*   `name()`
*   `number_of_enemies_killed()`
*   `number_of_men_alive()`
*   `ordered_position()`
*   `ordered_width()`
*   `play_anim_for_captain()`
*   `position()`
*   `position_of_officer()`
*   `set_current_ammo_unary()`
*   `starting_ammo()`
*   `trigger_sound_charge()`
*   `trigger_sound_taunt()`
*   `trigger_sound_warcry()`
*   `type()`
*   `unary_of_men_alive()`
*   `unit_distance()`
*   `unit_in_range()`

## battle.unit_controller
The `battle.unit_controller` interface provides high-level control over groups of units.


*   `new()`
*   `add_all_units()`
*   `add_group()`
*   `add_units(...)`
*   `attack_building()`
*   `attack_building_q()`
*   `attack_line()`
*   `attack_line_q()`
*   `attack_location()`
*   `attack_location_q()`
*   `attack_unit()`
*   `attack_unit_q()`
*   `change_behaviour_active()`
*   `change_current_walk_speed()`
*   `change_enabled()`
*   `change_fatigue_amount()`
*   `change_group_formation()`
*   `change_group_formation_q()`
*   `change_move_speed()`
*   `change_shot_type()`
*   `change_shot_type_q()`
*   `clear_all()`
*   `climb_building()`
*   `climb_building_q()`
*   `decrement_formation_width()`
*   `defend_building()`
*   `defend_building_q()`
*   `fire_at_will()`
*   `goto_location(position, move_fast)`
*   `goto_location_angle_width()`
*   `goto_location_angle_width_q()`
*   `goto_location_q()`
*   `halt()`
*   `hide_unit_card()`
*   `highlight()`
*   `increment_formation_width()`
*   `interact_with_deployable()`
*   `interact_with_deployable_q()`
*   `kill()`
*   `leave_building()`
*   `melee()`
*   `morale_behavior_default()`
*   `morale_behavior_fearless()`
*   `morale_behavior_rout()`
*   `occupy_vehicle()`
*   `occupy_vehicle_q()`
*   `occupy_zone()`
*   `occupy_zone_q()`
*   `perform_special_ability()`
*   `perform_special_ability_q()`
*   `release_control()`
*   `rotate()`
*   `rotate_q()`
*   `select_deployable_object()`
*   `set_always_visible_to_all()`
*   `set_invincible()`
*   `set_invisible_to_all()`
*   `start_celebrating()`
*   `start_taunting()`
*   `step_backward()`
*   `step_forward()`
*   `take_control()`
*   `teleport_to_location(position, bearing, width)`
*   `trigger_sound_vo()`
*   `update_card_existance_on_HUD()`
*   `withdraw()`
*   `withdraw_q()`

## battle_vector
The `battle_vector` interface represents a 3D vector in battle.


*   `new()`
*   `distance()`
*   `distance_xz()`
*   `get_x()`
*   `get_y()`
*   `get_z()`
*   `length()`
*   `length_xz()`
*   `set()`
*   `set_x()`
*   `set_y()`
*   `set_z()`


## zone_controller
The `zone_controller` interface manages zones and units within them.


*   `new()`
*   `activate()`
*   `add_sunit()`
*   `add_sunits()`
*   `add_zone()`
*   `all_units_routing()`
*   `assess()`
*   `check_sunits_health()`
*   `deactivate()`
*   `find_reinforcement()`
*   `get_enemy_alliance()`
*   `move_sunit()`
*   `reassign_sunits()`
*   `remove_sunit()`
*   `set_activation_callback()`
*   `set_debug()`
*   `remove_sunit()`
*   `set_activation_callback()`
*   `set_debug()`
*   `set_routing_callback()`
*   `sort_zone_list()`
*   `start()`
*   `stop()`
*   `sunits_have_taken_damage()`
*   `units_in_area()`
*   `update_unit_monitor()`
*   `watch_for_activate()`
*   `watch_for_deactivate()`
*   `watch_units_routing()`

## zone_manager
The `zone_manager` interface manages individual zones.


*   `new()`
*   `assess_threat()`
*   `assess_threat_by_units()`
*   `assess_threat_to_line()`
*   `get_centre_pos()`
*   `get_occupier()`
*   `get_occupier_start_hp()`
*   `get_threat()`
*   `is_occupied()`
*   `is_preferred()`
*   `is_usable()`
*   `set_occupier()`
*   `set_points()`
*   `set_preferred()`
*   `set_usable()`


## cinematic_script
The `cinematic_script` interface provides functions for cinematic scripting.


*   `cindy_playback()`
*   `cindy_playback_no_camera()`
*   `new()`
*   `stop_cindy_playback()`
*   `stop_cindy_playback_no_camera()`

## convex_area
The `convex_area` interface represents a convex area.


*   `count()`
*   `is_in_area()`
*   `item()`
*   `new()`
*   `number_in_area()`
*   `process_points()`
*   `standing_is_in_area()`
*   `standing_number_in_area()`
*   `validate_points()`

## cutscene
The `cutscene` interface provides functions for managing cutscenes.


*   `action()`
*   `enable_debug_timestamps()`
*   `enable_ui_on_end()`
*   `finish()`
*   `is_active()`
*   `is_any_cutscene_running()`
*   `is_playing_sound()`
*   `new()`
*   `output_debug_timestamp()`
*   `play_sound()`
*   `process_next_action()`
*   `release()`
*   `restore_camera_and_release()`
*   `set_close_advisor_on_end()`
*   `set_debug()`
*   `set_do_not_end()`
*   `set_intro_pan_time()`
*   `set_music()`
*   `set_music_resume_auto_playback()`
*   `set_post_cutscene_fade_time()`
*   `set_relative_mode()`
*   `set_restore_cam()`
*   `set_restore_cam_time()`
*   `set_should_release_players_army()`
*   `set_show_cinematic_bars()`
*   `set_skip_camera()`
*   `set_skippable()`
*   `set_wait_for_advisor_on_end()`
*   `set_wait_for_vo_on_end()`
*   `skip()`
*   `start()`
*   `subtitles()`
*   `suppress_unit_voices()`
*   `wait_for_advisor()`
*   `wait_for_vo()`

## decision_point
The `decision_point` interface represents a decision point in escape routes.


*   `add_escape_route()`
*   `get_detect_obj()`
*   `get_detection_radius()`
*   `get_next_route()`
*   `is_caution_point()`
*   `is_detect_area()`
*   `is_exit_point()`
*   `new()`
*   `set_caution_point()`
*   `set_debug()`
*   `set_detection_radius()`
*   `set_exit_point()`

## escape_manager
The `escape_manager` interface manages escape routes.


*   `decision_point_reached()`
*   `new()`
*   `next_route()`
*   `set_caution_callback()`
*   `set_debug()`
*   `set_escape_callback()`
*   `set_walk_to_waypoint()`
*   `start()`
*   `sunit_routing()`

## escape_route
The `escape_route` interface represents an individual escape route.


*   `add_route()`
*   `calculate_threat()`
*   `get_end_point()`
*   `get_route_points()`
*   `new()`
*   `set_debug()`

## event_handler
The `event_handler` interface manages event listeners.


*   `add_listener()`
*   `attach_to_event()`
*   `clean_listeners()`
*   `event_callback()`
*   `list_events()`
*   `new()`
*   `remove_listener()`

## firestorm_manager
The `firestorm_manager` interface manages firestorm effects.


*   `accelerate_burning()`
*   `add_armies()`
*   `add_convex_area()`
*   `building_is_in_area()`
*   `contains_building()`
*   `damage_unit()`
*   `extinguish_fire()`
*   `get_building_record()`
*   `heavily_damage_unit()`
*   `ignite_building()`
*   `inc_hurt_count()`
*   `make_fireproof()`
*   `new()`
*   `pre_ignite_building()`
*   `process_hurtareas()`
*   `retard_burning()`
*   `set_accelerator_modifier()`
*   `set_burn_notification()`
*   `set_burn_notification_alliance()`
*   `set_deathzone()`
*   `set_debug()`
*   `set_hurt_radius()`
*   `set_max_flammable_dist()`
*   `set_max_flammable_time()`
*   `set_min_flammable_time()`
*   `set_notification()`
*   `set_retardation_modifier()`
*   `spread_fire()`
*   `start()`
*   `watch_fire()`

## generated_army
The `generated_army` interface represents a generated army.


*   `attack()`
*   `attack_on_message()`
*   `build_sunits()`
*   `defend()`
*   `defend_on_message()`
*   `get_allied_and_enemy_forces()`
*   `get_casualty_rate()`
*   `get_rout_proportion()`
*   `message_on_casualties()`
*   `message_on_proximity_to_enemy()`
*   `message_on_rout_proportion()`
*   `message_on_seen_by_enemy()`
*   `new()`
*   `release()`
*   `release_control_of_all_sunits()`
*   `release_on_message()`
*   `take_control_of_all_sunits()`

## generated_battle
The `generated_battle` interface represents a generated battle.


*   `advice_on_message()`
*   `build_armies()`
*   `get_allied_force()`
*   `get_army()`
*   `get_enemy_force()`
*   `has_battle_started()`
*   `message_on_time_offset()`
*   `new()`
*   `start_battle()`
*   `start_deployment()`

## hiding_place
The `hiding_place` interface represents a hiding place.


*   `add_position()`
*   `add_trigger_area()`
*   `get_trigger_radius()`
*   `is_taken()`
*   `new()`
*   `set_taken()`
*   `set_taken_callback()`
*   `set_trigger_radius()`
*   `taken_by()`

## hurt_area
The `hurt_area` interface represents an area that causes damage.


*   `new()`
*   `process()`
*   `set_damage_per_tick()`
*   `set_debug()`
*   `start()`
*   `stop()`

## iterator
The `iterator` interface provides iteration functionality.


*   `get_next()`
*   `new()`
*   `reset()`

## patrol_manager
The `patrol_manager` interface manages unit patrols.


*   `add_waypoint()`
*   `arrived_at_waypoint()`
*   `cache_current_unit_pos()`
*   `complete()`
*   `get_angle_to_pos()`
*   `handle_unit_routing()`
*   `intercept()`
*   `is_enemy_in_range()`
*   `is_in_range_of_patrol_path_segment()`
*   `loop()`
*   `move_to_current_waypoint()`
*   `move_to_next_waypoint()`
*   `new()`
*   `restart()`
*   `resume_patrol()`
*   `set_abandon_callback()`
*   `set_completion_callback()`
*   `set_debug()`
*   `set_debug_all()`
*   `set_force_run()`
*   `set_intercept_callback()`
*   `set_intercept_time()`
*   `set_naval()`
*   `set_rout_callback()`
*   `set_stop_on_intercept()`
*   `set_stop_on_rout()`
*   `set_walk_speed()`
*   `set_waypoint_threshold()`
*   `set_width()`
*   `start()`
*   `stop()`
*   `stop_running_processes()`
*   `watch_for_unit_routing()`

## script_ai_planner
The `script_ai_planner` interface provides functions for AI planning.


*   `add_sunits()`
*   `any_controlled_sunit_standing()`
*   `attack_closest_unit()`
*   `attack_force()`
*   `attack_unit()`
*   `defend_force()`
*   `defend_position()`
*   `defend_position_action()`
*   `defend_position_of_sunit()`
*   `defend_position_of_sunit_complete()`
*   `get_centre_point()`
*   `merge_into()`
*   `move_to_position()`
*   `move_to_position_action()`
*   `move_to_position_of_sunit()`
*   `move_to_position_of_sunit_complete()`
*   `new()`
*   `patrol()`
*   `remove_sunits()`
*   `set_debug()`
*   `set_debug_all()`
*   `set_perform_patrol_prox_test()`
*   `set_should_reorder()`
*   `track_towards_merge_target()`

## script_messager
The `script_messager` interface provides functions for script messaging.


*   `add_listener()`
*   `dump()`
*   `new()`
*   `set_debug()`
*   `trigger_message()`

## script_unit
The `script_unit` interface represents a script-controlled unit.


*   `goto_start_location()`
*   `move_to_position_offset()`
*   `new()`
*   `set_current_patrol()`
*   `stop_current_patrol()`
*   `teleport_to_cached_location()`
*   `teleport_to_start_location()`
*   `teleport_to_start_location_offset()`

## teleport_squad
The `teleport_squad` interface manages teleporting squads.


*   `add_hiding_places()`
*   `add_sunits()`
*   `are_sunits_routing()`
*   `attack()`
*   `do_teleport()`
*   `force_teleport()`
*   `get_planner()`
*   `is_enemy_in_trigger_areas()`
*   `is_visible_to_enemy()`
*   `new()`
*   `set_attack_callback()`
*   `set_should_attack()`
*   `setup_planner()`
*   `start_watches_for_hiding_place()`
*   `stop_watches()`
*   `teleport()`

## waypoint
The `waypoint` interface represents a waypoint.


## GAME
The `GAME` interface provides global game functions and interactions.


*   `add_agent_experience()`
*   `add_attack_of_opportunity_overrides()`
*   `add_building_model_override()`
*   `add_circle_area_trigger()`
*   `add_custom_battlefield()`
*   `add_development_points_to_region()`
*   `add_event_restricted_building_record()`
*   `add_event_restricted_building_record_for_faction()`
*   `add_event_restricted_unit_record()`
*   `add_event_restricted_unit_record_for_faction()`
*   `add_exclusion_zone()`
*   `add_location_trigger()`
*   `add_marker()`
*   `add_outline_area_trigger()`
*   `add_restricted_building_level_record()`
*   `add_restricted_building_level_record_for_faction()`
*   `add_settlement_model_override()`
*   `add_time_trigger()`
*   `add_unit_model_overrides()`
*   `add_visibility_trigger()`
*   `advance_to_next_campaign()`
*   `allow_player_to_embark_navies()`
*   `apply_effect_bundle()`
*   `apply_effect_bundle_to_characters_force()`
*   `apply_effect_bundle_to_force()`
*   `attack()`
*   `autosave_at_next_opportunity()`
*   `award_experience_level()`
*   `cai_strategic_stance_manager_block_all_stances_but_that_specified_towards_target_faction()`
*   `cai_strategic_stance_manager_clear_all_blocking_between_factions()`
*   `cai_strategic_stance_manager_clear_all_promotions_between_factions()`
*   `cai_strategic_stance_manager_force_stance_update_between_factions()`
*   `cai_strategic_stance_manager_promote_specified_stance_towards_target_faction()`
*   `cai_strategic_stance_manager_promote_specified_stance_towards_target_faction_by_number()`
*   `cai_strategic_stance_manager_set_stance_blocking_between_factions_for_a_given_stance()`
*   `cai_strategic_stance_manager_set_stance_promotion_between_factions_for_a_given_stance()`
*   `cancel_actions_for()`
*   `cinematic()`
*   `compare_localised_string()`
*   `create_agent()`
*   `create_force()`
*   `disable_elections()`
*   `disable_end_turn()`
*   `disable_movement_for_ai_under_shroud()`
*   `disable_movement_for_character()`
*   `disable_movement_for_faction()`
*   `disable_rebellions_worldwide()`
*   `disable_saving_game()`
*   `disable_shopping_for_ai_under_shroud()`
*   `disable_shortcut()`
*   `dismiss_advice()`
*   `dismiss_advice_at_end_turn()`
*   `display_turns()`
*   `enable_auto_generated_missions()`
*   `enable_movement_for_character()`
*   `enable_movement_for_faction()`
*   `enable_ui()`
*   `end_turn()`
*   `exempt_region_from_tax()`
*   `force_add_ancillary()`
*   `force_add_skill()`
*   `force_add_trait()`
*   `force_agent_action_success_for_human()`
*   `force_assassination_success_for_human()`
*   `force_change_cai_faction_personality()`
*   `force_character_force_into_stance(char_cqi, stance)`
*   `force_declare_war()`
*   `force_diplomacy()`
*   `force_garrison_infiltration_success_for_human()`
*   `force_make_peace()`
*   `force_make_trade_agreement()`
*   `force_make_vassal()`
*   `force_rebellion_in_region()`
*   `grant_faction_handover()`
*   `grant_unit()`
*   `hide_character()`
*   `infect_force_with_plague()`
*   `infect_region_with_plague()`
*   `instant_set_building_health_percent()`
*   `instantly_dismantle_building()`
*   `instantly_repair_building()`
*   `is_new_game()`
*   `join_garrison()`
*   `kill_character()`
*   `leave_garrison()`
*   `load_named_value()`
*   `lock_technology()`
*   `make_neighbouring_regions_seen_in_shroud()`
*   `make_neighbouring_regions_visible_in_shroud()`
*   `make_region_seen_in_shroud()`
*   `make_region_visible_in_shroud()`
*   `make_sea_region_seen_in_shroud()`
*   `make_sea_region_visible_in_shroud()`
*   `make_son_come_of_age()`
*   `model()`
*   `modify_next_autoresolve_battle()`
*   `move_to(char_cqi, x, y, cmd_queue)`
*   `new()`
*   `optional_extras_for_episodics()`
*   `override_ui()`
*   `pending_auto_show_messages()`
*   `register_instant_movie()`
*   `register_movies()`
*   `register_outro_movie()`
*   `remove_area_trigger()`
*   `remove_attack_of_opportunity_overrides()`
*   `remove_barrier()`
*   `remove_building_model_override()`
*   `remove_custom_battlefield()`
*   `remove_effect_bundle()`
*   `remove_effect_bundle_from_characters_force()`
*   `remove_effect_bundle_from_force()`
*   `remove_event_restricted_building_record()`
*   `remove_event_restricted_building_record_for_faction()`
*   `remove_event_restricted_unit_record()`
*   `remove_event_restricted_unit_record_for_faction()`
*   `remove_location_trigger()`
*   `remove_marker()`
*   `remove_restricted_building_level_record()`
*   `remove_restricted_building_level_record_for_faction()`
*   `remove_settlement_model_override()`
*   `remove_time_trigger()`
*   `remove_visibility_trigger()`
*   `render_campaign_to_file()`
*   `replenish_action_points()`
*   `restore_shroud_from_snapshot()`
*   `save_named_value()`
*   `scroll_camera()`
*   `scroll_camera_with_direction()`
*   `seek_exchange()`
*   `set_ai_uses_human_display_speed()`
*   `set_campaign_ai_force_all_factions_boardering_human_vassals_to_have_invasion_behaviour()`
*   `set_campaign_ai_force_all_factions_boardering_humans_to_have_invasion_behaviour()`
*   `set_character_experience_disabled()`
*   `set_character_skill_tier_limit()`
*   `set_event_generation_enabled()`
*   `set_general_offered_dilemma_permitted()`
*   `set_ignore_end_of_turn_public_order()`
*   `set_liberation_options_disabled()`
*   `set_looting_options_disabled_for_human()`
*   `set_map_bounds()`
*   `set_non_scripted_ancillaries_disabled()`
*   `set_non_scripted_traits_disabled()`
*   `set_public_order_of_province_for_region()`
*   `set_tax_disabled()`
*   `set_tax_rate()`
*   `set_technology_research_disabled()`
*   `set_ui_notification_of_victory_disabled()`
*   `set_zoom_limit()`
*   `show_message_event()`
*   `show_shroud()`
*   `shown_message()`
*   `speedup_active()`
*   `steal_user_input()`
*   `stop_camera()`
*   `stop_user_input()`
*   `take_shroud_snapshot()`
*   `technology_osmosis_for_playables_enable_all()`
*   `technology_osmosis_for_playables_enable_culture()`
*   `toggle_speedup()`
*   `transfer_region_to_faction()`
*   `treasury_mod()`
*   `trigger_custom_dilemma()`
*   `trigger_custom_incident()`
*   `trigger_custom_mission()`
*   `unhide_character()`
*   `win_next_autoresolve_battle()`
*   `zero_action_points()`


## BUILDING_LIST_SCRIPT_INTERFACE
The `BUILDING_LIST_SCRIPT_INTERFACE` manages a list of buildings.


*   `is_empty()`
*   `item_at()`
*   `new()`
*   `num_items()`

## BUILDING_SCRIPT_INTERFACE
The `BUILDING_SCRIPT_INTERFACE` provides information about a building.


*   `chain()`
*   `faction()`
*   `model()`
*   `name()`
*   `new()`
*   `region()`
*   `slot()`
*   `superchain()`

## CAMPAIGN_AI_SCRIPT_INTERFACE
The `CAMPAIGN_AI_SCRIPT_INTERFACE` provides functions for interacting with campaign AI.


*   `new()`
*   `strategic_stance_between_factions()`
*   `strategic_stance_between_factions_available()`
*   `strategic_stance_between_factions_is_being_blocked()`
*   `strategic_stance_between_factions_is_being_blocked_until()`
*   `strategic_stance_between_factions_promotion_current_level()`
*   `strategic_stance_between_factions_promotion_end_level()`
*   `strategic_stance_between_factions_promotion_end_round()`
*   `strategic_stance_between_factions_promotion_is_active()`
*   `strategic_stance_between_factions_promotion_or_blocking_is_set()`
*   `strategic_stance_between_factions_promotion_start_level()`
*   `strategic_stance_between_factions_promotion_start_round()`

## CAMPAIGN_MISSION_SCRIPT_INTERFACE
The `CAMPAIGN_MISSION_SCRIPT_INTERFACE` provides information about campaign missions.


*   `model()`
*   `new()`

## CAMPAIGN_POLITICS_SCRIPT_INTERFACE
The `CAMPAIGN_POLITICS_SCRIPT_INTERFACE` provides functions for interacting with campaign politics.


*   `get_current_politics_government_type()`
*   `get_parties()`
*   `government_type_key()`
*   `new()`
*   `state_changed()`

## CHARACTER_LIST_SCRIPT_INTERFACE
The `CHARACTER_LIST_SCRIPT_INTERFACE` manages a list of characters.


*   `is_empty()`
*   `item_at()`
*   `new()`
*   `num_items()`

## CHARACTER_SCRIPT_INTERFACE
The `CHARACTER_SCRIPT_INTERFACE` provides information about a character.


*   `action_points_per_turn()`
*   `action_points_remaining_percent()`
*   `age()`
*   `battles_fought()`
*   `battles_won()`
*   `body_guard_casulties()`
*   `character_type(agent_type)`
*   `cqi()`
*   `defensive_ambush_battles_fought()`
*   `defensive_ambush_battles_won()`
*   `defensive_battles_fought()`
*   `defensive_battles_won()`
*   `defensive_naval_battles_fought()`
*   `defensive_naval_battles_won()`
*   `defensive_sieges_fought()`
*   `defensive_sieges_won()`
*   `display_position_x()`
*   `display_position_y()`
*   `faction()`
*   `forename()`
*   `fought_in_battle()`
*   `garrison_residence()`
*   `get_forename()`
*   `get_political_party_id()`
*   `get_surname()`
*   `has_ancillary(anciliary)`
*   `has_garrison_residence()`
*   `has_military_force()`
*   `has_recruited_mercenaries()`
*   `has_region()`
*   `has_skill(skill)`
*   `has_spouse()`
*   `has_trait(trait)`
*   `in_port()`
*   `in_settlement()`
*   `is_ambushing()`
*   `is_besieging()`
*   `is_blockading()`
*   `is_carrying_troops()`
*   `is_deployed()`
*   `is_embedded_in_military_force()`
*   `is_faction_leader()`
*   `is_hidden()`
*   `is_male()`
*   `is_polititian()`
*   `logical_position_x()`
*   `logical_position_y()`
*   `military_force()`
*   `model()`
*   `new()`
*   `number_of_traits()`
*   `offensive_ambush_battles_fought()`
*   `offensive_ambush_battles_won()`
*   `offensive_battles_fought()`
*   `offensive_battles_won()`
*   `offensive_naval_battles_fought()`
*   `offensive_naval_battles_won()`
*   `offensive_sieges_fought()`
*   `offensive_sieges_won()`
*   `percentage_of_own_alliance_killed()`
*   `performed_action_this_turn()`
*   `rank()`
*   `region()`
*   `routed_in_battle()`
*   `spouse()`
*   `surname()`
*   `trait_level()`
*   `trait_points()`
*   `turns_at_sea()`
*   `turns_in_enemy_regions()`
*   `turns_in_own_regions()`
*   `turns_without_battle_in_home_lands()`
*   `won_battle()`

## FACTION_LIST_SCRIPT_INTERFACE
The `FACTION_LIST_SCRIPT_INTERFACE` manages a list of factions.


*   `is_empty()`
*   `item_at()`
*   `new()`
*   `num_items()`

## FACTION_SCRIPT_INTERFACE
The `FACTION_SCRIPT_INTERFACE` provides information about a faction.


*   `allied_with()`
*   `ancillary_exists()`
*   `at_war()`
*   `character_list()`
*   `culture()`
*   `difficulty_level()`
*   `ended_war_this_turn()`
*   `faction_attitudes()`
*   `faction_leader()`
*   `government_type()`
*   `has_faction_leader()`
*   `has_food_shortage()`
*   `has_home_region()`
*   `has_researched_all_technologies()`
*   `has_technology()`
*   `home_region()`
*   `imperium_level()`
*   `is_human()`
*   `losing_money()`
*   `military_force_list()`
*   `model()`
*   `name()`
*   `new()`
*   `num_allies()`
*   `num_enemy_trespassing_armies()`
*   `num_factions_in_war_with()`
*   `num_generals()`
*   `num_trade_agreements()`
*   `politics()`
*   `politics_party_add_loyalty_modifier()`
*   `region_list()`
*   `research_queue_idle()`
*   `sea_trade_route_raided()`
*   `started_war_this_turn()`
*   `state_religion()`
*   `subculture()`
*   `tax_category()`
*   `tax_level()`
*   `total_food()`
*   `trade_resource_exists()`
*   `trade_route_limit_reached()`
*   `trade_ship_not_in_trade_node()`
*   `trade_value()`
*   `trade_value_percent()`
*   `treasury()`
*   `treasury_percent()`
*   `treaty_details()`
*   `unused_international_trade_route()`
*   `upkeep_expenditure_percent()`

## GARRISON_RESIDENCE_SCRIPT_INTERFACE
The `GARRISON_RESIDENCE_SCRIPT_INTERFACE` provides information about a garrison residence.


*   `army()`
*   `buildings()`
*   `faction()`
*   `has_army()`
*   `has_navy()`
*   `is_settlement()`
*   `is_slot()`
*   `is_under_siege()`
*   `model()`
*   `navy()`
*   `new()`
*   `region()`
*   `settlement_interface()`
*   `slot_interface()`
*   `unit_count()`

## MILITARY_FORCE_LIST_SCRIPT_INTERFACE
The `MILITARY_FORCE_LIST_SCRIPT_INTERFACE` manages a list of military forces.


*   `is_empty()`
*   `item_at(index)`
*   `new()`
*   `num_items()`

## MILITARY_FORCE_SCRIPT_INTERFACE
The `MILITARY_FORCE_SCRIPT_INTERFACE` provides information about a military force.


*   `character_list()`
*   `contains_mercenaries()`
*   `faction()`
*   `garrison_residence()`
*   `general_character()`
*   `has_garrison_residence()`
*   `has_general()`
*   `is_army()`
*   `is_navy()`
*   `model()`
*   `new()`
*   `unit_list()`
*   `upkeep()`

## MODEL_SCRIPT_INTERFACE
The `MODEL_SCRIPT_INTERFACE` provides access to various game model data.


*   `campaign_ai()`
*   `campaign_name()`
*   `campaign_type()`
*   `character_can_reach_character()`
*   `date_and_week_in_range()`
*   `date_in_range()`
*   `difficulty_level()`
*   `faction_is_local()`
*   `is_multiplayer()`
*   `is_player_turn()`
*   `new()`
*   `pending_battle()`
*   `player_steam_id_is_odd()`
*   `random_number()`
*   `random_percent()`
*   `season()`
*   `turn_number()`
*   `world()`

## NULL_SCRIPT_INTERFACE
The `NULL_SCRIPT_INTERFACE` represents a null script interface.


*   `new()`

## PENDING_BATTLE_SCRIPT_INTERFACE
The `PENDING_BATTLE_SCRIPT_INTERFACE` provides information about a pending battle.


*   `ambush_battle()`
*   `attacker()`
*   `attacker_battle_result()`
*   `attacker_commander_fought_in_battle()`
*   `attacker_commander_fought_in_melee()`
*   `attacker_is_stronger()`
*   `battle_type()`
*   `contested_garrison()`
*   `defender()`
*   `defender_battle_result()`
*   `defender_commander_fought_in_battle()`
*   `defender_commander_fought_in_melee()`
*   `failed_ambush_battle()`
*   `has_attacker()`
*   `has_contested_garrison()`
*   `has_defender()`
*   `is_active()`
*   `model()`
*   `naval_battle()`
*   `new()`
*   `night_battle()`
*   `percentage_of_attacker_killed()`
*   `percentage_of_attacker_routed()`
*   `percentage_of_defender_killed()`
*   `percentage_of_defender_routed()`
*   `seige_battle()`

## REGION_LIST_SCRIPT_INTERFACE
The `REGION_LIST_SCRIPT_INTERFACE` manages a list of regions.


*   `is_empty()`
*   `item_at()`
*   `new()`
*   `num_items()`

## REGION_MANAGER_SCRIPT_INTERFACE
The `REGION_MANAGER_SCRIPT_INTERFACE` manages regions in the game world.


*   `faction_region_list()`
*   `model()`
*   `new()`
*   `region_by_key(key)`
*   `region_list()`
*   `resource_exists_anywhere()`
*   `settlement_by_key(key)`
*   `slot_by_key(key)`

## REGION_SCRIPT_INTERFACE
The `REGION_SCRIPT_INTERFACE` provides information about a region.


*   `adjacent_region_list()`
*   `building_exists()`
*   `building_superchain_exists()`
*   `garrison_residence()`
*   `last_building_constructed_key()`
*   `majority_religion()`
*   `model()`
*   `name()`
*   `new()`
*   `num_buildings()`
*   `owning_faction()`
*   `province_name()`
*   `public_order()`
*   `region_wealth()`
*   `region_wealth_change_percent()`
*   `resource_exists()`
*   `sanitation()`
*   `settlement()`
*   `slot_list()`
*   `slot_type_exists()`
*   `squalor()`
*   `tax_income()`
*   `town_wealth_growth()`

## SETTLEMENT_SCRIPT_INTERFACE
The `SETTLEMENT_SCRIPT_INTERFACE` provides information about a settlement.


*   `castle_slot()`
*   `commander()`
*   `display_position_x()`
*   `display_position_y()`
*   `faction()`
*   `has_castle_slot()`
*   `has_commander()`
*   `logical_position_x()`
*   `logical_position_y()`
*   `model()`
*   `new()`
*   `region()`
*   `slot_list()`

## SLOT_LIST_SCRIPT_INTERFACE
The `SLOT_LIST_SCRIPT_INTERFACE` manages a list of building slots.


*   `buliding_type_exists()`
*   `is_empty()`
*   `item_at(index)`
*   `new()`
*   `num_items()`
*   `slot_type_exists()`

## SLOT_SCRIPT_INTERFACE
The `SLOT_SCRIPT_INTERFACE` provides information about a building slot.


*   `building()`
*   `faction()`
*   `has_building()`
*   `model()`
*   `name()`
*   `new()`
*   `region()`
*   `type()`

## UNIT_LIST_SCRIPT_INTERFACE
The `UNIT_LIST_SCRIPT_INTERFACE` manages a list of units.


*   `has_unit()`
*   `is_empty()`
*   `item_at(index)`
*   `new()`
*   `num_items()`

## UNIT_SCRIPT_INTERFACE
The `UNIT_SCRIPT_INTERFACE` provides information about a unit.


*   `faction()`
*   `force_commander()`
*   `has_force_commander()`
*   `has_unit_commander()`
*   `is_land_unit()`
*   `is_naval_unit()`
*   `military_force()`
*   `model()`
*   `new()`
*   `percentage_proportion_of_full_strength()`
*   `unit_category()`
*   `unit_class()`
*   `unit_commander()`
*   `unit_key()`

## WORLD_SCRIPT_INTERFACE
The `WORLD_SCRIPT_INTERFACE` provides access to global world data.


*   `ancillary_exists()`
*   `faction_by_key()`
*   `faction_exists()`
*   `faction_list()`
*   `model()`
*   `new()`
*   `region_manager()`

## HudManager
The `HudManager` interface manages the HUD.


*   `Dimensions()`
*   `MoveRelativeToHUD()`
*   `RegisterHud()`

## PanelManager
The `PanelManager` interface manages UI panels.


*   `ClearCachedComponent()`
*   `CloseAllPanels()`
*   `ClosePanel()`
*   `IsPanelOpen()`
*   `OpenPanel()`
*   `OpenPanels()`
*   `Reset()`

## effect
The `effect` interface provides functions for applying various effects.


*   `OpenBrowser()`
*   `add_agent_experience()`
*   `add_military_force_experience()`
*   `adjust_treasury()`
*   `advance_contextual_advice_thread()`
*   `advance_scripted_advice_thread()`
*   `advance_scripted_advice_thread_located()`
*   `advice()`
*   `ancillary()`
*   `historical_character()`
*   `historical_event()`
*   `remove_ancillary()`
*   `remove_trait()`
*   `rewind_scripted_advice()`
*   `suspend_contextual_advice()`
*   `trait()`

*   `new()`

## out
The `out` interface provides various output functions.


*   `design()`
*   `dylan()`
*   `kostas()`
*   `scott_b()`
*   `shane()`
*   `ting()`
*   `tom()`


## CampaignCharacter
The `CampaignCharacter` interface provides campaign character details.


*   `ActionPointsRatio()`
*   `Release()`
*   `new()`

## CampaignSettlement
The `CampaignSettlement` interface provides campaign settlement details.


*   `LabelDetails()`
*   `ListDetails()`
*   `Release()`
*   `Settlement()`
*   `new()`

## CampaignUI
The `CampaignUI` interface provides functions for interacting with the campaign UI.


*   `ClearSelection()`
*   `CurrentTabTypename()`
*   `GetCameraPosition()`
*   `HighlightComponent()`
*   `HighlightConstructionItem()`
*   `HighlightRecruitmentItem()`
*   `IsMultiplayer()`
*   `IsPreBattleTypeSiege()`
*   `SetCameraHeading()`
*   `SetCameraMaxTiltAngle()`
*   `SetCameraMinDistance()`
*   `SetCameraTarget()`
*   `SetCameraTargetInstant()`
*   `SetCameraZoom()`
*   `ToggleCinematicBorders()`
*   `ToggleScreenCover()`
*   `clear_highlights()`
*   `highlight_character()`
*   `highlight_position()`
*   `highlight_settlement()`
*   `unhighlight_character()`
*   `unhighlight_position()`
*   `unhighlight_settlement()`

## CoreUtils
The `CoreUtils` interface provides a collection of utility functions.


*   `Clamp()`
*   `CompareByValue()`
*   `CopyIntoTable()`
*   `CopyTable()`
*   `LoadTable()`
*   `Max()`
*   `Min()`
*   `NamespaceFile()`
*   `OffsetFrom()`
*   `PickFGColour()`
*   `PrintTable()`
*   `Require()`
*   `RoundToInt()`
*   `RupToInt()`
*   `SaveTable()`
*   `TimeString()`
*   `TruncToInt()`
*   `UnRequire()`
*   `UnRequireAll()`
*   `outputbitfield()`

## Cursor
The `Cursor` interface provides functions for cursor management.


*   `DistanceToBL()`
*   `Mode()`
*   `ModeString()`
*   `Modes()`
*   `SetMode()`
*   `new()`

## EpisodicScripting
The `EpisodicScripting` interface provides functions for episodic scripting.


*   `AddEventCallBack()`
*   `ClearEventCallbacks()`
*   `ClearMessageAutoShowOverrides()`
*   `DisableFeature()`
*   `EnableComponent()`
*   `EnableFeature()`
*   `HideComponent()`
*   `HighlightComponent()`
*   `HighlightConstructionItem()`
*   `HighlightRecruitmentItem()`
*   `InitFeature()`
*   `IsOnCampaignMap()`
*   `OnUICreated()`
*   `OverrideMessageAutoShow()`
*   `RevealComponent()`
*   `SetCampaign()`
*   `ShowHUD()`

## MPAvatar
The `MPAvatar` interface provides functions for multiplayer avatars.


*   `Free()`
*   `SetComponentTexture()`
*   `Valid()`
*   `new()`

## MessageManager
The `MessageManager` interface manages in-game messages.


*   `CanDismissAllMessages()`
*   `CheckForAutoOpen()`
*   `ClearMessagesFromEnv()`
*   `ClearOverrides()`
*   `ClosePanelIfNoMessage()`
*   `DestroyAllMessages()`
*   `DismissAllMessages()`
*   `HasMessagesStored()`
*   `HideAllMessages()`
*   `HideMessage()`
*   `HidingMessage()`
*   `InitMessageCallback()`
*   `OverrideAutoShow()`
*   `PendingAutoShowMessage()`
*   `ReInitialiseStackbase()`
*   `RestoreMessages()`
*   `SelectLayout()`
*   `SetCurrentMessageUnread()`
*   `ShowingMessage()`
*   `StoreMessages()`


## Keyboard
The `Keyboard` interface provides functions for keyboard input.


*   `DisableQuickload()`
*   `ReturnKey()`
*   `StealKey()`

## ScriptedValueRegistry
The `ScriptedValueRegistry` interface manages scripted values.


*   `LoadBool()`
*   `SaveBool()`
*   `new()`

## UIComponent
The `UIComponent` interface provides functions for interacting with UI components.


*   `Address()`
*   `Adopt()`
*   `AttachCustomControl()`
*   `Bounds()`
*   `CallbackId()`
*   `ChildCount()`
*   `CurrentAnimationId()`
*   `CurrentState()`
*   `CurrentStateUI()`
*   `DestroyChildren()`
*   `Dimensions()`
*   `Divorce()`
*   `DockingPoint()`
*   `Find()`
*   `FindPositionIntoCurrentText()`
*   `FindTextSnapPosition()`
*   `ForceEvent()`
*   `GetProperty()`
*   `GetStateText()`
*   `GetStateTextDetails()`
*   `GetTooltipText()`
*   `GlobalExists()`
*   `HasInterface()`
*   `Height()`
*   `Highlight()`
*   `Id()`
*   `InterfaceFunction()`
*   `IsCharPrintable()`
*   `IsDragged()`
*   `IsInteractive()`
*   `IsMouseOverChildren()`
*   `IsMoveable()`
*   `Layout()`
*   `LockPriority()`
*   `LuaCall()`
*   `MoveTo()`
*   `Parent()`
*   `PopulateTextures()`
*   `Position()`
*   `Priority()`
*   `PropagateImageColour()`
*   `PropagateOpacity()`
*   `PropagatePriority()`
*   `PropagateVisibility()`
*   `ReorderChildren()`
*   `Resize()`
*   `RestoreUIHeirarchy()`
*   `RunScript()`
*   `SaveUIHeirarchy()`
*   `SequentialFind()`
*   `SetDisabled()`
*   `SetDockingPoint()`
*   `SetDragged()`
*   `SetEventCallback()`
*   `SetGlobal()`
*   `SetImageColour()`
*   `SetImageRotation()`
*   `SetInteractive()`
*   `SetMoveable()`
*   `SetOpacity()`
*   `SetProperty()`
*   `SetState()`
*   `SetStateColours()`
*   `SetStateText()`
*   `SetStateTextDetails()`
*   `SetStateTextXOffset()`
*   `SetTooltipText()`
*   `SetVisible()`
*   `ShaderTechniqueGet()`
*   `ShaderTechniqueSet()`
*   `ShaderVarsGet()`
*   `ShaderVarsSet()`
*   `SimulateClick()`
*   `SimulateKey()`
*   `StealInputFocus()`
*   `StealShortcutKey()`
*   `TextDimensions()`
*   `TextShaderTechniqueSet()`
*   `TextShaderVarsGet()`
*   `TextShaderVarsSet()`
*   `TriggerAnimation()`
*   `TriggerShortcut()`
*   `UnLockPriority()`
*   `Visible()`
*   `Width()`
*   `WidthOfTextLine()`
*   `new()`
