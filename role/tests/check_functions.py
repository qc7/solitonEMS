from django.urls import reverse


def check_template_and_status_code(self,view_name, template_path, args=None):
    response = self.client.get(reverse(view_name, args=args))
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, template_path)


def check_process_view_get(self,view_name: object, args: object = None) -> object:
    response = self.client.get(reverse(view_name, args=args))
    self.assertEquals(response.status_code, 302)
    self.assertTemplateNotUsed(response)