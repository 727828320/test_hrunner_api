# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcases\demo_testcase_ref.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest ,RunTestCase
from testcases.login_testcase import TestCaseLoginTestcaseRef as login


class TestCaseDepartmentCreateTestcaseRef(HttpRunner):

    config = (
        Config("request methods testcase: reference testcase")
        .base_url("https://qyapi.weixin.qq.com")
        .verify(False)
    )

    teststeps = [
        Step(
            RunTestCase("获取access_token")
                .call(login)
        ),
        Step(
            RunRequest("删除部门")
            .get("/cgi-bin/department/delete")
            .with_params(**{"access_token": "$access_token", "id":"${department_data(id)}"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.errcode", 0)
            .assert_equal("body.errmsg", "deleted")
        ),
    ]

if __name__ == "__main__":
    TestCaseDepartmentCreateTestcaseRef().test_start()
