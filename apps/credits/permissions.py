from rest_framework import permissions

class ApiUserPermission(permissions.BasePermission):
	message = 'Your user is not allowed'#mensaje que lanza si el permiso no se cumple
	SELECTED_GROUP = 'api_user' # grupo de acceso a este permiso

	def has_permission(self,request,view):
		if request.user.groups.filter(name=self.SELECTED_GROUP) and request.method == 'GET':# obtiene el grupo de acceso del usuario que realizo la peticion  y verifica que el metodo sea GET 
			return True # pasa el permiso y tiene acesso a la informacion que  solicito
		return False
