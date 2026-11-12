# mkw-recomp mods

Switch mods ported to [mkw-recomp](https://github.com/adriadam10/mkw-recomp): each folder is one mod,
imported from the start screen's Mods page (zip or folder). A folder holds the Switch layout
(`romfs/`, `exefs/`) plus a `mod.json` naming the ported code's patch switches; the importer writes
the overlay `manifest.tsv` itself.

| Mod | Game | Status |
|---|---|---|
| [Timer/](Timer/) | 1.8.0 | works (mod menu + in-game verified) |
| [ClassicGP/](ClassicGP/) | 1.8.0 | ported (mod menu verified; in-game check pending) |
| [SecretTracks/](SecretTracks/) | 1.8.0 | RomFS-only, no code; enabling both merges their shared archive |
