from faker import Faker
from jobplus.models import db,User,Job,Resume
from random import randint


fake = Faker()


def iter_user():
    for i in range(200):
        yield User(
            username = str(randint(400,500))+fake.word(),
            email = fake.word()+'@'+fake.word()+'.com',
            password = '123456',
            role = 10,
            logo = fake.word()+fake.word(),
            companyname = str(randint(1,20))+fake.word()+fake.word(),
            website = fake.word()+fake.word()+'.com',
            address = fake.word()+fake.word(),
            intro = fake.word()+fake.word(),
            desc = fake.word()+fake.word(),
            is_disable = True

        )


def iter_company():
    for i in range(10):
        yield User(
            username = str(randint(300,350))+fake.word(),
            email = fake.word()+'@'+fake.word()+'.com',
            password = '123456',
            role = 20,
            logo = fake.word()+fake.word(),
            companyname = fake.word()+fake.word(),
            website = fake.word()+fake.word()+'.com',
            address = fake.word()+fake.word(),
            intro = fake.word()+fake.word(),
            desc = fake.word()+fake.word(),
            is_disable = True
            )



def iter_m_admin():
    yield User(
        username = '532604040@qq.com',
        email = '532604040@qq.com',
        password = '123456',
        role = 30,
        )

def iter_m_company():
    yield User(
        companyname = fake.word(),
        email = '532604040chris@qq.com',
        password = '123456',
        role = 20,
        )

def iter_m_user():
    yield User(
        username = fake.word(),
        email = '532604040@163.com',
        password = '123456',
        role = 10
        )
def iter_jobs():
    for i in range(50):
        yield Job(
            jobname = fake.word()+fake.word(),
            salary = fake.building_number(),
            exprequirement = fake.word(),
            edurequirement = fake.word(),
            address = fake.word(),
            desc = fake.word(),
            requirement = fake.word()
        )

def run():
    for job in iter_jobs():
        db.session.add(job)
    for company in iter_company():
        db.session.add(company)
    for user in iter_user():
        db.session.add(user)
    for one in iter_m_admin():
        db.session.add(one)
    for on in iter_m_user():
        db.session.add(on)
    for n in iter_m_company():
        db.session.add(n)
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        print('insert failed')
    for i in Job.query.all():
        a = randint(0,9)
        user = User.query.filter_by(role=20).all()[a]
        user.jobs.append(i)
        i.company_id = user.id
        db.session.add(user)
    for i in User.query.filter_by(role=10).all():
        jobs = Job.query.all()
        a = randint(0,49)
        job = jobs[a]
        resume =Resume()
        resume.job_id = job.id
        resume.user_id = i.id
        resume.company_id = job.users[0].id
        resume.status = 1
        db.session.add(resume)
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
