python manage.py dumpdata --indent 4 --format json \
	sites.Site \
	auth.User \
	articles.Article > initial_data.json