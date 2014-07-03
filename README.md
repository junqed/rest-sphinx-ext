rest-sphinx-ext
===============

Add the docs to a view function of your web-framework.
Example of the documentation:

views.py::

	def get_user():
		"""
		GET /users/:user_id/
		-----------
		Get users from the database.

		Parameters
		==========
		**user_id** : int
			A user ID.

		"""
		pass


and in the endpoints.rst file::

	.. autorestmethod:: your_main_package.api.views.get_user