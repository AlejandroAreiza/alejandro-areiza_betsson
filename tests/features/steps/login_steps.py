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
    if user_name == "<empty>": user_name = ""
    if user_password == "<empty>": user_password = ""
    _swap_labs(context).login_screen.login(user_name, user_password)

@then("the login button should be visible")
def step_verify_login_button_visible(context):
    is_button_visible = _swap_labs(context).login_screen.is_login_button_visible()
    assert_that(is_button_visible).is_true()

@then("I should see an error message")
def step_verify_error_message_visible(context):
    is_error_visible = _swap_labs(context).login_screen.is_error_message_visible()
    assert_that(is_error_visible).is_true()

@then('the error message should contain "{error_text}"')
def step_verify_error_message_text(context, error_text):
    actual_error = _swap_labs(context).login_screen.get_error_message()
    assert_that(actual_error).contains(error_text)

@then("I should remain on the login screen")
def step_verify_remain_on_login_screen(context):
    is_login_visible = _swap_labs(context).login_screen.is_login_screen_visible()
    assert_that(is_login_visible).is_true()
