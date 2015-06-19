def get_api_version(url):
  if "application/vdn.bespoke" in url:
    try: 
      return "v"+url.split('+')[0].split('v')[2]
    except IndexError: 
      return False
  else:
    return False