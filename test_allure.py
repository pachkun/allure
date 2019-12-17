import allure
import pytest


@allure.step
def passing_step():
    pass


@allure.step
def step_with_nested_steps():
    nested_step()


@allure.step
def nested_step():
    nested_step_with_arguments(1, 'abc')


@allure.step
def nested_step_with_arguments(arg1, arg2):
    pass


def test_with_imported_step():
    passing_step()


def test_with_nested_steps():
    passing_step()
    step_with_nested_steps()
    assert False

def test_sum():
    assert 1 + 1 == 3


def test_multiple_attachments():
    allure.attach.file('./data/image0.jpg', attachment_type=allure.attachment_type.PNG)
    allure.attach('<head></head><body> a page </body>', 'Attach with HTML type', allure.attachment_type.HTML)