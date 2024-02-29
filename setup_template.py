# clion setup

NONCFGTEMP = "MYMOD({}, {}, {}, {})" # guid, mod name, version, author
CFGTEMP = "MYMODCFG({}, {}, {}, {})" 

MAINCPPTTMP = """#include "mod/amlmod.h"
#include "mod/logger.h"
#include "mod/config.h"

:cfg:


extern "C" void OnModLoad()
{
    logger->SetTag("Mod Template");
    logger->Info("Mod loaded");
}
"""  # haha

modname = "mymod"
guid = "com.aml.mod"
author = 'aml'
version = "1.0.0"

ndkpath = "D:\\android-ndk"
def main():
    global version
    print("---------- AML Project in CLion setup ----------")
    print()
    print("     ----- Basic mod information -----")
    while True: #modname
        name = input("Mod name: ")
        if name:
            modname = name
            break
    while True: #input for guid
        guid_input = input("GUID: ")
        if guid_input:
            guid = guid_input
            break

    while True: #input for author
        author_input = input("Author: ")
        if author_input:
            author = author_input
            break

    version_input = input("Version (optional, defaults to 1.0.0): ")
    if version_input:
        version = version_input
  
    while True: #input for config
        cfg = input("Config(y/n): ")
        if cfg == "y":
            cfg_temp = CFGTEMP.format(guid, modname, version, author)
            break
        elif cfg == "n":
            cfg_temp = NONCFGTEMP.format(guid, modname, version, author)
            break

    main_cppt = MAINCPPTTMP.replace(":cfg:", cfg_temp)
    

    print("     ----- Builder information -----")
    while True: #input for ndk path
        ndk = input("NDK path: ")
        if ndk:
            ndkpath = ndk
            break
    
    print()
    print("     ----- Writing files -----")
    with open("main.cpp", "w") as f:
        f.write(main_cppt)
    with open("ndkpath.txt", 'w') as f:
        f.write(ndkpath)  
    
    print("""NOTES:
To be able to build the project, edit your run configuration to run "build.ps1" using powershell, you can delete the premade build configuration
""")
    input("\npress enter to exit...")

if __name__ == '__main__':
    main()