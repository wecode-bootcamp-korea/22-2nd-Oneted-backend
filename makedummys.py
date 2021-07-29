from jobpostings.models import *
import random
# jobs
jg1 = JobGroup.objects.create(name="개발")
j1 = Job.objects.create(job_group=jg1, name="nodeJS 개발자")
j2 = Job.objects.create(job_group=jg1, name="프론트엔드 개발자")
j3 = Job.objects.create(job_group=jg1, name="python 개발자")
j4 = Job.objects.create(job_group=jg1, name="소프트웨어 개발자")
j5 = Job.objects.create(job_group=jg1, name="C, C++ 개발자")
j6 = Job.objects.create(job_group=jg1, name="서버 개발자")
j7 = Job.objects.create(job_group=jg1, name="웹 개발자")
j8 = Job.objects.create(job_group=jg1, name="자바 개발자")

# company
ct1 = Country.objects.create(name="한국")
rg1 = Region.objects.create(country=ct1, name="서울")
rg2 = Region.objects.create(country=ct1, name="대전")
rg4 = Region.objects.create(country=ct1, name="부산")
c1 = Company.objects.create(region=rg1, name="모두싸인", description="모두싸모두싸인에 접속해 준비된 계약서를 업로드 한 후 계약 상대방의 이메일 주소 또는전화번호를 입력해 서명을 요청하면, 상대방은 이메일이나 카카오톡으로 링크를전달받습니다. 이 링크를 클릭해 전자서명을 하거나 전자 도장을 입력하면 계약이종료됩니다.", employee_count=178, coordinate={"latitude":"37.490894843703074", "longitude":" 127.00574996913497"})
c2 = Company.objects.create(region=rg1, name="카카오 뱅크", description="모바퇴근제. http://www.visual.camp", employee_count=510, coordinate={"latitude":"37.490894843703074", "longitude":"127.00574996913497"})

# tags
tc1 = TagCategory.objects.create(name="인원수", is_multiple_choice=False)
tc2 = TagCategory.objects.create(name="편의시설", is_multiple_choice=True)
tc3 = TagCategory.objects.create(name="근무&휴가", is_multiple_choice=True)
t1 = Tag.objects.create(tag_category=tc1, name="50명이하")
t2 = Tag.objects.create(tag_category=tc1, name="51~100명")
t3 = Tag.objects.create(tag_category=tc1, name="101~200명")
t4 = Tag.objects.create(tag_category=tc1, name="201~300명")
t5 = Tag.objects.create(tag_category=tc2, name="사내카페")
t6 = Tag.objects.create(tag_category=tc2, name="사내식당")
t7 = Tag.objects.create(tag_category=tc2, name="주차")
t8 = Tag.objects.create(tag_category=tc2, name="수면실")
t9 = Tag.objects.create(tag_category=tc2, name="휴게실")
t10 = Tag.objects.create(tag_category=tc2, name="위워크")
t11 = Tag.objects.create(tag_category=tc3, name="야근없음")
t12 = Tag.objects.create(tag_category=tc3, name="주35시간")
t13 = Tag.objects.create(tag_category=tc3, name="유연근무")
t14 = Tag.objects.create(tag_category=tc3, name="출산휴가")

# experience
exp1 = Experience.objects.create(name="신입")
exp2 = Experience.objects.create(name="1년차")
exp3 = Experience.objects.create(name="2년차")
exp4 = Experience.objects.create(name="3년차")
exp5 = Experience.objects.create(name="4년차")
exp6 = Experience.objects.create(name="5년차")
exp7 = Experience.objects.create(name="6년차")
exp8 = Experience.objects.create(name="7년차")
exp9 = Experience.objects.create(name="8년차")
exp10 = Experience.objects.create(name="9년차 이상")

# jobpostings


jp1 = JobPosting.objects.create(job=j1, experience=exp1, company=c1, title="백엔드 엔지니어 (주니어)", salary=50000000, main_task="- 모두싸인 백엔드 애플리케이션 설계 및 구현 \n- 더 나은 고객 경험을 제공하기 위한 서비스 개선 및 최적화 활동\n- 인하우스/백오피스  서비스 개발",requirement="\n- 한 가지 이상의 언어를 능숙하게 다루실 수 있는 분\n- RESTful API 개발 경험\n- SQL or NO-SQL 데이터베이스 경험\n- 다른 직무의 팀원과 적극적으로 대화할 수 있는 의사소통 태도와 능력\n- 장애 발생시 빠른 확인이 가능 한 트러블 슈팅 스킬\n- 새로운 것을 빠르게 배우고 호기심이 많으신 분\n- 해외여행 결격사유가 없는 분\n- 병역필 또는 면제자")
jp2 = JobPosting.objects.create(job=j2, experience=exp1, company=c1, title="프론트엔드 엔지니어 (주니어)", salary=50000000, main_task="- 모두싸인 백엔드 애플리케이션 설계 및 구현 \n- 더 나은 고객 경험을 제공하기 위한 서비스 개선 및 최적화 활동\n- 인하우스/백오피스  서비스 개발",requirement="\n- 한 가지 이상의 언어를 능숙하게 다루실 수 있는 분\n- RESTful API 개발 경험\n- SQL or NO-SQL 데이터베이스 경험\n- 다른 직무의 팀원과 적극적으로 대화할 수 있는 의사소통 태도와 능력\n- 장애 발생시 빠른 확인이 가능 한 트러블 슈팅 스킬\n- 새로운 것을 빠르게 배우고 호기심이 많으신 분\n- 해외여행 결격사유가 없는 분\n- 병역필 또는 면제자")
jp3 = JobPosting.objects.create(job=j3, experience=exp3, company=c1, title="파이썬 개발자", salary=80000000, main_task="- 모두싸인 백엔드 애플리케이션 설계 및 구현 \n- 더 나은 고객 경험을 제공하기 위한 서비스 개선 및 최적화 활동\n- 인하우스/백오피스  서비스 개발",requirement="\n- 한 가지 이상의 언어를 능숙하게 다루실 수 있는 분\n- RESTful API 개발 경험\n- SQL or NO-SQL 데이터베이스 경험\n- 다른 직무의 팀원과 적극적으로 대화할 수 있는 의사소통 태도와 능력\n- 장애 발생시 빠른 확인이 가능 한 트러블 슈팅 스킬\n- 새로운 것을 빠르게 배우고 호기심이 많으신 분\n- 해외여행 결격사유가 없는 분\n- 병역필 또는 면제자")
jp4 = JobPosting.objects.create(job=j4, experience=exp3, company=c1, title="소프트웨어 개발자", salary=100000000, main_task="- 모두싸인 백엔드 애플리케이션 설계 및 구현 \n- 더 나은 고객 경험을 제공하기 위한 서비스 개선 및 최적화 활동\n- 인하우스/백오피스  서비스 개발",requirement="\n- 한 가지 이상의 언어를 능숙하게 다루실 수 있는 분\n- RESTful API 개발 경험\n- SQL or NO-SQL 데이터베이스 경험\n- 다른 직무의 팀원과 적극적으로 대화할 수 있는 의사소통 태도와 능력\n- 장애 발생시 빠른 확인이 가능 한 트러블 슈팅 스킬\n- 새로운 것을 빠르게 배우고 호기심이 많으신 분\n- 해외여행 결격사유가 없는 분\n- 병역필 또는 면제자")
jp5 = JobPosting.objects.create(job=j1, experience=exp5, company=c2, title="백엔드 엔지니어 개발자", salary=120000000, main_task="• Flink/StreamSets 기반의 실시간 스트리밍 파이프라인 개발\n• 모던 데이터 아키텍처 기반의 이벤트/데이터 모델링\n• 데이터 전처리 및 검증 프로세스 개발")
jp6 = JobPosting.objects.create(job=j2, experience=exp5, company=c2, title="백엔드 엔지니어 개발자", salary=120000000, main_task="• Flink/StreamSets 기반의 실시간 스트리밍 파이프라인 개발\n• 모던 데이터 아키텍처 기반의 이벤트/데이터 모델링\n• 데이터 전처리 및 검증 프로세스 개발")
jp7 = JobPosting.objects.create(job=j3, experience=exp10, company=c2, title="백엔드 장인", salary=150000000, main_task="• Flink/StreamSets 기반의 실시간 스트리밍 파이프라인 개발\n• 모던 데이터 아키텍처 기반의 이벤트/데이터 모델링\n• 데이터 전처리 및 검증 프로세스 개발")
jp8 = JobPosting.objects.create(job=j4, experience=exp10, company=c2, title="프론트엔드 장인", salary=150000000, main_task="• Flink/StreamSets 기반의 실시간 스트리밍 파이프라인 개발\n• 모던 데이터 아키텍처 기반의 이벤트/데이터 모델링\n• 데이터 전처리 및 검증 프로세스 개발")

# jobpostings & tags
jp1.tags.add(t1,t5,t6,t7,t11,t12)
jp2.tags.add(t1,t5,t6,t7,t11,t12)
jp3.tags.add(t1,t5,t6,t7,t11,t12)
jp4.tags.add(t1,t5,t6,t7,t11,t12)
jp5.tags.add(t2,t8,t9,t10,t13,t14)
jp6.tags.add(t2,t8,t9,t10,t13,t14)
jp7.tags.add(t2,t8,t9,t10,t13,t14)
jp8.tags.add(t2,t8,t9,t10,t13,t14)

from users.models import *
# users
u1 = User.objects.create(name="Homer Simpson", email="homer@google.com", profile_image="https://metro.co.uk/wp-content/uploads/2020/02/PRI_142406335-e1589297035275.jpg?quality=90&strip=all&zoom=1&resize=480%2C276", kakao_api_id=1)
u2 = User.objects.create(name="Bart Simpson", email="bart@google.com", profile_image="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/f15f5662080793.5a8432e3d5b6b.jpg", kakao_api_id=2)
u3 = User.objects.create(name="Lisa Simpson", email="lisa@google.com", profile_image="https://upload.wikimedia.org/wikipedia/en/e/ec/Lisa_Simpson.png", kakao_api_id=3)
u4 = User.objects.create(name="Marge Simpson", email="marge@google.com", profile_image="https://media.npr.org/assets/img/2013/05/07/ap0908140151727_vert-06dfa531201681c1ebe2d126471494fdeb5048ae-s800-c85.jpg", kakao_api_id=4)
u5 = User.objects.create(name="Maggie Simpson", email="maggie@google.com", profile_image="https://ichef.bbci.co.uk/news/640/cpsprodpb/02F9/production/_104516700_3_spongebob_squarepants__hr.jpg", kakao_api_id=5)

# resumes
from resumes.models import *

r1 = Resume.objects.create(user=u1, title="호머 심슨 이력서", is_done=True,is_file=False, content={
    "description" : "DDDDDDDDDDDDhough!",
    "career" : "원자력 발전소 3년차",
    "education"  : "도넛대학교 2학년 중퇴",
    "skill" : "마지 심슨 골려먹기",
})
r2 = Resume.objects.create(user=u2, title="바트 심슨 이력서", is_done=True,is_file=False, content={
    "description" : "lalalaaa!",
    "career" : "중학교 1년차",
    "education"  : "도넛중학교 2학년 중퇴",
    "skill" : "매기 심슨 돌보다 말기",
})
r3 = Resume.objects.create(user=u3, title="리사 심슨 이력서", is_done=True,is_file=False, content={
    "description" : "hi!",
    "career" : "범생이 3년차",
    "education"  : "도넛대학교 2학년 ",
    "skill" : "토익 900점",
})
r4 = Resume.objects.create(user=u4, title="마지 심슨 이력서", is_done=True,is_file=False, content={
    "description" : "don't do that!",
    "career" : "주부 10년차",
    "education"  : "도넛대학교 졸업",
    "skill" : "머리 볶기",
})
r5 = Resume.objects.create(user=u5, title="매기 심슨 이력서", is_done=True,is_file=False, content={
    "description" : "응애!",
    "career" : "아기 3년차",
    "education"  : "",
    "skill" : "",
})

Resume.objects.create(user_id=7, title="성준's 첫번째 이력서", is_done=True,is_file=False, content={
    "description" : "응애!",
    "career" : "아기 3년차",
    "education"  : "",
    "skill" : "",
})
Resume.objects.create(user_id=7, title="성준's 두번째 이력서", is_done=True,is_file=False, content={
    "description" : "응애!",
    "career" : "아기 3년차",
    "education"  : "",
    "skill" : "",
})
Resume.objects.create(user_id=7, title="성준's 세번째 이력서", is_done=True,is_file=False, content={
    "description" : "응애!",
    "career" : "아기 3년차",
    "education"  : "",
    "skill" : "",
})
Resume.objects.create(user_id=7, title="성준's 네번째 이력서", is_done=True,is_file=False, content={
    "description" : "응애!",
    "career" : "아기 3년차",
    "education"  : "",
    "skill" : "",
})
Resume.objects.create(user_id=7, title="성준's 다섯번째 이력서", is_done=True,is_file=False, content={
    "description" : "응애!",
    "career" : "아기 3년차",
    "education"  : "",
    "skill" : "",
})

# jobpostings 가져오기
jp1 = JobPosting.objects.get(id=1)
jp2 = JobPosting.objects.get(id=2)
jp3 = JobPosting.objects.get(id=3)
jp4 = JobPosting.objects.get(id=4)
jp5 = JobPosting.objects.get(id=5)
jp6 = JobPosting.objects.get(id=6)
jp7 = JobPosting.objects.get(id=7)
jp8 = JobPosting.objects.get(id=8)

# apply
u1 = User.objects.get(id=1)
r = Resume.objects.filter(user=u1)
Apply.objects.create(user=u1,job_posting=jp1).resume.add(1,6,7,8,9)

# random datas
for i in range(100):
    ran_exp = random.randint(1,10)
    ran_job = random.randint(2,8)
    ran_salary = random.randint(3000,10000)
    JobPosting.objects.create(
        job_id=ran_job, 
        experience_id=ran_exp, 
        company_id=1, 
        title="백엔드 엔지니어 (주니어)", 
        salary=ran_salary * 1000, 
        main_task="- 모두싸인 백엔드 애플리케이션 설계 및 구현 \n- 더 나은 고객 경험을 제공하기 위한 서비스 개선 및 최적화 활동\n- 인하우스/백오피스  서비스 개발",
        requirement="\n- 한 가지 이상의 언어를 능숙하게 다루실 수 있는 분\n- RESTful API 개발 경험\n- SQL or NO-SQL 데이터베이스 경험\n- 다른 직무의 팀원과 적극적으로 대화할 수 있는 의사소통 태도와 능력\n- 장애 발생시 빠른 확인이 가능 한 트러블 슈팅 스킬\n- 새로운 것을 빠르게 배우고 호기심이 많으신 분\n- 해외여행 결격사유가 없는 분\n- 병역필 또는 면제자"
    )
