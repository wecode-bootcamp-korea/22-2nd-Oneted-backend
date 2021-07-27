from django.test    import TestCase, Client
from unittest.mock  import patch, MagicMock

from users.models   import User
from resumes.models import Resume

# ! : 하다 말음

class ResumeGetTest(TestCase):
    def setUp(self):
        user = User.objects.create(
            name="Homer Simpson",
            email="homer@google.com",
            kakao_api_id=1,
            profile_image="https://metro.co.uk/wp-content/uploads/2020/02/PRI_142406335-e1589297035275.jpg?quality=90&strip=all&zoom=1&resize=480%2C276"
        )
        Resume.objects.create(
            user=user,
            title="호머 심슨 이력서",
            is_done=True,
            is_file=False,
            file_uuid="1230897192837",
            content={
                "description" : "DDDDDDDDDDDDhough!",
                "career" : "원자력 발전소 3년차",
                "education"  : "도넛대학교 2학년 중퇴",
                "skill" : "마지 심슨 골려먹기",
            }
        )

    def tearDown(self):
        User.objects.all().delete()
        Resume.objects.all().delete()

    @patch("users.views.requests")
    def test_google_signin_new_user_success(self, mocked_requests):
        client = Client()
        print(mocked_requests)

        class MockedResponse:
            def json(self):
                return {
                    "id":123456789,
                    "kakao_account": { 
                    "profile_needs_agreement": False,
                    "profile": {
                        "nickname": "Homer Simpson",
                        "profile_image_url": "https://metro.co.uk/wp-content/uploads/2020/02/PRI_142406335-e1589297035275.jpg?quality=90&strip=all&zoom=1&resize=480%2C276",
                        "is_default_image":False
                    },
                    "email": "homer@google.com",
                    "email_needs_agreement":False, 
                    "is_email_valid": True,   
                    "is_email_verified": True,   
                    "age_range_needs_agreement":False,
                    "age_range":"20~29",
                    "birthday_needs_agreement":False,
                    "birthday":"1130"
                    }
                }
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        headers             = {"Authoriazation": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo3fQ.e7ograiiZoyWre5mmRTZ4A_eqBNK14NIRAV4MY--V5Q"}
        response            = client.get("/resumes/1", **headers)
        print(response)
        self.assertEqual(response.status_code, 200)