import asyncio
from BinaryOptionsToolsV2 import PocketOption

SSID = '42["auth",{"session":"90dcda6b139fe52217664e80d6930ace","isDemo":1,"uid":88209425,"platform":2,"isFastHistory":true,"isOptimized":true}]'

async def run_bot():
    print("🚀 Railway Bot Starting...")
    client = PocketOption(ssid=SSID)
    await client.connect()
    # Add your main trading or scanning loop here
    await asyncio.sleep(30) # Placeholder to keep the bot alive
    await client.close()

if __name__ == "__main__":
    asyncio.run(run_bot())
