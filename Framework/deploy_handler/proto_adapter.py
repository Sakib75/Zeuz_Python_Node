# Auhtor: sazid

import json
from pathlib import Path
from typing import Dict, List

# Uncomment the following lines for single-file debug
# import sys
# sys.path.append(str(Path.cwd() / "Framework" / "pb" / "v1"))
# from pb.v1.deploy_response_message_pb2 import DeployResponse

# Comment the following line for single-file debug
from Framework.pb.v1.deploy_response_message_pb2 import DeployResponse


def read_actions(actions_pb) -> List[Dict]:
    actions = []
    for action in actions_pb:
        rows = []
        actions.append({
            "action_name": action.name,
            "action_disabled": not action.enabled,
            "step_actions": rows,
        })

        for row in action.rows:
            rows.append([
                row.data[0],
                row.data[1],
                row.data[2],
            ])
    return actions


def read_steps(steps_pb) -> List[Dict]:
    steps = []
    for step in steps_pb:
        steps.append(
            {
                "step_id": step.step_id, # TODO: verify if it should be step.id or step.step_id
                "step_name": step.name,
                "step_sequence": step.sequence,
                "step_driver_type": step.step_info.driver,
                "automatablity": step.step_info.step_type,
                "always_run": step.step_info.always_run,
                "run_on_fail": step.step_info.run_on_fail,
                "step_function": "Sequential Actions",
                "step_driver": step.step_info.driver,
                "type": step.type,
                "step_attachments": list(step.step_info.attachments),
                "verify_point": step.step_info.verify_point,
                "continue_on_fail": step.step_info.step_continue,
                "step_time": step.time,
                "actions": read_actions(step.actions),
            }
        )
    return steps


def read_test_cases(test_cases_pb) -> List[Dict]:
    test_cases = []
    for tc in test_cases_pb:
        test_cases.append({
            "testcase_no": tc.test_case_detail.id,
            "title": tc.test_case_detail.name,
            "automatability": tc.test_case_detail.automatability,
            "debug_steps": [],
            "testcase_attachments_links": list(tc.attachments),
            "steps": read_steps(tc.steps),
        })
    return test_cases


def adapt(message: str, node_id: str) -> List[Dict]:
    """
    adapt takes the deploy_response and converts it to a python dictionary
    suitable for consumption by MainDriver.
    """

    r = DeployResponse()
    r.ParseFromString(message)

    # TODO: Check r.server_version and create different adapeter classes for new
    # schemaa changes.

    result = {
        "run_id": r.run_id,
        "server_version": r.server_version,
        "device_info": {
            "browser_stack": {},
        },
        "test_cases": read_test_cases(r.test_cases),
        "dependency_list": {
            "Browser": r.deploy_info.dependency.browser,
            "Mobile": r.deploy_info.dependency.mobile,
        },
        "debug": "yes" if r.deploy_info.debug.debug_mode else "no",
        "debug_clean": "YES" if r.deploy_info.debug.cleanup else "NO",
        "debug_step_actions": [],
        "debug_steps": [],
        "project_id": r.deploy_info.project_id,
        "team_id": r.deploy_info.team_id,
        "run_time": {},
        "objective": r.deploy_info.objective,
        "file_name": f"{node_id}_1"
    }

    if r.deploy_info.device_info:
        result["device_info"] = json.loads(r.deploy_info.device_info)

    # Add debug information
    for tc in r.deploy_info.debug.test_cases:
        actions = []
        for step in tc.steps:
            result["debug_steps"].append(step.sequence)
            actions += list(step.actions)

        result["debug_step_actions"] = actions
        # For now, node supports debugging only a single test case, which is why
        # we're breaking early. But this can be easily improved to handle
        # multiple test case debug.
        break


    # Read runtime parameters
    for rp in r.deploy_info.runtime_parameters:
        result["run_time"][rp.key] = {
            "field": rp.key,
            "subfield": rp.value,
        }

    return [result,]


if __name__ == "__main__":
    node_id = "admin_node1"
    with open("test.pb", "rb") as f:
        message = f.read()
        adapted_data = adapt(message, node_id)
        print(adapted_data)
