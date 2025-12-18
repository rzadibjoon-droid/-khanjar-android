[app]
title = KHANJAR
package.name = khanjar
package.domain = org.khanjar
source.dir = .
source.include_exts = py,kv,json,png,jpg
version = 1.0

requirements = python3==3.10.12,kivy==2.3.0,requests,numpy,plyer

orientation = portrait
fullscreen = 1

android.permissions = INTERNET,WAKE_LOCK,POST_NOTIFICATIONS
android.api = 33
android.minapi = 21
android.arch = armeabi-v7a, arm64-v8a

# ===== BUILDZOR PINNINGS =====
android.accept_sdk_license = True
android.build_tools_version = 33.0.2
android.ndk_version = 25b
android.allow_backup = True
android.logcat_filters = *:S python:D
