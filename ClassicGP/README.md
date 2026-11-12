# ClassicGP (mkw-recomp mod)

The Switch `classicgp.zip` mod, ported to mkw-recomp for MKW 1.8.0: import the `ClassicGP/` folder
from the start screen's Mods page. Grand Prix shows the 4 standalone courses per cup, without the
Knockout Tour connecting lines (the Special Cup unlock part of the Switch mod is skipped: the port's
own `MKW_UNLOCK_ALL` hack already does that).

| Part | What it does |
|---|---|
| `romfs/` | The cup CourseId swaps (`general_format.Product_180.sarc.zs`) |
| `exefs/` | The original Switch IPS + pchtxt (build-id matched at import; Switch/emulator use only) |
| `mod.json` | The port: `switches` with `CLASSICGP`, five `sites` in one `classicgp` set |

The five sites (`recomp` checks every original word at generate time):

| Site | Change | Why it is equivalent |
|---|---|---|
| `main+0xbb1360` `ldr w8, [x0, #0x14]` to `mov w8, #1` + `main+0xbb136c` `stp w8, w9` to `stp wzr, w9` | the cup-name `cbz` never fires, and the stored pair is still `(0, w9)`, exactly the `nop` fall-through; `w8` is dead after (`mov w8, #0x40`) | two words stand in for the unpatchable branch |
| `main+0x7d201c` `sub w10, #7` to `#8` | Grand Prix (mode 7) fails the map-lines check, Knockout Tour (mode 8) keeps them | the mod verbatim |
| `main+0x85a6e4` `add w8, #1` to `mov w8, wzr` | the cup-road highlight frame stays 0.0 | the mod verbatim |
| `main+0x5572e0` `ldrb w0, [x0]` to `mov w0, #1` | `IsOpenFirst` returns true; the function returns right after | the mod verbatim |

Enabling the mod sets `MKW_CLASSICGP=1` for the next start.

## Credits

Port of [Classic Grand Prix (No Intermissions!)](https://gamebanana.com/mods/736220) by liskadi, used under
[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) (non-commercial, no derivatives
beyond this port, credit kept). Ported with one deliberate omission: the Special Cup unlock is skipped because the port already unlocks everything with its own UNLOCK_ALL hack. Everything else is verbatim.
