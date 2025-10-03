from pyscript import display, document

def submit_contact(event=None):
    name = document.getElementById('name').value.strip()
    email = document.getElementById('email').value.strip()
    message = document.getElementById('message').value.strip()

    if not name or not email or not message:
        display('Please complete all fields.', target='contact-response')
        return

    if '@' not in email or '.' not in email:
        display('Please enter a valid email address.', target='contact-response')
        return

    # Simple success message — in a real site you'd send this to a server
    display(f"Thanks {name}! Your message has been received.\nWe will reply to {email} soon.", target='contact-response')

    # clear form
    document.getElementById('name').value = ''
    document.getElementById('email').value = ''
    document.getElementById('message').value = ''
