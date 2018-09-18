"""
This file contains everything to run the bot from a module command.
"""
import logging

from tilphan import TilphanBot

logging.basicConfig(
    format='%(asctime)s - %(name)s [%(levelname)s]: %(message)s',
    level=logging.INFO)


def main():
    token = input('Enter the bots token: ')
    bot = TilphanBot()
    bot.run(token)


if __name__ == "__main__":
    main()
