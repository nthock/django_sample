# Django Sample

Code to import export. Follow the https://django-import-export.readthedocs.io/en/latest/ to install the packages.

Then setup the below in your `app/admin.py`:

```python
class QuestionResource(resources.ModelResource):
  class Meta:
    model = Question
```

You can customise the fields to include / exclude from the export:

```python
class QuestionResource(resources.ModelResource):
  class Meta:
    model = Question
    exclude = ('pub_date', )
```

To export:

```python
import json

from polls.admin import QuestionResource

dataset = QuestionResource().export()

# Include in another dictionary
sample_dict = {}
sample_dict['question'] = json.loads(dataset.json)

print(sample_dict)
{'question': [{'id': 1,
   'question_text': "What's up?",
   'pub_date': '2020-03-09 07:29:43'},
  {'id': 2,
   'question_text': 'Another Question',
   'pub_date': '2020-03-25 08:55:13'}]}

   {'question': [{'id': 3,
   'question_text': "Question id 3",
   'pub_date': '2020-03-09 07:29:43'},
  {'id': 4,
   'question_text': 'Question id 4',
   'pub_date': '2020-03-25 08:55:13'}]}

# Convert to json
json.dumps(sample_dict)

# Output json to file
with open('data.json', 'w') as f:
  json.dump(sample_dict, f)
```

To import:

```python
import tablib
from import_export import resources
from polls.models import Question

question_resource = resources.modelresource_factory(model=Question)()

# json_data = <json>
json_data = json.dumps(sample_dict)

json.loads(json_data)

question_json_data = json.dumps(json.loads(json_data)["question"])

import_data = tablib.Dataset()
import_data.json = question_json_data


result = question_resource.import_data(import_data, dry_run=False)
```