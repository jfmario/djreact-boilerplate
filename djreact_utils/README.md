
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

### Classes #

#### Flash Messages #

`djreact_utils.flash_messages.FlashMessage`

A generic class for flash messages. The way to create a FlashMessage
(as well as the subclass LitFlashMessage) is this:

```python
fm = FlashMessage("This is a message", header="Cool!", severity="success")
# print(fm.css_class)
```

Possible values for severity are:

* `default`
* `primary` (the default)
* `info`
* `success`
* `warning`
* `danger`

In addition to having the members `message`, `header`, and `severity`, the 
object will also have the member `css_class`, which will be `alert-primary` or 
whatever the alert is. 


`djreact_utils.flash_messages.LitFlashMessage`

A class for flash messages compatible with lit.css, as it automatically 
changes the value of `css_class` to be compatible (ie, 
`alert-primary` becomes `bg-accent`)

**Using Flash Messages**

The template `djreact_utils/templates/djreact/lit/flash_message.html` is 
designed to work with `LitFlashMessage`. If you pass as part of the template 
data a list called "flash_messages" (which should be a list of LitFlashMessage
objects), they will be properly rendered if you include the template:

```html
<div>
  {% include 'djreact/lit/flash_messages.html' %}
</div>
```

## Acknowledgements #

### Authors #

* John F Marion

### Built With #

* Django
