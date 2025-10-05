from business.screens.swap_labs import SwapLabs
from tests.features.steps import assert_that, then


def _swap_labs(context) -> SwapLabs:
    return context.swap_labs_app


@then('I should be navigated to the "{screen_name}" screen')
def step_verify_navigation_to_screen(context, screen_name):
    if screen_name == "Products":
        is_visible = _swap_labs(context).products_screen.is_products_screen_visible()
        assert_that(is_visible).is_true()


@then("I should see the products catalog")
def step_verify_products_catalog_visible(context):
    is_catalog_visible = _swap_labs(context).products_screen.is_products_catalog_visible()
    assert_that(is_catalog_visible).is_true()


@then('the screen title should display "{title_text}"')
def step_verify_screen_title(context, title_text):
    actual_title = _swap_labs(context).products_screen.get_screen_title()
    assert_that(actual_title).is_equal_to(title_text)


@then("the cart icon should be visible in the navigation bar")
def step_verify_cart_icon_visible(context):
    is_cart_visible = _swap_labs(context).products_screen.is_cart_icon_visible()
    assert_that(is_cart_visible).is_true()
