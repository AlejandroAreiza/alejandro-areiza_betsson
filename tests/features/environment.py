from tests.features import (
    DataProvider,
    DesiredCapabilitiesDto,
    Logger,
    MobileDriverFactory,
    Path,
    subprocess,
)

logger = Logger.get_logger(__name__)
desired_capabilities_path = (
    Path(__file__).parent.parent.parent
    / "config"
    / "config_files"
    / "desired_capabilities.json"
)
app_folder = Path(__file__).parent.parent.parent / "business" / "app"


def before_all(context):
    logger.info("=" * 80)
    logger.info("STARTING TEST SUITE")
    try:
        subprocess.run(["nox", "-s", "start_appium"], check=True)
        logger.info("Appium server started")

        # Load capabilities to check headless setting
        capabilities = DataProvider.get_data(
            desired_capabilities_path, DesiredCapabilitiesDto
        )

        # Start emulator with headless flag based on capabilities
        emulator_cmd = ["nox", "-s", "start_emulator"]
        if hasattr(capabilities, 'headless') and capabilities.headless:
            emulator_cmd.extend(["--", "--headless"])

        subprocess.run(emulator_cmd, check=True)
        logger.info("Android emulator started")

        capabilities.app = str((app_folder / capabilities.app).absolute())
        context.driver = MobileDriverFactory.create_driver(capabilities)
    except Exception as e:
        logger.error(f"Setup failed: {e}")
        raise


def before_scenario(context, scenario):
    logger.info("_" * 80)
    logger.info(f"SCENARIO: {scenario.name}")
    context.driver.reset()


def after_scenario(context, scenario):
    if scenario.status == "failed":
        logger.error(f"✗ FAILED")
        failed_step = next((s for s in scenario.steps if s.status == "failed"), None)
        if failed_step and failed_step.exception:
            logger.error(f"Error: {failed_step.exception}")
    else:
        logger.info(f"✓ PASSED")
    logger.info("─" * 80)


def after_all(context):
    """Cleanup after all tests - ALWAYS runs."""

    # Quit driver
    if hasattr(context, "driver") and context.driver:
        try:
            context.driver.quit()
        except Exception as e:
            logger.error(f"✗ Failed to quit driver: {e}")

    # Stop emulator
    try:
        subprocess.run(["nox", "-s", "stop_emulator"], check=False)
        logger.info("Emulator stopped")
    except Exception as e:
        logger.error(f"✗ Failed to stop emulator: {e}")

    # Stop Appium
    try:
        subprocess.run(["nox", "-s", "stop_appium"], check=False)
        logger.info("Appium stopped")
    except Exception as e:
        logger.error(f"✗ Failed to stop Appium: {e}")

    logger.info("TEST SUITE COMPLETED")
    logger.info("=" * 80)
