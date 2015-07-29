from regparser.default_settings import *

#### Regulation M

IGNORE_DEFINITIONS_IN_PART_1013 = [
    'state the amount',
    'may state that',
    'may state terms',
    'states that certain terms apply',
    'states certain terms',
    'states any of the following',
    'shall also state the following',
    'states the items listed',
    'subject to the Act and this part',
    'act'
]
IGNORE_DEFINITIONS_IN['1013'] = IGNORE_DEFINITIONS_IN_PART_1013

INCLUDE_DEFINITIONS_IN_PART_1013 = [
    ('Bureau', 'Bureau')
]

INCLUDE_DEFINITIONS_IN['1013'] = INCLUDE_DEFINITIONS_IN_PART_1013
