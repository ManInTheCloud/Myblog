from django import template
import datetime

register=template.Library()

@register.tag(name="current_time")
def do_current_time(parser,token):
    #token是正在被解析的语句
    try:
        #split_contents() knows not to split quoted strings
        tag_name,format_string=token.split_contents()
    except ValueError:
        msg="%r tag requires a single argument"%token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode(format_string[1:-1])

class CurrentTimeNode(template.Node):
    def __init__(self,format_string):
        self.format_string=str(format_string)

    def render(self, context):
        now=datetime.datetime.now()
        return now.strftime(self.format_string)

class CurrentTimeNode2(template.Node):
    def __init__(self,format_string):
        self.format_string=str(format_string)

    def render(self,context):
        now=datetime.datetime.now()
        context['current_time']=now.strftime(self.format_string)
        return ''

#######################################################################3
def current_time(format_string):
    try:
        return datetime.datetime.now().strftime(str(format_string))
    except UnicodeDecodeError:
        return ''

register.simple_tag(current_time)

