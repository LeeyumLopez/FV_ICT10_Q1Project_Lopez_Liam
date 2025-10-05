from pyscript import display, document

# Contact page form handler
# This function is bound to the Send button via `py-click="submit_contact"` in
# the page's HTML. It performs simple client-side validation and then shows a
# confirmation message. For a production site you'd POST this data to a server
# endpoint instead of just displaying a message.
def submit_contact(event=None):
    # Read values from the form fields (trim whitespace)
    name = document.getElementById('name').value.strip()
    email = document.getElementById('email').value.strip()
    message = document.getElementById('message').value.strip()

    # Basic required-field check
    if not name or not email or not message:
        display('Please complete all fields.', target='contact-response')
        return

    # Very simple email sanity check. This is intentionally lightweight and
    # should be replaced with a proper regex or server-side validation if used
    # in production.
    if '@' not in email or '.' not in email:
        display('Please enter a valid email address.', target='contact-response')
        return

    # Success: show a confirmation message (multiline). The page's CSS uses
    # `white-space: pre-wrap` so the '\n' newlines appear as line breaks.
    display(f"Thanks {name}! Your message has been received.\nWe will reply to {email} soon.", target='contact-response')

    # Clear the form inputs to give visual feedback that the message was sent
    document.getElementById('name').value = ''
    document.getElementById('email').value = ''
    document.getElementById('message').value = ''

