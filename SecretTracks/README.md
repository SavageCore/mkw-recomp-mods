# SecretTracks (mkw-recomp mod)

The Switch `secrettracks.zip` mod, shipped for mkw-recomp for MKW 1.8.0: import the `SecretTracks/`
folder from the start screen's Mods page. Unlocks the secret track variants (Peach Beach, Desert
Hills, DK Pass, MooMoo Farm, West City, ShyGuy Bazaar, First Circuit, Koopa Troopa Beach, Central).

| Part | What it does |
|---|---|
| `romfs/System/GymlArchive/general_format.Product_180.sarc.zs` | 10 grown `CourseAreaGParam` members, 1 changed `CourseGParam`, 15 added members (minimap + preloads) |
| `romfs/Mals/...` | `MsgMain.msarc` (EUen/USen, track names) + `Ver180.msarc` (1.8.0 update-message mechanism, shipped verbatim) |
| `romfs/System/Resource/...rsizetable.zs` | the mod's size table for its sarc |
| `romfs/Layout/MiniMap_...bntx.zs` | the added Peach Beach minimap |

This mod is RomFS-only (no code, no switches). It replaces the same `general_format` sarc as
ClassicGP: enabling both at once serves only one. Use the [Combined](../Combined/) mod for both.
