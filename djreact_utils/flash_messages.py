
class FlashMessage:
  
  def __init__(self, message, header=None, severity='primary'):
    self.message = message
    self.header = header
    self.severity = severity
    self.css_class = "alert-{}".format(severity)
    
class LitFlashMessage(FlashMessage):
  def __init__(self, message, header=None, severity='primary'):
    super(LitFlashMessage, self).__init__(message, header, severity)
    if self.severity == 'primary':
      self.css_class = 'bg-accent'
    elif self.severity == 'default':
      self.css_class = 'bg-accent'
    elif self.severity == 'danger':
      self.css_class = 'bg-error'
    else:
      self.css_class = "bg-{}".format(self.severity)