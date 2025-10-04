from business.screens.swap_labs import SwapLabs
from tests.features.steps import assert_that, given, then, when


def _swap_labs(context) -> SwapLabs:
    return context.swap_labs_app


@given("the SwapLabsApp")
def step_launch_app(context):
    context.swap_labs_app = SwapLabs(context.driver)


@when("I get the current activity")
def step_get_current_activity(context):
    context.app_title = _swap_labs(context).get_current_activity()

@then('the activity name should be "{activity_name}"')
def step_then_activity_name(context, activity_name):
    assert_that(context.app_title).is_not_none().is_equal_to(activity_name)
