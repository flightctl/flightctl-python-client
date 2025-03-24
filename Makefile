generate-client:
	npx @openapitools/openapi-generator-cli version-manager set 7.11.0
	npx @openapitools/openapi-generator-cli generate \
	-g python \
	-i ./api/v1alpha1/openapi.yml \
	-o . \
	--additional-properties=packageName=flightctl \
	--git-user-id flightctl \
	--git-repo-id python-client
