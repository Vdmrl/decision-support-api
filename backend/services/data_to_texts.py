from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload

from db.engine import async_session_factory
from db.models.startup import Users, UserProject  # account
from db.models.startup import Projects, ProjectData, Forms, FormFields, Passports  # project data
from db.models.startup import Passports, PassportData, PassportFields  # project passports

from db.models.startup import (Supports, SupportSupportForms, SupportForms, SupportSupportMembers, SupportMembers,
                               SupportSupportReasons, SupportReasons, SupportSupportDirections, SupportDirections,
                               SupportRegions, Regions)
from db.models.startup import (Institutes, InstitutionInstitutionForms, InstitutionForms, InstitutionRegions, Regions)

import logging


class UserData:
    def __init__(self):
        self.texts = []

    async def accounts_to_texts(self, id_project: int) -> None:
        """
        denormalizes account data into text
        :rtype: user id pk
        """
        async with (async_session_factory() as session):
            query = (select(Projects)
                     .options(  # forms
                selectinload(Projects.user_project)  # one-to-many
                .joinedload(UserProject.users))  # many-to-one
                     .where(Projects.id_projects == id_project)
                     )
            result = await session.execute(query)
            project = result.scalar_one_or_none()
            if project:
                user_projects = project.user_project
                if user_projects:
                    for user_project in user_projects:
                        self.texts.append(user_project.role_description)
                        user = user_project.users
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
                        else:
                            logging.warning("no user in data_to_text")
                else:
                    logging.warning("no user_project in data_to_text")
            else:
                logging.warning("no project in data_to_text")

    async def project_data_to_texts(self, id_project: int) -> None:
        """
        denormalizes project data into text
        :rtype: project id pk
        """
        # TODO
        pass

    async def project_passport_to_texts(self, id_project: int) -> None:
        """
        denormalizes project passport into text
        :rtype: project id pk
        """
        # TODO
        pass

    async def event_to_texts(self, id_project: int) -> None:
        """
        denormalizes event into text
        :rtype: project id pk
        """
        async with async_session_factory() as session:
            query = (
                select(Projects)
                .options(
                    joinedload(Projects.forms).options(
                        selectinload(Forms.passports)
                    ))  # many-to-one
                .where(Projects.id_projects == id_project)
            )
            result = await session.execute(query)
            project = result.scalar_one_or_none()
            if project:
                event = project.forms
                if event:
                    # event
                    self.texts.append(event.description)
                    self.texts.append(event.members)
                    self.texts.append(event.event_format)
                    # passports
                    passports = event.passports
                    for passport in passports:
                        self.texts.append(passport.description)
                else:
                    logging.warning("no event in data_to_text")
            else:
                logging.warning("no project in data_to_text")

    async def get_texts(self) -> str:
        """
        :return: list of texts
        """
        return "".join(self.texts)


class SupportData:
    def __init__(self):
        self.texts = []

    async def support_to_texts(self, id_support: int) -> None:
        """
        denormalizes support measures data into text
        :rtype: support id pk
        """
        async with async_session_factory() as session:
            query = (
                select(Supports)
                .options(
                    # forms
                    selectinload(Supports.support_support_forms)  # one-to-many
                    .joinedload(SupportSupportForms.support_forms),  # many-to-one
                    # directions
                    selectinload(Supports.support_support_directions)  # one-to-many
                    .joinedload(SupportSupportDirections.support_directions),  # many-to-one
                    # reasons
                    selectinload(Supports.support_support_reasons)  # one-to-many
                    .joinedload(SupportSupportReasons.support_reasons),  # many-to-one
                    # members
                    selectinload(Supports.support_support_members)  # one-to-many
                    .joinedload(SupportSupportMembers.support_members),  # many-to-one
                    # regions
                    selectinload(Supports.support_regions)  # one-to-many
                    .joinedload(SupportRegions.regions),  # many-to-one
                )
                .where(Supports.id_supports == id_support)
            )
            result = await session.execute(query)
            support = result.scalar_one_or_none()
            if support:
                self.texts.append(support.description)
                # support forms
                support_support_forms = support.support_support_forms
                if support_support_forms:
                    for support_support_form in support_support_forms:
                        support_form = support_support_form.support_forms
                        if support_form:
                            self.texts.append(support_form.support_form_name)

                # support directions
                support_support_directions = support.support_support_directions
                if support_support_directions:
                    for support_support_direction in support_support_directions:
                        support_direction = support_support_direction.support_directions
                        if support_direction:
                            self.texts.append(support_direction.support_direction_name)

                # support reasons
                support_support_reasons = support.support_support_reasons
                if support_support_reasons:
                    for support_support_reason in support_support_reasons:
                        support_reason = support_support_reason.support_reasons
                        if support_reason:
                            self.texts.append(support_reason.support_reason_name)

                # support members
                support_support_members = support.support_support_members
                if support_support_members:
                    for support_support_member in support_support_members:
                        support_member = support_support_member.support_members
                        if support_member:
                            self.texts.append(support_member.support_members_name)

                # support regions
                support_regions = support.support_regions
                if support_regions:
                    for support_region in support_regions:
                        region = support_region.regions
                        if region:
                            self.texts.append(region.region_name)
                            self.texts.append(region.region_code)

            else:
                logging.warning("no support in data_to_text")

    async def institute_to_texts(self, id_support: int) -> None:
        """
        denormalizes institutes data into text
        :rtype: support id pk
        """
        async with async_session_factory() as session:
            query = (
                select(Supports)
                .options(
                    joinedload(Supports.institutes).options(  # many-to-one
                        selectinload(Institutes.institution_institution_forms)  # one-to-many
                        .joinedload(InstitutionInstitutionForms.institution_forms),  # many-to-one
                        selectinload(Institutes.institution_regions)  # one-to-many
                        .joinedload(InstitutionRegions.regions)  # many-to-one
                    )
                )
                .where(Supports.id_supports == id_support)
            )
            result = await session.execute(query)
            support = result.scalar_one_or_none()
            if support:
                # institute
                institute = support.institutes
                if institute:
                    self.texts.append(institute.description)
                    # institute forms
                    institution_institution_forms = institute.institution_institution_forms
                    if institution_institution_forms:
                        for institution_institution_form in institution_institution_forms:
                            institution_form = institution_institution_form.institution_forms
                            if institution_form:
                                self.texts.append(institution_form.institution_form_name)
                    # regions
                    institution_regions = institute.institution_regions
                    if institution_regions:
                        for institution_region in institution_regions:
                            region = institution_region.regions
                            if region:
                                self.texts.append(region.region_name)
                                self.texts.append(region.region_code)
                else:
                    logging.warning("no institute in data_to_text")
            else:
                logging.warning("no support in data_to_text")

    async def get_texts(self) -> str:
        """
        :return: list of texts
        """
        return "".join(self.texts)
