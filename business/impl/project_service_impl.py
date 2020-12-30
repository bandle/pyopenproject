from business.impl.command.project.create import Create
from business.impl.command.project.create_form import CreateForm
from business.impl.command.project.delete import Delete
from business.impl.command.project.find import Find
from business.impl.command.project.find_all import FindAll
from business.impl.command.project.find_parents import FindParents
from business.impl.command.project.find_types import FindTypes
from business.impl.command.project.update import Update
from business.impl.command.project.update_form import UpdateForm
from business.impl.command.project.find_schema import FindSchema
from business.impl.command.project.find_versions import FindVersions
from business.impl.command.project.find_budgets import FindBudgets
from business.project_service import ProjectService


class ProjectServiceImpl(ProjectService):

    def find(self, project):
        return Find(project).execute()

    def update(self, project):
        return Update(project).execute()

    def delete(self, project):
        return Delete(project).execute()

    def find_all(self):
        return FindAll().execute()

    def create(self, project):
        return Create(project).execute()

    def find_schema(self):
        return FindSchema().execute()

    def create_form(self, form):
        return CreateForm(form).execute()

    def update_form(self, project, form):
        return UpdateForm(project, form).execute()

    def find_parents(self, filters, of, sortBy):
        return FindParents(filters, of, sortBy).execute()

    def find_versions(self, project):
        return FindVersions(project).execute()

    def find_types(self, project):
        return FindTypes(project).execute()

    def find_budgets(self, project):
        return FindBudgets(project).execute()