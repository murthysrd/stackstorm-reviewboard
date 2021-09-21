from rbtools.api.client import RBClient

#  from st2common.runners.base_action import Action
__all__ = [
    'BaseReviewBoardAction'
]


class Action(object):
    def __init__(self, config):
        self.config = config


class BaseReviewBoardAction(Action):
    def __init__(self, config):
        super(BaseReviewBoardAction, self).__init__(config=config)
        self._client = self._get_client()

    def _get_client(self):
        config = self.config

        options = {
            'server': config['url'],
            'verify_ssl': config['verify'],
            'allow_caching': config['allow_caching'],
            'in_memory_cache': config['in_memory_cache'],
            'save_cookies': config['save_cookies'],
        }

        auth_method = config['auth_method']

        if auth_method == 'token':
            options['api_token'] = config['api_token']
        elif auth_method == 'basic':
            options['username'] = config['username']
            options['password'] = config['password']
        else:
            msg = ('You must set auth_method to either "token"',
                   'or "basic" your reviewboard.yaml config file.')
            raise Exception(msg)

        client = RBClient(config['url'], **options)
        return client.get_root()
