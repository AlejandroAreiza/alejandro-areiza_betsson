from business.screens.swap_labs import SwapLabs
from tests.features.steps import assert_that, given, then, when


def _swap_labs(context) -> SwapLabs:
    return context.swap_labs_app

@given("the Swag Labs app is installed and launched")
def step_launch_swag_labs_app(context):
    context.swap_labs_app = SwapLabs(context.driver)

@given("I am on the login screen")
@then("I am on the login screen")
def step_verify_login_screen(context):
    is_login_visible = _swap_labs(context).login_screen.is_login_screen_visible()
    assert_that(is_login_visible).is_true()

@when('I login with username "{user_name}" and password "{user_password}"')
def step_login_with_credentials(context, user_name, user_password):
    _swap_labs(context).login_screen.login(user_name, user_password)

@then("the login button should be visible")
def step_verify_login_button_visible(context):
    is_button_visible = _swap_labs(context).login_screen.is_login_button_visible()
    assert_that(is_button_visible).is_true()
