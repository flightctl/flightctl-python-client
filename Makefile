VERSION = 1.1.0
GENERATOR_VERSION = 7.17.0
COMMON_PROPS = packageName=flightctl,useOneOfDiscriminatorLookup=true,packageVersion=$(VERSION)
GIT_USER = flightctl
GIT_REPO = python-client

.PHONY: generate-client generate-core generate-v1alpha1 generate-imagebuilder bundle-specs

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
		--additional-properties=$(COMMON_PROPS) \
		--git-user-id $(GIT_USER) \
		--git-repo-id $(GIT_REPO)

# Core v1alpha1
generate-v1alpha1: bundle-specs
	npx @openapitools/openapi-generator-cli version-manager set $(GENERATOR_VERSION)
	npx @openapitools/openapi-generator-cli generate \
		-g python \
		-i api/bundled/core-v1alpha1.yaml \
		-o . \
		--additional-properties=packageName=flightctl.v1alpha1,useOneOfDiscriminatorLookup=true,generateSourceCodeOnly=true,packageVersion=$(VERSION) \
		--git-user-id $(GIT_USER) \
		--git-repo-id $(GIT_REPO)

# ImageBuilder v1alpha1
generate-imagebuilder: bundle-specs
	npx @openapitools/openapi-generator-cli version-manager set $(GENERATOR_VERSION)
	npx @openapitools/openapi-generator-cli generate \
		-g python \
		-i api/bundled/imagebuilder-v1alpha1.yaml \
		-o . \
		--additional-properties=packageName=flightctl.imagebuilder,useOneOfDiscriminatorLookup=true,generateSourceCodeOnly=true,packageVersion=$(VERSION) \
		--git-user-id $(GIT_USER) \
		--git-repo-id $(GIT_REPO)

generate-client: generate-core generate-v1alpha1 generate-imagebuilder