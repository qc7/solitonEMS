from django.urls import reverse, resolve


def check_response_200_ok(self, response, template_path):
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, template_path)


def check_response_redirects(response, self):
    self.assertEquals(response.status_code, 302)
    self.assertTemplateNotUsed(response)


def check_template_and_status_code(self, view_name, template_path, args=None):
    response = self.client.get(reverse(view_name, args=args))
    check_response_200_ok(response, self, template_path)


def check_process_view_get(self, view_name: object, args: object = None) -> object:
    response = self.client.get(reverse(view_name, args=args))
    check_response_redirects(response, self)


def check_process_view_post(self, view_name, payload=None):
    response = self.client.post(reverse(view_name), payload)
    check_response_redirects(response, self)


def check_page_url_is_resolved(self, url_name, view_function_name, args=None):
    url = reverse(url_name, args=args)
    self.assertEquals(resolve(url).func, view_function_name)
