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

# def create_included_obj(url, type, obj, obj_name=None):
#   # obj_name = type if not obj_name:
#   obj_name = (obj_name if obj_name else type)
#   return {
#     "type": type,
#     "id": obj.id,
#     "attributes": {
#       "username": obj.username,
#     },
#     "links": {
#       "self": url + "/" + type +"/" + str(obj.id)
#     }
#   }