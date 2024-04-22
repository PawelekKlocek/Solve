import unittest
from solve import check_resource


class TestVerifyJson(unittest.TestCase):
    def test_resource_with_asterisk(self):
        json_data = {
            "PolicyName": "root",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": [
                            "iam:ListRoles",
                            "iam:ListUsers"
                        ],
                        "Resource": "*"
                    }
                ]
            }
        }
        self.assertFalse(check_resource(json_data))

    def test_empty_json(self):
        json_data = {}
        self.assertTrue(check_resource(json_data))

    def test_resource_without_asterisk(self):
        json_data = {
            "PolicyName": "root",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": [
                            "iam:ListRoles",
                            "iam:ListUsers"
                        ],
                        "Resource": "arn:aws:iam::123456789012:role/MyRole"
                    }
                ]
            }
        }
        self.assertTrue(check_resource(json_data))

    def test_no_resource_field(self):
        json_data = {
            "PolicyName": "root",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": [
                            "iam:ListRoles",
                            "iam:ListUsers"
                        ]
                    }
                ]
            }
        }
        self.assertTrue(check_resource(json_data))

    def test_no_statement_field(self):
        json_data = {
            "PolicyName": "root",
            "PolicyDocument": {
                "Version": "2012-10-17"
            }
        }
        self.assertTrue(check_resource(json_data))


if __name__ == '__main__':
    unittest.main()