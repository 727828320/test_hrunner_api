# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcases\demo_testcase_ref.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


from httprunner import HttpRunner, Config, Step, RunTestCase
from testcases.login_testcase import TestCaseLoginTestcaseRef as login
from testcases.department_test.basic.department_create_testcase import TestCaseDepartmentCreateTestcaseRef as dept_create
from testcases.department_test.basic.department_delete_testcase import TestCaseDepartmentCreateTestcaseRef as dept_delete
from testcases.department_test.basic.department_update_testcase import TestCaseUpdateTestcaseRef as dept_update
from testcases.department_test.basic.department_getlist_testcase import TestCaseGetlistTestcaseRef as dept_list


class TestCaseDepartmentTestcaseRef(HttpRunner):

    config = (
        Config("request methods testcase: reference testcase")
        .base_url("https://qyapi.weixin.qq.com")
        .verify(False)
        .export("access_token")
    )

    teststeps = [
        Step(
            RunTestCase("获取access_token")
                .call(login)
        ),
        Step(
            RunTestCase("创建部门")
                .call(dept_create)
        ),
        Step(
            RunTestCase("更新部门")
                .call(dept_update)
        ),
        Step(
            RunTestCase("获取部门")
                .call(dept_list)
        ),
        Step(
            RunTestCase("删除部门")
                .call(dept_delete)
        ),
    ]

if __name__ == "__main__":
    TestCaseDepartmentTestcaseRef().test_start()
