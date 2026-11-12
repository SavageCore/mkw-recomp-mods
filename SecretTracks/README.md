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

This mod is RomFS-only (no code, no switches) and ships byte-identical to the Switch original. It
replaces the same `general_format` sarc as ClassicGP: enabling both makes the Mods page merge the
two automatically (their 8 + 26 inner files are disjoint, verified), with a winner picker if they
ever disagree on one.

## Credits

Port of [14 Added Hidden Tracks](https://gamebanana.com/mods/736373) by liskadi, used under
[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) (non-commercial, no derivatives
beyond this port, credit kept). Ported verbatim: same sarc members, messages, minimap and size table.
