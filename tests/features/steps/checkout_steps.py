from business.screens.swap_labs import SwapLabs
from tests.features.steps import assert_that, given, then, when, allure


def _swap_labs(context) -> SwapLabs:
    return context.swap_labs_app


@then('the cart badge should update to "{count}"')
@allure.step("Verify cart badge shows '{count}'")
def step_verify_cart_badge_count(context, count):
    actual_count = _swap_labs(context).products_screen.get_cart_badge_count()
    assert_that(actual_count).is_equal_to(count)


@when('I go to the "{screen_name}" screen')
@allure.step("Navigate to '{screen_name}' screen")
def step_navigate_to_screen(context, screen_name):
    _swap_labs(context).products_screen.go_to_cart()
    _swap_labs(context).cart_screen.tap_checkout()


@when(
    'I fill checkout information with "{first_name}", "{last_name}", and "{zip_code}"'
)
@allure.step(
    "Fill checkout form with first_name='{first_name}', last_name='{last_name}', zip_code='{zip_code}'"
)
def step_fill_checkout_information(context, first_name, last_name, zip_code):
    _swap_labs(context).checkout_screen.fill_checkout_information(
        first_name, last_name, zip_code
    )


@then('I should navigate to the "{screen_name}" screen')
@allure.step("Verify navigation to '{screen_name}' screen")
def step_verify_navigation_to_screen(context, screen_name):
    if screen_name == "Checkout: Overview":
        is_visible = _swap_labs(
            context
        ).checkout_overview_screen.is_checkout_overview_screen_visible()
        assert_that(is_visible).is_true()


@then("I should see the products in the order list")
@allure.step("Verify products are visible in order list")
def step_verify_order_list(context):
    is_visible = _swap_labs(context).checkout_overview_screen.is_order_list_visible()
    assert_that(is_visible).is_true()


@then("I should see the order summary with Item Total, Tax, and Total")
@allure.step("Verify order summary is visible")
def step_verify_order_summary(context):
    is_visible = _swap_labs(context).checkout_overview_screen.is_order_summary_visible()
    assert_that(is_visible).is_true()


@when('I tap the "{button_name}" button')
@allure.step("Tap '{button_name}' button")
def step_tap_button(context, button_name):
    if button_name == "Finish":
        _swap_labs(context).checkout_overview_screen.tap_finish()


@then("I should see an order confirmation popup")
@allure.step("Verify order confirmation popup is visible")
def step_verify_confirmation_popup(context):
    is_visible = _swap_labs(
        context
    ).checkout_overview_screen.is_confirmation_popup_visible()
    assert_that(is_visible).is_true()


@then('the popup should display "{expected_text}"')
@allure.step("Verify popup displays '{expected_text}'")
def step_verify_popup_text(context, expected_text):
    actual_text = _swap_labs(context).checkout_overview_screen.get_confirmation_text()
    assert_that(actual_text).is_equal_to(expected_text)


@when("I remove all products from checkout")
@allure.step("Remove all products from checkout")
def step_remove_all_products(context):
    _swap_labs(context).checkout_overview_screen.remove_all_products()


@then("I should see an incomplete order popup")
@allure.step("Verify order failed popup is visible")
def step_verify_failure_popup(context):
    is_visible = _swap_labs(context).checkout_overview_screen.is_incomplete_order_popup_visible()
    assert_that(is_visible).is_true()
