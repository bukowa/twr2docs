---
title: cliexecute
summary: A brief description of my document.
---
This document contains the raw output from the game's CLI command dump, useful for direct reference.
These commands can be passed to `CliExecute` lua function.

```
===============
Sets up cindy live playback
cindy_playback <cindy_xml_path> <clear_animated_scenes on completion true/false> <expire_camera_on_completion true/false>
cindy live
cindy_playback
===============
record frame times to a file
frame_rate_log <log filename>
battle
frame_rate_log
===============
Destroys current camera cindy playback object
stop_cindy_playback <clear_animated_scenes true/false>
cindy live
stop_cindy_playback
===============
Set to true to disable ssteam error reporting
disable_steam_error_reporting <true|false>
disable_steam_error_reporting
disable_steam_error_reporting
===============
Which mode the application starts in
game_startup_mode <battle|campaign|campaign_edit|frontend|naval> opt:<xml name> opt:<xsd name> opt:<building list>
game_startup_mode
game_startup_mode
===============
pause_bink_video
pause_bink_video
pause_bink_video
pause_bink_video
===============
take screenshot
take_custom_screenshot <filename> <sizeX> <sizeY>
engine
take_custom_screenshot
===============
Exit from battle after it is finished without showing results screen. Useful for automated replay runs.
exit_after_battle <true/false>
empire_battle
force_exit_after_battle
===============
speed-up replay by a multiplier
replay_speed <multiplier>
battle
replay_speed
===============
playback camera track during battle
battle_camera_track_file <filename>
battle
battle_camera_track_file
===============
adjust current battle camera fov
battle_fov <fov in degrees>
battle camera manager
battle_fov
===============
temp placeholder for setting campaign map settings
campaign_camera_placeholder
battle
campaign_camera_placeholder
===============
uses networked sync logging in multiplayer battles (use in conjunction with mp_network_sync_logging)
mp_network_sync_logging_in_battles
mp_network_sync_logging_in_battles
===============
when enabled all sync logs will be outputted
Output all sync logs
output_sync_logs
output_sync_logs
===============
we can decide to ignore the crew
add crew to ships <true|false>
add crew to ships
add_crew
===============
test_square_meta_data
test_square_meta_data
test_square_meta_data
test_square_meta_data
===============
debug_replay
debug_replay
===============
disables cursor intersections with 3d battle objects
disable_battle_cursor_intersection
battle
disable_battle_cursor_intersection
===============
toggle_building_shadow_capsules
battle
toggle_building_shadow_capsules
===============
toggle_building_lites_shadow_capsules
battle
toggle_building_lites_shadow_capsules
===============
toggle_projectiles_damage
battle
toggle_projectiles_damage
===============
toggle_unit_lanterns
battle
toggle_unit_lanterns
===============
Sets up campaign rendering
render_campaign <out_folder> <frame_name> <frames_per_second> <motion_blur_frames> <duration>
render_campaign_to_file
render_campaign_to_file
===============
campaign_cam_move
campaign_cam_move
campaign_cam_move
campaign_cam_move
===============
render_stat
empire_battle
campaign_stat
===============
toggle_campaign_shadow_capsules
campaign
toggle_campaign_shadow_capsules
===============
check_loc
===============
Destroy the record of the displayed advisories.
reset_advisories
advice
reset_advisories
===============
keyboard_shortcuts_disabled
keyboard
keyboard_shortcuts_disabled
===============
auto_run_script
Specify an auto run script to execute
Frontend
auto_run_script
===============
sets gigantic army budget in multiplayer battles
mp_army_budget_gigantic
mp_army_budget_gigantic
===============
Clears all component templates from the cache so the next time they are accessed they are re-loaded from the template library or disk
clear_template_cache
clear_template_cache
===============
skip_avatar_creation
skip_avatar_creation
go_to_battle_list
===============
dock_ui
===============
toggle_1bit_alpha
===============
enable_ai_mp
enable_ai_mp
enable_ai_mp
===============
set_palette_entry
===============
adds test unit effect icon for ui
add_unit_effect_icon <unit_special_ability_record index>
battle ui
add_unit_effect_icon
===============
Redirect the non-pack (and mod pack) file search
add_working_directory <directory name>
add_working_directory
===============
Audit the VFS
audit_vfs
audit_vfs
===============
Exclude pack file from the virtual file system
exclude_pack_file <pack file name>
exclude_pack_file
===============
list the commands
help
system
help
===============
Add a mod to the startup list
mod <file name>
===============
Set the source directory of design data
set_design_directory <directory name>
set_design_directory
===============
test the command parser
test_cmd p1 p2 p3 [blib=blib value] [blab=blab value] [blob=blob value]
system
test_cmd
===============
compile_all_shaders
warscape
compile_all_shaders
===============
disable_gpu_profiler
warscape
disable_gpu_profiler
===============
force_rigid_lod
warscape
force_rigid_lod
===============
cache fxc/hlsl file timestamps
warscape
fxc_timestamp_cache
===============
reloads single texture from disk
reload_texture filename
texture_manager
reload_texture
===============
render_stat
warscape
render_stats
===============
set_shader_path
engine
set_shader_path
===============
show all textures using this RC
texture_manager_show_rc <rc_name>
Texture Manager
texture_manager_show_rc
===============
always_load_tile_database
warscape
always_load_tile_database
===============
render_stat
warscape
begin_profile
===============
report_rigid_models
warscape
report_rigid_models
===============
Tick Simulation
Tick simulation
rigid
rigid_simulation_step
===============
set_skeleton_bone_limit
set_skeleton_bone_limit
set_skeleton_bone_limit
set_skeleton_bone_limit
===============
Load light xml
load_light_xml <filename>
load_light_xml
load_light_xml
===============
texdbg
texdbg
texdbg
texdbg
===============
load tile database in parallel (faster)
warscape
tile_database_parallel_load
===============
toggle_terrain_vtex
toggle_terrain_vtex
toggle_terrain_vtex
toggle_terrain_vtex
===============
upgrade_tile
upgrade_tile
upgrade_tile
upgrade_tile
===============
vtex_request_page_each_frame
vtex_request_page_each_frame
vtex_request_page_each_frame
vtex_request_page_each_frame
===============
Sets up cindy live no camera playback
cindy_playback_no_camera <cindy_xml_path> <clear_animated_scenes on completion true/false>
cindy live
cindy_playback_no_camera
===============
play at predictable frame rate
frame_rate_test_fps fps
battle
frame_rate_test_fps
===============
Destroys current camera cindy no camera playback object
stop_cindy_playback_no_camera <clear_animated_scenes true/false>
cindy live
stop_cindy_playback_no_camera
===============
log the frame rate
benchmark false|true
system
benchmark
===============
take screenshot
hdr_screenshot
engine
hdr_screenshot
===============
play_bink_video
play_bink_video
play_bink_video
play_bink_video
===============
Activate campaign AI map data processing during the startpos processing.
process_campaign_ai_map_data
process_campaign_ai_map_data
process_campaign_ai_map_data
===============
Adds name to list of campaigns to preprocess
process_campaign_startpos name
process_campaign_startpos
process_campaign_startpos
===============
quit_after_campaign_processing
quit_after_campaign_processing
quit_after_campaign_processing
===============
resume_bink_video
resume_bink_video
resume_bink_video
resume_bink_video
===============
take screenshot
screenshot
engine
screenshot2
===============
take screenshot
screenshot
engine
screenshot3
===============
take screenshot
screenshot
engine
screenshot4
===============
take screenshot
screenshot
engine
screenshot
===============
take screenshot
screenshot
engine
screenshot_360
===============
take screenshot
screenshot
engine
screenshot_mul
===============
Shows specific piece of advice given the advice_levels_key
show_advice <advice_thread_key>
advice
show_advice
===============
skip directX version check
skip_directx_version_check
engine
skip_directx_version_check
===============
report string memory usage
report
strings
string_report
===============
restart_replay
restart_replay
restart_replay
restart_replay
===============
adjust battle camera default fov
battle_default_fov <fov in degrees>
battle camera manager
battle_default_fov
===============
adjust current battle camera depth of field
battle_dof <focus_distance> <focal_length> <blur_size>
battle camera manager
battle_dof
===============
enable tbb tick task
battle_enable_tbb_tick_task <true|false>
battle
battle_enable_tbb_tick_task
===============
enable recording of camera track
record_battle_camera <true|false>
battle
record_battle_camera
===============
toggle_entity_shadow_capsules
battle
toggle_entity_shadow_capsules
===============
toggle_naval_shadow_capsules
campaign
toggle_naval_shadow_capsules
===============
toggle_tree_shadow_capsules
battle
toggle_tree_shadow_capsules
===============
toggle_projectiles_ignite_buildings
battle
toggle_projectiles_ignite_buildings
===============
Allow the campaign to be rendered into files by MOVIE_MAKER
enable_campaign_render_to_file
enable_campaign_render_to_file
===============
campaign
fast_campaign_target
===============
campaign
fast_campaign_toggle
===============
Forces the first round of a given dilemma/incident to a new value
force_first_round <dillema/incident> <first_round>
campaign
force_first_round
===============
Fix random seed for battle and campaign setup
Fix random seed
Random seed
constant_random_seed
===============
Enable one or all types of ai behaviour monitoring.  This command can be used multiple times to enable a specific set of monitoring.
enable_campaign_ai_behaviour_monitoring <army_fragmentation|army_idle_ungarrisoned|army_stuck_on_navy|diplomatic_indecision|suboptimal_recruitment|non_trade_navy_on_trade_node|indecisive_movement|all>
enable_campaign_ai_behaviour_monitoring
enable_campaign_ai_behaviour_monitoring
===============
mouse_cursor_disabled
mouse
mouse_cursor_disabled
===============
change the default ui skin
ui_skin_hack
ui_skin_hack
===============
set_battle_size
set_battle_size
set_battle_size
set_battle_size
===============
automatically match players and (clients only) ready-up
mp_automatch
mp_automatch
===============
which xml to use for multiplayer battle
mp_battle_xml <xml name>
mp_battle_xml
mp_battle_xml
===============
enables hosting and joining by anyone, not just original players
mp_campaign_all_resume_any_players
mp_campaign_all_resume_any_players
===============
when enabled, data checksum will not prevent from joining
Data checksum always succeeds
mp_data_checksum_pass
mp_data_checksum_pass
===============
when disabled, a desync will not cause a disconnection
Multiplayer Desync Disconnects
mp_desync_kick_enabled
mp_desync_kick_enabled
===============
when enabled, executable checksum will not prevent from joining
Exe checksum always succeeds
mp_exe_checksum_pass
mp_exe_checksum_pass
===============
when ignored, an unexpected disconnection from the online service will not cause a player to leave the game
Ignore Online Service Disconnection
mp_ignore_online_service_disco
mp_ignore_online_service_disco
===============
uses extreme sync logging in multiplayer
mp_network_sync_logging
mp_network_sync_logging
===============
when enabled, the game will never host a Quickgame battle (it will only try to join)
Quickgame Never Host
mp_quick_match_never_host
mp_quick_match_never_host
===============
when disabled, stalls will never cause a disconnect
Multiplayer Stall Disconnects
mp_stall_disconnect_disabled
mp_stall_disconnect_disabled
===============
report_missing_ui_images
report_missing_ui_images
report_missing_ui_images
===============
Overrides coords used for campaign battle generator
override_generator_coords <x> <y>
override_generator_coords
override_generator_coords
===============
Swaps to the keyset named and remaps all keys
use_keyset
keyboard
use_keyset
===============
Use to test experience gains
add_unit_experience <experience
battle ui
add_unit_experience
===============
Clears the workign data directories
clear_paths
clear_paths
===============
Create a documentation file of all CLI commands, tweaks, custom Lua commands and Lua-response-enabled messages
docudemon
system
docudemon
===============
Import all mod packs
import_all_mods
import_all_mods
===============
load this preference file
preference \
system
preferences
===============
quit the application
quit
system
quit
===============
lhs pack is required by rhs pack (lhs < rhs): lhs will be loaded first and used by rhs pack
set_pack_file_dependency <pack file name> <pack file name>
set_pack_file_dependency
===============
lhs pack supersedes rhs pack (lhs < rhs): lhs will be searched before rhs for files
set_pack_file_precedence <pack file name> <pack file name>
set_pack_file_precedence
===============
Prints search paths in vfs tab
show_paths
show_paths
===============
Dumps the render statistics to a CSV file in App Data/The Creative Assembly/log/graphics. Specify the file name as argument to this command.
Dump Render Stats to File
dump_render_stats
dump_render_stats
===============
enable_gpu_profiler
warscape
enable_gpu_profiler
===============
Flush non visible sprites
Flush non visible sprites
flush_non_visible_sprites
===============
report_texture_usage
warscape
report_texture_usage
===============
set_shadowmap_fade_range
set_shadowmap_fade_range
set_shadowmap_fade_range
set_shadowmap_fade_range
===============
set_ui_scale
warscape
set_ui_scale
===============
animation_texture_count
animation_texture_count
animation_texture_count
===============
enable_rigid_tesellation
tesselation
enable_rigid_tesellation
===============
render_stat
warscape
end_profile
===============
set_terrain_far_distance_in_tiles
warscape
set_terrain_far_distance_in_tiles
===============
calculate terrain height map in parallel (faster)
warscape
terrain_height_calc_parallel
===============
force_lq_lf_height_map
force_lq_lf_height_map
force_lq_lf_height_map
force_lq_lf_height_map
===============
set_terrain_season
set_terrain_season
set_terrain_season
set_terrain_season
===============
set_terrain_texture_params
set_terrain_texture_params
set_terrain_texture_params
set_terrain_texture_params
===============
terrain_enable_battle_vtex
terrain_enable_battle_vtex
terrain_enable_battle_vtex
terrain_enable_battle_vtex
===============
terrain_enable_campaign_vtex
terrain_enable_campaign_vtex
terrain_enable_campaign_vtex
terrain_enable_campaign_vtex
===============
terrain_write_html
terrain_write_html
terrain_write_html
terrain_write_html
===============
terrain_write_html
terrain_write_html
terrain_write_html_area
terrain_write_html_area
===============
terrain_write_html
terrain_write_html
terrain_write_html_around_camera
terrain_write_html_around_camera
===============
texdbg_add
texdbg_add
texdbg_add
texdbg_add
===============
texdbg_show
texdbg_show
texdbg_show
texdbg_show
===============
Compile and load debug shaders
use_debug_shaders
use_debug_shaders
use_debug_shaders
===============
vtex_set_render_debug
vtex_set_render_debug
vtex_set_render_debug
vtex_set_render_debug
===============
vtex_sync_gpu_page_table
vtex_sync_gpu_page_table
vtex_sync_gpu_page_table
vtex_sync_gpu_page_table

Total valid functions with matches: 147

```