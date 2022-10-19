from python.testware.seleniumwrapper import SeleniumBaseTest


class BasePageObjectTest(SeleniumBaseTest):

    def test_verify_element_is_visible__should_pass_on_visible_element(self):
        self.fail("Write this test!")

    def test_verify_element_is_visible__should_fail_on_nonexistent_element(self):
        self.fail("Write this test!")

    def test_verify_element_is_visible__should_fail_on_valid_element_out_of_screen_bounds(self):
        self.fail("Write this test!")