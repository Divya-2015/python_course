camera = 1 
microphone = 4 
storage = 4
location = 8 

approved_apps = ["coding app", "math app", "reading app", "science app"]

student_name = input("enter your name: ")
requested_app = input("enter the app you want to access: ").lower()

print("\n--- identity operator check---")

if type(student_name)is str:
    print("the student name is stored as text")

if type(requested_app)is not int: print("the requested app is not stored asa number")

print("\n---membership operation check---")

if requested_app in approved_apps:
    print(requested_app, "is an approved student app")
else:
    print(requested_app, "is not an approved student app")

restricted_apps = ["gaming app", "shopping app", "social media app"]

if requested_app not in restricted_apps:
    print("the app is not in the restricted list")
else:
    print("access denied because the app is restricted")

print("\n---app permisions settings---")

student_permisions = camera | microphone | storage

print("permission value:", student_permisions)
print("permission bits:", bin(student_permisions))

if student_permisions & camera:
    print("camera permissions: enabled")

if student_permisions & microphone:
    print("microphone permission: enabled")

if student_permisions & storage:
    print("storage permission: enabled")

if student_permisions & location:
    print("location permission: enabled")
else:
    print("location permission: disabled")

print("\n---bit shift demonstration---")

next_permission = camera << 1

print("camera bit:", bin(camera))
print("after left shift:", bin(next_permission))

previous_permission = storage >> 1

print("storage bit:", bin(storage))
print("after right shift:", bin(previous_permission))

print("\n---final access result---")

if requested_app in approved_apps and requested_app not in restricted_apps:
    print("access granted to", requested_app) 
else:
    print("access denied to", requested_app)