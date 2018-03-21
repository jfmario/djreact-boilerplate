
# Django-React Utils #

This is a Django app included in the Djreact boilerplate.

## Docs #

### Management Commands #

**Create Test Users**

`python3 manage.py create_test_users`

This creates 6 test user accounts with the following info:

| Username | Password |
| --- | --- |
| applejack | orange |
| pinkiePie | pink |
| rarity | white |
| twilightSparkle | purple |
| rainbowDash | blue |
| fluttershy | yellow |

### Custom Model Fields #

**JSON Field**

`djreact_utils.fields.JsonField`

This is a model field that can be used in your models. It subclasses the 
normal TextField but automatically serializes and deserializes JSON.

Example:

```python
class MyModel(models.Model):
  json_info = JsonField()
```

### Models #

**Abstract Singleton Model**

`djreact_utils.models.SingletonModel`

This is a model that you can subclass in order to create a model that will 
only ever have one instance. This is useful for creating custom 
app settings objects.

## Acknowledgements #

### Authors #

* John F Marion

### Built With #

* Django
