"""
Eagle Lenz - Pocket Option Bot for Railway (Async + Retry Logic)
"""

import asyncio
from BinaryOptionsToolsV2 import PocketOptionAsync

# Your SSID - GET A FRESH ONE!
SSID = '42["auth",{"session":"90dcda6b139fe52217664e80d6930ace","isDemo":1,"uid":88209425,"platform":2,"isFastHistory":true,"isOptimized":true}]'

async def get_candles_with_retry(client, asset, period, count, retries=3):
    """Retry candle fetch with delays between attempts"""
    for attempt in range(retries):
        try:
            candles = await client.get_candles(asset, period, count)
            if candles:
                return candles
        except Exception as e:
            print(f"   ⚠️ Attempt {attempt+1}/{retries} failed: {e}")
            if attempt < retries - 1:
                await asyncio.sleep(5)
    return None

async def main():
    print("=" * 50)
    print("🚀 Eagle Lenz - Pocket Option Bot")
    print("=" * 50)
    
    # Create async client
    print("\n[1] Creating client...")
    client = PocketOptionAsync(ssid=SSID)
    print("   ✅ Client created")
    
    # Connect
    print("\n[2] Connecting...")
    if not await client.connect():
        print("   ❌ Connection failed")
        return
    
    print("   ✅ Connected!")
    
    # CRITICAL: Wait for WebSocket to stabilize
    print("\n[3] Waiting for connection to stabilize...")
    await asyncio.sleep(5)  # 5 seconds - important!
    
    # Get balance
    print("\n[4] Getting balance...")
    balance = await client.get_balance()
    
    if balance == -1.0 or balance is None:
        print("   ❌ Invalid SSID or session expired")
        print("   Please get a fresh SSID from your browser")
        return
    
    print(f"   ✅ Balance: ${balance}")
    
    # Wait a bit more before candles
    await asyncio.sleep(2)
    
    # Get candles with retry
    print("\n[5] Fetching candles...")
    candles = await get_candles_with_retry(client, "EURUSD_otc", 60, 5)
    
    if candles:
        print(f"   ✅ Got {len(candles)} candles!")
        for c in candles:
            print(f"      Time: {c.get('time')}, Close: {c.get('close')}")
    else:
        print("   ❌ Failed to get candles after retries")
    
    # Keep the bot alive
    print("\n[6] Bot is running. Press Ctrl+C to stop.")
    try:
        while True:
            await asyncio.sleep(60)
            print("   💓 Heartbeat - Bot still alive")
    except KeyboardInterrupt:
        print("\n   Shutting down...")
    finally:
        await client.close()
        print("   ✅ Disconnected")

if __name__ == "__main__":
    asyncio.run(main())
