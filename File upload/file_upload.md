# File upload
We can upload jpg extension in file upload page:

tmp/image.jpg succesfully uploaded.


A great way to exploit such feature would be to upload malicious file containing malicious code. If we can for example
upload a reverse shell in a php file, we could get a remote access to the machine. But .jpg is the only extension working.
This project doesnt require us to actually exploit the machine, so lets just put 'bash' inside our image.

## The Vuln

echo 'bash' > image.jpg

Upload the image and observe network tab. Our request worked, but since its a .jpg, we will not be able to execute it with a request.
Click edit on the request and resend. Now you can change extension from .jpg to .php in the body. The mistake they made is that the extension is only verified front side.