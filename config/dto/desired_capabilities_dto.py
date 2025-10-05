from dataclasses import dataclass


@dataclass
class DesiredCapabilitiesDto:
    platformName: str
    automationName: str
    deviceName: str
    app: str
    appPackage: str
    appActivity: str
    noReset: bool
    fullReset: bool
    newCommandTimeout: int
    autoGrantPermissions: bool
    headless: bool = True
