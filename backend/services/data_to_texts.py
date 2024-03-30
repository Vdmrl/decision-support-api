from sqlalchemy import select

from db.engine import async_session_factory
from db.models.startup import Users  # account
from db.models.startup import Projects, ProjectData, FormFields  # project data
from db.models.startup import Passports, PassportData, PassportFields  # project passports


class UserData:
    def __init__(self):
        self.texts = []

    async def account_to_texts(self, user_id: int) -> None:
        """
        denormalizes account data into text
        :rtype: user id pk
        """
        async with async_session_factory() as session:
            query = select(Users).where(Users.id == user_id)
            result = await session.execute(query)
            user = result.scalar_one_or_none()
            if user:
                self.texts.append(user.country)
                self.texts.append(user.country)
                self.texts.append(user.region)
                self.texts.append(user.locality)
                self.texts.append(user.place_of_work_study)
                self.texts.append(user.name_of_company)
                self.texts.append(user.position)
                self.texts.append(user.education)
                self.texts.append(user.specialty)
                self.texts.append(user.university)
                self.texts.append(user.academic_degree)
                self.texts.append(user.academic_rank)
                self.texts.append(user.experience)
                self.texts.append(user.progress)
                self.texts.append(user.resume1)
                self.texts.append(user.resume2)
                self.texts.append(user.resume3)
                self.texts.append(user.year_of_graduation)
                self.texts.append(user.scientific_specialty)
                self.texts.append(user.work_experience)
                self.texts.append(user.tracking_experience)
                self.texts.append(user.business_experience)
                self.texts.append(user.teaching_experience)
                self.texts.append(user.expertise_experience)
                self.texts.append(user.main_publications)
                self.texts.append(user.languages)
                self.texts.append(user.programs)

    async def project_data_to_texts(self, project_id: int) -> None:
        """
        denormalizes project data into text
        :rtype: project id pk
        """
        pass

    async def project_passport_to_texts(self, project_id: int) -> None:
        """
        denormalizes project passport into text
        :rtype: project id pk
        """
        pass

    async def get_texts(self) -> str:
        """
        :return: list of texts
        """
        return "".join(self.texts)


class SupportData:
    def __init__(self):
        self.texts = []

    async def account_to_texts(self, support_id: int) -> None:
        """
        denormalizes support measures data into text
        :rtype: support id pk
        """
        pass

    async def project_data_to_texts(self, support_id: int) -> None:
        """
        denormalizes institutes data into text
        :rtype: support id pk
        """
        pass

    async def get_texts(self) -> str:
        """
        :return: list of texts
        """
        return "".join(self.texts)
