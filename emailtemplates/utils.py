
def send_email_template(slug, to_address, context={}, attachments=None, headers=None):
    from emailtemplates.models import EmailTemplate
    email_template = EmailTemplate.objects.get(slug=slug)
    return email_template.send(to_address, context, attachments, headers)
