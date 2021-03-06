from .source import *
from .test import *
from .smscru import SmscruSource
from .nexmo import NexmoSource

by_config_name = {
    'webhook test source' : WebhookTestSource,
    'on demand test source' : OndemandTestSource,
    'nexmo' : NexmoSource,
    'smsc.ru' : SmscruSource
}

def spawn(source_list, persistence):
    all_sources = {}
    for source_type, sources in source_list.items():
        cls = by_config_name[source_type]
        for source_name, config_params in sources.items():
            params = {
                **config_params,
                'name' : source_name,
                'persistence' : persistence
            }
            source = cls(**params)
            all_sources[source_name] = source
    return all_sources

