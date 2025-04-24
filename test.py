import flightctl
from flightctl.models.device import Device
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "https://api.10.0.7.163.nip.io:3443"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.DeviceApi(api_client)
    name = 'device-ansible-example' # str | The name of the Device resource to get.

    try:
        api_response = api_instance.get_device(name)
        print("The response of DeviceApi->get_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device: %s\n" % e)