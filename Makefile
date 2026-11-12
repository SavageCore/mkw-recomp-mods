# mkw-recomp mods: build install-ready zips into dist/ (gitignored).
# Same zips the release workflow publishes. Needs only zip and python3.
#
#   make            all mods
#   make Timer      one mod (Timer, ClassicGP or SecretTracks)
#   make validate   mod.json checks (same as CI)
#   make clean      remove dist/

MODS := $(sort $(patsubst ./%/mod.json,%,$(wildcard ./*/mod.json)))
ZIPS := $(addprefix dist/,$(addsuffix .zip,$(MODS)))

.PHONY: all clean validate $(MODS)

all: $(ZIPS)

$(MODS): %: dist/%.zip

dist/%.zip: %/mod.json
	mkdir -p dist
	rm -f $@
	cd $(CURDIR) && zip -qr $@ $* -x '*/manifest.tsv'
	@echo "wrote $@"

validate:
	python3 tools/validate.py

clean:
	rm -rf dist
