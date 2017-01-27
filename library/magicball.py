#!/usr/bin/python

from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

def main():
    module = AnsibleModule(
        argument_spec = dict(
            question = dict(required=True, type='str')
        )
    )

    question = module.params.get('question')
    url_endpoint = "https://8ball.delegator.com/magic/JSON/%s" % question
    request = open_url(url_endpoint, http_agent='ansible', validate_certs=False, )

    data = json.loads(request.read())
    answer = data['magic']['answer']

    module.exit_json(changed = False, answer = answer, question = question, msg = answer)

if __name__ == '__main__':
    main()

