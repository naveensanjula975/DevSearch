
Terminal Commands


```python manage.py shell```

```
from projects.models import Project

projects = Project.objects.all()

print(projects)

projectObj = Project.objects.get(title="Portfolio Website")

print(projectObj)

print(projectObj.title)

print(projectObj.created)

projects = Project.objects.filter(title__startswith="po")

print(projects)

projects = Project.objects.filter(vote_ratio__gte=50)

print(projects)

projects = Project.objects.filter(vote_ratio__lte=50)

print(projects)

project = Project.objects.get(title="Ecommerce Website")

print(project)

print(project.review_set.all())
```
