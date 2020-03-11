# -*- coding: utf-8 -*-




import pytest
import allure
@allure.feature("类级别标签")
class TestAllure:
    @allure.title("用例1")
    @allure.description("我是备注执行测试用例1的结果是成功")
    @allure.story("方法级别标签1")
    def test_1(self):
        print("test_1")

    @allure.title("用例2")
    @allure.description("我是备注执行测试用例2的结果是成功")
    @allure.story("方法级别标签2")
    def test_2(self):
        print("test_2")

    @allure.title("用例3")
    @allure.description("我是备注执行测试用例3的结果是成功")
    @allure.story("方法级别标签3")
    def test_3(self):
        print("test_3")
    @pytest.mark.parametrize("case",["csae1","case2"])
    def test_4(self,case):
        print(case)
        allure.dynamic.title(case)