def get_api_version(url):
  if "application/vdn.bespoke" in url:
    try: 
      return url.split('.')[2].split('+')[0];
    except IndexError: 
      return False
  else:
    return False