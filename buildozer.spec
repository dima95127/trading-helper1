[app]

title = Trading Helper
package.name = tradinghelper
package.domain = org.tradinghelper
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 1.0

# numpy, pandas, matplotlib — есть рецепты в python-for-android
# ta, yfinance, multitasking, ccxt — чистый Python, pip установит сам
requirements = python3,kivy,ccxt,requests,pandas,numpy,matplotlib,ta,yfinance,multitasking

orientation = portrait
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.accept_sdk_license = True
icon.filename = icon.png
fullscreen = False
log_level = 2

[buildozer]
