def create_relationship_obj(url, obj, type, related_obj, obj_name=None):
  obj_name = (obj_name if obj_name else type)
  return {
    obj_name: {
      "links" :{
        "self" : url + "/relationships/" + obj_name,
        "related" : url + "/" + obj_name
      },
      "data" : {
        "type" : type,
        "id" : related_obj.id,
      }
    }
  }
