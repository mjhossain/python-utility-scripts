# Developer: Mohammed J Hossain
# Date: 12/21/2022
# Description: Python Script to create a QR Code to WIFI login
# Packages: segno
# Usage: ssid - wifi name, password - wifi password, security - WEP|WPA|WPA2 (most home network)


from segno import helpers

qrcode = helpers.make_wifi(ssid='Your Wifi SSID',
                           password='Your Wifi Password', security='WPA2')
qrcode.designator
'3-M'
qrcode.save('wifi_qr.png', scale=10)
