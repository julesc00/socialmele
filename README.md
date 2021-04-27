Social Site from Melé book

1. Declare app in settings.py atop so its custom authentication templates get loaded first.

2. In order for proper resetting password redirects, I had to declare a success_url in the urls path.
