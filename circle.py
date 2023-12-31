import fcl
import numpy as np

# library: https://github.com/BerkeleyAutomation/python-fcl

geom1 = fcl.Sphere(1)  #半径を入れる
obj1 = fcl.CollisionObject(geom1)

geom2 = fcl.Sphere(1) 
obj2 = fcl.CollisionObject(geom2, fcl.Transform(np.array([1.5, 0.0, 0.0])))

geom3 = fcl.Sphere(1) 
obj3 = fcl.CollisionObject(geom3, fcl.Transform(np.array([6.0, 0.0, 0.0])))

geoms = [geom1, geom2, geom3]
objs = [obj1, obj2, obj3]
names = ['obj1', 'obj2', 'obj3']

# Create map from geometry IDs to objects
geom_id_to_obj = { id(geom) : obj for geom, obj in zip(geoms, objs) }

# Create map from geometry IDs to string names
geom_id_to_name = { id(geom) : name for geom, name in zip(geoms, names) }

# Create manager
manager = fcl.DynamicAABBTreeCollisionManager()
manager.registerObjects(objs)
manager.setup()

# Create collision request structure
crequest = fcl.CollisionRequest(num_max_contacts=100, enable_contact=True)
cdata = fcl.CollisionData(crequest, fcl.CollisionResult())

# Run collision request
manager.collide(cdata, fcl.defaultCollisionCallback)

# Extract collision data from contacts and use that to infer set of
# objects that are in collision
objs_in_collision = set()

print("cdata")
print(cdata.result.contacts)
for contact in cdata.result.contacts:
    # Extract collision geometries that are in contact
    coll_geom_0 = contact.o1
    coll_geom_1 = contact.o2

    # Get their names
    coll_names = [geom_id_to_name[id(coll_geom_0)], geom_id_to_name[id(coll_geom_1)]]
    coll_names = tuple(sorted(coll_names))
    objs_in_collision.add(coll_names)

for coll_pair in objs_in_collision:
    print('Object {} in collision with object {}!'.format(coll_pair[0], coll_pair[1]))
