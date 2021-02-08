def validateName(name):
    if len(name)>0 and len(name)<=100:
        return True
    return False

def validateDuration(duration):
    if duration<=0:
        return False
    return True

def validateParticipants(arr):
    x = len(arr)
    if x==0:
        return True
    count=0
    if x<=10:
        for names in arr:
            if len(names)<=100:
                count=count+1
        if count==x:
            return True
    return False

def validatePodcast(type, host):
    if type=="podcast" and len(host)<=0:
        return False
    if type=="podcast" and len(host)>100:
        return False
    return True
        
def validateAudioBook(type, author, narrator):
    if type!="audiobook":
        return True
    if type=="audiobook":
        if len(author)<=100 and len(author)>0:
            if len(narrator)<=100 and len(narrator)>0:
                return True
    return False