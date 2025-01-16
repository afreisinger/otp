# https://pyauth.github.io/pyotp/#working-example

import pyotp
totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
print("Current OTP:", totp.now())