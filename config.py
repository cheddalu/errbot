import logging

#BACKEND = 'Text'
BACKEND = 'Slack'

BOT_DATA_DIR = r'/root/errbot-root/data'
BOT_EXTRA_PLUGIN_DIR = r'/root/errbot-root/plugins'

BOT_LOG_FILE = r'/root/errbot-root/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('@chedda', )

BOT_IDENTITY = {
    'token': '',
    }
