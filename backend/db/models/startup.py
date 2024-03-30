from typing import List, Optional

from sqlalchemy import Date, DateTime, Float, ForeignKeyConstraint, Index, Integer, String, Text, text
from sqlalchemy.dialects.mysql import LONGTEXT, TINYINT
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from db.engine import Base


class ApiSettings(Base):
    __tablename__ = 'api_settings'

    id_api_settings = mapped_column(Integer, primary_key=True)
    zvonobot = mapped_column(String(1000))
    jivo = mapped_column(String(1000))
    yandex = mapped_column(Text)
    smsc_login = mapped_column(String(255))
    smsc_password = mapped_column(String(255))
    leader_id = mapped_column(String(1000))
    leader_secret = mapped_column(String(1000))
    only_leader = mapped_column(TINYINT(1))
    only_auth = mapped_column(TINYINT(1))
    type_call = mapped_column(String(45), server_default=text("'plusofon'"))
    plusofon_client = mapped_column(String(255))
    plusofon_token = mapped_column(String(1000))
    storage_key = mapped_column(String(255))
    storage_secret = mapped_column(String(255))
    storage_bucket = mapped_column(String(255))


class AuthAttempt(Base):
    __tablename__ = 'auth_attempt'
    __table_args__ = (
        Index('phone_UNIQUE', 'phone', unique=True),
    )

    id_auth_attempt = mapped_column(Integer, primary_key=True)
    phone = mapped_column(String(20))
    count_attempt = mapped_column(Integer)


class CertificateType(Base):
    __tablename__ = 'certificate_type'

    id_certificate_type = mapped_column(Integer, primary_key=True)
    name_of_certificate_type = mapped_column(String(600))

    certificate_templates: Mapped[List['CertificateTemplates']] = relationship('CertificateTemplates', uselist=True,
                                                                               back_populates='certificate_type')
    certificates: Mapped[List['Certificates']] = relationship('Certificates', uselist=True,
                                                              back_populates='certificate_type')


class Config(Base):
    __tablename__ = 'config'

    id_config = mapped_column(Integer, primary_key=True)
    logo = mapped_column(LONGTEXT, comment='Логотип после авторизации\n')
    wallpaper = mapped_column(LONGTEXT, comment='Заставка авторизации')
    background_header = mapped_column(String(45), server_default=text("'#343a40'"), comment='hex шапки\n')
    background_nav = mapped_column(String(45), server_default=text("'#474f56'"), comment='HEX навигации\n')
    color_header = mapped_column(String(45), server_default=text("'#b7bcc1'"), comment='hex цвета шрифта шапки')
    color_nav = mapped_column(String(45), server_default=text("'#ffffff'"), comment='hex цвета шрифта навигации')
    background_btn = mapped_column(String(45), server_default=text("'#3d8acc'"))
    robots = mapped_column(Text)
    title = mapped_column(String(255))
    description = mapped_column(String(600))
    active_step = mapped_column(String(45))
    logo_auth = mapped_column(LONGTEXT)


class EventRoles(Base):
    __tablename__ = 'event_roles'

    id_event_roles = mapped_column(Integer, primary_key=True)
    event_role_name = mapped_column(String(255))

    user_events: Mapped[List['UserEvents']] = relationship('UserEvents', uselist=True, back_populates='event_roles')


class EventStatuses(Base):
    __tablename__ = 'event_statuses'

    id_event_statuses = mapped_column(Integer, primary_key=True)
    status_event_name = mapped_column(String(255))

    forms: Mapped[List['Forms']] = relationship('Forms', uselist=True, back_populates='event_statuses')


class ExpertiseCriteriaTypes(Base):
    __tablename__ = 'expertise_criteria_types'

    id_expertise_criteria_types = mapped_column(Integer, primary_key=True)
    type_name = mapped_column(String(45))
    description = mapped_column(String(255))

    expertise_criteria: Mapped[List['ExpertiseCriteria']] = relationship('ExpertiseCriteria', uselist=True,
                                                                         back_populates='expertise_criteria_types')
    template_expertise_criteria: Mapped[List['TemplateExpertiseCriteria']] = relationship('TemplateExpertiseCriteria',
                                                                                          uselist=True,
                                                                                          back_populates='expertise_criteria_types')


class FeedbackFieldTypes(Base):
    __tablename__ = 'feedback_field_types'

    id_feedback_field_types = mapped_column(Integer, primary_key=True)
    type_name = mapped_column(String(45))
    description = mapped_column(String(255))

    feedback_form_fields: Mapped[List['FeedbackFormFields']] = relationship('FeedbackFormFields', uselist=True,
                                                                            back_populates='feedback_field_types')
    template_feedback_form_fields: Mapped[List['TemplateFeedbackFormFields']] = relationship(
        'TemplateFeedbackFormFields', uselist=True, back_populates='feedback_field_types')


class FieldTypes(Base):
    __tablename__ = 'field_types'

    id_field_types = mapped_column(Integer, primary_key=True)
    type_name = mapped_column(String(45))
    description = mapped_column(String(255))

    form_fields: Mapped[List['FormFields']] = relationship('FormFields', uselist=True, back_populates='field_types')
    template_fields: Mapped[List['TemplateFields']] = relationship('TemplateFields', uselist=True,
                                                                   back_populates='field_types')


class Groups(Base):
    __tablename__ = 'groups'

    id_groups = mapped_column(Integer, primary_key=True)
    group_name = mapped_column(String(45))

    users: Mapped[List['Users']] = relationship('Users', uselist=True, back_populates='groups')


class InstitutionForms(Base):
    __tablename__ = 'institution_forms'

    id_institution_forms = mapped_column(Integer, primary_key=True)
    institution_form_name = mapped_column(String(600))

    institution_institution_forms: Mapped[List['InstitutionInstitutionForms']] = relationship(
        'InstitutionInstitutionForms', uselist=True, back_populates='institution_forms')


class InstitutionStatuses(Base):
    __tablename__ = 'institution_statuses'

    id_institution_statuses = mapped_column(Integer, primary_key=True)
    status_name = mapped_column(String(45))

    institutes: Mapped[List['Institutes']] = relationship('Institutes', uselist=True,
                                                          back_populates='institution_statuses')


class Markers(Base):
    __tablename__ = 'markers'

    id_markers = mapped_column(Integer, primary_key=True)
    marker = mapped_column(String(255))

    user_markers: Mapped[List['UserMarkers']] = relationship('UserMarkers', uselist=True, back_populates='markers')


class PassportFieldTypes(Base):
    __tablename__ = 'passport_field_types'

    id_passport_field_types = mapped_column(Integer, primary_key=True)
    type_name = mapped_column(String(45))
    description = mapped_column(String(255))

    passport_fields: Mapped[List['PassportFields']] = relationship('PassportFields', uselist=True,
                                                                   back_populates='passport_field_types')
    template_passport_fields: Mapped[List['TemplatePassportFields']] = relationship('TemplatePassportFields',
                                                                                    uselist=True,
                                                                                    back_populates='passport_field_types')


class PassportStatuses(Base):
    __tablename__ = 'passport_statuses'

    id_passport_statuses = mapped_column(Integer, primary_key=True)
    status_name = mapped_column(String(255))

    passport_information: Mapped[List['PassportInformation']] = relationship('PassportInformation', uselist=True,
                                                                             back_populates='passport_statuses')


class ProjectRoles(Base):
    __tablename__ = 'project_roles'

    id_project_roles = mapped_column(Integer, primary_key=True)
    project_role_name = mapped_column(String(255))

    user_project: Mapped[List['UserProject']] = relationship('UserProject', uselist=True,
                                                             back_populates='project_roles')


class ProjectSearchType(Base):
    __tablename__ = 'project_search_type'

    id_project_search_type = mapped_column(Integer, primary_key=True)
    name_of_search_type = mapped_column(String(255))

    project_search: Mapped[List['ProjectSearch']] = relationship('ProjectSearch', uselist=True,
                                                                 back_populates='project_search_type')


class ProjectStatuses(Base):
    __tablename__ = 'project_statuses'

    id_project_statuses = mapped_column(Integer, primary_key=True)
    status_project_name = mapped_column(String(45))
    priority = mapped_column(Integer)

    projects: Mapped[List['Projects']] = relationship('Projects', uselist=True, back_populates='project_statuses')


class Regions(Base):
    __tablename__ = 'regions'

    id_regions = mapped_column(Integer, primary_key=True)
    region_name = mapped_column(String(255))
    region_code = mapped_column(String(255))

    institution_regions: Mapped[List['InstitutionRegions']] = relationship('InstitutionRegions', uselist=True,
                                                                           back_populates='regions')
    support_regions: Mapped[List['SupportRegions']] = relationship('SupportRegions', uselist=True,
                                                                   back_populates='regions')


class Sendpulse(Base):
    __tablename__ = 'sendpulse'

    id_sendpulse = mapped_column(Integer, primary_key=True)
    confirm_register = mapped_column(String(255))
    demo_day = mapped_column(String(255))
    acceleration = mapped_column(String(255))
    qualifying = mapped_column(String(255))
    applicant = mapped_column(String(255))
    info = mapped_column(String(255))
    good = mapped_column(String(255))
    rejected = mapped_column(String(255))
    failed_moderation = mapped_column(String(255))
    expertise = mapped_column(String(255))
    moderation = mapped_column(String(255))
    confirm_email = mapped_column(String(255))
    user_id = mapped_column(String(1000))
    secret = mapped_column(String(1000))


class Sendsay(Base):
    __tablename__ = 'sendsay'

    id_sendsay = mapped_column(Integer, primary_key=True)
    confirm_register = mapped_column(String(255))
    demo_day = mapped_column(String(255))
    acceleration = mapped_column(String(255))
    qualifying = mapped_column(String(255))
    applicant = mapped_column(String(255))
    info = mapped_column(String(255))
    good = mapped_column(String(255))
    rejected = mapped_column(String(255))
    failed_moderation = mapped_column(String(255))
    expertise = mapped_column(String(255))
    moderation = mapped_column(String(255))
    confirm_email = mapped_column(String(255))
    login = mapped_column(String(1000))
    api_key = mapped_column(String(1000))
    preacceleration = mapped_column(String(1000))
    completed = mapped_column(String(1000))
    postaccompaniment = mapped_column(String(1000))


class SendsayLogs(Base):
    __tablename__ = 'sendsay_logs'

    id_sendsay_logs = mapped_column(Integer, primary_key=True)
    email = mapped_column(String(100))
    track_id = mapped_column(String(45))
    warnings = mapped_column(String(1000))
    subject = mapped_column(String(1000))
    date_creation = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class SupportDirections(Base):
    __tablename__ = 'support_directions'

    id_support_directions = mapped_column(Integer, primary_key=True)
    support_direction_name = mapped_column(String(600))

    support_support_directions: Mapped[List['SupportSupportDirections']] = relationship('SupportSupportDirections',
                                                                                        uselist=True,
                                                                                        back_populates='support_directions')


class SupportForms(Base):
    __tablename__ = 'support_forms'

    id_support_forms = mapped_column(Integer, primary_key=True)
    support_form_name = mapped_column(String(600))

    support_support_forms: Mapped[List['SupportSupportForms']] = relationship('SupportSupportForms', uselist=True,
                                                                              back_populates='support_forms')


class SupportMembers(Base):
    __tablename__ = 'support_members'

    id_support_members = mapped_column(Integer, primary_key=True)
    support_members_name = mapped_column(String(600))

    support_support_members: Mapped[List['SupportSupportMembers']] = relationship('SupportSupportMembers', uselist=True,
                                                                                  back_populates='support_members')


class SupportReasons(Base):
    __tablename__ = 'support_reasons'

    id_support_reasons = mapped_column(Integer, primary_key=True)
    support_reason_name = mapped_column(String(600))

    support_support_reasons: Mapped[List['SupportSupportReasons']] = relationship('SupportSupportReasons', uselist=True,
                                                                                  back_populates='support_reasons')


class SupportStatuses(Base):
    __tablename__ = 'support_statuses'

    id_support_statuses = mapped_column(Integer, primary_key=True)
    status_name = mapped_column(String(45))

    supports: Mapped[List['Supports']] = relationship('Supports', uselist=True, back_populates='support_statuses')


class TrackingFieldTypes(Base):
    __tablename__ = 'tracking_field_types'

    id_tracking_field_types = mapped_column(Integer, primary_key=True)
    type_name = mapped_column(String(45))
    description = mapped_column(String(255))

    tracking_form_fields: Mapped[List['TrackingFormFields']] = relationship('TrackingFormFields', uselist=True,
                                                                            back_populates='tracking_field_types')
    tracking_template_fields: Mapped[List['TrackingTemplateFields']] = relationship('TrackingTemplateFields',
                                                                                    uselist=True,
                                                                                    back_populates='tracking_field_types')


class TrackingStatuses(Base):
    __tablename__ = 'tracking_statuses'

    id_tracking_statuses = mapped_column(Integer, primary_key=True)
    status_tracking_name = mapped_column(String(255))

    tracking_information: Mapped[List['TrackingInformation']] = relationship('TrackingInformation', uselist=True,
                                                                             back_populates='tracking_statuses')


class Forms(Base):
    __tablename__ = 'forms'
    __table_args__ = (
        ForeignKeyConstraint(['event_statuses_id_event_statuses'], ['event_statuses.id_event_statuses'],
                             name='fk_forms_event_statuses1'),
        Index('fk_forms_event_statuses1_idx', 'event_statuses_id_event_statuses')
    )

    id_forms = mapped_column(Integer, primary_key=True)
    event_statuses_id_event_statuses = mapped_column(Integer, nullable=False)
    form_name = mapped_column(String(1000))
    description = mapped_column(Text)  # used
    date_end = mapped_column(DateTime)
    date_start = mapped_column(DateTime)
    logo = mapped_column(String(255))
    background = mapped_column(String(255))
    prizes = mapped_column(Text)
    organizers = mapped_column(Text)
    site = mapped_column(String(255))
    city = mapped_column(String(255))
    contact_person = mapped_column(String(255))
    email = mapped_column(String(255))
    phone = mapped_column(String(45))
    file1 = mapped_column(String(255))
    file2 = mapped_column(String(255))
    file3 = mapped_column(String(255))
    tag = mapped_column(String(255))
    background_thumb = mapped_column(String(255))
    members = mapped_column(Text)  # used
    event_format = mapped_column(String(100))  # used
    date_event_end = mapped_column(DateTime)
    date_event_start = mapped_column(DateTime)
    date_expertises_start = mapped_column(DateTime)
    date_expertises_end = mapped_column(DateTime)
    date_tracking_start = mapped_column(DateTime)
    date_tracking_end = mapped_column(DateTime)
    date_training_start = mapped_column(DateTime)
    date_training_end = mapped_column(DateTime)
    form_date_creation = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    guid_leader = mapped_column(String(200))
    contact_person2 = mapped_column(String(255))
    email2 = mapped_column(String(255))
    phone2 = mapped_column(String(45))
    contact_person3 = mapped_column(String(45))
    email3 = mapped_column(String(45))
    phone3 = mapped_column(String(45))
    feedback = mapped_column(TINYINT(1), server_default=text("'0'"))

    event_statuses: Mapped['EventStatuses'] = relationship('EventStatuses', back_populates='forms')
    allow_base: Mapped[List['AllowBase']] = relationship('AllowBase', uselist=True, back_populates='forms')
    certificate_templates: Mapped[List['CertificateTemplates']] = relationship('CertificateTemplates', uselist=True,
                                                                               back_populates='forms')
    direction_events: Mapped[List['DirectionEvents']] = relationship('DirectionEvents', uselist=True,
                                                                     back_populates='forms')
    expertises: Mapped[List['Expertises']] = relationship('Expertises', uselist=True, back_populates='forms')
    feedback_form_fields: Mapped[List['FeedbackFormFields']] = relationship('FeedbackFormFields', uselist=True,
                                                                            back_populates='forms')
    form_fields: Mapped[List['FormFields']] = relationship('FormFields', uselist=True, back_populates='forms')
    industry_directions: Mapped[List['IndustryDirections']] = relationship('IndustryDirections', uselist=True,
                                                                           back_populates='forms')
    learning_modules: Mapped[List['LearningModules']] = relationship('LearningModules', uselist=True,
                                                                     back_populates='forms')
    moder_criteria: Mapped[List['ModerCriteria']] = relationship('ModerCriteria', uselist=True, back_populates='forms')
    passports: Mapped[List['Passports']] = relationship('Passports', uselist=True, back_populates='forms')
    pervich_criteria: Mapped[List['PervichCriteria']] = relationship('PervichCriteria', uselist=True,
                                                                     back_populates='forms')
    steps: Mapped[List['Steps']] = relationship('Steps', uselist=True, back_populates='forms')
    tracking_form_fields: Mapped[List['TrackingFormFields']] = relationship('TrackingFormFields', uselist=True,
                                                                            back_populates='forms')
    tracking_steps: Mapped[List['TrackingSteps']] = relationship('TrackingSteps', uselist=True, back_populates='forms')
    user_events: Mapped[List['UserEvents']] = relationship('UserEvents', uselist=True, back_populates='forms')
    user_files: Mapped[List['UserFiles']] = relationship('UserFiles', uselist=True, back_populates='forms')
    utm_events: Mapped[List['UtmEvents']] = relationship('UtmEvents', uselist=True, back_populates='forms')
    expertise_criteria: Mapped[List['ExpertiseCriteria']] = relationship('ExpertiseCriteria', uselist=True,
                                                                         back_populates='forms')
    projects: Mapped[List['Projects']] = relationship('Projects', uselist=True, back_populates='forms')
    certificates: Mapped[List['Certificates']] = relationship('Certificates', uselist=True, back_populates='forms')


class Institutes(Base):
    __tablename__ = 'institutes'
    __table_args__ = (
        ForeignKeyConstraint(['institution_statuses_id_institution_statuses'],
                             ['institution_statuses.id_institution_statuses'],
                             name='fk_institutes_institution_statuses1'),
        Index('fk_institutes_institution_statuses1_idx', 'institution_statuses_id_institution_statuses'),
        Index('id_institutes_ctt_UNIQUE', 'id_institutes_ctt', unique=True),
        Index('institute_name_UNIQUE', 'institute_name', unique=True)
    )

    id_institutes = mapped_column(Integer, primary_key=True)
    institution_statuses_id_institution_statuses = mapped_column(Integer, nullable=False)
    institute_name = mapped_column(String(1000))
    site = mapped_column(String(1000))
    logo = mapped_column(String(600))
    description = mapped_column(Text)
    logo_thumb = mapped_column(String(600))
    date_creation = mapped_column(DateTime)
    id_institutes_ctt = mapped_column(Integer)

    institution_statuses: Mapped['InstitutionStatuses'] = relationship('InstitutionStatuses',
                                                                       back_populates='institutes')
    institution_institution_forms: Mapped[List['InstitutionInstitutionForms']] = relationship(
        'InstitutionInstitutionForms', uselist=True, back_populates='institutes')
    institution_regions: Mapped[List['InstitutionRegions']] = relationship('InstitutionRegions', uselist=True,
                                                                           back_populates='institutes')
    supports: Mapped[List['Supports']] = relationship('Supports', uselist=True, back_populates='institutes')


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        ForeignKeyConstraint(['groups_id_groups'], ['groups.id_groups'], name='fk_users_groups'),
        Index('email_UNIQUE', 'email', unique=True),
        Index('fk_users_groups_idx', 'groups_id_groups'),
        Index('phone_UNIQUE', 'phone', unique=True)
    )

    id = mapped_column(Integer, primary_key=True)
    groups_id_groups = mapped_column(Integer, nullable=False)
    first_name = mapped_column(String(255))
    last_name = mapped_column(String(255))
    patronymic = mapped_column(String(255))
    country = mapped_column(String(255))  # used
    region = mapped_column(String(255))  # used
    locality = mapped_column(String(255))  # used
    email = mapped_column(String(255))
    phone = mapped_column(String(200))
    password = mapped_column(String(255))
    activate_key = mapped_column(String(45))
    activate = mapped_column(TINYINT)
    date_reg = mapped_column(Date)
    date_of_birth = mapped_column(Date)
    place_of_work_study = mapped_column(String(400))  # used
    name_of_company = mapped_column(String(400))  # used
    position = mapped_column(String(400))  # used
    education = mapped_column(String(600))  # used
    specialty = mapped_column(String(600))  # used
    university = mapped_column(String(255))  # used
    academic_degree = mapped_column(String(255))  # used
    academic_rank = mapped_column(String(255))  # used
    experience = mapped_column(Text)  # used
    progress = mapped_column(Text)  # used
    skype = mapped_column(String(255))
    facebook = mapped_column(String(255))
    vk = mapped_column(String(255))
    resume1 = mapped_column(Text)  # used
    resume2 = mapped_column(Text)  # used
    resume3 = mapped_column(String(500))  # used
    photo = mapped_column(String(255))
    photo_thumb = mapped_column(String(255))
    inn = mapped_column(String(256))
    year_of_graduation = mapped_column(String(45))  # used
    scientific_specialty = mapped_column(Text)  # used
    work_experience = mapped_column(Text)  # used
    tracking_experience = mapped_column(Text)  # used
    business_experience = mapped_column(Text)  # used
    teaching_experience = mapped_column(Text)  # used
    expertise_experience = mapped_column(Text)  # used
    number_of_publications = mapped_column(Integer)
    number_of_scopus = mapped_column(Integer)
    h_index_rsci = mapped_column(Integer)
    h_index_scopus = mapped_column(Integer)
    main_publications = mapped_column(Text)  # used
    languages = mapped_column(Text)  # used
    programs = mapped_column(Text)  # used
    activate_email_key = mapped_column(String(255))
    activate_email = mapped_column(TINYINT(1))
    max_events = mapped_column(Integer, server_default=text("'0'"))
    ban = mapped_column(TINYINT(1))
    temporary_password = mapped_column(TINYINT(1), server_default=text("'0'"))
    date_hash = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    id_leader = mapped_column(Integer)
    token_leader = mapped_column(Text)

    groups: Mapped['Groups'] = relationship('Groups', back_populates='users')
    allow_base: Mapped[List['AllowBase']] = relationship('AllowBase', uselist=True, back_populates='users')
    delete_storage: Mapped[List['DeleteStorage']] = relationship('DeleteStorage', uselist=True, back_populates='users')
    expertise_templates: Mapped[List['ExpertiseTemplates']] = relationship('ExpertiseTemplates', uselist=True,
                                                                           back_populates='users')
    learning_templates: Mapped[List['LearningTemplates']] = relationship('LearningTemplates', uselist=True,
                                                                         back_populates='users')
    resume_files: Mapped[List['ResumeFiles']] = relationship('ResumeFiles', uselist=True, back_populates='users')
    sessions: Mapped[List['Sessions']] = relationship('Sessions', uselist=True, back_populates='users')
    subscriptions: Mapped[List['Subscriptions']] = relationship('Subscriptions', uselist=True, back_populates='users')
    template_passports: Mapped[List['TemplatePassports']] = relationship('TemplatePassports', uselist=True,
                                                                         back_populates='users')
    templates: Mapped[List['Templates']] = relationship('Templates', uselist=True, back_populates='users')
    tracking_templates: Mapped[List['TrackingTemplates']] = relationship('TrackingTemplates', uselist=True,
                                                                         back_populates='users')
    user_events: Mapped[List['UserEvents']] = relationship('UserEvents', uselist=True, back_populates='users')
    user_files: Mapped[List['UserFiles']] = relationship('UserFiles', uselist=True, back_populates='users')
    user_markers: Mapped[List['UserMarkers']] = relationship('UserMarkers', uselist=True, back_populates='users')
    utm: Mapped[List['Utm']] = relationship('Utm', uselist=True, back_populates='users')
    utm_events: Mapped[List['UtmEvents']] = relationship('UtmEvents', uselist=True, back_populates='users')
    utm_role: Mapped[List['UtmRole']] = relationship('UtmRole', uselist=True, back_populates='users')
    allow_forms: Mapped[List['AllowForms']] = relationship('AllowForms', uselist=True, back_populates='users')
    certificates: Mapped[List['Certificates']] = relationship('Certificates', uselist=True, back_populates='users')
    learning_leader: Mapped[List['LearningLeader']] = relationship('LearningLeader', uselist=True,
                                                                   back_populates='users')
    lecturers: Mapped[List['Lecturers']] = relationship('Lecturers', uselist=True, back_populates='users')
    tracking_storage: Mapped[List['TrackingStorage']] = relationship('TrackingStorage', uselist=True,
                                                                     back_populates='users')
    user_project: Mapped[List['UserProject']] = relationship('UserProject', uselist=True, back_populates='users')


class AllowBase(Base):
    __tablename__ = 'allow_base'
    __table_args__ = (
        ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], ondelete='CASCADE', name='fk_allow_base_forms1'),
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE', name='fk_allow_base_users1'),
        Index('fk_allow_base_forms1_idx', 'forms_id_forms'),
        Index('fk_allow_base_users1_idx', 'users_id')
    )

    id_allow_users = mapped_column(Integer, primary_key=True)
    users_id = mapped_column(Integer, nullable=False)
    forms_id_forms = mapped_column(Integer, nullable=False)
    personal = mapped_column(TINYINT(1))
    work = mapped_column(TINYINT(1))
    contacts = mapped_column(TINYINT(1))
    resume = mapped_column(TINYINT(1))
    tracking_form = mapped_column(TINYINT(1))
    tracking_summary = mapped_column(TINYINT(1))
    expertise = mapped_column(TINYINT(1))
    learning = mapped_column(TINYINT(1))

    forms: Mapped['Forms'] = relationship('Forms', back_populates='allow_base')
    users: Mapped['Users'] = relationship('Users', back_populates='allow_base')


class CertificateTemplates(Base):
    __tablename__ = 'certificate_templates'
    __table_args__ = (
        ForeignKeyConstraint(['certificate_type_id_certificate_type'], ['certificate_type.id_certificate_type'],
                             name='fk_certificate_templates_certificate_type1'),
        ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], ondelete='CASCADE',
                             name='fk_certificate_templates_forms1'),
        Index('fk_certificate_templates_certificate_type1_idx', 'certificate_type_id_certificate_type'),
        Index('fk_certificate_templates_forms1_idx', 'forms_id_forms')
    )

    id_certificate_templates = mapped_column(Integer, primary_key=True)
    forms_id_forms = mapped_column(Integer, nullable=False)
    certificate_type_id_certificate_type = mapped_column(Integer, nullable=False)
    x_fio = mapped_column(Integer)
    y_fio = mapped_column(Integer)
    font = mapped_column(String(600))
    url_file = mapped_column(String(600))
    size_fio = mapped_column(Integer)
    x_project = mapped_column(Integer)
    y_project = mapped_column(Integer)
    size_project = mapped_column(Integer)
    break_fio = mapped_column(Integer)
    break_project = mapped_column(Integer)
    color = mapped_column(String(45))
    date_cert = mapped_column(Date)
    status = mapped_column(String(600))
    name_of_certificate = mapped_column(String(200))

    certificate_type: Mapped['CertificateType'] = relationship('CertificateType',
                                                               back_populates='certificate_templates')
    forms: Mapped['Forms'] = relationship('Forms', back_populates='certificate_templates')


class DeleteStorage(Base):
    __tablename__ = 'delete_storage'
    __table_args__ = (
        ForeignKeyConstraint(['users_id'], ['users.id'], name='fk_delete_storage_users1'),
        Index('fk_delete_storage_users1_idx', 'users_id')
    )

    id_delete_storage = mapped_column(Integer, primary_key=True)
    users_id = mapped_column(Integer, nullable=False)
    key = mapped_column(String(500))
    date_creation = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    full = mapped_column(TINYINT(1))

    users: Mapped['Users'] = relationship('Users', back_populates='delete_storage')


class DirectionEvents(Base):
    __tablename__ = 'direction_events'
    __table_args__ = (
        ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], name='fk_direction_events_forms1'),
        Index('fk_direction_events_forms1_idx', 'forms_id_forms')
    )

    id_direction_events = mapped_column(Integer, primary_key=True)
    forms_id_forms = mapped_column(Integer, nullable=False)
    direction_name = mapped_column(String(255))

    forms: Mapped['Forms'] = relationship('Forms', back_populates='direction_events')


class ExpertiseTemplates(Base):
    __tablename__ = 'expertise_templates'
    __table_args__ = (
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='SET NULL', name='fk_expertise_templates_users1'),
        Index('fk_expertise_templates_users1_idx', 'users_id')
    )

    id_expertise_templates = mapped_column(Integer, primary_key=True)
    template_name = mapped_column(String(45))
    users_id = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', back_populates='expertise_templates')
    template_expertises: Mapped[List['TemplateExpertises']] = relationship('TemplateExpertises', uselist=True,
                                                                           back_populates='expertise_templates')
    template_expertise_criteria: Mapped[List['TemplateExpertiseCriteria']] = relationship('TemplateExpertiseCriteria',
                                                                                          uselist=True,
                                                                                          back_populates='expertise_templates')


class Expertises(Base):
    __tablename__ = 'expertises'
    __table_args__ = (
        ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], ondelete='CASCADE', name='fk_expertises_forms1'),
        Index('fk_expertises_forms1_idx', 'forms_id_forms')
    )

    id_expertises = mapped_column(Integer, primary_key=True)
    expertise_name = mapped_column(String(255))
    forms_id_forms = mapped_column(Integer)
    expertise_code = mapped_column(String(45))
    priority = mapped_column(Integer)
    closed = mapped_column(TINYINT(1))

    forms: Mapped[Optional['Forms']] = relationship('Forms', back_populates='expertises')
    expertise_criteria: Mapped[List['ExpertiseCriteria']] = relationship('ExpertiseCriteria', uselist=True,
                                                                         back_populates='expertises')
    project_search: Mapped[List['ProjectSearch']] = relationship('ProjectSearch', uselist=True,
                                                                 back_populates='expertises')
    experts: Mapped[List['Experts']] = relationship('Experts', uselist=True, back_populates='expertises')
    expertise_information: Mapped[List['ExpertiseInformation']] = relationship('ExpertiseInformation', uselist=True,
                                                                               back_populates='expertises')
    expertise_project_data: Mapped[List['ExpertiseProjectData']] = relationship('ExpertiseProjectData', uselist=True,
                                                                                back_populates='expertises')


class FeedbackFormFields(Base):
    __tablename__ = 'feedback_form_fields'
    __table_args__ = (ForeignKeyConstraint(['feedback_field_types_id_feedback_field_types'],
                                           ['feedback_field_types.id_feedback_field_types'],
                                           name='fk_feedback_form_fields_feedback_field_types1'),
                      ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], ondelete='CASCADE',
                                           name='fk_form_fields_forms11'),
                      Index('fk_feedback_form_fields_feedback_field_types1_idx',
                            'feedback_field_types_id_feedback_field_types'),
                      Index('fk_form_fields_forms1_idx', 'forms_id_forms')
                      )

    id_feedback_form_fields = mapped_column(Integer, primary_key=True)
    forms_id_forms = mapped_column(Integer, nullable=False)
    feedback_field_types_id_feedback_field_types = mapped_column(Integer, nullable=False)
    field_name = mapped_column(String(255))
    label = mapped_column(String(255))
    required = mapped_column(TINYINT)
    priority = mapped_column(Integer)
    hint = mapped_column(String(600))
    max_value = mapped_column(Integer)
    min_value = mapped_column(Integer)
    default_value = mapped_column(String(800))

    feedback_field_types: Mapped['FeedbackFieldTypes'] = relationship('FeedbackFieldTypes',
                                                                      back_populates='feedback_form_fields')
    forms: Mapped['Forms'] = relationship('Forms', back_populates='feedback_form_fields')
    feedback_sets_values_fields: Mapped[List['FeedbackSetsValuesFields']] = relationship('FeedbackSetsValuesFields',
                                                                                         uselist=True,
                                                                                         back_populates='feedback_form_fields')


class FormFields(Base):
    __tablename__ = 'form_fields'

    __table_args__ = (
        ForeignKeyConstraint(['field_types_id_field_types'], ['field_types.id_field_types'], ondelete='CASCADE',
                             name='fk_forms_field_types1'),
        ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], ondelete='CASCADE', name='fk_form_fields_forms1'),
        Index('fk_form_fields_forms1_idx', 'forms_id_forms'),
        Index('fk_forms_field_types1_idx', 'field_types_id_field_types')
    )

    id_form_fields = mapped_column(Integer, primary_key=True)
    field_types_id_field_types = mapped_column(Integer, nullable=False)
    forms_id_forms = mapped_column(Integer, nullable=False)
    field_name = mapped_column(String(255))
    step = mapped_column(Integer)
    label = mapped_column(String(255))
    required = mapped_column(TINYINT)
    priority = mapped_column(Integer)
    hint = mapped_column(String(600))
    max_value = mapped_column(Integer)
    min_value = mapped_column(Integer)
    default_value = mapped_column(String(800))
    guid_leader = mapped_column(String(200))

    field_types: Mapped['FieldTypes'] = relationship('FieldTypes', back_populates='form_fields')
    forms: Mapped['Forms'] = relationship('Forms', back_populates='form_fields')
    allow_forms: Mapped[List['AllowForms']] = relationship('AllowForms', uselist=True, back_populates='form_fields')
    passport_fields: Mapped[List['PassportFields']] = relationship('PassportFields', uselist=True,
                                                                   back_populates='form_fields')
    project_search: Mapped[List['ProjectSearch']] = relationship('ProjectSearch', uselist=True,
                                                                 back_populates='form_fields')
    sets_values_fields: Mapped[List['SetsValuesFields']] = relationship('SetsValuesFields', uselist=True,
                                                                        back_populates='form_fields')
    project_data: Mapped[List['ProjectData']] = relationship('ProjectData', back_populates='form_fields')

class IndustryDirections(Base):
    __tablename__ = 'industry_directions'
    __table_args__ = (
        ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], ondelete='CASCADE',
                             name='fk_industry_directions_forms1'),
        Index('fk_industry_directions_forms1_idx', 'forms_id_forms')
    )

    id_industry_directions = mapped_column(Integer, primary_key=True)
    forms_id_forms = mapped_column(Integer, nullable=False)
    direction = mapped_column(String(255))

    forms: Mapped['Forms'] = relationship('Forms', back_populates='industry_directions')
    projects: Mapped[List['Projects']] = relationship('Projects', uselist=True, back_populates='industry_directions')


class InstitutionInstitutionForms(Base):
    __tablename__ = 'institution_institution_forms'
    __table_args__ = (
        ForeignKeyConstraint(['institutes_id_institutes'], ['institutes.id_institutes'], ondelete='CASCADE',
                             name='fk_institution_institution_forms_institutes1'),
        ForeignKeyConstraint(['institution_forms_id_institution_forms'], ['institution_forms.id_institution_forms'],
                             ondelete='CASCADE', name='fk_institution_institution_forms_institution_forms1'),
        Index('fk_institution_institution_forms_institutes1_idx', 'institutes_id_institutes'),
        Index('fk_institution_institution_forms_institution_forms1_idx', 'institution_forms_id_institution_forms')
    )

    id_institution_institution_forms = mapped_column(Integer, primary_key=True)
    institution_forms_id_institution_forms = mapped_column(Integer, nullable=False)
    institutes_id_institutes = mapped_column(Integer, nullable=False)

    institutes: Mapped['Institutes'] = relationship('Institutes', back_populates='institution_institution_forms')
    institution_forms: Mapped['InstitutionForms'] = relationship('InstitutionForms',
                                                                 back_populates='institution_institution_forms')


class InstitutionRegions(Base):
    __tablename__ = 'institution_regions'
    __table_args__ = (
        ForeignKeyConstraint(['institutes_id_institutes'], ['institutes.id_institutes'], ondelete='CASCADE',
                             name='fk_institution_region_institutes1'),
        ForeignKeyConstraint(['regions_id_regions'], ['regions.id_regions'], ondelete='CASCADE',
                             name='fk_institution_region_regions1'),
        Index('fk_institution_region_institutes1_idx', 'institutes_id_institutes'),
        Index('fk_institution_region_regions1_idx', 'regions_id_regions')
    )

    id_institution_region = mapped_column(Integer, primary_key=True)
    regions_id_regions = mapped_column(Integer, nullable=False)
    institutes_id_institutes = mapped_column(Integer, nullable=False)

    institutes: Mapped['Institutes'] = relationship('Institutes', back_populates='institution_regions')
    regions: Mapped['Regions'] = relationship('Regions', back_populates='institution_regions')


class LearningModules(Base):
    __tablename__ = 'learning_modules'
    __table_args__ = (
        ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], ondelete='CASCADE',
                             name='fk_learning_modules_forms1'),
        Index('fk_learning_modules_forms1_idx', 'forms_id_forms')
    )

    id_learning_modules = mapped_column(Integer, primary_key=True)
    forms_id_forms = mapped_column(Integer, nullable=False)
    date_start = mapped_column(Date)
    date_end = mapped_column(Date)
    closed = mapped_column(TINYINT(1))
    module_name = mapped_column(String(1000))
    important = mapped_column(String(600))

    forms: Mapped['Forms'] = relationship('Forms', back_populates='learning_modules')
    learning_topics: Mapped[List['LearningTopics']] = relationship('LearningTopics', uselist=True,
                                                                   back_populates='learning_modules')


class LearningTemplates(Base):
    __tablename__ = 'learning_templates'
    __table_args__ = (
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='SET NULL', name='fk_learning_templates_users1'),
        Index('fk_learning_templates_users1_idx', 'users_id')
    )

    id_learning_templates = mapped_column(Integer, primary_key=True)
    template_name = mapped_column(String(255))
    users_id = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', back_populates='learning_templates')
    template_feedback_form_fields: Mapped[List['TemplateFeedbackFormFields']] = relationship(
        'TemplateFeedbackFormFields', uselist=True, back_populates='learning_templates')
    template_learning_modules: Mapped[List['TemplateLearningModules']] = relationship('TemplateLearningModules',
                                                                                      uselist=True,
                                                                                      back_populates='learning_templates')


class ModerCriteria(Base):
    __tablename__ = 'moder_criteria'
    __table_args__ = (
        ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], ondelete='CASCADE',
                             name='fk_moder_criteria_forms2'),
        Index('fk_moder_criteria_forms2_idx', 'forms_id_forms')
    )

    id_moder_criteria = mapped_column(Integer, primary_key=True)
    forms_id_forms = mapped_column(Integer, nullable=False)
    criterion_moder_name = mapped_column(String(255))
    description_moder_criteria = mapped_column(String(255))

    forms: Mapped['Forms'] = relationship('Forms', back_populates='moder_criteria')
    project_moder_evaluation: Mapped[List['ProjectModerEvaluation']] = relationship('ProjectModerEvaluation',
                                                                                    uselist=True,
                                                                                    back_populates='moder_criteria')


class Passports(Base):
    __tablename__ = 'passports'
    __table_args__ = (
        ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], ondelete='CASCADE', name='fk_passports_forms1'),
        Index('fk_passports_forms1_idx', 'forms_id_forms')
    )

    id_passports = mapped_column(Integer, primary_key=True)
    forms_id_forms = mapped_column(Integer, nullable=False)
    passport_name = mapped_column(String(255))
    priority = mapped_column(Integer)
    closed = mapped_column(TINYINT(1))
    date_start = mapped_column(Date)
    date_end = mapped_column(Date)
    status = mapped_column(String(600))
    description = mapped_column(Text)

    forms: Mapped['Forms'] = relationship('Forms', back_populates='passports')
    passport_fields: Mapped[List['PassportFields']] = relationship('PassportFields', uselist=True,
                                                                   back_populates='passports')
    passport_information: Mapped[List['PassportInformation']] = relationship('PassportInformation', uselist=True,
                                                                             back_populates='passports')


class PervichCriteria(Base):
    __tablename__ = 'pervich_criteria'
    __table_args__ = (
        ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], ondelete='CASCADE',
                             name='fk_pervich_criteria_forms1'),
        Index('fk_pervich_criteria_forms1_idx', 'forms_id_forms')
    )

    id_pervich_criteria = mapped_column(Integer, primary_key=True)
    forms_id_forms = mapped_column(Integer, nullable=False)
    criterion_pervich_name = mapped_column(String(255))

    forms: Mapped['Forms'] = relationship('Forms', back_populates='pervich_criteria')
    project_pervich_evaluation: Mapped[List['ProjectPervichEvaluation']] = relationship('ProjectPervichEvaluation',
                                                                                        uselist=True,
                                                                                        back_populates='pervich_criteria')


class ResumeFiles(Base):
    __tablename__ = 'resume_files'
    __table_args__ = (
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE', onupdate='SET NULL',
                             name='fk_resume_files_users1'),
        Index('fk_resume_files_users1_idx', 'users_id')
    )

    id_resume_files = mapped_column(Integer, primary_key=True)
    title_file = mapped_column(String(255))
    url_file = mapped_column(String(255))
    users_id = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', back_populates='resume_files')


class Sessions(Base):
    __tablename__ = 'sessions'
    __table_args__ = (
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE', name='fk_sessions_users1'),
        Index('fk_sessions_users1_idx', 'users_id')
    )

    id_sessions = mapped_column(Integer, primary_key=True)
    users_id = mapped_column(Integer, nullable=False)
    session = mapped_column(String(256))
    date_creation = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    date_end = mapped_column(DateTime)

    users: Mapped['Users'] = relationship('Users', back_populates='sessions')


class Steps(Base):
    __tablename__ = 'steps'
    __table_args__ = (
        ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], ondelete='CASCADE', name='fk_steps_forms1'),
        Index('fk_steps_forms1_idx', 'forms_id_forms')
    )

    id_steps = mapped_column(Integer, primary_key=True)
    forms_id_forms = mapped_column(Integer, nullable=False)
    step = mapped_column(Integer)
    step_name = mapped_column(String(255))
    priority = mapped_column(Integer)

    forms: Mapped['Forms'] = relationship('Forms', back_populates='steps')


class Subscriptions(Base):
    __tablename__ = 'subscriptions'
    __table_args__ = (
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE', name='fk_subscriptions_users1'),
        Index('fk_subscriptions_users1_idx', 'users_id')
    )

    id_subscriptions = mapped_column(Integer, primary_key=True)
    users_id = mapped_column(Integer, nullable=False)
    url = mapped_column(String(600))
    subscription_name = mapped_column(String(200))

    users: Mapped['Users'] = relationship('Users', back_populates='subscriptions')


class Supports(Base):
    __tablename__ = 'supports'
    __table_args__ = (
        ForeignKeyConstraint(['institutes_id_institutes'], ['institutes.id_institutes'], ondelete='SET NULL',
                             name='fk_supports_institutes1'),
        ForeignKeyConstraint(['support_statuses_id_support_statuses'], ['support_statuses.id_support_statuses'],
                             name='fk_supports_support_statuses1'),
        Index('fk_supports_institutes1_idx', 'institutes_id_institutes'),
        Index('fk_supports_support_statuses1_idx', 'support_statuses_id_support_statuses'),
        Index('gov_number_UNIQUE', 'gov_number', unique=True),
        Index('id_supports_ctt_UNIQUE', 'id_supports_ctt', unique=True)
    )

    id_supports = mapped_column(Integer, primary_key=True)
    support_statuses_id_support_statuses = mapped_column(Integer, nullable=False)
    institutes_id_institutes = mapped_column(Integer)
    support_name = mapped_column(String(600))
    support_name_manual = mapped_column(String(600))
    description = mapped_column(Text)
    site = mapped_column(String(600))
    logo = mapped_column(String(600))
    no_finance = mapped_column(TINYINT(1))
    amount = mapped_column(Float)
    no_deadline = mapped_column(TINYINT(1))
    date_end = mapped_column(Date)
    date_creation = mapped_column(DateTime)
    logo_thumb = mapped_column(String(600))
    gov_number = mapped_column(Integer)
    id_supports_ctt = mapped_column(Integer)
    closed = mapped_column(TINYINT(1))

    institutes: Mapped[Optional['Institutes']] = relationship('Institutes', back_populates='supports')
    support_statuses: Mapped['SupportStatuses'] = relationship('SupportStatuses', back_populates='supports')
    support_regions: Mapped[List['SupportRegions']] = relationship('SupportRegions', uselist=True,
                                                                   back_populates='supports')
    support_support_directions: Mapped[List['SupportSupportDirections']] = relationship('SupportSupportDirections',
                                                                                        uselist=True,
                                                                                        back_populates='supports')
    support_support_forms: Mapped[List['SupportSupportForms']] = relationship('SupportSupportForms', uselist=True,
                                                                              back_populates='supports')
    support_support_members: Mapped[List['SupportSupportMembers']] = relationship('SupportSupportMembers', uselist=True,
                                                                                  back_populates='supports')
    support_support_reasons: Mapped[List['SupportSupportReasons']] = relationship('SupportSupportReasons', uselist=True,
                                                                                  back_populates='supports')


class TemplatePassports(Base):
    __tablename__ = 'template_passports'
    __table_args__ = (
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='SET NULL', name='fk_template_passports_users1'),
        Index('fk_template_passports_users1_idx', 'users_id')
    )

    id_template_passports = mapped_column(Integer, primary_key=True)
    passport_name = mapped_column(String(255))
    priority = mapped_column(Integer)
    closed = mapped_column(TINYINT(1))
    date_start = mapped_column(DateTime)
    date_end = mapped_column(DateTime)
    status = mapped_column(String(600))
    description = mapped_column(Text)
    date_creation = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    template_name = mapped_column(String(255))
    users_id = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', back_populates='template_passports')
    template_passport_fields: Mapped[List['TemplatePassportFields']] = relationship('TemplatePassportFields',
                                                                                    uselist=True,
                                                                                    back_populates='template_passports')


class Templates(Base):
    __tablename__ = 'templates'
    __table_args__ = (
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE', name='fk_templates_users1'),
        Index('fk_templates_users1_idx', 'users_id')
    )

    id_templates = mapped_column(Integer, primary_key=True)
    template_name = mapped_column(String(255))
    users_id = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', back_populates='templates')
    template_fields: Mapped[List['TemplateFields']] = relationship('TemplateFields', uselist=True,
                                                                   back_populates='templates')
    template_steps: Mapped[List['TemplateSteps']] = relationship('TemplateSteps', uselist=True,
                                                                 back_populates='templates')


class TrackingFormFields(Base):
    __tablename__ = 'tracking_form_fields'
    __table_args__ = (
        ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], ondelete='CASCADE', name='fk_form_fields_forms10'),
        ForeignKeyConstraint(['tracking_field_types_id_tracking_field_types'],
                             ['tracking_field_types.id_tracking_field_types'], ondelete='CASCADE',
                             name='fk_tracking_form_fields_tracking_field_types1'),
        Index('fk_form_fields_forms1_idx', 'forms_id_forms'),
        Index('fk_tracking_form_fields_tracking_field_types1_idx', 'tracking_field_types_id_tracking_field_types')
    )

    id_tracking_form_fields = mapped_column(Integer, primary_key=True)
    forms_id_forms = mapped_column(Integer, nullable=False)
    tracking_field_types_id_tracking_field_types = mapped_column(Integer, nullable=False)
    field_name = mapped_column(String(255))
    step = mapped_column(Integer)
    label = mapped_column(String(255))
    required = mapped_column(TINYINT)
    priority = mapped_column(Integer)
    visible = mapped_column(TINYINT)
    min_value = mapped_column(Integer, server_default=text("'0'"))
    max_value = mapped_column(Integer)
    default_value = mapped_column(String(800))
    for_user = mapped_column(TINYINT(1), server_default=text("'0'"))
    active_step = mapped_column(Integer)
    hint = mapped_column(String(600))

    forms: Mapped['Forms'] = relationship('Forms', back_populates='tracking_form_fields')
    tracking_field_types: Mapped['TrackingFieldTypes'] = relationship('TrackingFieldTypes',
                                                                      back_populates='tracking_form_fields')
    project_search: Mapped[List['ProjectSearch']] = relationship('ProjectSearch', uselist=True,
                                                                 back_populates='tracking_form_fields')
    sets_values_tracking_fields: Mapped[List['SetsValuesTrackingFields']] = relationship('SetsValuesTrackingFields',
                                                                                         uselist=True,
                                                                                         back_populates='tracking_form_fields')


class TrackingSteps(Base):
    __tablename__ = 'tracking_steps'
    __table_args__ = (
        ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], ondelete='CASCADE', name='fk_steps_forms10'),
        Index('fk_steps_forms1_idx', 'forms_id_forms')
    )

    id_tracking_steps = mapped_column(Integer, primary_key=True)
    forms_id_forms = mapped_column(Integer, nullable=False)
    step = mapped_column(Integer)
    step_name = mapped_column(String(255))
    session_time = mapped_column(Integer, server_default=text("'2'"))
    priority = mapped_column(Integer)
    closed = mapped_column(TINYINT(1))

    forms: Mapped['Forms'] = relationship('Forms', back_populates='tracking_steps')
    tracking_storage_field: Mapped[List['TrackingStorageField']] = relationship('TrackingStorageField', uselist=True,
                                                                                back_populates='tracking_steps')
    tracking_results: Mapped[List['TrackingResults']] = relationship('TrackingResults', uselist=True,
                                                                     back_populates='tracking_steps')
    tracking_call: Mapped[List['TrackingCall']] = relationship('TrackingCall', uselist=True,
                                                               back_populates='tracking_steps')


class TrackingTemplates(Base):
    __tablename__ = 'tracking_templates'
    __table_args__ = (
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='SET NULL', name='fk_tracking_templates_users1'),
        Index('fk_tracking_templates_users1_idx', 'users_id')
    )

    id_tracking_templates = mapped_column(Integer, primary_key=True)
    template_name = mapped_column(String(255))
    users_id = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', back_populates='tracking_templates')
    tracking_template_fields: Mapped[List['TrackingTemplateFields']] = relationship('TrackingTemplateFields',
                                                                                    uselist=True,
                                                                                    back_populates='tracking_templates')
    tracking_template_steps: Mapped[List['TrackingTemplateSteps']] = relationship('TrackingTemplateSteps', uselist=True,
                                                                                  back_populates='tracking_templates')


class UserEvents(Base):
    __tablename__ = 'user_events'
    __table_args__ = (
        ForeignKeyConstraint(['event_roles_id_event_roles'], ['event_roles.id_event_roles'], ondelete='CASCADE',
                             name='fk_user_events_event_roles1'),
        ForeignKeyConstraint(['events_id_forms'], ['forms.id_forms'], ondelete='CASCADE',
                             name='fk_user_events_events1'),
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE', onupdate='SET NULL',
                             name='fk_user_events_users1'),
        Index('fk_user_events_event_roles1_idx', 'event_roles_id_event_roles'),
        Index('fk_user_events_events1_idx', 'events_id_forms'),
        Index('fk_user_events_users1_idx', 'users_id')
    )

    id_user_events = mapped_column(Integer, primary_key=True)
    events_id_forms = mapped_column(Integer, nullable=False)
    event_roles_id_event_roles = mapped_column(Integer, nullable=False)
    users_id = mapped_column(Integer)

    event_roles: Mapped['EventRoles'] = relationship('EventRoles', back_populates='user_events')
    forms: Mapped['Forms'] = relationship('Forms', back_populates='user_events')
    users: Mapped[Optional['Users']] = relationship('Users', back_populates='user_events')


class UserFiles(Base):
    __tablename__ = 'user_files'
    __table_args__ = (
        ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], ondelete='SET NULL', onupdate='SET NULL',
                             name='fk_user_files_forms1'),
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE', name='fk_user_files_users1'),
        Index('fk_user_files_forms1_idx', 'forms_id_forms'),
        Index('fk_user_files_users1_idx', 'users_id')
    )

    id_user_files = mapped_column(Integer, primary_key=True)
    users_id = mapped_column(Integer, nullable=False)
    file_name = mapped_column(String(600))
    forms_id_forms = mapped_column(Integer)
    url_file = mapped_column(String(600))
    date_upload = mapped_column(DateTime)

    forms: Mapped[Optional['Forms']] = relationship('Forms', back_populates='user_files')
    users: Mapped['Users'] = relationship('Users', back_populates='user_files')


class UserMarkers(Base):
    __tablename__ = 'user_markers'
    __table_args__ = (
        ForeignKeyConstraint(['markers_id_markers'], ['markers.id_markers'], ondelete='CASCADE',
                             name='fk_user_markers_markers1'),
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='SET NULL', onupdate='SET NULL',
                             name='fk_user_markers_users1'),
        Index('fk_user_markers_markers1_idx', 'markers_id_markers'),
        Index('fk_user_markers_users1_idx', 'users_id')
    )

    id_user_markers = mapped_column(Integer, primary_key=True)
    markers_id_markers = mapped_column(Integer, nullable=False)
    users_id = mapped_column(Integer)

    markers: Mapped['Markers'] = relationship('Markers', back_populates='user_markers')
    users: Mapped[Optional['Users']] = relationship('Users', back_populates='user_markers')


class Utm(Base):
    __tablename__ = 'utm'
    __table_args__ = (
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE', name='fk_utm_users1'),
        Index('fk_utm_users1_idx', 'users_id')
    )

    id_utm = mapped_column(Integer, primary_key=True)
    users_id = mapped_column(Integer, nullable=False)
    utm_value = mapped_column(String(255))
    utm_name = mapped_column(String(255))

    users: Mapped['Users'] = relationship('Users', back_populates='utm')


class UtmEvents(Base):
    __tablename__ = 'utm_events'
    __table_args__ = (
        ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], ondelete='CASCADE', name='fk_utm_events_forms1'),
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE', name='fk_utm_events_users1'),
        Index('fk_utm_events_forms1_idx', 'forms_id_forms'),
        Index('fk_utm_events_users1_idx', 'users_id')
    )

    id_utm_events = mapped_column(Integer, primary_key=True)
    users_id = mapped_column(Integer, nullable=False)
    forms_id_forms = mapped_column(Integer, nullable=False)

    forms: Mapped['Forms'] = relationship('Forms', back_populates='utm_events')
    users: Mapped['Users'] = relationship('Users', back_populates='utm_events')


class UtmRole(Base):
    __tablename__ = 'utm_role'
    __table_args__ = (
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE', name='fk_utm_role_users1'),
        Index('fk_utm_role_users1_idx', 'users_id')
    )

    id_utm_role = mapped_column(Integer, primary_key=True)
    users_id = mapped_column(Integer, nullable=False)
    utm_role_value = mapped_column(String(255))

    users: Mapped['Users'] = relationship('Users', back_populates='utm_role')


class AllowForms(Base):
    __tablename__ = 'allow_forms'
    __table_args__ = (
        ForeignKeyConstraint(['form_fields_id_form_fields'], ['form_fields.id_form_fields'], ondelete='CASCADE',
                             name='fk_allow_forms_form_fields1'),
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE', name='fk_allow_forms_users1'),
        Index('fk_allow_forms_form_fields1_idx', 'form_fields_id_form_fields'),
        Index('fk_allow_forms_users1_idx', 'users_id')
    )

    id_allow_forms = mapped_column(Integer, primary_key=True)
    users_id = mapped_column(Integer, nullable=False)
    form_fields_id_form_fields = mapped_column(Integer, nullable=False)

    form_fields: Mapped['FormFields'] = relationship('FormFields', back_populates='allow_forms')
    users: Mapped['Users'] = relationship('Users', back_populates='allow_forms')


class ExpertiseCriteria(Base):
    __tablename__ = 'expertise_criteria'
    __table_args__ = (
        ForeignKeyConstraint(['expertise_criteria_types_id_expertise_criteria_types'],
                             ['expertise_criteria_types.id_expertise_criteria_types'],
                             name='fk_expertise_criteria_expertise_criteria_types1'),
        ForeignKeyConstraint(['expertises_id_expertises'], ['expertises.id_expertises'], ondelete='CASCADE',
                             name='fk_expertise_criteria_expertises1'),
        ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], name='fk_expertise_criteria_forms1'),
        Index('fk_expertise_criteria_expertise_criteria_types1_idx',
              'expertise_criteria_types_id_expertise_criteria_types'),
        Index('fk_expertise_criteria_expertises1_idx', 'expertises_id_expertises'),
        Index('fk_expertise_criteria_forms1_idx', 'forms_id_forms')
    )

    id_expertise_criteria = mapped_column(Integer, primary_key=True)
    expertises_id_expertises = mapped_column(Integer, nullable=False)
    expertise_criteria_types_id_expertise_criteria_types = mapped_column(Integer, nullable=False)
    field_name = mapped_column(String(255))
    label = mapped_column(String(255))
    required = mapped_column(TINYINT)
    priority = mapped_column(Integer)
    visible = mapped_column(TINYINT)
    min_value = mapped_column(Integer, server_default=text("'0'"))
    max_value = mapped_column(Integer)
    default_value = mapped_column(String(800))
    hint = mapped_column(String(600))
    forms_id_forms = mapped_column(Integer)

    expertise_criteria_types: Mapped['ExpertiseCriteriaTypes'] = relationship('ExpertiseCriteriaTypes',
                                                                              back_populates='expertise_criteria')
    expertises: Mapped['Expertises'] = relationship('Expertises', back_populates='expertise_criteria')
    forms: Mapped[Optional['Forms']] = relationship('Forms', back_populates='expertise_criteria')
    sets_values_criteria: Mapped[List['SetsValuesCriteria']] = relationship('SetsValuesCriteria', uselist=True,
                                                                            back_populates='expertise_criteria')


class FeedbackSetsValuesFields(Base):
    __tablename__ = 'feedback_sets_values_fields'
    __table_args__ = (
        ForeignKeyConstraint(['feedback_form_fields_id_feedback_form_fields'],
                             ['feedback_form_fields.id_feedback_form_fields'], ondelete='CASCADE',
                             name='fk_feedback_sets_values_fields_feedback_form_fields1'),
        Index('fk_feedback_sets_values_fields_feedback_form_fields1_idx',
              'feedback_form_fields_id_feedback_form_fields')
    )

    id_feedback_sets_values_fields = mapped_column(Integer, primary_key=True)
    feedback_form_fields_id_feedback_form_fields = mapped_column(Integer, nullable=False)
    value_field = mapped_column(String(255))

    feedback_form_fields: Mapped['FeedbackFormFields'] = relationship('FeedbackFormFields',
                                                                      back_populates='feedback_sets_values_fields')


class LearningTopics(Base):
    __tablename__ = 'learning_topics'
    __table_args__ = (
        ForeignKeyConstraint(['learning_modules_id_learning_modules'], ['learning_modules.id_learning_modules'],
                             ondelete='CASCADE', name='fk_learning_topics_learning_modules1'),
        Index('fk_learning_topics_learning_modules1_idx', 'learning_modules_id_learning_modules')
    )

    id_learning_topics = mapped_column(Integer, primary_key=True)
    learning_modules_id_learning_modules = mapped_column(Integer, nullable=False)
    priority = mapped_column(Integer)
    topic_name = mapped_column(String(1000))
    heading = mapped_column(String(1000))
    link_leader = mapped_column(String(255))
    only_leader = mapped_column(TINYINT(1))
    enable_leader = mapped_column(TINYINT(1))
    status_leader = mapped_column(String(500))
    date_update_leader = mapped_column(DateTime)

    learning_modules: Mapped['LearningModules'] = relationship('LearningModules', back_populates='learning_topics')
    learning_leader: Mapped[List['LearningLeader']] = relationship('LearningLeader', uselist=True,
                                                                   back_populates='learning_topics')
    learning_stat: Mapped[List['LearningStat']] = relationship('LearningStat', uselist=True,
                                                               back_populates='learning_topics')
    learning_task: Mapped[List['LearningTask']] = relationship('LearningTask', uselist=True,
                                                               back_populates='learning_topics')
    lecturers: Mapped[List['Lecturers']] = relationship('Lecturers', uselist=True, back_populates='learning_topics')


class PassportFields(Base):
    __tablename__ = 'passport_fields'
    __table_args__ = (
        ForeignKeyConstraint(['form_fields_id_form_fields'], ['form_fields.id_form_fields'], ondelete='SET NULL',
                             name='fk_passport_fields_form_fields1'),
        ForeignKeyConstraint(['passport_field_types_id_passport_field_types'],
                             ['passport_field_types.id_passport_field_types'], ondelete='CASCADE',
                             name='fk_passport_fields_passport_field_types1'),
        ForeignKeyConstraint(['passports_id_passports'], ['passports.id_passports'], ondelete='CASCADE',
                             name='fk_passport_fields_passports1'),
        Index('fk_passport_fields_form_fields1_idx', 'form_fields_id_form_fields'),
        Index('fk_passport_fields_passport_field_types1_idx', 'passport_field_types_id_passport_field_types'),
        Index('fk_passport_fields_passports1_idx', 'passports_id_passports')
    )

    id_passport_fields = mapped_column(Integer, primary_key=True)
    passport_field_types_id_passport_field_types = mapped_column(Integer, nullable=False)
    passports_id_passports = mapped_column(Integer, nullable=False)
    field_name = mapped_column(String(255))
    label = mapped_column(String(255))
    required = mapped_column(TINYINT)
    priority = mapped_column(Integer)
    hint = mapped_column(String(600))
    max_value = mapped_column(Integer)
    min_value = mapped_column(Integer)
    default_value = mapped_column(String(800))
    form_fields_id_form_fields = mapped_column(Integer)

    form_fields: Mapped[Optional['FormFields']] = relationship('FormFields', back_populates='passport_fields')
    passport_field_types: Mapped['PassportFieldTypes'] = relationship('PassportFieldTypes',
                                                                      back_populates='passport_fields')
    passports: Mapped['Passports'] = relationship('Passports', back_populates='passport_fields')
    passport_data: Mapped[List['PassportData']] = relationship('PassportData', uselist=True,
                                                               back_populates='passport_fields')
    sets_values_passport_fields: Mapped[List['SetsValuesPassportFields']] = relationship('SetsValuesPassportFields',
                                                                                         uselist=True,
                                                                                         back_populates='passport_fields')


class ProjectSearch(Base):
    __tablename__ = 'project_search'
    __table_args__ = (
        ForeignKeyConstraint(['expertises_id_expertises'], ['expertises.id_expertises'],
                             name='fk_project_search_expertises1'),
        ForeignKeyConstraint(['form_fields_id_form_fields'], ['form_fields.id_form_fields'],
                             name='fk_project_search_form_fields1'),
        ForeignKeyConstraint(['project_search_type_id_project_search_type'],
                             ['project_search_type.id_project_search_type'],
                             name='fk_project_search_project_search_type1'),
        ForeignKeyConstraint(['tracking_form_fields_id_tracking_form_fields'],
                             ['tracking_form_fields.id_tracking_form_fields'],
                             name='fk_project_search_tracking_form_fields1'),
        Index('fk_project_search_expertises1_idx', 'expertises_id_expertises'),
        Index('fk_project_search_form_fields1_idx', 'form_fields_id_form_fields'),
        Index('fk_project_search_project_search_type1_idx', 'project_search_type_id_project_search_type'),
        Index('fk_project_search_tracking_form_fields1_idx', 'tracking_form_fields_id_tracking_form_fields')
    )

    id_project_search = mapped_column(Integer, primary_key=True)
    project_search_type_id_project_search_type = mapped_column(Integer, nullable=False)
    form_fields_id_form_fields = mapped_column(Integer)
    expertises_id_expertises = mapped_column(Integer)
    tracking_form_fields_id_tracking_form_fields = mapped_column(Integer)

    expertises: Mapped[Optional['Expertises']] = relationship('Expertises', back_populates='project_search')
    form_fields: Mapped[Optional['FormFields']] = relationship('FormFields', back_populates='project_search')
    project_search_type: Mapped['ProjectSearchType'] = relationship('ProjectSearchType',
                                                                    back_populates='project_search')
    tracking_form_fields: Mapped[Optional['TrackingFormFields']] = relationship('TrackingFormFields',
                                                                                back_populates='project_search')


class Projects(Base):
    __tablename__ = 'projects'
    __table_args__ = (
        ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], ondelete='CASCADE', name='fk_projects_forms1'),
        ForeignKeyConstraint(['industry_directions_id_industry_directions'],
                             ['industry_directions.id_industry_directions'], ondelete='SET NULL',
                             name='fk_projects_industry_directions1'),
        ForeignKeyConstraint(['project_statuses_id_project_statuses'], ['project_statuses.id_project_statuses'],
                             name='fk_projects_project_statuses1'),
        Index('fk_projects_forms1_idx', 'forms_id_forms'),
        Index('fk_projects_industry_directions1_idx', 'industry_directions_id_industry_directions'),
        Index('fk_projects_project_statuses1_idx', 'project_statuses_id_project_statuses')
    )

    id_projects = mapped_column(Integer, primary_key=True)
    project_statuses_id_project_statuses = mapped_column(Integer, nullable=False)
    project_name = mapped_column(String(500))
    date_creation = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    forms_id_forms = mapped_column(Integer)
    industry_directions_id_industry_directions = mapped_column(Integer)
    feedback_status = mapped_column(TINYINT(1))
    id_form_projects = mapped_column(Integer)

    forms: Mapped[Optional['Forms']] = relationship('Forms', back_populates='projects')
    industry_directions: Mapped[Optional['IndustryDirections']] = relationship('IndustryDirections',
                                                                               back_populates='projects')
    project_statuses: Mapped['ProjectStatuses'] = relationship('ProjectStatuses', back_populates='projects')
    certificates: Mapped[List['Certificates']] = relationship('Certificates', uselist=True, back_populates='projects')
    feedback_project_data: Mapped[List['FeedbackProjectData']] = relationship('FeedbackProjectData', uselist=True,
                                                                              back_populates='projects')
    learning_leader: Mapped[List['LearningLeader']] = relationship('LearningLeader', uselist=True,
                                                                   back_populates='projects')
    learning_stat: Mapped[List['LearningStat']] = relationship('LearningStat', uselist=True, back_populates='projects')
    learning_task: Mapped[List['LearningTask']] = relationship('LearningTask', uselist=True, back_populates='projects')
    passport_data: Mapped[List['PassportData']] = relationship('PassportData', uselist=True, back_populates='projects')
    passport_information: Mapped[List['PassportInformation']] = relationship('PassportInformation', uselist=True,
                                                                             back_populates='projects')
    project_data: Mapped[List['ProjectData']] = relationship('ProjectData', uselist=True, back_populates='projects')
    project_moder_comments: Mapped[List['ProjectModerComments']] = relationship('ProjectModerComments', uselist=True,
                                                                                back_populates='projects')
    project_moder_evaluation: Mapped[List['ProjectModerEvaluation']] = relationship('ProjectModerEvaluation',
                                                                                    uselist=True,
                                                                                    back_populates='projects')
    tracking_information: Mapped[List['TrackingInformation']] = relationship('TrackingInformation', uselist=True,
                                                                             back_populates='projects')
    tracking_project_data: Mapped[List['TrackingProjectData']] = relationship('TrackingProjectData', uselist=True,
                                                                              back_populates='projects')
    tracking_results: Mapped[List['TrackingResults']] = relationship('TrackingResults', uselist=True,
                                                                     back_populates='projects')
    tracking_storage: Mapped[List['TrackingStorage']] = relationship('TrackingStorage', uselist=True,
                                                                     back_populates='projects')
    user_project: Mapped[List['UserProject']] = relationship('UserProject', uselist=True, back_populates='projects')
    expertise_information: Mapped[List['ExpertiseInformation']] = relationship('ExpertiseInformation', uselist=True,
                                                                               back_populates='projects')
    expertise_project_data: Mapped[List['ExpertiseProjectData']] = relationship('ExpertiseProjectData', uselist=True,
                                                                                back_populates='projects')
    project_pervich_evaluation: Mapped[List['ProjectPervichEvaluation']] = relationship('ProjectPervichEvaluation',
                                                                                        uselist=True,
                                                                                        back_populates='projects')


class SetsValuesFields(Base):
    __tablename__ = 'sets_values_fields'
    __table_args__ = (
        ForeignKeyConstraint(['form_fields_id_form_fields'], ['form_fields.id_form_fields'], ondelete='CASCADE',
                             name='fk_sets_values_fields_form_fields1'),
        Index('fk_sets_values_fields_form_fields1_idx', 'form_fields_id_form_fields')
    )

    id_sets_values_fields = mapped_column(Integer, primary_key=True)
    form_fields_id_form_fields = mapped_column(Integer, nullable=False)
    value_field = mapped_column(String(255))

    form_fields: Mapped['FormFields'] = relationship('FormFields', back_populates='sets_values_fields')


class SetsValuesTrackingFields(Base):
    __tablename__ = 'sets_values_tracking_fields'
    __table_args__ = (
        ForeignKeyConstraint(['tracking_form_fields_id_tracking_form_fields'],
                             ['tracking_form_fields.id_tracking_form_fields'], ondelete='CASCADE',
                             name='fk_sets_values_tracking_fields_tracking_form_fields1'),
        Index('fk_sets_values_tracking_fields_tracking_form_fields1_idx',
              'tracking_form_fields_id_tracking_form_fields')
    )

    id_sets_values_tracking_fields = mapped_column(Integer, primary_key=True)
    tracking_form_fields_id_tracking_form_fields = mapped_column(Integer, nullable=False)
    value_field = mapped_column(String(255))

    tracking_form_fields: Mapped['TrackingFormFields'] = relationship('TrackingFormFields',
                                                                      back_populates='sets_values_tracking_fields')


class SupportRegions(Base):
    __tablename__ = 'support_regions'
    __table_args__ = (
        ForeignKeyConstraint(['regions_id_regions'], ['regions.id_regions'], ondelete='CASCADE',
                             name='fk_support_region_regions1'),
        ForeignKeyConstraint(['supports_id_supports'], ['supports.id_supports'], ondelete='CASCADE',
                             name='fk_support_region_supports1'),
        Index('fk_support_region_regions1_idx', 'regions_id_regions'),
        Index('fk_support_region_supports1_idx', 'supports_id_supports')
    )

    id_support_region = mapped_column(Integer, primary_key=True)
    supports_id_supports = mapped_column(Integer, nullable=False)
    regions_id_regions = mapped_column(Integer, nullable=False)

    regions: Mapped['Regions'] = relationship('Regions', back_populates='support_regions')
    supports: Mapped['Supports'] = relationship('Supports', back_populates='support_regions')


class SupportSupportDirections(Base):
    __tablename__ = 'support_support_directions'
    __table_args__ = (
        ForeignKeyConstraint(['support_directions_id_support_directions'], ['support_directions.id_support_directions'],
                             ondelete='CASCADE', name='fk_support_support_directions_support_directions1'),
        ForeignKeyConstraint(['supports_id_supports'], ['supports.id_supports'], ondelete='CASCADE',
                             name='fk_support_support_directions_supports1'),
        Index('fk_support_support_directions_support_directions1_idx', 'support_directions_id_support_directions'),
        Index('fk_support_support_directions_supports1_idx', 'supports_id_supports')
    )

    id_support_support_directions = mapped_column(Integer, primary_key=True)
    supports_id_supports = mapped_column(Integer, nullable=False)
    support_directions_id_support_directions = mapped_column(Integer, nullable=False)

    support_directions: Mapped['SupportDirections'] = relationship('SupportDirections',
                                                                   back_populates='support_support_directions')
    supports: Mapped['Supports'] = relationship('Supports', back_populates='support_support_directions')


class SupportSupportForms(Base):
    __tablename__ = 'support_support_forms'
    __table_args__ = (
        ForeignKeyConstraint(['support_forms_id_support_forms'], ['support_forms.id_support_forms'], ondelete='CASCADE',
                             name='fk_supports_support_forms_support_forms1'),
        ForeignKeyConstraint(['supports_id_supports'], ['supports.id_supports'], ondelete='CASCADE',
                             name='fk_supports_support_forms_supports1'),
        Index('fk_supports_support_forms_support_forms1_idx', 'support_forms_id_support_forms'),
        Index('fk_supports_support_forms_supports1_idx', 'supports_id_supports')
    )

    id_support_support_forms = mapped_column(Integer, primary_key=True)
    supports_id_supports = mapped_column(Integer, nullable=False)
    support_forms_id_support_forms = mapped_column(Integer, nullable=False)

    support_forms: Mapped['SupportForms'] = relationship('SupportForms', back_populates='support_support_forms')
    supports: Mapped['Supports'] = relationship('Supports', back_populates='support_support_forms')


class SupportSupportMembers(Base):
    __tablename__ = 'support_support_members'
    __table_args__ = (
        ForeignKeyConstraint(['support_members_id_support_members'], ['support_members.id_support_members'],
                             ondelete='CASCADE', name='fk_support_support_members_support_members1'
                             ),
        ForeignKeyConstraint(['supports_id_supports'], ['supports.id_supports'], ondelete='CASCADE',
                             name='fk_support_support_members_supports1'),
        Index('fk_support_support_members_support_members1_idx', 'support_members_id_support_members'),
        Index('fk_support_support_members_supports1_idx', 'supports_id_supports')
    )

    id_support_support_members = mapped_column(Integer, primary_key=True)
    support_members_id_support_members = mapped_column(Integer, nullable=False)
    supports_id_supports = mapped_column(Integer, nullable=False)

    support_members: Mapped['SupportMembers'] = relationship('SupportMembers', back_populates='support_support_members')
    supports: Mapped['Supports'] = relationship('Supports', back_populates='support_support_members')


class SupportSupportReasons(Base):
    __tablename__ = 'support_support_reasons'
    __table_args__ = (
        ForeignKeyConstraint(['support_reasons_id_support_reasons'], ['support_reasons.id_support_reasons'],
                             ondelete='CASCADE', name='fk_support_support_reasons_support_reasons1'
                             ),
        ForeignKeyConstraint(['supports_id_supports'], ['supports.id_supports'], ondelete='CASCADE',
                             name='fk_support_support_reasons_supports1'),
        Index('fk_support_support_reasons_support_reasons1_idx', 'support_reasons_id_support_reasons'),
        Index('fk_support_support_reasons_supports1_idx', 'supports_id_supports')
    )

    id_support_support_reasons = mapped_column(Integer, primary_key=True)
    supports_id_supports = mapped_column(Integer, nullable=False)
    support_reasons_id_support_reasons = mapped_column(Integer, nullable=False)

    support_reasons: Mapped['SupportReasons'] = relationship('SupportReasons', back_populates='support_support_reasons')
    supports: Mapped['Supports'] = relationship('Supports', back_populates='support_support_reasons')


class TemplateExpertises(Base):
    __tablename__ = 'template_expertises'
    __table_args__ = (
        ForeignKeyConstraint(['expertise_templates_id_expertise_templates'],
                             ['expertise_templates.id_expertise_templates'],
                             name='fk_template_expertises_expertise_templates1'),
        Index('fk_template_expertises_expertise_templates1_idx', 'expertise_templates_id_expertise_templates')
    )

    id_template_expertises = mapped_column(Integer, primary_key=True)
    expertise_templates_id_expertise_templates = mapped_column(Integer, nullable=False)
    expertise_name = mapped_column(String(255))
    expertise_code = mapped_column(String(45))
    priority = mapped_column(Integer)

    expertise_templates: Mapped['ExpertiseTemplates'] = relationship('ExpertiseTemplates',
                                                                     back_populates='template_expertises')
    template_expertise_criteria: Mapped[List['TemplateExpertiseCriteria']] = relationship('TemplateExpertiseCriteria',
                                                                                          uselist=True,
                                                                                          back_populates='template_expertises')


class TemplateFeedbackFormFields(Base):
    __tablename__ = 'template_feedback_form_fields'
    __table_args__ = (
        ForeignKeyConstraint(['feedback_field_types_id_feedback_field_types'],
                             ['feedback_field_types.id_feedback_field_types'],
                             name='fk_feedback_form_fields_feedback_field_types10'),
        ForeignKeyConstraint(['learning_templates_id_learning_templates'], ['learning_templates.id_learning_templates'],
                             ondelete='CASCADE', name='fk_template_feedback_form_fields_learning_templates1'),
        Index('fk_feedback_form_fields_feedback_field_types1_idx', 'feedback_field_types_id_feedback_field_types'),
        Index('fk_template_feedback_form_fields_learning_templates1_idx', 'learning_templates_id_learning_templates')
    )

    id_template_feedback_form_fields = mapped_column(Integer, primary_key=True)
    feedback_field_types_id_feedback_field_types = mapped_column(Integer, nullable=False)
    learning_templates_id_learning_templates = mapped_column(Integer, nullable=False)
    field_name = mapped_column(String(255))
    label = mapped_column(String(255))
    required = mapped_column(TINYINT)
    priority = mapped_column(Integer)
    hint = mapped_column(String(600))
    max_value = mapped_column(Integer)
    min_value = mapped_column(Integer)
    default_value = mapped_column(String(800))

    feedback_field_types: Mapped['FeedbackFieldTypes'] = relationship('FeedbackFieldTypes',
                                                                      back_populates='template_feedback_form_fields')
    learning_templates: Mapped['LearningTemplates'] = relationship('LearningTemplates',
                                                                   back_populates='template_feedback_form_fields')
    feedback_sets_values_template_fields: Mapped[List['FeedbackSetsValuesTemplateFields']] = relationship(
        'FeedbackSetsValuesTemplateFields', uselist=True, back_populates='template_feedback_form_fields')


class TemplateFields(Base):
    __tablename__ = 'template_fields'
    __table_args__ = (
        ForeignKeyConstraint(['field_types_id_field_types'], ['field_types.id_field_types'],
                             name='fk_forms_field_types10'),
        ForeignKeyConstraint(['templates_id_templates'], ['templates.id_templates'],
                             name='fk_form_fields_copy1_templates1'),
        Index('fk_form_fields_copy1_templates1_idx', 'templates_id_templates'),
        Index('fk_forms_field_types1_idx', 'field_types_id_field_types')
    )

    id_template_fields = mapped_column(Integer, primary_key=True)
    field_types_id_field_types = mapped_column(Integer, nullable=False)
    templates_id_templates = mapped_column(Integer, nullable=False)
    field_name = mapped_column(String(255))
    step = mapped_column(Integer)
    label = mapped_column(String(255))
    required = mapped_column(TINYINT)
    priority = mapped_column(Integer)
    hint = mapped_column(String(600))
    max_value = mapped_column(Integer)
    min_value = mapped_column(Integer)

    field_types: Mapped['FieldTypes'] = relationship('FieldTypes', back_populates='template_fields')
    templates: Mapped['Templates'] = relationship('Templates', back_populates='template_fields')
    sets_values_template_fields: Mapped[List['SetsValuesTemplateFields']] = relationship('SetsValuesTemplateFields',
                                                                                         uselist=True,
                                                                                         back_populates='template_fields')


class TemplateLearningModules(Base):
    __tablename__ = 'template_learning_modules'
    __table_args__ = (
        ForeignKeyConstraint(['learning_templates_id_learning_templates'], ['learning_templates.id_learning_templates'],
                             ondelete='CASCADE', name='fk_template_learning_modules_learning_templates1'),
        Index('fk_template_learning_modules_learning_templates1_idx', 'learning_templates_id_learning_templates')
    )

    id_template_learning_modules = mapped_column(Integer, primary_key=True)
    learning_templates_id_learning_templates = mapped_column(Integer, nullable=False)
    date_start = mapped_column(Date)
    date_end = mapped_column(Date)
    closed = mapped_column(TINYINT(1))
    module_name = mapped_column(String(255))

    learning_templates: Mapped['LearningTemplates'] = relationship('LearningTemplates',
                                                                   back_populates='template_learning_modules')
    template_learning_topics: Mapped[List['TemplateLearningTopics']] = relationship('TemplateLearningTopics',
                                                                                    uselist=True,
                                                                                    back_populates='template_learning_modules')


class TemplatePassportFields(Base):
    __tablename__ = 'template_passport_fields'
    __table_args__ = (
        ForeignKeyConstraint(['passport_field_types_id_passport_field_types'],
                             ['passport_field_types.id_passport_field_types'], ondelete='CASCADE',
                             name='fk_passport_fields_passport_field_types10'),
        ForeignKeyConstraint(['template_passports_id_template_passports'], ['template_passports.id_template_passports'],
                             ondelete='CASCADE', name='fk_passport_fields_copy1_template_passports1'),
        Index('fk_passport_fields_copy1_template_passports1_idx', 'template_passports_id_template_passports'),
        Index('fk_passport_fields_passport_field_types1_idx', 'passport_field_types_id_passport_field_types')
    )

    id_template_passport_fields = mapped_column(Integer, primary_key=True)
    passport_field_types_id_passport_field_types = mapped_column(Integer, nullable=False)
    template_passports_id_template_passports = mapped_column(Integer, nullable=False)
    field_name = mapped_column(String(255))
    label = mapped_column(String(255))
    required = mapped_column(TINYINT)
    priority = mapped_column(Integer)
    hint = mapped_column(String(600))
    max_value = mapped_column(Integer)
    min_value = mapped_column(Integer)
    default_value = mapped_column(String(800))

    passport_field_types: Mapped['PassportFieldTypes'] = relationship('PassportFieldTypes',
                                                                      back_populates='template_passport_fields')
    template_passports: Mapped['TemplatePassports'] = relationship('TemplatePassports',
                                                                   back_populates='template_passport_fields')
    template_sets_values_passport_fields: Mapped[List['TemplateSetsValuesPassportFields']] = relationship(
        'TemplateSetsValuesPassportFields', uselist=True, back_populates='template_passport_fields')


class TemplateSteps(Base):
    __tablename__ = 'template_steps'
    __table_args__ = (
        ForeignKeyConstraint(['templates_id_templates'], ['templates.id_templates'], ondelete='CASCADE',
                             name='fk_steps_copy1_templates1'),
        Index('fk_steps_copy1_templates1_idx', 'templates_id_templates')
    )

    id_template_steps = mapped_column(Integer, primary_key=True)
    templates_id_templates = mapped_column(Integer, nullable=False)
    step = mapped_column(Integer)
    step_name = mapped_column(String(255))

    templates: Mapped['Templates'] = relationship('Templates', back_populates='template_steps')


class TrackingStorageField(Base):
    __tablename__ = 'tracking_storage_field'
    __table_args__ = (
        ForeignKeyConstraint(['tracking_steps_id_tracking_steps'], ['tracking_steps.id_tracking_steps'],
                             name='fk_tracking_storage_field_tracking_steps1'),
        Index('fk_tracking_storage_field_tracking_steps1_idx', 'tracking_steps_id_tracking_steps')
    )

    id_tracking_storage_field = mapped_column(Integer, primary_key=True)
    tracking_steps_id_tracking_steps = mapped_column(Integer, nullable=False)
    for_user = mapped_column(TINYINT(1), server_default=text("'0'"))
    visible = mapped_column(TINYINT(1))
    member_allowed = mapped_column(TINYINT(1), server_default=text("'0'"))
    tracker_allowed = mapped_column(TINYINT(1), server_default=text("'0'"))
    for_tracker = mapped_column(TINYINT(1), server_default=text("'0'"))

    tracking_steps: Mapped['TrackingSteps'] = relationship('TrackingSteps', back_populates='tracking_storage_field')
    tracking_storage: Mapped[List['TrackingStorage']] = relationship('TrackingStorage', uselist=True,
                                                                     back_populates='tracking_storage_field')


class TrackingTemplateFields(Base):
    __tablename__ = 'tracking_template_fields'
    __table_args__ = (
        ForeignKeyConstraint(['tracking_field_types_id_tracking_field_types'],
                             ['tracking_field_types.id_tracking_field_types'], ondelete='CASCADE',
                             name='fk_tracking_template_fields_tracking_field_types1'),
        ForeignKeyConstraint(['tracking_templates_id_tracking_templates'], ['tracking_templates.id_tracking_templates'],
                             ondelete='CASCADE', name='fk_tracking_template_fields_tracking_templates1'),
        Index('fk_tracking_template_fields_tracking_field_types1_idx', 'tracking_field_types_id_tracking_field_types'),
        Index('fk_tracking_template_fields_tracking_templates1_idx', 'tracking_templates_id_tracking_templates')
    )

    id_tracking_template_fields = mapped_column(Integer, primary_key=True)
    tracking_field_types_id_tracking_field_types = mapped_column(Integer, nullable=False)
    tracking_templates_id_tracking_templates = mapped_column(Integer, nullable=False)
    field_name = mapped_column(String(255))
    step = mapped_column(Integer)
    label = mapped_column(String(255))
    required = mapped_column(TINYINT)
    priority = mapped_column(Integer)
    visible = mapped_column(TINYINT)
    min_value = mapped_column(Integer)
    max_value = mapped_column(Integer)
    default_value = mapped_column(String(800))
    hint = mapped_column(String(600))
    for_user = mapped_column(TINYINT(1))

    tracking_field_types: Mapped['TrackingFieldTypes'] = relationship('TrackingFieldTypes',
                                                                      back_populates='tracking_template_fields')
    tracking_templates: Mapped['TrackingTemplates'] = relationship('TrackingTemplates',
                                                                   back_populates='tracking_template_fields')
    sets_values_tracking_template_fields: Mapped[List['SetsValuesTrackingTemplateFields']] = relationship(
        'SetsValuesTrackingTemplateFields', uselist=True, back_populates='tracking_template_fields')


class TrackingTemplateSteps(Base):
    __tablename__ = 'tracking_template_steps'
    __table_args__ = (
        ForeignKeyConstraint(['tracking_templates_id_tracking_templates'], ['tracking_templates.id_tracking_templates'],
                             ondelete='CASCADE', name='fk_tracking_template_steps_tracking_templates1'),
        Index('fk_tracking_template_steps_tracking_templates1_idx', 'tracking_templates_id_tracking_templates')
    )

    id_tracking_template_steps = mapped_column(Integer, primary_key=True)
    tracking_templates_id_tracking_templates = mapped_column(Integer, nullable=False)
    step = mapped_column(Integer)
    step_name = mapped_column(String(255))
    session_time = mapped_column(Integer)

    tracking_templates: Mapped['TrackingTemplates'] = relationship('TrackingTemplates',
                                                                   back_populates='tracking_template_steps')


class Certificates(Base):
    __tablename__ = 'certificates'
    __table_args__ = (
        ForeignKeyConstraint(['certificate_type_id_certificate_type'], ['certificate_type.id_certificate_type'],
                             ondelete='CASCADE', name='fk_certificates_certificate_type1'),
        ForeignKeyConstraint(['forms_id_forms'], ['forms.id_forms'], ondelete='CASCADE', name='fk_certificates_forms1'),
        ForeignKeyConstraint(['projects_id_projects'], ['projects.id_projects'], ondelete='SET NULL',
                             name='fk_certificates_projects1'),
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE', name='fk_certificates_users1'),
        Index('fk_certificates_certificate_type1_idx', 'certificate_type_id_certificate_type'),
        Index('fk_certificates_forms1_idx', 'forms_id_forms'),
        Index('fk_certificates_projects1_idx', 'projects_id_projects'),
        Index('fk_certificates_users1_idx', 'users_id')
    )

    id_certificates = mapped_column(Integer, primary_key=True)
    certificate_type_id_certificate_type = mapped_column(Integer, nullable=False)
    users_id = mapped_column(Integer, nullable=False)
    url_file = mapped_column(String(600))
    projects_id_projects = mapped_column(Integer)
    forms_id_forms = mapped_column(Integer)

    certificate_type: Mapped['CertificateType'] = relationship('CertificateType', back_populates='certificates')
    forms: Mapped[Optional['Forms']] = relationship('Forms', back_populates='certificates')
    projects: Mapped[Optional['Projects']] = relationship('Projects', back_populates='certificates')
    users: Mapped['Users'] = relationship('Users', back_populates='certificates')


class FeedbackProjectData(Base):
    __tablename__ = 'feedback_project_data'
    __table_args__ = (
        ForeignKeyConstraint(['projects_id_projects'], ['projects.id_projects'], ondelete='CASCADE',
                             name='fk_feedback_project_data_projects1'),
        Index('fk_feedback_project_data_projects1_idx', 'projects_id_projects')
    )

    id_feedback_project_data = mapped_column(Integer, primary_key=True)
    projects_id_projects = mapped_column(Integer, nullable=False)
    field_name = mapped_column(String(255))
    data = mapped_column(String(1000))
    label = mapped_column(String(255))
    file = mapped_column(TINYINT(1))

    projects: Mapped['Projects'] = relationship('Projects', back_populates='feedback_project_data')


class FeedbackSetsValuesTemplateFields(Base):
    __tablename__ = 'feedback_sets_values_template_fields'
    __table_args__ = (
        ForeignKeyConstraint(['template_feedback_form_fields_id_template_feedback_form_fields'],
                             ['template_feedback_form_fields.id_template_feedback_form_fields'], ondelete='CASCADE',
                             name='fk_feedback_sets_values_template_fields_template_feedback_for1'),
        Index('fk_feedback_sets_values_template_fields_template_feedback_f_idx',
              'template_feedback_form_fields_id_template_feedback_form_fields')
    )

    id_feedback_sets_values_template_fields = mapped_column(Integer, primary_key=True)
    template_feedback_form_fields_id_template_feedback_form_fields = mapped_column(Integer, nullable=False)
    value_field = mapped_column(String(255))

    template_feedback_form_fields: Mapped['TemplateFeedbackFormFields'] = relationship('TemplateFeedbackFormFields',
                                                                                       back_populates='feedback_sets_values_template_fields')


class LearningLeader(Base):
    __tablename__ = 'learning_leader'
    __table_args__ = (
        ForeignKeyConstraint(['learning_topics_id_learning_topics'], ['learning_topics.id_learning_topics'],
                             name='fk_learning_leader_learning_topics1'),
        ForeignKeyConstraint(['projects_id_projects'], ['projects.id_projects'],
                             name='fk_learning_leader_projects1'),
        ForeignKeyConstraint(['users_id'], ['users.id'], name='fk_learning_leader_users1'),
        Index('fk_learning_leader_learning_topics1_idx', 'learning_topics_id_learning_topics'),
        Index('fk_learning_leader_projects1_idx', 'projects_id_projects'),
        Index('fk_learning_leader_users1_idx', 'users_id')
    )
    id_learning_leader = mapped_column(Integer, primary_key=True)
    users_id = mapped_column(Integer, nullable=False)
    learning_topics_id_learning_topics = mapped_column(Integer, nullable=False)
    projects_id_projects = mapped_column(Integer, nullable=False)
    full_response = mapped_column(Text)
    status = mapped_column(String(255))
    date_creation = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    message = mapped_column(Text)
    learning_topics: Mapped['LearningTopics'] = relationship('LearningTopics', back_populates='learning_leader')
    projects: Mapped['Projects'] = relationship('Projects', back_populates='learning_leader')
    users: Mapped['Users'] = relationship('Users', back_populates='learning_leader')


class LearningStat(Base):
    __tablename__ = 'learning_stat'
    __table_args__ = (
        ForeignKeyConstraint(['learning_topics_id_learning_topics'], ['learning_topics.id_learning_topics'],
                             ondelete='CASCADE', name='fk_learning_stat_learning_topics1'),
        ForeignKeyConstraint(['projects_id_projects'], ['projects.id_projects'], ondelete='CASCADE',
                             name='fk_learning_stat_projects1'),
        Index('fk_learning_stat_learning_topics1_idx', 'learning_topics_id_learning_topics'),
        Index('fk_learning_stat_projects1_idx', 'projects_id_projects')
    )

    id_learning_stat = mapped_column(Integer, primary_key=True)
    projects_id_projects = mapped_column(Integer, nullable=False)
    learning_topics_id_learning_topics = mapped_column(Integer, nullable=False)
    content = mapped_column(TINYINT(1))
    task = mapped_column(TINYINT(1))
    video = mapped_column(TINYINT(1))
    key = mapped_column(String(45))
    webinar = mapped_column(TINYINT(1))

    learning_topics: Mapped['LearningTopics'] = relationship('LearningTopics', back_populates='learning_stat')
    projects: Mapped['Projects'] = relationship('Projects', back_populates='learning_stat')


class LearningTask(Base):
    __tablename__ = 'learning_task'
    __table_args__ = (
        ForeignKeyConstraint(['learning_topics_id_learning_topics'], ['learning_topics.id_learning_topics'],
                             ondelete='CASCADE', name='fk_learning_task_learning_topics1'),
        ForeignKeyConstraint(['projects_id_projects'], ['projects.id_projects'], ondelete='CASCADE',
                             name='fk_learning_task_projects1'),
        Index('fk_learning_task_learning_topics1_idx', 'learning_topics_id_learning_topics'),
        Index('fk_learning_task_projects1_idx', 'projects_id_projects')
    )

    id_learning_task = mapped_column(Integer, primary_key=True)
    projects_id_projects = mapped_column(Integer, nullable=False)
    learning_topics_id_learning_topics = mapped_column(Integer, nullable=False)
    task = mapped_column(Text)
    file = mapped_column(String(600))
    tutor_estimation = mapped_column(Integer)
    tutor_comment = mapped_column(Text)
    tutor_file = mapped_column(String(255))
    submitted = mapped_column(TINYINT(1))

    learning_topics: Mapped['LearningTopics'] = relationship('LearningTopics', back_populates='learning_task')
    projects: Mapped['Projects'] = relationship('Projects', back_populates='learning_task')


class Lecturers(Base):
    __tablename__ = 'lecturers'
    __table_args__ = (
        ForeignKeyConstraint(['learning_topics_id_learning_topics'], ['learning_topics.id_learning_topics'],
                             ondelete='CASCADE', name='fk_lecturers_learning_topics1'),
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE', name='fk_lecturers_users1'),
        Index('fk_lecturers_learning_topics1_idx', 'learning_topics_id_learning_topics'),
        Index('fk_lecturers_users1_idx', 'users_id')
    )

    id_lecturers = mapped_column(Integer, primary_key=True)
    learning_topics_id_learning_topics = mapped_column(Integer, nullable=False)
    users_id = mapped_column(Integer, nullable=False)
    about = mapped_column(Text)

    learning_topics: Mapped['LearningTopics'] = relationship('LearningTopics', back_populates='lecturers')
    users: Mapped['Users'] = relationship('Users', back_populates='lecturers')


class PassportData(Base):
    __tablename__ = 'passport_data'
    __table_args__ = (
        ForeignKeyConstraint(['passport_fields_id_passport_fields'], ['passport_fields.id_passport_fields'],
                             name='fk_passport_data_passport_fields1'),
        ForeignKeyConstraint(['projects_id_projects'], ['projects.id_projects'], name='fk_passport_data_projects1'),
        Index('fk_passport_data_passport_fields1_idx', 'passport_fields_id_passport_fields'),
        Index('fk_passport_data_projects1_idx', 'projects_id_projects')
    )

    id_passport_data = mapped_column(Integer, primary_key=True)
    passport_fields_id_passport_fields = mapped_column(Integer, nullable=False)
    projects_id_projects = mapped_column(Integer, nullable=False)
    data = mapped_column(Text)
    file = mapped_column(TINYINT(1))

    passport_fields: Mapped['PassportFields'] = relationship('PassportFields', back_populates='passport_data')
    projects: Mapped['Projects'] = relationship('Projects', back_populates='passport_data')


class PassportInformation(Base):
    __tablename__ = 'passport_information'
    __table_args__ = (
        ForeignKeyConstraint(['passport_statuses_id_passport_statuses'], ['passport_statuses.id_passport_statuses'],
                             name='fk_passport_information_passport_statuses1'),
        ForeignKeyConstraint(['passports_id_passports'], ['passports.id_passports'],
                             name='fk_passport_information_passports1'),
        ForeignKeyConstraint(['projects_id_projects'], ['projects.id_projects'],
                             name='fk_passport_information_projects1'),
        Index('fk_passport_information_passport_statuses1_idx', 'passport_statuses_id_passport_statuses'),
        Index('fk_passport_information_passports1_idx', 'passports_id_passports'),
        Index('fk_passport_information_projects1_idx', 'projects_id_projects')
    )

    id_passport_information = mapped_column(Integer, primary_key=True)
    passports_id_passports = mapped_column(Integer, nullable=False)
    projects_id_projects = mapped_column(Integer, nullable=False)
    passport_statuses_id_passport_statuses = mapped_column(Integer, nullable=False)
    date_last = mapped_column(DateTime)
    comment = mapped_column(Text)

    passport_statuses: Mapped['PassportStatuses'] = relationship('PassportStatuses',
                                                                 back_populates='passport_information')
    passports: Mapped['Passports'] = relationship('Passports', back_populates='passport_information')
    projects: Mapped['Projects'] = relationship('Projects', back_populates='passport_information')


class ProjectData(Base):
    __tablename__ = 'project_data'
    __table_args__ = (
        ForeignKeyConstraint(['projects_id_projects'], ['projects.id_projects'], ondelete='CASCADE',
                             name='fk_project_data_projects1'),
        Index('fk_project_data_projects1_idx', 'projects_id_projects'),

        ForeignKeyConstraint(['form_fields_id_form_fields'], ['form_fields.id_form_fields'], ondelete='CASCADE',
                             name='fk_form_fields_id_form_fields1'),
        Index('fk_form_fields_id_form_fields1_idx', 'form_fields_id_form_fields')
    )

    id_project_data = mapped_column(Integer, primary_key=True)
    field_name = mapped_column(String(255), nullable=False)
    projects_id_projects = mapped_column(Integer, nullable=False)
    data = mapped_column(String(1000))
    visible = mapped_column(TINYINT)
    label = mapped_column(String(255))
    file = mapped_column(TINYINT)
    step = mapped_column(Integer)
    form_fields_id_form_fields = mapped_column(Integer, nullable=False)

    projects: Mapped['Projects'] = relationship('Projects', back_populates='project_data')
    form_fields: Mapped['FormFields'] = relationship('FormFields', back_populates='project_data')


class ProjectModerComments(Base):
    __tablename__ = 'project_moder_comments'
    __table_args__ = (
        ForeignKeyConstraint(['projects_id_projects'], ['projects.id_projects'], name='fk_moder_comments_projects1'),
        Index('fk_moder_comments_projects1_idx', 'projects_id_projects')
    )

    id_project_moder_comments = mapped_column(Integer, primary_key=True)
    comment = mapped_column(Text)
    projects_id_projects = mapped_column(Integer)

    projects: Mapped[Optional['Projects']] = relationship('Projects', back_populates='project_moder_comments')


class ProjectModerEvaluation(Base):
    __tablename__ = 'project_moder_evaluation'
    __table_args__ = (
        ForeignKeyConstraint(['moder_criteria_id_moder_criteria'], ['moder_criteria.id_moder_criteria'],
                             ondelete='CASCADE', name='fk_project_moder_evaluation_moder_criteria1'),
        ForeignKeyConstraint(['projects_id_projects'], ['projects.id_projects'], ondelete='CASCADE',
                             name='fk_project_moder_evaluation_projects10'),
        Index('fk_project_moder_evaluation_moder_criteria1_idx', 'moder_criteria_id_moder_criteria'),
        Index('fk_project_moder_evaluation_projects1_idx', 'projects_id_projects')
    )

    id_project_moder_evaluation = mapped_column(Integer, primary_key=True)
    projects_id_projects = mapped_column(Integer, nullable=False)
    moder_criteria_id_moder_criteria = mapped_column(Integer, nullable=False)
    comment = mapped_column(Text)

    moder_criteria: Mapped['ModerCriteria'] = relationship('ModerCriteria', back_populates='project_moder_evaluation')
    projects: Mapped['Projects'] = relationship('Projects', back_populates='project_moder_evaluation')


class SetsValuesCriteria(Base):
    __tablename__ = 'sets_values_criteria'
    __table_args__ = (
        ForeignKeyConstraint(['expertise_criteria_id_expertise_criteria'], ['expertise_criteria.id_expertise_criteria'],
                             ondelete='CASCADE', name='fk_sets_values_template_fields_copy1_expertise_criteria1'),
        Index('fk_sets_values_template_fields_copy1_expertise_criteria1_idx',
              'expertise_criteria_id_expertise_criteria')
    )

    id_sets_values_criteria = mapped_column(Integer, primary_key=True)
    expertise_criteria_id_expertise_criteria = mapped_column(Integer, nullable=False)
    value_field = mapped_column(String(255))

    expertise_criteria: Mapped['ExpertiseCriteria'] = relationship('ExpertiseCriteria',
                                                                   back_populates='sets_values_criteria')


class SetsValuesPassportFields(Base):
    __tablename__ = 'sets_values_passport_fields'
    __table_args__ = (
        ForeignKeyConstraint(['passport_fields_id_passport_fields'], ['passport_fields.id_passport_fields'],
                             ondelete='CASCADE', name='fk_sets_values_passport_fields_passport_fields1'),
        Index('fk_sets_values_passport_fields_passport_fields1_idx', 'passport_fields_id_passport_fields')
    )

    id_sets_values_passport_fields = mapped_column(Integer, primary_key=True)
    passport_fields_id_passport_fields = mapped_column(Integer, nullable=False)
    value_field = mapped_column(String(255))

    passport_fields: Mapped['PassportFields'] = relationship('PassportFields',
                                                             back_populates='sets_values_passport_fields')


class SetsValuesTemplateFields(Base):
    __tablename__ = 'sets_values_template_fields'
    __table_args__ = (
        ForeignKeyConstraint(['template_fields_id_template_fields'], ['template_fields.id_template_fields'],
                             ondelete='CASCADE', name='fk_sets_values_fields_copy1_template_fields1'),
        Index('fk_sets_values_fields_copy1_template_fields1_idx', 'template_fields_id_template_fields')
    )

    id_sets_values_template_fields = mapped_column(Integer, primary_key=True)
    template_fields_id_template_fields = mapped_column(Integer, nullable=False)
    value_field = mapped_column(String(255))

    template_fields: Mapped['TemplateFields'] = relationship('TemplateFields',
                                                             back_populates='sets_values_template_fields')


class SetsValuesTrackingTemplateFields(Base):
    __tablename__ = 'sets_values_tracking_template_fields'
    __table_args__ = (
        ForeignKeyConstraint(['tracking_template_fields_id_tracking_template_fields'],
                             ['tracking_template_fields.id_tracking_template_fields'], ondelete='CASCADE',
                             name='fk_sets_values_template_fields_copy1_tracking_template_fields1'),
        Index('fk_sets_values_template_fields_copy1_tracking_template_fiel_idx',
              'tracking_template_fields_id_tracking_template_fields')
    )

    id_sets_values_tracking_template_fields = mapped_column(Integer, primary_key=True)
    tracking_template_fields_id_tracking_template_fields = mapped_column(Integer, nullable=False)
    value_field = mapped_column(String(255))

    tracking_template_fields: Mapped['TrackingTemplateFields'] = relationship('TrackingTemplateFields',
                                                                              back_populates='sets_values_tracking_template_fields')


class TemplateExpertiseCriteria(Base):
    __tablename__ = 'template_expertise_criteria'
    __table_args__ = (
        ForeignKeyConstraint(['expertise_criteria_types_id_expertise_criteria_types'],
                             ['expertise_criteria_types.id_expertise_criteria_types'],
                             name='fk_expertise_criteria_expertise_criteria_types10'),
        ForeignKeyConstraint(['expertise_templates_id_expertise_templates'],
                             ['expertise_templates.id_expertise_templates'],
                             name='fk_expertise_criteria_templates_expertise_templates1'),
        ForeignKeyConstraint(['template_expertises_id_template_expertises'],
                             ['template_expertises.id_template_expertises'],
                             name='fk_expertise_criteria_templates_template_expertises1'),
        Index('fk_expertise_criteria_expertise_criteria_types1_idx',
              'expertise_criteria_types_id_expertise_criteria_types'),
        Index('fk_expertise_criteria_templates_expertise_templates1_idx', 'expertise_templates_id_expertise_templates'),
        Index('fk_expertise_criteria_templates_template_expertises1_idx', 'template_expertises_id_template_expertises')
    )

    id_template_expertise_criteria = mapped_column(Integer, primary_key=True)
    expertise_criteria_types_id_expertise_criteria_types = mapped_column(Integer, nullable=False)
    expertise_templates_id_expertise_templates = mapped_column(Integer, nullable=False)
    template_expertises_id_template_expertises = mapped_column(Integer, nullable=False)
    field_name = mapped_column(String(255))
    label = mapped_column(String(255))
    required = mapped_column(TINYINT)
    priority = mapped_column(Integer)
    visible = mapped_column(TINYINT)
    min_value = mapped_column(Integer, server_default=text("'0'"))
    max_value = mapped_column(Integer)
    default_value = mapped_column(String(800))
    hint = mapped_column(String(600))

    expertise_criteria_types: Mapped['ExpertiseCriteriaTypes'] = relationship('ExpertiseCriteriaTypes',
                                                                              back_populates='template_expertise_criteria')
    expertise_templates: Mapped['ExpertiseTemplates'] = relationship('ExpertiseTemplates',
                                                                     back_populates='template_expertise_criteria')
    template_expertises: Mapped['TemplateExpertises'] = relationship('TemplateExpertises',
                                                                     back_populates='template_expertise_criteria')
    sets_values_template_criteria: Mapped[List['SetsValuesTemplateCriteria']] = relationship(
        'SetsValuesTemplateCriteria', uselist=True, back_populates='template_expertise_criteria')


class TemplateLearningTopics(Base):
    __tablename__ = 'template_learning_topics'
    __table_args__ = (
        ForeignKeyConstraint(['template_learning_modules_id_template_learning_modules'],
                             ['template_learning_modules.id_template_learning_modules'], ondelete='CASCADE',
                             name='fk_template_learning_topics_template_learning_modules1'),
        Index('fk_template_learning_topics_template_learning_modules1_idx',
              'template_learning_modules_id_template_learning_modules')
    )

    id_template_learning_topics = mapped_column(Integer, primary_key=True)
    template_learning_modules_id_template_learning_modules = mapped_column(Integer, nullable=False)
    priority = mapped_column(Integer)
    topic_name = mapped_column(String(255))
    heading = mapped_column(String(255))

    template_learning_modules: Mapped['TemplateLearningModules'] = relationship('TemplateLearningModules',
                                                                                back_populates='template_learning_topics')


class TemplateSetsValuesPassportFields(Base):
    __tablename__ = 'template_sets_values_passport_fields'
    __table_args__ = (
        ForeignKeyConstraint(['template_passport_fields_id_template_passport_fields'],
                             ['template_passport_fields.id_template_passport_fields'], ondelete='CASCADE',
                             name='fk_template_sets_values_passport_fields_template_passport_fie1'),
        Index('fk_template_sets_values_passport_fields_template_passport_f_idx',
              'template_passport_fields_id_template_passport_fields')
    )

    id_template_sets_values_passport_fields = mapped_column(Integer, primary_key=True)
    template_passport_fields_id_template_passport_fields = mapped_column(Integer, nullable=False)
    value_field = mapped_column(String(255))

    template_passport_fields: Mapped['TemplatePassportFields'] = relationship('TemplatePassportFields',
                                                                              back_populates='template_sets_values_passport_fields')


class TopicInfo(LearningTopics):
    __tablename__ = 'topic_info'
    __table_args__ = (
        ForeignKeyConstraint(['learning_topics_id_learning_topics'], ['learning_topics.id_learning_topics'],
                             ondelete='CASCADE', name='fk_topic_info_learning_topics1'),
        Index('fk_topic_info_learning_topics1_idx', 'learning_topics_id_learning_topics')
    )

    learning_topics_id_learning_topics = mapped_column(Integer, primary_key=True)
    description = mapped_column(Text)
    webinar = mapped_column(String(600))
    webinar_date = mapped_column(DateTime)
    webinar_date_end = mapped_column(DateTime)
    video1 = mapped_column(String(600))
    video2 = mapped_column(String(600))
    video3 = mapped_column(String(600))
    video4 = mapped_column(String(600))
    video5 = mapped_column(String(600))
    content = mapped_column(Text)
    content_file1 = mapped_column(String(600))
    content_file2 = mapped_column(String(600))
    content_file3 = mapped_column(String(600))
    content_file4 = mapped_column(String(600))
    content_file5 = mapped_column(String(600))
    task = mapped_column(Text)
    task_file1 = mapped_column(String(600))
    task_file2 = mapped_column(String(600))
    task_file3 = mapped_column(String(600))
    task_file4 = mapped_column(String(600))
    task_file5 = mapped_column(String(600))
    filled = mapped_column(TINYINT(1))
    content_link1 = mapped_column(String(1000))
    content_link2 = mapped_column(String(1000))
    content_link3 = mapped_column(String(1000))
    content_link4 = mapped_column(String(1000))
    content_link5 = mapped_column(String(1000))
    frame1 = mapped_column(TINYINT(1))
    frame2 = mapped_column(TINYINT(1))
    frame3 = mapped_column(TINYINT(1))
    frame4 = mapped_column(TINYINT(1))
    frame5 = mapped_column(TINYINT(1))
    task_date_start = mapped_column(DateTime)
    task_date_end = mapped_column(DateTime)


class TrackingInformation(Base):
    __tablename__ = 'tracking_information'
    __table_args__ = (
        ForeignKeyConstraint(['projects_id_projects'], ['projects.id_projects'], ondelete='CASCADE',
                             name='fk_tracking_information_projects1'),
        ForeignKeyConstraint(['tracking_statuses_id_tracking_statuses'], ['tracking_statuses.id_tracking_statuses'],
                             ondelete='CASCADE', name='fk_tracking_information_tracking_statuses1'),
        Index('fk_tracking_information_projects1_idx', 'projects_id_projects'),
        Index('fk_tracking_information_tracking_statuses1_idx', 'tracking_statuses_id_tracking_statuses')
    )

    id_tracking_information = mapped_column(Integer, primary_key=True)
    projects_id_projects = mapped_column(Integer, nullable=False)
    report = mapped_column(String(255))
    tracking_statuses_id_tracking_statuses = mapped_column(Integer)
    active_step = mapped_column(Integer)
    chat = mapped_column(String(600))
    calendar = mapped_column(String(600))
    traction_card = mapped_column(String(600))

    projects: Mapped['Projects'] = relationship('Projects', back_populates='tracking_information')
    tracking_statuses: Mapped[Optional['TrackingStatuses']] = relationship('TrackingStatuses',
                                                                           back_populates='tracking_information')
    tracking_call: Mapped[List['TrackingCall']] = relationship('TrackingCall', uselist=True,
                                                               back_populates='tracking_information')


class TrackingProjectData(Base):
    __tablename__ = 'tracking_project_data'
    __table_args__ = (
        ForeignKeyConstraint(['projects_id_projects'], ['projects.id_projects'], ondelete='CASCADE',
                             name='fk_project_data_projects10'),
        Index('fk_project_data_projects1_idx', 'projects_id_projects')
    )

    id_tracking_project_data = mapped_column(Integer, primary_key=True)
    field_name = mapped_column(String(255), nullable=False)
    projects_id_projects = mapped_column(Integer, nullable=False)
    data = mapped_column(String(1000))
    visible = mapped_column(TINYINT)
    label = mapped_column(String(255))
    file = mapped_column(TINYINT)
    step = mapped_column(Integer)

    projects: Mapped['Projects'] = relationship('Projects', back_populates='tracking_project_data')


class TrackingResults(Base):
    __tablename__ = 'tracking_results'
    __table_args__ = (
        ForeignKeyConstraint(['projects_id_projects'], ['projects.id_projects'], ondelete='CASCADE',
                             name='fk_tracking_results_projects1'),
        ForeignKeyConstraint(['tracking_steps_id_tracking_steps'], ['tracking_steps.id_tracking_steps'],
                             ondelete='CASCADE', name='fk_tracking_results_tracking_steps1'),
        Index('fk_tracking_results_projects1_idx', 'projects_id_projects'),
        Index('fk_tracking_results_tracking_steps1_idx', 'tracking_steps_id_tracking_steps')
    )

    id_tracking_results = mapped_column(Integer, primary_key=True)
    projects_id_projects = mapped_column(Integer, nullable=False)
    tracking_steps_id_tracking_steps = mapped_column(Integer, nullable=False)
    comment = mapped_column(Text)
    file1 = mapped_column(String(600))
    file2 = mapped_column(String(600))
    file3 = mapped_column(String(600))
    file4 = mapped_column(String(600))
    file5 = mapped_column(String(600))

    projects: Mapped['Projects'] = relationship('Projects', back_populates='tracking_results')
    tracking_steps: Mapped['TrackingSteps'] = relationship('TrackingSteps', back_populates='tracking_results')


class TrackingStorage(Base):
    __tablename__ = 'tracking_storage'
    __table_args__ = (
        ForeignKeyConstraint(['projects_id_projects'], ['projects.id_projects'], name='fk_tracking_storage_projects1'),
        ForeignKeyConstraint(['tracking_storage_field_id_tracking_storage_field'],
                             ['tracking_storage_field.id_tracking_storage_field'],
                             name='fk_tracking_storage_tracking_storage_field1'),
        ForeignKeyConstraint(['users_id'], ['users.id'], name='fk_tracking_storage_users1'),
        Index('fk_tracking_storage_projects1_idx', 'projects_id_projects'),
        Index('fk_tracking_storage_tracking_storage_field1_idx', 'tracking_storage_field_id_tracking_storage_field'),
        Index('fk_tracking_storage_users1_idx', 'users_id'),
        Index('key_UNIQUE', 'key', unique=True)
    )

    id_tracking_storage = mapped_column(Integer, primary_key=True)
    projects_id_projects = mapped_column(Integer, nullable=False)
    tracking_storage_field_id_tracking_storage_field = mapped_column(Integer, nullable=False)
    users_id = mapped_column(Integer, nullable=False)
    key = mapped_column(String(500))
    file_name = mapped_column(String(500))
    date_creation = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    projects: Mapped['Projects'] = relationship('Projects', back_populates='tracking_storage')
    tracking_storage_field: Mapped['TrackingStorageField'] = relationship('TrackingStorageField',
                                                                          back_populates='tracking_storage')
    users: Mapped['Users'] = relationship('Users', back_populates='tracking_storage')


class UserProject(Base):
    __tablename__ = 'user_project'
    __table_args__ = (
        ForeignKeyConstraint(['project_roles_id_project_roles'], ['project_roles.id_project_roles'], ondelete='CASCADE',
                             name='fk_user_project_project_roles1'),
        ForeignKeyConstraint(['projects_id_projects'], ['projects.id_projects'], ondelete='CASCADE',
                             onupdate='SET NULL', name='fk_user_project_projects1'),
        ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='SET NULL', onupdate='SET NULL',
                             name='fk_user_project_users1'),
        Index('fk_user_project_project_roles1_idx', 'project_roles_id_project_roles'),
        Index('fk_user_project_projects1_idx', 'projects_id_projects'),
        Index('fk_user_project_users1_idx', 'users_id')
    )

    id_user_project = mapped_column(Integer, primary_key=True)
    project_roles_id_project_roles = mapped_column(Integer, nullable=False)
    users_id = mapped_column(Integer)
    projects_id_projects = mapped_column(Integer)
    role_description = mapped_column(String(255))

    project_roles: Mapped['ProjectRoles'] = relationship('ProjectRoles', back_populates='user_project')
    projects: Mapped[Optional['Projects']] = relationship('Projects', back_populates='user_project')
    users: Mapped[Optional['Users']] = relationship('Users', back_populates='user_project')
    experts: Mapped[List['Experts']] = relationship('Experts', uselist=True, back_populates='user_project')


class Experts(Base):
    __tablename__ = 'experts'
    __table_args__ = (
        ForeignKeyConstraint(['expertises_id_expertises'], ['expertises.id_expertises'], ondelete='SET NULL',
                             name='fk_experts_expertises1'),
        ForeignKeyConstraint(['user_project_id_user_project'], ['user_project.id_user_project'], ondelete='SET NULL',
                             onupdate='SET NULL', name='fk_experts_user_project1'),
        Index('fk_experts_expertises1_idx', 'expertises_id_expertises'),
        Index('fk_experts_user_project1_idx', 'user_project_id_user_project')
    )

    id_experts = mapped_column(Integer, primary_key=True)
    expertises_id_expertises = mapped_column(Integer)
    user_project_id_user_project = mapped_column(Integer)

    expertises: Mapped[Optional['Expertises']] = relationship('Expertises', back_populates='experts')
    user_project: Mapped[Optional['UserProject']] = relationship('UserProject', back_populates='experts')
    expertise_information: Mapped[List['ExpertiseInformation']] = relationship('ExpertiseInformation', uselist=True,
                                                                               back_populates='experts')
    expertise_project_data: Mapped[List['ExpertiseProjectData']] = relationship('ExpertiseProjectData', uselist=True,
                                                                                back_populates='experts')
    project_pervich_evaluation: Mapped[List['ProjectPervichEvaluation']] = relationship('ProjectPervichEvaluation',
                                                                                        uselist=True,
                                                                                        back_populates='experts')


class SetsValuesTemplateCriteria(Base):
    __tablename__ = 'sets_values_template_criteria'
    __table_args__ = (
        ForeignKeyConstraint(['template_expertise_criteria_id_template_expertise_criteria'],
                             ['template_expertise_criteria.id_template_expertise_criteria'],
                             name='fk_sets_values_templates_criteria_template_expertise_criteria1'),
        Index('fk_sets_values_templates_criteria_template_expertise_criter_idx',
              'template_expertise_criteria_id_template_expertise_criteria')
    )

    id_sets_values_template_criteria = mapped_column(Integer, primary_key=True)
    template_expertise_criteria_id_template_expertise_criteria = mapped_column(Integer, nullable=False)
    value_field = mapped_column(String(255))

    template_expertise_criteria: Mapped['TemplateExpertiseCriteria'] = relationship('TemplateExpertiseCriteria',
                                                                                    back_populates='sets_values_template_criteria')


class TrackingCall(Base):
    __tablename__ = 'tracking_call'
    __table_args__ = (
        ForeignKeyConstraint(['tracking_information_id_tracking_information'],
                             ['tracking_information.id_tracking_information'], ondelete='CASCADE',
                             name='fk_tracking_call_tracking_information1'),
        ForeignKeyConstraint(['tracking_steps_id_tracking_steps'], ['tracking_steps.id_tracking_steps'],
                             ondelete='CASCADE', name='fk_tracking_call_tracking_steps1'),
        Index('fk_tracking_call_tracking_information1_idx', 'tracking_information_id_tracking_information'),
        Index('fk_tracking_call_tracking_steps1_idx', 'tracking_steps_id_tracking_steps')
    )

    id_tracking_call = mapped_column(Integer, primary_key=True)
    tracking_steps_id_tracking_steps = mapped_column(Integer, nullable=False)
    tracking_information_id_tracking_information = mapped_column(Integer, nullable=False)
    link = mapped_column(String(600))
    all_steps = mapped_column(TINYINT(1))

    tracking_information: Mapped['TrackingInformation'] = relationship('TrackingInformation',
                                                                       back_populates='tracking_call')
    tracking_steps: Mapped['TrackingSteps'] = relationship('TrackingSteps', back_populates='tracking_call')


class ExpertiseInformation(Base):
    __tablename__ = 'expertise_information'
    __table_args__ = (
        ForeignKeyConstraint(['expertises_id_expertises'], ['expertises.id_expertises'], ondelete='SET NULL',
                             name='fk_expertise_information_expertises1'),
        ForeignKeyConstraint(['experts_id_experts'], ['experts.id_experts'], ondelete='SET NULL',
                             name='fk_expertise_information_experts1'),
        ForeignKeyConstraint(['projects_id_projects'], ['projects.id_projects'], ondelete='SET NULL',
                             onupdate='SET NULL', name='fk_expertise_information_projects1'),
        Index('fk_expertise_information_expertises1_idx', 'expertises_id_expertises'),
        Index('fk_expertise_information_experts1_idx', 'experts_id_experts'),
        Index('fk_expertise_information_projects1_idx', 'projects_id_projects')
    )

    id_expertise_information = mapped_column(Integer, primary_key=True)
    signed_file = mapped_column(String(255))
    projects_id_projects = mapped_column(Integer)
    submitted = mapped_column(TINYINT(1))
    expertises_id_expertises = mapped_column(Integer)
    experts_id_experts = mapped_column(Integer)

    expertises: Mapped[Optional['Expertises']] = relationship('Expertises', back_populates='expertise_information')
    experts: Mapped[Optional['Experts']] = relationship('Experts', back_populates='expertise_information')
    projects: Mapped[Optional['Projects']] = relationship('Projects', back_populates='expertise_information')


class ExpertiseProjectData(Base):
    __tablename__ = 'expertise_project_data'
    __table_args__ = (
        ForeignKeyConstraint(['expertises_id_expertises'], ['expertises.id_expertises'], ondelete='SET NULL',
                             onupdate='SET NULL', name='fk_expertise_project_data_expertises1'),
        ForeignKeyConstraint(['experts_id_experts'], ['experts.id_experts'], ondelete='SET NULL', onupdate='SET NULL',
                             name='fk_expertise_project_data_experts1'),
        ForeignKeyConstraint(['projects_id_projects'], ['projects.id_projects'], ondelete='SET NULL',
                             onupdate='SET NULL', name='fk_project_data_projects100'),
        Index('fk_expertise_project_data_expertises1_idx', 'expertises_id_expertises'),
        Index('fk_expertise_project_data_experts1_idx', 'experts_id_experts'),
        Index('fk_project_data_projects1_idx', 'projects_id_projects')
    )

    id_expertise_project_data = mapped_column(Integer, primary_key=True)
    field_name = mapped_column(String(255), nullable=False)
    data = mapped_column(String(1000))
    projects_id_projects = mapped_column(Integer)
    visible = mapped_column(TINYINT)
    label = mapped_column(String(255))
    file = mapped_column(TINYINT)
    expertises_id_expertises = mapped_column(Integer)
    experts_id_experts = mapped_column(Integer)

    expertises: Mapped[Optional['Expertises']] = relationship('Expertises', back_populates='expertise_project_data')
    experts: Mapped[Optional['Experts']] = relationship('Experts', back_populates='expertise_project_data')
    projects: Mapped[Optional['Projects']] = relationship('Projects', back_populates='expertise_project_data')


class ProjectPervichEvaluation(Base):
    __tablename__ = 'project_pervich_evaluation'
    __table_args__ = (
        ForeignKeyConstraint(['experts_id_experts'], ['experts.id_experts'],
                             name='fk_project_pervich_evaluation_experts1'),
        ForeignKeyConstraint(['pervich_criteria_id_pervich_criteria'], ['pervich_criteria.id_pervich_criteria'],
                             name='fk_project_moder_evaluation_copy1_pervich_criteria1'),
        ForeignKeyConstraint(['projects_id_projects'], ['projects.id_projects'],
                             name='fk_project_moder_evaluation_projects100'),
        Index('fk_project_moder_evaluation_copy1_pervich_criteria1_idx', 'pervich_criteria_id_pervich_criteria'),
        Index('fk_project_moder_evaluation_projects1_idx', 'projects_id_projects'),
        Index('fk_project_pervich_evaluation_experts1_idx', 'experts_id_experts')
    )

    id_project_pervich_evaluation = mapped_column(Integer, primary_key=True)
    projects_id_projects = mapped_column(Integer, nullable=False)
    pervich_criteria_id_pervich_criteria = mapped_column(Integer, nullable=False)
    experts_id_experts = mapped_column(Integer)
    comment = mapped_column(Text)

    experts: Mapped[Optional['Experts']] = relationship('Experts', back_populates='project_pervich_evaluation')
    pervich_criteria: Mapped['PervichCriteria'] = relationship('PervichCriteria',
                                                               back_populates='project_pervich_evaluation')
    projects: Mapped['Projects'] = relationship('Projects', back_populates='project_pervich_evaluation')
