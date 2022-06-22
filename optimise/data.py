fsutil_cmds = (
    "fsutil behavior set memoryusage 2",
    "fsutil behavior set encryptpagingfile 0",
    "fsutil behavior set disable8dot3 1",
    "fsutil behavior set disablecompression 1",
    "fsutil behavior set disabledeletenotify 0"
)
# ("", "Reg_DWORD", "")
memReg = {
    # Disable UserAssist
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\settings" : (
        ("NoLog", "Reg_DWORD", "1"),
    ),
    # Disable Prefetch
    r"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters" : (
        ("EnablePrefetcher", "Reg_DWORD", "3"),
        ("EnableSuperfetch", "Reg_DWORD", "0"),
        ("EnableBoottrace", "Reg_DWORD", "0")
    ),
    # Disable Hibernation
    r"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Power" : (
        ("HiberbootEnabled", "Reg_DWORD", "0"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Control\Power" : (
        ("HibernateEnabled", "Reg_DWORD", "0"),
    ),
    # Wait to kill non-responding app before and after shutdown
    r"HKCU\Control Panel\Desktop" : (
        ("WaitToKillAppTimeout", "Reg_SZ", "5000"),
        ("HungAppTimeout", "Reg_SZ", "4000"),
        ("AutoEndTasks", "Reg_SZ", "1"),
        ("MenuShowDelay", "Reg_SZ", "0"),
        ("WaitToKillServiceTimeout", "Reg_SZ", "1000"),
        ("LowLevelHooksTimeout", "Reg_SZ", "1000"),
        ("ForegroundLockTimeout", "Reg_SZ", "150000")
    ),
    # Disk Optimizations
    r"HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" : (
        ("DontVerifyRandomDrivers", "Reg_DWORD", "1"),
        ("LongPathsEnabled", "Reg_DWORD", "0"),
        ("NtfsMftZoneReservation", "Reg_DWORD", "1"),
        ("NTFSDisable8dot3NameCreation", "Reg_DWORD", "1"),
        ("NTFSDisableLastAccessUpdate", "Reg_DWORD", "1"),
        ("ContigFileAllocSize", "Reg_DWORD", "40")
    ),
    # Disable background apps
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications" : (
        ("GlobalUserDisabled", "Reg_DWORD", "1"),
        ("LetAppsRunInBackground", "Reg_DWORD", "2")
    ),
    r"HKLM\Software\Policies\Microsoft\Windows\AppPrivacy" : (
        ("LetAppsRunInBackground", "Reg_DWORD", "2"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\Search" : (
        ("BackgroundAppGlobalToggle", "Reg_DWORD", "0"),
    ),
    # Disable Cortana
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" : (
        ("AllowCortana", "Reg_DWORD", "0"),
    ),
    # Expedite startup
    r"HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\Serialize" : (
        ("StartupDelayInMSec", "Reg_DWORD", "0"),
    ),
    # Disallow drivers to get paged into virtual memory / Disable Paging Combining / Use Large System Cache to improve microstuttering
    r"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" : (
        ("DisablePagingExecutive", "Reg_DWORD", "1"),
        ("DisablePagingCombining", "Reg_DWORD", "1"),
        ("LargeSystemCache", "Reg_DWORD", "1")
    ),
    # Unload .dll to free up memory
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer" : (
        ("AlwaysUnloadDLL", "Reg_DWORD", "1"),
        ("Max Cached Icons", "Reg_SZ", "2000")
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\AlwaysUnloadDLL" : (
        ("Default", "Reg_DWORD", "1"),
    ),
    # Free unused ram
    r"HKLM\System\CurrentControlSet\Control\Session Manager" : (
        ("HeapDeCommitFreeBlockThreshold", "Reg_DWORD", "262144"),
    ),
    # Disable Open Save Files
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32" : (
        ("NoFileMru", "Reg_DWORD", "1"),
    ),
    # Optimise explorer
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" : (
        ("NoRun", "Reg_DWORD", "0"),
        ("NoControlPanel", "Reg_DWORD", "0"),
        ("NoResolveTrack", "Reg_DWORD", "1"),
        ("NoFolderOptions", "Reg_DWORD", "0"),
        ("NoResolveSearch", "Reg_DWORD", "1"),
        ("NoViewContextMenu", "Reg_DWORD", "0"),
        ("NoInternetOpenWith", "Reg_DWORD", "1"),
        ("NoRecentDocsHistory", "Reg_DWORD", "1"),
        ("NoLowDiskSpaceChecks", "Reg_DWORD", "1"),
        ("LinkResolveIgnoreLinkInfo", "Reg_DWORD", "1")
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" : (
        ("EnableBalloonTips", "Reg_DWORD", "0"),
    ),
}

powerReg = {
    # Optimise power management
    r"HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\0cc5b647-c1df-4637-891a-dec35c318583" : (
        ("ValueMax", "Reg_DWORD", "100"),
        ("ValueMin", "Reg_DWORD", "0")
    ),
    r"HKLM\SYSTEM\ControlSet001\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\0cc5b647-c1df-4637-891a-dec35c318583" : (
        ("ValueMax", "Reg_DWORD", "100"),
        ("ValueMin", "Reg_DWORD", "0")
    ),
    r"HKLM\SYSTEM\ControlSet002\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\0cc5b647-c1df-4637-891a-dec35c318583" : (
        ("ValueMax", "Reg_DWORD", "100"),
        ("ValueMin", "Reg_DWORD", "0")
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Control\Power" : (
        ("HibernateEnabled", "Reg_DWORD", "0"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Power" : (
        ("HiberbootEnabled", "Reg_DWORD", "0"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerThrottling" : (
        ("PowerThrottlingOff", "Reg_DWORD", "1"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\893dee8e-2bef-41e0-89c6-b55d0929964c" : (
        ("ValueMax", "Reg_DWORD", "100"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\893dee8e-2bef-41e0-89c6-b55d0929964c\DefaultPowerSchemeValues\8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c" : (
        ("ValueMax", "Reg_DWORD", "100"),
    ),
}

debloatReg = {
    r"HKLM\SYSTEM\CurrentControlSet\Control\WMI\AutoLogger\AutoLogger-Diagtrack-Listener" : (
        ("Start", "REG_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\WindowsSelfHost\UI\Visibility" : (
        ("DiagnosticErrorText", "REG_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\WindowsSelfHost\UI\Strings" : (
        ("DiagnosticErrorText", "REG_SZ", ""),
        ("DiagnosticLinkText", "REG_SZ", "")
    ),
    r"HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Storage\microsoft.microsoftedge_8wekyb3d8bbwe\MicrosoftEdge\PhishingFilter" : (
        ("EnabledV9", "REG_DWORD", ""),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\TabletPC" : (
        ("PreventHandwritingDataSharing", "REG_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\HandwritingErrorReports" : (
        ("PreventHandwritingErrorReports", "REG_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\AppCompat" : (
        ("DisableInventory", "REG_DWORD", "1"),
        ("DisableUAR", "REG_DWORD", "1")
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\Personalization" : (
        ("NoLockScreenCamera", "REG_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo" : (
        ("Enabled", "REG_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo" : (
        ("Enabled", "REG_DWORD", "0"),
    ),
    r"HKCU\Software\Microsoft\Input\TIPC" : (
        ("Enabled", "REG_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\PolicyManager\current\device\System" : (
        ("AllowExperimentation", "REG_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\PolicyManager\current\device\Bluetooth" : (
        ("AllowAdvertising", "REG_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\SQMClient\Windows" : (
        ("CEIPEnable", "REG_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\Messaging" : (
        ("AllowMessageSync", "REG_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Biometrics" : (
        ("Enabled", "REG_DWORD", "0"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\PushNotifications" : (
        ("ToastEnabled", "REG_DWORD", "0"),
    ),
    r"HKCU\Control Panel\International\User Profile" : (
        ("HttpAcceptLanguageOptOut", "REG_DWORD", "1"),
    ),
}
