import Pyto

from rubicon.objc import *
UIPasteboard = ObjCClass("UIPasteboard")

# Code here

print("Your pasteboard is: ")
print(UIPasteboard.generalPasteboard.string)