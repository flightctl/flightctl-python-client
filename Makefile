# Python package version. Override on generate:
#   make generate-client VERSION=1.3.0
VERSION ?= 1.2.1
GENERATOR_VERSION = 7.17.0
COMMON_PROPS = packageName=flightctl,useOneOfDiscriminatorLookup=true,packageVersion=$(VERSION),removeEnumValuePrefix=false
GIT_USER = flightctl
GIT_REPO = python-client
# Required: flightctl/flightctl release tag.
# Example: make fetch-specs FLIGHTCTL_VERSION=v1.3.0
FLIGHTCTL_REPO = https://raw.githubusercontent.com/flightctl/flightctl
FLIGHTCTL_VERSION ?=
SPEC_FILES = \
	api/core/v1beta1/openapi.yaml \
	api/core/v1alpha1/openapi.yaml \
	api/imagebuilder/v1alpha1/openapi.yaml

.PHONY: generate-client generate-core generate-v1alpha1 generate-imagebuilder bundle-specs fetch-specs fix-enum-number-prefix

# Fetch OpenAPI specs from a specific flightctl/flightctl version
fetch-specs:
	@if [ -z "$(FLIGHTCTL_VERSION)" ]; then \
		echo "FLIGHTCTL_VERSION is required (flightctl/flightctl release tag)."; \
		echo "Example: make fetch-specs FLIGHTCTL_VERSION=v1.3.0"; \
		exit 1; \
	fi
	@for f in $(SPEC_FILES); do \
		echo "Fetching $$f from flightctl/flightctl@$(FLIGHTCTL_VERSION)"; \
		mkdir -p $$(dirname $$f); \
		curl -fsSL "$(FLIGHTCTL_REPO)/$(FLIGHTCTL_VERSION)/$$f" -o $$f; \
	done
	@echo "Fetched specs from flightctl/flightctl@$(FLIGHTCTL_VERSION)"

# Rewrite Enum.NUMBER_PascalCase -> Enum.PascalCase in generated Python.
# Spec defaults stay intact so wire values match the Go server.
fix-enum-number-prefix:
	python3 scripts/fix-enum-number-prefix.py

# Bundle specs (resolve $refs into self-contained files)
bundle-specs:
	@mkdir -p api/bundled
	npx @redocly/cli bundle api/core/v1beta1/openapi.yaml -o api/bundled/core-v1beta1.yaml
	npx @redocly/cli bundle api/core/v1alpha1/openapi.yaml -o api/bundled/core-v1alpha1.yaml
	npx @redocly/cli bundle api/imagebuilder/v1alpha1/openapi.yaml -o api/bundled/imagebuilder-v1alpha1.yaml

# Core v1beta1
generate-core: bundle-specs
	npx @openapitools/openapi-generator-cli version-manager set $(GENERATOR_VERSION)
	npx @openapitools/openapi-generator-cli generate \
		-g python \
		-i api/bundled/core-v1beta1.yaml \
		-o . \
		--skip-validate-spec \
		--additional-properties=$(COMMON_PROPS) \
		--git-user-id $(GIT_USER) \
		--git-repo-id $(GIT_REPO)
	$(MAKE) fix-enum-number-prefix

# Core v1alpha1
generate-v1alpha1: bundle-specs
	npx @openapitools/openapi-generator-cli version-manager set $(GENERATOR_VERSION)
	npx @openapitools/openapi-generator-cli generate \
		-g python \
		-i api/bundled/core-v1alpha1.yaml \
		-o . \
		--skip-validate-spec \
		--additional-properties=packageName=flightctl.v1alpha1,useOneOfDiscriminatorLookup=true,generateSourceCodeOnly=true,packageVersion=$(VERSION),removeEnumValuePrefix=false \
		--git-user-id $(GIT_USER) \
		--git-repo-id $(GIT_REPO)
	$(MAKE) fix-enum-number-prefix

# ImageBuilder v1alpha1
generate-imagebuilder: bundle-specs
	npx @openapitools/openapi-generator-cli version-manager set $(GENERATOR_VERSION)
	npx @openapitools/openapi-generator-cli generate \
		-g python \
		-i api/bundled/imagebuilder-v1alpha1.yaml \
		-o . \
		--skip-validate-spec \
		--additional-properties=packageName=flightctl.imagebuilder,useOneOfDiscriminatorLookup=true,generateSourceCodeOnly=true,packageVersion=$(VERSION),removeEnumValuePrefix=false \
		--git-user-id $(GIT_USER) \
		--git-repo-id $(GIT_REPO)
	$(MAKE) fix-enum-number-prefix

generate-client:
	@echo "Generating Python client package Version=$(VERSION)"
	$(MAKE) VERSION=$(VERSION) generate-core generate-v1alpha1 generate-imagebuilder
