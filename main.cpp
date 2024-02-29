#include "mod/amlmod.h"
#include "mod/logger.h"
#include "mod/config.h"

MYMODCFG(net.rusjj.mymod.guid, AML Mod Template, 1.0, RusJJ)


extern "C" void OnModLoad()
{
    logger->SetTag("Mod Template");
    logger->Info("Mod loaded");
}
