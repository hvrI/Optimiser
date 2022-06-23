fsutil_cmds = (
    ("fsutil behavior set memoryusage 2", "Raised the limit of paged pool memory."),
    ("fsutil behavior set encryptpagingfile 0", "Disabled Virtual Memory Pagefile Encryption."),
    ("fsutil behavior set disable8dot3 1", "Disabled the creation of legacy 8.3 character-length file names on FAT- and NTFS-formatted volumes."),
    ("fsutil behavior set disablecompression 1", "Disabled NTFS compression."),
    ("fsutil behavior set disabledeletenotify 0", "Enabled Trim.")
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
    # Disable Windows Search and others
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" : (
        ("ConnectedSearchUseWeb", "Reg_DWORD", "0"),
        ("AllowCloudSearch", "Reg_DWORD", "0"),
        ("AllowCortana", "Reg_DWORD", "0"),
        ("DisableWebSearch", "Reg_DWORD", "0"),
        ("AllowSearchToUseLocation", "Reg_DWORD", "0")
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
        ("EnabledV9", "REG_DWORD", "0"),
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
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\AppHost" : (
        ("EnableWebContentEvaluation", "REG_DWORD", "0"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{C1D23ACC-752B-43E5-8448-8D0E519CD6D6}" : (
        ("Value", "REG_SZ", "Deny"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" : (
        ("Start_TrackProgs", "REG_DWORD", "0"),
        ("ShowSyncProviderNotifications", "REG_DWORD", "0")
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{2297E4E2-5DBE-466D-A12B-0F8286F0D9CA}" : (
        ("Value", "REG_SZ", "Deny"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{E5323777-F976-4f5b-9B55-B94699C46E44}" : (
        ("Value", "REG_SZ", "Deny"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{2EEF81BE-33FA-4800-9670-1CD474972C3F}" : (
        ("Value", "REG_SZ", "Deny"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{52079E78-A92B-413F-B213-E8FE35712E72}" : (
        ("Value", "REG_SZ", "Deny"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{7D7E8402-7C54-4821-A34E-AEEFD62DED93}" : (
        ("Value", "REG_SZ", "Deny"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{D89823BA-7180-4B81-B50C-7E471E6121A3}" : (
        ("Value", "REG_SZ", "Deny"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{8BC668CF-7728-45BD-93F8-CF2B3B41D7AB}" : (
        ("Value", "REG_SZ", "Deny"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{9231CB4C-BF57-4AF3-8C55-FDA7BFCC04C5}" : (
        ("Value", "REG_SZ", "Deny"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{E390DF20-07DF-446D-B962-F5C953062741}" : (
        ("Value", "REG_SZ", "Deny"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{992AFA70-6F47-4148-B3E9-3003349C1548}" : (
        ("Value", "REG_SZ", "Deny"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications" : (
        ("GlobalUserDisabled", "REG_DWORD", "1"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Services\DiagTrack" : (
        ("Start", "REG_DWORD", "4"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Services\dmwappushservice" : (
        ("Start", "REG_DWORD", "4"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Control\WMI\Autologger\AutoLogger-Diagtrack-Listener" : (
        ("Start", "REG_DWORD", "0"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Services\FontCache" : (
        ("Start", "REG_DWORD", "4"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Services\FontCache3.0.0.0" : (
        ("Start", "REG_DWORD", "4"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Services\stisvc" : (
        ("Start", "REG_DWORD", "4"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\WMDRM" : (
        ("DisableOnline", "REG_DWORD", "1"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{A8804298-2D5F-42E3-9531-9C8C39EB29CE}e" : (
        ("Value", "REG_SZ", "Deny"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\LooselyCoupled" : (
        ("Value", "REG_SZ", "Deny"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\CredUI" : (
        ("DisablePasswordReveal", "REG_DWORD", "1"),
    ),
    r"HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Storage\microsoft.microsoftedge_8wekyb3d8bbwe\MicrosoftEdge\Main" : (
        ("DoNotTrack", "REG_DWORD", "1"),
        ("OptimizeWindowsSearchResultsForScreenReaders", "REG_DWORD", "0")
    ),
    r"HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Storage\microsoft.microsoftedge_8wekyb3d8bbwe\MicrosoftEdge\FlipAhead" : (
        ("FPEnabled", "REG_DWORD", "0"),
    ),
    r"HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Storage\microsoft.microsoftedge_8wekyb3d8bbwe\MicrosoftEdge\User\Default\SearchScopes" : (
        ("ShowSearchSuggestionsGlobal", "REG_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\PolicyManager\current\device\Browser" : (
        ("AllowAddressBarDropdown", "REG_DWORD", "0"),
    ),
    r"HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Storage\microsoft.microsoftedge_8wekyb3d8bbwe\MicrosoftEdge\Privacy" : (
        ("EnableEncryptedMediaExtensions", "REG_DWORD", "0"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\SettingSync" : (
        ("SyncPolicy", "REG_DWORD", "5"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Personalization" : (
        ("Enabled", "REG_DWORD", "0"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\SettingSync\Groups\BrowserSettings" : (
        ("Enabled", "REG_DWORD", "0"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Credentials" : (
        ("Enabled", "REG_DWORD", "0"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Language" : (
        ("Enabled", "REG_DWORD", "0"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Accessibility" : (
        ("Enabled", "REG_DWORD", "0"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Windows" : (
        ("Enabled", "REG_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Speech_OneCore\Preferences" : (
        ("ModelDownloadAllowed", "REG_DWORD", "0"),
    ),
    r"HKCU\Software\Microsoft\InputPersonalization\TrainedDataStore" : (
        ("HarvestContacts", "REG_DWORD", "0"),
    ),
    r"HKCU\Software\Microsoft\InputPersonalization" : (
        ("RestrictImplicitTextCollection", "REG_DWORD", "1"),
        ("RestrictImplicitInkCollection", "REG_DWORD", "1")
    ),
    r"HKCU\Software\Microsoft\Personalization\Settings" : (
        ("AcceptedPrivacyPolicy", "REG_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors" : (
        ("DisableWindowsLocationProvider", "REG_DWORD", "1"),
        ("DisableLocationScripting", "REG_DWORD", "1")
    ),
    r"HKCU\Software\Microsoft\Windows NT\CurrentVersion\Sensor\Permissions\{BFA794E4-F964-4FDB-90F6-51056BFE4B44}" : (
        ("SensorPermissionState", "REG_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" : (
        ("AllowTelemetry", "REG_DWORD", "0"),
        ("DoNotShowFeedbackNotifications", "REG_DWORD", "1")
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection" : (
        ("AllowTelemetry", "REG_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization" : (
        ("DODownloadMode", "REG_DWORD", "0"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\DeliveryOptimization" : (
        ("SystemSettingsDownloadMode", "REG_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Speech" : (
        ("AllowSpeechModelUpdate", "REG_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate" : (
        ("DeferUpgrade", "REG_DWORD", "1"),
        ("DeferUpgradePeriod", "REG_DWORD", "1"),
        ("DeferUpdatePeriod", "REG_DWORD", "0")
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Device Metadata" : (
        ("PreventDeviceMetadataFromNetwork", "REG_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsStore\WindowsUpdate" : (
        ("AutoDownload", "REG_DWORD", "2"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" : (
        ("NoAutoUpdate", "REG_DWORD", "1"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Services\wuauserv" : (
        ("Start", "REG_DWORD", "3"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Services\7971f918-a847-4430-9279-4a52d1efe18d" : (
        ("RegisteredWithAU", "REG_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\OneDrive" : (
        ("PreventNetworkTrafficPreUserSignIn", "REG_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet" : (
        ("SpyNetReporting", "REG_DWORD", "0"),
        ("SubmitSamplesConsent", "REG_DWORD", "2")
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\MRT" : (
        ("DontReportInfectionInformation", "REG_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" : (
        ("DisableAntiSpyware", "REG_DWORD", "1"),
    ),
    r"HKCU\Software\Microsoft\Siuf\Rules" : (
        ("NumberOfSIUFInPeriod", "REG_DWORD", "0"),
        ("PeriodInNanoSeconds", "REG_DWORD", "0")
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\Search" : (
        ("BingSearchEnabled", "REG_DWORD", "0"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" : (
        ("SilentInstalledAppsEnabled", "REG_DWORD", "0"),
        ("SoftLandingEnabled", "REG_DWORD", "0")
    ),
}

delBloatReg = (
    r"HKEY_CLASSES_ROOT\Extensions\ContractId\Windows.BackgroundTasks\PackageId\46928bounde.EclipseManager_2.2.4.51_neutral__a5h4egax66k6y",
    r"HKEY_CLASSES_ROOT\Extensions\ContractId\Windows.BackgroundTasks\PackageId\ActiproSoftwareLLC.562882FEEB491_2.6.18.18_neutral__24pqs290vpjk0",
    r"HKEY_CLASSES_ROOT\Extensions\ContractId\Windows.BackgroundTasks\PackageId\Microsoft.MicrosoftOfficeHub_17.7909.7600.0_x64__8wekyb3d8bbwe",
    r"HKEY_CLASSES_ROOT\Extensions\ContractId\Windows.BackgroundTasks\PackageId\Microsoft.PPIProjection_10.0.15063.0_neutral_neutral_cw5n1h2txyewy",
    r"HKEY_CLASSES_ROOT\Extensions\ContractId\Windows.BackgroundTasks\PackageId\Microsoft.XboxGameCallableUI_1000.15063.0.0_neutral_neutral_cw5n1h2txyewy",
    r"HKEY_CLASSES_ROOT\Extensions\ContractId\Windows.BackgroundTasks\PackageId\Microsoft.XboxGameCallableUI_1000.16299.15.0_neutral_neutral_cw5n1h2txyewy",
    r"HKEY_CLASSES_ROOT\Extensions\ContractId\Windows.File\PackageId\ActiproSoftwareLLC.562882FEEB491_2.6.18.18_neutral__24pqs290vpjk0",
    r"HKEY_CLASSES_ROOT\Extensions\ContractId\Windows.Launch\PackageId\46928bounde.EclipseManager_2.2.4.51_neutral__a5h4egax66k6y",
    r"HKEY_CLASSES_ROOT\Extensions\ContractId\Windows.Launch\PackageId\ActiproSoftwareLLC.562882FEEB491_2.6.18.18_neutral__24pqs290vpjk0",
    r"HKEY_CLASSES_ROOT\Extensions\ContractId\Windows.Launch\PackageId\Microsoft.PPIProjection_10.0.15063.0_neutral_neutral_cw5n1h2txyewy",
    r"HKEY_CLASSES_ROOT\Extensions\ContractId\Windows.Launch\PackageId\Microsoft.XboxGameCallableUI_1000.15063.0.0_neutral_neutral_cw5n1h2txyewy",
    r"HKEY_CLASSES_ROOT\Extensions\ContractId\Windows.Launch\PackageId\Microsoft.XboxGameCallableUI_1000.16299.15.0_neutral_neutral_cw5n1h2txyewy",
    r"HKEY_CLASSES_ROOT\Extensions\ContractId\Windows.PreInstalledConfigTask\PackageId\Microsoft.MicrosoftOfficeHub_17.7909.7600.0_x64__8wekyb3d8bbwe",
    r"HKEY_CLASSES_ROOT\Extensions\ContractId\Windows.Protocol\PackageId\ActiproSoftwareLLC.562882FEEB491_2.6.18.18_neutral__24pqs290vpjk0",
    r"HKEY_CLASSES_ROOT\Extensions\ContractId\Windows.Protocol\PackageId\Microsoft.PPIProjection_10.0.15063.0_neutral_neutral_cw5n1h2txyewy",
    r"HKEY_CLASSES_ROOT\Extensions\ContractId\Windows.Protocol\PackageId\Microsoft.XboxGameCallableUI_1000.15063.0.0_neutral_neutral_cw5n1h2txyewy",
    r"HKEY_CLASSES_ROOT\Extensions\ContractId\Windows.Protocol\PackageId\Microsoft.XboxGameCallableUI_1000.16299.15.0_neutral_neutral_cw5n1h2txyewy",
    r"HKEY_CLASSES_ROOT\HKCR:\Extensions\ContractId\Windows.ShareTarget\PackageId\ActiproSoftwareLLC.562882FEEB491_2.6.18.18_neutral__24pqs290vpjk0"
)

cachePaths = {
        "local": {
            "Spotify": [
                "\\Spotify\\Data",
                "\\Spotify\\Browser\\Cache\\Cache_Data",
                "\\Spotify\\Browser\\b28de9e6439b2e08c7a4321b3701d53bf18d0783\\Cache\\Cache_Data"
            ],
            "Packages Cache": [
                "\\Package Cache"
            ],
            "Temp": [
                "\\Temp"
            ],
            "D3DSCache": [
                "\\D3DSCache"
            ],
            "Chrome": [
                "\\Google\\Chrome\\User Data\\Default\\Cache\\Cache_Data"
            ],
            "Steam": [
                "\\Steam\\htmlcache\\Cache"
            ],
            "Valorant": [
                "\\VALORANT\\Saved\\webcache\\Cache",
            ]
        },
        "roaming": {
            "Discord": [
                "\\discord\\blob_storage",
                "\\discord\\Cache",
                "\\discord\\GPUCache"
            ],
            "Nvidia": [
                "\\NVIDIA\\ComputeCache"
            ],
            "Code": [
                "\\Code\\Cache\\Cache_Data"
            ],
            "Wps": [
                "\\kingsoft\\wps\\addons\\data\\win-i386\\cef\\cache\\KWPSBubble\\Cache",
                "\\kingsoft\\wps\\addons\\data\\win-i386\\cef\\globalcache\\KWPSBubble\\Cache"
            ]
        },
        "misc": {
            "Prefetch": [
                "C:\\Windows\\prefetch"
            ],
            "Temp": [
                "C:\\Windows\\Temp"
            ]
        }
    }

gameReg = {
    r"HKCU\SOFTWARE\Microsoft\Games" : (
        ("FpsAll", "Reg_DWORD", "1"),
        ("GameFluidity", "Reg_DWORD", "1"),
        ("FpsStatusGames", "Reg_DWORD", "16"),
        ("FpsStatusGamesAll", "Reg_DWORD", "4")
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" : (
        ("Affinity", "Reg_DWORD", "0"),
        ("Background Only", "Reg_SZ", "False"),
        ("Clock Rate", "Reg_DWORD", "10000"),
        ("GPU Priority", "Reg_DWORD", "8"),
        ("Priority", "Reg_DWORD", "6"),
        ("Scheduling Category", "Reg_SZ", "High"),
        ("SFIO Priority", "Reg_SZ", "High"),
        ("Latency Sensitive", "Reg_SZ", "True"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Low Latency" : (
        ("Affinity", "Reg_DWORD", "0"),
        ("Background Only", "Reg_SZ", "False"),
        ("Clock Rate", "Reg_DWORD", "10000"),
        ("GPU Priority", "Reg_DWORD", "8"),
        ("Priority", "Reg_DWORD", "2"),
        ("Scheduling Category", "Reg_SZ", "High"),
        ("SFIO Priority", "Reg_SZ", "High"),
        ("Latency Sensitive", "Reg_SZ", "True"),
    )
}