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
