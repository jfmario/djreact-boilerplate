
import json

from django.db import models

def json_to_python(s):
  return json.loads(s)

class JsonField(models.TextField):

  description = "Json representation of a Python list or dictionary."

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  def from_db_value(self, value, expression, connection):
    if value is None:
      return None
    else:
      return json_to_python(value)

  def to_python(self, value):
    if isinstance(value, list):
      return value
    if isinstance(value, dict):
      return value
    if value is None:
      return None
    return json_to_python(value)

  def get_prep_value(self, value):
    return json.dumps(value)
