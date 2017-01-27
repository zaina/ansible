#!/usr/bin/python

from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

def main():
    module = AnsibleModule(
        argument_spec = dict(
            latitude = dict(required=True),
            longitude = dict(required=True),
            api_key = dict(required=True)
        )
    )

    latitude = module.params.get('latitude')
    longitude = module.params.get('longitude')
    api_key = module.params.get('api_key')
    url_endpoint = "https://api.darksky.net/forecast/%s/%s,%s" % (api_key, latitude, longitude)
    request = open_url(url_endpoint, http_agent='ansible', validate_certs=False)

    data = json.loads(request.read())
    module.exit_json(changed = False, ansible_facts=dict(daily_data=data['daily']))

if __name__ == '__main__':
    main()
