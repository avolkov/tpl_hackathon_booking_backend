import requests
import json


payload = {
    'id': '27131029111111',
    'firstName': 'John',
    'lastName': 'Doe',
    'resourceId': '1',
    'capabilities': ['GOOD_STANDING', '3D_PRINTER']
}

resp = requests.post(
    'http://localhost:8000/library_branch/booking',
    data=json.dumps(payload))

import ipdb; ipdb.set_trace()
