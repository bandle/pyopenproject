from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.role.role_command import RoleCommand
from openproject.model.role import Role


class Find(RoleCommand):

    def __init__(self, connection, role):
        super().__init__(connection)
        self.role = role

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.role.id}").execute()
            return Role(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding role by id: {self.role.id}") from re