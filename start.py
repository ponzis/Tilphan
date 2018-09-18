"""
This is a simple script to start the bot from the outside.
"""
import logging
from logging import handlers

from tilphan import TilphanBot, config

LOGFILE = 'bot.log'

log_formater = logging.Formatter("%(asctime)s [%(name)s] [%(levelname)s]  %(message)s")

fileHandler = handlers.RotatingFileHandler(LOGFILE, maxBytes=(1048576 * 5), backupCount=7)
fileHandler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

logging.basicConfig(format="%(asctime)s [%(levelname)-5.5s] [%(name)s] %(message)s",
                    level=logging.DEBUG,
                    handlers=[console_handler, fileHandler])

logger = logging.getLogger(__name__)


def main():
    logger.info('Starting up the bot.')

    config_var = config.load_config('config.json')
    bot = TilphanBot()
    bot.run(config_var['token'])

    logger.info('Closed the bot.')


if __name__ == "__main__":
    main()

# TODO add some task mamagers
# TODO add a way to laod folders
# TODO fix logging
# TODO add command system
# TODO add some error handaling
