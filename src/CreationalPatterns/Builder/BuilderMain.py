from CreationalPatterns.Builder.PersonBuilder import PersonBuilder
def main():
    person_builder = PersonBuilder()
    person = person_builder\
        .personalInfo.his_name('Ayman').his_age(22).his_gender('Male')\
        .liveInfo.lives_at('Eithad St.').city('Damascus')\
        .workInfo.as_a('Computer Vision Enginner').works_at('MaxSoft').earnings(100000)\
        .build()
    print(person)
