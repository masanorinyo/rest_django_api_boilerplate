import types

def create_data(obj, type):
  if not hasattr(obj, 'id'):
    obj_data = []
    for related_obj in obj:
      obj_data.append({"id": related_obj.id, "type": type})
  else:  
    obj_data = {"id":obj.id, "type":type}

  return obj_data


def create_relationship_obj(url, obj, type, data):

  return {
    type: {
      "links" :{
        "self" : url + "/relationships/" + type,
        "related" : url + "/" + type
      },
      "data" : data
    }
  }
