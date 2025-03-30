---
title: lua loading
summary: How the game loads the lua scripts.
---

The game has 3 basic stages of loading lua scripts and populating lua state.
/// admonition | Attention
    type: attention
Lua state is not transferred between stages, so the game has to load all the scripts again.
///

- **frontend**:  
    - When the game is started, databases are loaded and just before the main menu is shown, the game loads the frontend lua scripts.
    - `frontend_scripted.lua`
- **campaign**:
    - After the user selects a campaign and the loading screen is shown, the game loads the campaign lua scripts.
    - `all_scripted.lua`
    - `campaigns/<campaign_name>/scripting.lua`
- **battle**:
    - When the user selects a battle and the loading screen is shown, the game loads the battle lua scripts.
    - `battle_scripted.lua`

    /// admonition | Battle API
        type: warning
    The battle API for interacting with the units won't be enabled by default see more link.
    ///
