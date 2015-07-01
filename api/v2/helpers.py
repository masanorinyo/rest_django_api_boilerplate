import types

def create_relationship_obj(url, obj, type, related_objs, obj_name=None):
  obj_name = (obj_name if obj_name else type)
  obj_data = 'test'

  if not hasattr(related_objs, 'id'):
    obj_data = []
    for related_obj in related_objs:
      obj_data.append({"id": related_obj.id, "type": type})
  else:  
    obj_data = {"id":related_objs.id, "type":type}

  return {
    obj_name: {
      "links" :{
        "self" : url + "/relationships/" + obj_name,
        "related" : url + "/" + obj_name
      },
      "data" : obj_data
    }
  }
