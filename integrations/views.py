from django.shortcuts import render
from django.http import *
from integrations.models import user_code_queue
from tempfile import NamedTemporaryFile
import errno
import os
#extracts the code from a url
def obtain_url_code(url):
    print(f"code request {url}")
    try:
        index = url.index("code=") #throws ValueError if index not found
        amp_separator = url.find("&", index) #sometimes codes re delimited by '&'
        code = ""
        if (amp_separator != -1):
            code = url[index+5:amp_separator]
        else:
            code = url[index+5:len(url)-3]
        return code
    except Exception as e:
        print(f"could not find code in string {str(url)}")
        return -1
    
def redirect(request): #used to extrapolate code info from redirect uris
    try: 
        url = str(request.build_absolute_uri)
        code = obtain_url_code(url)
        if(code is -1):
            msg = "Code not set as it was not found in redirect. Url probably malformed..."
            print(msg)
            return(msg)
        if os.path.exists("code.txt"):
            os.remove("code.txt") 
        write_code_to_file = open("code.txt","w")
        write_code_to_file.write(code)
        write_code_to_file.close()
    except Exception as e:
        pass
    finally:
        return HttpResponse("<h1>Redirect page<h1>")

def index(request):
    userinfo = {'current_user': 'bingo',
                'top_tracks': 'Some Music',
                'top_artists': 'Celine Dion'}
    return render(request, 'integrations/index.html', {'userinfo':userinfo})