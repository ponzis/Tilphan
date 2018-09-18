class Test:

    def __init__(self, bot):
        print("This is a test.")

    async def on_yay(self):
        print('yay')

    def __unload(self):
        print('The plugin has been unloaded')


def setup(bot):
    bot.register_plugin(Test(bot))
    print("Test")


def teardown(bot):
    print('teardown')
