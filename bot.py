"""
Pocket Option Bot - With Connection Stabilization
"""

from BinaryOptionsToolsV2 import PocketOption
import time

SSID = '42["auth",{"session":"90dcda6b139fe52217664e80d6930ace","isDemo":1,"uid":88209425,"platform":2,"isFastHistory":true,"isOptimized":true}]'

print("=" * 50)
print("🚀 Pocket Option Bot (With Stabilization)")
print("=" * 50)

try:
    print("\n[1] Creating client...")
    client = PocketOption(ssid=SSID)
    print("   ✅ Client created")
    
    print("\n[2] Connecting...")
    client.connect()
    print("   ✅ Connected!")
    
    # CRITICAL: Wait for WebSocket to stabilize
    print("\n[3] Waiting for connection to stabilize...")
    for i in range(5):
        print(f"   Waiting... {5-i} seconds")
        time.sleep(1)
    
    print("\n[4] Getting balance...")
    balance = client.balance()
    print(f"   ✅ Balance: ${balance}")
    
    # Additional delay after balance
    time.sleep(2)
    
    print("\n[5] Getting candles (with retry)...")
    candles = None
    for attempt in range(3):
        try:
            print(f"   Attempt {attempt + 1}/3...")
            candles = client.get_candles("EURUSD_otc", 60, 5)
            if candles and len(candles) > 0:
                print(f"   ✅ Got {len(candles)} candles!")
                break
        except Exception as e:
            print(f"   ⚠️ Attempt {attempt + 1} failed: {e}")
            if attempt < 2:
                print(f"   Waiting 3 seconds before retry...")
                time.sleep(3)
    
    if candles:
        print(f"\n📊 Last candle: {candles[-1]}")
    else:
        print("\n   ❌ Failed to get candles after 3 attempts")
    
    print("\n[6] Keeping connection alive...")
    print("   Press Ctrl+C to stop")
    
    while True:
        time.sleep(30)
        print("   💓 Heartbeat - Bot alive")
        
except KeyboardInterrupt:
    print("\n   Stopping...")
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
finally:
    try:
        client.close()
        print("   ✅ Disconnected")
    except:
        pass
